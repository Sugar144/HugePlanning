from pathlib import Path
import shutil
import yaml

from governance.tools.validate_pass_03_review_preparation import PREP_REL, validate

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

def test_rejects_missing_review_prompt(tmp_path: Path) -> None:
    root = isolated(tmp_path); (root / "governance/prompts/reviews/HP-PROMPT-037-gov-aud-001-pass-03-adversarial-review-v0.1.0.md").unlink()
    assert "instantiated review prompt missing" in diagnostics(root)

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

def test_rejects_invalid_state_advancement_after_incomplete_review(tmp_path: Path) -> None:
    root = isolated(tmp_path); path = root / PREP_REL / "contract.yaml"
    rewrite(path, lambda d: d["review_execution_contract"]["result_semantics"]["PASS_03_REVIEW_INVALID_OR_INCOMPLETE"].update(pass_03_state_transition="REVIEW_EXECUTED_PENDING_PROJECT_OWNER_DISPOSITION"))
    assert "incomplete-state semantics" in diagnostics(root)
