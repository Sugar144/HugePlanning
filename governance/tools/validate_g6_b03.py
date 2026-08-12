#!/usr/bin/env python3
"""Deterministically validate G6 B-03's explicit adopter configuration seam."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FROZEN_REVISION = "6fc4fa1a14a665fabfcceb00729222527cd192ba"
CORE = ROOT / "governance/core/project-operating-contract.md"
SCHEMA = ROOT / "governance/core/configuration-schema.yaml"
CONFIG = ROOT / "governance/adopters/hugeplanning/configuration.yaml"
BINDING = ROOT / "governance/adopters/hugeplanning/core-binding.yaml"
COMPATIBILITY = ROOT / "governance/methodology/project-operating-contract.md"
INSTRUCTIONS = ("AGENTS.md", "governance/AGENTS.md", "CLAUDE.md")

VALUES = {
    "configuration.correction_example.base_run_id": "KGR-006",
    "configuration.correction_example.first_correction_id": "KGR-006-R1",
    "configuration.paths.formal_run_prompt_snapshots": "governance/runs/<run>/prompt/",
    "configuration.paths.learning_readme": "../learning/README.md",
}


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, text=True, stdout=subprocess.PIPE).stdout


def main() -> int:
    errors: list[str] = []
    core = CORE.read_text(encoding="utf-8")
    placeholders = set(re.findall(r"\{\{([^{}]+)\}\}", core))
    if placeholders != set(VALUES):
        errors.append("core placeholders do not exactly match the B-03 contract")
    resolved = core
    for placeholder, value in VALUES.items():
        resolved = resolved.replace("{{" + placeholder + "}}", value)
        if placeholder not in SCHEMA.read_text(encoding="utf-8"):
            errors.append(f"schema omits {placeholder}")
        if value not in CONFIG.read_text(encoding="utf-8"):
            errors.append(f"project configuration omits value for {placeholder}")
    frozen = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{FROZEN_REVISION}:governance/methodology/project-operating-contract.md"],
        check=True, text=True, stdout=subprocess.PIPE,
    ).stdout
    if resolved != frozen:
        errors.append("resolved HugePlanning contract is not byte-equivalent to the B-01 baseline")
    if "HugePlanning" in core or "KGR-006" in core or "governance/runs/" in core:
        errors.append("reusable core retains a hardcoded project value")
    binding = BINDING.read_text(encoding="utf-8")
    if "configuration_contract: ../../core/configuration-schema.yaml" not in binding or "project_configuration: configuration.yaml" not in binding:
        errors.append("adopter binding does not own the explicit configuration")
    compatibility = COMPATIBILITY.read_text(encoding="utf-8")
    if "core_contract: ../core/project-operating-contract.md" not in compatibility or "adopter_binding: ../adopters/hugeplanning/core-binding.yaml" not in compatibility:
        errors.append("existing compatibility entrypoint does not resolve the configured core")
    if git("diff", "--name-only", "8889161", "--", *INSTRUCTIONS).strip():
        errors.append("an active instruction surface changed during B-02/B-03")
    if errors:
        print("FAIL: " + "; ".join(errors), file=sys.stderr)
        return 1
    print("PASS: explicit configuration resolves byte-identical HugePlanning semantics")
    print("PASS: reusable core has no hardcoded HugePlanning path or run value")
    print("PASS: project-owned configuration and compatibility binding are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
