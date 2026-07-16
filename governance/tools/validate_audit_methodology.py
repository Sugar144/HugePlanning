#!/usr/bin/env python3
"""Validate the prospective GOV-AUD-001 methodology and review protocol."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib.strict_yaml import load, loads


AUDIT_REL = Path("governance/audits/GOV-AUD-001-gov7-enablement")
METHOD_REL = AUDIT_REL / "07-audit-methodology-and-review-protocol.yaml"
RUN_REL = AUDIT_REL / "runs/GOV-AUD-001-P02-R1"

FINDING_BASES = {
    "NORMATIVE_REQUIREMENT",
    "ACCEPTED_OWNER_DIRECTION",
    "REPOSITORY_FACT_OR_CONTRADICTION",
    "OBSERVED_FAILURE_OR_BURDEN",
    "ARCHITECTURAL_INVARIANT",
    "EXTERNAL_EVIDENCE",
    "ADVERSARIAL_COUNTEREXAMPLE",
    "MODEL_INFERENCE_ONLY",
}
ROOT_CAUSES = {
    "AGENT_EXECUTION_DEFECT",
    "RUN_PROMPT_DEFECT",
    "OPERATING_PROTOCOL_GAP",
    "GOVERNANCE_POLICY_GAP",
    "TOOLING_DEFECT",
    "AMBIGUOUS_OR_CONFLICTING_AUTHORITY",
    "INSUFFICIENT_EVIDENCE",
}
VALIDITY_SEQUENCE = [
    "OBSERVED_DEVIATION",
    "APPLICABLE_INSTRUCTION_AND_AUTHORITY_SOURCES",
    "HIERARCHY_OR_CONFLICT_ANALYSIS",
    "AVAILABLE_COMPLIANT_ALTERNATIVES",
    "ROOT_CAUSE_LAYER",
    "AUTHORITY_AND_EVIDENCE_IMPACT",
    "MATERIALITY",
    "EXECUTION_VALIDITY_CONCLUSION",
]
REVIEW_TYPES = {
    "DETERMINISTIC_VALIDATION",
    "TARGETED_CONFIRMATION",
    "INDEPENDENT_SUBSTANTIVE_REVIEW",
    "ADVERSARIAL_REVIEW",
}
REVIEW_FIELDS = {
    "review_type",
    "purpose",
    "allowed_conclusions",
    "required_independence",
    "minimum_evidence",
    "must_not_claim",
    "may_produce_pass_disposition",
}
REVIEW_SECTIONS = {
    "REVIEW_IDENTITY_AND_TYPE",
    "PURPOSE_SCOPE_AND_ALLOWED_CONCLUSIONS",
    "INDEPENDENCE_BASIS",
    "IMMUTABLE_CANDIDATE_AND_INPUT_HASHES",
    "METHOD_CHECKS_OR_ATTACKS_ATTEMPTED",
    "FINDINGS_WITH_BASIS_ROOT_CAUSE_AND_MATERIALITY",
    "LIMITATIONS_AND_UNRESOLVED_EVIDENCE",
    "CONCLUSION_AND_AUTHORITY_BOUNDARY",
}
ATTACK_DIMENSIONS = {
    "CONCRETE_COUNTEREXAMPLES",
    "SMALLEST_SUFFICIENT_RIVAL_DESIGN",
    "AUTHORITY_LEAKAGE_OR_CIRCULAR_AUTHORITY",
    "EVIDENCE_LOSS_CONTRADICTION_REWRITING_OR_PROVENANCE_FAILURE",
    "VERSION_MIGRATION_COMPATIBILITY_AND_ROLLBACK_FAILURE",
    "RECOVERY_AND_MANUAL_ESCAPE_FAILURE",
    "SELF_HOSTING_CAPTURE_OR_SELF_CERTIFICATION",
    "EXCESSIVE_OWNER_BURDEN_OR_OPERATIONAL_BUREAUCRACY",
    "UNSUPPORTED_ASSUMPTIONS_AND_REASONABLE_UNKNOWN_UNKNOWNS",
}
BLOCKING_DIMENSIONS = {
    "AUTHORITY",
    "TRUST_ROOT",
    "EVIDENCE_INTEGRITY",
    "CANONICAL_OWNERSHIP",
    "TRACEABILITY",
    "DECISION_VALIDITY",
    "COMPATIBILITY_OR_MIGRATION",
    "RECOVERY_OR_ROLLBACK",
    "INDEPENDENT_EVALUATION",
    "SCOPE_DISCIPLINE",
    "REQUIRED_CONTRACTED_OUTPUT",
    "PROJECT_OWNER_CHECKPOINT_DECISION",
}
NON_BLOCKING_CLASSES = {
    "NON_BLOCKING",
    "OPTIONAL_IMPROVEMENT",
    "FOLLOW_UP_CANDIDATE",
    "RESEARCH_REQUIRED",
    "OWNER_DECISION_REQUIRED",
}
TRACEABILITY_CHAIN = [
    "OBSERVED_EVENT_OR_PROBLEM",
    "METHODOLOGY_REQUIREMENT",
    "CHANGED_CANONICAL_ARTIFACT",
    "VALIDATOR_OR_REVIEW_CONTROL_WHERE_APPLICABLE",
    "VALIDATION_EVIDENCE",
    "FUTURE_GOV_7_PROPOSAL_OR_DEFERRAL_WHERE_APPLICABLE",
]
RUN_RULE = (
    "Instruction conflicts: Durable instructions do not silently expand run authority, "
    "and run prompts do not silently suppress durable obligations. Append-only learning "
    "evidence caused by the current run may be preserved when it changes no authority, "
    "accepted state, prior evidence, implementation, or risk; record the exception. "
    "Otherwise stop before acting and request Project Owner authority."
)
REVIEWER_RULE = (
    "Before declaring an execution invalid, determine whether the deviation arose from "
    "an agent defect, prompt defect, protocol gap, governance gap, tooling defect, or "
    "unresolved instruction conflict."
)
IDENTITY_RULE = (
    "Never assign repository identities from chat memory. Resolve and verify the next "
    "available identity from canonical repository registries before prospective custody "
    "or repository modification."
)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
SUPPORT_CLASSIFICATIONS = {
    "VERIFIED_FACT",
    "EVIDENCE_SUPPORTED_INFERENCE",
    "MODEL_INFERENCE_ONLY",
}
PASS_07_RESULTS = {
    "SUITABLE_FOR_PROJECT_OWNER_DECISION",
    "RETURN_FOR_BOUNDED_VERSIONED_CORRECTION",
    "INVALID_AUDIT_EXECUTION",
    "INSUFFICIENT_EVIDENCE_FOR_PASS_07_DISPOSITION",
}
ATTACK_RECORD_FIELDS = {
    "attack_id", "attack_dimension", "target_claim_or_assumption", "attack_method",
    "counterexample_or_failure_scenario", "evidence_examined", "result", "impact",
}
ATTACK_RECORD_DIMENSIONS = {
    "ASSUMPTION_REFUTATION", "COUNTEREXAMPLE_CONSTRUCTION", "AUTHORITY_CIRCULARITY_ATTACK",
    "FAILURE_MODE_ATTACK", "MINIMALITY_CHALLENGE", "MIGRATION_OR_ROLLBACK_ATTACK",
    "EVIDENCE_LOSS_OR_CONTRADICTION_ATTACK", "INDEPENDENCE_OR_SELF_CERTIFICATION_ATTACK",
    "OWNER_BURDEN_OR_BUREAUCRACY_CHALLENGE", "RIVAL_ARCHITECTURE_CHALLENGE",
}
P02_HASHES = {
    "authorization/owner-authorization.yaml": "efec5e415e9fadb25e33d6693e83b29a6df3f282d16976a3f43d99711450a376",
    "evaluation/pass-02-validation-report.yaml": "ecc2bf4d4d6c5b3d07af34ea79b716e3c1c2c6063f39cc9e8b79d85584d69e8e",
    "input/input-manifest.yaml": "bc5c9764ab0a30a2c96665e09c4d3e720d20be35631e4ad06aa7c10dd656f239",
    "manifest.yaml": "03b5a19764d424268bcd5285a410fabaf5109e88eaa4a6c402d5eaefe1a4ee87",
    "output/01-bounded-context-and-ownership-model.yaml": "8ee03f87ca792fc41c366f0150abebc9a3d718441fe7669955baf0d827132742",
    "output/02-cross-layer-interface-and-contract-assessment.md": "ac92b827e6a8ffc3245a792a8ac12de1a6beba3297e0dd65a5b31709232e5415",
    "output/03-typed-relationship-and-query-model.yaml": "71122a28793a24f3debfbf586ce5b17357ab397a11b0dda2454bcaaf8b3e8e14",
    "output/04-version-migration-and-impact-model.md": "52e155f1a3f2817f5ae9f5113eba6c73dbe6ed239cd0376b76b987f0ea2ac0d0",
    "output/05-controlled-self-hosting-and-trust-boundaries.md": "4858fd98661ae274ef382a51e1de4a0e5c5d919db763db0a6ef8591b5fbdbed0",
    "output/06-architecture-style-comparison.yaml": "f00845265751fce8bb22e082abc0547312469043bc01f923c2af551d4a50bd67",
    "output/07-pass-02-findings-and-checkpoint-a-handoff.md": "459e339b6849f32a3d2fed205247af33880f69059e08059998ba49521a6e1f6e",
    "prompt/GOV-AUD-PROMPT-021-pass-02-execution-v0.1.0.md": "b41cafb36922839781a334b4d851c00c80a253bc5ab7ecf96dd84955501e669c",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _string_list(value) -> bool:
    return isinstance(value, list) and bool(value) and all(isinstance(item, str) and item for item in value)


def _present(value) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return value is not None


def _as_string_set(value) -> set[str] | None:
    if isinstance(value, str) and value:
        return {value}
    if isinstance(value, list) and value and all(isinstance(item, str) and item for item in value):
        return set(value)
    return None


def _review_records(method: dict) -> dict[str, dict]:
    records = method.get("review_contract", {}).get("review_types", [])
    return {
        record.get("review_type"): record
        for record in records
        if isinstance(record, dict) and isinstance(record.get("review_type"), str)
    }


def _discover_pass_contracts(root: Path) -> tuple[dict[str, tuple[Path, dict]], list[str]]:
    """Discover canonical pass contracts without a permanent pass-name allowlist."""
    errors: list[str] = []
    discovered: dict[str, tuple[Path, dict]] = {}
    contract_ids: set[str] = set()
    passes = root / AUDIT_REL / "passes"
    for path in sorted(passes.glob("*/contract.yaml")):
        try:
            contract = load(path).get("pass", {})
        except Exception as exc:
            errors.append(f"pass contract unreadable: {path}: {exc}")
            continue
        pass_id = contract.get("id") if isinstance(contract, dict) else None
        identity = contract.get("contract_identity", {}) if isinstance(contract, dict) else {}
        contract_id = identity.get("contract_id") if isinstance(identity, dict) else None
        if not isinstance(pass_id, str) or not pass_id or path.parent.name != pass_id:
            errors.append(f"pass contract path/id mismatch: {path}")
            continue
        if not isinstance(contract_id, str) or not contract_id or not _present(identity.get("version")):
            # Legacy/unbound contracts remain discoverable as paths but cannot satisfy a structured review binding.
            continue
        if pass_id in discovered or contract_id in contract_ids:
            errors.append(f"duplicate or ambiguous pass contract: {pass_id} / {contract_id}")
            continue
        discovered[pass_id] = (path, contract)
        contract_ids.add(contract_id)
    return discovered, errors


def _validate_finding(method: dict, finding: dict, label: str, errors: list[str]) -> None:
    contract = method.get("instance_validation_contract", {}).get("finding_instances", {})
    required = set(contract.get("required_fields", []))
    if not isinstance(finding, dict):
        errors.append(f"{label}: finding must be a mapping")
        return
    missing = sorted(field for field in required if field not in finding)
    if missing:
        errors.append(f"{label}: finding required fields missing: {', '.join(missing)}")
        return
    for field in ("finding_id", "statement_and_scope", "evidence_refs_or_reasoning", "disposition_class", "traceability"):
        if not _present(finding.get(field)):
            errors.append(f"{label}: finding field is empty: {field}")
    bases = _as_string_set(finding.get("finding_basis"))
    allowed_bases = set(method.get("finding_contract", {}).get("finding_basis", []))
    if bases is None or not bases <= allowed_bases:
        errors.append(f"{label}: finding basis is absent or not allowed")
        bases = set()
    support = finding.get("support_classification")
    if support not in SUPPORT_CLASSIFICATIONS:
        errors.append(f"{label}: finding support classification is not allowed")
    if not isinstance(finding.get("verified_fact"), bool):
        errors.append(f"{label}: finding verified_fact must be boolean")
    inference_only = "MODEL_INFERENCE_ONLY" in bases or support == "MODEL_INFERENCE_ONLY"
    if inference_only:
        if bases != {"MODEL_INFERENCE_ONLY"} or support != "MODEL_INFERENCE_ONLY":
            errors.append(f"{label}: MODEL_INFERENCE_ONLY must remain a distinct support classification")
        if finding.get("verified_fact") is not False:
            errors.append(f"{label}: MODEL_INFERENCE_ONLY cannot be represented as verified fact")
        follow_up = _as_string_set(finding.get("required_follow_up"))
        allowed_follow_up = set(
            method.get("finding_contract", {})
            .get("model_inference_only", {})
            .get("required_follow_up_one_or_more", [])
        )
        if follow_up is None or not follow_up <= allowed_follow_up:
            errors.append(f"{label}: MODEL_INFERENCE_ONLY requires an allowed follow-up")
    materiality = finding.get("materiality")
    required_materiality = set(contract.get("materiality_required_fields", []))
    if not isinstance(materiality, dict):
        errors.append(f"{label}: materiality must be a mapping")
        return
    if required_materiality - set(materiality):
        errors.append(f"{label}: materiality fields missing")
    classification = materiality.get("classification")
    allowed_non_blocking = set(method.get("materiality", {}).get("non_blocking_classes", []))
    if classification not in allowed_non_blocking | {"BLOCKING"}:
        errors.append(f"{label}: materiality classification is not allowed")
    dimensions = _as_string_set(materiality.get("dimensions"))
    if dimensions is None:
        errors.append(f"{label}: materiality dimensions must be a non-empty string list")
    elif classification == "BLOCKING" and not dimensions <= BLOCKING_DIMENSIONS:
        errors.append(f"{label}: blocking materiality dimension is not allowed")
    if not _present(materiality.get("analysis")):
        errors.append(f"{label}: materiality analysis is required")


def validate_instance(root: Path, instance_path: Path) -> dict:
    errors: list[str] = []
    method_path = root / METHOD_REL
    if not method_path.is_file():
        return {"result": "INVALID", "diagnostics": ["audit methodology protocol missing"]}
    method = load(method_path).get("audit_methodology", {})
    contracts, discovery_errors = _discover_pass_contracts(root)
    errors.extend(discovery_errors)
    document = load(instance_path)
    instance_contract = method.get("instance_validation_contract", {})
    root_key = instance_contract.get("root_key")
    instance = document.get(root_key, {}) if isinstance(document, dict) else {}
    if not isinstance(instance, dict):
        return {"result": "INVALID", "diagnostics": ["methodology instance root must be a mapping"]}
    if instance.get("protocol") != instance_contract.get("protocol_binding"):
        errors.append("methodology instance protocol binding mismatch")

    findings = instance.get(instance_contract.get("finding_instances", {}).get("collection_key", "findings"), [])
    if findings is not None:
        if not isinstance(findings, list):
            errors.append("methodology instance findings must be a list")
        else:
            for index, finding in enumerate(findings):
                _validate_finding(method, finding, f"findings[{index}]", errors)

    review_key = instance_contract.get("review_instances", {}).get("root_key", "review")
    review = instance.get(review_key)
    if review is not None:
        if not isinstance(review, dict):
            errors.append("review instance must be a mapping")
        else:
            review_contract = instance_contract.get("review_instances", {})
            required = set(review_contract.get("required_fields", []))
            missing = sorted(field for field in required if field not in review)
            if missing:
                errors.append(f"review required fields missing: {', '.join(missing)}")
            records = _review_records(method)
            review_type = review.get("review_type")
            record = records.get(review_type)
            if record is None:
                errors.append("review type is absent or not allowed")
                record = {}
            pass_id = review.get("pass_id")
            if not isinstance(pass_id, str) or not pass_id:
                errors.append("review pass_id is required")
            binding = review.get("contract_binding")
            bound_contract: dict = {}
            required_binding = set(review_contract.get("contract_binding_required_fields", []))
            if not isinstance(binding, dict) or required_binding - set(binding):
                errors.append("review contract binding is incomplete")
            else:
                resolved = contracts.get(pass_id)
                if resolved is None:
                    errors.append("review pass contract is missing or ambiguous")
                else:
                    contract_path, bound_contract = resolved
                    identity = bound_contract.get("contract_identity", {})
                    if any((
                        binding.get("contract_id") != identity.get("contract_id"),
                        str(binding.get("version")) != str(identity.get("version")),
                        not isinstance(binding.get("sha256"), str),
                        isinstance(binding.get("sha256"), str) and not SHA256_RE.fullmatch(binding["sha256"]),
                        binding.get("sha256") != sha256(contract_path),
                    )):
                        errors.append("review contract identity, version or hash binding mismatch")

            review_findings = review.get("findings", [])
            if not isinstance(review_findings, list):
                errors.append("review findings must be a list")
            else:
                for index, finding in enumerate(review_findings):
                    _validate_finding(method, finding, f"review.findings[{index}]", errors)

            conclusions = review.get("review_conclusions")
            if not isinstance(conclusions, list) or len(conclusions) != 1:
                errors.append("review must declare exactly one conclusion")
                conclusion = None
            else:
                conclusion = conclusions[0]
                if conclusion not in set(record.get("allowed_conclusions", [])):
                    errors.append("review conclusion is not allowed for the declared review type")

            attacks = review.get("method_checks_or_attacks_attempted")
            if not isinstance(attacks, list):
                errors.append("review method checks or attacks must be a list")
                attacks = []
            if review_type == "ADVERSARIAL_REVIEW":
                if not attacks:
                    errors.append("adversarial review must record actual attack attempts")
                for index, attack in enumerate(attacks):
                    if not isinstance(attack, dict) or ATTACK_RECORD_FIELDS - set(attack):
                        errors.append(f"adversarial attack record is incomplete: {index}")
                        continue
                    if attack.get("attack_dimension") not in ATTACK_RECORD_DIMENSIONS:
                        errors.append(f"adversarial attack dimension is not allowed: {index}")
                    for field in ATTACK_RECORD_FIELDS - {"attack_dimension"}:
                        if not _present(attack.get(field)):
                            errors.append(f"adversarial attack field is nominal or empty: {field}: {index}")
                    target = str(attack.get("target_claim_or_assumption", "")).lower()
                    method_text = str(attack.get("attack_method", "")).lower()
                    scenario = str(attack.get("counterexample_or_failure_scenario", "")).lower()
                    evidence = attack.get("evidence_examined")
                    if target in {"candidate", "artifact", "acceptance criteria", "reviewed adversarially"} or len(target) < 12:
                        errors.append(f"adversarial attack lacks a specific target: {index}")
                    if len(method_text) < 12 or method_text in {"review", "attack", "test"}:
                        errors.append(f"adversarial attack lacks a meaningful method: {index}")
                    if len(scenario) < 16 or scenario in {"none", "not applicable", "n/a"}:
                        errors.append(f"adversarial attack lacks a counterexample or failure scenario: {index}")
                    if not isinstance(evidence, list) or not _string_list(evidence):
                        errors.append(f"adversarial attack lacks evidence examined: {index}")
                if conclusion == "SURVIVED_RECORDED_ADVERSARIAL_ATTACKS" and not attacks:
                    errors.append("adversarial survival conclusion has no meaningful attack")

            invalidity = conclusion == "INVALID_EXECUTION_AFTER_ROOT_CAUSE_AND_MATERIALITY_ANALYSIS"
            pass_results = review.get("pass_results")
            pass_contracts = method.get("review_contract", {}).get("pass_result_contracts", {})
            pass_result_contract = pass_contracts.get(pass_id)
            if pass_result_contract:
                if review_type not in set(pass_result_contract.get("disposition_review_types", [])):
                    errors.append("declared review type cannot produce the pass disposition")
                if not isinstance(pass_results, list) or len(pass_results) != 1:
                    errors.append("review must declare exactly one pass result")
                elif pass_results[0] not in set(pass_result_contract.get("permitted_results", [])):
                    errors.append("pass result is not permitted by the pass contract")
                elif conclusion is not None:
                    expected = pass_result_contract.get("mapping", {}).get(review_type, {}).get(conclusion)
                    if pass_results[0] != expected:
                        errors.append("review conclusion does not map to the declared pass result")
                bound_output = bound_contract.get("output_structure", {})
                if bound_output:
                    if review_type not in set(bound_output.get("disposition_review_types", [])):
                        errors.append("declared review type is not allowed by the bound pass contract")
                    if (
                        isinstance(pass_results, list)
                        and len(pass_results) == 1
                        and pass_results[0] not in set(bound_output.get("permitted_results", []))
                    ):
                        errors.append("pass result is not allowed by the bound pass contract")
                binding_contract = bound_contract.get("review_contract", {})
                if binding_contract:
                    allowed_types = set(binding_contract.get("allowed_review_types", []))
                    allowed_conclusions = set(binding_contract.get("allowed_conclusions_by_review_type", {}).get(review_type, []))
                    if review_type not in allowed_types:
                        errors.append("declared review type is not allowed by the bound pass contract")
                    if conclusion is not None and conclusion not in allowed_conclusions:
                        errors.append("review conclusion is not compatible with the bound pass contract")
                    mapping = binding_contract.get("conclusion_to_result", {}).get(review_type, {})
                    if isinstance(pass_results, list) and len(pass_results) == 1 and mapping and pass_results[0] != mapping.get(conclusion):
                        errors.append("review conclusion/result is not compatible with the bound pass contract")
                else:
                    errors.append("bound pass contract lacks review compatibility metadata")
                if isinstance(pass_results, list) and pass_results == ["INVALID_AUDIT_EXECUTION"]:
                    invalidity = True
            elif pass_results not in ([], None):
                errors.append("review declares a pass result without a methodology pass-result contract")

            deviations = review.get("deviations")
            if not isinstance(deviations, list):
                errors.append("review deviations must be a list")
                deviations = []
            if invalidity:
                if not deviations:
                    errors.append("invalidity conclusion requires causal, authority-impact and materiality analysis")
                required_deviation = set(review_contract.get("invalidity_analysis_required_fields", []))
                for index, deviation in enumerate(deviations):
                    if not isinstance(deviation, dict) or required_deviation - set(deviation):
                        errors.append(f"invalidity analysis fields missing: {index}")
                        continue
                    if deviation.get("root_cause_layer") not in ROOT_CAUSES:
                        errors.append(f"invalidity root cause is not allowed: {index}")
                    for field in (
                        "causal_analysis",
                        "authority_and_evidence_impact",
                        "materiality",
                        "execution_validity_conclusion",
                    ):
                        if not _present(deviation.get(field)):
                            errors.append(f"invalidity analysis is empty for {field}: {index}")

    return {"result": "VALID" if not errors else "INVALID", "diagnostics": errors}


def validate(root: Path) -> dict:
    errors: list[str] = []
    path = root / METHOD_REL
    if not path.is_file():
        return {"result": "INVALID", "diagnostics": ["audit methodology protocol missing"]}

    method = load(path).get("audit_methodology", {})
    if any((
        method.get("document_id") != "GOV-AUD-001-METHOD-001",
        str(method.get("version")) != "0.3.0",
        method.get("supersedes") != "GOV-AUD-001-METHOD-001/0.2.0",
        method.get("applies_to") != "NEW_OR_VERSIONED_GOV_AUD_001_FINDINGS_REVIEWS_AND_PROMPTS",
        method.get("historical_evidence_rule") != "COMPLETED_RUNS_REVIEWS_PROMPTS_INPUTS_OUTPUTS_MANIFESTS_AND_HASHES_REMAIN_IMMUTABLE",
    )):
        errors.append("methodology identity, version or prospective boundary mismatch")

    policy = method.get("policy_boundary", {})
    if policy != {
        "kernel_amendment": False,
        "gov_7_policy_adopted": False,
        "gov_7_activated": False,
        "temporary_operating_control_only": True,
    }:
        errors.append("methodology policy boundary mismatch")

    finding = method.get("finding_contract", {})
    if set(finding.get("finding_basis", [])) != FINDING_BASES:
        errors.append("finding basis taxonomy mismatch")
    required_finding_fields = {
        "finding_id",
        "statement_and_scope",
        "finding_basis",
        "evidence_refs_or_reasoning",
        "support_classification",
        "materiality",
        "disposition_class",
        "traceability",
    }
    if set(finding.get("required_for_material_findings", [])) != required_finding_fields:
        errors.append("material finding contract mismatch")
    inference = finding.get("model_inference_only", {})
    if any((
        inference.get("must_be_explicit") is not True,
        inference.get("may_be_represented_as_verified_fact") is not False,
        not set(inference.get("required_follow_up_one_or_more", [])) >= {
            "ADVERSARIAL_TESTING",
            "EXTERNAL_VALIDATION",
            "EMPIRICAL_EVIDENCE",
            "PROJECT_OWNER_DISPOSITION",
        },
    )):
        errors.append("MODEL_INFERENCE_ONLY marking or follow-up contract mismatch")
    if set(finding.get("support_classification", [])) != SUPPORT_CLASSIFICATIONS:
        errors.append("finding support classification taxonomy mismatch")

    deviation = method.get("deviation_and_validity_contract", {})
    if deviation.get("required_reasoning_sequence") != VALIDITY_SEQUENCE:
        errors.append("root-cause-before-invalidity sequence mismatch")
    if set(deviation.get("root_cause_layer", [])) != ROOT_CAUSES:
        errors.append("root cause taxonomy mismatch")
    if set(deviation.get("agent_action_value", [])) != {"BENEFICIAL", "NEUTRAL", "HARMFUL"}:
        errors.append("agent action value taxonomy mismatch")
    if set(deviation.get("formal_conformance", [])) != {"CONFORMANT", "NONCONFORMANT", "AMBIGUOUS"}:
        errors.append("formal conformance taxonomy mismatch")
    invalidity = str(deviation.get("invalidity_rule", "")).lower()
    if "deviation alone is insufficient" not in invalidity or "material authority or evidence impact" not in invalidity:
        errors.append("invalidity conclusion guard missing")

    review = method.get("review_contract", {})
    if set(review.get("required_sections", [])) != REVIEW_SECTIONS:
        errors.append("review contract sections mismatch")
    records = review.get("review_types", [])
    if not isinstance(records, list) or {item.get("review_type") for item in records if isinstance(item, dict)} != REVIEW_TYPES:
        errors.append("review type identity mismatch")
    for record in records if isinstance(records, list) else []:
        if not isinstance(record, dict):
            errors.append("review type record must be a mapping")
            continue
        missing = REVIEW_FIELDS - set(record)
        if missing:
            errors.append(f"review type required fields missing: {record.get('review_type')}")
        for field in ("allowed_conclusions", "minimum_evidence", "must_not_claim"):
            if not _string_list(record.get(field)):
                errors.append(f"review type {field} invalid: {record.get('review_type')}")
        if not isinstance(record.get("purpose"), str) or not record.get("purpose"):
            errors.append(f"review type purpose missing: {record.get('review_type')}")
        if not isinstance(record.get("required_independence"), str) or not record.get("required_independence"):
            errors.append(f"review type independence missing: {record.get('review_type')}")
        if not isinstance(record.get("may_produce_pass_disposition"), bool):
            errors.append(f"review type pass-disposition flag missing: {record.get('review_type')}")
    adversarial = next((item for item in records if isinstance(item, dict) and item.get("review_type") == "ADVERSARIAL_REVIEW"), {})
    if adversarial.get("method") != "ATTEMPT_TO_REFUTE_THE_CANDIDATE":
        errors.append("adversarial review does not require attempted refutation")
    if set(adversarial.get("required_attack_dimensions_when_applicable", [])) != ATTACK_DIMENSIONS:
        errors.append("adversarial attack dimensions mismatch")
    survival = str(adversarial.get("survival_rule", "")).lower()
    if "attempted attacks" not in survival or "no finding is required" not in survival:
        errors.append("adversarial survival or no-invented-findings rule missing")
    pass_07 = review.get("pass_result_contracts", {}).get("PASS-07", {})
    if any((
        set(pass_07.get("disposition_review_types", [])) != {
            "INDEPENDENT_SUBSTANTIVE_REVIEW",
            "ADVERSARIAL_REVIEW",
        },
        set(pass_07.get("auxiliary_review_types_without_disposition_authority", [])) != {
            "DETERMINISTIC_VALIDATION",
            "TARGETED_CONFIRMATION",
        },
        set(pass_07.get("permitted_results", [])) != PASS_07_RESULTS,
        pass_07.get("insufficient_evidence_result") != "INSUFFICIENT_EVIDENCE_FOR_PASS_07_DISPOSITION",
        pass_07.get("exactly_one_result") is not True,
    )):
        errors.append("PASS-07 result contract mismatch")
    mappings = pass_07.get("mapping", {})
    for review_type in ("INDEPENDENT_SUBSTANTIVE_REVIEW", "ADVERSARIAL_REVIEW"):
        allowed = set(_review_records(method).get(review_type, {}).get("allowed_conclusions", []))
        if set(mappings.get(review_type, {})) != allowed:
            errors.append(f"PASS-07 conclusion mapping incomplete: {review_type}")
    if any(
        _review_records(method).get(review_type, {}).get("may_produce_pass_disposition") is not expected
        for review_type, expected in {
            "DETERMINISTIC_VALIDATION": False,
            "TARGETED_CONFIRMATION": False,
            "INDEPENDENT_SUBSTANTIVE_REVIEW": True,
            "ADVERSARIAL_REVIEW": True,
        }.items()
    ):
        errors.append("review-type pass-disposition eligibility mismatch")

    materiality = method.get("materiality", {})
    if set(materiality.get("blocking_when_materially_affecting_one_or_more", [])) != BLOCKING_DIMENSIONS:
        errors.append("blocking materiality dimensions mismatch")
    if set(materiality.get("non_blocking_classes", [])) != NON_BLOCKING_CLASSES:
        errors.append("non-blocking classification mismatch")
    non_blocking_rule = str(materiality.get("non_blocking_rule", "")).lower()
    if "do not block" not in non_blocking_rule or "blocking dimension" not in non_blocking_rule:
        errors.append("bounded non-blocking materiality rule missing")
    instance_contract = method.get("instance_validation_contract", {})
    if any((
        instance_contract.get("root_key") != "methodology_instance",
        instance_contract.get("protocol_binding") != "GOV-AUD-001-METHOD-001/0.3.0",
        instance_contract.get("finding_instances", {}).get("collection_key") != "findings",
        instance_contract.get("review_instances", {}).get("root_key") != "review",
        instance_contract.get("review_instances", {}).get("exactly_one_review_conclusion") is not True,
        instance_contract.get("review_instances", {}).get("exactly_one_pass_result_for_pass_disposition") is not True,
        instance_contract.get("review_instances", {}).get("adversarial_attack_attempt_required") is not True,
    )):
        errors.append("bounded instance-validation contract mismatch")
    if set(instance_contract.get("review_instances", {}).get("adversarial_attack_record_required_fields", [])) != ATTACK_RECORD_FIELDS:
        errors.append("adversarial attack record field contract mismatch")
    if set(instance_contract.get("review_instances", {}).get("adversarial_attack_dimensions", [])) != ATTACK_RECORD_DIMENSIONS:
        errors.append("adversarial attack dimension contract mismatch")
    discovery = method.get("pass_contract_discovery", {})
    contracts, contract_errors = _discover_pass_contracts(root)
    errors.extend(contract_errors)
    if any((
        discovery.get("canonical_root") != str(AUDIT_REL / "passes"),
        discovery.get("contract_filename") != "contract.yaml",
        not contracts,
    )):
        errors.append("generic pass-contract discovery contract mismatch")

    conflict = method.get("temporary_instruction_conflict_control", {})
    if any((
        conflict.get("run_rule") != RUN_RULE,
        conflict.get("reviewer_rule") != REVIEWER_RULE,
        conflict.get("future_route") != "HP-MPROP-006",
        conflict.get("not_an_adopted_policy") is not True,
        conflict.get("not_a_kernel_amendment") is not True,
    )):
        errors.append("temporary instruction-conflict control mismatch")

    identity = method.get("canonical_identity_control", {})
    if identity.get("rule") != IDENTITY_RULE or identity.get("second_identity_authority_created") is not False:
        errors.append("canonical identity-resolution control mismatch")
    if len(identity.get("allocation_evidence_required", [])) != 4:
        errors.append("identity-resolution evidence contract mismatch")

    traceability = method.get("finding_traceability", {})
    if traceability.get("required_chain") != TRACEABILITY_CHAIN:
        errors.append("finding traceability chain mismatch")
    correction_map = traceability.get("correction_map", [])
    if not isinstance(correction_map, list) or len(correction_map) < 12:
        errors.append("methodology correction traceability map incomplete")
    else:
        for index, item in enumerate(correction_map):
            if not isinstance(item, dict) or not all(
                item.get(field) is not None
                for field in ("observed_problem", "methodology_requirement", "changed_canonical_artifact", "validator_or_review_control", "validation_evidence")
            ):
                errors.append(f"methodology correction traceability item incomplete: {index}")

    report_path = root / AUDIT_REL / "09-methodology-bounded-correction-validation.yaml"
    if not report_path.is_file():
        errors.append("methodology correction validation report missing")
    else:
        report = load(report_path).get("validation_report", {})
        resolution = report.get("canonical_identity_resolution", {})
        resolved_ids = {
            item.get("identity")
            for item in resolution.get("resolved", [])
            if isinstance(item, dict)
        }
        if any((
            report.get("record_id") != "GOV-AUD-VAL-005",
            report.get("methodology_protocol") != "GOV-AUD-001-METHOD-001/0.3.0",
            report.get("status") != "VALIDATED",
            report.get("result") != "VALID",
            resolution.get("rule") != "NEVER_ASSIGN_FROM_CHAT_MEMORY_RESOLVE_FROM_CANONICAL_REGISTRY_VERIFY_UNUSED_RECORD_EVIDENCE_BEFORE_BINDING",
            not {
                "HP-PROMPT-030/0.3.0",
                "GOV-AUD-VAL-005",
                "HP-MPROP-007",
                "GOV-AUD-001-METHOD-001/0.3.0",
            } <= resolved_ids,
            resolution.get("new_run_identity_created") is not False,
        )):
            errors.append("methodology validation or canonical identity-resolution evidence mismatch")
        authority = report.get("authority_boundary", {})
        if any(value is not False for value in authority.values()):
            errors.append("methodology validation report crossed authority boundary")

    templates = [
        root / AUDIT_REL / "prompts/templates/GOV-AUD-PROMPT-020-pass-02-cross-layer-self-hosting-v0.2.0.md",
        root / AUDIT_REL / "prompts/templates/GOV-AUD-PROMPT-070-pass-07-independent-evaluation-v0.2.0.md",
    ]
    for template in templates:
        if not template.is_file():
            errors.append(f"corrected prompt template missing: {template.name}")
            continue
        text = template.read_text()
        for required in (IDENTITY_RULE, REVIEWER_RULE if "070-" in template.name else RUN_RULE):
            if required not in text:
                errors.append(f"compact methodology control missing from template: {template.name}")
    if templates[1].is_file():
        review_text = templates[1].read_text()
        for review_type in REVIEW_TYPES:
            if review_type not in review_text:
                errors.append(f"review type missing from corrected review template: {review_type}")
        if "genuinely attempt to refute" not in review_text.lower():
            errors.append("corrected review template lacks adversarial refutation requirement")
        if "cannot independently produce the pass-07 disposition" not in review_text.lower():
            errors.append("corrected review template permits auxiliary review types to dispose PASS-07")

    backlog_path = root / "governance/methodology/METHODOLOGY_BACKLOG.md"
    if not backlog_path.is_file():
        errors.append("canonical methodology backlog missing")
    else:
        backlog_text = backlog_path.read_text()
        for required in (
            "HP-MPROP-007",
            "OWNER_ACCEPTED_FOR_FUTURE_AUDIT_CLARIFICATION",
            "AFTER_CHECKPOINT_A_BEFORE_PASS_03",
            "observable execution event",
            "selective retrieval",
            "recurrence reduction",
            "bounded contract clarification after CHECKPOINT-A",
            "before PASS-03",
        ):
            if required not in backlog_text:
                errors.append(f"execution-insight proposal requirement missing: {required}")
        try:
            proposal_section = backlog_text.split("## HP-MPROP-007", 1)[1]
            proposal_yaml = proposal_section.split("```yaml", 1)[1].split("```", 1)[0]
            proposal = loads(proposal_yaml, str(backlog_path)).get("proposal", {})
        except (IndexError, ValueError) as exc:
            errors.append(f"execution-insight proposal YAML is unavailable or invalid: {exc}")
            proposal = {}
        if any((
            proposal.get("id") != "HP-MPROP-007",
            proposal.get("classification") != "METHODOLOGY_PROPOSAL",
            proposal.get("scope") != "GOV-AUD-001",
            proposal.get("status") != "OWNER_ACCEPTED_FOR_FUTURE_AUDIT_CLARIFICATION",
            proposal.get("implementation_status") != "NOT_STARTED",
            proposal.get("incorporation_point") != "AFTER_CHECKPOINT_A_BEFORE_PASS_03",
            proposal.get("target_passes") != ["PASS-03", "PASS-04", "PASS-06", "PASS-07"],
            proposal.get("verification_states") != ["HYPOTHESIS_PENDING_VERIFICATION", "CONFIRMED", "REFUTED", "PARTIALLY_CONFIRMED", "UNRESOLVED"],
        )):
            errors.append("execution-insight proposal classification, scope, status or pipeline mismatch")
        allocation = proposal.get("future_allocation", {})
        if set(allocation) != {"PASS-03", "PASS-04", "PASS-06", "PASS-07"}:
            errors.append("execution-insight proposal pass allocation mismatch")
        boundaries = " ".join(proposal.get("boundaries", [])).lower()
        for required_boundary in (
            "no hidden chain-of-thought",
            "repository evidence remains canonical",
            "traces are non-authoritative",
            "hypotheses remain distinct",
            "no silent procedural promotion",
            "no automatic governance or kernel modification",
            "no automatic risk acceptance",
            "material learning requires human or independent disposition",
            "low-value and duplicate learning",
            "recurrence reduction and retrieval usefulness",
        ):
            if required_boundary not in boundaries:
                errors.append(f"execution-insight proposal boundary missing: {required_boundary}")
        proposal_text = proposal_section.lower()
        for required in ("planned verification", "partially confirmed", "unresolved conclusion", "evidence-aware triage", "privacy", "redaction", "retention", "manual-fallback", "executor self-assertion", "candidate_destinations", "promotion_states", "tooling_boundary"):
            if required not in proposal_text:
                errors.append(f"execution-insight proposal completeness requirement missing: {required}")

    pass_02_root = root / RUN_REL
    if pass_02_root.exists():
        for relative, expected in P02_HASHES.items():
            candidate = pass_02_root / relative
            if not candidate.is_file() or sha256(candidate) != expected:
                errors.append(f"immutable PASS-02 R1 custody mismatch: {relative}")

    status_path = root / AUDIT_REL / "02-audit-status.yaml"
    if status_path.is_file():
        audit_status = load(status_path).get("audit", {})
        execution = audit_status.get("pass_02_execution", {})
        execution_crossed = bool(execution) and any((
            execution.get("pass_02_accepted") is not False,
            execution.get("checkpoint_a_completed") is not False,
            execution.get("pass_03_authorized_or_executed") is not False,
            execution.get("gov_7_activated") is not False,
        ))
        if execution_crossed or audit_status.get("implementation_authorized") is not False:
            errors.append("methodology correction crossed audit authority boundary")

    return {"result": "VALID" if not errors else "INVALID", "diagnostics": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--instance", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    result = validate(root)
    if result["result"] == "VALID" and args.instance is not None:
        instance_path = args.instance if args.instance.is_absolute() else root / args.instance
        result = validate_instance(root, instance_path.resolve())
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["result"] == "VALID" else 1


if __name__ == "__main__":
    raise SystemExit(main())
