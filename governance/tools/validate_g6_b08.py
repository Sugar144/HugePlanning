#!/usr/bin/env python3
"""Deterministically validate the G6 B-08 OpenAI Codex L4 adapter."""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

from render_g6_b08_codex_context import BINDING, ROOT, build_context
from _lib.strict_yaml import StrictYAMLError, load


START_REVISION = "28313653db4d384997efd3565162b12a14475163"
ADAPTER_DIR = ROOT / "governance/adapters/codex"
INSTRUCTIONS = ("AGENTS.md", "governance/AGENTS.md", "CLAUDE.md")
FORBIDDEN_CORE_LITERALS = ("codex", "openai", "claude", "governance/adapters")


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, text=True, stdout=subprocess.PIPE).stdout


def main() -> int:
    errors: list[str] = []
    try:
        binding = load(BINDING)
        context = build_context()
    except (StrictYAMLError, ValueError, OSError) as exc:
        errors.append(str(exc))
        binding, context = {}, {}
    if not isinstance(binding, dict):
        errors.append("Codex binding is not a mapping")
        binding = {}
    required = {
        "document_id": "GOV-GEN-G6-CODEX-ADAPTER-001",
        "provider_executor": "OpenAI Codex",
        "logical_layer": "L4",
        "normative_content": "NONE",
        "execution_surface": "ephemeral_codex_context_json",
    }
    for key, expected in required.items():
        if binding.get(key) != expected:
            errors.append(f"Codex binding {key} mismatch")
    ownership = binding.get("ownership", {})
    if not isinstance(ownership, dict) or ownership.get("core_semantics") != "governance/core" or ownership.get("project_values") != "governance/adopters/hugeplanning" or ownership.get("canonical_history") != "governance/learning":
        errors.append("Codex binding ownership boundary mismatch")
    for path in ADAPTER_DIR.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".py"}:
            text = path.read_text(encoding="utf-8").lower()
            if "project-operating-contract.md" in text and path.name != "binding.yaml":
                errors.append(f"adapter duplicates a core path outside its binding: {path.relative_to(ROOT)}")
    core_files = [ROOT / "governance/core/project-operating-contract.md", *sorted((ROOT / "governance/core/l6").glob("*.py"))]
    for path in core_files:
        text = path.read_text(encoding="utf-8").lower()
        if any(literal in text for literal in FORBIDDEN_CORE_LITERALS):
            errors.append(f"reusable core contains provider-specific literal: {path.relative_to(ROOT)}")
    if context.get("resolved_core_contract") is None or "{{" in str(context.get("resolved_core_contract")):
        errors.append("Codex context did not resolve the reusable core")
    if context.get("adopter_binding") != "governance/adopters/hugeplanning/core-binding.yaml":
        errors.append("Codex context does not retain project-owned adopter binding")
    if git("diff", "--name-only", START_REVISION, "--", "governance/core", "governance/adopters/hugeplanning", "governance/learning").strip():
        errors.append("B-08 changed reusable core, project ownership, or canonical L5 custody")
    if git("diff", "--name-only", START_REVISION, "--", *INSTRUCTIONS).strip():
        errors.append("B-08 changed an active instruction surface")
    legacy_l4 = sorted(ROOT.glob("governance/skills/*/agents/openai.yaml"))
    claude_root = ROOT / "CLAUDE.md"
    claude_is_core_adapter = "governance/core/project-operating-contract.md" in claude_root.read_text(encoding="utf-8")
    if len(legacy_l4) != 4:
        errors.append("expected four existing L4 openai binding artifacts is not met")
    if errors:
        print("FAIL: " + "; ".join(errors), file=sys.stderr)
        return 1
    print("PASS: Codex resolves the configured reusable core without normative L4 duplication")
    print("PASS: reusable core has no Codex, OpenAI, Claude, or adapter dependency")
    print("PASS: L3/L5 ownership and active instruction surfaces are unchanged")
    if not (ROOT / "governance/adapters/claude").exists() and not claude_is_core_adapter:
        print("RESIDUAL: FIRST_PROVIDER_CORE_ADAPTER_NOT_EVIDENCED")
    print("resolved_core_sha256=" + str(context["resolved_core_sha256"]))
    print("adapter_sha256=" + hashlib.sha256(BINDING.read_bytes()).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
