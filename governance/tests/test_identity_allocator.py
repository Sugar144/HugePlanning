from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import json
from multiprocessing import get_context
from pathlib import Path

from governance.framework_runtime import l6_module

identity_module = l6_module("identity")
Allocator, parse, resolve_historical = identity_module.Allocator, identity_module.parse, identity_module.resolve_historical


def _allocate(state_path: str, ledger_path: str) -> str:
    allocator = Allocator(namespace="example.program", state_path=state_path, ledger_path=ledger_path)
    return allocator.allocate("RECORD", purpose="parallel test").identity


def test_parallel_allocations_are_unique_and_monotonic(tmp_path: Path) -> None:
    state_path = tmp_path / "state.json"
    ledger_path = tmp_path / "ledger.jsonl"
    with ThreadPoolExecutor(max_workers=8) as pool:
        identities = list(pool.map(_allocate, [str(state_path)] * 32, [str(ledger_path)] * 32))

    assert len(set(identities)) == 32
    assert {parse(identity).sequence for identity in identities} == set(range(1, 33))
    state = json.loads(state_path.read_text())
    assert state["next_sequences"] == {"RECORD": 33}
    assert len(ledger_path.read_text().splitlines()) == 32


def test_process_parallel_allocations_are_unique_and_monotonic(tmp_path: Path) -> None:
    state_path = tmp_path / "state.json"
    ledger_path = tmp_path / "ledger.jsonl"
    with get_context("spawn").Pool(8) as pool:
        identities = pool.starmap(_allocate, [(str(state_path), str(ledger_path))] * 32)

    assert len(set(identities)) == 32
    assert {parse(identity).sequence for identity in identities} == set(range(1, 33))
    assert json.loads(state_path.read_text())["next_sequences"] == {"RECORD": 33}
    assert len(ledger_path.read_text().splitlines()) == 32


def test_failed_publication_cannot_recycle_reserved_identity(tmp_path: Path) -> None:
    allocator = Allocator(namespace="example.program", state_path=tmp_path / "state.json", ledger_path=tmp_path / "ledger.jsonl")
    first = allocator.allocate("RECORD", purpose="failed later publication")
    second = allocator.allocate("RECORD", purpose="replacement publication")
    assert (first.sequence, second.sequence) == (1, 2)


def test_historical_references_are_preserved_or_forward_mapped() -> None:
    historical = "HP-FAIL-004"
    assert resolve_historical(historical, {}) == historical
    assert resolve_historical(historical, {historical: "hp.hugeplanning.learning:FAIL:000004"}) == "hp.hugeplanning.learning:FAIL:000004"
    try:
        resolve_historical("hp.hugeplanning.learning:FAIL:000004", {"hp.hugeplanning.learning:FAIL:000004": "hp.hugeplanning.learning:FAIL:000005"})
    except ValueError:
        pass
    else:  # pragma: no cover - explicit compatibility-direction guard
        raise AssertionError("namespaced mapping keys must be rejected")
