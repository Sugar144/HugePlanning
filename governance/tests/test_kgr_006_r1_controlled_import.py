from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import zipfile

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
GOV = ROOT / "governance"
sys.path.insert(0, str(GOV / "tools"))
from _lib.strict_yaml import load
from prepare_enforcement_correction import (
    EVALUATION_OUTPUTS,
    OUTPUTS,
    validate_reconciliation,
)

RUN = GOV / "runs/KGR-006-R1-enforcement-analysis-correction"
REVIEW = GOV / "reviews/kgr-006-r1-controlled-import-and-owner-review"
SOURCE = Path("/home/sugar/Documents/HugePlanning-workspace/formal-runs/KGR-006-R1/output/HugePlanning-KGR-006-R1-minimum-enforcement-analysis-correction-v0.1.0.zip")
EVALUATION = Path("/home/sugar/Documents/HugePlanning-workspace/formal-runs/KGR-006-R1/evaluation/HugePlanning-KGR-006-R1-independent-evaluation-v0.1.0.zip")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_exact_packages_reconcile_with_imports_and_consumed_authorization():
    result = validate_reconciliation(ROOT, SOURCE, EVALUATION)
    assert result == {
        "result": "VALID",
        "diagnostics": [],
        "run": "KGR-006-R1",
        "source_package_sha256": "0f496b5b17feb724977f189413f485100b9a66d98b1f79dc05cf45fb60aee66b",
        "evaluation_package_sha256": "ab133dc6e92b0a51f9911f5dd39bf65f3b2e244f97b023d98ea06a695f5fbe62",
        "source_member_count": 7,
        "evaluation_member_count": 3,
        "execution_count_limit": 1,
        "execution_count_consumed": 1,
        "remaining_execution_available": False,
    }


def test_every_immutable_member_is_byte_identical_and_allowlisted_exactly_once():
    record = load(REVIEW / "kgr-006-r1-import-validation-v0.1.0.yaml")
    schema = json.loads((GOV / "schemas/governance-validation-record.schema.json").read_text())
    jsonschema.Draft202012Validator(schema).validate(record)
    allowlist = record["subject"]["immutable_artifact_style_exclusion_allowlist"]
    expected_paths = [f"governance/runs/KGR-006-R1-enforcement-analysis-correction/outputs/{name}" for name in OUTPUTS]
    expected_paths += [f"governance/runs/KGR-006-R1-enforcement-analysis-correction/evaluation/{name}" for name in EVALUATION_OUTPUTS]
    assert allowlist == expected_paths
    for package, directory, names in ((SOURCE, RUN / "outputs", OUTPUTS), (EVALUATION, RUN / "evaluation", EVALUATION_OUTPUTS)):
        with zipfile.ZipFile(package) as archive:
            assert archive.namelist() == names
            for name in names:
                assert archive.read(name) == (directory / name).read_bytes()


def test_authorization_consumption_is_exact_and_nonreusable():
    authorization = load(RUN / "authorization/execution-authorization.yaml")["execution_authorization"]
    assert authorization["status"] == "CONSUMED"
    assert authorization["execution_count_limit"] == authorization["execution_count_consumed"] == 1
    assert authorization["execution_available"] is False
    assert authorization["consumed_by_output_package_sha256"] == digest(SOURCE)
    assert authorization["consumption_events"] == [{
        "sequence": 1,
        "run": "KGR-006-R1",
        "output_package_sha256": digest(SOURCE),
        "source_declared_result": "CORRECTION_COMPLETE_PENDING_INDEPENDENT_EVALUATION",
        "reconciliation_evidence": "governance/reviews/kgr-006-r1-controlled-import-and-owner-review/kgr-006-r1-import-validation-v0.1.0.yaml",
    }]


def test_decision_dossier_preserves_order_questions_and_authority_boundaries():
    text = (REVIEW / "project-owner-decision-dossier-v0.1.0.md").read_text()
    assert text.index("### OD-002") < text.index("### OD-003") < text.index("### OD-001")
    questions = [
        "Appoint an evaluator outside the Engineer's unilateral control and address disclosed conflicts.",
        "Confirm the exact Kernel version and scope presented for decision without broadening the single-user minimum analysis into later functionality.",
        "Decide whether the final decision packet is sufficiently comprehensible or must be simplified or reviewed under ER-015.",
        "Return, reject, or separately ratify the exact proposed Kernel after independent evaluation.",
        "If later ratification occurs, accept, reject, or return the recommended minimum GOV-7 package and separately authorize any implementation.",
        "Define any later pilot transition, provider, data or jurisdiction, effect classes, budget, and competent specialist or operational owners.",
    ]
    assert all(text.count(question) >= 1 for question in questions)
    for field in ("Why it exists", "Relevant Kernel clause or clauses", "Options available", "Enforcement Engineer recommendation", "Independent Evaluator assessment", "Consequences", "Residual risk", "Reversibility", "Deferral possible", "What deferral blocks", "Dependencies", "Proposed answer format", "Current status"):
        assert text.count(field) >= 6
    assert text.count("| SD-001 / ER-007 |") == 1
    assert text.count("| SD-002 / ER-012 |") == 1
    assert text.count("| SD-003 / ER-015 |") == 1
    assert text.count("| SD-004 / ER-019 |") == 1
    assert "PROPOSED_NOT_RATIFIED" in text
    assert "RECOMMENDATION_ONLY" in text


def test_phase_readiness_is_prepared_not_executed_and_fully_classified():
    review = load(REVIEW / "gov-5-phase-closure-readiness-v0.1.0.yaml")["phase_closure_readiness_review"]
    assert review["status"] == "PREPARED_FOR_PROJECT_OWNER_REVIEW_NOT_EXECUTED"
    assert review["authoritative_to_close_phase"] is False
    assert review["creates_new_governance_layer"] is False
    allowed = set(review["allowed_classifications"])
    for group in review["inventory"].values():
        assert group
        for item in group:
            assert item["classification"] in allowed
    ideas = review["inventory"]["strategic_ideas_relevant_to_phase_transition"]
    assert [item["id"] for item in ideas] == [f"HP-MCAND-{number:03d}" for number in range(1, 11)]
    decisions = {item["id"]: item["classification"] for item in review["inventory"]["unresolved_owner_decisions"]}
    assert decisions["OD-002"] == decisions["OD-003"] == "MUST_RESOLVE_BEFORE_GOV_6"
    assert review["personal_tfg_boundary"]["canonical_project_requirement_created"] is False
    assert review["readiness_summary"]["gov_5_closed"] is False
    assert review["readiness_summary"]["gov_6_activated"] is False
