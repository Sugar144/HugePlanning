from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import zipfile

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[2]
GOV = ROOT / "governance"
sys.path.insert(0, str(GOV / "tools"))
from _lib.strict_yaml import load
from prepare_enforcement_correction import (
    CLAUSES,
    DEPENDENCIES,
    ER012_BOUNDARY,
    OMITTED_PAIRS,
    OUTPUTS,
    PACKAGE_HASHES,
    RUN_REL,
    ROUTES,
    build,
    canonical_pairs,
    validate_output,
    validate_reconciliation,
)

RUN = ROOT / RUN_REL


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_correction_identity_methodology_is_prospective_and_immutable():
    text = (GOV / "methodology/project-operating-contract.md").read_text()
    assert "<BASE_RUN_ID>-R<N>" in text
    assert "overwrite\nor replace the base run" in text
    assert "consume the next unrelated sequential run\nidentity" in text
    assert "new independent evaluation" in text


def test_control_preserves_canonical_pairs_and_exact_evaluation_omissions():
    control = load(RUN / "control/canonical-clause-route-anchors.yaml")["canonical_clause_route_anchors"]
    assert len(canonical_pairs(control)) == 46
    assert set(control["evaluation_omissions_requiring_explicit_preservation"]) == OMITTED_PAIRS
    assert control["deferred_pairs"] == {"LLR-020": ["K-004", "K-005"]}
    assert control["llr_020_disposition"]["later_phase_destination"] == "GOV-8"


def test_contract_schema_and_exact_correction_boundaries():
    contract = load(RUN / "output-contract.yaml")
    schema = json.loads((GOV / "schemas/protocols/GOV-PROTOCOL-004/0.2.0/enforcement-analysis-correction-output-contract.schema.json").read_text())
    jsonschema.Draft202012Validator(schema).validate(contract)
    body = contract["output_contract"]
    assert [item["filename"] for item in body["outputs"]] == OUTPUTS
    assert body["specialist_dependencies"]["requirement_ids"] == list(DEPENDENCIES.values())
    assert body["owner_decisions"]["required_ids"] == [f"OD-{n:03d}" for n in range(1, 7)]
    assert body["minimum_gov_7_package"] == "RECOMMENDATION_ONLY"


def test_corrected_matrix_schema_uses_canonical_dependency_references():
    schema = json.loads((GOV / "schemas/protocols/GOV-PROTOCOL-004/0.2.0/corrected-clause-implication-matrix.schema.json").read_text())
    requirement = schema["$defs"]["requirement"]
    assert "specialist_dependency_id" in requirement["required"]
    assert "specialist_dependency" not in requirement["properties"]
    dependencies = schema["properties"]["enforcement_analysis"]["properties"]["specialist_dependencies"]
    assert dependencies["minItems"] == dependencies["maxItems"] == 4


def test_formal_input_package_remains_deterministic_after_execution(tmp_path):
    first = tmp_path / "first.zip"
    second = tmp_path / "second.zip"
    inventory = RUN / "input-inventory.yaml"
    build(ROOT, inventory, first)
    build(ROOT, inventory, second)
    assert first.read_bytes() == second.read_bytes()
    assert digest(first) == "ad59170b931563e42ffbc65cf04b0427b414521d62efe08b0705a810ebac9fd8"
    with zipfile.ZipFile(first) as archive:
        assert len(archive.namelist()) == 14


def test_repository_execution_authorization_is_consumed_once():
    source = Path("/home/sugar/Documents/HugePlanning-workspace/formal-runs/KGR-006-R1/output/HugePlanning-KGR-006-R1-minimum-enforcement-analysis-correction-v0.1.0.zip")
    evaluation = Path("/home/sugar/Documents/HugePlanning-workspace/formal-runs/KGR-006-R1/evaluation/HugePlanning-KGR-006-R1-independent-evaluation-v0.1.0.zip")
    result = validate_reconciliation(ROOT, source, evaluation)
    assert result["result"] == "VALID"
    assert result["diagnostics"] == []
    assert result["execution_count_limit"] == 1
    assert result["execution_count_consumed"] == 1
    assert result["remaining_execution_available"] is False


