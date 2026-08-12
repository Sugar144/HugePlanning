#!/usr/bin/env python3
"""Deterministically validate G6 B-03's explicit adopter configuration seam."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

from _lib.strict_yaml import StrictYAMLError, load


ROOT = Path(__file__).resolve().parents[2]
FROZEN_REVISION = "6fc4fa1a14a665fabfcceb00729222527cd192ba"
CORE = ROOT / "governance/core/project-operating-contract.md"
SCHEMA = ROOT / "governance/core/configuration-schema.yaml"
CONFIG = ROOT / "governance/adopters/hugeplanning/configuration.yaml"
BINDING = ROOT / "governance/adopters/hugeplanning/core-binding.yaml"
COMPATIBILITY = ROOT / "governance/methodology/project-operating-contract.md"
INSTRUCTIONS = ("AGENTS.md", "governance/AGENTS.md", "CLAUDE.md")

def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, text=True, stdout=subprocess.PIPE).stdout


def nested_value(mapping: dict, dotted_key: str) -> object:
    value: object = mapping
    for segment in dotted_key.split("."):
        if not isinstance(value, dict) or segment not in value:
            raise KeyError(dotted_key)
        value = value[segment]
    return value


def main() -> int:
    errors: list[str] = []
    try:
        schema = load(SCHEMA)
        config_document = load(CONFIG)
    except StrictYAMLError as exc:
        errors.append(f"configuration artifact is not strict YAML: {exc}")
        schema = {}
        config_document = {}
    if not isinstance(schema, dict) or not isinstance(config_document, dict):
        errors.append("configuration artifacts must be mappings")
        schema = {}
        config_document = {}
    required_keys = schema.get("required_configuration_keys", [])
    configuration = config_document.get("configuration")
    if not isinstance(required_keys, list) or not all(isinstance(key, str) for key in required_keys):
        errors.append("configuration schema has no deterministic required-key list")
        required_keys = []
    if not isinstance(configuration, dict):
        errors.append("project configuration has no configuration mapping")
        configuration = {}
    core = CORE.read_text(encoding="utf-8")
    placeholders = set(re.findall(r"\{\{([^{}]+)\}\}", core))
    if placeholders != set(required_keys):
        errors.append("core placeholders do not exactly match the B-03 contract")
    resolved = core
    for placeholder in required_keys:
        try:
            value = nested_value({"configuration": configuration}, placeholder)
        except KeyError:
            errors.append(f"project configuration omits value for {placeholder}")
            continue
        if not isinstance(value, str):
            errors.append(f"project configuration value for {placeholder} must be a string")
            continue
        resolved = resolved.replace("{{" + placeholder + "}}", value)
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
