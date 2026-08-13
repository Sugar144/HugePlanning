from __future__ import annotations

import ast
import json
from pathlib import Path

import pytest

from governance.framework_runtime import framework_path, l6_module

authority_module = l6_module("authority")
AppendOnlyAudit, AuthorityError, Authorization, Request, guarded_execute = (authority_module.AppendOnlyAudit, authority_module.AuthorityError, authority_module.Authorization, authority_module.Request, authority_module.guarded_execute)


def authority() -> Authorization:
    return Authorization(
        principal="delegated-agent", context="G6-B06", allowed_actions=("LOCAL_MODIFY", "DETERMINISTIC_VALIDATE", "LOCAL_COMMIT"),
        allowed_paths=("governance/core/l6", "governance/tests"), forbidden_actions=("PUSH", "PUBLICATION", "HISTORICAL_REWRITE", "ARCHITECTURE_CHANGE", "SCOPE_EXPANSION"),
        constraints={"side_effects": "local-only"}, provenance="GOV-GEN-G6-B06/0.1.0",
    )


@pytest.mark.parametrize("action", ["LOCAL_MODIFY", "DETERMINISTIC_VALIDATE", "LOCAL_COMMIT"])
def test_authorized_bounded_effect_runs_once(action: str, tmp_path: Path) -> None:
    effects: list[str] = []
    result = guarded_execute(authority(), Request("delegated-agent", "G6-B06", action, ("governance/core/l6/authority.py",)), AppendOnlyAudit(tmp_path / "audit.jsonl"), lambda: effects.append(action))
    assert result is None and effects == [action]


@pytest.mark.parametrize("action", ["PUSH", "PUBLICATION", "HISTORICAL_REWRITE", "ARCHITECTURE_CHANGE", "SCOPE_EXPANSION"])
def test_denied_action_never_runs_and_is_audited(action: str, tmp_path: Path) -> None:
    audit_path = tmp_path / "audit.jsonl"; effects: list[str] = []
    with pytest.raises(AuthorityError) as failure:
        guarded_execute(authority(), Request("delegated-agent", "G6-B06", action, ("governance/core/l6/authority.py",)), AppendOnlyAudit(audit_path), lambda: effects.append("ran"))
    refusal = json.loads(str(failure.value))
    assert effects == [] and refusal["state"] == "DENIED" and refusal["requested_action"] == action and refusal["authority_presented"] == "GOV-GEN-G6-B06/0.1.0" and refusal["retry_with_new_authority"] is True
    assert json.loads(audit_path.read_text()) ["decision"]["state"] == "DENIED"


def test_indeterminate_missing_authority_never_runs_and_appends_without_rewriting(tmp_path: Path) -> None:
    audit_path = tmp_path / "audit.jsonl"; audit_path.write_text('{"prior":true}\n'); prior = audit_path.read_bytes(); effects: list[str] = []
    with pytest.raises(AuthorityError) as failure:
        guarded_execute(None, Request("delegated-agent", "G6-B06", "LOCAL_MODIFY", ("governance/core/l6/authority.py",)), AppendOnlyAudit(audit_path), lambda: effects.append("ran"))
    refusal = json.loads(str(failure.value))
    assert effects == [] and refusal["state"] == "INDETERMINATE" and refusal["boundary"] == "explicit authority is missing" and refusal["retry_with_new_authority"] is True
    assert audit_path.read_bytes().startswith(prior)


def test_scope_escape_is_denied_without_partial_effect(tmp_path: Path) -> None:
    effects: list[str] = []
    with pytest.raises(AuthorityError):
        guarded_execute(authority(), Request("delegated-agent", "G6-B06", "LOCAL_MODIFY", ("governance/CURRENT_STATE.md",)), AppendOnlyAudit(tmp_path / "audit.jsonl"), lambda: effects.append("ran"))
    assert effects == []


def test_effect_callback_has_no_straightforward_unguarded_callsite() -> None:
    source = framework_path("framework/core/l6/authority.py").read_text()
    tree = ast.parse(source)
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "effect"]
    assert len(calls) == 1
    assert "if decision.state != AUTHORIZED:" in source