def test_bound_external_packages_and_imported_originals_remain_exact():
    inventory = load(RUN / "input-inventory.yaml")["input_inventory"]
    package_entries = [item for item in inventory["entries"] if item["member"] in PACKAGE_HASHES]
    assert len(package_entries) == 3
    for item in package_entries:
        assert digest(Path(item["source"])) == PACKAGE_HASHES[item["member"]]
    checks = [
        (
            Path(package_entries[1]["source"]),
            GOV / "runs/KGR-006-enforcement-analysis/outputs",
            7,
        ),
        (
            Path(package_entries[2]["source"]),
            GOV / "runs/KGR-006-enforcement-analysis/evaluation",
            3,
        ),
    ]
    for archive_path, custody, count in checks:
        with zipfile.ZipFile(archive_path) as archive:
            assert len(archive.namelist()) == count
            for name in archive.namelist():
                assert archive.read(name) == (custody / name).read_bytes()


def test_prompt_snapshot_is_exact_and_outputs_are_exactly_imported():
    name = "07-enforcement-engineer-minimum-analysis-correction-prompt-v0.2.0.md"
    assert (RUN / "prompt" / name).read_bytes() == (GOV / "methodology/roles/enforcement-engineer/protocols/minimum-analysis" / name).read_bytes()
    assert sorted(path.name for path in (RUN / "outputs").iterdir() if path.name != "README.md") == sorted(OUTPUTS)


