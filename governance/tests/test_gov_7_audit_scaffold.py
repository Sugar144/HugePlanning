from __future__ import annotations

import hashlib
from pathlib import Path

import yaml

from governance.tools.validate_audit_scaffold import PASS_IDS, PROMPT_HASH, validate


ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "governance/audits/GOV-AUD-001-gov7-enablement"


def test_canonical_audit_scaffold_is_valid() -> None:
    assert validate(ROOT) == {"result": "VALID", "diagnostics": []}


def test_exact_scaffold_prompt_hash_and_planning_state() -> None:
    prompt = AUDIT / "prompts/GOV-AUD-PROMPT-000-audit-program-scaffold-v0.2.0.md"
    assert hashlib.sha256(prompt.read_bytes()).hexdigest() == PROMPT_HASH
    status = yaml.safe_load((AUDIT / "02-audit-status.yaml").read_text())
    assert status["audit"]["status"] == "PLANNED_NOT_EXECUTED"
    assert status["audit"]["passes_executed"] == 0
    assert status["audit"]["gov_7_activated"] is False
    assert status["audit"]["implementation_authorized"] is False


def test_all_passes_are_contracts_not_execution_outputs() -> None:
    for pass_id in PASS_IDS:
        contract = yaml.safe_load((AUDIT / f"passes/{pass_id}/contract.yaml").read_text())["pass"]
        assert contract["status"] == "PLANNED_NOT_EXECUTED"
    assert [path.name for path in (AUDIT / "runs").iterdir()] == ["README.md"]
    assert [path.name for path in (AUDIT / "decisions").iterdir()] == ["README.md"]
