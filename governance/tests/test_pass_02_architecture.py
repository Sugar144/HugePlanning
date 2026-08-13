from __future__ import annotations

from pathlib import Path
import shutil

import yaml

from governance.tools.validate_pass_02 import RUN_REL, validate


ROOT = Path(__file__).resolve().parents[2]


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


def test_canonical_pass_02_candidate_is_valid() -> None:
    assert validate(ROOT) == {"result": "VALID", "diagnostics": []}


def test_rejects_duplicate_bounded_context_identity(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/01-bounded-context-and-ownership-model.yaml"

    def mutate(doc: dict) -> None:
        contexts = doc["bounded_context_model"]["contexts"]
        contexts[1]["context_id"] = contexts[0]["context_id"]

    rewrite_yaml(path, mutate)
    assert "duplicate bounded-context IDs" in diagnostics(root)


def test_rejects_unknown_relationship_endpoint_kind(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/03-typed-relationship-and-query-model.yaml"

    def mutate(doc: dict) -> None:
        doc["relationship_model"]["relationship_types"][0]["target_entity_kinds"].append(
            "UNDECLARED_KIND"
        )

    rewrite_yaml(path, mutate)
    assert "relationship endpoint kind missing" in diagnostics(root)


def test_rejects_orphan_query_traversal(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/03-typed-relationship-and-query-model.yaml"

    def mutate(doc: dict) -> None:
        doc["relationship_model"]["query_contracts"][0]["traversals"].append(
            "UNDECLARED_RELATIONSHIP"
        )

    rewrite_yaml(path, mutate)
    assert "orphan query traversal" in diagnostics(root)


def test_rejects_incomplete_query_coverage(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/03-typed-relationship-and-query-model.yaml"

    def mutate(doc: dict) -> None:
        queries = doc["relationship_model"]["query_contracts"]
        queries.pop()
        doc["relationship_model"]["required_query_count"] = len(queries)

    rewrite_yaml(path, mutate)
    assert "required query coverage mismatch" in diagnostics(root)


def test_rejects_selected_architecture_winner(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/06-architecture-style-comparison.yaml"

    def mutate(doc: dict) -> None:
        comparison = doc["architecture_style_comparison"]
        comparison["selected_option"] = comparison["styles"][0]["style_id"]
        comparison["winner_selected"] = True

    rewrite_yaml(path, mutate)
    assert "architecture winner selected" in diagnostics(root)


def test_rejects_silent_compatibility_matrix_shrink(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/04-version-migration-and-impact-model.md"
    text = path.read_text()
    path.write_text(text.replace("compatibility_combination_count: 77", "compatibility_combination_count: 76", 1))
    assert "compatibility combination count mismatch" in diagnostics(root)


def test_rejects_self_hosting_implementation_claim(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/05-controlled-self-hosting-and-trust-boundaries.md"
    text = path.read_text()
    path.write_text(text.replace("system_self_hosting_status: NOT_IMPLEMENTED", "system_self_hosting_status: IMPLEMENTED", 1))
    assert "system self-hosting status must remain not implemented" in diagnostics(root)


def test_rejects_bound_input_hash_drift(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "input/input-manifest.yaml"

    def mutate(doc: dict) -> None:
        doc["manifest"]["inputs"][0]["sha256"] = "0" * 64

    rewrite_yaml(path, mutate)
    assert "bound input hash mismatch" in diagnostics(root)


def test_allows_pass_03_preparation_authority(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    plan_path = root / "governance/audits/GOV-AUD-001-gov7-enablement/01-audit-plan.yaml"
    status_path = root / "governance/audits/GOV-AUD-001-gov7-enablement/02-audit-status.yaml"

    rewrite_yaml(
        plan_path,
        lambda doc: (
            doc["audit_program"].update(passes_executed=2),
            next(item for item in doc["audit_program"]["sequence"] if item["id"] == "PASS-03").update(
                status="AUTHORIZED_FOR_PREPARATION_NOT_EXECUTION"
            ),
        ),
    )
    rewrite_yaml(
        status_path,
        lambda doc: doc["audit"].update(
            passes_executed=2,
            pass_03_preparation_status="AUTHORIZED_FOR_PREPARATION_NOT_EXECUTION",
            pass_03_execution_authorized=False,
            pass_03_authorization_consumed=False,
            pass_03_executed=False,
            pass_03_status=None,
        ),
    )
    assert validate(root) == {"result": "VALID", "diagnostics": []}


def test_allows_valid_pass_03_successor_execution() -> None:
    assert validate(ROOT) == {"result": "VALID", "diagnostics": []}


def test_rejects_pass_03_execution_authority_without_lifecycle_authority(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    plan = root / "governance/audits/GOV-AUD-001-gov7-enablement/01-audit-plan.yaml"
    status = root / "governance/audits/GOV-AUD-001-gov7-enablement/02-audit-status.yaml"
    rewrite_yaml(plan, lambda doc: (
        doc["audit_program"].update(passes_executed=2),
        next(item for item in doc["audit_program"]["sequence"] if item["id"] == "PASS-03").update(status="PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION"),
    ))
    rewrite_yaml(status, lambda doc: doc["audit"].update(passes_executed=2, pass_03_preparation_status="PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION", pass_03_executed=False))
    assert "PASS-03 execution authority or lifecycle mismatch" in diagnostics(root)


def test_rejects_checkpoint_or_premature_pass_03_execution(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / "governance/audits/GOV-AUD-001-gov7-enablement/01-audit-plan.yaml"

    def mutate(doc: dict) -> None:
        sequence = {item["id"]: item for item in doc["audit_program"]["sequence"]}
        sequence["CHECKPOINT-A"]["status"] = "COMPLETED"
        sequence["PASS-03"]["status"] = "EXECUTED"

    rewrite_yaml(path, mutate)
    diagnostic_text = diagnostics(root)
    assert "CHECKPOINT-A completed or changed" in diagnostic_text
    assert "PASS-03 executed or authorized without a valid later lifecycle" in diagnostic_text
