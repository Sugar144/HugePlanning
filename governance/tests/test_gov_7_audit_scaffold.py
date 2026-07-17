from __future__ import annotations

import hashlib
from pathlib import Path
import shutil

import pytest
import yaml

from governance.tools.validate_audit_scaffold import (
    C1_ARTIFACT_HASHES,
    C2_AUTHORIZATION_HASH,
    C2_INPUT_HASH,
    C2_OUTPUT_HASHES,
    C2_PROMPT_HASH,
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
P02_REL = AUDIT_REL / "runs/GOV-AUD-001-P02-R1"
P03_REL = AUDIT_REL / "runs/GOV-AUD-001-P03-R1"
C2_REL = RUN_REL / "corrections/GOV-AUD-001-P01-R1-C2"
C3_REL = RUN_REL / "corrections/GOV-AUD-001-P01-R1-C3"
ACCEPTANCE_REL = AUDIT_REL / "decisions/GOV-AUD-DECISION-001-pass-01-acceptance-v0.1.0.yaml"
C2_REGISTRY_IDS = {
    "GOV-AUD-001-P01-R1-C2",
    "GOV-AUD-CORR-AUTH-002",
    "HP-PROMPT-026",
    "GOV-AUD-C2-OUT-001",
    "GOV-AUD-C2-OUT-002",
    "GOV-AUD-C2-OUT-003",
    "GOV-AUD-C2-OUT-004",
    "GOV-AUD-C2-VAL-001",
}
P02_REGISTRY_IDS = {
    "GOV-AUD-001-P02-R1",
    "GOV-AUD-AUTH-002",
    "HP-PROMPT-029",
    "GOV-AUD-P02-OUT-001",
    "GOV-AUD-P02-OUT-002",
    "GOV-AUD-P02-OUT-003",
    "GOV-AUD-P02-OUT-004",
    "GOV-AUD-P02-OUT-005",
    "GOV-AUD-P02-OUT-006",
    "GOV-AUD-P02-OUT-007",
    "GOV-AUD-VAL-002",
    "GOV-AUD-001-P02-REVIEW-CUSTODY-001",
    "GOV-AUD-001-P02-IER-002",
}
P03_REGISTRY_IDS = {
    "GOV-AUD-001-P03-R1", "GOV-AUD-AUTH-003", "HP-PROMPT-035",
    "GOV-AUD-P03-INPUT-001", "GOV-AUD-P03-OUT-001", "GOV-AUD-P03-OUT-002",
    "GOV-AUD-P03-OUT-003", "GOV-AUD-P03-OUT-004", "GOV-AUD-P03-OUT-005",
    "GOV-AUD-P03-OUT-006", "GOV-AUD-P03-OUT-007", "GOV-AUD-P03-OUT-008",
    "GOV-AUD-P03-OUT-009", "GOV-AUD-P03-VAL-001", "GOV-AUD-P03-REVIEW-PACKAGE-001",
}


def isolated(tmp_path: Path) -> Path:
    target = tmp_path / "repository"
    shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns(".agents", ".codex", "__pycache__"))
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
            substantive_correction_id=None,
            pass_01_accepted=False,
            checkpoints_approved=0,
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
            pass_01_accepted=False,
            checkpoints_completed=0,
            pass_01_status="PLANNED_NOT_EXECUTED",
            pass_02_status="PLANNED_NOT_EXECUTED",
            last_completed_step="NONE",
            next_action="SEPARATE_PROJECT_OWNER_PASS_01_AUTHORIZATION_REQUIRED",
        )
        status.pop("pass_02_execution_authorized", None)
        status.pop("pass_02_authorization_consumed", None)
        status.pop("pass_02_execution", None)
        status.pop("validation_lifecycle_correction", None)
        status.pop("substantive_output_correction", None)

    rewrite_yaml(audit / "01-audit-plan.yaml", plan_mutation)
    rewrite_yaml(audit / "02-audit-status.yaml", status_mutation)
    rewrite_yaml(
        audit / "prompt-registry.yaml",
        lambda doc: doc["prompt_registry"].update(
            version="0.1.0",
            prompts=[
                item for item in doc["prompt_registry"]["prompts"]
                if item["prompt_id"] not in {"GOV-AUD-PROMPT-011", "GOV-AUD-PROMPT-012", "GOV-AUD-PROMPT-013", "GOV-AUD-PROMPT-015", "GOV-AUD-PROMPT-016", "GOV-AUD-PROMPT-021", "HP-PROMPT-033", "GOV-AUD-PROMPT-031"}
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
        "GOV-AUD-001-P01-C2-IER-001",
        "GOV-AUD-001-P01-R1-C3", "HP-PROMPT-027", "GOV-AUD-001-P01-C3-IER-001",
        "GOV-AUD-DECISION-001", "HP-PROMPT-028",
    } | C2_REGISTRY_IDS | P02_REGISTRY_IDS | P03_REGISTRY_IDS | {"GOV-AUD-DECISION-003", "HP-PROMPT-033", "GOV-AUD-001-PASS-03-CONTRACT", "GOV-AUD-P03-PREP-INPUT-001", "GOV-AUD-P03-OUTPUT-SPEC-001", "GOV-AUD-P03-VALIDATION-PLAN-001", "GOV-AUD-P03-ADVERSARIAL-PLAN-001"}

    def registry_mutation(doc: dict) -> None:
        doc["artifacts"] = [item for item in doc["artifacts"] if item["id"] not in run_and_correction_ids]
        next(item for item in doc["artifacts"] if item["id"] == "GOV-AUD-001")["status"] = "PLANNED_NOT_EXECUTED"

    rewrite_yaml(root / "governance/ARTIFACT_REGISTRY.yaml", registry_mutation)
    runs_readme = audit / "runs/README.md"
    runs_readme.write_text(runs_readme.read_text().split("## Registered runs", 1)[0] + "## Registered runs\n\n- None.\n")
    (audit / "decisions/GOV-AUD-DECISION-001-pass-01-acceptance-v0.1.0.yaml").unlink()
    (audit / "decisions/GOV-AUD-DECISION-003-pass-02-checkpoint-a-approval-v0.1.0.yaml").unlink()
    shutil.rmtree(root / RUN_REL)
    shutil.rmtree(root / P02_REL)
    shutil.rmtree(root / P03_REL)


def c1_only(root: Path) -> None:
    audit = root / AUDIT_REL

    def plan_mutation(doc: dict) -> None:
        plan = doc["audit_program"]
        plan.update(
            status="IN_PROGRESS_PASS_01_EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION",
            authority="PASS_01_ONLY_PROJECT_OWNER_AUTHORIZATION_CONSUMED",
            passes_executed=1,
            substantive_correction_id=None,
            pass_01_accepted=False,
            checkpoints_approved=0,
        )
        next(item for item in plan["sequence"] if item["id"] == "PASS-01")["status"] = "EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION"
        next(item for item in plan["sequence"] if item["id"] == "PASS-02")["status"] = "PLANNED_NOT_EXECUTED"
        next(item for item in plan["sequence"] if item["id"] == "CHECKPOINT-A")["status"] = "PENDING_OWNER_DECISION"
        next(item for item in plan["sequence"] if item["id"] == "PASS-03")["status"] = "PLANNED_NOT_EXECUTED"

    def status_mutation(doc: dict) -> None:
        status = doc["audit"]
        status.update(
            status="IN_PROGRESS_PASS_01_EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION",
            authority="PASS_01_ONLY_PROJECT_OWNER_AUTHORIZATION_CONSUMED",
            passes_executed=1,
            pass_01_status="EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION",
            pass_02_status="PLANNED_NOT_EXECUTED",
            pass_01_accepted=False,
            checkpoints_completed=0,
            pass_03_preparation_status=None,
            pass_03_execution_authorized=False,
            pass_03_executed=False,
            last_completed_step="PASS_01_EXECUTED_AND_VALIDATED",
            next_action="PROJECT_OWNER_PASS_01_DISPOSITION_AND_SEPARATE_PASS_02_AUTHORIZATION_DECISION",
        )
        status.pop("pass_02_execution_authorized", None)
        status.pop("pass_02_authorization_consumed", None)
        status.pop("pass_02_execution", None)
        status.pop("substantive_output_correction", None)

    rewrite_yaml(audit / "01-audit-plan.yaml", plan_mutation)
    rewrite_yaml(audit / "02-audit-status.yaml", status_mutation)
    rewrite_yaml(
        audit / "prompt-registry.yaml",
        lambda doc: doc["prompt_registry"].update(
            version="0.2.0",
            prompts=[item for item in doc["prompt_registry"]["prompts"] if item["prompt_id"] not in {"GOV-AUD-PROMPT-013", "GOV-AUD-PROMPT-015", "GOV-AUD-PROMPT-016", "GOV-AUD-PROMPT-021", "HP-PROMPT-033", "GOV-AUD-PROMPT-031"}],
        ),
    )

    def registry_mutation(doc: dict) -> None:
        removed = C2_REGISTRY_IDS | P02_REGISTRY_IDS | P03_REGISTRY_IDS | {"GOV-AUD-001-P01-R1-C3", "HP-PROMPT-027", "GOV-AUD-001-P01-C3-IER-001", "GOV-AUD-DECISION-001", "HP-PROMPT-028", "GOV-AUD-DECISION-003", "HP-PROMPT-033", "GOV-AUD-001-PASS-03-CONTRACT", "GOV-AUD-P03-PREP-INPUT-001", "GOV-AUD-P03-OUTPUT-SPEC-001", "GOV-AUD-P03-VALIDATION-PLAN-001", "GOV-AUD-P03-ADVERSARIAL-PLAN-001"}
        doc["artifacts"] = [item for item in doc["artifacts"] if item["id"] not in removed]
        next(item for item in doc["artifacts"] if item["id"] == "GOV-AUD-001")["status"] = "IN_PROGRESS_PASS_01_EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION"

    rewrite_yaml(root / "governance/ARTIFACT_REGISTRY.yaml", registry_mutation)
    (audit / "decisions/GOV-AUD-DECISION-001-pass-01-acceptance-v0.1.0.yaml").unlink()
    (audit / "decisions/GOV-AUD-DECISION-003-pass-02-checkpoint-a-approval-v0.1.0.yaml").unlink()
    shutil.rmtree(root / C3_REL)
    shutil.rmtree(root / C2_REL)
    shutil.rmtree(root / P02_REL)
    shutil.rmtree(root / P03_REL)


def test_canonical_three_pass_executed_state_is_valid() -> None:
    assert validate(ROOT) == {"result": "VALID", "diagnostics": []}


def test_coherent_c1_only_state_is_valid(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    c1_only(root)
    assert validate(root) == {"result": "VALID", "diagnostics": []}


def test_coherent_planning_only_state_is_valid(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    planning_only(root)
    assert validate(root) == {"result": "VALID", "diagnostics": []}


def test_exact_prompt_hashes_and_substantive_output_hashes() -> None:
    scaffold_prompt = AUDIT / "prompts/GOV-AUD-PROMPT-000-audit-program-scaffold-v0.2.0.md"
    correction_prompt = AUDIT / "runs/GOV-AUD-001-P01-R1/corrections/GOV-AUD-001-P01-R1-C1/prompt/GOV-AUD-PROMPT-012-correct-pass-01-audit-validation-lifecycle-v0.1.0.md"
    assert hashlib.sha256(scaffold_prompt.read_bytes()).hexdigest() == PROMPT_HASH
    assert hashlib.sha256(correction_prompt.read_bytes()).hexdigest() == CORRECTION_PROMPT_HASH
    c2_prompt = AUDIT / "runs/GOV-AUD-001-P01-R1/corrections/GOV-AUD-001-P01-R1-C2/prompt/GOV-AUD-PROMPT-013-correct-pass-01-substantive-outputs-v0.1.0.md"
    c2_authorization = AUDIT / "runs/GOV-AUD-001-P01-R1/corrections/GOV-AUD-001-P01-R1-C2/authorization/GOV-AUD-CORR-AUTH-002-v0.1.0.yaml"
    c2_input = AUDIT / "runs/GOV-AUD-001-P01-R1/corrections/GOV-AUD-001-P01-R1-C2/input/input-manifest.yaml"
    assert hashlib.sha256(c2_prompt.read_bytes()).hexdigest() == C2_PROMPT_HASH
    assert hashlib.sha256(c2_authorization.read_bytes()).hexdigest() == C2_AUTHORIZATION_HASH
    assert hashlib.sha256(c2_input.read_bytes()).hexdigest() == C2_INPUT_HASH
    for name, expected in OUTPUT_HASHES.items():
        output = AUDIT / "runs/GOV-AUD-001-P01-R1/output" / name
        assert hashlib.sha256(output.read_bytes()).hexdigest() == expected
    for name, expected in C2_OUTPUT_HASHES.items():
        output = AUDIT / "runs/GOV-AUD-001-P01-R1/corrections/GOV-AUD-001-P01-R1-C2/output" / name
        assert hashlib.sha256(output.read_bytes()).hexdigest() == expected
    c1 = AUDIT / "runs/GOV-AUD-001-P01-R1/corrections/GOV-AUD-001-P01-R1-C1"
    for relative, expected in C1_ARTIFACT_HASHES.items():
        assert hashlib.sha256((c1 / relative).read_bytes()).hexdigest() == expected


def test_pass_contracts_remain_planned_and_run_is_registered() -> None:
    for pass_id in PASS_IDS:
        contract = yaml.safe_load((AUDIT / f"passes/{pass_id}/contract.yaml").read_text())["pass"]
        expected = "PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION" if pass_id == "PASS-03" else "PLANNED_NOT_EXECUTED"
        assert contract["status"] == expected
    run_dirs = sorted(path.name for path in (AUDIT / "runs").iterdir() if path.is_dir())
    assert run_dirs == ["GOV-AUD-001-P01-R1", "GOV-AUD-001-P02-R1", "GOV-AUD-001-P03-R1"]


def test_only_affected_pass_contracts_have_bindable_versions() -> None:
    expected = {
        "PASS-02": "GOV-AUD-001-PASS-02-CONTRACT",
        "PASS-03": "GOV-AUD-001-PASS-03-CONTRACT",
        "PASS-07": "GOV-AUD-001-PASS-07-CONTRACT",
    }
    for pass_id in PASS_IDS:
        contract = yaml.safe_load((AUDIT / f"passes/{pass_id}/contract.yaml").read_text())["pass"]
        identity = contract.get("contract_identity")
        if pass_id in expected:
            assert identity["contract_id"] == expected[pass_id]
            assert identity["version"] == "0.2.0"
            if pass_id != "PASS-03":
                assert identity["prompt_binding_rule"] == "INSTANTIATED_PROMPT_MUST_BIND_CONTRACT_ID_VERSION_AND_SHA256"
        else:
            assert identity is None


def test_rejects_pass_contract_without_bindable_version(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / AUDIT_REL / "passes/PASS-07/contract.yaml"
    rewrite_yaml(path, lambda doc: doc["pass"].pop("contract_identity"))
    assert "versioned contract binding mismatch: PASS-07" in diagnostics(root)


def test_rejects_pass_07_without_insufficient_evidence_result(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / AUDIT_REL / "passes/PASS-07/contract.yaml"
    rewrite_yaml(
        path,
        lambda doc: doc["pass"]["output_structure"]["permitted_results"].remove(
            "INSUFFICIENT_EVIDENCE_FOR_PASS_07_DISPOSITION"
        ),
    )
    assert "PASS-07 review-type or result contract mismatch" in diagnostics(root)


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


def test_rejects_pass_03_execution_before_checkpoint_a(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / AUDIT_REL / "01-audit-plan.yaml"
    rewrite_yaml(
        path,
        lambda doc: next(item for item in doc["audit_program"]["sequence"] if item["id"] == "PASS-03").update(status="EXECUTED"),
    )
    assert "sequence status mismatch: PASS-03" in diagnostics(root)


def test_rejects_automatic_pass_01_acceptance_without_decision(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    (root / AUDIT_REL / "decisions/GOV-AUD-DECISION-001-pass-01-acceptance-v0.1.0.yaml").unlink()
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


def test_rejects_mutated_original_output_under_c2(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/01-verified-capability-inventory.yaml"
    path.write_text(path.read_text() + "\n")
    assert "C2 immutable R1 output mismatch" in diagnostics(root)


def test_rejects_mutated_c1_artifact_under_c2(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "corrections/GOV-AUD-001-P01-R1-C1/manifest.yaml"
    path.write_text(path.read_text() + "\n")
    assert "C2 immutable C1 artifact mismatch" in diagnostics(root)


def test_rejects_c2_input_hash_drift(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / C2_REL / "input/input-manifest.yaml"
    rewrite_yaml(path, lambda doc: doc["manifest"]["inputs"][0].update(sha256="0" * 64))
    assert "C2 input manifest custody or hash mismatch" in diagnostics(root)


def test_rejects_not_a_gap_high_leverage(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / C2_REL / "output/03-corrected-ranked-gap-register.yaml"
    rewrite_yaml(
        path,
        lambda doc: next(item for item in doc["gap_register"]["entries"] if item["gap_id"] == "GAP-013").update(preliminary_leverage="HIGH"),
    )
    text = diagnostics(root)
    assert "C2 output custody or hash mismatch" in text or "C2 NOT_A_GAP leverage mismatch" in text


def test_rejects_unconditional_provider_p0_priority(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / C2_REL / "output/03-corrected-ranked-gap-register.yaml"
    rewrite_yaml(
        path,
        lambda doc: next(item for item in doc["gap_register"]["entries"] if item["gap_id"] == "GAP-008").update(priority="P0_BEFORE_MATERIAL_GOV_7_WORK"),
    )
    text = diagnostics(root)
    assert "C2 output custody or hash mismatch" in text or "C2 trigger priority mismatch: GAP-008" in text


def test_rejects_c3_compound_classification(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / C3_REL / "output/03-corrected-ranked-gap-register.yaml"
    rewrite_yaml(path, lambda doc: next(item for item in doc["gap_register"]["entries"] if item["gap_id"] == "GAP-002").update(classification="DEMONSTRATED_HISTORICAL_RESIDUAL_GAP"))
    assert "C3 noncanonical or compound classification: GAP-002" in diagnostics(root)


def test_rejects_historical_corrected_current_residual_claim(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / C3_REL / "output/03-corrected-ranked-gap-register.yaml"
    rewrite_yaml(path, lambda doc: next(item for item in doc["gap_register"]["entries"] if item["gap_id"] == "GAP-001").update(current_residual_status="DEMONSTRATED"))
    assert "C3 historical corrected item asserted as current residual: GAP-001" in diagnostics(root)


def test_generic_historical_rule_handles_synthetic_gap_id(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / C3_REL / "output/03-corrected-ranked-gap-register.yaml"
    def mutate(doc: dict) -> None:
        entry = next(item for item in doc["gap_register"]["entries"] if item["gap_id"] == "GAP-002")
        entry.update(gap_id="GAP-SYNTHETIC-901", current_residual_status="DEMONSTRATED")
    rewrite_yaml(path, mutate)
    assert "C3 historical corrected item asserted as current residual: GAP-SYNTHETIC-901" in diagnostics(root)


def test_c3_temporal_semantics_validator_has_no_named_gap_rule() -> None:
    source = (ROOT / "governance/tools/validate_audit_scaffold.py").read_text()
    function = source.split("def validate_c3_classification_and_temporal_semantics", 1)[1].split("def validate_substantive_correction_custody", 1)[0]
    assert "GAP-002" not in function
    assert "GAP-003" not in function
