#!/usr/bin/env python3
"""Validate the durable KGR-006-R1/GOV-7 direction state across governance surfaces."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib.strict_yaml import load


OUTPUT_SHA256 = "0f496b5b17feb724977f189413f485100b9a66d98b1f79dc05cf45fb60aee66b"
RUN_REL = Path("governance/runs/KGR-006-R1-enforcement-analysis-correction")
REVIEW_REL = Path("governance/reviews/kgr-006-r1-controlled-import-and-owner-review")
DECISION_RECORD_REL = REVIEW_REL / "project-owner-decision-record-v0.2.0.yaml"
EXECUTED_REVIEW_REL = REVIEW_REL / "gov-5-phase-closure-readiness-v0.2.0.yaml"
RATIFICATION_RECORD_REL = Path("governance/reviews/gov-6-ratification/kernel-ratification-decision-record-v0.1.0.yaml")
GOV_7_DIRECTION_RECORD_REL = Path("governance/reviews/gov-7-direction/od-005-gov-7-direction-decision-record-v0.1.0.yaml")
READY_REVIEW_STATUS = "EXECUTED_READY_FOR_PROJECT_OWNER_DECISION"
READY_REVIEW_RESULT = "READY_FOR_PROJECT_OWNER_GOV_5_CLOSURE_DECISION"
ALLOWED_REVIEW_RESULTS = {
    READY_REVIEW_RESULT,
    "RETURN_FOR_REMEDIATION",
    "OWNER_DECISION_REQUIRED_BEFORE_GOV_5_CLOSURE",
    "INVALID_REVIEW",
}


def markdown_state(path: Path, marker: str) -> dict:
    text = path.read_text()
    match = re.search(
        rf"<!-- {re.escape(marker)} -->\n```yaml\n(?P<body>.*?)\n```",
        text,
        re.DOTALL,
    )
    if not match:
        raise ValueError(f"{path}: missing structured marker {marker}")
    from _lib.strict_yaml import loads

    return loads(match.group("body"), f"{path}:{marker}")


def markdown_yaml_section(path: Path, heading: str) -> dict:
    text = path.read_text()
    match = re.search(
        rf"^{re.escape(heading)}\n\n```yaml\n(?P<body>.*?)\n```",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ValueError(f"{path}: missing structured section {heading}")
    from _lib.strict_yaml import loads

    return loads(match.group("body"), f"{path}:{heading}")


def markdown_table(path: Path, heading: str) -> dict[str, str]:
    text = path.read_text()
    start = text.find(heading)
    if start < 0:
        raise ValueError(f"{path}: missing table section {heading}")
    lines = text[start + len(heading):].splitlines()
    table_lines: list[str] = []
    started = False
    for line in lines:
        if line.startswith("|"):
            started = True
            table_lines.append(line)
        elif started:
            break
    if len(table_lines) < 3:
        raise ValueError(f"{path}: incomplete table section {heading}")
    result: dict[str, str] = {}
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 2 or cells[0] in result:
            raise ValueError(f"{path}: invalid table row in {heading}")
        result[cells[0]] = cells[1]
    return result


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_executed_review(review: dict, errors: list[str]) -> None:
    expected_flags = {
        "status": READY_REVIEW_STATUS,
        "authority": "NONE",
        "authoritative_to_accept_run": False,
        "authoritative_to_close_phase": False,
        "phase_transition_requested": False,
        "creates_new_governance_layer": False,
        "accepts_risk": False,
        "ratifies_kernel": False,
        "activates_gov_6": False,
    }
    for key, value in expected_flags.items():
        if review.get(key) != value:
            errors.append(f"executed closure review {key} mismatch")
    if review.get("completion_gate", {}).get("overall_satisfied") is not True:
        errors.append("executed closure review GOV-5 completion gate mismatch")
    for gate in ("clause_feasibility_and_coverage", "unresolved_owner_decisions"):
        if review.get("completion_gate", {}).get(gate, {}).get("satisfied") is not True:
            errors.append(f"executed closure review gate {gate} mismatch")

    result_values: list[str] = []
    def collect(value):
        if isinstance(value, dict):
            for item in value.values():
                collect(item)
        elif isinstance(value, list):
            for item in value:
                collect(item)
        elif value in ALLOWED_REVIEW_RESULTS:
            result_values.append(value)
    collect(review)
    if result_values != [READY_REVIEW_RESULT] or review.get("review_result") != READY_REVIEW_RESULT:
        errors.append("executed closure review must emit exactly one allowed ready result")

    required_item_fields = set(review.get("item_field_contract", {}).get("required_fields", []))
    expected_item_fields = {
        "id", "category", "item", "current_status", "evidence", "closure_relevance",
        "blocks_gov_5_closure", "legitimate_deferral_destination",
        "future_action_trigger", "owner_decision_required",
    }
    if required_item_fields != expected_item_fields:
        errors.append("executed closure review item field contract mismatch")
    items = review.get("items", [])
    ids = [item.get("id") for item in items if isinstance(item, dict)]
    if len(ids) != len(set(ids)) or len(ids) != len(items):
        errors.append("executed closure review item IDs must be unique")
    for item in items:
        if set(item) != expected_item_fields:
            errors.append(f"executed closure review item field mismatch: {item.get('id')}")
        if not isinstance(item.get("evidence"), list) or not item.get("evidence"):
            errors.append(f"executed closure review item evidence missing: {item.get('id')}")
        if not isinstance(item.get("blocks_gov_5_closure"), bool):
            errors.append(f"executed closure review item blocking value invalid: {item.get('id')}")
    if {f"RR-{number:03d}" for number in range(1, 16)} - set(ids):
        errors.append("executed closure review must classify all fifteen residual risks")
    if {f"SD-{number:03d}" for number in range(1, 5)} - set(ids):
        errors.append("executed closure review must classify all four specialist dependencies")
    if {f"OD-{number:03d}" for number in range(1, 7)} - set(ids):
        errors.append("executed closure review must classify OD-001 through OD-006")
    for required in (
        "HP-FAIL-005", "HP-FAIL-020", "IE-MC-001", "IE-MC-002", "IE-MC-003",
        "MINIMUM-GOV-7-RECOMMENDATION", "PROJECT-OWNER-KGR-006-R1-ACCEPTANCE",
        "PROJECT-OWNER-GOV-5-CLOSURE", "PHASE-TRANSITION-BOUNDARY",
    ):
        if required not in ids:
            errors.append(f"executed closure review missing material item {required}")

    reassessments = review.get("explicit_reassessments", {})
    if reassessments.get("HP-FAIL-005", {}).get("blocks_gov_5") is not False or reassessments.get("HP-FAIL-005", {}).get("blocks_gov_6") is not False:
        errors.append("executed closure review HP-FAIL-005 reassessment mismatch")
    if reassessments.get("HP-FAIL-020_recurrence", {}).get("validated_before_review") is not True:
        errors.append("executed closure review HP-FAIL-020 recurrence validation mismatch")
    if reassessments.get("OD-002_and_OD-003", {}).get("fully_satisfy_decisions_required_before_gov_6") is not True:
        errors.append("executed closure review OD-002/OD-003 reassessment mismatch")
    if reassessments.get("OD-004", {}).get("disposition") != "CORRECTLY_ROUTED_TO_GOV_6":
        errors.append("executed closure review OD-004 disposition mismatch")
    if reassessments.get("OD-005", {}).get("disposition") != "CORRECTLY_ROUTED_AFTER_ANY_RATIFICATION_AND_BEFORE_AFFECTED_GOV_7_WORK":
        errors.append("executed closure review OD-005 disposition mismatch")
    if reassessments.get("OD-006", {}).get("disposition") != "MAY_REMAIN_DEFERRED_UNTIL_RELEVANT_PROVIDER_DATA_PILOT_OR_REAL_WORLD_BOUNDARY":
        errors.append("executed closure review OD-006 disposition mismatch")
    risks = reassessments.get("residual_risks", {})
    if risks.get("exact_count") != 15 or risks.get("accepted") is not False or risks.get("routed") is not True:
        errors.append("executed closure review residual-risk treatment mismatch")
    dependencies = reassessments.get("specialist_dependencies", {})
    if dependencies.get("exact_count") != 4 or dependencies.get("trigger_gated_correctly") is not True:
        errors.append("executed closure review specialist-dependency treatment mismatch")
    if reassessments.get("research_items", {}).get("blocks_constitutional_ratification") is not False:
        errors.append("executed closure review research-item reassessment mismatch")

    disposition = review.get("readiness_disposition", {})
    if disposition.get("gate_satisfied") is not True or disposition.get("remediation_required") != []:
        errors.append("executed closure review readiness disposition mismatch")
    if disposition.get("blocking_items") != [
        "PROJECT-OWNER-KGR-006-R1-ACCEPTANCE", "PROJECT-OWNER-GOV-5-CLOSURE"
    ]:
        errors.append("executed closure review blocking items mismatch")
    state = review.get("resulting_state", {})
    if state.get("KGR-006-R1", {}).get("project_owner_acceptance") != "PENDING":
        errors.append("executed closure review acceptance state mismatch")
    if state.get("GOV-5") != {
        "status": "IN_PROGRESS", "closure_review": READY_REVIEW_STATUS, "closed": False
    }:
        errors.append("executed closure review GOV-5 resulting state mismatch")
    if [state.get(f"GOV-{number}") for number in range(6, 10)] != ["INACTIVE"] * 4:
        errors.append("executed closure review later-phase state mismatch")
    if state.get("kernel") != "0.2.0-proposed/PROPOSED_NOT_RATIFIED":
        errors.append("executed closure review Kernel state mismatch")


def validate_markdown_links(root: Path, paths: list[Path], errors: list[str]) -> None:
    for relative in paths:
        path = root / relative
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local = target.split("#", 1)[0]
            if not local:
                continue
            candidate = (path.parent / local).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                errors.append(f"Markdown link escapes repository: {relative} -> {target}")
                continue
            if not candidate.exists():
                errors.append(f"Markdown link target missing: {relative} -> {target}")


def validate(root: Path) -> dict:
    errors: list[str] = []
    run = load(root / RUN_REL / "run-manifest.yaml")
    authorization = load(root / RUN_REL / "authorization/execution-authorization.yaml")["execution_authorization"]
    decisions = load(root / DECISION_RECORD_REL)["project_owner_decision_record"]
    ratification = load(root / RATIFICATION_RECORD_REL)["kernel_ratification_decision_record"]
    gov_7_direction = load(root / GOV_7_DIRECTION_RECORD_REL)["gov_7_direction_decision_record"]
    executed_review = load(root / EXECUTED_REVIEW_REL)["phase_closure_readiness_review"]
    registry = load(root / "governance/ARTIFACT_REGISTRY.yaml")
    current_path = root / "governance/CURRENT_STATE.md"
    plan_path = root / "governance/GOVERNANCE_MASTER_PLAN.md"
    readme_path = root / "governance/README.md"
    current = markdown_state(current_path, "GOVERNANCE_STATE_V1")["governance_state"]
    current_durable = markdown_yaml_section(current_path, "## Durable state")
    current_table = markdown_table(current_path, "# Current Governance State")
    plan = markdown_state(plan_path, "GOVERNANCE_STATE_V1")["governance_state"]
    plan_table = markdown_table(plan_path, "## Status summary")
    readme = markdown_state(readme_path, "GOVERNANCE_STATE_V1")["governance_state"]
    log = (root / "governance/DECISION_LOG.md").read_text()

    validate_executed_review(executed_review, errors)

    expected_decisions = {
        "KGR-006-R1": ("ACCEPTED_BY_PROJECT_OWNER", None),
        "GOV-5": ("COMPLETED_CLOSED", None),
        "OD-002": ("RESOLVED", "CONFIRM_EXACT_SCOPE"),
        "OD-003": ("RESOLVED", "PACKET_SUFFICIENT"),
        "OD-004": ("UNRESOLVED", None),
        "OD-005": ("UNRESOLVED", None),
        "OD-006": ("UNRESOLVED", None),
    }
    actual_decisions = {
        item["id"]: (item["status"], item.get("selection"))
        for item in decisions.get("decisions", [])
    }
    if actual_decisions != expected_decisions:
        errors.append("Owner decision record state mismatch")
    decisions_by_id = {item["id"]: item for item in decisions.get("decisions", [])}
    if decisions_by_id.get("KGR-006-R1", {}).get("decision") != "ACCEPT_KGR_006_R1":
        errors.append("Owner decision record KGR-006-R1 acceptance mismatch")
    if decisions_by_id.get("GOV-5", {}).get("decision") != "CLOSE_GOV_5":
        errors.append("Owner decision record GOV-5 closure mismatch")
    if decisions.get("status") != "ACCEPTED_KGR_006_R1_AND_GOV_5_CLOSED":
        errors.append("Owner decision record status mismatch")
    if decisions.get("additional_owner_rationale") != "NOT_PROVIDED":
        errors.append("Owner decision rationale must remain NOT_PROVIDED")

    if ratification.get("document_id") != "GOV-DECISION-RECORD-002" or ratification.get("status") != "RATIFIED_EXACT_KERNEL_0_2_0_GOV_6_CLOSED":
        errors.append("GOV-6 ratification record identity or status mismatch")
    decision = ratification.get("decision", {})
    if decision != {
        "id": "OD-004",
        "selection": "RATIFY_EXACT_KERNEL_0_2_0",
        "status": "RESOLVED_RATIFY_EXACT_KERNEL_0_2_0",
    }:
        errors.append("GOV-6 ratification record OD-004 mismatch")
    kernel = ratification.get("ratified_kernel", {})
    if kernel.get("version") != "0.2.0" or kernel.get("scope") != "HugePlanning level 3 under the Kernel scope rules":
        errors.append("GOV-6 ratification record Kernel version or scope mismatch")
    conditions = ratification.get("ratification_conditions", {})
    if conditions != {
        "residual_risk_accepted": False,
        "enforceability_claimed": False,
        "implementation_status": "NOT_PERFORMED",
        "gov_7_authorized": False,
        "provider_or_real_data_authorized": False,
    }:
        errors.append("GOV-6 ratification conditions mismatch")
    resulting = ratification.get("resulting_state", {})
    expected_ratification_state = {
        "OD-004": "RESOLVED_RATIFY_EXACT_KERNEL_0_2_0",
        "kernel": "0.2.0/RATIFIED",
        "GOV-6": "COMPLETED_CLOSED",
        "GOV-7": "INACTIVE",
        "OD-005": "UNRESOLVED",
        "OD-006": "UNRESOLVED_TRIGGER_GATED",
        "residual-risk-accepted": False,
        "enforcement-implementation": "NOT_PERFORMED",
        "minimum-GOV-7-package": "RECOMMENDATION_ONLY",
    }
    if resulting != expected_ratification_state:
        errors.append("GOV-6 ratification resulting state mismatch")

    if gov_7_direction.get("document_id") != "GOV-DECISION-RECORD-003" or gov_7_direction.get("status") != "RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION":
        errors.append("OD-005 direction record identity or status mismatch")
    if gov_7_direction.get("decision") != {
        "id": "OD-005",
        "selection": "ACCEPT_MINIMUM_GOV_7_DIRECTION",
        "status": "RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION",
    }:
        errors.append("OD-005 direction record decision mismatch")
    if gov_7_direction.get("accepted") != [
        "seven-component capability direction",
        "one bounded governed transition as the initial target",
        "reuse of existing deterministic custody and validation primitives",
        "read-only tooling and methodology audit",
        "GOV-7 design preparation",
    ]:
        errors.append("OD-005 direction record accepted scope mismatch")
    if gov_7_direction.get("authority_exclusions") != [
        "GOV_7_IMPLEMENTATION",
        "GOV_7_REPOSITORY_MODIFICATIONS_BEYOND_THIS_DECISION_CUSTODY",
        "TECHNOLOGY_OR_FRAMEWORK_ADOPTION",
        "PROVIDER_USE",
        "REAL_DATA_PROCESSING",
        "PILOT_EXECUTION",
        "RESIDUAL_RISK_ACCEPTANCE",
        "OD_006_RESOLUTION",
    ]:
        errors.append("OD-005 direction record authority exclusions mismatch")
    expected_direction_state = {
        "OD-005": "RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION",
        "GOV-7": "INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY",
        "OD-006": "UNRESOLVED_TRIGGER_GATED",
        "minimum-GOV-7-package": "DIRECTION_ACCEPTED_NOT_IMPLEMENTED",
        "residual-risk-accepted": False,
        "enforcement-implementation": "NOT_PERFORMED",
    }
    if gov_7_direction.get("resulting_state") != expected_direction_state:
        errors.append("OD-005 direction record resulting state mismatch")
    if gov_7_direction.get("constitutional_authority") != "PROJECT_OWNER_DIRECTION_DECISION_ONLY":
        errors.append("OD-005 direction record authority mismatch")
    for fragment in (
        "## GOV-DEC-026 — OD-005 minimum GOV-7 direction",
        "Status: RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION",
        "Source: Project Owner instruction `HP-PROMPT-022/0.1.0` and `GOV-DECISION-RECORD-003/0.1.0`.",
        "GOV-7 remains `INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY`",
    ):
        if fragment not in log:
            errors.append("OD-005 decision log custody mismatch")

    expected_authorization = {
        "status": "CONSUMED",
        "execution_count_limit": 1,
        "execution_count_consumed": 1,
        "execution_available": False,
        "consumed_by_output_package_sha256": OUTPUT_SHA256,
    }
    for key, value in expected_authorization.items():
        if authorization.get(key) != value:
            errors.append(f"authorization {key} mismatch")
    terminal = authorization.get("terminal_reconciliation", {})
    if terminal.get("decision_log_entry") != "GOV-DEC-020" or terminal.get("creates_new_execution_authority") is not False:
        errors.append("authorization is missing terminal GOV-DEC-020 reconciliation")
    if f"consuming output SHA-256: `{OUTPUT_SHA256}`" not in log:
        errors.append("decision log terminal authorization hash mismatch or reconciliation missing")

    run_decisions = run.get("owner_decisions", {})
    if run.get("run", {}).get("status") != "ACCEPTED_BY_PROJECT_OWNER":
        errors.append("run manifest KGR-006-R1 state mismatch")
    if run_decisions.get("OD-002") != "RESOLVED_CONFIRM_EXACT_SCOPE" or run_decisions.get("OD-003") != "RESOLVED_PACKET_SUFFICIENT":
        errors.append("run manifest OD-002/OD-003 state mismatch")
    if [run_decisions.get(item) for item in ("OD-004", "OD-005", "OD-006")] != ["UNRESOLVED"] * 3:
        errors.append("run manifest must leave OD-004 through OD-006 unresolved")
    run_review = run.get("phase_closure_review", {})
    if run.get("run", {}).get("readiness") != "ACCEPTED_BY_PROJECT_OWNER_GOV_5_CLOSED_READY_FOR_SEPARATE_GOV_6_DECISION":
        errors.append("run manifest closure-review readiness mismatch")
    if run_review != {
        "path": EXECUTED_REVIEW_REL.as_posix(),
        "status": READY_REVIEW_STATUS,
        "result": READY_REVIEW_RESULT,
        "authoritative_to_accept_run": False,
        "authoritative_to_close_phase": False,
        "gov_5_closed": True,
        "gov_6_activated": False,
    }:
        errors.append("run manifest phase-closure review state mismatch")

    surfaces = {"CURRENT_STATE": current, "GOVERNANCE_MASTER_PLAN": plan, "README": readme}
    expected_surface = {
        "phase": "GOV-6_CLOSED",
        "gov_5_status": "COMPLETED_CLOSED",
        "gov_5_closure_review": READY_REVIEW_STATUS,
        "kgr_006_r1_status": "ACCEPTED_BY_PROJECT_OWNER",
        "authorization_status": "CONSUMED_1_OF_1_NONE_REMAINING",
        "od_002": "RESOLVED_CONFIRM_EXACT_SCOPE",
        "od_003": "RESOLVED_PACKET_SUFFICIENT",
        "od_004": "RESOLVED_RATIFY_EXACT_KERNEL_0_2_0",
        "od_005": "RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION",
        "od_006": "UNRESOLVED_TRIGGER_GATED",
        "gov_6_status": "COMPLETED_CLOSED",
        "gov_7_status": "INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY",
        "gov_8_through_gov_9": "INACTIVE",
        "kernel": "0.2.0/RATIFIED",
        "minimum_gov_7_package": "DIRECTION_ACCEPTED_NOT_IMPLEMENTED",
        "risk_accepted": False,
        "enforcement_implementation": "NOT_PERFORMED",
    }
    for name, surface in surfaces.items():
        for key, value in expected_surface.items():
            if surface.get(key) != value:
                errors.append(f"{name} {key} mismatch")

    durable_run = current_durable.get("KGR-006-R1", {})
    if durable_run.get("status") != "ACCEPTED_BY_PROJECT_OWNER":
        errors.append("CURRENT_STATE Durable state KGR-006-R1 status mismatch")
    if durable_run.get("project_owner_acceptance") != "ACCEPTED_BY_PROJECT_OWNER":
        errors.append("CURRENT_STATE Durable state Project Owner acceptance mismatch")
    if durable_run.get("owner_decisions") != {
        "OD-002": "RESOLVED_CONFIRM_EXACT_SCOPE",
        "OD-003": "RESOLVED_PACKET_SUFFICIENT",
        "OD-004": "UNRESOLVED",
        "OD-005": "UNRESOLVED",
        "OD-006": "UNRESOLVED",
    }:
        errors.append("CURRENT_STATE Durable state Owner decisions mismatch")
    durable_gov_5 = current_durable.get("GOV-5", {})
    if durable_gov_5.get("status") != "COMPLETED_CLOSED" or durable_gov_5.get("closed") is not True:
        errors.append("CURRENT_STATE Durable state GOV-5 closed status mismatch")
    if durable_gov_5.get("closure_review") != READY_REVIEW_STATUS:
        errors.append("CURRENT_STATE Durable state GOV-5 closure review mismatch")
    if current_durable.get("GOV-6", {}).get("status") != "COMPLETED_CLOSED" or current_durable.get("GOV-7") != {
        "status": "INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY",
        "decision": "OD-005",
        "direction_record": "GOV-DECISION-RECORD-003/0.1.0",
        "minimum_package": "DIRECTION_ACCEPTED_NOT_IMPLEMENTED",
    } or [current_durable.get(f"GOV-{number}", {}).get("status") for number in range(8, 10)] != ["INACTIVE"] * 2:
        errors.append("CURRENT_STATE Durable state GOV-6 closure or later-phase state mismatch")
    if current_durable.get("kernel") != {
        "version": "0.2.0",
        "status": "RATIFIED",
        "scope": "HugePlanning level 3 under the Kernel scope rules",
        "ratification_record": "GOV-DECISION-RECORD-002/0.1.0",
        "enforceability_claimed": False,
        "implementation_status": "NOT_PERFORMED",
        "operational": False,
    }:
        errors.append("CURRENT_STATE Durable state Kernel mismatch")

    current_table_expectations = {
        "Current governance phase": ("GOV-6", "COMPLETED / CLOSED", "ratified exact Kernel `0.2.0`"),
        "GOV-5 status": ("COMPLETED / CLOSED", "ACCEPTED_BY_PROJECT_OWNER", f"closure review remains `{READY_REVIEW_STATUS}`"),
        "Enforcement Engineering gate": ("CLOSED", "1 of 1"),
        "GOV-6 status": ("COMPLETED / CLOSED", "ratified exact Kernel `0.2.0`"),
        "Human ratification": ("RATIFIED", "0.2.0"),
        "Phase-transition boundary": ("GOV-6 is closed", "GOV-7 remains inactive pending audit and separate design or implementation authority"),
    }
    for row, fragments in current_table_expectations.items():
        value = current_table.get(row, "")
        if not all(fragment in value for fragment in fragments):
            errors.append(f"CURRENT_STATE table {row} mismatch")

    plan_table_expectations = {
        "GOV-5 Enforcement analysis and derived governance requirements": ("COMPLETED / CLOSED", "KGR-006-R1 accepted by the Project Owner"),
        "GOV-6 Human ratification": ("COMPLETED / CLOSED", "ratified exact Kernel `0.2.0`"),
        "GOV-7 Minimum executable governance bootstrap": ("INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY", "DIRECTION_ACCEPTED_NOT_IMPLEMENTED"),
        "GOV-8 Honest S0a–S1 adoption and regularization": ("PLANNED",),
        "GOV-9 S2 governed pilot": ("PLANNED",),
    }
    for row, fragments in plan_table_expectations.items():
        value = plan_table.get(row, "")
        if not all(fragment in value for fragment in fragments):
            errors.append(f"GOVERNANCE_MASTER_PLAN table {row} mismatch")

    artifacts = {item.get("id"): item for item in registry.get("artifacts", [])}
    if len(artifacts) != len(registry.get("artifacts", [])):
        errors.append("artifact registry IDs must be unique")
    for artifact_id, artifact in artifacts.items():
        value = artifact.get("path")
        if not isinstance(value, str):
            errors.append(f"artifact registry path missing for {artifact_id}")
            continue
        pure = PurePosixPath(value.rstrip("/"))
        if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
            errors.append(f"artifact registry path unsafe for {artifact_id}")
            continue
        if not (root / Path(*pure.parts)).exists():
            errors.append(f"artifact registry path missing for {artifact_id}")
    for required in (
        "KGR-006-R1", "GOV-AUTH-001", "GOV-DECISION-RECORD-001",
        "GOV-VAL-008", "GOV-REVIEW-014", "HP-PROMPT-018",
        "GOV-VAL-009", "GOV-REVIEW-015", "GOV-REVIEW-016", "HP-PROMPT-019", "HP-PROMPT-020",
        "GOV-DECISION-RECORD-002", "HP-PROMPT-021", "GOV-DECISION-RECORD-003", "HP-PROMPT-022",
    ):
        if required not in artifacts:
            errors.append(f"artifact registry missing {required}")
        elif not (root / artifacts[required]["path"]).exists():
            errors.append(f"artifact registry path missing for {required}")
    auth_entry = artifacts.get("GOV-AUTH-001", {})
    if auth_entry.get("status") != "CONSUMED" or OUTPUT_SHA256 not in " ".join(auth_entry.get("notes", [])):
        errors.append("artifact registry authorization terminal state mismatch")
    run_entry = artifacts.get("KGR-006-R1", {})
    if run_entry.get("status") != "ACCEPTED_BY_PROJECT_OWNER":
        errors.append("artifact registry KGR-006-R1 state mismatch")
    direction_entry = artifacts.get("GOV-DECISION-RECORD-003", {})
    if direction_entry.get("status") != "RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION" or direction_entry.get("source_path") != "governance/prompts/orchestration/HP-PROMPT-022-record-od-005-gov-7-direction-decision-v0.1.0.md":
        errors.append("artifact registry OD-005 direction decision custody mismatch")
    prompt_entry = artifacts.get("HP-PROMPT-022", {})
    if prompt_entry.get("status") != "EXECUTED" or prompt_entry.get("aliases") != ["GOV-DEC-026"]:
        errors.append("artifact registry HP-PROMPT-022 custody mismatch")

    immutable = load(root / REVIEW_REL / "kgr-006-r1-import-validation-v0.1.0.yaml")["subject"]
    for group, directory in (("source_package", "outputs"), ("evaluation_package", "evaluation")):
        for item in immutable[group]["inventory"]:
            path = root / RUN_REL / directory / item["member"]
            if sha256(path) != item["sha256"]:
                errors.append(f"immutable artifact hash mismatch: {path.relative_to(root)}")

    validate_markdown_links(root, [
        Path("governance/CURRENT_STATE.md"),
        Path("governance/GOVERNANCE_MASTER_PLAN.md"),
        Path("governance/README.md"),
        Path("governance/learning/FAILURE_AND_LESSONS_INDEX.md"),
        Path("governance/prompts/orchestration/HP-PROMPT-019-gov-5-phase-closure-readiness-review-v0.1.0.md"),
        Path("governance/prompts/orchestration/HP-PROMPT-020-accept-kgr-006-r1-and-close-gov-5-v0.1.0.md"),
        Path("governance/prompts/orchestration/HP-PROMPT-021-ratify-kernel-0-2-0-and-close-gov-6-v0.1.0.md"),
        Path("governance/prompts/orchestration/HP-PROMPT-022-record-od-005-gov-7-direction-decision-v0.1.0.md"),
        REVIEW_REL / "gov-5-phase-closure-readiness-implementation-report-v0.1.0.md",
    ], errors)

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
