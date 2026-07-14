"""Stateful comparison of a small loop model with Controller calculation."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import tempfile

from hypothesis import settings, strategies as st
from hypothesis.stateful import RuleBasedStateMachine, invariant, precondition, rule

from apply_loop_transition import calculate, replay
from conftest import LOOP, STATE_MACHINE_EXAMPLES, STATE_MACHINE_STEPS


ZERO = {"completed_targeted_closure_runs": 0, "completed_designer_remediation_runs": 0}
TERMINAL = {"CLOSURE_CONFIRMED", "STRUCTURAL_REDESIGN_REQUIRED", "LOOP_LIMIT_REACHED"}
ADVERSARY_RESULTS = (
    "CLOSURE_CONFIRMED", "DESIGNER_REMEDIATION_REQUIRED", "OWNER_DECISION_REQUIRED",
    "RESEARCH_REQUIRED", "STRUCTURAL_REDESIGN_REQUIRED",
)
DESIGNER_RESULTS = (
    "READY_FOR_TARGETED_CLOSURE", "OWNER_DECISION_REQUIRED",
    "RESEARCH_REQUIRED", "STRUCTURAL_REDESIGN_REQUIRED",
)
NON_COMPLETIONS = ("INVALID_IMPORT", "PAUSED", "INTERRUPTED", "BLOCKED_BY_PACKAGE_CONFLICT")


class ControllerModel(RuleBasedStateMachine):
    """Compare routing/counters only; constitutional judgments stay outside the model."""

    def __init__(self) -> None:
        super().__init__()
        self.state = "READY_FOR_TARGETED_CLOSURE"
        self.counters = dict(ZERO)
        self.accepted_history: list[dict] = []
        self.last_record: dict | None = None
        self.temp = tempfile.TemporaryDirectory(prefix="hp-controller-stateful.")
        self.history_root = Path(self.temp.name)

    def teardown(self) -> None:
        self.temp.cleanup()

    def _history_for_current_state(self) -> list[dict]:
        if self.state == "READY_FOR_TARGETED_CLOSURE" and self.counters == ZERO:
            return []
        return [{
            "source_run": "KGR-004",
            "previous_state": "READY_FOR_TARGETED_CLOSURE",
            "counters_before": dict(ZERO),
            "counters_after": dict(self.counters),
            "resulting_state": self.state,
        }]

    def _calculate(self, command: str, source_run: str, payload: dict) -> tuple[dict, list, bool]:
        record, diagnostics, recordable = calculate(
            command, LOOP, source_run, payload, self.history_root, None, False
        )
        self.last_record = record
        return record, diagnostics, recordable

    @precondition(lambda self: self.state == "READY_FOR_TARGETED_CLOSURE")
    @rule()
    def begin_targeted_closure(self) -> None:
        payload = {"typed_event": "TARGETED_CLOSURE_EXECUTION_BEGAN", "history": self._history_for_current_state()}
        record, diagnostics, _ = self._calculate("event", f"KGR-{5 + 2 * self.counters['completed_targeted_closure_runs']:03d}", payload)
        assert diagnostics == []
        self.state = "TARGETED_CLOSURE_IN_PROGRESS"
        assert record["resulting_state"] == self.state

    @precondition(lambda self: self.state == "DESIGNER_REMEDIATION_REQUIRED")
    @rule()
    def begin_designer_remediation(self) -> None:
        payload = {"typed_event": "DESIGNER_REMEDIATION_EXECUTION_BEGAN", "history": self._history_for_current_state()}
        record, diagnostics, _ = self._calculate("event", f"KGR-{6 + 2 * self.counters['completed_designer_remediation_runs']:03d}", payload)
        assert diagnostics == []
        self.state = "DESIGNER_REMEDIATION_IN_PROGRESS"
        assert record["resulting_state"] == self.state

    @precondition(lambda self: self.state == "TARGETED_CLOSURE_IN_PROGRESS")
    @rule(result=st.sampled_from(ADVERSARY_RESULTS))
    def import_targeted_closure(self, result: str) -> None:
        before_state = self.state
        payload = {
            "fixture_id": "stateful", "input_state": self.state, "source_role": "adversary",
            "source_mode": "TARGETED_CLOSURE", "input_result": result,
            "counters_before": dict(self.counters), "history": [],
        }
        source_run = f"KGR-{5 + 2 * self.counters['completed_targeted_closure_runs']:03d}"
        record, diagnostics, _ = self._calculate("import", source_run, payload)
        assert diagnostics == []
        self.counters["completed_targeted_closure_runs"] += 1
        if result == "DESIGNER_REMEDIATION_REQUIRED":
            if self.counters["completed_targeted_closure_runs"] >= 3 or self.counters["completed_designer_remediation_runs"] >= 2:
                self.state = "LOOP_LIMIT_REACHED"
            else:
                self.state = "DESIGNER_REMEDIATION_REQUIRED"
        else:
            self.state = result
        self._accept(source_run, before_state, record)

    @precondition(lambda self: self.state == "DESIGNER_REMEDIATION_IN_PROGRESS")
    @rule(result=st.sampled_from(DESIGNER_RESULTS))
    def import_designer_remediation(self, result: str) -> None:
        before_state = self.state
        payload = {
            "fixture_id": "stateful", "input_state": self.state, "source_role": "designer",
            "source_mode": "CLOSURE_REMEDIATION", "input_result": result,
            "counters_before": dict(self.counters), "history": [],
        }
        source_run = f"KGR-{6 + 2 * self.counters['completed_designer_remediation_runs']:03d}"
        record, diagnostics, _ = self._calculate("import", source_run, payload)
        assert diagnostics == []
        self.counters["completed_designer_remediation_runs"] += 1
        self.state = result
        self._accept(source_run, before_state, record)

    @precondition(lambda self: self.state in {"OWNER_DECISION_REQUIRED", "RESEARCH_REQUIRED"})
    @rule(route=st.sampled_from(("READY_FOR_TARGETED_CLOSURE", "DESIGNER_REMEDIATION_REQUIRED", "OWNER_DECISION_REQUIRED")))
    def validated_reentry(self, route: str) -> None:
        allowed = {
            "OWNER_DECISION_REQUIRED": {"READY_FOR_TARGETED_CLOSURE", "DESIGNER_REMEDIATION_REQUIRED"},
            "RESEARCH_REQUIRED": {"READY_FOR_TARGETED_CLOSURE", "DESIGNER_REMEDIATION_REQUIRED", "OWNER_DECISION_REQUIRED"},
        }
        before_state = self.state
        payload = {
            "resulting_state": route,
            "artifact": {"id": "STATEFUL-REENTRY", "applicable": True},
            "history": self._history_for_current_state(),
        }
        record, diagnostics, _ = self._calculate("reenter", f"KGR-{20 + len(self.accepted_history):03d}", payload)
        if route not in allowed[before_state]:
            assert "REENTRY_ROUTE_INVALID" in {item.code for item in diagnostics}
            assert self.state == before_state
            return
        assert diagnostics == []
        self.state = route
        self._accept(record["source_run"], before_state, record)

    @rule(outcome=st.sampled_from(NON_COMPLETIONS))
    def invalid_or_noncompletion_does_not_mutate_history(self, outcome: str) -> None:
        before = (self.state, dict(self.counters), deepcopy(self.accepted_history))
        payload = {
            "fixture_id": "stateful-invalid", "input_state": self.state,
            "source_role": "adversary", "source_mode": "TARGETED_CLOSURE",
            "input_result": outcome, "counters_before": dict(self.counters), "history": [],
        }
        _, _, recordable = self._calculate("import", "KGR-005", payload)
        assert recordable is False
        assert before == (self.state, self.counters, self.accepted_history)

    @rule()
    def history_replay_is_stable(self) -> None:
        assert replay(deepcopy(self.accepted_history)) == replay(deepcopy(self.accepted_history))

    def _accept(self, source_run: str, before_state: str, record: dict) -> None:
        assert record["resulting_state"] == self.state
        assert record["counters_after"] == self.counters
        self.accepted_history.append({
            "source_run": source_run,
            "previous_state": before_state,
            "counters_before": record["counters_before"],
            "counters_after": record["counters_after"],
            "resulting_state": record["resulting_state"],
        })

    @invariant()
    def implementation_matches_reference_model(self) -> None:
        if self.last_record is not None:
            assert self.last_record["resulting_state"] == self.state
            assert self.last_record["counters_after"] == self.counters
        assert 0 <= self.counters["completed_targeted_closure_runs"] <= 3
        assert 0 <= self.counters["completed_designer_remediation_runs"] <= 2

    @invariant()
    def terminal_states_have_no_automatic_continuation(self) -> None:
        if self.state in TERMINAL and self.last_record is not None:
            assert self.last_record["next_role"] is None
            assert self.last_record["next_mode"] is None


TestControllerModel = ControllerModel.TestCase
TestControllerModel.settings = settings(
    max_examples=STATE_MACHINE_EXAMPLES,
    stateful_step_count=STATE_MACHINE_STEPS,
    deadline=None,
    database=None,
)
