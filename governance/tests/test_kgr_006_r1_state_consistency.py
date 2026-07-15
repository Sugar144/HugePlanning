from __future__ import annotations

from pathlib import Path
import shutil
import json

import jsonschema
import yaml

from governance.tools.validate_governance_state import validate


ROOT = Path(__file__).resolve().parents[2]


def isolated(tmp_path: Path) -> Path:
    target = tmp_path / "repository"
    shutil.copytree(ROOT / "governance", target / "governance")
    return target


def rewrite_yaml(path: Path, mutate) -> None:
    value = yaml.safe_load(path.read_text())
    mutate(value)
    path.write_text(yaml.safe_dump(value, sort_keys=False))


def replace(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    assert old in text
    path.write_text(text.replace(old, new, 1))


def diagnostics(root: Path) -> str:
    return "\n".join(validate(root)["diagnostics"])


def test_canonical_state_is_consistent():
    assert validate(ROOT) == {"result": "VALID", "diagnostics": []}


def test_validation_record_conforms_to_canonical_schema():
    record = yaml.safe_load((ROOT / "governance/reviews/kgr-006-r1-owner-decisions-state-reconciliation/cross-surface-state-validation-v0.1.0.yaml").read_text())
    schema = json.loads((ROOT / "governance/schemas/governance-validation-record.schema.json").read_text())
    jsonschema.Draft202012Validator(schema).validate(record)


def test_rejects_consumed_authorization_represented_as_available(tmp_path):
    root = isolated(tmp_path)
    path = root / "governance/runs/KGR-006-R1-enforcement-analysis-correction/authorization/execution-authorization.yaml"
    rewrite_yaml(path, lambda doc: doc["execution_authorization"].update(execution_available=True))
    assert "authorization execution_available mismatch" in diagnostics(root)


def test_rejects_missing_terminal_authorization_reconciliation(tmp_path):
    root = isolated(tmp_path)
    path = root / "governance/runs/KGR-006-R1-enforcement-analysis-correction/authorization/execution-authorization.yaml"
    rewrite_yaml(path, lambda doc: doc["execution_authorization"].pop("terminal_reconciliation"))
    assert "missing terminal GOV-DEC-020 reconciliation" in diagnostics(root)


def test_rejects_inconsistent_od_002_or_od_003(tmp_path):
    root = isolated(tmp_path)
    path = root / "governance/reviews/kgr-006-r1-controlled-import-and-owner-review/project-owner-decision-record-v0.1.0.yaml"
    rewrite_yaml(path, lambda doc: doc["project_owner_decision_record"]["decisions"][0].update(selection="REJECT_SCOPE"))
    assert "exact selections" in diagnostics(root)


def test_rejects_obsolete_readme_kgr_005_gov_4_state(tmp_path):
    root = isolated(tmp_path)
    path = root / "governance/README.md"
    replace(path, "phase: GOV-5", "phase: GOV-4")
    assert "README phase mismatch" in diagnostics(root)


def test_rejects_gov_5_closed(tmp_path):
    root = isolated(tmp_path)
    path = root / "governance/CURRENT_STATE.md"
    replace(path, "gov_5_status: IN_PROGRESS", "gov_5_status: COMPLETED")
    assert "CURRENT_STATE gov_5_status mismatch" in diagnostics(root)


def test_rejects_gov_6_active(tmp_path):
    root = isolated(tmp_path)
    path = root / "governance/GOVERNANCE_MASTER_PLAN.md"
    replace(path, "gov_6_through_gov_9: INACTIVE", "gov_6_through_gov_9: ACTIVE")
    assert "GOVERNANCE_MASTER_PLAN gov_6_through_gov_9 mismatch" in diagnostics(root)


def test_rejects_ratified_kernel(tmp_path):
    root = isolated(tmp_path)
    path = root / "governance/CURRENT_STATE.md"
    replace(path, "kernel: 0.2.0-proposed/PROPOSED_NOT_RATIFIED", "kernel: 0.2.0/RATIFIED")
    assert "CURRENT_STATE kernel mismatch" in diagnostics(root)


def test_rejects_consuming_output_hash_mismatch(tmp_path):
    root = isolated(tmp_path)
    path = root / "governance/runs/KGR-006-R1-enforcement-analysis-correction/authorization/execution-authorization.yaml"
    rewrite_yaml(path, lambda doc: doc["execution_authorization"].update(consumed_by_output_package_sha256="0" * 64))
    assert "authorization consumed_by_output_package_sha256 mismatch" in diagnostics(root)