def write_valid_completed_output(output_dir: Path) -> None:
    output_dir.mkdir()
    control = load(RUN / "control/canonical-clause-route-anchors.yaml")["canonical_clause_route_anchors"]
    routes_by_clause = {
        clause: [route for route, anchors in control["applicable_pairs"].items() if clause in anchors]
        for clause in CLAUSES
    }
    requirement_ids = ["ER-001", "ER-007", "ER-012", "ER-015", "ER-019", "ER-020", "ER-002"]
    dep_by_requirement = {requirement: dependency for dependency, requirement in DEPENDENCIES.items()}
    clauses = []
    for clause, requirement in zip(CLAUSES, requirement_ids):
        clauses.append({
            "clause_id": clause,
            "effect_families": [{"name": f"{clause} canonical anchors", "routing_ids": routes_by_clause[clause]}],
            "requirements": [{
                "id": requirement,
                "kind": "DERIVED_REQUIREMENT",
                "statement": "Preserved bounded requirement.",
                "timing": "SHOULD_LATER",
                "lower_layers": ["evidence"],
                "capability_status": "GAP",
                "evidence_refs": ["bound-evidence"],
                "feasibility_limit": "Not implemented.",
                "cost_and_burden": "Not measured.",
                "residual_risk": "Not accepted.",
                "reserved_human_decision": "Project Owner retains the decision.",
                "scope_posture": "CURRENT_SINGLE_USER_MINIMUM",
                "specialist_dependency_id": dep_by_requirement.get(requirement),
            }],
        })
    dependencies = []
    for dependency, requirement in DEPENDENCIES.items():
        boundary = ER012_BOUNDARY if requirement == "ER-012" else "Do not proceed beyond the unsupported boundary."
        dependencies.append({
            "id": dependency,
            "requirement_id": requirement,
            "trigger": "bounded_specialist_trigger",
            "affected_clause": "K-001",
            "affected_effect_or_requirement": requirement,
            "why_general_analysis_is_insufficient": "Specialist evidence is required.",
            "required_specialist_type": "Competent specialist",
            "blocking_or_nonblocking": "NONBLOCKING_WITH_EXPLICIT_UNSUPPORTED_BOUNDARY",
            "safe_interim_boundary": boundary,
            "later_phase_destination": "PRE_RATIFICATION_OWNER_DECISION",
        })
    matrix = {
        "enforcement_analysis": {
            "schema_version": "0.2.0",
            "run": "KGR-006-R1",
            "base_run": "KGR-006",
            "role": "Enforcement Engineer",
            "mode": "MINIMUM_ENFORCEMENT_ANALYSIS",
            "protocol": {"id": "GOV-PROTOCOL-004", "version": "0.2.0"},
            "status": "CORRECTION_COMPLETE_PENDING_INDEPENDENT_EVALUATION",
            "kernel": {"version": "0.2.0-proposed", "status": "PROPOSED_NOT_RATIFIED", "ratified": False, "enforceable": False, "implemented": False, "operational": False},
            "correction": {
                "base_input_package_sha256": "d7a92ed0d617bc61d01868e020a4ea9b5237aef6bb8bd569202f0eed2dd6a5d7",
                "base_output_package_sha256": "10f41f15cb8d76eb91d625b47f200d114efca746ad6a28b26555e8f5b26de07a",
                "evaluation_package_sha256": "1c2167a093ec5d7bf636fe2ab25202e714e5375389ec4464653b0eefd45ed39e",
                "evaluation_result": "RETURN_FOR_VERSIONED_CORRECTION",
                "material_challenges": ["IE-MC-001", "IE-MC-002", "IE-MC-003"],
                "canonical_anchor_source": "KD-R05",
            },
            "clauses": clauses,
            "routing_coverage": [{
                "route_id": route,
                "applicability": "NOT_APPLICABLE_TO_GOV_5_EXECUTION" if route == "LLR-020" else "APPLICABLE_TO_GOV_5_EXECUTION",
                "justification": "Deferred historical regularization." if route == "LLR-020" else "Accounted for in correction.",
                "later_phase_destination": "GOV-8" if route == "LLR-020" else None,
            } for route in ROUTES],
            "capability_summary": {"GAP": 7},
            "specialist_dependencies": dependencies,
            "owner_decisions": [{"id": decision, "status": "SATISFIED_FOR_EVALUATOR_APPOINTMENT" if decision == "OD-001" else "UNRESOLVED"} for decision in [f"OD-{n:03d}" for n in range(1, 7)]],
            "minimum_gov_7_package": {"posture": "RECOMMENDATION_ONLY"},
            "parity": {"markdown_outputs_materially_consistent": True},
        }
    }
    (output_dir / "01-clause-implication-matrix.yaml").write_text(yaml.safe_dump(matrix, sort_keys=False))
    contract = load(RUN / "output-contract.yaml")["output_contract"]
    for item in contract["outputs"]:
        if item["format"] != "MARKDOWN":
            continue
        body = "\n".join(f"## {heading}\n\nBounded correction evidence." for heading in item["required_headings"])
        (output_dir / item["filename"]).write_text(
            "---\nrun: KGR-006-R1\nstatus: CORRECTION_COMPLETE_PENDING_INDEPENDENT_EVALUATION\n---\n\n" + body + "\n"
        )


def test_completed_output_validator_accepts_exact_contract_and_rejects_material_challenges(tmp_path):
    output_dir = tmp_path / "outputs"
    write_valid_completed_output(output_dir)
    assert validate_output(ROOT, output_dir)["result"] == "VALID"

    matrix_path = output_dir / "01-clause-implication-matrix.yaml"
    matrix = load(matrix_path)
    k2 = matrix["enforcement_analysis"]["clauses"][1]
    k2["effect_families"][0]["routing_ids"].remove("LLR-017")
    matrix_path.write_text(yaml.safe_dump(matrix, sort_keys=False))
    missing = validate_output(ROOT, output_dir)
    assert missing["result"] == "INVALID"
    assert any("K-002/LLR-017" in item for item in missing["diagnostics"])

    write_valid_completed_output(output_dir := tmp_path / "outputs-er12")
    matrix_path = output_dir / "01-clause-implication-matrix.yaml"
    matrix = load(matrix_path)
    matrix["enforcement_analysis"]["specialist_dependencies"][1]["safe_interim_boundary"] = "Only block the governed pilot."
    matrix_path.write_text(yaml.safe_dump(matrix, sort_keys=False))
    narrowed = validate_output(ROOT, output_dir)
    assert narrowed["result"] == "INVALID"
    assert "ER-012 safe interim boundary mismatch" in narrowed["diagnostics"]
