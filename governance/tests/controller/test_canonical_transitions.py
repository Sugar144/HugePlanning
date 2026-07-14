"""Authoritative regression coverage for all twenty transition fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest

from _lib.strict_yaml import load
from apply_loop_transition import calculate
from conftest import LOOP, TRANSITION_FIXTURES


FIXTURES = sorted(TRANSITION_FIXTURES.glob("*.yaml"))


def test_canonical_fixture_inventory_is_exactly_twenty() -> None:
    assert len(FIXTURES) == 20
    assert [path.name[:2] for path in FIXTURES] == [f"{number:02d}" for number in range(1, 21)]


@pytest.mark.parametrize("fixture_path", FIXTURES, ids=lambda path: path.stem)
def test_canonical_transition(fixture_path: Path, tmp_path: Path) -> None:
    data = load(fixture_path)
    record, diagnostics, _ = calculate(
        "import", LOOP, data["source_run"], data, tmp_path / "history", None, False
    )

    expected = data["expected_diagnostic"]
    codes = {diagnostic.code for diagnostic in diagnostics}
    if expected:
        assert expected in codes
    else:
        assert diagnostics == []
    assert record["counters_after"] == data["expected_counters_after"]
    assert record["resulting_state"] == data["expected_transition"]
    assert record["next_role"] == data["expected_next_role"]
    assert record["next_mode"] == data["expected_next_mode"]
