#!/usr/bin/env python3
"""Copy-safe placeholder substitution for the S0a client template."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Replace {{KEY}} placeholders in UTF-8 template files.")
    parser.add_argument("root", type=Path)
    parser.add_argument("--replace", nargs=2, action="append", default=[], metavar=("KEY", "VALUE"))
    args = parser.parse_args()
    replacements = dict(args.replace)

    for path in sorted(args.root.rglob("*")):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for key, value in replacements.items():
            text = text.replace("{{" + key + "}}", value)
        remaining = sorted(set(re.findall(r"\{\{([A-Z0-9_]+)\}\}", text)))
        if remaining:
            raise SystemExit(f"unresolved placeholders in {path}: {', '.join(remaining)}")
        path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
