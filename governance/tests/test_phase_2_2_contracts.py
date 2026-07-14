from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[2]
SKILLS = {
    "governance-review-packager": ROOT / "governance/skills/governance-review-packager",
    "agent-session-reviewer": ROOT / "governance/skills/agent-session-reviewer",
}


def frontmatter(path: Path) -> dict:
    text = path.read_text()
    assert text.startswith("---\n")
    boundary = text.find("\n---\n", 4)
    assert boundary > 0
    data = yaml.safe_load(text[4:boundary])
    assert set(data) == {"name", "description"}
    return data


def test_skill_structure_and_interfaces() -> None:
    for name, directory in SKILLS.items():
        metadata = frontmatter(directory / "SKILL.md")
        assert metadata["name"] == name
        assert len(metadata["description"]) >= 80
        interface = yaml.safe_load((directory / "agents/openai.yaml").read_text())["interface"]
        assert set(interface) == {"display_name", "short_description", "default_prompt"}
        assert 25 <= len(interface["short_description"]) <= 64
        assert interface["default_prompt"]


def test_review_packager_authority_and_deterministic_routing() -> None:
    text = (SKILLS["governance-review-packager"] / "SKILL.md").read_text()
    assert "build_review_bundle.py" in text
    assert "Do not reimplement inventory, diff, ZIP, hashing, manifest" in text
    for boundary in ("stage", "commit", "push", "pull request", "ratify", "formal run", "Controller transition"):
        assert boundary in text


def test_session_reviewer_outcomes_routes_and_evidence_boundary() -> None:
    text = (SKILLS["agent-session-reviewer"] / "SKILL.md").read_text()
    for outcome in (
        "MATERIAL_FINDINGS_IDENTIFIED",
        "SESSION_REVIEW_COMPLETE_NO_MATERIAL_FINDINGS",
        "INSUFFICIENT_OBSERVABLE_EVIDENCE",
    ):
        assert outcome in text
    for route in ("learning system", "methodology backlog", "tool proposal", "skill proposal", "versioned correction"):
        assert route in text
    assert "Never claim access to hidden reasoning" in text
    assert "Do not manufacture findings" in text
    assert "modify the repository without explicit authority" in text


def test_review_bundle_schema_is_strict() -> None:
    schema = json.loads((ROOT / "governance/schemas/review-bundle-config.schema.json").read_text())
    jsonschema.Draft202012Validator.check_schema(schema)
    assert schema["additionalProperties"] is False
    assert schema["properties"]["repository"]["additionalProperties"] is False
    assert schema["$defs"]["command"]["additionalProperties"] is False


def test_backlog_phase_2_2_status_and_strict_yaml_documents() -> None:
    backlog = (ROOT / "governance/methodology/METHODOLOGY_BACKLOG.md").read_text()
    for proposal in ("HP-MPROP-002", "HP-MPROP-003", "HP-MPROP-004"):
        section = backlog.split(f"## {proposal}", 1)[1].split("## ", 1)[0]
        assert "status: IMPLEMENTED_LOCALLY_PENDING_REVIEW" in section
    registry = yaml.safe_load((ROOT / "governance/ARTIFACT_REGISTRY.yaml").read_text())
    ids = [artifact["id"] for artifact in registry["artifacts"]]
    assert len(ids) == len(set(ids))
    for artifact_id in ("GOV-TOOL-003", "GOV-SKILL-001", "GOV-SKILL-002", "GOV-REVIEW-005"):
        assert artifact_id in ids
