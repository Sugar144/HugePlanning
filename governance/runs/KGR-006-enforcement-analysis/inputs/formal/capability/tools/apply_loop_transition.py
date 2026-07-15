#!/usr/bin/env python3
"""Replay GOV-LOOP-001 history and simulate or record one transition."""

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
import json
import sys
from typing import Any

from _lib import __version__
from _lib.atomic import ImmutableTargetError, write_new
from _lib.canonical import canonical_sha256, compact_json, json_bytes, sha256_file
from _lib.diagnostics import Diagnostic, ordered
from _lib.schemas import load_schema, validate as schema_validate
from _lib.strict_yaml import StrictYAMLError, load


INITIAL_STATE = "READY_FOR_TARGETED_CLOSURE"
ZERO = {"completed_targeted_closure_runs":0, "completed_designer_remediation_runs":0}
SEQUENCE = {
    "KGR-005": ("Kernel Adversary", "TARGETED_CLOSURE", 1),
    "KGR-006": ("Kernel Designer", "CLOSURE_REMEDIATION", 1),
    "KGR-007": ("Kernel Adversary", "TARGETED_CLOSURE", 2),
    "KGR-008": ("Kernel Designer", "CLOSURE_REMEDIATION", 2),
    "KGR-009": ("Kernel Adversary", "TARGETED_CLOSURE", 3),
}
ADV_PRIORITY = {"STRUCTURAL_REDESIGN_REQUIRED":1,"OWNER_DECISION_REQUIRED":2,"RESEARCH_REQUIRED":3,"DESIGNER_REMEDIATION_REQUIRED":4,"CLOSURE_CONFIRMED":5}
DES_PRIORITY = {"STRUCTURAL_REDESIGN_REQUIRED":1,"OWNER_DECISION_REQUIRED":2,"RESEARCH_REQUIRED":3,"READY_FOR_TARGETED_CLOSURE":4}
NON_COMPLETION = {"BLOCKED_BY_PACKAGE_CONFLICT","BLOCKED_BY_PACKAGE_CONFLICT_MEMBER_HASH_MISMATCH","INVALID_OUTPUT_PACKAGE","INVALID_IMPORT","PAUSED","INTERRUPTED","ABORTED_BEFORE_SUBSTANTIVE_COMPLETION"}
UPDATES = ["governance/ARTIFACT_REGISTRY.yaml","governance/CURRENT_STATE.md","governance/GOVERNANCE_MASTER_PLAN.md","source run manifest and validated package custody records"]


def _load_input(path: Path) -> dict[str, Any]:
    data = load(path)
    if not isinstance(data, dict): raise ValueError("input root must be a mapping")
    return data


def _role_result(data: dict[str, Any]) -> tuple[str | None, dict[str, Any]]:
    if "role_result" in data and isinstance(data["role_result"], dict):
        return _role_result(data["role_result"])
    if "closure_result" in data:
        root = data["closure_result"]; return root.get("adversary_result",{}).get("status"), root
    if "designer_remediation_result" in data:
        root = data["designer_remediation_result"]; return root.get("designer_result",{}).get("status"), root
    return data.get("input_result") or data.get("result"), data


def blocking_signature(findings: list[dict[str, Any]]) -> tuple[str, int, list[str]]:
    normalized = []
    reopened = []
    for item in findings:
        severity = item.get("original_or_assigned_severity", item.get("severity", item.get("original_severity")))
        verdict = item.get("adversary_verdict", item.get("verdict"))
        blocking = item.get("blocking")
        if blocking is None: blocking = severity in ("CRITICAL","HIGH","MEDIUM") or verdict == "REOPENED"
        if not blocking: continue
        finding_id = item.get("finding_id", "")
        if verdict == "REOPENED": reopened.append(finding_id)
        relationships = sorted({(x.get("type",""), x.get("parent_id", x.get("finding_id",""))) for x in item.get("relationships",[])})
        normalized.append({"adversary_verdict":verdict,"failed_criterion_ids":sorted(set(item.get("failed_criteria", item.get("failed_criterion_ids",[])))),"finding_id":finding_id,"original_or_assigned_severity":severity,"relationships":[{"parent_id":p,"type":t} for t,p in relationships]})
    normalized.sort(key=lambda x:x["finding_id"])
    return canonical_sha256(normalized), len(normalized), sorted(set(reopened))


