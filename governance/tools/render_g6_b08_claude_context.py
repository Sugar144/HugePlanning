"""Render non-persistent Claude Code context from the reusable core binding."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:  # Supports both direct tool execution and repository test imports.
    from _lib.strict_yaml import load
    from render_g6_b08_codex_context import ROOT, nested_value, resolve_relative
except ModuleNotFoundError:  # pragma: no cover - selected by import context.
    from governance.tools._lib.strict_yaml import load
    from governance.tools.render_g6_b08_codex_context import (
        ROOT,
        nested_value,
        resolve_relative,
    )


def build_context(l7_projection: Path | None = None) -> dict[str, object]:
    """Resolve the common core with the Claude L4 binding, without new semantics."""
    import hashlib
    import re

    binding_path = ROOT / "governance/adapters/claude/binding.yaml"
    binding = load(binding_path)
    if not isinstance(binding, dict) or binding.get("provider_executor") != "Claude Code":
        raise ValueError("binding is not a Claude Code adapter")
    core_path = resolve_relative(binding_path, binding.get("core_contract"))
    adopter_path = resolve_relative(binding_path, binding.get("adopter_binding"))
    config_path = resolve_relative(binding_path, binding.get("project_configuration"))
    core = core_path.read_text(encoding="utf-8")
    configuration_document = load(config_path)
    if not isinstance(configuration_document, dict) or not isinstance(configuration_document.get("configuration"), dict):
        raise TypeError("project configuration is missing")
    resolved = core
    for key in sorted(set(re.findall(r"\{\{([^{}]+)\}\}", core))):
        value = nested_value({"configuration": configuration_document["configuration"]}, key)
        if not isinstance(value, str):
            raise TypeError(f"configured core value is not a string: {key}")
        resolved = resolved.replace("{{" + key + "}}", value)
    context: dict[str, object] = {
        "document_id": "GOV-GEN-G6-CLAUDE-CODE-CONTEXT-001",
        "adapter": binding["document_id"],
        "provider_executor": binding["provider_executor"],
        "core_contract": binding["core_contract"],
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


def render(context: dict[str, object]) -> str:
    result = "# Ephemeral governance context for Claude Code\n\n"
    result += f"Adapter: `{context['adapter']}`\n\n"
    result += "## Resolved reusable core\n\n" + str(context["resolved_core_contract"]).rstrip() + "\n"
    if "l7_projection" in context:
        result += "\n## Bounded L7 projection\n\n```json\n"
        result += json.dumps(context["l7_projection"], sort_keys=True, indent=2) + "\n```\n"
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="directory for ephemeral Claude context")
    parser.add_argument("--l7-projection", type=Path)
    args = parser.parse_args()
    context = build_context(args.l7_projection)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    (output / "claude-context.md").write_text(render(context), encoding="utf-8")
    print(json.dumps({"adapter": context["adapter"], "resolved_core_sha256": context["resolved_core_sha256"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
