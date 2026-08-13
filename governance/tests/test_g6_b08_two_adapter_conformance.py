from __future__ import annotations

import subprocess
from pathlib import Path

from governance.tools.build_g6_b07_projection import build
from governance.tools.render_g6_b08_claude_context import ROOT, build_context
from governance.tools.render_g6_b08_codex_context import (
    build_context as build_codex_context,
)


def test_two_adapters_resolve_identical_configured_core() -> None:
    claude, codex = build_context(), build_codex_context()
    assert claude["core_sha256"] == codex["core_sha256"]
    assert claude["resolved_core_sha256"] == codex["resolved_core_sha256"]
    assert claude["adopter_binding"] == codex["adopter_binding"] == "governance/adopters/hugeplanning/core-binding.yaml"


def test_claude_context_accepts_bounded_b07_projection_and_is_ephemeral(tmp_path: Path) -> None:
    projection_root = tmp_path / "projection"
    build(ROOT, "g6-b08", "Claude adapter conformance", projection_root)
    context = build_context(projection_root / "projection.json")
    assert context["instruction_surface"] == "ephemeral_claude_context_markdown"
    assert context["l7_projection"]["token_measurement"]["count"] <= context["l7_projection"]["token_measurement"]["limit"]
    subprocess.run(["python3", "governance/tools/render_g6_b08_claude_context.py", "--output", str(tmp_path), "--l7-projection", str(projection_root / "projection.json")], cwd=ROOT, check=True)
    rendered = (tmp_path / "claude-context.md").read_text()
    assert "# Ephemeral governance context for Claude Code" in rendered
    assert "## Bounded L7 projection" in rendered
