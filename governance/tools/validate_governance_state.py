#!/usr/bin/env python3
"""Validate the durable KGR-006-R1/GOV-5 state across governance surfaces."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib.strict_yaml import load


OUTPUT_SHA256 = "0f496b5b17feb724977f189413f485100b9a66d98b1f79dc05cf45fb60aee66b"
RUN_REL = Path("governance/runs/KGR-006-R1-enforcement-analysis-correction")
REVIEW_REL = Path("governance/reviews/kgr-006-r1-controlled-import-and-owner-review")
DECISION_RECORD_REL = REVIEW_REL / "project-owner-decision-record-v0.1.0.yaml"


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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root: Path) -> dict:
    errors: list[str] = []
    run = load(root / RUN_REL / "run-manifest.yaml")
    authorization = load(root / RUN_REL / "authorization/execution-authorization.yaml")["execution_authorization"]
    decisions = load(root / DECISION_RECORD_REL)["project_owner_decision_record"]
    registry = load(root / "governance/ARTIFACT_REGISTRY.yaml")
    current = markdown_state(root / "governance/CURRENT_STATE.md", "GOVERNANCE_STATE_V1")["governance_state"]
    plan = markdown_state(root / "governance/GOVERNANCE_MASTER_PLAN.md", "GOVERNANCE_STATE_V1")["governance_state"]
    readme = markdown_state(root / "governance/README.md", "GOVERNANCE_STATE_V1")["governance_state"]
    log = (root / "governance/DECISION_LOG.md").read_text()

    expected_decisions = {
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
        errors.append("Owner decision record must resolve only OD-002 and OD-003 with the exact selections")
    if decisions.get("additional_owner_rationale") != "NOT_PROVIDED":
        errors.append("Owner decision rationale must remain NOT_PROVIDED")

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
    if run.get("run", {}).get("status") != "IMPORTED_AND_EVALUATED_PENDING_PROJECT_OWNER_ACCEPTANCE":
        errors.append("run manifest KGR-006-R1 state mismatch")
    if run_decisions.get("OD-002") != "RESOLVED_CONFIRM_EXACT_SCOPE" or run_decisions.get("OD-003") != "RESOLVED_PACKET_SUFFICIENT":
        errors.append("run manifest OD-002/OD-003 state mismatch")
    if [run_decisions.get(item) for item in ("OD-004", "OD-005", "OD-006")] != ["UNRESOLVED"] * 3:
        errors.append("run manifest must leave OD-004 through OD-006 unresolved")

    surfaces = {"CURRENT_STATE": current, "GOVERNANCE_MASTER_PLAN": plan, "README": readme}
    expected_surface = {
        "phase": "GOV-5",
        "gov_5_status": "IN_PROGRESS",
        "gov_5_closure_review": "NOT_EXECUTED",
        "kgr_006_r1_status": "IMPORTED_AND_EVALUATED_PENDING_PROJECT_OWNER_ACCEPTANCE",
        "authorization_status": "CONSUMED_1_OF_1_NONE_REMAINING",
        "od_002": "RESOLVED_CONFIRM_EXACT_SCOPE",
        "od_003": "RESOLVED_PACKET_SUFFICIENT",
        "od_004_through_od_006": "UNRESOLVED",
        "gov_6_through_gov_9": "INACTIVE",
        "kernel": "0.2.0-proposed/PROPOSED_NOT_RATIFIED",
        "minimum_gov_7_package": "RECOMMENDATION_ONLY",
        "risk_accepted": False,
        "enforcement_implementation": "NOT_PERFORMED",
    }
    for name, surface in surfaces.items():
        for key, value in expected_surface.items():
            if surface.get(key) != value:
                errors.append(f"{name} {key} mismatch")

    artifacts = {item.get("id"): item for item in registry.get("artifacts", [])}
    for required in (
        "KGR-006-R1", "GOV-AUTH-001", "GOV-DECISION-RECORD-001",
        "GOV-VAL-008", "GOV-REVIEW-014", "HP-PROMPT-018",
    ):
        if required not in artifacts:
            errors.append(f"artifact registry missing {required}")
        elif not (root / artifacts[required]["path"]).exists():
            errors.append(f"artifact registry path missing for {required}")
    auth_entry = artifacts.get("GOV-AUTH-001", {})
    if auth_entry.get("status") != "CONSUMED" or OUTPUT_SHA256 not in " ".join(auth_entry.get("notes", [])):
        errors.append("artifact registry authorization terminal state mismatch")
    run_entry = artifacts.get("KGR-006-R1", {})
    if run_entry.get("status") != "IMPORTED_AND_EVALUATED_PENDING_PROJECT_OWNER_ACCEPTANCE":
        errors.append("artifact registry KGR-006-R1 state mismatch")

    immutable = load(root / REVIEW_REL / "kgr-006-r1-import-validation-v0.1.0.yaml")["subject"]
    for group, directory in (("source_package", "outputs"), ("evaluation_package", "evaluation")):
        for item in immutable[group]["inventory"]:
            path = root / RUN_REL / directory / item["member"]
            if sha256(path) != item["sha256"]:
                errors.append(f"immutable artifact hash mismatch: {path.relative_to(root)}")

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
