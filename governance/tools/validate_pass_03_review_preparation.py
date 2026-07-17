#!/usr/bin/env python3
"""Validate the prospective executable PASS-03 adversarial-review package."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib.strict_yaml import load
from validate_pass_03_execution import RUN_REL, package_hash, sha256

ROOT = Path(__file__).resolve().parents[2]
AUDIT_REL = Path("governance/audits/GOV-AUD-001-gov7-enablement")
PREP_REL = AUDIT_REL / "review-executions/GOV-AUD-001-P03-AR-001"
PACKAGE_HASH = "d93c98535e38d952582b59e460d17ac62db8fea3ebfed794383d384a0b9f43fe"
PENDING = "EXECUTED_VALIDATED_PENDING_INDEPENDENT_ADVERSARIAL_REVIEW_AND_PROJECT_OWNER_DISPOSITION"
PREPARED = "PREPARED_VALIDATED_PENDING_PROJECT_OWNER_REVIEW_EXECUTION_AUTHORIZATION"
RESULTS = {"PASS_03_CONFIRMED_SUITABLE_FOR_PROJECT_OWNER_DISPOSITION", "PASS_03_R2_REQUIRED", "PASS_03_REVIEW_INVALID_OR_INCOMPLETE"}
ATTACK_FIELDS = {"attack_id", "attack_dimension", "target_claim_or_assumption", "attack_method", "counterexample_or_failure_scenario", "evidence_examined", "result", "impact"}
RESULT_REL = PREP_REL / "output/pass-03-adversarial-review-result.yaml"


def errors_for(root: Path) -> list[str]:
    errors: list[str] = []
    prep = root / PREP_REL
    required = ["contract.yaml", "input/input-manifest.yaml", "output-artifact-specification.yaml", "validation-plan.yaml", "custody-and-publication-rules.md", "manifest.yaml", "reviewer-independence-declaration-template.yaml", "operational-evidence/failed-review-attempt-001.yaml"]
    for item in required:
        if not (prep / item).is_file(): errors.append(f"review preparation artifact missing: {item}")
    prompt = root / "governance/prompts/reviews/HP-PROMPT-037-gov-aud-001-pass-03-adversarial-review-v0.1.0.md"
    if not prompt.is_file(): errors.append("instantiated review prompt missing")
    if errors: return errors
    source = load(root / RUN_REL / "manifest.yaml")
    review_package = load(root / RUN_REL / "review-package/manifest.yaml").get("review_package", {})
    if source.get("run", {}).get("status") != PENDING or source.get("adversarial_review_package", {}).get("independent_review_executed") is not False:
        errors.append("PASS-03 source state or review consumption mismatch")
    if review_package.get("package_sha256") != PACKAGE_HASH or package_hash(review_package.get("members", [])) != PACKAGE_HASH:
        errors.append("immutable review package aggregate hash mismatch")
    contract = load(prep / "contract.yaml").get("review_execution_contract", {})
    if contract.get("contract_id") != "GOV-AUD-001-PASS-03-ADVERSARIAL-REVIEW-CONTRACT" or str(contract.get("version")) != "0.1.0" or contract.get("status") != PREPARED:
        errors.append("review contract identity or status mismatch")
    if contract.get("immutable_evidence_package", {}).get("package_sha256") != PACKAGE_HASH or contract.get("review_identity", {}).get("execution_count_consumed") != 0:
        errors.append("review contract immutable package or execution count mismatch")
    independence = contract.get("reviewer_independence", {})
    if set(independence.get("required_classifications", [])) != {"INDEPENDENT", "PARTIALLY_INDEPENDENT_WITH_DISCLOSED_LIMITATIONS", "NOT_INDEPENDENT", "UNVERIFIABLE"} or set(independence.get("permitted_to_proceed", [])) != {"INDEPENDENT", "PARTIALLY_INDEPENDENT_WITH_DISCLOSED_LIMITATIONS"}:
        errors.append("reviewer independence classification contract mismatch")
    attack = contract.get("attack_requirements", {})
    if set(attack.get("required_attack_fields", [])) != ATTACK_FIELDS or attack.get("minimum_meaningful_attacks") != 3 or len(set(attack.get("attack_dimensions", []))) < 16:
        errors.append("adversarial attack record contract mismatch")
    semantics = contract.get("result_semantics", {})
    if set(semantics.get("permitted_terminal_results", [])) != RESULTS or semantics.get("exactly_one_terminal_result") is not True or semantics.get("PASS_03_REVIEW_INVALID_OR_INCOMPLETE", {}).get("pass_03_state_transition") != "NO_PASS_03_STATE_ADVANCEMENT":
        errors.append("PASS-03 review result or incomplete-state semantics mismatch")
    if "PASS_04_authority" not in " ".join(contract.get("invalid_review_conditions", [])):
        errors.append("premature PASS-04 authority prohibition missing")
    manifest = load(prep / "input/input-manifest.yaml").get("review_input_manifest", {})
    if manifest.get("manifest_id") != "GOV-AUD-001-P03-AR-001-INPUT-001" or manifest.get("immutable_review_package", {}).get("aggregate_sha256") != PACKAGE_HASH:
        errors.append("review input manifest identity or immutable package mismatch")
    members = manifest.get("members", [])
    if manifest.get("member_count") != len(members) or package_hash(members) != manifest.get("input_package_sha256"):
        errors.append("review input manifest package hash mismatch")
    for item in members:
        path = root / item.get("path", "")
        if not path.is_file() or sha256(path) != item.get("sha256"):
            errors.append(f"review input member hash mismatch: {item.get('path')}")
    spec = load(prep / "output-artifact-specification.yaml").get("review_output_specification", {})
    required_fields = {"review_id", "review_contract_id", "review_contract_version", "review_prompt_id", "review_prompt_version", "reviewed_run", "review_package_id", "review_package_sha256", "reviewer_model", "reviewer_mode", "independence_classification", "independence_evidence", "attacks", "material_findings", "non_blocking_observations", "result", "r2_required", "r2_scope", "files_modified", "validation", "timestamp"}
    if set(spec.get("required_fields", [])) != required_fields or set(spec.get("result_rules", {}).get("permitted", [])) != RESULTS:
        errors.append("review output specification mismatch")
    template = load(prep / "reviewer-independence-declaration-template.yaml").get("reviewer_independence_declaration_template", {})
    if "independence_classification" not in template.get("required_fields", []) or template.get("execution_value") != "NOT_CREATED_PENDING_SEPARATE_OWNER_REVIEW_EXECUTION_AUTHORIZATION":
        errors.append("reviewer independence declaration template mismatch")
    operational = load(prep / "operational-evidence/failed-review-attempt-001.yaml").get("operational_evidence", {})
    if operational.get("status") != "PRESERVED_NOT_AN_EXECUTED_ADVERSARIAL_REVIEW" or "independent_review_executed" not in operational.get("prohibited_interpretations", []):
        errors.append("failed review attempt preservation mismatch")
    package = load(prep / "manifest.yaml").get("review_execution_package", {})
    if package.get("status") != PREPARED or package.get("review_executed") is not False or package.get("review_opportunity_consumed") is not False or package.get("reviewed_package_sha256") != PACKAGE_HASH:
        errors.append("review execution package state mismatch")
    if any(package.get("authority_boundary", {}).get(key) is not False for key in ("PASS_03_accepted", "PASS_03_completed", "PASS_04_authorized_or_executed", "tooling_selected", "learning_pipeline_implemented", "GOV_7_activated", "Kernel_changed", "OD_006_resolved", "risk_accepted")):
        errors.append("review execution package authority boundary mismatch")
    text = prompt.read_text()
    for required_text in ("GOV-AUD-001-P03-AR-001", "GOV-AUD-001-PASS-03-ADVERSARIAL-REVIEW-CONTRACT/0.1.0", PACKAGE_HASH, "PASS_03_REVIEW_INVALID_OR_INCOMPLETE", "Do not modify the reviewed run"):
        if required_text not in text: errors.append("instantiated review prompt content mismatch")
    result_path = root / RESULT_REL
    if result_path.is_file():
        result = load(result_path).get("pass_03_adversarial_review", {})
        if set(result) != required_fields:
            errors.append("materialized review diagnostic field mismatch")
        if any((
            result.get("review_id") != "GOV-AUD-001-P03-AR-001",
            result.get("review_contract_id") != "GOV-AUD-001-PASS-03-ADVERSARIAL-REVIEW-CONTRACT",
            str(result.get("review_contract_version")) != "0.1.0",
            result.get("reviewed_run") != "GOV-AUD-001-P03-R1",
            result.get("review_package_id") != "GOV-AUD-P03-REVIEW-PACKAGE-001",
            result.get("review_package_sha256") != PACKAGE_HASH,
        )):
            errors.append("materialized review diagnostic identity mismatch")
        if any((
            result.get("result") != "PASS_03_REVIEW_INVALID_OR_INCOMPLETE",
            result.get("r2_required") is not False,
            result.get("r2_scope") != "NOT_APPLICABLE_INVALID_REVIEW_DOES_NOT_AUTHORIZE_R2",
            package.get("review_executed") is not False,
            package.get("review_opportunity_consumed") is not False,
        )):
            errors.append("invalid review diagnostic advanced PASS-03 lifecycle")
    return errors


def validate(root: Path = ROOT) -> dict:
    errors = errors_for(root)
    return {"result": "VALID" if not errors else "INVALID", "diagnostics": errors}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(); result = validate(args.root.resolve()); print(json.dumps(result, sort_keys=True)); raise SystemExit(result["result"] != "VALID")
