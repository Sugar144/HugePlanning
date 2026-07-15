from __future__ import annotations

import json
from pathlib import Path
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
GOV = ROOT / "governance"
sys.path.insert(0, str(GOV / "tools"))
from _lib.strict_yaml import load
from prepare_enforcement_run import CLAUSES, OUTPUTS, ROUTES

RUN = GOV / "runs/KGR-006-enforcement-analysis"


def test_output_contract_schema_and_exact_enums():
    doc = load(RUN / "output-contract.yaml")
    schema = json.loads((GOV / "schemas/protocols/GOV-PROTOCOL-004/0.1.0/enforcement-analysis-output-contract.schema.json").read_text())
    jsonschema.Draft202012Validator(schema).validate(doc)
    contract = doc["output_contract"]
    assert contract["coverage"]["clause_ids"] == CLAUSES
    assert contract["coverage"]["routing_ids"] == ROUTES
    assert [x["filename"] for x in contract["outputs"]] == OUTPUTS


def test_canonical_routing_has_twenty_rows_and_exact_disposition():
    source = (GOV / "runs/KGR-004-kernel-designer-revision/outputs/05-lower-layer-routing-v0.2.md").read_text()
    rows = [line for line in source.splitlines() if line.startswith("| ")][1:]
    assert len(rows) == 20
    index = load(RUN / "control/lower-layer-routing-index.yaml")["routing_index"]
    assert [x["id"] for x in index["entries"]] == ROUTES
    assert index["entries"][-1]["title"] == "Historical repository audit and S1 regularization"
    assert index["gov_5_disposition"]["LLR-020"] == {
        "applicability": "NOT_APPLICABLE_TO_GOV_5_EXECUTION",
        "later_phase_destination": "GOV-8",
        "reason": "GOV-5 analyzes enforcement implications and derived requirements; it does not perform historical S0a-S1 audit or regularization.",
    }


def test_historical_preparation_validation_remains_preserved():
    record = load(GOV / "reviews/gov-5-contract-preparation/kgr-006-readiness-v0.1.0.yaml")
    assert record["record_id"] == "GOV-VAL-003"
    assert record["result"] == "VALID"
    assert record["subject"]["package_sha256"] == "d7a92ed0d617bc61d01868e020a4ea9b5237aef6bb8bd569202f0eed2dd6a5d7"
    assert record["subject"]["execution_status"] == "NOT_STARTED"
    assert record["subject"]["formal_outputs"] == "ABSENT"


def test_prompt_snapshot_matches_canonical():
    assert (RUN / "prompt/06-enforcement-engineer-minimum-analysis-prompt-v0.1.0.md").read_bytes() == (GOV / "methodology/roles/enforcement-engineer/protocols/minimum-analysis/06-enforcement-engineer-minimum-analysis-prompt-v0.1.0.md").read_bytes()


def test_manifest_preserves_external_execution_evaluation_and_authority_gates():
    manifest = load(RUN / "run-manifest.yaml")
    assert manifest["run"]["status"] == "EXECUTED_EVALUATED_CORRECTION_REQUIRED"
    assert manifest["execution"]["authorized"] is True
    assert manifest["execution"]["authorization_evidence"] == {
        "id": "GOV-ATT-001",
        "classification": "RETROSPECTIVE_PROJECT_OWNER_ATTESTATION",
        "contemporaneous_repository_custody": False,
        "original_authorization_text": "NOT_PRESERVED",
    }
    assert manifest["outputs"]["status"] == "IMPORTED_BYTE_IDENTICAL_NOT_ACCEPTED_CORRECTION_REQUIRED"
    assert manifest["outputs"]["completed_run_package"]["substantive_validation"] is False
    assert manifest["independent_evaluation"]["result"] == "RETURN_FOR_VERSIONED_CORRECTION"
    assert manifest["authority"]["enforcement_engineering_gate"] == "CLOSED_TO_FURTHER_EXECUTION_PENDING_VERSIONED_CORRECTION"
    assert manifest["authority"]["human_ratification"] == "NOT_STARTED"


def test_matrix_schema_rejects_missing_not_applicable_destination():
    schema = json.loads((GOV / "schemas/protocols/GOV-PROTOCOL-004/0.1.0/clause-implication-matrix.schema.json").read_text())
    route_schema = schema["properties"]["enforcement_analysis"]["properties"]["routing_coverage"]["items"]
    invalid = {"route_id": "LLR-020", "applicability": "NOT_APPLICABLE_TO_GOV_5_EXECUTION", "justification": "deferred", "later_phase_destination": None}
    assert list(jsonschema.Draft202012Validator(route_schema).iter_errors(invalid))
