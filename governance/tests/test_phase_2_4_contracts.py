from __future__ import annotations

from pathlib import Path
import sys
import zipfile

import yaml


ROOT = Path(__file__).resolve().parents[2]
GOV = ROOT / "governance"
TOOLS = GOV / "tools"
sys.path.insert(0, str(TOOLS))

from _lib.strict_yaml import load_bytes
from apply_loop_transition import replay, run_directory
from validate_run_package import validate_package


PACKAGE = Path("/home/sugar/Downloads/HugePlanning-KGR-005-targeted-closure-v0.2-proposed.zip")
ENVELOPE = GOV / "runs/KGR-005-kernel-adversary-targeted-closure/input-envelope.yaml"
PROMPT = GOV / "runs/KGR-005-kernel-adversary-targeted-closure/prompt/05-kernel-adversary-targeted-closure-prompt-sol-high-v0.1.0.md"
LOOP = GOV / "runs/KGR-005-kernel-adversary-targeted-closure/control/kernel-design-closure-loop-v0.1.0.yaml"
SKILL = GOV / "skills/governance-result-importer"


def package_entries() -> dict[str, bytes]:
    with zipfile.ZipFile(PACKAGE) as archive:
        return {item.filename: archive.read(item) for item in archive.infolist()}


def write_zip(path: Path, entries: dict[str, bytes]) -> Path:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in entries.items():
            archive.writestr(name, data)
    return path


def validate(path: Path, stage: str = "output", import_root: Path | None = None):
    return validate_package(stage, "adversary", path, ENVELOPE, PROMPT, LOOP, import_root)


def test_skill_structure_and_bounded_contract() -> None:
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    boundary = text.find("\n---\n", 4)
    metadata = yaml.safe_load(text[4:boundary])
    assert set(metadata) == {"name", "description"}
    assert metadata["name"] == "governance-result-importer"
    interface = yaml.safe_load((SKILL / "agents/openai.yaml").read_text(encoding="utf-8"))["interface"]
    assert set(interface) == {"display_name", "short_description", "default_prompt"}
    assert "$governance-result-importer" in interface["default_prompt"]
    for required in ("--stage output", "--import-root", "apply_loop_transition.py", "Never apply more than one transition", "PROPOSED_NOT_RATIFIED"):
        assert required in text


def test_exact_completed_package_has_expected_classification_and_facts() -> None:
    facts, diagnostics = validate(PACKAGE)
    assert diagnostics == []
    assert facts["classification"] == "VALIDATED_COMPLETED_OUTPUT_PACKAGE"
    assert facts["package_sha256"] == "4e8de3b72d0ac9d70b7f13d7a1768d18a1cd57c1af090f5593f3b40e534f198b"
    assert facts["member_count"] == 8
    result = load_bytes(package_entries()["06-closure-result.yaml"])
    assert result["closure_result"]["adversary_result"]["status"] == "CLOSURE_CONFIRMED"


def test_all_member_utf8_validation_covers_markdown(tmp_path: Path) -> None:
    entries = package_entries()
    entries["03-regression-and-new-findings.md"] = b"\xff\xfe"
    _, diagnostics = validate(write_zip(tmp_path / "invalid-utf8.zip", entries))
    assert "PACKAGE_MEMBER_NOT_UTF8" in {item.code for item in diagnostics}


def test_output_identity_and_result_parity_mutations_fail(tmp_path: Path) -> None:
    entries = package_entries()
    result = load_bytes(entries["06-closure-result.yaml"])
    result["closure_result"]["run"] = "KGR-007"
    entries["06-closure-result.yaml"] = yaml.safe_dump(result, sort_keys=False).encode()
    _, diagnostics = validate(write_zip(tmp_path / "wrong-run.zip", entries))
    assert "OUTPUT_RUN_IDENTITY_MISMATCH" in {item.code for item in diagnostics}

    entries = package_entries()
    result = load_bytes(entries["06-closure-result.yaml"])
    result["closure_result"]["findings"]["confirmed_closed"].pop()
    entries["06-closure-result.yaml"] = yaml.safe_dump(result, sort_keys=False).encode()
    _, diagnostics = validate(write_zip(tmp_path / "parity.zip", entries))
    assert "RESULT_VERDICT_PARITY_MISMATCH" in {item.code for item in diagnostics}


