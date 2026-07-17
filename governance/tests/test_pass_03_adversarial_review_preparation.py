from pathlib import Path
import shutil
import yaml

from governance.tools.validate_pass_03_review_preparation import PREP_REL, RESULT_REL, validate

ROOT = Path(__file__).resolve().parents[2]

def isolated(tmp_path: Path) -> Path:
    target = tmp_path / "repository"
    shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns(".agents", ".codex", "__pycache__"))
    return target

def rewrite(path: Path, mutate) -> None:
    data = yaml.safe_load(path.read_text()); mutate(data); path.write_text(yaml.safe_dump(data, sort_keys=False))

def diagnostics(root: Path) -> str:
    return "\n".join(validate(root)["diagnostics"])

def test_valid_independent_review_package() -> None:
    assert validate(ROOT) == {"result": "VALID", "diagnostics": []}

def test_invalid_review_diagnostic_preserves_pass_03_state() -> None:
    result = yaml.safe_load((ROOT / RESULT_REL).read_text())["pass_03_adversarial_review"]
    package = yaml.safe_load((ROOT / PREP_REL / "manifest.yaml").read_text())["review_execution_package"]
    assert result["result"] == "PASS_03_REVIEW_INVALID_OR_INCOMPLETE"
    assert result["r2_required"] is False
    assert package["review_executed"] is False
    assert package["review_opportunity_consumed"] is False

def test_rejects_missing_review_prompt(tmp_path: Path) -> None:
    root = isolated(tmp_path); (root / "governance/prompts/reviews/HP-PROMPT-037-gov-aud-001-pass-03-adversarial-review-v0.1.0.md").unlink()
    assert "instantiated review prompt missing" in diagnostics(root)

def test_rejects_missing_root_instruction_binding(tmp_path: Path) -> None:
    root = isolated(tmp_path); path = root / PREP_REL / "input/input-manifest.yaml"
    rewrite(path, lambda d: d["review_input_manifest"].update(members=[item for item in d["review_input_manifest"]["members"] if item["role"] != "ROOT_REPOSITORY_INSTRUCTIONS"], member_count=11))
    assert "root or project instruction binding missing" in diagnostics(root)

def test_rejects_missing_owner_review_authorization(tmp_path: Path) -> None:
    root = isolated(tmp_path); (root / PREP_REL / "authorization/owner-authorization.yaml").unlink()
    assert "review preparation artifact missing: authorization/owner-authorization.yaml" in diagnostics(root)

def test_rejects_invalid_evidence_package_hash(tmp_path: Path) -> None:
    root = isolated(tmp_path); path = root / PREP_REL / "contract.yaml"
    rewrite(path, lambda d: d["review_execution_contract"]["immutable_evidence_package"].update(package_sha256="0" * 64))
    assert "review contract immutable package" in diagnostics(root)

def test_rejects_missing_independence_basis(tmp_path: Path) -> None:
    root = isolated(tmp_path); path = root / PREP_REL / "contract.yaml"
    rewrite(path, lambda d: d["review_execution_contract"]["reviewer_independence"].pop("permitted_to_proceed"))
    assert "reviewer independence classification" in diagnostics(root)

def test_rejects_nominal_adversarial_evidence(tmp_path: Path) -> None:
    root = isolated(tmp_path); path = root / PREP_REL / "contract.yaml"
    rewrite(path, lambda d: d["review_execution_contract"]["attack_requirements"].update(minimum_meaningful_attacks=0))
    assert "adversarial attack record" in diagnostics(root)

def test_rejects_invalid_result(tmp_path: Path) -> None:
    root = isolated(tmp_path); path = root / PREP_REL / "output-artifact-specification.yaml"
    rewrite(path, lambda d: d["review_output_specification"]["result_rules"].update(permitted=["INVALID"]))
    assert "review output specification" in diagnostics(root)

def test_rejects_premature_pass_04_authority(tmp_path: Path) -> None:
    root = isolated(tmp_path); path = root / PREP_REL / "manifest.yaml"
    rewrite(path, lambda d: d["review_execution_package"]["authority_boundary"].update(PASS_04_authorized_or_executed=True))
    assert "authority boundary" in diagnostics(root)

def test_rejects_premature_pass_03_acceptance(tmp_path: Path) -> None:
    root = isolated(tmp_path); path = root / PREP_REL / "manifest.yaml"
    rewrite(path, lambda d: d["review_execution_package"]["authority_boundary"].update(PASS_03_accepted=True))
    assert "authority boundary" in diagnostics(root)

def test_rejects_invalid_diagnostic_state_advancement(tmp_path: Path) -> None:
    root = isolated(tmp_path); path = root / RESULT_REL
    rewrite(path, lambda d: d["pass_03_adversarial_review"].update(result="PASS_03_CONFIRMED_SUITABLE_FOR_PROJECT_OWNER_DISPOSITION"))
    assert "invalid review diagnostic advanced PASS-03 lifecycle" in diagnostics(root)

def test_rejects_invalid_state_advancement_after_incomplete_review(tmp_path: Path) -> None:
    root = isolated(tmp_path); path = root / PREP_REL / "contract.yaml"
    rewrite(path, lambda d: d["review_execution_contract"]["result_semantics"]["PASS_03_REVIEW_INVALID_OR_INCOMPLETE"].update(pass_03_state_transition="REVIEW_EXECUTED_PENDING_PROJECT_OWNER_DISPOSITION"))
    assert "incomplete-state semantics" in diagnostics(root)
