#!/usr/bin/env python3
"""Request a new namespaced identity from the configured project allocator."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import yaml


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", help="Configured identity kind, for example FAIL")
    parser.add_argument("--purpose", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(root))
    from governance.framework_runtime import l6_module
    identity = l6_module("identity")
    Allocator, IdentityError = identity.Allocator, identity.IdentityError

    config = yaml.safe_load((root / "governance/adopters/hugeplanning/configuration.yaml").read_text(encoding="utf-8"))
    allocation = config["configuration"]["identity_allocator"]
    allocator = Allocator(
        namespace=allocation["namespace"],
        state_path=root / allocation["state_path"],
        ledger_path=root / allocation["ledger_path"],
    )
    try:
        result = allocator.peek(args.kind) if args.dry_run else allocator.allocate(args.kind, purpose=args.purpose)
    except IdentityError as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print(result.identity)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