def _history_records(root: Path, embedded: list[Any]) -> tuple[list[dict[str, Any]], list[Diagnostic]]:
    records: list[dict[str, Any]] = []
    diags: list[Diagnostic] = []
    if root.exists():
        for path in sorted(root.glob("KGR-*/controller/controller-transition.json")):
            try:
                value = json.loads(path.read_text(encoding="utf-8"))
                if not isinstance(value, dict): raise ValueError("record root is not object")
                records.append(value)
            except (OSError, ValueError, json.JSONDecodeError) as exc:
                diags.append(Diagnostic("HISTORY_RECORD_INVALID", str(path), str(exc)))
    records.extend(x for x in embedded if isinstance(x, dict))
    return records, diags


def run_directory(root: Path, source_run: str) -> Path:
    candidates = sorted(path for path in root.glob(f"{source_run}-*") if path.is_dir())
    if len(candidates) > 1:
        raise ValueError(f"ambiguous canonical run directory for {source_run}")
    return candidates[0] if candidates else root / source_run


def replay(records: list[dict[str, Any]]) -> tuple[str, dict[str,int], list[dict[str, Any]], list[Diagnostic]]:
    state = INITIAL_STATE; counters = dict(ZERO); accepted=[]; diags=[]; seen=set()
    for index, record in enumerate(sorted(records, key=lambda x:x.get("source_run",""))):
        run = record.get("source_run")
        if run in seen: diags.append(Diagnostic("HISTORY_FORK", f"$history[{index}]", f"duplicate source run {run}")); continue
        seen.add(run)
        before = record.get("counters_before", counters)
        previous = record.get("previous_state", state)
        role = record.get("source_role")
        active_bridge = (
            (role == "Kernel Adversary" and state == "READY_FOR_TARGETED_CLOSURE" and previous == "TARGETED_CLOSURE_IN_PROGRESS")
            or (role == "Kernel Designer" and state == "DESIGNER_REMEDIATION_REQUIRED" and previous == "DESIGNER_REMEDIATION_IN_PROGRESS")
        )
        if before != counters or (previous != state and not active_bridge):
            diags.append(Diagnostic("HISTORY_FORK", f"$history[{index}]", "counter or state chain diverges")); continue
        after = record.get("counters_after", before)
        if not isinstance(after, dict): diags.append(Diagnostic("HISTORY_RECORD_INVALID",f"$history[{index}]","invalid counters_after")); continue
        counters = dict(after); state = record.get("resulting_state", record.get("expected_transition", state)); accepted.append(record)
    return state, counters, accepted, diags


def _identity(source_run: str, data: dict[str, Any]) -> tuple[str | None,str | None]:
    expected = SEQUENCE.get(source_run)
    role = data.get("source_role")
    mode = data.get("source_mode")
    if role == "adversary": role = "Kernel Adversary"
    if role == "designer": role = "Kernel Designer"
    return role or (expected[0] if expected else None), mode or (expected[1] if expected else None)


