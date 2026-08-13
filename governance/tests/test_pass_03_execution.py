from __future__ import annotations

from pathlib import Path
import shutil

import yaml

from governance.tools.validate_pass_03_execution import RUN_REL, validate


ROOT = Path(__file__).resolve().parents[2]


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


def test_canonical_pass_03_execution_is_valid() -> None:
    assert validate(ROOT) == {"result": "VALID", "diagnostics": []}


def test_rejects_missing_required_observable_field(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/01-observable-event-requirements.yaml"
    rewrite_yaml(
        path,
        lambda doc: doc["observable_event_requirements"].update(
            observable_fields=[
                item
                for item in doc["observable_event_requirements"]["observable_fields"]
                if item["field"] != "run_id"
            ]
        ),
    )
    assert "observable field or availability coverage mismatch" in diagnostics(root)


def test_rejects_evidence_class_collapse(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/02-evidence-and-authority-model.yaml"
    rewrite_yaml(path, lambda doc: doc["evidence_and_authority_model"]["evidence_classes"].pop())
    assert "evidence class distinction mismatch" in diagnostics(root)


def test_rejects_missing_invalid_transition(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/03-learning-lifecycle-and-state-machine.yaml"
    rewrite_yaml(path, lambda doc: doc["learning_lifecycle_and_state_machine"]["invalid_transitions"].clear())
    assert "invalid lifecycle transition missing" in diagnostics(root)


def test_rejects_global_learning_injection(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/05-selective-retrieval-requirements.yaml"
    rewrite_yaml(path, lambda doc: doc["selective_retrieval_requirements"]["authority_boundary"].update(global_injection_of_all_learning="ALLOWED"))
    assert "global learning injection prohibition missing" in diagnostics(root)


def test_rejects_metric_coverage_shrink(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/06-effectiveness-and-burden-metrics.yaml"
    rewrite_yaml(path, lambda doc: doc["effectiveness_and_burden_metrics"]["metrics"].pop())
    assert "effectiveness and burden metric coverage mismatch" in diagnostics(root)


def test_rejects_hidden_reasoning_capture(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/07-privacy-retention-and-rollback-requirements.yaml"
    rewrite_yaml(path, lambda doc: doc["privacy_retention_and_rollback_requirements"]["authority_boundary"].update(hidden_chain_of_thought_capture="REQUIRED"))
    assert "privacy authority or hidden-reasoning boundary mismatch" in diagnostics(root)


def test_rejects_premature_solution_selection(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/08-tooling-neutral-capability-model.yaml"
    rewrite_yaml(path, lambda doc: doc["tooling_neutral_capability_model"]["present_disposition"].update(selected_solution="SELECTED"))
    assert "premature tooling selection or PASS-04 authority" in diagnostics(root)


def test_rejects_review_package_hash_drift(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "review-package/manifest.yaml"
    rewrite_yaml(path, lambda doc: doc["review_package"].update(package_sha256="0" * 64))
    assert "adversarial review package aggregate hash mismatch" in diagnostics(root)
