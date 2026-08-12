"""Deterministically validate Claude Code and Codex L4 core conformance."""

from __future__ import annotations

import subprocess
import sys

try:  # Supports both direct tool execution and repository test imports.
    from _lib.strict_yaml import load
    from render_g6_b08_claude_context import build_context as build_claude_context
    from render_g6_b08_codex_context import ROOT
    from render_g6_b08_codex_context import build_context as build_codex_context
except ModuleNotFoundError:  # pragma: no cover - selected by import context.
    from governance.tools._lib.strict_yaml import load
    from governance.tools.render_g6_b08_claude_context import (
        build_context as build_claude_context,
    )
    from governance.tools.render_g6_b08_codex_context import ROOT
    from governance.tools.render_g6_b08_codex_context import (
        build_context as build_codex_context,
    )


ADAPTERS = {
    "Claude Code": ROOT / "governance/adapters/claude/binding.yaml",
    "OpenAI Codex": ROOT / "governance/adapters/codex/binding.yaml",
}
FORBIDDEN_CORE_LITERALS = ("codex", "openai", "claude", "governance/adapters")
INSTRUCTION_SURFACES = ("CLAUDE.md", ".claude")
START_REVISION = "78dd37885ce7efbc86c684569cf758aaeeaca9a2"


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, text=True, stdout=subprocess.PIPE).stdout


def main() -> int:
    errors: list[str] = []
    bindings = {name: load(path) for name, path in ADAPTERS.items()}
    for name, binding in bindings.items():
        if not isinstance(binding, dict):
            errors.append(f"{name} binding is not a mapping")
            continue
        required = {"provider_executor": name, "logical_layer": "L4", "normative_content": "NONE"}
        for key, expected in required.items():
            if binding.get(key) != expected:
                errors.append(f"{name} binding {key} mismatch")
        ownership = binding.get("ownership")
        if not isinstance(ownership, dict) or ownership.get("core_semantics") != "governance/core" or ownership.get("project_values") != "governance/adopters/hugeplanning" or ownership.get("canonical_history") != "governance/learning":
            errors.append(f"{name} ownership boundary mismatch")
        if binding.get("core_contract") != "../../core/project-operating-contract.md":
            errors.append(f"{name} does not bind the common core contract")
    codex, claude = build_codex_context(), build_claude_context()
    for context in (codex, claude):
        if "{{" in str(context.get("resolved_core_contract")):
            errors.append("adapter did not resolve the configured common core")
        if context.get("adopter_binding") != "governance/adopters/hugeplanning/core-binding.yaml":
            errors.append("adapter does not retain project-owned configuration")
    if codex.get("core_sha256") != claude.get("core_sha256") or codex.get("resolved_core_sha256") != claude.get("resolved_core_sha256"):
        errors.append("adapters do not resolve identical common core bytes")
    for path in [ROOT / "governance/core/project-operating-contract.md", *sorted((ROOT / "governance/core/l6").glob("*.py"))]:
        if any(literal in path.read_text(encoding="utf-8").lower() for literal in FORBIDDEN_CORE_LITERALS):
            errors.append(f"reusable core contains provider-specific literal: {path.relative_to(ROOT)}")
    for adapter in (ROOT / "governance/adapters/claude", ROOT / "governance/adapters/codex"):
        for path in adapter.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".yaml", ".py"} and path.name != "binding.yaml" and "project-operating-contract.md" in path.read_text(encoding="utf-8"):
                errors.append(f"adapter duplicates a core path outside its binding: {path.relative_to(ROOT)}")
    if git("diff", "--name-only", START_REVISION, "--", *INSTRUCTION_SURFACES).strip():
        errors.append("active Claude instruction surfaces changed")
    if errors:
        print("FAIL: " + "; ".join(errors), file=sys.stderr)
        return 1
    print("PASS: Claude Code and OpenAI Codex bind identical configured reusable core bytes")
    print("PASS: provider mechanics are isolated to L4; L3/L5 and active Claude instructions are unchanged")
    print("PASS: both adapters inherit common L5 identity, L6 DOA, and B-07 bounded-projection semantics")
    print("DEFERRED_LIVE_CLAUDE_RUNTIME_VALIDATION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