def calculate(command: str, loop_path: Path, source_run: str, data: dict[str, Any], history_root: Path, authorization: str | None, applied: bool) -> tuple[dict[str, Any], list[Diagnostic], bool]:
    diags=[]
    loop = load(loop_path)
    if loop.get("loop",{}).get("id") != "GOV-LOOP-001" or loop.get("loop",{}).get("version") != "0.1.0": diags.append(Diagnostic("UNSUPPORTED_LOOP_VERSION","$.loop","only GOV-LOOP-001 0.1.0 is supported"))
    request = data.get("controller_import", data)
    if not isinstance(request, dict): request = data
    embedded = request.get("history", [])
    records, history_diags = _history_records(history_root, embedded if isinstance(embedded,list) else [])
    diags.extend(history_diags)
    state, counters, accepted, replay_diags = replay(records); diags.extend(replay_diags)
    if request.get("fixture_id"):
        state = request.get("input_state", state)
        declared_before = request.get("counters_before", counters)
        if not embedded: counters = dict(declared_before)
    if any(x.get("source_run") == source_run for x in accepted):
        diags.append(Diagnostic("DUPLICATE_SOURCE_RUN_TRANSITION", "$.source_run", f"transition already exists for {source_run}"))
    result, root = _role_result(request)
    role, mode = _identity(source_run, request)
    supplied_role_result = request.get("role_result", request)
    schema_root = Path(__file__).resolve().parents[1] / "schemas/protocols"
    if isinstance(supplied_role_result, dict) and "closure_result" in supplied_role_result:
        diags.extend(schema_validate(supplied_role_result, load_schema(schema_root / "GOV-PROTOCOL-002/0.1.0/closure-result.schema.json"), "$role_result"))
    if isinstance(supplied_role_result, dict) and "designer_remediation_result" in supplied_role_result:
        diags.extend(schema_validate(supplied_role_result, load_schema(schema_root / "GOV-PROTOCOL-003/0.1.0/designer-remediation-result.schema.json"), "$role_result"))
    expected = SEQUENCE.get(source_run)
    if command == "import":
        if expected is None: diags.append(Diagnostic("RUN_SEQUENCE_INVALID","$.source_run","run must be KGR-005 through KGR-009"))
        elif (role,mode) != expected[:2]: diags.append(Diagnostic("ROLE_MODE_MISMATCH","$.source_role","role/mode do not match run sequence"))
    counters_before = dict(counters); counters_after = dict(counters); resulting = state
    next_role=None; next_mode=None; next_run=None; guards={"blocking_finding_signature":None,"previous_blocking_finding_signature":None,"same_signature":False,"net_blocking_finding_reduction":None,"repeated_finding_ids":[],"exhausted":[]}
    is_noncompletion = result in NON_COMPLETION
    recordable = not is_noncompletion
    if command == "import":
        expected_active = "TARGETED_CLOSURE_IN_PROGRESS" if role == "Kernel Adversary" else "DESIGNER_REMEDIATION_IN_PROGRESS"
        evidence = request.get("active_state_evidence")
        evidence_valid = isinstance(evidence, dict) and evidence.get("source_run") == source_run and evidence.get("state") == expected_active and evidence.get("execution_started") is True and isinstance(evidence.get("evidence_ref"), str) and bool(evidence.get("evidence_ref"))
        if not is_noncompletion and state != expected_active and evidence_valid:
            state = expected_active
        if not is_noncompletion and state != expected_active:
            diags.append(Diagnostic("ACTIVE_STATE_EVIDENCE_MISSING","$.input_state",f"completed import requires {expected_active}"))
        allowed = ADV_PRIORITY if role == "Kernel Adversary" else DES_PRIORITY
        if not is_noncompletion and result not in allowed: diags.append(Diagnostic("RESULT_ENUM_INVALID","$.input_result",f"invalid result for {role}"))
        matrix = root.get("decision_matrix", {}) if isinstance(root,dict) else {}
        if matrix and result in allowed:
            if matrix.get("selected_result") != result or matrix.get("selected_priority") != allowed[result] or matrix.get("evaluated_in_priority_order") is not True:
                diags.append(Diagnostic("MATRIX_PRIORITY_INCONSISTENT","$.decision_matrix","selected priority/result is inconsistent"))
            accounted = matrix.get("higher_priority_conditions_confirmed_false", [])
            if allowed[result] > 1 and len(accounted) < allowed[result]-1:
                diags.append(Diagnostic("HIGHER_PRIORITY_OUTCOMES_UNACCOUNTED","$.decision_matrix.higher_priority_conditions_confirmed_false","every higher priority requires an accounting"))
        if request.get("identity_valid") is False or request.get("prompt_envelope_identity_match") is False:
            diags.append(Diagnostic("PROMPT_ENVELOPE_IDENTITY_MISMATCH","$.identity","prompt/envelope identity mismatch"))
        if is_noncompletion:
            recordable=False
            resulting=state
            if result.startswith("BLOCKED_BY_PACKAGE_CONFLICT"):
                resulting = state
                next_role=role; next_mode=mode
        elif result in (ADV_PRIORITY if role == "Kernel Adversary" else DES_PRIORITY):
            counter_key = "completed_targeted_closure_runs" if role == "Kernel Adversary" else "completed_designer_remediation_runs"
            counters_after[counter_key] += 1
            if counters_after["completed_targeted_closure_runs"] > 3: diags.append(Diagnostic("TARGETED_CLOSURE_LIMIT_EXCEEDED","$.counters_after","fourth targeted closure refused"))
            if counters_after["completed_designer_remediation_runs"] > 2: diags.append(Diagnostic("DESIGNER_REMEDIATION_LIMIT_EXCEEDED","$.counters_after","third Designer remediation refused"))
            findings = request.get("blocking_findings", root.get("blocking_findings", root.get("guard_relevant_facts", [])) if isinstance(root,dict) else [])
            if not isinstance(findings,list): findings=[]
            signature,count,reopened = blocking_signature(findings)
            guards["blocking_finding_signature"] = signature
            prior_adv = [x for x in accepted if x.get("source_role") == "Kernel Adversary"]
            if prior_adv:
                previous_guard = prior_adv[-1].get("guards", prior_adv[-1].get("guard_evaluation",{}))
                guards["previous_blocking_finding_signature"] = previous_guard.get("blocking_finding_signature")
                guards["same_signature"] = signature == guards["previous_blocking_finding_signature"]
                previous_count = previous_guard.get("blocking_finding_count", count)
                guards["net_blocking_finding_reduction"] = previous_count - count
                if guards["same_signature"] and guards["net_blocking_finding_reduction"] == 0 and counters_after["completed_designer_remediation_runs"] >= 2:
                    guards["exhausted"].append("NO_PROGRESS")
            guards["blocking_finding_count"] = count
            prior_reopened={}
            for x in prior_adv:
                for fid in x.get("guards",{}).get("reopened_finding_ids",[]): prior_reopened[fid]=x.get("source_run")
            guards["reopened_finding_ids"] = reopened
            guards["repeated_finding_ids"] = sorted(fid for fid in reopened if fid in prior_reopened and counters_after["completed_designer_remediation_runs"] >= 1)
            if guards["repeated_finding_ids"]: guards["exhausted"].append("REPEATED_FINDING")
            if role == "Kernel Adversary":
                if result == "DESIGNER_REMEDIATION_REQUIRED":
                    if counters_after["completed_targeted_closure_runs"] >= 3 or counters_after["completed_designer_remediation_runs"] >= 2 or guards["exhausted"]: resulting="LOOP_LIMIT_REACHED"
                    else: resulting="DESIGNER_REMEDIATION_REQUIRED"; next_role="Kernel Designer"; next_mode="CLOSURE_REMEDIATION"; next_run=f"KGR-{int(source_run[4:])+1:03d}"
                else: resulting=result
            else:
                resulting=result
                if result == "READY_FOR_TARGETED_CLOSURE":
                    next_role="Kernel Adversary"; next_mode="TARGETED_CLOSURE"; next_run=f"KGR-{int(source_run[4:])+1:03d}"
    elif command == "event":
        event = request.get("typed_event", request.get("event"))
        mapping={"TARGETED_CLOSURE_EXECUTION_BEGAN":("READY_FOR_TARGETED_CLOSURE","TARGETED_CLOSURE_IN_PROGRESS"),"DESIGNER_REMEDIATION_EXECUTION_BEGAN":("DESIGNER_REMEDIATION_REQUIRED","DESIGNER_REMEDIATION_IN_PROGRESS")}
        if event not in mapping: diags.append(Diagnostic("EVENT_ENUM_INVALID","$.typed_event","unsupported typed event"))
        elif state != mapping[event][0]: diags.append(Diagnostic("EVENT_SOURCE_STATE_INVALID","$.typed_event",f"event requires {mapping[event][0]}"))
        else: resulting=mapping[event][1]
        result=event; role="Loop Controller"; mode="CONTROLLER_EVENT"
    else:
        route=request.get("resulting_state"); artifact=request.get("artifact",{})
        allowed={"OWNER_DECISION_REQUIRED":{"DESIGNER_REMEDIATION_REQUIRED","READY_FOR_TARGETED_CLOSURE"},"RESEARCH_REQUIRED":{"DESIGNER_REMEDIATION_REQUIRED","READY_FOR_TARGETED_CLOSURE","OWNER_DECISION_REQUIRED"}}
        if state not in allowed or route not in allowed.get(state,set()): diags.append(Diagnostic("REENTRY_ROUTE_INVALID","$.resulting_state","re-entry route is not allowed"))
        if not isinstance(artifact,dict) or not artifact.get("id") or artifact.get("applicable") is not True: diags.append(Diagnostic("REENTRY_ARTIFACT_INVALID","$.artifact","new identified applicable artifact required"))
        else: resulting=route
        result=request.get("typed_event","VALIDATED_REENTRY_ARTIFACT"); role="Loop Controller"; mode="CONTROLLER_REENTRY"
    guards["exhausted"] = sorted(set(guards["exhausted"]))
    record={"applied":applied,"authorization_reference":authorization,"constitutional_authority":"NONE","counters_after":counters_after,"counters_before":counters_before,"evidence_semantics":"VALIDATED_TRANSITION_RECORD_NOT_RATIFICATION_OR_ROLE_EXECUTION_EVIDENCE","guards":guards,"human_reviewed_repository_updates_required":UPDATES,"input":{"typed_event":result} if command != "import" else {"declared_role_result":result},"loop":{"id":"GOV-LOOP-001","sha256":sha256_file(loop_path),"version":"0.1.0"},"next_mode":next_mode,"next_role":next_role,"next_run_to_prepare":next_run,"package_validation_reference":request.get("package_validation_reference"),"previous_state":state,"resulting_state":resulting,"schema_version":"0.1.0","source_mode":mode,"source_role":role,"source_run":source_run}
    schema=load_schema(Path(__file__).resolve().parents[1]/"schemas/controller-transition.schema.json")
    diags.extend(schema_validate(record,schema))
    return record, ordered(diags), recordable


