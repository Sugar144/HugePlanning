#!/usr/bin/env python3
"""Validate a technology-neutral PASS-02 architecture candidate generically."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib.strict_yaml import load, loads
from validate_pass_03_execution import SUCCESS as PASS_03_SUCCESS, validate as validate_pass_03_execution


RUN_REL = Path(
    "governance/audits/GOV-AUD-001-gov7-enablement/"
    "runs/GOV-AUD-001-P02-R1"
)
OUTPUT_NAMES = {
    "01-bounded-context-and-ownership-model.yaml",
    "02-cross-layer-interface-and-contract-assessment.md",
    "03-typed-relationship-and-query-model.yaml",
    "04-version-migration-and-impact-model.md",
    "05-controlled-self-hosting-and-trust-boundaries.md",
    "06-architecture-style-comparison.yaml",
    "07-pass-02-findings-and-checkpoint-a-handoff.md",
}
LABELS = {
    "VERIFIED_FACT",
    "INFERENCE",
    "PROPOSAL",
    "RECOMMENDATION",
    "OWNER_DECISION_REQUIRED",
    "DEFERRED",
    "REJECTED",
}
QUERY_COVERAGE = {
    "CLAUSE_TO_CONTROLS",
    "REQUIREMENT_TO_STAGES",
    "CONTROL_TO_EXECUTOR_VALIDATOR",
    "CLAIM_TO_EVIDENCE_TEST",
    "TRANSITION_TO_BLOCKING_GATE",
    "FINDING_TO_OWNER",
    "SCHEMA_CHANGE_IMPACT",
    "REQUIREMENT_CHANGE_IMPACT",
    "PROJECT_MIGRATION_SET",
    "HISTORICAL_CORRECTION_LINEAGE",
    "COMPATIBILITY_CHECK",
    "METHODOLOGY_STAGE_CHANGE_IMPACT",
    "AGENT_SKILL_CHANGE_IMPACT",
    "VALIDATOR_CHANGE_IMPACT",
    "CONTROL_SUPERSESSION_IMPACT",
    "INDEPENDENCE_CHAIN_AUDIT",
}
PASS_03_PREPARATION_STATES = {
    "AUTHORIZED_FOR_PREPARATION_NOT_EXECUTION",
    "PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION",
}
CONTEXT_FIELDS = {
    "context_id",
    "purpose",
    "canonical_owner",
    "owned_state_and_artifacts",
    "accepted_inputs",
    "produced_outputs",
    "allowed_writers",
    "allowed_readers",
    "authority_level",
    "source_of_truth",
    "derived_non_authoritative_projections",
    "failure_boundary",
    "stopping_condition",
    "recovery_path",
    "manual_escape_path",
}
RELATIONSHIP_FIELDS = {
    "type_name",
    "statement_label",
    "source_entity_kinds",
    "target_entity_kinds",
    "direction",
    "cardinality",
    "required_provenance",
    "validity_version_fields",
    "authority",
    "validation_rule",
    "invalidation_or_supersession",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or (boundary := text.find("\n---\n", 4)) < 0:
        raise ValueError(f"{path}: missing YAML front matter")
    metadata = loads(text[4:boundary], str(path))
    if not isinstance(metadata, dict):
        raise ValueError(f"{path}: front matter must be a mapping")
    return metadata, text[boundary + 5 :]


def unique(values: list[Any], label: str, errors: list[str]) -> None:
    if len(values) != len(set(values)):
        errors.append(f"duplicate {label}")


def git_blob(root: Path, revision: str, relative: str) -> bytes | None:
    result = subprocess.run(
        ["git", "-C", str(root), "show", f"{revision}:{relative}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.stdout if result.returncode == 0 else None


def validate_markdown(path: Path, root: Path, errors: list[str]) -> dict[str, Any]:
    try:
        metadata, body = frontmatter(path)
    except Exception as exc:
        errors.append(str(exc))
        return {}
    if body.count("```") % 2:
        errors.append(f"Markdown fence mismatch: {path.relative_to(root)}")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local = target.split("#", 1)[0]
        if local and not (path.parent / local).resolve().exists():
            errors.append(f"Markdown link missing: {path.relative_to(root)} -> {target}")
    observed_labels = set(re.findall(r"\*\*([A-Z][A-Z_]+)(?::|\s*—)", body))
    unknown = observed_labels - LABELS
    if unknown:
        errors.append(f"unknown statement labels in {path.name}: {sorted(unknown)}")
    if not observed_labels:
        errors.append(f"no material statement labels found in {path.name}")
    return metadata


def validate_bound_inputs(
    root: Path, run_manifest: dict[str, Any], input_doc: dict[str, Any], errors: list[str]
) -> None:
    run = run_manifest.get("run", {})
    manifest = input_doc.get("manifest", {})
    inputs = manifest.get("inputs", [])
    paths = [item.get("path") for item in inputs]
    if manifest.get("member_count") != len(inputs):
        errors.append("input member count mismatch")
    unique(paths, "input paths", errors)
    if not inputs or any(not isinstance(item, dict) for item in inputs):
        errors.append("input inventory is empty or malformed")
        return
    starting_head = manifest.get("starting_local_head")
    if starting_head != run.get("starting_local_head"):
        errors.append("input/run starting HEAD mismatch")
    observed_lines: list[str] = []
    run_prefix = RUN_REL.as_posix() + "/"
    for item in inputs:
        relative = item.get("path")
        expected = item.get("sha256")
        if not isinstance(relative, str) or not re.fullmatch(r"[0-9a-f]{64}", str(expected)):
            errors.append("input path or SHA-256 malformed")
            continue
        path = root / relative
        if relative.startswith(run_prefix):
            data = path.read_bytes() if path.is_file() else None
        else:
            data = git_blob(root, starting_head, relative)
        actual = sha256_bytes(data) if data is not None else None
        if actual != expected:
            errors.append(f"bound input hash mismatch: {relative}")
        observed_lines.append(f"{expected}  {relative}\n")
    package_hash = sha256_bytes("".join(sorted(observed_lines, key=lambda x: x.split("  ", 1)[1])).encode())
    if package_hash != manifest.get("input_package_sha256"):
        errors.append("input package SHA-256 mismatch")
    if run_manifest.get("input", {}).get("input_package_sha256") != package_hash:
        errors.append("run/input package SHA-256 mismatch")


def validate(root: Path) -> dict[str, Any]:
    errors: list[str] = []
    run_root = root / RUN_REL
    manifest_path = run_root / "manifest.yaml"
    auth_path = run_root / "authorization/owner-authorization.yaml"
    prompt_path = run_root / "prompt/GOV-AUD-PROMPT-021-pass-02-execution-v0.1.0.md"
    input_path = run_root / "input/input-manifest.yaml"
    output_root = run_root / "output"

    for path in (manifest_path, auth_path, prompt_path, input_path):
        if not path.is_file():
            errors.append(f"required custody file missing: {path.relative_to(root)}")
    if errors:
        return {"result": "INVALID", "diagnostics": errors}

    manifest = load(manifest_path)
    authorization = load(auth_path).get("authorization", {})
    input_doc = load(input_path)
    run = manifest.get("run", {})
    prompt = manifest.get("prompt", {})
    auth = manifest.get("authorization", {})

    expected_run = {
        "audit_id": "GOV-AUD-001",
        "pass_id": "PASS-02",
        "run_id": "GOV-AUD-001-P02-R1",
        "status": "ACCEPTED_COMPLETED",
        "lifecycle": "EXECUTED",
        "execution_count_limit": 1,
        "execution_count_consumed": 1,
    }
    for field, expected in expected_run.items():
        if run.get(field) != expected:
            errors.append(f"run field mismatch: {field}")
    if any(
        (
            authorization.get("authorization_id") != "GOV-AUD-AUTH-002",
            authorization.get("authorized_run") != "GOV-AUD-001-P02-R1",
            authorization.get("authorized_pass") != "PASS-02",
            authorization.get("catalog_prompt_identity") != "HP-PROMPT-029/0.1.0",
            authorization.get("status") != "AUTHORIZED_NOT_YET_CONSUMED",
            authorization.get("execution_count_limit") != 1,
            authorization.get("execution_count_consumed") != 0,
        )
    ):
        errors.append("authorization identity or consumption mismatch")
    if auth.get("sha256") != sha256(auth_path):
        errors.append("authorization hash mismatch")
    if auth.get("status") != "CONSUMED":
        errors.append("run authorization consumption status mismatch")
    if any(
        (
            prompt.get("prompt_id") != "GOV-AUD-PROMPT-021",
            prompt.get("catalog_prompt_id") != "HP-PROMPT-029",
            prompt.get("lifecycle") != "EXECUTED",
            prompt.get("exact_text_preserved") is not True,
            prompt.get("sha256") != sha256(prompt_path),
        )
    ):
        errors.append("prompt identity, lifecycle or hash mismatch")
    prompt_text = prompt_path.read_text(encoding="utf-8")
    if "HP-PROMPT-029" not in prompt_text or "HP-PROMPT-028" in prompt_text:
        errors.append("amended prompt catalog identity mismatch")
    if manifest.get("input", {}).get("manifest_sha256") != sha256(input_path):
        errors.append("input manifest hash mismatch")
    validate_bound_inputs(root, manifest, input_doc, errors)

    actual_outputs = {path.name for path in output_root.iterdir() if path.is_file()} if output_root.is_dir() else set()
    if actual_outputs != OUTPUT_NAMES:
        errors.append("required output set mismatch")
    declared_outputs = manifest.get("output_contract", {}).get("required_outputs", [])
    if manifest.get("output_contract", {}).get("substantive_output_count") != len(OUTPUT_NAMES):
        errors.append("output contract count mismatch")
    if {Path(item.get("path", "")).name for item in declared_outputs} != OUTPUT_NAMES:
        errors.append("output contract identity mismatch")
    for item in declared_outputs:
        path = root / item.get("path", "")
        if not path.is_file() or sha256(path) != item.get("sha256"):
            errors.append(f"output contract hash mismatch: {path.name}")
    markdown_metadata: dict[str, dict[str, Any]] = {}
    for name in sorted(OUTPUT_NAMES):
        path = output_root / name
        if not path.is_file():
            continue
        if path.suffix == ".yaml":
            try:
                load(path)
            except Exception as exc:
                errors.append(f"invalid YAML {name}: {exc}")
        else:
            markdown_metadata[name] = validate_markdown(path, root, errors)

    ownership = load(output_root / "01-bounded-context-and-ownership-model.yaml").get(
        "bounded_context_model", {}
    )
    contexts = ownership.get("contexts", [])
    if ownership.get("context_count") != len(contexts) or not contexts:
        errors.append("bounded-context count mismatch")
    context_ids = [item.get("context_id") for item in contexts]
    unique(context_ids, "bounded-context IDs", errors)
    for item in contexts:
        if CONTEXT_FIELDS - set(item):
            errors.append(f"bounded-context fields missing: {item.get('context_id')}")
        for field in (
            "owned_state_and_artifacts",
            "accepted_inputs",
            "produced_outputs",
            "allowed_writers",
            "allowed_readers",
            "source_of_truth",
            "derived_non_authoritative_projections",
        ):
            if not isinstance(item.get(field), list) or not item.get(field):
                errors.append(f"bounded-context list empty: {item.get('context_id')}.{field}")

    relationship = load(output_root / "03-typed-relationship-and-query-model.yaml").get(
        "relationship_model", {}
    )
    entity_kinds = relationship.get("entity_kinds", [])
    kinds = [item.get("kind") for item in entity_kinds]
    unique(kinds, "entity kinds", errors)
    kind_set = set(kinds)
    relationship_types = relationship.get("relationship_types", [])
    type_names = [item.get("type_name") for item in relationship_types]
    unique(type_names, "relationship types", errors)
    if relationship.get("relationship_type_count") != len(relationship_types):
        errors.append("relationship-type count mismatch")
    type_set = set(type_names)
    for item in relationship_types:
        if RELATIONSHIP_FIELDS - set(item):
            errors.append(f"relationship fields missing: {item.get('type_name')}")
        if item.get("statement_label") not in LABELS:
            errors.append(f"relationship statement label invalid: {item.get('type_name')}")
        if item.get("authority") != "DERIVED_NON_AUTHORITATIVE":
            errors.append(f"relationship authority invalid: {item.get('type_name')}")
        for kind in item.get("source_entity_kinds", []) + item.get("target_entity_kinds", []):
            if kind not in kind_set:
                errors.append(f"relationship endpoint kind missing: {item.get('type_name')} -> {kind}")
    queries = relationship.get("query_contracts", [])
    query_ids = [item.get("query_id") for item in queries]
    unique(query_ids, "query IDs", errors)
    if relationship.get("required_query_count") != len(queries):
        errors.append("required-query count mismatch")
    coverage = [item.get("coverage_tag") for item in queries]
    unique(coverage, "query coverage tags", errors)
    if set(coverage) != QUERY_COVERAGE:
        errors.append("required query coverage mismatch")
    for item in queries:
        for traversal in item.get("traversals", []):
            if traversal not in type_set:
                errors.append(f"orphan query traversal: {item.get('query_id')} -> {traversal}")
        for kind in item.get("start_kinds", []) + item.get("result_kinds", []):
            if kind not in kind_set:
                errors.append(f"query endpoint kind missing: {item.get('query_id')} -> {kind}")

    compatibility = markdown_metadata.get("04-version-migration-and-impact-model.md", {})
    domains = compatibility.get("compatibility_domains", [])
    mechanisms = compatibility.get("compatibility_mechanisms", [])
    unique(domains, "compatibility domains", errors)
    unique(mechanisms, "compatibility mechanisms", errors)
    if compatibility.get("compatibility_domain_count") != len(domains):
        errors.append("compatibility domain count mismatch")
    if compatibility.get("compatibility_mechanism_count") != len(mechanisms):
        errors.append("compatibility mechanism count mismatch")
    if compatibility.get("compatibility_combination_count") != len(domains) * len(mechanisms):
        errors.append("compatibility combination count mismatch")

    self_hosting = markdown_metadata.get("05-controlled-self-hosting-and-trust-boundaries.md", {})
    if self_hosting.get("system_self_hosting_status") != "NOT_IMPLEMENTED":
        errors.append("system self-hosting status must remain not implemented")
    if self_hosting.get("infrastructure_self_hosting_status") != "NOT_IMPLEMENTED_OR_SELECTED":
        errors.append("infrastructure self-hosting status must remain not implemented or selected")

    styles = load(output_root / "06-architecture-style-comparison.yaml").get(
        "architecture_style_comparison", {}
    )
    style_items = styles.get("styles", [])
    style_ids = [item.get("style_id") for item in style_items]
    unique(style_ids, "architecture style IDs", errors)
    if styles.get("style_count") != len(style_items):
        errors.append("architecture style count mismatch")
    if styles.get("selected_option") is not None or styles.get("winner_selected") is not False:
        errors.append("architecture winner selected")
    if styles.get("technology_selected") is not False or styles.get("graph_technology_selected") is not False:
        errors.append("architecture or graph technology selected")
    if "NO_DISTRIBUTION_YET" not in {item.get("name") for item in style_items}:
        errors.append("NO_DISTRIBUTION_YET option missing")

    handoff = markdown_metadata.get("07-pass-02-findings-and-checkpoint-a-handoff.md", {})
    handoff_body = (output_root / "07-pass-02-findings-and-checkpoint-a-handoff.md").read_text(encoding="utf-8")
    decision_ids = sorted(set(re.findall(r"OD-P02-[0-9]{3}", handoff_body)))
    if handoff.get("owner_decision_count") != len(decision_ids):
        errors.append("owner-decision count mismatch")
    if any(
        (
            handoff.get("pass_02_accepted") is not False,
            handoff.get("checkpoint_a_completed") is not False,
            handoff.get("pass_03_authorized_or_executed") is not False,
            handoff.get("gov_7_activated") is not False,
        )
    ):
        errors.append("handoff authority boundary mismatch")

    validation_record = manifest.get("output_contract", {}).get("validation_report", {})
    validation_path = root / validation_record.get("path", "")
    if not validation_path.is_file() or sha256(validation_path) != validation_record.get("sha256"):
        errors.append("validation report custody or hash mismatch")
    else:
        report = load(validation_path).get("validation_report", {})
        if any(
            (
                report.get("record_id") != "GOV-AUD-VAL-002",
                report.get("run_id") != "GOV-AUD-001-P02-R1",
                report.get("pass_id") != "PASS-02",
                report.get("status") != "VALIDATED",
                report.get("result") != "VALID",
                report.get("independent_evaluation_performed") is not False,
                report.get("pass_02_accepted") is not False,
                report.get("checkpoint_a_completed") is not False,
                report.get("pass_03_authorized_or_executed") is not False,
                report.get("architecture_selected") is not False,
                report.get("graph_technology_selected") is not False,
                report.get("implementation_authorized") is not False,
                report.get("gov_7_activated") is not False,
                report.get("risk_accepted") is not False,
                report.get("commit_performed") is not False,
                report.get("push_performed") is not False,
            )
        ):
            errors.append("validation report identity, result or authority boundary mismatch")

    plan = load(root / "governance/audits/GOV-AUD-001-gov7-enablement/01-audit-plan.yaml")[
        "audit_program"
    ]
    status = load(root / "governance/audits/GOV-AUD-001-gov7-enablement/02-audit-status.yaml")[
        "audit"
    ]
    sequence = {item["id"]: item["status"] for item in plan.get("sequence", [])}
    if sequence.get("PASS-02") != "ACCEPTED_COMPLETED":
        errors.append("PASS-02 terminal lifecycle status mismatch")
    if sequence.get("CHECKPOINT-A") != "APPROVED_COMPLETED":
        errors.append("CHECKPOINT-A completed or changed")
    pass_03_state = sequence.get("PASS-03")
    pass_03_executed = pass_03_state == PASS_03_SUCCESS
    if pass_03_state not in PASS_03_PREPARATION_STATES and not pass_03_executed:
        errors.append("PASS-03 executed or authorized without a valid later lifecycle")
    if pass_03_executed:
        if any((
            status.get("pass_03_preparation_authorized") is not True,
            status.get("pass_03_preparation_status") != "PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION",
            status.get("pass_03_execution_authorized") is not True,
            status.get("pass_03_authorization_consumed") is not True,
            status.get("pass_03_executed") is not True,
            status.get("pass_03_status") != PASS_03_SUCCESS,
        )):
            errors.append("PASS-03 execution authority or lifecycle mismatch")
        successor = validate_pass_03_execution(root)
        errors.extend(f"PASS-03 successor: {item}" for item in successor["diagnostics"])
    elif any(
        (
            status.get("pass_03_preparation_authorized") is not True,
            status.get("pass_03_preparation_status") != pass_03_state,
            status.get("pass_03_execution_authorized") is not False,
            status.get("pass_03_executed") is not False,
        )
    ):
        errors.append("PASS-03 execution authority or lifecycle mismatch")
    if any(
        (
            plan.get("passes_executed") != (3 if pass_03_executed else 2),
            plan.get("completed") is not False,
            plan.get("gov_7_activated") is not False,
            status.get("pass_02_status") != "ACCEPTED_COMPLETED",
            status.get("checkpoint_a_completed") is not True,
            status.get("gov_7_activated") is not False,
        )
    ):
        errors.append("audit lifecycle or authority boundary mismatch")
    current_state = (root / "governance/CURRENT_STATE.md").read_text(encoding="utf-8")
    for required in (
        "kernel: 0.2.0/RATIFIED",
        "gov_7_status: INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY",
        "od_006: UNRESOLVED_TRIGGER_GATED",
    ):
        if required not in current_state:
            errors.append(f"unchanged governance baseline missing: {required}")

    boundary = manifest.get("authority_boundary", {})
    for field in (
        "pass_03_authorized_or_executed",
        "recommendations_accepted",
        "architecture_selected",
        "implementation_authorized",
        "gov_7_activated",
        "commit_authorized",
        "push_authorized",
    ):
        if boundary.get(field) is not False:
            errors.append(f"manifest authority boundary mismatch: {field}")
    if boundary.get("pass_02_accepted") is not True or boundary.get("checkpoint_a_completed") is not True:
        errors.append("manifest checkpoint disposition mismatch")
    if boundary.get("pass_03_preparation_authorized") is not True:
        errors.append("manifest PASS-03 preparation authority mismatch")

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
