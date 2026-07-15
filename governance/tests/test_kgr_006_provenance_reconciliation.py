from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
GOV = ROOT / "governance"
sys.path.insert(0, str(GOV / "tools"))
from _lib.strict_yaml import load
from prepare_enforcement_run import OUTPUTS

RUN = GOV / "runs/KGR-006-enforcement-analysis"
EVALUATION_OUTPUTS = [
    "00-independent-evaluation-basis.md",
    "01-independent-evaluation-findings.yaml",
    "02-independent-evaluation-report.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_retrospective_attestation_is_explicit_and_never_contemporaneous():
    attestation = load(RUN / "provenance/retrospective-execution-authorization-attestation-v0.1.0.yaml")["attestation"]
    assert attestation["evidence_classification"] == "RETROSPECTIVE_PROJECT_OWNER_ATTESTATION"
    assert attestation["attested_execution"]["run"] == "KGR-006"
    assert attestation["attested_execution"]["execution_count"] == 1
    assert attestation["original_authorization_custody"]["contemporaneous_repository_record"] is False
    assert attestation["original_authorization_custody"]["exact_historical_authorization_text"] == "NOT_PRESERVED"
    assert attestation["methodological_use"]["sufficient_for_bounded_import"] is True
    assert "substantive validation" in attestation["methodological_use"]["does_not_establish"]


def test_source_outputs_match_exact_import_validation_inventory():
    record = load(GOV / "reviews/gov-5-provenance-reconciliation/kgr-006-import-validation-v0.1.0.yaml")
    source = record["subject"]["source_package"]
    assert source["package_sha256"] == "10f41f15cb8d76eb91d625b47f200d114efca746ad6a28b26555e8f5b26de07a"
    assert source["imported_outputs_byte_identical"] is True
    assert [item["member"] for item in source["inventory"]] == OUTPUTS
    for item in source["inventory"]:
        path = RUN / "outputs" / item["member"]
        assert path.stat().st_size == item["size"]
        assert sha256(path) == item["sha256"]


def test_independent_evaluation_matches_inventory_and_return_result():
    record = load(GOV / "reviews/gov-5-provenance-reconciliation/kgr-006-import-validation-v0.1.0.yaml")
    evaluation = record["subject"]["evaluation_package"]
    assert evaluation["package_sha256"] == "1c2167a093ec5d7bf636fe2ab25202e714e5375389ec4464653b0eefd45ed39e"
    assert evaluation["declared_result"] == "RETURN_FOR_VERSIONED_CORRECTION"
    assert evaluation["imported_artifacts_byte_identical"] is True
    assert [item["member"] for item in evaluation["inventory"]] == EVALUATION_OUTPUTS
    for item in evaluation["inventory"]:
        path = RUN / "evaluation" / item["member"]
        assert path.stat().st_size == item["size"]
        assert sha256(path) == item["sha256"]
    findings = load(RUN / "evaluation/01-independent-evaluation-findings.yaml")["independent_evaluation"]
    assert findings["declared_result"] == "RETURN_FOR_VERSIONED_CORRECTION"
    assert len(findings["material_challenges"]) == 3


def test_import_validation_record_schema_and_nonacceptance_boundary():
    record = load(GOV / "reviews/gov-5-provenance-reconciliation/kgr-006-import-validation-v0.1.0.yaml")
    schema = json.loads((GOV / "schemas/governance-validation-record.schema.json").read_text())
    jsonschema.Draft202012Validator(schema).validate(record)
    assert record["result"] == "VALID"
    status = record["subject"]["substantive_status"]
    assert status == {
        "source_execution": "EXTERNALLY_EXECUTED_RETROSPECTIVELY_ATTESTED",
        "independent_evaluation": "COMPLETED_RETURN_FOR_VERSIONED_CORRECTION",
        "kgr_006_validated": False,
        "accepted": False,
        "gov_5_completed": False,
        "kernel_ratified": False,
        "enforceable": False,
        "implemented": False,
        "operational": False,
    }


def test_learning_records_preserve_three_material_challenges():
    records = {record_id: load(GOV / f"learning/records/{record_id}.yaml")["failure_record"] for record_id in ("HP-FAIL-014", "HP-FAIL-015", "HP-FAIL-016")}
    assert records["HP-FAIL-014"]["status"] == "CONTAINED"
    assert records["HP-FAIL-014"]["severity"] == "HIGH"
    assert records["HP-FAIL-015"]["status"] == "CONTAINED"
    assert records["HP-FAIL-016"]["status"] == "CONTAINED"
    assert all(record["accepted_risk"] is None for record in records.values())
