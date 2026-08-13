#!/usr/bin/env python3
"""Validate GOV-LOOP-001 structure without constitutional judgment."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Any

from _lib import __version__
from _lib.canonical import compact_json, sha256_file
from _lib.diagnostics import Diagnostic, ordered
from _lib.schemas import load_schema, validate as schema_validate
from _lib.strict_yaml import StrictYAMLError, load


STATES = [
    "READY_FOR_TARGETED_CLOSURE", "TARGETED_CLOSURE_IN_PROGRESS",
    "DESIGNER_REMEDIATION_REQUIRED", "DESIGNER_REMEDIATION_IN_PROGRESS",
    "CLOSURE_CONFIRMED", "OWNER_DECISION_REQUIRED", "RESEARCH_REQUIRED",
    "STRUCTURAL_REDESIGN_REQUIRED", "LOOP_LIMIT_REACHED",
]
ADVERSARY_MATRIX = [
    (1, "STRUCTURAL_REDESIGN_REQUIRED", "ANY", ["local_designer_remediation_is_incapable_of_resolving_a_material_constitutional_defect", "bounded_loop_scope_is_no_longer_sufficient"]),
    (2, "OWNER_DECISION_REQUIRED", "ANY", ["an_explicit_reserved_owner_decision_is_required", "competing_constitutional_values_cannot_be_resolved_by_existing_authority", "continuation_requires_owner_risk_acceptance"]),
    (3, "RESEARCH_REQUIRED", "ALL", ["required_evidence_is_absent", "the_missing_evidence_can_materially_change_the_closure_verdict", "no_owner_decision_or_local_remediation_can_substitute_for_it"]),
    (4, "DESIGNER_REMEDIATION_REQUIRED", "ANY", ["any_original_finding_required_for_closure_is_reopened", "any_new_or_regression_constitutional_finding_is_blocking", "markdown_yaml_parity_failed", "proportionality_or_operability_failed", "required_routing_is_incorrect_or_claims_unavailable_capability"]),
    (5, "CLOSURE_CONFIRMED", "ALL", ["all_closure_requirements_pass"]),
]
DESIGNER_RESULTS = ["STRUCTURAL_REDESIGN_REQUIRED", "OWNER_DECISION_REQUIRED", "RESEARCH_REQUIRED", "READY_FOR_TARGETED_CLOSURE"]
DESIGNER_MAPPING_ORDER = ["READY_FOR_TARGETED_CLOSURE", "OWNER_DECISION_REQUIRED", "RESEARCH_REQUIRED", "STRUCTURAL_REDESIGN_REQUIRED"]
SEQUENCE = [("KGR-005", "TARGETED_CLOSURE", 1), ("KGR-006", "DESIGNER_REMEDIATION", 1), ("KGR-007", "TARGETED_CLOSURE", 2), ("KGR-008", "DESIGNER_REMEDIATION", 2), ("KGR-009", "TARGETED_CLOSURE", 3)]


def _expect(diags: list[Diagnostic], condition: bool, code: str, path: str, message: str) -> None:
    if not condition:
        diags.append(Diagnostic(code, path, message))


def _matrix_rows(data: dict[str, Any]) -> list[tuple[Any, Any, Any, Any]]:
    return [(row.get("priority"), row.get("result"), row.get("condition_logic"), row.get("when")) for row in data.get("result_decision_matrix", {}).get("substantive", [])]


def validate_loop(data: Any, schema_path: Path, adversary_text: str | None, designer_text: str | None) -> list[Diagnostic]:
    if not isinstance(data, dict):
        return [Diagnostic("LOOP_ROOT_INVALID", "$", "loop root must be a mapping")]
    diags = schema_validate(data, load_schema(schema_path))
    loop = data.get("loop", {})
    _expect(diags, loop.get("id") == "GOV-LOOP-001" and loop.get("version") == "0.1.0", "UNSUPPORTED_LOOP_VERSION", "$.loop", "only GOV-LOOP-001 version 0.1.0 is supported")
    states = data.get("states", [])
    _expect(diags, states == STATES, "STATE_SET_MISMATCH", "$.states", "exact ordered nine-state profile required")
    refs = set()
    for row in data.get("transitions", []): refs.update((row.get("from"), row.get("to")))
    _expect(diags, refs <= set(states), "UNDECLARED_STATE_REFERENCE", "$.transitions", "every source and destination must resolve")
    active = set(data.get("state_classes", {}).get("active", []))
    for state in active:
        _expect(diags, any(row.get("from") == state for row in data.get("transitions", [])), "ACTIVE_STATE_WITHOUT_EXIT", f"$.state_classes.active.{state}", "active states require explicit exits")
    attempt = data.get("attempt_events", [])
    _expect(diags, len(attempt) == 2 and all(x.get("outcome") == "BLOCKED_BY_PACKAGE_CONFLICT" and x.get("persistent_state_changes") is False and x.get("substantive_stage_started") is False for x in attempt), "ATTEMPT_EVENT_PROFILE_MISMATCH", "$.attempt_events", "typed non-mutating package-conflict attempts required")
    noncomp = data.get("non_completion_events", [])
    _expect(diags, {(x.get("applies_while_persistent_state_is"), x.get("event")) for x in noncomp} == {(s, e) for s in ("TARGETED_CLOSURE_IN_PROGRESS", "DESIGNER_REMEDIATION_IN_PROGRESS") for e in ("INVALID_OUTPUT_PACKAGE", "INVALID_IMPORT")}, "NON_COMPLETION_PROFILE_MISMATCH", "$.non_completion_events", "exact typed invalid-output/import events required")
    _expect(diags, all(x.get("counter_increment") is False and x.get("persistent_state_changes") is False for x in noncomp), "NON_COMPLETION_MUTATES", "$.non_completion_events", "non-completion events consume no counter and preserve state")
    _expect(diags, _matrix_rows(data) == ADVERSARY_MATRIX, "ADVERSARY_MATRIX_MISMATCH", "$.result_decision_matrix.substantive", "exact ordered Adversary matrix required")
    matrix = data.get("result_decision_matrix", {})
    _expect(diags, matrix.get("exactly_one_substantive_result_required") is True and matrix.get("multiple_substantive_results_prohibited") is True, "FINAL_RESULT_EXCLUSIVITY_MISSING", "$.result_decision_matrix", "exactly one substantive result is required")
    designer = data.get("designer_remediation_controller_mapping", {})
    _expect(diags, list(k for k in designer if k.isupper()) == DESIGNER_MAPPING_ORDER, "DESIGNER_MATRIX_MISMATCH", "$.designer_remediation_controller_mapping", "exact ordered Designer Controller mapping required")
    _expect(diags, designer.get("designer_may_emit_closure_confirmed") is False and "CLOSURE_CONFIRMED" not in designer, "DESIGNER_SELF_CLOSURE", "$.designer_remediation_controller_mapping", "Designer cannot emit CLOSURE_CONFIRMED")
    closure = data.get("closure_confirmed_requires", {})
    required_closure = {"package_validation":"PASSED", "substantive_review_completed":True, "blocking_new_findings":0, "blocking_regression_findings":0, "markdown_yaml_parity":"PASSED", "seven_clause_proportionality":"PASSED", "solo_owner_operability":"PASSED", "authority_integrity":"PASSED", "owner_decision_required":False, "research_required":False, "structural_redesign_required":False, "kernel_status":"PROPOSED_NOT_RATIFIED"}
    _expect(diags, all(closure.get(k) == v for k, v in required_closure.items()) and closure.get("original_findings") == {"KA-F-001_through_KA-F-014":"CONFIRMED_CLOSED", "KA-F-015":"ROUTED_CONFIRMED"}, "CLOSURE_REQUIREMENTS_MISMATCH", "$.closure_confirmed_requires", "exact closure-confirmed requirements required")
    counters = data.get("counters", {})
    _expect(diags, counters == {"completed_targeted_closure_runs":0, "completed_designer_remediation_runs":0}, "INITIAL_COUNTERS_NOT_ZERO", "$.counters", "initial counters must be zero")
    increments = data.get("increment_rules", {})
    adv_results = [r[1] for r in ADVERSARY_MATRIX]
    _expect(diags, increments.get("targeted_closure", {}).get("increment_on_valid_completed_results") == ["CLOSURE_CONFIRMED", "DESIGNER_REMEDIATION_REQUIRED", "OWNER_DECISION_REQUIRED", "RESEARCH_REQUIRED", "STRUCTURAL_REDESIGN_REQUIRED"], "TARGETED_INCREMENT_RULE_MISMATCH", "$.increment_rules.targeted_closure", "exact completed-result increment enum required")
    _expect(diags, increments.get("designer_remediation", {}).get("increment_on_valid_completed_results") == ["READY_FOR_TARGETED_CLOSURE", "OWNER_DECISION_REQUIRED", "RESEARCH_REQUIRED", "STRUCTURAL_REDESIGN_REQUIRED"], "DESIGNER_INCREMENT_RULE_MISMATCH", "$.increment_rules.designer_remediation", "exact completed-result increment enum required")
    for name in ("BLOCKED_BY_PACKAGE_CONFLICT", "INVALID_OUTPUT_PACKAGE", "INVALID_IMPORT"):
        _expect(diags, name in increments.get("do_not_increment_for", []), "NON_CONSUMING_EVENT_MISSING", "$.increment_rules.do_not_increment_for", f"{name} must consume no counter")
    limits = data.get("limits", {})
    _expect(diags, limits.get("maximum_targeted_closure_runs") == 3 and limits.get("allowed_targeted_closure_ordinals") == [1,2,3] and limits.get("fourth_targeted_closure_may_be_prepared") is False, "TARGETED_LIMIT_MISMATCH", "$.limits", "maximum three targeted closures")
    _expect(diags, limits.get("maximum_designer_remediation_runs") == 2 and limits.get("allowed_designer_remediation_ordinals") == [1,2] and limits.get("third_designer_remediation_may_be_prepared") is False, "DESIGNER_LIMIT_MISMATCH", "$.limits", "maximum two Designer remediations")
    seq = data.get("controller_post_import_logic", {}).get("maximum_valid_sequence", [])
    _expect(diags, [(x.get("run"), x.get("function"), x.get("ordinal")) for x in seq] == SEQUENCE, "RUN_SEQUENCE_MISMATCH", "$.controller_post_import_logic.maximum_valid_sequence", "exact KGR-005 through KGR-009 sequence required")
    sig = data.get("blocking_finding_signature", {})
    canon = sig.get("canonicalization", {})
    _expect(diags, sig.get("record_components") == ["finding_id","adversary_verdict","original_or_assigned_severity","sorted_failed_criterion_ids","sorted_relationship_type_and_parent_id_when_applicable"] and canon == {"encoding":"UTF-8","format":"JSON","object_key_order":"LEXICOGRAPHIC","record_order":"SORT_BY_FINDING_ID","failed_criterion_ids":"SORT_LEXICOGRAPHICALLY_AND_DEDUPLICATE","relationships":"SORT_BY_TYPE_THEN_PARENT_ID_AND_DEDUPLICATE","whitespace":"NONE_OUTSIDE_JSON_STRING_VALUES","line_ending":"NONE"} and sig.get("hash") == {"algorithm":"SHA-256","representation":"LOWERCASE_HEXADECIMAL"}, "SIGNATURE_RULE_MISMATCH", "$.blocking_finding_signature", "exact deterministic signature rules required")
    ng = data.get("no_progress_guard", {})
    _expect(diags, ng.get("transition") == "LOOP_LIMIT_REACHED" and ng.get("requires") == {"same_blocking_finding_signature":True,"net_blocking_finding_reduction":0}, "NO_PROGRESS_GUARD_MISMATCH", "$.no_progress_guard", "exact no-progress guard required")
    rg = data.get("finding_reappearance_guard", {})
    _expect(diags, rg.get("threshold") == 2 and rg.get("transition") == "LOOP_LIMIT_REACHED" and rg.get("requires", {}).get("valid_designer_remediation_runs_between") == "AT_LEAST_1", "REAPPEARANCE_GUARD_MISMATCH", "$.finding_reappearance_guard", "exact repeated-finding guard required")
    reentry = data.get("reentry_rules", {})
    _expect(diags, reentry.get("owner_decision_required", {}).get("prerequisite") == "new_explicit_formal_owner_decision_artifact", "OWNER_REENTRY_MISMATCH", "$.reentry_rules.owner_decision_required", "owner decision artifact required")
    _expect(diags, reentry.get("research_required", {}).get("prerequisite") == "new_formal_applicable_research_or_evidence_artifact", "RESEARCH_REENTRY_MISMATCH", "$.reentry_rules.research_required", "research artifact required")
    _expect(diags, reentry.get("structural_redesign_required", {}).get("exits_bounded_loop") is True, "REDESIGN_EXIT_MISSING", "$.reentry_rules.structural_redesign_required", "structural redesign exits bounded loop")
    _expect(diags, data.get("controller_import_rules", {}).get("only_ready_for_targeted_closure_permits_next_adversary_run_preparation") is True, "ADVERSARY_PREPARATION_GUARD_MISSING", "$.controller_import_rules", "only READY_FOR_TARGETED_CLOSURE may prepare another Adversary run")
    artifacts = data.get("artifact_resolution", {})
    _expect(diags, artifacts.get("immutable_history") is True and artifacts.get("original_review", {}).get("initial_source_run") == "KGR-003" and artifacts.get("run_envelopes", {}).get("earlier_envelopes_are_rewritten") is False, "ARTIFACT_RESOLUTION_MISMATCH", "$.artifact_resolution", "immutable exact artifact-resolution rules required")
    transitions = data.get("transitions", [])
    for source, destination in [("OWNER_DECISION_REQUIRED","READY_FOR_TARGETED_CLOSURE"),("RESEARCH_REQUIRED","READY_FOR_TARGETED_CLOSURE"),("RESEARCH_REQUIRED","OWNER_DECISION_REQUIRED")]:
        _expect(diags, any(x.get("from") == source and x.get("to") == destination for x in transitions), "REENTRY_TRANSITION_MISSING", "$.transitions", f"missing {source} to {destination}")
    if adversary_text is not None:
        for token in ("GOV-PROTOCOL-002", "version: 0.1.0", "GOV-LOOP-001", "GOV-PROMPT-007", *[x[1] for x in ADVERSARY_MATRIX]):
            _expect(diags, token in adversary_text, "ADVERSARY_PROTOCOL_BINDING_MISMATCH", "$protocol.adversary", f"missing identity/result {token}")
    if designer_text is not None:
        for token in ("GOV-PROTOCOL-003", "version: 0.1.0", "GOV-LOOP-001", *DESIGNER_RESULTS):
            _expect(diags, token in designer_text, "DESIGNER_PROTOCOL_BINDING_MISMATCH", "$protocol.designer", f"missing identity/result {token}")
        _expect(diags, "The Designer must never emit `CLOSURE_CONFIRMED`" in designer_text, "DESIGNER_PROTOCOL_SELF_CLOSURE_GUARD_MISSING", "$protocol.designer", "explicit Designer self-closure prohibition required")
    return ordered(diags)


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--loop", required=True)
    p.add_argument("--adversary-protocol")
    p.add_argument("--designer-protocol")
    p.add_argument("--json", action="store_true")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        loop_path = Path(args.loop)
        data = load(loop_path)
        root = Path(__file__).resolve().parents[1]
        schema = root / "schemas/kernel-design-closure-loop.schema.json"
        adversary = Path(args.adversary_protocol).read_text(encoding="utf-8") if args.adversary_protocol else None
        designer = Path(args.designer_protocol).read_text(encoding="utf-8") if args.designer_protocol else None
        diagnostics = validate_loop(data, schema, adversary, designer)
        report = {"constitutional_authority":"NONE", "diagnostics":[d.as_dict() for d in diagnostics], "loop":{"id":data.get("loop",{}).get("id"), "sha256":sha256_file(loop_path), "version":data.get("loop",{}).get("version")}, "result":"VALID" if not diagnostics else "INVALID", "tool":{"name":"validate_closure_loop.py","version":__version__}}
        print(compact_json(report) if args.json else f"{report['result']}: {len(diagnostics)} diagnostic(s)")
        return 0 if not diagnostics else 1
    except (OSError, StrictYAMLError, ValueError) as exc:
        print(f"operational failure: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
