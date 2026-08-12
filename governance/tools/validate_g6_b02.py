#!/usr/bin/env python3
"""Deterministically validate the G6 B-02 core and adopter boundary."""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FROZEN_REVISION = "6fc4fa1a14a665fabfcceb00729222527cd192ba"
CORE = ROOT / "governance/core/project-operating-contract.md"
BINDING = ROOT / "governance/methodology/project-operating-contract.md"
ADOPTER = ROOT / "governance/adopters/hugeplanning/core-binding.yaml"
INSTRUCTIONS = ("AGENTS.md", "governance/AGENTS.md", "CLAUDE.md")


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, text=True, stdout=subprocess.PIPE).stdout


def main() -> int:
    errors: list[str] = []
    frozen = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{FROZEN_REVISION}:governance/methodology/project-operating-contract.md"],
        check=True, stdout=subprocess.PIPE,
    ).stdout
    if CORE.read_bytes() != frozen:
        errors.append("core contract differs from the B-01 frozen source")
    binding = BINDING.read_text(encoding="utf-8")
    if "core_contract: ../core/project-operating-contract.md" not in binding:
        errors.append("compatibility binding does not resolve the core contract")
    adopter = ADOPTER.read_text(encoding="utf-8")
    if "core_contract: ../../core/project-operating-contract.md" not in adopter:
        errors.append("adopter binding does not resolve the core contract")
    core_text = CORE.read_text(encoding="utf-8")
    if "HugePlanning" in core_text:
        errors.append("core contains a HugePlanning literal")
    if git("diff", "--name-only", "8889161", "--", *INSTRUCTIONS).strip():
        errors.append("an active instruction surface changed during B-02")
    tracked = git("ls-files", "governance/core", "governance/adopters/hugeplanning").splitlines()
    if sorted(tracked) != sorted([
        "governance/adopters/hugeplanning/core-binding.yaml",
        "governance/core/README.md",
        "governance/core/project-operating-contract.md",
    ]):
        errors.append("unexpected B-02 core/adopter tracked surface")
    if errors:
        print("FAIL: " + "; ".join(errors), file=sys.stderr)
        return 1
    print("PASS: semantic equivalence, literal/path isolation, adopter binding, and provenance boundary")
    print("core_sha256=" + hashlib.sha256(frozen).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
