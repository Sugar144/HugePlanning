"""Bounded properties of Controller calculation and history replay."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

from hypothesis import given, strategies as st

from apply_loop_transition import NON_COMPLETION, blocking_signature, calculate, replay
from conftest import LOOP


COUNTER_KEYS = ("completed_targeted_closure_runs", "completed_designer_remediation_runs")
ADVERSARY_RESULTS = (
    "STRUCTURAL_REDESIGN_REQUIRED",
    "OWNER_DECISION_REQUIRED",
    "RESEARCH_REQUIRED",
    "DESIGNER_REMEDIATION_REQUIRED",
    "CLOSURE_CONFIRMED",
)
DESIGNER_RESULTS = (
    "STRUCTURAL_REDESIGN_REQUIRED",
    "OWNER_DECISION_REQUIRED",
    "RESEARCH_REQUIRED",
    "READY_FOR_TARGETED_CLOSURE",
)


def request(role: str, result: str, targeted: int, remediation: int) -> tuple[str, dict]:
    adversary = role == "adversary"
    return (
        "KGR-005" if adversary else "KGR-006",
        {
            "fixture_id": "generated",
            "input_state": "TARGETED_CLOSURE_IN_PROGRESS" if adversary else "DESIGNER_REMEDIATION_IN_PROGRESS",
            "source_role": role,
            "source_mode": "TARGETED_CLOSURE" if adversary else "CLOSURE_REMEDIATION",
            "input_result": result,
            "counters_before": {
                "completed_targeted_closure_runs": targeted,
                "completed_designer_remediation_runs": remediation,
            },
            "history": [],
        },
    )


@given(
    role=st.sampled_from(("adversary", "designer")),
    targeted=st.integers(min_value=0, max_value=2),
    remediation=st.integers(min_value=0, max_value=1),
    data=st.data(),
)
def test_counters_never_decrease(role: str, targeted: int, remediation: int, data: st.DataObject, tmp_path: Path) -> None:
    results = ADVERSARY_RESULTS if role == "adversary" else DESIGNER_RESULTS
    source_run, payload = request(role, data.draw(st.sampled_from(results)), targeted, remediation)
    record, diagnostics, _ = calculate("import", LOOP, source_run, payload, tmp_path, None, False)
    assert diagnostics == []
    for key in COUNTER_KEYS:
        assert record["counters_after"][key] >= record["counters_before"][key]


@given(
    role=st.sampled_from(("adversary", "designer")),
    outcome=st.sampled_from(sorted(NON_COMPLETION)),
    targeted=st.integers(min_value=0, max_value=3),
    remediation=st.integers(min_value=0, max_value=2),
)
def test_non_completion_inputs_do_not_consume_counters(
    role: str, outcome: str, targeted: int, remediation: int, tmp_path: Path
) -> None:
    source_run, payload = request(role, outcome, targeted, remediation)
    record, diagnostics, recordable = calculate("import", LOOP, source_run, payload, tmp_path, None, False)
    assert diagnostics == []
    assert recordable is False
    assert record["counters_after"] == record["counters_before"]


@given(
    role=st.sampled_from(("adversary", "designer")),
    invalid_result=st.text(min_size=1, max_size=16),
)
def test_invalid_inputs_are_not_accepted(role: str, invalid_result: str, tmp_path: Path) -> None:
    source_run, payload = request(role, invalid_result, 1, 1)
    payload["input_result"] = "INVALID_GENERATED_" + invalid_result
    before = list(tmp_path.rglob("controller-transition.json"))
    _, diagnostics, _ = calculate("import", LOOP, source_run, payload, tmp_path, None, False)
    after = list(tmp_path.rglob("controller-transition.json"))
    assert "RESULT_ENUM_INVALID" in {diagnostic.code for diagnostic in diagnostics}
    assert before == after == []


def test_fourth_targeted_closure_and_third_remediation_are_refused(tmp_path: Path) -> None:
    adversary_run, adversary = request("adversary", "CLOSURE_CONFIRMED", 3, 2)
    _, adversary_diags, _ = calculate("import", LOOP, adversary_run, adversary, tmp_path, None, False)
    designer_run, designer = request("designer", "READY_FOR_TARGETED_CLOSURE", 2, 2)
    _, designer_diags, _ = calculate("import", LOOP, designer_run, designer, tmp_path, None, False)
    assert "TARGETED_CLOSURE_LIMIT_EXCEEDED" in {item.code for item in adversary_diags}
    assert "DESIGNER_REMEDIATION_LIMIT_EXCEEDED" in {item.code for item in designer_diags}
    assert not list(tmp_path.rglob("controller-transition.json"))


def test_designer_cannot_produce_closure_confirmed(tmp_path: Path) -> None:
    source_run, payload = request("designer", "CLOSURE_CONFIRMED", 1, 0)
    _, diagnostics, _ = calculate("import", LOOP, source_run, payload, tmp_path, None, False)
    assert "RESULT_ENUM_INVALID" in {item.code for item in diagnostics}


@given(terminal=st.sampled_from(("CLOSURE_CONFIRMED", "LOOP_LIMIT_REACHED", "STRUCTURAL_REDESIGN_REQUIRED")))
def test_terminal_states_cannot_continue_automatically(terminal: str, tmp_path: Path) -> None:
    history = [{
        "source_run": "KGR-005",
        "previous_state": "READY_FOR_TARGETED_CLOSURE",
        "counters_before": {"completed_targeted_closure_runs": 0, "completed_designer_remediation_runs": 0},
        "counters_after": {"completed_targeted_closure_runs": 1, "completed_designer_remediation_runs": 0},
        "resulting_state": terminal,
    }]
    payload = {"typed_event": "TARGETED_CLOSURE_EXECUTION_BEGAN", "history": history}
    record, diagnostics, _ = calculate("event", LOOP, "KGR-006", payload, tmp_path, None, False)
    assert "EVENT_SOURCE_STATE_INVALID" in {item.code for item in diagnostics}
    assert record["resulting_state"] == terminal
    assert record["next_role"] is None and record["next_mode"] is None


@given(st.permutations((
    {"finding_id": "KA-F-019", "severity": "MEDIUM", "adversary_verdict": "NEW_FINDING"},
    {"finding_id": "KA-F-020", "severity": "HIGH", "adversary_verdict": "REOPENED", "failed_criteria": ["b", "a"]},
    {"finding_id": "KA-F-021", "severity": "LOW", "adversary_verdict": "NEW_FINDING", "blocking": False},
)))
def test_finding_signatures_are_independent_of_input_order(findings: list[dict]) -> None:
    expected = blocking_signature(sorted(deepcopy(findings), key=lambda item: item["finding_id"]))
    assert blocking_signature(list(findings)) == expected


@given(st.lists(st.sampled_from(("READY_FOR_TARGETED_CLOSURE", "OWNER_DECISION_REQUIRED", "RESEARCH_REQUIRED")), min_size=0, max_size=5))
def test_history_replay_is_deterministic(states: list[str]) -> None:
    records = []
    state = "READY_FOR_TARGETED_CLOSURE"
    counters = {"completed_targeted_closure_runs": 0, "completed_designer_remediation_runs": 0}
    for index, resulting in enumerate(states):
        record = {
            "source_run": f"KGR-{index + 5:03d}", "previous_state": state,
            "counters_before": dict(counters), "counters_after": dict(counters),
            "resulting_state": resulting,
        }
        records.append(record)
        state = resulting
    assert replay(deepcopy(records)) == replay(deepcopy(records))
