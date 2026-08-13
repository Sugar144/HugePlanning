#!/usr/bin/env python3
"""Validate the completed GOV-AUD-001 PASS-03 source execution and review package."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib.strict_yaml import load, loads


ROOT = Path(__file__).resolve().parents[2]
AUDIT_REL = Path("governance/audits/GOV-AUD-001-gov7-enablement")
RUN_REL = AUDIT_REL / "runs/GOV-AUD-001-P03-R1"
SUCCESS = "EXECUTED_VALIDATED_PENDING_INDEPENDENT_ADVERSARIAL_REVIEW_AND_PROJECT_OWNER_DISPOSITION"
OUTPUTS = {
    "01-observable-event-requirements.yaml": "observable_event_requirements",
    "02-evidence-and-authority-model.yaml": "evidence_and_authority_model",
    "03-learning-lifecycle-and-state-machine.yaml": "learning_lifecycle_and_state_machine",
    "04-candidate-routing-and-promotion-model.yaml": "candidate_routing_and_promotion_model",
    "05-selective-retrieval-requirements.yaml": "selective_retrieval_requirements",
    "06-effectiveness-and-burden-metrics.yaml": "effectiveness_and_burden_metrics",
    "07-privacy-retention-and-rollback-requirements.yaml": "privacy_retention_and_rollback_requirements",
    "08-tooling-neutral-capability-model.yaml": "tooling_neutral_capability_model",
    "09-risks-open-questions-and-pass-04-handoff.md": None,
}
EVIDENCE_CLASSES = {
    "OPERATIONAL_TRACE", "VISIBLE_MODEL_STATEMENT", "MODEL_INFERENCE", "HYPOTHESIS",
    "PLANNED_VERIFICATION", "VERIFICATION_RESULT", "REPOSITORY_EVIDENCE",
    "FORMAL_RUN_EVIDENCE", "LEARNING_CANDIDATE", "ACCEPTED_DURABLE_LEARNING",
    "PROCEDURAL_CONTROL", "INDEPENDENTLY_VALIDATED_CONTROL", "DEMONSTRATED_EFFECTIVENESS",
    "OWNER_DECISION",
}
VERIFICATION_STATES = {
    "HYPOTHESIS_PENDING_VERIFICATION", "CONFIRMED", "REFUTED",
    "PARTIALLY_CONFIRMED", "UNRESOLVED",
}
DESTINATIONS = {
    "OPERATIONAL_OBSERVATION", "FORMAL_RUN_EVIDENCE", "FAILURE_OR_LESSON_RECORD",
    "METHODOLOGY_PROPOSAL", "OWNER_DECISION_CANDIDATE", "TOOLING_CANDIDATE",
    "PROMPT_CANDIDATE", "SKILL_CANDIDATE", "VALIDATOR_CANDIDATE",
    "REGRESSION_TEST_CANDIDATE", "PROCEDURAL_CONTROL_CANDIDATE", "RESEARCH_REQUIRED",
    "DUPLICATE_OR_LINKED_EXISTING_RECORD", "DISCARD",
}
PROMOTION_STATES = {"CAPTURED", "ACCEPTED", "IMPLEMENTED", "VALIDATED", "SHOWN_EFFECTIVE"}
CAPABILITIES = {
    "TRACE_CAPTURE", "INSIGHT_EXTRACTION", "EVIDENCE_VERIFICATION", "CANDIDATE_TRIAGE",
    "PROCEDURAL_PROMOTION", "SELECTIVE_RETRIEVAL", "EFFECTIVENESS_EVALUATION",
}
METRICS = {
    "recurrence_rate", "repeated_owner_corrections", "repeated_manual_repairs",
    "correction_cycles", "promoted_lessons", "independently_validated_controls",
    "failures_prevented", "relevant_retrieval_rate", "irrelevant_context_rate",
    "false_learning_rate", "duplicate_learning_rate", "stale_learning_rate",
    "discarded_noise_rate", "rollback_frequency", "token_burden",
    "execution_time_burden", "owner_burden",
}
ATTACKS = {
    "false_learning", "unsupported_promotion", "authority_escalation", "privacy_leak",
    "telemetry_overcollection", "irrelevant_context", "stale_learning", "contradiction",
    "metric_gaming", "bureaucracy_owner_burden", "vendor_lock_in_or_premature_tool_selection",
    "rollback_deletion_failure", "unavailable_observability",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def package_hash(items: list[dict]) -> str:
    lines = "".join(
        f"{item['sha256']}  {item['path']}\n"
        for item in sorted(items, key=lambda item: item["path"])
    )
    return hashlib.sha256(lines.encode()).hexdigest()


def frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    if not text.startswith("---\n") or (end := text.find("\n---\n", 4)) < 0:
        raise ValueError(f"{path}: missing front matter")
    return loads(text[4:end], str(path)), text[end + 5:]


def validate(root: Path = ROOT) -> dict:
    errors: list[str] = []
    run = root / RUN_REL
    required = [
        "authorization/owner-authorization.yaml", "input/input-manifest.yaml",
        "prompt/GOV-AUD-PROMPT-031-pass-03-execution-v0.1.0.md", "manifest.yaml",
        "evaluation/pass-03-validation-report.yaml", "review-package/manifest.yaml",
    ] + [f"output/{name}" for name in OUTPUTS]
    for relative in required:
        if not (run / relative).is_file():
            errors.append(f"required PASS-03 artifact missing: {relative}")
    if errors:
        return {"result": "INVALID", "diagnostics": errors}

    authorization = load(run / required[0])["authorization"]
    input_manifest = load(run / required[1])["manifest"]
    if any((
        authorization.get("authorization_id") != "GOV-AUD-AUTH-003",
        authorization.get("authorized_run") != "GOV-AUD-001-P03-R1",
        authorization.get("authorized_pass") != "PASS-03",
        authorization.get("execution_count_limit") != 1,
        authorization.get("execution_count_consumed") != 0,
        authorization.get("status") != "AUTHORIZED_NOT_YET_CONSUMED",
        authorization.get("starting_local_head") != "e5bdeeafdc2278a2baef67c659eef4a8eab5d867",
        authorization.get("starting_remote_head") != "e5bdeeafdc2278a2baef67c659eef4a8eab5d867",
    )):
        errors.append("PASS-03 authorization identity, count or starting state mismatch")
    prompt_path = run / "prompt/GOV-AUD-PROMPT-031-pass-03-execution-v0.1.0.md"
    catalog_prompt = root / "governance/prompts/orchestration/HP-PROMPT-035-execute-gov-aud-001-pass-03-v0.1.0.md"
    if sha256(prompt_path) != input_manifest.get("execution_prompt_sha256") or sha256(prompt_path) != authorization.get("prompt_sha256"):
        errors.append("execution prompt hash mismatch")
    if not catalog_prompt.is_file() or sha256(catalog_prompt) != input_manifest.get("catalog_prompt_sha256") or sha256(catalog_prompt) != authorization.get("catalog_prompt_sha256"):
        errors.append("catalog prompt custody or hash mismatch")
    if sha256(run / "authorization/owner-authorization.yaml") != input_manifest.get("authorization_sha256"):
        errors.append("authorization hash mismatch")
    if input_manifest.get("member_count") != len(input_manifest.get("inputs", [])) or input_manifest.get("member_count") != 33:
        errors.append("input member count mismatch")
    starting_head = input_manifest.get("starting_local_head")
    for item in input_manifest.get("inputs", []):
        result = subprocess.run(
            ["git", "-C", str(root), "show", f"{starting_head}:{item['path']}"],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False,
        )
        actual = hashlib.sha256(result.stdout).hexdigest() if result.returncode == 0 else None
        if actual != item.get("sha256"):
            errors.append(f"input identity mismatch: {item['path']}")
    if package_hash(input_manifest.get("inputs", [])) != input_manifest.get("input_package_sha256"):
        errors.append("input package hash mismatch")
    if input_manifest.get("input_package_sha256") != authorization.get("evidence_package_sha256"):
        errors.append("authorization does not bind the input evidence package")

    docs: dict[str, dict] = {}
    for index, (name, root_key) in enumerate(OUTPUTS.items(), 1):
        path = run / "output" / name
        if root_key:
            doc = load(path).get(root_key, {})
        else:
            metadata, body = frontmatter(path)
            doc = {"metadata": metadata, "body": body}
        docs[name] = doc
        artifact_id = doc.get("artifact_id") if root_key else doc["metadata"].get("artifact_id")
        if artifact_id != f"GOV-AUD-P03-OUT-{index:03d}":
            errors.append(f"output artifact identity mismatch: {name}")

    observable = docs["01-observable-event-requirements.yaml"]
    fields = {item.get("field"): item for item in observable.get("observable_fields", [])}
    required_fields = {
        "run_id", "session_id", "role", "execution_mode", "prompt_id", "prompt_version",
        "prompt_path", "prompt_sha256", "input_packages", "model_identity", "reasoning_mode",
        "changed_files", "retry_count", "correction_cycle_count", "owner_interventions",
        "stop_reason", "output_inventory", "duration", "input_tokens", "output_tokens", "monetary_cost",
    }
    if not required_fields <= fields.keys() or set(observable.get("availability_classes", {})) != {"REQUIRED", "OPTIONAL", "DERIVED", "UNAVAILABLE"}:
        errors.append("observable field or availability coverage mismatch")
    if observable.get("authority_boundary", {}).get("hidden_chain_of_thought_capture") != "PROHIBITED":
        errors.append("hidden chain-of-thought prohibition missing")

    evidence = docs["02-evidence-and-authority-model.yaml"]
    if {item.get("class") for item in evidence.get("evidence_classes", [])} != EVIDENCE_CLASSES:
        errors.append("evidence class distinction mismatch")
    if evidence.get("authority_boundary", {}).get("repository_evidence_canonical") is False:
        errors.append("repository canonicality weakened")
    evidence_text = json.dumps(evidence)
    for token in ("OPERATIONAL_TRACE_AS_REPOSITORY_EVIDENCE", "EXECUTOR_ASSERTION_AS_VERIFICATION_RESULT", "IMPLEMENTED_CONTROL_AS_VALIDATED_CONTROL"):
        if token not in evidence_text:
            errors.append(f"prohibited evidence conflation missing: {token}")

    lifecycle = docs["03-learning-lifecycle-and-state-machine.yaml"]
    states = {item.get("state") for item in lifecycle.get("states", [])}
    if not VERIFICATION_STATES <= states:
        errors.append("verification state coverage mismatch")
    transitions = {(item.get("from"), item.get("to")) for item in lifecycle.get("valid_transitions", [])}
    invalid = {(item.get("from"), item.get("to")) for item in lifecycle.get("invalid_transitions", [])}
    for pair in (("PLANNED_VERIFICATION", "CONFIRMED"), ("PLANNED_VERIFICATION", "REFUTED"), ("PLANNED_VERIFICATION", "PARTIALLY_CONFIRMED"), ("PLANNED_VERIFICATION", "UNRESOLVED")):
        if pair not in transitions:
            errors.append(f"valid verification transition missing: {pair}")
    for pair in (("HYPOTHESIS_PENDING_VERIFICATION", "LEARNING_CANDIDATE"), ("REFUTED", "LEARNING_CANDIDATE"), ("UNRESOLVED", "PROCEDURAL_PROMOTION")):
        if pair not in invalid:
            errors.append(f"invalid lifecycle transition missing: {pair}")
    verification_required = set(lifecycle.get("verification_evidence", {}).get("required_fields", []))
    if not {"evidence_references", "verification_method", "verifier_identity_or_mechanism", "confidence_or_limitation", "contradictions_checked", "unsupported_portions"} <= verification_required:
        errors.append("verification evidence requirements incomplete")

    routing = docs["04-candidate-routing-and-promotion-model.yaml"]
    if {item.get("destination") for item in routing.get("destinations", [])} != DESTINATIONS:
        errors.append("candidate destination coverage mismatch")
    if {item.get("state") for item in routing.get("promotion_states", [])} != PROMOTION_STATES:
        errors.append("promotion state distinction mismatch")
    if set(routing.get("prohibited_triage_decisions", [])) != {"scope", "constitutional_matter", "risk_acceptance", "ratification", "phase_transition", "implementation_approval", "release", "adoption"}:
        errors.append("candidate triage authority boundary mismatch")

    retrieval = docs["05-selective-retrieval-requirements.yaml"]
    if len(set(retrieval.get("dimensions", []))) < 12:
        errors.append("selective retrieval dimensions incomplete")
    if retrieval.get("authority_boundary", {}).get("global_injection_of_all_learning") != "PROHIBITED":
        errors.append("global learning injection prohibition missing")
    if retrieval.get("stale_conflict_fallback_controls", {}).get("nothing_relevant", {}).get("action") != "RETURN_EMPTY_PACKAGE":
        errors.append("retrieval no-result fallback mismatch")

    metrics = docs["06-effectiveness-and-burden-metrics.yaml"]
    if {item.get("metric") for item in metrics.get("metrics", [])} != METRICS:
        errors.append("effectiveness and burden metric coverage mismatch")
    if len(metrics.get("anti_gaming_controls", [])) < 8 or "record count" not in metrics.get("success_rule", ""):
        errors.append("metric anti-gaming or volume-is-not-success rule missing")

    privacy = docs["07-privacy-retention-and-rollback-requirements.yaml"]
    if privacy.get("authority_boundary", {}).get("hidden_chain_of_thought_capture") != "PROHIBITED" or privacy.get("authority_boundary", {}).get("creates_new_privacy_authority") is not False:
        errors.append("privacy authority or hidden-reasoning boundary mismatch")
    for key in ("minimization", "redaction", "retention", "deletion", "rollback", "disablement", "manual_fallback", "failure_safe_behavior"):
        if not privacy.get(key):
            errors.append(f"privacy lifecycle control missing: {key}")

    capability = docs["08-tooling-neutral-capability-model.yaml"]
    if {item.get("capability") for item in capability.get("separated_capabilities", [])} != CAPABILITIES:
        errors.append("tooling-neutral capability separation mismatch")
    if capability.get("present_disposition", {}).get("selected_solution") != "NONE" or capability.get("present_disposition", {}).get("pass_04_authorized_or_executed") is not False:
        errors.append("premature tooling selection or PASS-04 authority")
    if len(capability.get("prohibited_selections", [])) != 9:
        errors.append("prohibited tooling selection coverage mismatch")

    handoff = docs["09-risks-open-questions-and-pass-04-handoff.md"]
    for heading in ("## Evidence boundary", "## Material risks and unresolved questions", "## Bounded PASS-04 comparison contract", "## Bounded source self-critique", "## Exact handoff state"):
        if heading not in handoff["body"]:
            errors.append(f"PASS-04 handoff section missing: {heading}")
    if handoff["metadata"].get("tool_selected") is not False or handoff["metadata"].get("pass_04_prepared_or_executed") is not False:
        errors.append("PASS-04 handoff selected tooling or executed PASS-04")

    manifest = load(run / "manifest.yaml")
    if manifest.get("run", {}).get("status") != SUCCESS or manifest.get("run", {}).get("execution_count_consumed") != 1:
        errors.append("PASS-03 run terminal source status mismatch")
    if manifest.get("authority_boundary", {}).get("pass_03_accepted") is not False or manifest.get("authority_boundary", {}).get("pass_04_authorized_or_executed") is not False:
        errors.append("PASS-03 manifest authority boundary mismatch")
    output_records = manifest.get("output_contract", {}).get("required_outputs", [])
    if len(output_records) != 9:
        errors.append("PASS-03 manifest output count mismatch")
    for item in output_records:
        path = root / item.get("path", "")
        if not path.is_file() or sha256(path) != item.get("sha256"):
            errors.append(f"PASS-03 output custody or hash mismatch: {item.get('path')}")

    validation = load(run / "evaluation/pass-03-validation-report.yaml").get("validation_report", {})
    if validation.get("result") != "VALID" or validation.get("evidence_class") != "SOURCE_RUN_DETERMINISTIC_VALIDATION_NOT_INDEPENDENT_ADVERSARIAL_REVIEW":
        errors.append("PASS-03 deterministic validation report mismatch")
    if validation.get("self_critique", {}).get("independent_review_performed") is not False:
        errors.append("source self-critique conflated with independent review")

    review = load(run / "review-package/manifest.yaml").get("review_package", {})
    if review.get("status") != "PREPARED_IMMUTABLE_NOT_REVIEWED" or set(review.get("attack_dimensions", [])) != ATTACKS:
        errors.append("adversarial review package state or attack coverage mismatch")
    members = review.get("members", [])
    if review.get("member_count") != len(members):
        errors.append("adversarial review package member count mismatch")
    for item in members:
        path = root / item.get("path", "")
        if not path.is_file() or sha256(path) != item.get("sha256"):
            errors.append(f"adversarial review package member hash mismatch: {item.get('path')}")
    if package_hash(members) != review.get("package_sha256"):
        errors.append("adversarial review package aggregate hash mismatch")

    output_text = "\n".join((run / "output" / name).read_text() for name in OUTPUTS)
    if re.search(r"hidden.chain.of.thought[^\n]{0,80}(required|enabled|collect(ed|ion)?:? true)", output_text, re.I):
        errors.append("hidden chain-of-thought collection requirement detected")
    return {"result": "VALID" if not errors else "INVALID", "diagnostics": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    result = validate(args.root.resolve())
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["result"] == "VALID" else 1


if __name__ == "__main__":
    raise SystemExit(main())
