#!/usr/bin/env python3
"""Render a non-persistent Codex context from the reusable core binding."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

try:  # Supports both direct tool execution and repository test imports.
    from _lib.strict_yaml import StrictYAMLError, load
except ModuleNotFoundError:  # pragma: no cover - selected by import context.
    from governance.tools._lib.strict_yaml import StrictYAMLError, load


ROOT = Path(__file__).resolve().parents[2]
BINDING = ROOT / "governance/adapters/codex/binding.yaml"


def nested_value(mapping: dict[str, Any], dotted_key: str) -> Any:
    value: Any = mapping
    for segment in dotted_key.split("."):
        if not isinstance(value, dict) or segment not in value:
            raise ValueError(f"missing configured value: {dotted_key}")
        value = value[segment]
    return value


def resolve_relative(binding_path: Path, value: object) -> Path:
    if not isinstance(value, str):
        raise ValueError("adapter binding path is not a string")
    path = (binding_path.parent / value).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ValueError("adapter binding path escapes repository") from exc
    if not path.is_file():
        raise ValueError(f"adapter binding target is missing: {value}")
    return path


def build_context(l7_projection: Path | None = None) -> dict[str, Any]:
    try:
        binding = load(BINDING)
    except StrictYAMLError as exc:
        raise ValueError(f"invalid Codex adapter binding: {exc}") from exc
    if not isinstance(binding, dict) or binding.get("provider_executor") != "OpenAI Codex":
        raise ValueError("binding is not an OpenAI Codex adapter")
    core_path = resolve_relative(BINDING, binding.get("core_contract"))
    adopter_path = resolve_relative(BINDING, binding.get("adopter_binding"))
    config_path = resolve_relative(BINDING, binding.get("project_configuration"))
    core = core_path.read_text(encoding="utf-8")
    adopter = load(adopter_path)
    configuration_document = load(config_path)
    if not isinstance(adopter, dict) or not isinstance(configuration_document, dict):
        raise ValueError("adapter inputs must be mappings")
    configuration = configuration_document.get("configuration")
    if not isinstance(configuration, dict):
        raise ValueError("project configuration is missing")
    resolved = core
    for key in sorted(set(re.findall(r"\{\{([^{}]+)\}\}", core))):
        value = nested_value({"configuration": configuration}, key)
        if not isinstance(value, str):
            raise ValueError(f"configured core value is not a string: {key}")
        resolved = resolved.replace("{{" + key + "}}", value)
    context: dict[str, Any] = {
        "document_id": "GOV-GEN-G6-CODEX-CONTEXT-001",
        "adapter": binding["document_id"],
        "provider_executor": binding["provider_executor"],
        "core_contract": str(core_path.relative_to(ROOT)),
        "core_sha256": hashlib.sha256(core.encode()).hexdigest(),
        "resolved_core_sha256": hashlib.sha256(resolved.encode()).hexdigest(),
        "resolved_core_contract": resolved,
        "adopter_binding": str(adopter_path.relative_to(ROOT)),
        "configuration": str(config_path.relative_to(ROOT)),
        "canonical_history": binding["ownership"]["canonical_history"],
        "instruction_surface": binding["execution_surface"],
    }
    if l7_projection is not None:
        projection = json.loads(l7_projection.read_text(encoding="utf-8"))
        measurement = projection.get("token_measurement") if isinstance(projection, dict) else None
        if not isinstance(measurement, dict) or measurement.get("count", 0) > measurement.get("limit", -1):
            raise ValueError("L7 projection has no valid bounded token measurement")
        context["l7_projection"] = projection
    return context


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="directory for ephemeral Codex context")
    parser.add_argument("--l7-projection", type=Path)
    args = parser.parse_args()
    context = build_context(args.l7_projection)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    (output / "codex-context.json").write_text(json.dumps(context, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({"adapter": context["adapter"], "resolved_core_sha256": context["resolved_core_sha256"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