def parser() -> argparse.ArgumentParser:
    p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(dest="command",required=True)
    for name in ("import","event","reenter"):
        q=sub.add_parser(name); q.add_argument("--loop",required=True); q.add_argument("--source-run",required=True); q.add_argument("--input",required=True); q.add_argument("--history-root",default="governance/runs"); q.add_argument("--authorization-ref"); q.add_argument("--apply",action="store_true"); q.add_argument("--json",action="store_true")
    return p


def main(argv: list[str] | None=None) -> int:
    args=parser().parse_args(argv)
    try:
        data=_load_input(Path(args.input))
        proposed,diags,recordable=calculate(args.command,Path(args.loop),args.source_run,data,Path(args.history_root),args.authorization_ref,args.apply)
        if diags:
            report={"applied":False,"diagnostics":[d.as_dict() for d in diags],"proposed_transition":proposed,"result":"INVALID","tool":{"name":"apply_loop_transition.py","version":__version__}}
            print(compact_json(report) if args.json else f"INVALID: {len(diags)} diagnostic(s)"); return 1
        if args.apply and recordable and not args.authorization_ref:
            proposed["applied"]=False
            report={"applied":False,"diagnostics":[],"proposed_transition":proposed,"result":"AUTHORIZATION_REQUIRED","tool":{"name":"apply_loop_transition.py","version":__version__}}
            print(compact_json(report) if args.json else "AUTHORIZATION_REQUIRED"); return 3
        created=None
        if args.apply and recordable:
            target=run_directory(Path(args.history_root),args.source_run)/"controller/controller-transition.json"
            write_new(target,json_bytes(proposed,trailing_newline=True)); created=str(target)
        report={"applied":bool(created),"created_path":created,"diagnostics":[],"proposed_transition":proposed,"result":"VALID","tool":{"name":"apply_loop_transition.py","version":__version__}}
        print(compact_json(report) if args.json else "VALID"); return 0
    except ImmutableTargetError as exc:
        print(f"immutable-target conflict: {exc}",file=sys.stderr); return 1
    except (OSError,StrictYAMLError,ValueError,json.JSONDecodeError) as exc:
        print(f"operational failure: {exc}",file=sys.stderr); return 2


if __name__=="__main__": raise SystemExit(main())
