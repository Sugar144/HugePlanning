from __future__ import annotations

import json
from pathlib import Path
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
GOV = ROOT / "governance"
sys.path.insert(0, str(GOV / "tools"))
from _lib.strict_yaml import load
from prepare_enforcement_run import CLAUSES, OUTPUTS, ROUTES, validate_preparation

RUN = GOV / "runs/KGR-006-enforcement-analysis"
PACKAGE = Path("/tmp/HugePlanning-KGR-006-formal-input-package.zip")


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


def test_preparation_package_is_valid_and_outputs_absent():
    result = validate_preparation(ROOT, PACKAGE)
    assert result["result"] == "VALID"
    assert result["member_count"] == 44
    assert result["execution_status"] == "NOT_STARTED"
    assert result["readiness"] == "READY_FOR_EXPLICIT_FORMAL_EXECUTION_AUTHORIZATION"


def test_prompt_snapshot_matches_canonical():
    assert (RUN / "prompt/06-enforcement-engineer-minimum-analysis-prompt-v0.1.0.md").read_bytes() == (GOV / "methodology/roles/enforcement-engineer/protocols/minimum-analysis/06-enforcement-engineer-minimum-analysis-prompt-v0.1.0.md").read_bytes()


def test_manifest_preserves_non_execution_and_authority_gates():
    manifest = load(RUN / "run-manifest.yaml")
    assert manifest["run"]["status"] == "NOT_STARTED"
    assert manifest["execution"]["authorized"] is False
    assert manifest["outputs"]["status"] == "ABSENT_NOT_EXECUTED"
    assert manifest["authority"]["enforcement_engineering_gate"] == "CLOSED"
    assert manifest["authority"]["human_ratification"] == "NOT_STARTED"


def test_matrix_schema_rejects_missing_not_applicable_destination():
    schema = json.loads((GOV / "schemas/protocols/GOV-PROTOCOL-004/0.1.0/clause-implication-matrix.schema.json").read_text())
    route_schema = schema["properties"]["enforcement_analysis"]["properties"]["routing_coverage"]["items"]
    invalid = {"route_id": "LLR-020", "applicability": "NOT_APPLICABLE_TO_GOV_5_EXECUTION", "justification": "deferred", "later_phase_destination": None}
    assert list(jsonschema.Draft202012Validator(route_schema).iter_errors(invalid))
