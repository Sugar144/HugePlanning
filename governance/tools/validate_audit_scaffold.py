#!/usr/bin/env python3
"""Validate the GOV-AUD-001 scaffold and its first reachable lifecycle state."""

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


AUDIT_REL = Path("governance/audits/GOV-AUD-001-gov7-enablement")
PROMPT_HASH = "7ea731bb822d88328c26bfe69b5280a84a37153bc525f963d051fb74b6033b07"
CORRECTION_PROMPT_HASH = "7b180f5c96a75ab2203efe2de3c10e31d985c4f9d17b26aea569119f5c4edc5d"
PASS_IDS = [f"PASS-{number:02d}" for number in range(1, 8)]
SCAFFOLD_PROMPT_IDS = ["GOV-AUD-PROMPT-000"] + [f"GOV-AUD-PROMPT-{number:03d}" for number in range(10, 71, 10)]
RUN_ID = "GOV-AUD-001-P01-R1"
RUN_REL = AUDIT_REL / "runs" / RUN_ID
CORRECTION_ID = "GOV-AUD-001-P01-R1-C1"
CORRECTION_REL = RUN_REL / "corrections" / CORRECTION_ID
PASS_01_EXECUTED_STATUS = "EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION"
AUDIT_IN_PROGRESS_STATUS = "IN_PROGRESS_PASS_01_EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION"
OUTPUT_HASHES = {
    "01-verified-capability-inventory.yaml": "0e1ae26cfd8201e781768eec81045c056b1bc1cd557b0ab1f9fbcae1d47cb124",
    "02-repetition-waste-and-burden-analysis.md": "57cbd6fc8d151d6c338a14c9c6f51e702f9a8519136d5dde5b2d20b2327f900f",
    "03-ranked-gap-register.yaml": "8a485a3df850d6f9b37c4490435980715ddd84c689567ad3a94be89dca674cde",
    "04-pass-01-findings-and-handoff.md": "fd3e035812150b61f1dc54ad33412d5d8c09dcb31abe5a8ddaebd34e8323d2ff",
}
LABELS = ["VERIFIED_FACT", "INFERENCE", "PROPOSAL", "RECOMMENDATION", "OWNER_DECISION_REQUIRED", "DEFERRED", "REJECTED"]
PRINCIPLES = {
    "repository_first_gap_driven", "prompt_economy", "ai_first_effort",
    "whole_work_unit", "strategy_neutrality", "relationship_model_neutrality",
    "controlled_self_hosting", "open_tool_discovery",
}
REQUIRED_CONTRACT_FIELDS = {
    "id", "title", "status", "purpose", "authority", "required_predecessors",
    "checkpoint_dependency", "governance_phase_prerequisites", "canonical_inputs",
    "read_only_repository_scope", "permitted_external_research", "mandatory_principles",
    "required_questions", "required_outputs", "output_structure", "required_evidence",
    "validation", "stopping_conditions", "prohibited_actions", "prohibited_claims",
    "model_class_recommendation", "ai_first_effort_dimensions", "correction_protocol",
    "handoff_to_next_pass",
}
EXPECTED_PREDECESSORS = {
    "PASS-01": [], "PASS-02": ["PASS-01"], "PASS-03": ["CHECKPOINT-A"],
    "PASS-04": ["PASS-03"], "PASS-05": ["CHECKPOINT-B"],
    "PASS-06": ["PASS-05"], "PASS-07": ["PASS-06"],
}
EXPECTED_CHECKPOINT = {
    "PASS-01": None, "PASS-02": None, "PASS-03": "CHECKPOINT-A",
    "PASS-04": "CHECKPOINT-A", "PASS-05": "CHECKPOINT-B",
    "PASS-06": "CHECKPOINT-B", "PASS-07": "CHECKPOINT-B",
}
TEMPLATE_NAMES = {
    "PASS-01": "GOV-AUD-PROMPT-010-pass-01-capability-gap-v0.1.0.md",
    "PASS-02": "GOV-AUD-PROMPT-020-pass-02-cross-layer-self-hosting-v0.1.0.md",
    "PASS-03": "GOV-AUD-PROMPT-030-pass-03-measurement-interviewer-evaluation-v0.1.0.md",
    "PASS-04": "GOV-AUD-PROMPT-040-pass-04-targeted-tooling-v0.1.0.md",
    "PASS-05": "GOV-AUD-PROMPT-050-pass-05-gov7-strategy-v0.1.0.md",
    "PASS-06": "GOV-AUD-PROMPT-060-pass-06-synthesis-v0.1.0.md",
    "PASS-07": "GOV-AUD-PROMPT-070-pass-07-independent-evaluation-v0.1.0.md",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    if not text.startswith("---\n") or (boundary := text.find("\n---\n", 4)) < 0:
        raise ValueError(f"{path}: missing YAML front matter")
    return loads(text[4:boundary], str(path)), text[boundary + 5:]


def validate_markdown(path: Path, root: Path, errors: list[str]) -> None:
    text = path.read_text()
    if "\x00" in text:
        errors.append(f"Markdown contains NUL: {path.relative_to(root)}")
    if text.count("```") % 2:
        errors.append(f"Markdown fence mismatch: {path.relative_to(root)}")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local = target.split("#", 1)[0]
        if local and not (path.parent / local).resolve().exists():
            errors.append(f"Markdown link missing: {path.relative_to(root)} -> {target}")


def validate_registered_pass_01(root: Path, registry: dict, errors: list[str]) -> None:
    run_root = root / RUN_REL
    manifest_path = run_root / "manifest.yaml"
    if not manifest_path.is_file():
        errors.append("executed PASS-01 has no registered run manifest")
        return

    manifest = load(manifest_path)
    run = manifest.get("run", {})
    for key, expected in {
        "audit_id": "GOV-AUD-001",
        "pass_id": "PASS-01",
        "run_id": RUN_ID,
        "status": PASS_01_EXECUTED_STATUS,
        "lifecycle": "EXECUTED",
        "execution_count_limit": 1,
        "execution_count_consumed": 1,
    }.items():
        if run.get(key) != expected:
            errors.append(f"PASS-01 run {key} mismatch")

    authorization = manifest.get("authorization", {})
    authorization_path = root / authorization.get("path", "")
    if (
        authorization.get("id") != "GOV-AUD-AUTH-001"
        or authorization.get("status") != "CONSUMED"
        or not authorization_path.is_file()
        or sha256(authorization_path) != authorization.get("sha256")
    ):
        errors.append("PASS-01 authorization identity, custody or hash mismatch")
    else:
        authorization_record = load(authorization_path).get("authorization", {})
        if any((
            authorization_record.get("authorization_id") != "GOV-AUD-AUTH-001",
            authorization_record.get("authorized_run") != RUN_ID,
            authorization_record.get("authorized_pass") != "PASS-01",
            authorization_record.get("execution_count_limit") != 1,
            authorization_record.get("prompt_identity") != "GOV-AUD-PROMPT-011/0.2.0",
        )):
            errors.append("PASS-01 authorization scope mismatch")

    prompt = manifest.get("prompt", {})
    prompt_path = root / prompt.get("path", "")
    if any((
        prompt.get("prompt_id") != "GOV-AUD-PROMPT-011",
        prompt.get("catalog_prompt_id") != "HP-PROMPT-024",
        str(prompt.get("version")) != "0.2.0",
        prompt.get("lifecycle") != "EXECUTED",
        not prompt_path.is_file(),
        prompt_path.is_file() and sha256(prompt_path) != prompt.get("sha256"),
    )):
        errors.append("PASS-01 prompt identity, custody or hash mismatch")

    input_record = manifest.get("input", {})
    input_path = root / input_record.get("manifest_path", "")
    if any((
        input_record.get("manifest_id") != "GOV-AUD-001-P01-R1-INPUT-001",
        not input_path.is_file(),
        input_path.is_file() and sha256(input_path) != input_record.get("manifest_sha256"),
    )):
        errors.append("PASS-01 input manifest identity, custody or hash mismatch")

    required_outputs = manifest.get("output_contract", {}).get("required_outputs", [])
    declared = {}
    for item in required_outputs:
        path = root / item.get("path", "")
        declared[path.name] = item.get("sha256")
        if not path.is_file() or sha256(path) != item.get("sha256"):
            errors.append(f"PASS-01 output custody or hash mismatch: {path.name}")
    if manifest.get("output_contract", {}).get("substantive_output_count") != 4 or declared != OUTPUT_HASHES:
        errors.append("PASS-01 output contract identity or count mismatch")

    report_path = root / manifest.get("output_contract", {}).get("validation_report", {}).get("path", "")
    if not report_path.is_file():
        errors.append("PASS-01 validation report missing")
    else:
        report = load(report_path).get("validation_report", {})
        if any((
            report.get("record_id") != "GOV-AUD-VAL-001",
            report.get("audit_id") != "GOV-AUD-001",
            report.get("run_id") != RUN_ID,
            report.get("pass_id") != "PASS-01",
            report.get("status") != "VALIDATED",
            report.get("result") != "VALID",
            report.get("prompt", {}).get("prompt_id") != "GOV-AUD-PROMPT-011",
            report.get("authorization", {}).get("authorization_id") != "GOV-AUD-AUTH-001",
            report.get("recommendations_accepted") is not False,
            report.get("implementation_authorized") is not False,
            report.get("pass_02_executed") is not False,
            report.get("checkpoint_a_completed") is not False,
        )):
            errors.append("PASS-01 validation identity or authority boundary mismatch")
        initial = report.get("initial_validation", {})
        correction = report.get("correction", {})
        if any((
            initial.get("targeted_checks") != "PASSED",
            initial.get("full_governance_suite") != "FAILED",
            initial.get("passed_tests") != 141,
            initial.get("failed_tests") != 3,
            initial.get("result") != "INCOMPLETE_VALIDATION",
            initial.get("cause") != "PLANNING_ONLY_VALIDATOR_LIFECYCLE_DEFECT",
            correction.get("correction_id") != CORRECTION_ID,
            correction.get("validator_corrected") is not True,
            correction.get("regression_tests_updated") is not True,
            correction.get("substantive_outputs_changed") is not False,
            correction.get("corrected_full_suite") != "PASSED",
            correction.get("final_validation_result") != "VALID",
        )):
            errors.append("PASS-01 correction validation sequence mismatch")

    prompt_records = {item.get("prompt_id"): item for item in registry.get("prompts", [])}
    run_prompt = prompt_records.get("GOV-AUD-PROMPT-011", {})
    if (
        run_prompt.get("run_id") != RUN_ID
        or run_prompt.get("lifecycle") != "EXECUTED"
        or run_prompt.get("exact_text_sha256") != prompt.get("sha256")
    ):
        errors.append("PASS-01 prompt registry/run mismatch")


def validate_correction_custody(root: Path, registry: dict, errors: list[str]) -> None:
    correction_root = root / CORRECTION_REL
    if not correction_root.exists():
        return
    prompt_path = correction_root / "prompt/GOV-AUD-PROMPT-012-correct-pass-01-audit-validation-lifecycle-v0.1.0.md"
    authorization_path = correction_root / "authorization/GOV-AUD-CORR-AUTH-001-v0.1.0.yaml"
    manifest_path = correction_root / "manifest.yaml"
    if not prompt_path.is_file() or sha256(prompt_path) != CORRECTION_PROMPT_HASH:
        errors.append("correction prompt custody or hash mismatch")
    if not authorization_path.is_file():
        errors.append("correction authorization custody missing")
        return
    authorization = load(authorization_path).get("authorization", {})
    if any((
        authorization.get("authorization_id") != "GOV-AUD-CORR-AUTH-001",
        authorization.get("correction_id") != CORRECTION_ID,
        authorization.get("source_run_id") != RUN_ID,
        authorization.get("prompt_identity") != "GOV-AUD-PROMPT-012/0.1.0",
        authorization.get("catalog_prompt_identity") != "HP-PROMPT-025/0.1.0",
        authorization.get("prompt_sha256") != CORRECTION_PROMPT_HASH,
        authorization.get("prior_authorization", {}).get("reusable") is not False,
    )):
        errors.append("correction authorization identity or boundary mismatch")
    if not manifest_path.is_file():
        errors.append("correction manifest custody missing")
    else:
        correction = load(manifest_path).get("correction", {})
        if any((
            correction.get("correction_id") != CORRECTION_ID,
            correction.get("audit_id") != "GOV-AUD-001",
            correction.get("source_run_id") != RUN_ID,
            correction.get("status") != "VALIDATED",
            correction.get("prompt", {}).get("sha256") != CORRECTION_PROMPT_HASH,
            correction.get("authorization", {}).get("authorization_id") != "GOV-AUD-CORR-AUTH-001",
            correction.get("authorization", {}).get("execution_count_limit") != 1,
            correction.get("authorization", {}).get("execution_count_consumed") != 1,
            correction.get("authorization", {}).get("prior_authorization_reused") is not False,
            correction.get("substantive_outputs", {}).get("changed") is not False,
            correction.get("authority_boundary", {}).get("pass_01_accepted") is not False,
            correction.get("authority_boundary", {}).get("checkpoint_a_completed") is not False,
            correction.get("authority_boundary", {}).get("pass_02_authorized_or_executed") is not False,
            correction.get("authority_boundary", {}).get("gov_7_activated") is not False,
            correction.get("authority_boundary", {}).get("recommendations_accepted") is not False,
            correction.get("authority_boundary", {}).get("implementation_authorized") is not False,
            correction.get("authority_boundary", {}).get("od_006_status") != "UNRESOLVED_TRIGGER_GATED",
        )):
            errors.append("correction manifest identity, validation or authority boundary mismatch")
    prompt_records = {item.get("prompt_id"): item for item in registry.get("prompts", [])}
    correction_prompt = prompt_records.get("GOV-AUD-PROMPT-012", {})
    if any((
        correction_prompt.get("catalog_prompt_id") != "HP-PROMPT-025",
        correction_prompt.get("correction_id") != CORRECTION_ID,
        correction_prompt.get("lifecycle") != "EXECUTED",
        correction_prompt.get("exact_text_sha256") != CORRECTION_PROMPT_HASH,
    )):
        errors.append("correction prompt registry mismatch")


def validate(root: Path) -> dict:
    errors: list[str] = []
    audit = root / AUDIT_REL
    required = [
        "00-audit-charter.md", "01-audit-plan.yaml", "02-audit-status.yaml",
        "03-baseline-input-manifest.yaml", "04-artifact-and-custody-contract.md",
        "05-owner-checkpoints.md", "06-model-routing-policy.md", "prompt-registry.yaml",
        "runs/README.md", "decisions/README.md",
    ]
    for relative in required:
        if not (audit / relative).is_file():
            errors.append(f"missing required scaffold file: {relative}")
    if errors:
        return {"result": "INVALID", "diagnostics": errors}

    plan = load(audit / "01-audit-plan.yaml")["audit_program"]
    status = load(audit / "02-audit-status.yaml")
    registry = load(audit / "prompt-registry.yaml")["prompt_registry"]
    manifest = load(audit / "03-baseline-input-manifest.yaml")["manifest"]

    passes_executed = plan.get("passes_executed")
    if plan.get("audit_id") != "GOV-AUD-001" or passes_executed not in (0, 1):
        errors.append("audit identity or supported lifecycle state mismatch")
    expected_plan_status = "PLANNED_NOT_EXECUTED" if passes_executed == 0 else AUDIT_IN_PROGRESS_STATUS
    if plan.get("status") != expected_plan_status:
        errors.append("audit plan lifecycle status mismatch")
    correction_present = (root / CORRECTION_REL).exists()
    expected_correction_id = CORRECTION_ID if correction_present else None
    if plan.get("validation_correction_id") != expected_correction_id:
        errors.append("audit plan validation correction identity mismatch")
    for key, expected in {
        "checkpoints_approved": 0, "gov_7_activated": False,
        "recommendations_accepted": False, "implementation_authorized": False,
        "graph_technology_selected": False, "vertical_slice_selected": False,
        "audit_executed": False, "completed": False, "pass_01_accepted": False,
    }.items():
        if plan.get(key) != expected:
            errors.append(f"audit plan {key} mismatch")

    expected_sequence = [
        "PASS-01", "PASS-02", "CHECKPOINT-A", "PASS-03", "PASS-04",
        "CHECKPOINT-B", "PASS-05", "PASS-06", "PASS-07", "CHECKPOINT-C",
    ]
    sequence = plan.get("sequence", [])
    if [item.get("id") for item in sequence] != expected_sequence:
        errors.append("audit sequence mismatch")
    if len({item.get("id") for item in sequence}) != len(sequence):
        errors.append("duplicate sequence ID")
    sequence_by_id = {item.get("id"): item for item in sequence}
    for item in sequence:
        if item.get("id") == "PASS-01" and passes_executed == 1:
            expected_status = PASS_01_EXECUTED_STATUS
        else:
            expected_status = "PENDING_OWNER_DECISION" if item.get("id", "").startswith("CHECKPOINT") else "PLANNED_NOT_EXECUTED"
        if item.get("status") != expected_status:
            errors.append(f"sequence status mismatch: {item.get('id')}")
    if sequence_by_id.get("PASS-02", {}).get("status") != "PLANNED_NOT_EXECUTED":
        errors.append("PASS-02 executed before CHECKPOINT-A disposition")
    if sequence_by_id.get("CHECKPOINT-A", {}).get("status") != "PENDING_OWNER_DECISION":
        errors.append("CHECKPOINT-A must remain pending after PASS-01")

    audit_status = status.get("audit", {})
    for key, expected in {
        "id": "GOV-AUD-001", "status": expected_plan_status, "passes_executed": passes_executed,
        "checkpoints_completed": 0, "gov_7_activated": False,
        "recommendations_accepted": False, "implementation_authorized": False,
        "audit_execution_authorized": False, "graph_implemented": False,
        "telemetry_implemented": False, "interviewer_simulation_implemented": False,
        "self_hosting_implemented": False, "owner_decision_inferred": False,
        "completed": False, "pass_01_accepted": False,
    }.items():
        if audit_status.get(key) != expected:
            errors.append(f"audit status {key} mismatch")
    expected_pass_01_status = "PLANNED_NOT_EXECUTED" if passes_executed == 0 else PASS_01_EXECUTED_STATUS
    if audit_status.get("pass_01_status") != expected_pass_01_status:
        errors.append("audit status PASS-01 lifecycle mismatch")
    if audit_status.get("pass_02_status") != "PLANNED_NOT_EXECUTED":
        errors.append("audit status PASS-02 must remain unexecuted")
    if audit_status.get("pass_01_execution_authorized") is not (passes_executed == 1):
        errors.append("PASS-01 execution authorization lifecycle mismatch")
    if audit_status.get("pass_01_authorization_consumed") is not (passes_executed == 1):
        errors.append("PASS-01 authorization consumption lifecycle mismatch")
    correction_status = audit_status.get("validation_lifecycle_correction")
    if correction_present:
        if any((
            not isinstance(correction_status, dict),
            isinstance(correction_status, dict) and correction_status.get("correction_id") != CORRECTION_ID,
            isinstance(correction_status, dict) and correction_status.get("initial_full_suite") != {"result": "FAILED", "passed_tests": 141, "failed_tests": 3},
            isinstance(correction_status, dict) and correction_status.get("corrected_full_suite") != {"result": "PASSED", "passed_tests": 152, "failed_tests": 0},
            isinstance(correction_status, dict) and correction_status.get("substantive_outputs_changed") is not False,
        )):
            errors.append("audit status validation correction mismatch")
    elif correction_status is not None:
        errors.append("planning-only state contains validation correction status")
    baseline = status.get("governance_baseline", {})
    if baseline.get("kernel") != {"version": "0.2.0", "status": "RATIFIED", "implemented": False, "enforceability_claimed": False, "operational": False}:
        errors.append("Kernel baseline mismatch")
    if baseline.get("gov_5", {}).get("status") != "COMPLETED_CLOSED" or baseline.get("gov_6", {}).get("status") != "COMPLETED_CLOSED":
        errors.append("GOV-5/GOV-6 baseline mismatch")
    if baseline.get("gov_7", {}).get("status") != "INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY":
        errors.append("GOV-7 baseline mismatch")
    if baseline.get("od_006", {}).get("status") != "UNRESOLVED_TRIGGER_GATED":
        errors.append("OD-006 baseline mismatch")

    raw_prompt = audit / "prompts/GOV-AUD-PROMPT-000-audit-program-scaffold-v0.2.0.md"
    if not raw_prompt.is_file() or sha256(raw_prompt) != PROMPT_HASH:
        errors.append("exact scaffold prompt hash mismatch")
    prompts = registry.get("prompts", [])
    expected_prompt_ids = list(SCAFFOLD_PROMPT_IDS)
    if passes_executed == 1:
        expected_prompt_ids.append("GOV-AUD-PROMPT-011")
    if correction_present:
        expected_prompt_ids.append("GOV-AUD-PROMPT-012")
    identities = [(item.get("prompt_id"), str(item.get("version"))) for item in prompts]
    if [item[0] for item in identities] != expected_prompt_ids or len(identities) != len(set(identities)):
        errors.append("prompt registry identity/order mismatch")
    for item in prompts:
        path = root / item.get("path", "")
        if not path.is_file():
            errors.append(f"registered prompt path missing: {item.get('prompt_id')}")
        if item.get("prompt_id") == "GOV-AUD-PROMPT-000":
            if item.get("lifecycle") != "EXECUTED" or item.get("exact_text_sha256") != PROMPT_HASH or item.get("audit_pass_executed") is not False:
                errors.append("scaffold prompt registry metadata mismatch")
        elif item.get("prompt_id") in SCAFFOLD_PROMPT_IDS and item.get("lifecycle") != "TEMPLATE":
            errors.append(f"future prompt not TEMPLATE: {item.get('prompt_id')}")

    for index, pass_id in enumerate(PASS_IDS, 1):
        contract_path = audit / f"passes/{pass_id}/contract.yaml"
        if not contract_path.is_file():
            errors.append(f"missing pass contract: {pass_id}")
            continue
        contract = load(contract_path).get("pass", {})
        if REQUIRED_CONTRACT_FIELDS - set(contract):
            errors.append(f"contract fields missing: {pass_id}")
        if contract.get("id") != pass_id or contract.get("status") != "PLANNED_NOT_EXECUTED":
            errors.append(f"contract identity/status mismatch: {pass_id}")
        if contract.get("required_predecessors") != EXPECTED_PREDECESSORS[pass_id]:
            errors.append(f"contract predecessor mismatch: {pass_id}")
        if contract.get("checkpoint_dependency") != EXPECTED_CHECKPOINT[pass_id]:
            errors.append(f"contract checkpoint mismatch: {pass_id}")
        if set(contract.get("mandatory_principles", {})) != PRINCIPLES:
            errors.append(f"mandatory principles mismatch: {pass_id}")
        if contract.get("output_structure", {}).get("statement_labels") != LABELS:
            errors.append(f"statement labels mismatch: {pass_id}")
        prohibited = " ".join(contract.get("prohibited_actions", [])).lower()
        for phrase in ("modify repository", "accept", "owner decisions", "rewrite", "chat memory"):
            if phrase not in prohibited:
                errors.append(f"contract prohibition missing ({phrase}): {pass_id}")
        prereq = contract.get("governance_phase_prerequisites", {})
        if prereq.get("gov_5") != "COMPLETED_CLOSED" or prereq.get("gov_6") != "COMPLETED_CLOSED":
            errors.append(f"governance prerequisite mismatch: {pass_id}")
        if prereq.get("gov_7") != "INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY":
            errors.append(f"GOV-7 prerequisite mismatch: {pass_id}")

        template = audit / "prompts/templates" / TEMPLATE_NAMES[pass_id]
        if not template.is_file():
            errors.append(f"missing prompt template: {pass_id}")
            continue
        metadata, body = frontmatter(template)
        expected_prompt = f"GOV-AUD-PROMPT-{index * 10:03d}"
        if metadata.get("prompt_id") != expected_prompt or metadata.get("pass_id") != pass_id or metadata.get("lifecycle") != "TEMPLATE":
            errors.append(f"template metadata mismatch: {pass_id}")
        for classification in ("KEEP", "REMOVE", "MAKE_CONDITIONAL", "MOVE_TO_FOLLOW_UP"):
            if f"`{classification}`" not in body:
                errors.append(f"anti-bloat classification missing ({classification}): {pass_id}")
        if "not an executable prompt" not in body.lower() or "Required instantiation bindings" not in body:
            errors.append(f"template instantiation boundary missing: {pass_id}")

    starting_head = manifest.get("starting_head")
    for item in manifest.get("inputs", []):
        path = root / item.get("path", "")
        if not path.is_file():
            errors.append(f"baseline input path missing: {item.get('path')}")
            continue
        result = subprocess.run(
            ["git", "-C", str(root), "show", f"{starting_head}:{item.get('path')}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        actual = hashlib.sha256(result.stdout).hexdigest() if result.returncode == 0 else None
        if actual != item.get("sha256"):
            errors.append(f"baseline input hash mismatch at starting HEAD: {item.get('path')}")

    run_directories = sorted(path.name for path in (audit / "runs").iterdir() if path.is_dir())
    registered_runs = sorted(
        path.name for path in (audit / "runs").iterdir()
        if path.is_dir() and (path / "manifest.yaml").is_file()
    )
    if len(registered_runs) != passes_executed:
        errors.append("executed-pass count does not match registered run count")
    if passes_executed == 0 and run_directories:
        errors.append("planning-only state contains an audit run directory")
    if passes_executed == 1:
        if run_directories != [RUN_ID] or registered_runs != [RUN_ID]:
            errors.append("one-pass state must contain exactly the registered PASS-01 run")
        else:
            validate_registered_pass_01(root, registry, errors)
            validate_correction_custody(root, registry, errors)

    run_members = sorted(path.relative_to(audit / "runs").as_posix() for path in (audit / "runs").rglob("*") if path.is_file())
    decision_members = sorted(path.relative_to(audit / "decisions").as_posix() for path in (audit / "decisions").rglob("*") if path.is_file())
    if passes_executed == 0 and run_members != ["README.md"]:
        errors.append("planning-only state contains execution artifacts")
    if decision_members != ["README.md"]:
        errors.append("unexpected decision artifacts detected")
    forbidden_names = {"output", "outputs", "evaluation", "telemetry", "projection", "graph"}
    if passes_executed == 0:
        for path in audit.rglob("*"):
            if path.is_dir() and path.name.lower() in forbidden_names:
                errors.append(f"forbidden placeholder implementation/output directory: {path.relative_to(audit)}")

    global_registry = load(root / "governance/ARTIFACT_REGISTRY.yaml")
    artifacts = global_registry.get("artifacts", [])
    artifact_ids = [item.get("id") for item in artifacts]
    if len(artifact_ids) != len(set(artifact_ids)):
        errors.append("global artifact registry contains duplicate IDs")
    for item in artifacts:
        path = root / item.get("path", "")
        if not path.exists():
            errors.append(f"global artifact registered path missing: {item.get('id')}")
    audit_entry = next((item for item in artifacts if item.get("id") == "GOV-AUD-001"), {})
    if audit_entry.get("status") != expected_plan_status:
        errors.append("global audit registry lifecycle status mismatch")
    required_ids = ["GOV-AUD-001", "HP-PROMPT-023", "GOV-TOOL-004"]
    if passes_executed == 1:
        required_ids.extend(("GOV-AUD-001-P01-R1", "GOV-AUD-AUTH-001", "HP-PROMPT-024", "GOV-AUD-VAL-001"))
    if correction_present:
        required_ids.extend((CORRECTION_ID, "GOV-AUD-CORR-AUTH-001", "HP-PROMPT-025"))
    for required_id in required_ids:
        if required_id not in artifact_ids:
            errors.append(f"global artifact registration missing: {required_id}")

    for path in sorted(audit.rglob("*.yaml")):
        try:
            load(path)
        except Exception as exc:
            errors.append(f"invalid YAML {path.relative_to(root)}: {exc}")
    for path in sorted(audit.rglob("*.md")):
        validate_markdown(path, root, errors)

    return {"result": "VALID" if not errors else "INVALID", "diagnostics": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    result = validate(args.root.resolve())
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["result"] == "VALID" else 1


if __name__ == "__main__":
    raise SystemExit(main())