def test_import_root_requires_byte_identical_exact_formal_set(tmp_path: Path) -> None:
    entries = package_entries()
    custody = tmp_path / "outputs"
    custody.mkdir()
    for name, data in entries.items():
        (custody / name).write_bytes(data)
    (custody / "README.md").write_text("historical placeholder\n", encoding="utf-8")
    facts, diagnostics = validate(PACKAGE, "import", custody)
    assert diagnostics == []
    assert facts["classification"] == "VALIDATED_COMPLETED_OUTPUT_PACKAGE"
    (custody / "00-targeted-closure-basis.md").write_bytes(b"changed")
    _, diagnostics = validate(PACKAGE, "import", custody)
    assert "IMPORT_CUSTODY_MISMATCH" in {item.code for item in diagnostics}


def test_markdown_parity_declaration_must_pass(tmp_path: Path) -> None:
    entries = package_entries()
    entries["04-markdown-yaml-parity-review.md"] = entries["04-markdown-yaml-parity-review.md"].replace(b"parity_result: PASSED", b"parity_result: FAILED", 1)
    _, diagnostics = validate(write_zip(tmp_path / "parity-failed.zip", entries))
    assert "MARKDOWN_YAML_PARITY_NOT_PASSED" in {item.code for item in diagnostics}


def test_controller_resolves_canonical_suffixed_run_directory(tmp_path: Path) -> None:
    canonical = tmp_path / "KGR-005-kernel-adversary-targeted-closure"
    canonical.mkdir()
    assert run_directory(tmp_path, "KGR-005") == canonical
    assert run_directory(tmp_path, "KGR-006") == tmp_path / "KGR-006"


def test_replay_accepts_supported_active_state_evidence_bridge() -> None:
    record = yaml.safe_load((GOV / "runs/KGR-005-kernel-adversary-targeted-closure/controller/controller-transition.json").read_text())
    state, counters, accepted, diagnostics = replay([record])
    assert diagnostics == []
    assert state == "CLOSURE_CONFIRMED"
    assert counters == {"completed_targeted_closure_runs": 1, "completed_designer_remediation_runs": 0}
    assert accepted == [record]
    record["previous_state"] = "UNRELATED_STATE"
    assert "HISTORY_FORK" in {item.code for item in replay([record])[3]}


def test_phase_2_4_registry_and_durable_state_are_consistent() -> None:
    registry = yaml.safe_load((GOV / "ARTIFACT_REGISTRY.yaml").read_text(encoding="utf-8"))
    artifacts = {item["id"]: item for item in registry["artifacts"]}
    assert len(artifacts) == len(registry["artifacts"])
    for artifact_id in ("GOV-PKG-007", "GOV-SKILL-004", "GOV-VAL-002", "GOV-REVIEW-007", "KGR-005"):
        assert artifact_id in artifacts
        path = artifacts[artifact_id]["path"].rstrip("/")
        assert (ROOT / path).exists()
    assert artifacts["KGR-005"]["status"] == "COMPLETED"
    assert artifacts["GOV-PKG-007"]["source_sha256"] == "4e8de3b72d0ac9d70b7f13d7a1768d18a1cd57c1af090f5593f3b40e534f198b"
    state = (GOV / "CURRENT_STATE.md").read_text(encoding="utf-8")
    assert "GOV-4 — `COMPLETED`" in state
    assert "PROPOSED_NOT_RATIFIED" in state
    assert "Enforcement Engineering gate | `CLOSED`" in state


def test_dry_run_and_applied_transition_have_identical_calculation() -> None:
    dry = yaml.safe_load((GOV / "runs/KGR-005-kernel-adversary-targeted-closure/controller/controller-dry-run-v0.1.0.json").read_text())["proposed_transition"]
    applied = yaml.safe_load((GOV / "runs/KGR-005-kernel-adversary-targeted-closure/controller/controller-transition.json").read_text())
    assert dry.pop("applied") is False
    assert applied.pop("applied") is True
    assert dry == applied
