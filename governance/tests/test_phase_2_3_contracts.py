from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest
import yaml


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "governance/skills/formal-governance-run-preparer"
READINESS = ROOT / "governance/reviews/phase-2-3-formal-run-preparation/kgr-005-readiness-v0.1.0.yaml"


def test_skill_structure_and_interface() -> None:
    text = (SKILL / "SKILL.md").read_text()
    assert text.startswith("---\n")
    boundary = text.find("\n---\n", 4)
    metadata = yaml.safe_load(text[4:boundary])
    assert set(metadata) == {"name", "description"}
    assert metadata["name"] == "formal-governance-run-preparer"
    assert len(metadata["description"]) >= 80
    interface = yaml.safe_load((SKILL / "agents/openai.yaml").read_text())["interface"]
    assert set(interface) == {"display_name", "short_description", "default_prompt"}
    assert 25 <= len(interface["short_description"]) <= 64
    assert "$formal-governance-run-preparer" in interface["default_prompt"]


def test_skill_routes_deterministic_work_and_stops_before_execution() -> None:
    text = (SKILL / "SKILL.md").read_text()
    for tool in (
        "validate_run_package.py",
        "validate_closure_loop.py",
        "validate_prompts.py",
        "manage_learning.py",
        "build_review_bundle.py",
    ):
        assert tool in text
    for binding in ("role", "mode", "prompt", "protocol", "loop", "envelope", "hashes"):
        assert binding in text
    for boundary in (
        "Stop before formal execution",
        "invoke an LLM role",
        "Controller transition",
        "successor run",
        "modify the Kernel",
        "accept risk",
        "pull request",
        "merge",
        "release",
    ):
        assert boundary in text


def test_kgr_005_readiness_record_schema_and_boundary() -> None:
    record = yaml.safe_load(READINESS.read_text())
    schema = json.loads(
        (ROOT / "governance/schemas/governance-validation-record.schema.json").read_text()
    )
    jsonschema.Draft202012Validator(schema).validate(record)
    subject = record["subject"]
    assert subject["run"] == "KGR-005"
    assert subject["package_sha256"] == "26291b32594f2b73e12107bec9572b528e4ec3e32e4ca08f9746c5aba1adf9cf"
    assert subject["member_count"] == 19
    assert subject["execution_status"] == "NOT_STARTED"
    assert subject["formal_outputs"] == "ABSENT"
    assert subject["completed_output_package"] == "ABSENT"
    assert subject["controller_transition"] == "ABSENT"
    assert subject["readiness"] == "READY_FOR_EXPLICIT_FORMAL_EXECUTION_AUTHORIZATION"


def test_validation_record_tool_rejects_unexpected_properties() -> None:
    record = yaml.safe_load(READINESS.read_text())
    schema = json.loads(
        (ROOT / "governance/schemas/governance-validation-record.schema.json").read_text()
    )
    record["tool"]["unexpected"] = "forbidden"
    with pytest.raises(jsonschema.ValidationError, match="Additional properties"):
        jsonschema.Draft202012Validator(schema).validate(record)


def test_phase_2_3_registry_and_backlog_status() -> None:
    registry = yaml.safe_load((ROOT / "governance/ARTIFACT_REGISTRY.yaml").read_text())
    ids = [item["id"] for item in registry["artifacts"]]
    assert len(ids) == len(set(ids))
    for artifact_id in ("GOV-SKILL-003", "GOV-VAL-001", "GOV-REVIEW-006"):
        assert artifact_id in ids
    backlog = (ROOT / "governance/methodology/METHODOLOGY_BACKLOG.md").read_text()
    section = backlog.split("## HP-MPROP-002", 1)[1].split("## ", 1)[0]
    proposal = yaml.safe_load(section.split("```yaml", 1)[1].split("```", 1)[0])["proposal"]
    assert proposal["first_skill"]["name"] == "formal-governance-run-preparer"
    assert proposal["first_skill"]["status"] == "IMPLEMENTED_LOCALLY_PENDING_REVIEW"
    assert "without executing it" in proposal["first_skill"]["purpose"]
    assert any("execute a run" in item and "explicit authorization" in item for item in proposal["non_goals"])
