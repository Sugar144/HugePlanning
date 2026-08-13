from __future__ import annotations

import json
import subprocess
from pathlib import Path

from governance.tools.build_g6_b07_projection import build
from governance.tools.render_g6_b08_codex_context import ROOT, build_context


def test_codex_context_resolves_configured_core_without_embedding_adapter_rules(tmp_path: Path) -> None:
    context = build_context()
    assert context["provider_executor"] == "OpenAI Codex"
    assert "{{" not in context["resolved_core_contract"]
    assert context["adopter_binding"] == "governance/adopters/hugeplanning/core-binding.yaml"
    assert context["instruction_surface"] == "ephemeral_codex_context_json"


def test_codex_context_accepts_a_bounded_b07_projection(tmp_path: Path) -> None:
    projection_root = tmp_path / "projection"
    build(ROOT, "g6-b08", "Codex adapter conformance", projection_root)
    context = build_context(projection_root / "projection.json")
    assert context["l7_projection"]["token_measurement"]["count"] <= context["l7_projection"]["token_measurement"]["limit"]


def test_codex_renderer_emits_ephemeral_context(tmp_path: Path) -> None:
    subprocess.run(["python3", "governance/tools/render_g6_b08_codex_context.py", "--output", str(tmp_path)], cwd=ROOT, check=True)
    context = json.loads((tmp_path / "codex-context.json").read_text())
    assert context["adapter"] == "GOV-GEN-G6-CODEX-ADAPTER-001"
    assert context["core_contract"] == "framework/core/project-operating-contract.md"
