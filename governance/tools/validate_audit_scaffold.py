#!/usr/bin/env python3
"""Validate the planning-only GOV-AUD-001 audit program scaffold."""

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
PASS_IDS = [f"PASS-{number:02d}" for number in range(1, 8)]
PROMPT_IDS = ["GOV-AUD-PROMPT-000"] + [f"GOV-AUD-PROMPT-{number:03d}" for number in range(10, 71, 10)]
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

    if plan.get("audit_id") != "GOV-AUD-001" or plan.get("status") != "PLANNED_NOT_EXECUTED":
        errors.append("audit identity or planning status mismatch")
    for key, expected in {
        "passes_executed": 0, "checkpoints_approved": 0, "gov_7_activated": False,
        "recommendations_accepted": False, "implementation_authorized": False,
        "graph_technology_selected": False, "vertical_slice_selected": False,
        "audit_executed": False,
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
    for item in sequence:
        expected_status = "PENDING_OWNER_DECISION" if item.get("id", "").startswith("CHECKPOINT") else "PLANNED_NOT_EXECUTED"
        if item.get("status") != expected_status:
            errors.append(f"sequence status mismatch: {item.get('id')}")

    audit_status = status.get("audit", {})
    for key, expected in {
        "id": "GOV-AUD-001", "status": "PLANNED_NOT_EXECUTED", "passes_executed": 0,
        "checkpoints_completed": 0, "gov_7_activated": False,
        "recommendations_accepted": False, "implementation_authorized": False,
        "audit_execution_authorized": False, "graph_implemented": False,
        "telemetry_implemented": False, "interviewer_simulation_implemented": False,
        "self_hosting_implemented": False, "owner_decision_inferred": False,
    }.items():
        if audit_status.get(key) != expected:
            errors.append(f"audit status {key} mismatch")
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
    identities = [(item.get("prompt_id"), str(item.get("version"))) for item in prompts]
    if [item[0] for item in identities] != PROMPT_IDS or len(identities) != len(set(identities)):
        errors.append("prompt registry identity/order mismatch")
    for item in prompts:
        path = root / item.get("path", "")
        if not path.is_file():
            errors.append(f"registered prompt path missing: {item.get('prompt_id')}")
        if item.get("prompt_id") == "GOV-AUD-PROMPT-000":
            if item.get("lifecycle") != "EXECUTED" or item.get("exact_text_sha256") != PROMPT_HASH or item.get("audit_pass_executed") is not False:
                errors.append("scaffold prompt registry metadata mismatch")
        elif item.get("lifecycle") != "TEMPLATE":
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

    run_members = sorted(path.relative_to(audit / "runs").as_posix() for path in (audit / "runs").rglob("*") if path.is_file())
    decision_members = sorted(path.relative_to(audit / "decisions").as_posix() for path in (audit / "decisions").rglob("*") if path.is_file())
    if run_members != ["README.md"] or decision_members != ["README.md"]:
        errors.append("fake or placeholder execution/decision artifacts detected")
    forbidden_names = {"output", "outputs", "evaluation", "telemetry", "projection", "graph"}
    for path in audit.rglob("*"):
        if path.is_dir() and path.name.lower() in forbidden_names:
            errors.append(f"forbidden placeholder implementation/output directory: {path.relative_to(audit)}")

    global_registry = load(root / "governance/ARTIFACT_REGISTRY.yaml")
    artifact_ids = [item.get("id") for item in global_registry.get("artifacts", [])]
    if len(artifact_ids) != len(set(artifact_ids)):
        errors.append("global artifact registry contains duplicate IDs")
    for required_id in ("GOV-AUD-001", "HP-PROMPT-023", "GOV-TOOL-004"):
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
