from __future__ import annotations

import hashlib
from pathlib import Path
import shutil

import pytest
import yaml

from governance.tools.validate_audit_scaffold import (
    CORRECTION_PROMPT_HASH,
    OUTPUT_HASHES,
    PASS_IDS,
    PROMPT_HASH,
    validate,
)


ROOT = Path(__file__).resolve().parents[2]
AUDIT_REL = Path("governance/audits/GOV-AUD-001-gov7-enablement")
AUDIT = ROOT / AUDIT_REL
RUN_REL = AUDIT_REL / "runs/GOV-AUD-001-P01-R1"


def isolated(tmp_path: Path) -> Path:
    target = tmp_path / "repository"
    shutil.copytree(ROOT, target)
    return target


def rewrite_yaml(path: Path, mutate) -> None:
    value = yaml.safe_load(path.read_text())
    mutate(value)
    path.write_text(yaml.safe_dump(value, sort_keys=False))


def diagnostics(root: Path) -> str:
    return "\n".join(validate(root)["diagnostics"])


def planning_only(root: Path) -> None:
    audit = root / AUDIT_REL

    def plan_mutation(doc: dict) -> None:
        plan = doc["audit_program"]
        plan.update(
            status="PLANNED_NOT_EXECUTED",
            authority="SCAFFOLD_CREATION_ONLY",
            passes_executed=0,
            validation_correction_id=None,
        )
        for item in plan["sequence"]:
            item["status"] = "PENDING_OWNER_DECISION" if item["id"].startswith("CHECKPOINT") else "PLANNED_NOT_EXECUTED"

    def status_mutation(doc: dict) -> None:
        status = doc["audit"]
        status.update(
            status="PLANNED_NOT_EXECUTED",
            authority="SCAFFOLD_CREATION_ONLY",
            passes_executed=0,
            pass_01_execution_authorized=False,
            pass_01_authorization_consumed=False,
            pass_01_status="PLANNED_NOT_EXECUTED",
            pass_02_status="PLANNED_NOT_EXECUTED",
            last_completed_step="NONE",
            next_action="SEPARATE_PROJECT_OWNER_PASS_01_AUTHORIZATION_REQUIRED",
        )
        status.pop("validation_lifecycle_correction", None)

    rewrite_yaml(audit / "01-audit-plan.yaml", plan_mutation)
    rewrite_yaml(audit / "02-audit-status.yaml", status_mutation)
    rewrite_yaml(
        audit / "prompt-registry.yaml",
        lambda doc: doc["prompt_registry"].update(
            version="0.1.0",
            prompts=[
                item for item in doc["prompt_registry"]["prompts"]
                if item["prompt_id"] not in {"GOV-AUD-PROMPT-011", "GOV-AUD-PROMPT-012"}
            ]
        ),
    )
    run_and_correction_ids = {
        "GOV-AUD-001-P01-R1",
        "GOV-AUD-AUTH-001",
        "HP-PROMPT-024",
        "GOV-AUD-OUT-001",
        "GOV-AUD-OUT-002",
        "GOV-AUD-OUT-003",
        "GOV-AUD-OUT-004",
        "GOV-AUD-VAL-001",
        "GOV-AUD-001-P01-R1-C1",
        "GOV-AUD-CORR-AUTH-001",
        "HP-PROMPT-025",
    }

    def registry_mutation(doc: dict) -> None:
        doc["artifacts"] = [item for item in doc["artifacts"] if item["id"] not in run_and_correction_ids]
        next(item for item in doc["artifacts"] if item["id"] == "GOV-AUD-001")["status"] = "PLANNED_NOT_EXECUTED"

    rewrite_yaml(root / "governance/ARTIFACT_REGISTRY.yaml", registry_mutation)
    runs_readme = audit / "runs/README.md"
    runs_readme.write_text(runs_readme.read_text().split("## Registered runs", 1)[0] + "## Registered runs\n\n- None.\n")
    shutil.rmtree(root / RUN_REL)


def test_canonical_one_pass_executed_state_is_valid() -> None:
    assert validate(ROOT) == {"result": "VALID", "diagnostics": []}


def test_coherent_planning_only_state_is_valid(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    planning_only(root)
    assert validate(root) == {"result": "VALID", "diagnostics": []}


def test_exact_prompt_hashes_and_substantive_output_hashes() -> None:
    scaffold_prompt = AUDIT / "prompts/GOV-AUD-PROMPT-000-audit-program-scaffold-v0.2.0.md"
    correction_prompt = AUDIT / "runs/GOV-AUD-001-P01-R1/corrections/GOV-AUD-001-P01-R1-C1/prompt/GOV-AUD-PROMPT-012-correct-pass-01-audit-validation-lifecycle-v0.1.0.md"
    assert hashlib.sha256(scaffold_prompt.read_bytes()).hexdigest() == PROMPT_HASH
    assert hashlib.sha256(correction_prompt.read_bytes()).hexdigest() == CORRECTION_PROMPT_HASH
    for name, expected in OUTPUT_HASHES.items():
        output = AUDIT / "runs/GOV-AUD-001-P01-R1/output" / name
        assert hashlib.sha256(output.read_bytes()).hexdigest() == expected


def test_pass_contracts_remain_planned_and_run_is_registered() -> None:
    for pass_id in PASS_IDS:
        contract = yaml.safe_load((AUDIT / f"passes/{pass_id}/contract.yaml").read_text())["pass"]
        assert contract["status"] == "PLANNED_NOT_EXECUTED"
    run_dirs = sorted(path.name for path in (AUDIT / "runs").iterdir() if path.is_dir())
    assert run_dirs == ["GOV-AUD-001-P01-R1"]


def test_rejects_executed_pass_count_without_registered_run(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    shutil.rmtree(root / RUN_REL)
    assert "executed-pass count does not match registered run count" in diagnostics(root)


def test_rejects_registered_run_without_coherent_pass_status(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / AUDIT_REL / "01-audit-plan.yaml"
    rewrite_yaml(
        path,
        lambda doc: next(item for item in doc["audit_program"]["sequence"] if item["id"] == "PASS-01").update(status="PLANNED_NOT_EXECUTED"),
    )
    assert "sequence status mismatch: PASS-01" in diagnostics(root)


def test_rejects_pass_02_execution_before_checkpoint_a(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / AUDIT_REL / "01-audit-plan.yaml"
    rewrite_yaml(
        path,
        lambda doc: next(item for item in doc["audit_program"]["sequence"] if item["id"] == "PASS-02").update(status="EXECUTED"),
    )
    assert "PASS-02 executed before CHECKPOINT-A disposition" in diagnostics(root)


def test_rejects_automatic_pass_01_acceptance(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / AUDIT_REL / "02-audit-status.yaml"
    rewrite_yaml(path, lambda doc: doc["audit"].update(pass_01_accepted=True))
    assert "audit status pass_01_accepted mismatch" in diagnostics(root)


def test_rejects_gov_7_activation_after_pass_01(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / AUDIT_REL / "01-audit-plan.yaml"
    rewrite_yaml(path, lambda doc: doc["audit_program"].update(gov_7_activated=True))
    assert "audit plan gov_7_activated mismatch" in diagnostics(root)


@pytest.mark.parametrize("field", ["recommendations_accepted", "implementation_authorized"])
def test_rejects_recommendation_acceptance_or_implementation_authority(tmp_path: Path, field: str) -> None:
    root = isolated(tmp_path)
    path = root / AUDIT_REL / "02-audit-status.yaml"
    rewrite_yaml(path, lambda doc: doc["audit"].update({field: True}))
    assert f"audit status {field} mismatch" in diagnostics(root)
