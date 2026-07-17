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
from validate_audit_methodology import validate as validate_audit_methodology
from validate_pass_02 import validate as validate_pass_02
from validate_pass_03_execution import validate as validate_pass_03_execution
from validate_pass_03_review_preparation import validate as validate_pass_03_review_preparation


AUDIT_REL = Path("governance/audits/GOV-AUD-001-gov7-enablement")
PROMPT_HASH = "7ea731bb822d88328c26bfe69b5280a84a37153bc525f963d051fb74b6033b07"
CORRECTION_PROMPT_HASH = "7b180f5c96a75ab2203efe2de3c10e31d985c4f9d17b26aea569119f5c4edc5d"
C2_PROMPT_HASH = "0075610713cf0ce9dbb530693bdb518a509098e3bfd6b4c0af3694f12d78d1a0"
C2_AUTHORIZATION_HASH = "9fcc990418e4ae9f0f65ab25bda0cf811a83e1247dc5b2cf5999d3f9d24b9a41"
C2_INPUT_HASH = "c804b3309126cc2aba7bf9f6cf42f24f49a8e2ad6fe4d83eaa9b9d0441effb4a"
METHODOLOGY_PROTOCOL = "GOV-AUD-001-METHOD-001/0.3.0"
METHODOLOGY_CORRECTION_PROMPT = "HP-PROMPT-030/0.3.0"
METHODOLOGY_CORRECTION_PROMPT_PATH = "governance/prompts/orchestration/HP-PROMPT-030-gov-aud-001-audit-methodology-correction-v0.3.0.md"
METHODOLOGY_CORRECTION_PROMPT_HASH = "b47cce4e96daf09657cedfd918a3b47f9ab461ecdc3c55b559fffa1b9fdaad81"
PASS_IDS = [f"PASS-{number:02d}" for number in range(1, 8)]
SCAFFOLD_PROMPT_IDS = ["GOV-AUD-PROMPT-000"] + [f"GOV-AUD-PROMPT-{number:03d}" for number in range(10, 71, 10)]
RUN_ID = "GOV-AUD-001-P01-R1"
RUN_REL = AUDIT_REL / "runs" / RUN_ID
CORRECTION_ID = "GOV-AUD-001-P01-R1-C1"
CORRECTION_REL = RUN_REL / "corrections" / CORRECTION_ID
SUBSTANTIVE_CORRECTION_ID = "GOV-AUD-001-P01-R1-C2"
SUBSTANTIVE_CORRECTION_REL = RUN_REL / "corrections" / SUBSTANTIVE_CORRECTION_ID
PASS_01_EXECUTED_STATUS = "EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION"
AUDIT_IN_PROGRESS_STATUS = "IN_PROGRESS_PASS_01_EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION"
C2_STATUS = "EXECUTED_VALIDATED_PENDING_INDEPENDENT_EVALUATION_AND_PROJECT_OWNER_DISPOSITION"
C2_AUDIT_STATUS = "IN_PROGRESS_PASS_01_CORRECTED_VALIDATED_PENDING_INDEPENDENT_EVALUATION_AND_PROJECT_OWNER_DISPOSITION"
ACCEPTED_AUDIT_STATUS = "IN_PROGRESS_PASS_01_ACCEPTED_COMPLETED"
ACCEPTED_PASS_01_STATUS = "PASS_01_ACCEPTED_COMPLETED"
PASS_02_RUN_ID = "GOV-AUD-001-P02-R1"
PASS_02_RUN_REL = AUDIT_REL / "runs" / PASS_02_RUN_ID
PASS_02_STATUS = "EXECUTED_VALIDATED_PENDING_INDEPENDENT_EVALUATION_AND_PROJECT_OWNER_DISPOSITION"
PASS_02_AUDIT_STATUS = "IN_PROGRESS_PASS_02_EXECUTED_VALIDATED_PENDING_INDEPENDENT_EVALUATION_AND_PROJECT_OWNER_DISPOSITION"
PASS_03_RUN_ID = "GOV-AUD-001-P03-R1"
PASS_03_RUN_REL = AUDIT_REL / "runs" / PASS_03_RUN_ID
PASS_03_STATUS = "EXECUTED_VALIDATED_PENDING_INDEPENDENT_ADVERSARIAL_REVIEW_AND_PROJECT_OWNER_DISPOSITION"
PASS_03_AUDIT_STATUS = "IN_PROGRESS_PASS_03_EXECUTED_VALIDATED_PENDING_INDEPENDENT_ADVERSARIAL_REVIEW_AND_PROJECT_OWNER_DISPOSITION"
ACCEPTANCE_REL = AUDIT_REL / "decisions/GOV-AUD-DECISION-001-pass-01-acceptance-v0.1.0.yaml"
METHODOLOGY_ACCEPTANCE_REL = AUDIT_REL / "decisions/GOV-AUD-DECISION-002-methodology-acceptance-v0.1.0.yaml"
OUTPUT_HASHES = {
    "01-verified-capability-inventory.yaml": "0e1ae26cfd8201e781768eec81045c056b1bc1cd557b0ab1f9fbcae1d47cb124",
    "02-repetition-waste-and-burden-analysis.md": "57cbd6fc8d151d6c338a14c9c6f51e702f9a8519136d5dde5b2d20b2327f900f",
    "03-ranked-gap-register.yaml": "8a485a3df850d6f9b37c4490435980715ddd84c689567ad3a94be89dca674cde",
    "04-pass-01-findings-and-handoff.md": "fd3e035812150b61f1dc54ad33412d5d8c09dcb31abe5a8ddaebd34e8323d2ff",
}
C2_OUTPUT_HASHES = {
    "01-corrected-verified-capability-inventory.yaml": "d099e9bcbec6b5fc27e405759360909b9c29c982b6faed3465d75148bc0047b9",
    "02-corrected-repetition-waste-and-burden-analysis.md": "df5f310afc64b666eea32385f14163fcee75d4871676e0759b893e7c951c5a00",
    "03-corrected-ranked-gap-register.yaml": "d79018cb99728edac9095698e2a91f3b5d9d49ab62229f371d0482408927f5f0",
    "04-corrected-pass-01-findings-and-handoff.md": "401c313f96bf705b39a66e389d1028161df3e73e73b4619ac94e4af19638cb42",
}
C1_ARTIFACT_HASHES = {
    "authorization/GOV-AUD-CORR-AUTH-001-v0.1.0.yaml": "0aac29d22a7eb4556869a8c2b6bc2cb19f2baf6b69da7e470bf52f5d2af1a269",
    "manifest.yaml": "f1b5c2c5b60761907999ea86bfb10da4d505aae71bacebb7583a15bdaa0ce857",
    "prompt/GOV-AUD-PROMPT-012-correct-pass-01-audit-validation-lifecycle-v0.1.0.md": CORRECTION_PROMPT_HASH,
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
ACTIVE_TEMPLATE_NAMES = {
    "PASS-01": "GOV-AUD-PROMPT-010-pass-01-capability-gap-v0.1.0.md",
    "PASS-02": "GOV-AUD-PROMPT-020-pass-02-cross-layer-self-hosting-v0.2.0.md",
    "PASS-03": "GOV-AUD-PROMPT-030-pass-03-measurement-interviewer-evaluation-v0.1.0.md",
    "PASS-04": "GOV-AUD-PROMPT-040-pass-04-targeted-tooling-v0.1.0.md",
    "PASS-05": "GOV-AUD-PROMPT-050-pass-05-gov7-strategy-v0.1.0.md",
    "PASS-06": "GOV-AUD-PROMPT-060-pass-06-synthesis-v0.1.0.md",
    "PASS-07": "GOV-AUD-PROMPT-070-pass-07-independent-evaluation-v0.2.0.md",
}
VERSIONED_CONTRACTS = {
    "PASS-02": {
        "contract_id": "GOV-AUD-001-PASS-02-CONTRACT",
        "version": "0.2.0",
        "predecessor_sha256": "9fa786dfad87b4612671928fc9985e07fcb31aafc366487550fed2a262d3a496",
    },
    "PASS-07": {
        "contract_id": "GOV-AUD-001-PASS-07-CONTRACT",
        "version": "0.2.0",
        "predecessor_sha256": "e2caa6f2ba67261e3c76e53342d848856642b5793fd4e49ede172d63825f50bb",
    },
    "PASS-03": {
        "contract_id": "GOV-AUD-001-PASS-03-CONTRACT",
        "version": "0.2.0",
        "predecessor_sha256": "a41aef15eeb22f0ce779356f92abd761dfaf52db5082247ca75e7b4b3bcea00c",
    },
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


def validate_bound_c2_inputs(root: Path, manifest: dict, errors: list[str]) -> None:
    inputs = manifest.get("inputs", [])
    paths = [item.get("path") for item in inputs]
    if len(inputs) != 92 or len(paths) != len(set(paths)):
        errors.append("C2 input manifest count or path uniqueness mismatch")
    starting_head = manifest.get("starting_local_head")
    current_prefix = SUBSTANTIVE_CORRECTION_REL.as_posix() + "/"
    current_suffixes = ("/prompt/", "/authorization/")
    for item in inputs:
        relative = item.get("path", "")
        if not isinstance(relative, str) or not item.get("role"):
            errors.append("C2 input manifest path or role missing")
            continue
        path = root / relative
        if relative.startswith(current_prefix) and any(part in relative for part in current_suffixes):
            actual = sha256(path) if path.is_file() else None
        else:
            result = subprocess.run(
                ["git", "-C", str(root), "show", f"{starting_head}:{relative}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                check=False,
            )
            actual = hashlib.sha256(result.stdout).hexdigest() if result.returncode == 0 else None
        if actual != item.get("sha256"):
            errors.append(f"C2 bound input hash mismatch: {relative}")


def validate_ranking_node(node, errors: list[str], label: str = "gap register") -> None:
    if isinstance(node, dict):
        if {"frequency", "current_burden", "failure_risk", "score"} <= set(node):
            values = [node[field].get("value") for field in ("frequency", "current_burden", "failure_risk")]
            expected = values[0] * values[1] * values[2] if all(isinstance(value, int) for value in values) else "UNKNOWN"
            if node.get("score") != expected:
                errors.append(f"C2 ranking arithmetic mismatch: {label}")
        for key, value in node.items():
            validate_ranking_node(value, errors, f"{label}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            validate_ranking_node(value, errors, f"{label}[{index}]")


def validate_c2_evidence_paths(root: Path, node, errors: list[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"evidence", "evidence_paths"} and isinstance(value, list):
                for relative in value:
                    if isinstance(relative, str) and not (root / relative).exists():
                        errors.append(f"C2 evidence path missing: {relative}")
            validate_c2_evidence_paths(root, value, errors)
    elif isinstance(node, list):
        for value in node:
            validate_c2_evidence_paths(root, value, errors)


def validate_c3_classification_and_temporal_semantics(root: Path, errors: list[str]) -> None:
    """Prospectively reject classification/temporal conflation in a C3 package."""
    path = root / RUN_REL / "corrections/GOV-AUD-001-P01-R1-C3/output/03-corrected-ranked-gap-register.yaml"
    if not path.is_file():
        return
    register = load(path).get("gap_register", {})
    vocabulary = {"EXISTING_CAPABILITY", "PARTIAL_CAPABILITY", "DEMONSTRATED_GAP", "REQUIREMENT_WITHOUT_IMPLEMENTATION", "RESEARCH_REQUIRED", "OWNER_DECISION_REQUIRED", "NOT_A_GAP"}
    entries = register.get("entries", [])
    for entry in entries:
        classification = entry.get("classification")
        if classification not in vocabulary or "_HISTORICAL_" in str(classification) or "_RESIDUAL_" in str(classification):
            errors.append(f"C3 noncanonical or compound classification: {entry.get('gap_id')}")
        temporal_fields = {"temporal_status", "current_residual_status", "recurrence_status", "future_extension_status"}
        if temporal_fields & set(entry):
            if not temporal_fields <= set(entry):
                errors.append(f"C3 temporal fields missing: {entry.get('gap_id')}")
            if (
                entry.get("temporal_status") == "HISTORICAL_CORRECTED"
                and entry.get("recurrence_status") == "UNKNOWN"
                and entry.get("current_residual_status") == "DEMONSTRATED"
            ):
                errors.append(f"C3 historical corrected item asserted as current residual: {entry.get('gap_id')}")
        for subproblem in entry.get("subproblems", []):
            if subproblem.get("classification") not in vocabulary:
                errors.append(f"C3 subproblem classification mismatch: {subproblem.get('subproblem_id')}")
            if subproblem.get("temporal_status") == "HISTORICAL_CORRECTED":
                if subproblem.get("recurrence_status") != "UNKNOWN":
                    errors.append(f"C3 historical corrected recurrence mismatch: {subproblem.get('subproblem_id')}")
                if subproblem.get("current_residual_status") == "DEMONSTRATED":
                    errors.append(f"C3 historical corrected subproblem asserted as current residual: {subproblem.get('subproblem_id')}")
            priority = subproblem.get("evidence_priority", {})
            if subproblem.get("temporal_status") == "HISTORICAL_CORRECTED" and priority.get("score") != "UNKNOWN" and priority.get("time_basis") != "HISTORICAL":
                errors.append(f"C3 ranking time basis missing: {subproblem.get('subproblem_id')}")


def validate_substantive_correction_custody(root: Path, registry: dict, errors: list[str]) -> None:
    correction_root = root / SUBSTANTIVE_CORRECTION_REL
    if not correction_root.exists():
        return
    prompt_path = correction_root / "prompt/GOV-AUD-PROMPT-013-correct-pass-01-substantive-outputs-v0.1.0.md"
    authorization_path = correction_root / "authorization/GOV-AUD-CORR-AUTH-002-v0.1.0.yaml"
    input_path = correction_root / "input/input-manifest.yaml"
    manifest_path = correction_root / "manifest.yaml"
    report_path = correction_root / "evaluation/correction-validation-report.yaml"
    if not prompt_path.is_file() or sha256(prompt_path) != C2_PROMPT_HASH:
        errors.append("C2 prompt custody or hash mismatch")
    if not authorization_path.is_file() or sha256(authorization_path) != C2_AUTHORIZATION_HASH:
        errors.append("C2 authorization custody or hash mismatch")
    else:
        authorization = load(authorization_path).get("authorization", {})
        if any((
            authorization.get("authorization_id") != "GOV-AUD-CORR-AUTH-002",
            authorization.get("correction_id") != SUBSTANTIVE_CORRECTION_ID,
            authorization.get("source_run_id") != RUN_ID,
            authorization.get("prior_correction_id") != CORRECTION_ID,
            authorization.get("prompt_identity") != "GOV-AUD-PROMPT-013/0.1.0",
            authorization.get("catalog_prompt_identity") != "HP-PROMPT-026/0.1.0",
            authorization.get("prompt_sha256") != C2_PROMPT_HASH,
            authorization.get("execution_count_limit") != 1,
            authorization.get("evidence_review_disposition", {}).get("result") != "RETURN_PASS_01_FOR_BOUNDED_SUBSTANTIVE_CORRECTION",
            any(item.get("reusable") is not False for item in authorization.get("prior_authorizations", [])),
        )):
            errors.append("C2 authorization identity, disposition or boundary mismatch")
    if not input_path.is_file() or sha256(input_path) != C2_INPUT_HASH:
        errors.append("C2 input manifest custody or hash mismatch")
    else:
        input_manifest = load(input_path).get("manifest", {})
        if any((
            input_manifest.get("manifest_id") != "GOV-AUD-001-P01-R1-C2-INPUT-001",
            input_manifest.get("branch") != "governance/kernel-designer-revision-v0.1",
            input_manifest.get("starting_local_head") != "22b66c97851316b4c461077f057fc3f1bc2de851",
            input_manifest.get("starting_remote_head") != "22b66c97851316b4c461077f057fc3f1bc2de851",
            input_manifest.get("prompt", {}).get("sha256") != C2_PROMPT_HASH,
            input_manifest.get("authorization", {}).get("sha256") != C2_AUTHORIZATION_HASH,
        )):
            errors.append("C2 input manifest identity or starting-state mismatch")
        validate_bound_c2_inputs(root, input_manifest, errors)
    if not manifest_path.is_file():
        errors.append("C2 manifest custody missing")
        return
    correction = load(manifest_path).get("correction", {})
    if any((
        correction.get("correction_id") != SUBSTANTIVE_CORRECTION_ID,
        correction.get("source_run_id") != RUN_ID,
        correction.get("prior_correction_id") != CORRECTION_ID,
        correction.get("status") != C2_STATUS,
        correction.get("execution_count_limit") != 1,
        correction.get("execution_count_consumed") != 1,
        correction.get("prompt", {}).get("sha256") != C2_PROMPT_HASH,
        correction.get("authorization", {}).get("sha256") != C2_AUTHORIZATION_HASH,
        correction.get("authorization", {}).get("execution_count_consumed") != 1,
        correction.get("authorization", {}).get("prior_authorizations_reused") is not False,
        correction.get("input", {}).get("sha256") != C2_INPUT_HASH,
        correction.get("input", {}).get("member_count") != 92,
        correction.get("immutable_evidence", {}).get("original_outputs_modified") is not False,
        correction.get("immutable_evidence", {}).get("prior_correction_artifacts_modified") is not False,
    )):
        errors.append("C2 manifest identity, custody or status mismatch")
    boundary = correction.get("authority_boundary", {})
    for field in (
        "pass_01_accepted", "independent_evaluation_completed", "checkpoint_a_completed",
        "pass_02_authorized_or_executed", "gov_7_activated", "recommendations_accepted",
        "implementation_authorized", "risk_accepted", "architecture_or_technology_selected",
        "kernel_substance_modified", "planning_product_or_runtime_modified", "publication_performed",
    ):
        if boundary.get(field) is not False:
            errors.append(f"C2 authority boundary mismatch: {field}")
    if boundary.get("od_006_status") != "UNRESOLVED_TRIGGER_GATED":
        errors.append("C2 OD-006 boundary mismatch")
    declared_outputs = {
        Path(item.get("path", "")).name: item.get("sha256")
        for item in correction.get("output_contract", {}).get("outputs", [])
    }
    if correction.get("output_contract", {}).get("corrected_output_count") != 4 or declared_outputs != C2_OUTPUT_HASHES:
        errors.append("C2 output contract identity or count mismatch")
    for name, expected in C2_OUTPUT_HASHES.items():
        path = correction_root / "output" / name
        if not path.is_file() or sha256(path) != expected:
            errors.append(f"C2 output custody or hash mismatch: {name}")
    for name, expected in OUTPUT_HASHES.items():
        if sha256(root / RUN_REL / "output" / name) != expected:
            errors.append(f"C2 immutable R1 output mismatch: {name}")
    for relative, expected in C1_ARTIFACT_HASHES.items():
        if sha256(root / CORRECTION_REL / relative) != expected:
            errors.append(f"C2 immutable C1 artifact mismatch: {relative}")
    capability = load(correction_root / "output/01-corrected-verified-capability-inventory.yaml")
    families = capability.get("capability_inventory", {}).get("capability_families", [])
    if len(families) != 14 or len({item.get("capability_id") for item in families}) != 14:
        errors.append("C2 capability family count or ID uniqueness mismatch")
    gap_document = load(correction_root / "output/03-corrected-ranked-gap-register.yaml")
    gap_register = gap_document.get("gap_register", {})
    entries = gap_register.get("entries", [])
    if [item.get("gap_id") for item in entries] != [f"GAP-{number:03d}" for number in range(1, 15)]:
        errors.append("C2 gap identity or traceability mismatch")
    if gap_register.get("implementation_coverage_baseline", {}).get("fully_supported_by_implementation_evidence") != 0:
        errors.append("C2 zero-of-20 implementation baseline mismatch")
    for entry in entries:
        if entry.get("classification") == "NOT_A_GAP" and (
            entry.get("preliminary_leverage") != "UNKNOWN"
            or entry.get("leverage_status") != "NOT_APPLICABLE_NOT_A_GAP"
        ):
            errors.append(f"C2 NOT_A_GAP leverage mismatch: {entry.get('gap_id')}")
    for gap_id in ("GAP-008", "GAP-009", "GAP-010", "GAP-011"):
        item = next((entry for entry in entries if entry.get("gap_id") == gap_id), {})
        if item.get("priority") != "DEFER" or not str(item.get("conditional_priority", "")).startswith("P0_IF_"):
            errors.append(f"C2 trigger priority mismatch: {gap_id}")
    validate_ranking_node(gap_register, errors)
    validate_c2_evidence_paths(root, capability, errors)
    validate_c2_evidence_paths(root, gap_document, errors)
    if not report_path.is_file():
        errors.append("C2 deterministic validation report missing")
    else:
        report = load(report_path).get("validation_report", {})
        if any((
            report.get("record_id") != "GOV-AUD-C2-VAL-001",
            report.get("correction_id") != SUBSTANTIVE_CORRECTION_ID,
            report.get("evidence_class") != "SOURCE_CORRECTION_DETERMINISTIC_VALIDATION_NOT_INDEPENDENT_EVALUATION",
            report.get("status") != "VALIDATED",
            report.get("result") != "VALID",
            report.get("independent_evaluation_performed") is not False,
            report.get("pass_01_accepted") is not False,
            report.get("checkpoint_a_completed") is not False,
            report.get("pass_02_authorized_or_executed") is not False,
            report.get("recommendations_accepted") is not False,
            report.get("risk_accepted") is not False,
            report.get("implementation_authorized") is not False,
        )):
            errors.append("C2 validation report identity, result or authority boundary mismatch")
    prompt_records = {item.get("prompt_id"): item for item in registry.get("prompts", [])}
    c2_prompt = prompt_records.get("GOV-AUD-PROMPT-013", {})
    if any((
        c2_prompt.get("catalog_prompt_id") != "HP-PROMPT-026",
        c2_prompt.get("correction_id") != SUBSTANTIVE_CORRECTION_ID,
        c2_prompt.get("lifecycle") != "EXECUTED",
        c2_prompt.get("exact_text_sha256") != C2_PROMPT_HASH,
        c2_prompt.get("independent_evaluation_completed") is not False,
        c2_prompt.get("pass_02_authorized_or_executed") is not False,
    )):
        errors.append("C2 prompt registry mismatch")


def validate(root: Path) -> dict:
    errors: list[str] = []
    audit = root / AUDIT_REL
    required = [
        "00-audit-charter.md", "01-audit-plan.yaml", "02-audit-status.yaml",
        "03-baseline-input-manifest.yaml", "04-artifact-and-custody-contract.md",
        "05-owner-checkpoints.md", "06-model-routing-policy.md",
        "07-audit-methodology-and-review-protocol.yaml", "prompt-registry.yaml",
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
    pass_03_prepared = plan.get("status") == "IN_PROGRESS_PASS_03_PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION"
    pass_03_executed = plan.get("status") == PASS_03_AUDIT_STATUS
    pass_03_ready = pass_03_prepared or pass_03_executed
    if any((
        registry.get("methodology_protocol") != METHODOLOGY_PROTOCOL,
        registry.get("methodology_correction_prompt") != METHODOLOGY_CORRECTION_PROMPT,
        registry.get("methodology_correction_prompt_path") != METHODOLOGY_CORRECTION_PROMPT_PATH,
        registry.get("methodology_correction_prompt_sha256") != METHODOLOGY_CORRECTION_PROMPT_HASH,
        sha256(root / METHODOLOGY_CORRECTION_PROMPT_PATH) != METHODOLOGY_CORRECTION_PROMPT_HASH,
        registry.get("identity_resolution_rule") != "RESOLVE_FROM_CANONICAL_REGISTRIES_VERIFY_UNUSED_AND_RECORD_EVIDENCE_BEFORE_BINDING",
    )):
        errors.append("audit prompt registry methodology or identity-resolution binding mismatch")
    registry_contracts = registry.get("pass_contracts", {})
    for pass_id, expected in VERSIONED_CONTRACTS.items():
        record = registry_contracts.get(pass_id, {})
        contract_path = audit / f"passes/{pass_id}/contract.yaml"
        if any((
            record.get("contract_id") != expected["contract_id"],
            str(record.get("version")) != expected["version"],
            record.get("status") != ("PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION" if pass_id == "PASS-03" else "ACTIVE_FOR_FUTURE_INSTANTIATION"),
            record.get("path") != contract_path.relative_to(root).as_posix(),
            not contract_path.is_file(),
            contract_path.is_file() and record.get("sha256") != sha256(contract_path),
            (
                record.get("historical_run_binding_preserved", {}).get("predecessor_sha256")
                if pass_id == "PASS-02"
                else record.get("predecessor_sha256")
            ) != expected["predecessor_sha256"],
        )):
            errors.append(f"audit prompt registry contract binding mismatch: {pass_id}")
    if plan.get("audit_id") != "GOV-AUD-001" or passes_executed not in (0, 1, 2, 3):
        errors.append("audit identity or supported lifecycle state mismatch")
    correction_present = (root / CORRECTION_REL).exists()
    c2_present = (root / SUBSTANTIVE_CORRECTION_REL).exists()
    acceptance_path = root / ACCEPTANCE_REL
    accepted = acceptance_path.is_file()
    expected_plan_status = (
        PASS_03_AUDIT_STATUS if pass_03_executed
        else "IN_PROGRESS_PASS_03_PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION" if pass_03_prepared
        else
        "PLANNED_NOT_EXECUTED" if passes_executed == 0
        else PASS_02_AUDIT_STATUS if passes_executed == 2
        else ACCEPTED_AUDIT_STATUS if accepted
        else C2_AUDIT_STATUS if c2_present
        else AUDIT_IN_PROGRESS_STATUS
    )
    if plan.get("status") != expected_plan_status:
        errors.append("audit plan lifecycle status mismatch")
    methodology_binding = plan.get("methodology_protocol", {})
    if methodology_binding != {
        "id": "GOV-AUD-001-METHOD-001",
        "version": "0.3.0",
        "path": "governance/audits/GOV-AUD-001-gov7-enablement/07-audit-methodology-and-review-protocol.yaml",
        "applies_prospectively": True,
        "historical_runs_modified": False,
    }:
        errors.append("audit methodology binding mismatch")
    expected_correction_id = CORRECTION_ID if correction_present else None
    if plan.get("validation_correction_id") != expected_correction_id:
        errors.append("audit plan validation correction identity mismatch")
    if plan.get("substantive_correction_id") != (SUBSTANTIVE_CORRECTION_ID if c2_present else None):
        errors.append("audit plan substantive correction identity mismatch")
    for key, expected in {
        "checkpoints_approved": 1 if pass_03_ready else 0, "gov_7_activated": False,
        "recommendations_accepted": False, "implementation_authorized": False,
        "graph_technology_selected": False, "vertical_slice_selected": False,
        "audit_executed": False, "completed": False, "pass_01_accepted": accepted,
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
        if item.get("id") == "PASS-01" and passes_executed >= 1:
            expected_status = ACCEPTED_PASS_01_STATUS if accepted else C2_STATUS if c2_present else PASS_01_EXECUTED_STATUS
        elif item.get("id") == "PASS-02" and passes_executed >= 2:
            expected_status = "ACCEPTED_COMPLETED" if pass_03_ready else PASS_02_STATUS
        elif item.get("id") == "CHECKPOINT-A" and pass_03_ready:
            expected_status = "APPROVED_COMPLETED"
        elif item.get("id") == "PASS-03" and pass_03_ready:
            expected_status = PASS_03_STATUS if pass_03_executed else "PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION"
        else:
            expected_status = "PENDING_PROJECT_OWNER_DISPOSITION" if accepted and item.get("id") == "CHECKPOINT-A" else "PENDING_OWNER_DECISION" if item.get("id", "").startswith("CHECKPOINT") else "PLANNED_NOT_EXECUTED"
        if item.get("status") != expected_status:
            errors.append(f"sequence status mismatch: {item.get('id')}")
    if passes_executed < 2 and sequence_by_id.get("PASS-02", {}).get("status") != "PLANNED_NOT_EXECUTED":
        errors.append("PASS-02 status is inconsistent with executed-pass count")
    if sequence_by_id.get("CHECKPOINT-A", {}).get("status") != ("APPROVED_COMPLETED" if pass_03_ready else "PENDING_PROJECT_OWNER_DISPOSITION" if accepted else "PENDING_OWNER_DECISION"):
        errors.append("CHECKPOINT-A must remain pending after PASS-01")

    audit_status = status.get("audit", {})
    for key, expected in {
        "id": "GOV-AUD-001", "status": expected_plan_status, "passes_executed": passes_executed,
        "checkpoints_completed": 1 if pass_03_ready else 0, "gov_7_activated": False,
        "recommendations_accepted": False, "implementation_authorized": False,
        "audit_execution_authorized": False, "graph_implemented": False,
        "telemetry_implemented": False, "interviewer_simulation_implemented": False,
        "self_hosting_implemented": False, "owner_decision_inferred": False,
        "completed": False, "pass_01_accepted": accepted,
    }.items():
        if audit_status.get(key) != expected:
            errors.append(f"audit status {key} mismatch")
    expected_pass_01_status = (
        "PLANNED_NOT_EXECUTED" if passes_executed == 0
        else ACCEPTED_PASS_01_STATUS if accepted else C2_STATUS if c2_present
        else PASS_01_EXECUTED_STATUS
    )
    if audit_status.get("pass_01_status") != expected_pass_01_status:
        errors.append("audit status PASS-01 lifecycle mismatch")
    expected_pass_02_status = ("ACCEPTED_COMPLETED" if pass_03_ready else PASS_02_STATUS) if passes_executed >= 2 else "PLANNED_NOT_EXECUTED"
    if audit_status.get("pass_02_status") != expected_pass_02_status:
        errors.append("audit status PASS-02 lifecycle mismatch")
    if audit_status.get("pass_01_execution_authorized") is not (passes_executed >= 1):
        errors.append("PASS-01 execution authorization lifecycle mismatch")
    if audit_status.get("pass_01_authorization_consumed") is not (passes_executed >= 1):
        errors.append("PASS-01 authorization consumption lifecycle mismatch")
    if audit_status.get("pass_02_execution_authorized", False) is not (passes_executed >= 2):
        errors.append("PASS-02 execution authorization lifecycle mismatch")
    if audit_status.get("pass_02_authorization_consumed", False) is not (passes_executed >= 2):
        errors.append("PASS-02 authorization consumption lifecycle mismatch")
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
    substantive_status = audit_status.get("substantive_output_correction")
    if c2_present:
        if any((
            not isinstance(substantive_status, dict),
            isinstance(substantive_status, dict) and substantive_status.get("correction_id") != SUBSTANTIVE_CORRECTION_ID,
            isinstance(substantive_status, dict) and substantive_status.get("status") != C2_STATUS,
            isinstance(substantive_status, dict) and substantive_status.get("original_outputs_modified") is not False,
            isinstance(substantive_status, dict) and substantive_status.get("prior_correction_modified") is not False,
            isinstance(substantive_status, dict) and substantive_status.get("independent_evaluation_completed") is not accepted,
            isinstance(substantive_status, dict) and substantive_status.get("pass_01_accepted") is not accepted,
            isinstance(substantive_status, dict) and substantive_status.get("pass_02_authorized_or_executed") is not False,
            isinstance(substantive_status, dict) and substantive_status.get("checkpoint_a_completed") is not False,
            isinstance(substantive_status, dict) and substantive_status.get("gov_7_activated") is not False,
        )):
            errors.append("audit status substantive correction mismatch")
    elif substantive_status is not None:
        errors.append("pre-C2 state contains substantive correction status")
    if accepted:
        decision = load(acceptance_path).get("project_owner_decision", {})
        if any((
            decision.get("decision_id") != "GOV-AUD-DECISION-001",
            decision.get("final_status") != ACCEPTED_PASS_01_STATUS,
            decision.get("accepted_evidence", {}).get("independent_confirmation") != "GOV-AUD-001-P01-C3-IER-001",
            decision.get("accepted_evidence", {}).get("independent_result") != "CONFIRMED_SUITABLE_FOR_PROJECT_OWNER_DISPOSITION",
            decision.get("audit_program_completed") is not False,
            decision.get("pass_02_status") != "PLANNED_NOT_EXECUTED_UNAUTHORIZED",
            decision.get("checkpoint_a_status") != "PENDING_PROJECT_OWNER_DISPOSITION",
            decision.get("gov_7_status") != "INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY",
            decision.get("od_006_status") != "UNRESOLVED_TRIGGER_GATED",
            decision.get("immutable_evidence") != {"R1": True, "C1": True, "C2": True, "C3": True, "independent_review_evidence": True, "prompts_manifests_outputs_and_learning_records": True},
        )):
            errors.append("PASS-01 acceptance decision boundary mismatch")
        confirmation = root / RUN_REL / "evaluation/GOV-AUD-001-P01-C3-IER-001/output/independent-confirmation.md"
        if not confirmation.is_file() or confirmation.read_text() != "CONFIRMED_SUITABLE_FOR_PROJECT_OWNER_DISPOSITION\n":
            errors.append("PASS-01 independent confirmation custody mismatch")
    methodology_acceptance = root / METHODOLOGY_ACCEPTANCE_REL
    if methodology_acceptance.is_file():
        decision = load(methodology_acceptance).get("project_owner_decision", {})
        if any((
            decision.get("decision_id") != "GOV-AUD-DECISION-002",
            decision.get("decision") != "ACCEPT_GOV_AUD_001_METHOD_001_0_3_0",
            decision.get("accepted_artifact", {}).get("id") != "GOV-AUD-001-METHOD-001",
            str(decision.get("accepted_artifact", {}).get("version")) != "0.3.0",
            decision.get("accepted_artifact", {}).get("independent_confirmation") != "CONFIRMED_SUITABLE_FOR_PROJECT_OWNER_DISPOSITION",
            decision.get("preserved_boundaries", {}).get("pass_02_r1_immutable") is not True,
            decision.get("preserved_boundaries", {}).get("pass_02_accepted") is not False,
            decision.get("preserved_boundaries", {}).get("checkpoint_a_completed") is not False,
            decision.get("preserved_boundaries", {}).get("pass_03_prepared_or_executed") is not False,
            decision.get("preserved_boundaries", {}).get("gov_7_activated") is not False,
            decision.get("preserved_boundaries", {}).get("kernel_amended") is not False,
            decision.get("preserved_boundaries", {}).get("od_006_resolved") is not False,
        )):
            errors.append("methodology acceptance decision boundary mismatch")
        methodology = load(audit / "07-audit-methodology-and-review-protocol.yaml").get("audit_methodology", {})
        correction = audit_status.get("methodology_correction", {})
        if any((
            methodology.get("status") != "ACCEPTED_PROSPECTIVE_AUDIT_METHODOLOGY",
            correction.get("status") != "ACCEPTED_PROSPECTIVE_AUDIT_METHODOLOGY",
            correction.get("bounded_review_result") != "CONFIRMED_SUITABLE_FOR_PROJECT_OWNER_DISPOSITION",
            correction.get("acceptance_record") != "GOV-AUD-DECISION-002/0.1.0",
        )):
            errors.append("methodology acceptance state mismatch")
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
    expected_executed_prompt_ids = ["GOV-AUD-PROMPT-000"]
    if passes_executed >= 1:
        expected_executed_prompt_ids.append("GOV-AUD-PROMPT-011")
    if correction_present:
        expected_executed_prompt_ids.append("GOV-AUD-PROMPT-012")
    if c2_present:
        expected_executed_prompt_ids.append("GOV-AUD-PROMPT-013")
    if (root / RUN_REL / "corrections/GOV-AUD-001-P01-R1-C3").exists():
        expected_executed_prompt_ids.append("GOV-AUD-PROMPT-015")
    if accepted:
        expected_executed_prompt_ids.append("GOV-AUD-PROMPT-016")
    if passes_executed >= 2:
        expected_executed_prompt_ids.append("GOV-AUD-PROMPT-021")
    if pass_03_ready:
        expected_executed_prompt_ids.append("HP-PROMPT-033")
    if pass_03_executed:
        expected_executed_prompt_ids.append("GOV-AUD-PROMPT-031")
    identities = [(item.get("prompt_id"), str(item.get("version"))) for item in prompts]
    if len(identities) != len(set(identities)):
        errors.append("prompt registry contains duplicate prompt identity/version")
    executed_prompt_ids = [
        item.get("prompt_id")
        for item in prompts
        if item.get("lifecycle") not in {"TEMPLATE", "SUPERSEDED", "INSTANTIATED_NOT_EXECUTED"}
    ]
    if executed_prompt_ids != expected_executed_prompt_ids:
        errors.append("prompt registry executed identity/order mismatch")
    for item in prompts:
        path = root / item.get("path", "")
        if not path.is_file():
            errors.append(f"registered prompt path missing: {item.get('prompt_id')}")
        if item.get("prompt_id") == "GOV-AUD-PROMPT-000":
            if item.get("lifecycle") != "EXECUTED" or item.get("exact_text_sha256") != PROMPT_HASH or item.get("audit_pass_executed") is not False:
                errors.append("scaffold prompt registry metadata mismatch")
    for index, pass_id in enumerate(PASS_IDS, 1):
        expected_prompt = f"GOV-AUD-PROMPT-{index * 10:03d}"
        lineage = [item for item in prompts if item.get("prompt_id") == expected_prompt]
        active = [item for item in lineage if item.get("lifecycle") == "TEMPLATE"]
        if len(active) != 1 or active[0].get("pass_id") != pass_id:
            errors.append(f"active prompt template registry mismatch: {pass_id}")
        for item in lineage:
            if item.get("lifecycle") not in {"TEMPLATE", "SUPERSEDED"}:
                errors.append(f"future prompt lifecycle invalid: {expected_prompt}")

    for index, pass_id in enumerate(PASS_IDS, 1):
        contract_path = audit / f"passes/{pass_id}/contract.yaml"
        if not contract_path.is_file():
            errors.append(f"missing pass contract: {pass_id}")
            continue
        contract = load(contract_path).get("pass", {})
        if pass_id == "PASS-03" and contract.get("status") == "PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION":
            identity = contract.get("contract_identity", {})
            if identity.get("contract_id") != "GOV-AUD-001-PASS-03-CONTRACT" or str(identity.get("version")) != "0.2.0":
                errors.append("versioned contract binding mismatch: PASS-03")
            continue
        if REQUIRED_CONTRACT_FIELDS - set(contract):
            errors.append(f"contract fields missing: {pass_id}")
        if contract.get("id") != pass_id or contract.get("status") != "PLANNED_NOT_EXECUTED":
            errors.append(f"contract identity/status mismatch: {pass_id}")
        expected_contract = VERSIONED_CONTRACTS.get(pass_id)
        if expected_contract:
            identity = contract.get("contract_identity", {})
            supersession = identity.get("supersession", {})
            if any((
                identity.get("contract_id") != expected_contract["contract_id"],
                str(identity.get("version")) != expected_contract["version"],
                identity.get("status") != "ACTIVE_FOR_FUTURE_INSTANTIATION",
                supersession.get("status") != "SUPERSEDES_PREVIOUS_UNVERSIONED_SNAPSHOT",
                supersession.get("predecessor_sha256") != expected_contract["predecessor_sha256"],
                identity.get("prompt_binding_rule") != "INSTANTIATED_PROMPT_MUST_BIND_CONTRACT_ID_VERSION_AND_SHA256",
                contract.get("methodology_protocol") != METHODOLOGY_PROTOCOL,
            )):
                errors.append(f"versioned contract binding mismatch: {pass_id}")
        elif "contract_identity" in contract:
            errors.append(f"unrelated pass contract was versioned by bounded correction: {pass_id}")
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

        template = audit / "prompts/templates" / ACTIVE_TEMPLATE_NAMES[pass_id]
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
        registry_active = next(
            (
                item for item in prompts
                if item.get("prompt_id") == expected_prompt and item.get("lifecycle") == "TEMPLATE"
            ),
            {},
        )
        if registry_active.get("path") != template.relative_to(root).as_posix() or str(registry_active.get("version")) != str(metadata.get("version")):
            errors.append(f"active template registry/path mismatch: {pass_id}")
        if expected_contract:
            for binding_name in ("PASS_CONTRACT_ID", "PASS_CONTRACT_VERSION", "PASS_CONTRACT_SHA256"):
                if binding_name not in body:
                    errors.append(f"contract binding missing ({binding_name}): {pass_id}")

    pass_07_contract = load(audit / "passes/PASS-07/contract.yaml").get("pass", {})
    pass_07_output = pass_07_contract.get("output_structure", {})
    if any((
        set(pass_07_output.get("disposition_review_types", [])) != {
            "INDEPENDENT_SUBSTANTIVE_REVIEW",
            "ADVERSARIAL_REVIEW",
        },
        set(pass_07_output.get("auxiliary_review_types_without_disposition_authority", [])) != {
            "DETERMINISTIC_VALIDATION",
            "TARGETED_CONFIRMATION",
        },
        set(pass_07_output.get("permitted_results", [])) != {
            "SUITABLE_FOR_PROJECT_OWNER_DECISION",
            "RETURN_FOR_BOUNDED_VERSIONED_CORRECTION",
            "INVALID_AUDIT_EXECUTION",
            "INSUFFICIENT_EVIDENCE_FOR_PASS_07_DISPOSITION",
        },
        pass_07_output.get("exactly_one_result") is not True,
    )):
        errors.append("PASS-07 review-type or result contract mismatch")

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
            validate_substantive_correction_custody(root, registry, errors)
            validate_c3_classification_and_temporal_semantics(root, errors)
    if passes_executed == 2:
        expected_runs = sorted([RUN_ID, PASS_02_RUN_ID])
        if run_directories != expected_runs or registered_runs != expected_runs:
            errors.append("two-pass state must contain exactly the registered PASS-01 and PASS-02 runs")
        else:
            validate_registered_pass_01(root, registry, errors)
            validate_correction_custody(root, registry, errors)
            validate_substantive_correction_custody(root, registry, errors)
            validate_c3_classification_and_temporal_semantics(root, errors)
            if not pass_03_prepared:
                pass_02_result = validate_pass_02(root)
                errors.extend(f"PASS-02: {item}" for item in pass_02_result["diagnostics"])
    if passes_executed == 3:
        expected_runs = sorted([RUN_ID, PASS_02_RUN_ID, PASS_03_RUN_ID])
        if run_directories != expected_runs or registered_runs != expected_runs:
            errors.append("three-pass state must contain exactly the registered PASS-01, PASS-02 and PASS-03 runs")
        else:
            validate_registered_pass_01(root, registry, errors)
            validate_correction_custody(root, registry, errors)
            validate_substantive_correction_custody(root, registry, errors)
            validate_c3_classification_and_temporal_semantics(root, errors)
            pass_02_result = validate_pass_02(root)
            errors.extend(f"PASS-02: {item}" for item in pass_02_result["diagnostics"])
            pass_03_result = validate_pass_03_execution(root)
            errors.extend(f"PASS-03: {item}" for item in pass_03_result["diagnostics"])
            pass_03_review_preparation = validate_pass_03_review_preparation(root)
            errors.extend(f"PASS-03-REVIEW-PREPARATION: {item}" for item in pass_03_review_preparation["diagnostics"])
    methodology_result = validate_audit_methodology(root)
    errors.extend(f"AUDIT-METHODOLOGY: {item}" for item in methodology_result["diagnostics"])

    run_members = sorted(path.relative_to(audit / "runs").as_posix() for path in (audit / "runs").rglob("*") if path.is_file())
    decision_members = sorted(path.relative_to(audit / "decisions").as_posix() for path in (audit / "decisions").rglob("*") if path.is_file())
    if passes_executed == 0 and run_members != ["README.md"]:
        errors.append("planning-only state contains execution artifacts")
    expected_decision_members = sorted(["README.md"] + (["GOV-AUD-DECISION-001-pass-01-acceptance-v0.1.0.yaml"] if accepted else []) + (["GOV-AUD-DECISION-002-methodology-acceptance-v0.1.0.yaml"] if methodology_acceptance.is_file() else []) + (["GOV-AUD-DECISION-003-pass-02-checkpoint-a-approval-v0.1.0.yaml"] if pass_03_ready else []))
    if decision_members != expected_decision_members:
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
    required_ids = [
        "GOV-AUD-001", "GOV-AUD-001-METHOD-001", "HP-PROMPT-023",
        "HP-PROMPT-030", "GOV-AUD-VAL-003", "GOV-AUD-VAL-004",
        "GOV-AUD-001-PASS-02-CONTRACT", "GOV-AUD-001-PASS-07-CONTRACT",
        "GOV-TOOL-004", "GOV-TOOL-006",
    ]
    if passes_executed >= 1:
        required_ids.extend(("GOV-AUD-001-P01-R1", "GOV-AUD-AUTH-001", "HP-PROMPT-024", "GOV-AUD-VAL-001"))
    if correction_present:
        required_ids.extend((CORRECTION_ID, "GOV-AUD-CORR-AUTH-001", "HP-PROMPT-025"))
    if c2_present:
        required_ids.extend((
            SUBSTANTIVE_CORRECTION_ID, "GOV-AUD-CORR-AUTH-002", "HP-PROMPT-026",
            "GOV-AUD-C2-OUT-001", "GOV-AUD-C2-OUT-002", "GOV-AUD-C2-OUT-003",
            "GOV-AUD-C2-OUT-004", "GOV-AUD-C2-VAL-001",
        ))
    if accepted:
        required_ids.extend(("HP-PROMPT-027", "GOV-AUD-001-P01-C3-IER-001", "GOV-AUD-DECISION-001", "HP-PROMPT-028"))
    if passes_executed >= 2:
        required_ids.extend((
            "GOV-AUD-001-P02-R1", "GOV-AUD-AUTH-002", "HP-PROMPT-029",
            "GOV-AUD-P02-OUT-001", "GOV-AUD-P02-OUT-002", "GOV-AUD-P02-OUT-003",
            "GOV-AUD-P02-OUT-004", "GOV-AUD-P02-OUT-005", "GOV-AUD-P02-OUT-006",
            "GOV-AUD-P02-OUT-007", "GOV-AUD-VAL-002", "GOV-TOOL-005",
        ))
    if passes_executed == 3:
        required_ids.extend((
            "GOV-AUD-001-P03-R1", "GOV-AUD-AUTH-003", "HP-PROMPT-035",
            "GOV-AUD-P03-INPUT-001", "GOV-AUD-P03-OUT-001", "GOV-AUD-P03-OUT-002",
            "GOV-AUD-P03-OUT-003", "GOV-AUD-P03-OUT-004", "GOV-AUD-P03-OUT-005",
            "GOV-AUD-P03-OUT-006", "GOV-AUD-P03-OUT-007", "GOV-AUD-P03-OUT-008",
            "GOV-AUD-P03-OUT-009", "GOV-AUD-P03-VAL-001", "GOV-AUD-P03-REVIEW-PACKAGE-001",
            "GOV-AUD-P03-REVIEW-EXECUTION-PACKAGE-001", "GOV-AUD-001-P03-AR-001",
            "GOV-AUD-001-PASS-03-ADVERSARIAL-REVIEW-CONTRACT", "GOV-AUD-P03-AR-INPUT-001",
            "GOV-AUD-P03-AR-OUTPUT-SPEC-001", "GOV-AUD-P03-AR-VALIDATION-PLAN-001", "HP-PROMPT-037",
        ))
    if methodology_acceptance.is_file():
        required_ids.extend(("GOV-AUD-VAL-005", "GOV-AUD-DECISION-002", "HP-PROMPT-031"))
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
