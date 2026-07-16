from __future__ import annotations

from pathlib import Path
import hashlib
import shutil

import yaml

from governance.tools.validate_audit_methodology import (
    METHOD_REL,
    RUN_REL,
    validate,
    validate_instance,
)


ROOT = Path(__file__).resolve().parents[2]


def isolated(tmp_path: Path) -> Path:
    target = tmp_path / "repository"
    shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns(".agents", ".codex", "__pycache__"))
    return target


def rewrite_method(root: Path, mutate) -> None:
    path = root / METHOD_REL
    value = yaml.safe_load(path.read_text())
    mutate(value["audit_methodology"])
    path.write_text(yaml.safe_dump(value, sort_keys=False))


def diagnostics(root: Path) -> str:
    return "\n".join(validate(root)["diagnostics"])


def write_instance(root: Path, document: dict) -> Path:
    path = root / "methodology-instance.yaml"
    path.write_text(yaml.safe_dump(document, sort_keys=False))
    return path


def pass_07_binding(root: Path) -> dict:
    path = root / "governance/audits/GOV-AUD-001-gov7-enablement/passes/PASS-07/contract.yaml"
    return {
        "contract_id": "GOV-AUD-001-PASS-07-CONTRACT",
        "version": "0.2.0",
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def valid_finding() -> dict:
    return {
        "finding_id": "SYNTHETIC-FINDING-901",
        "statement_and_scope": "A bounded synthetic finding for validator coverage.",
        "finding_basis": ["NORMATIVE_REQUIREMENT"],
        "evidence_refs_or_reasoning": ["governance/AGENTS.md"],
        "support_classification": "VERIFIED_FACT",
        "verified_fact": True,
        "materiality": {
            "classification": "BLOCKING",
            "dimensions": ["AUTHORITY"],
            "analysis": "The synthetic deviation would affect an explicit authority boundary.",
        },
        "disposition_class": "RETURN_FOR_BOUNDED_VERSIONED_CORRECTION",
        "traceability": ["SYNTHETIC-TRACE-901"],
    }


def valid_pass_07_instance(root: Path) -> dict:
    return {
        "methodology_instance": {
            "protocol": "GOV-AUD-001-METHOD-001/0.3.0",
            "findings": [],
            "review": {
                "review_id": "SYNTHETIC-REVIEW-901",
                "review_type": "INDEPENDENT_SUBSTANTIVE_REVIEW",
                "pass_id": "PASS-07",
                "contract_binding": pass_07_binding(root),
                "method_checks_or_attacks_attempted": [
                    {
                        "attempt": "Evaluate the bounded criteria against immutable evidence.",
                        "evidence_or_result": "Evidence was insufficient for a substantive conclusion.",
                    }
                ],
                "findings": [],
                "deviations": [],
                "review_conclusions": ["INSUFFICIENT_EVIDENCE_FOR_SUBSTANTIVE_CONCLUSION"],
                "pass_results": ["INSUFFICIENT_EVIDENCE_FOR_PASS_07_DISPOSITION"],
            },
        }
    }


def test_canonical_audit_methodology_is_valid() -> None:
    assert validate(ROOT) == {"result": "VALID", "diagnostics": []}


def test_rejects_unknown_finding_basis(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    rewrite_method(root, lambda method: method["finding_contract"]["finding_basis"].append("UNREGISTERED_BASIS"))
    assert "finding basis taxonomy mismatch" in diagnostics(root)


def test_rejects_model_inference_presented_as_verified(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    rewrite_method(
        root,
        lambda method: method["finding_contract"]["model_inference_only"].update(
            may_be_represented_as_verified_fact=True
        ),
    )
    assert "MODEL_INFERENCE_ONLY marking or follow-up contract mismatch" in diagnostics(root)


def test_rejects_invalidity_before_root_cause_sequence(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    rewrite_method(
        root,
        lambda method: method["deviation_and_validity_contract"]["required_reasoning_sequence"].reverse(),
    )
    assert "root-cause-before-invalidity sequence mismatch" in diagnostics(root)


def test_rejects_missing_review_type_contract_section(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    rewrite_method(root, lambda method: method["review_contract"]["required_sections"].pop())
    assert "review contract sections mismatch" in diagnostics(root)


def test_rejects_adversarial_confirmation_without_refutation(tmp_path: Path) -> None:
    root = isolated(tmp_path)

    def mutate(method: dict) -> None:
        adversarial = next(
            item for item in method["review_contract"]["review_types"]
            if item["review_type"] == "ADVERSARIAL_REVIEW"
        )
        adversarial["method"] = "CONFIRM_COMPLIANCE"

    rewrite_method(root, mutate)
    assert "adversarial review does not require attempted refutation" in diagnostics(root)


def test_rejects_unbounded_materiality_taxonomy(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    rewrite_method(
        root,
        lambda method: method["materiality"]["blocking_when_materially_affecting_one_or_more"].append(
            "STYLE_PREFERENCE"
        ),
    )
    assert "blocking materiality dimensions mismatch" in diagnostics(root)


def test_rejects_missing_compact_conflict_rule(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    rewrite_method(
        root,
        lambda method: method["temporary_instruction_conflict_control"].update(run_rule="STOP"),
    )
    assert "temporary instruction-conflict control mismatch" in diagnostics(root)


def test_rejects_chat_memory_identity_rule(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    rewrite_method(
        root,
        lambda method: method["canonical_identity_control"].update(rule="Use the next remembered identity."),
    )
    assert "canonical identity-resolution control mismatch" in diagnostics(root)


def test_rejects_modified_immutable_pass_02_r1_evidence(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = root / RUN_REL / "output/07-pass-02-findings-and-checkpoint-a-handoff.md"
    path.write_text(path.read_text() + "\n")
    assert "immutable PASS-02 R1 custody mismatch" in diagnostics(root)


def test_validates_structured_pass_07_insufficient_evidence_instance(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    path = write_instance(root, valid_pass_07_instance(root))
    assert validate_instance(root, path) == {"result": "VALID", "diagnostics": []}


def test_rejects_auxiliary_review_type_as_pass_07_disposition(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    document = valid_pass_07_instance(root)
    review = document["methodology_instance"]["review"]
    review["review_type"] = "DETERMINISTIC_VALIDATION"
    review["review_conclusions"] = ["VALID_AGAINST_DECLARED_MACHINE_CONTRACT"]
    review["pass_results"] = ["SUITABLE_FOR_PROJECT_OWNER_DECISION"]
    path = write_instance(root, document)
    text = "\n".join(validate_instance(root, path)["diagnostics"])
    assert "declared review type cannot produce the pass disposition" in text


def test_rejects_unmapped_pass_07_result(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    document = valid_pass_07_instance(root)
    document["methodology_instance"]["review"]["pass_results"] = ["SUITABLE_FOR_PROJECT_OWNER_DECISION"]
    path = write_instance(root, document)
    assert "review conclusion does not map to the declared pass result" in "\n".join(
        validate_instance(root, path)["diagnostics"]
    )


def test_rejects_adversarial_review_without_actual_attack_attempt(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    document = valid_pass_07_instance(root)
    review = document["methodology_instance"]["review"]
    review["review_type"] = "ADVERSARIAL_REVIEW"
    review["method_checks_or_attacks_attempted"] = []
    review["review_conclusions"] = ["INSUFFICIENT_EVIDENCE_FOR_ADVERSARIAL_CONCLUSION"]
    path = write_instance(root, document)
    assert "adversarial review must record actual attack attempts" in "\n".join(
        validate_instance(root, path)["diagnostics"]
    )


def adversarial_attack() -> dict:
    return {
        "attack_id": "SYNTHETIC-ATTACK-901",
        "attack_dimension": "COUNTEREXAMPLE_CONSTRUCTION",
        "target_claim_or_assumption": "The synthetic contract binding uniquely identifies the reviewed pass contract.",
        "attack_method": "Substitute a conflicting contract identity and compare the resolved binding.",
        "counterexample_or_failure_scenario": "A duplicate contract ID could cause a review to bind an unrelated pass contract.",
        "evidence_examined": ["synthetic contract bytes", "resolved contract hash"],
        "result": "The duplicate binding was rejected by deterministic contract discovery.",
        "impact": "Prevents a false review conclusion from being attached to the wrong contract.",
    }


def test_accepts_genuine_structured_adversarial_attack(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    document = valid_pass_07_instance(root)
    review = document["methodology_instance"]["review"]
    review["review_type"] = "ADVERSARIAL_REVIEW"
    review["method_checks_or_attacks_attempted"] = [adversarial_attack()]
    review["review_conclusions"] = ["SURVIVED_RECORDED_ADVERSARIAL_ATTACKS"]
    review["pass_results"] = ["SUITABLE_FOR_PROJECT_OWNER_DECISION"]
    assert validate_instance(root, write_instance(root, document))["result"] == "VALID"


def test_rejects_nominal_adversarial_attack(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    document = valid_pass_07_instance(root)
    review = document["methodology_instance"]["review"]
    review["review_type"] = "ADVERSARIAL_REVIEW"
    review["method_checks_or_attacks_attempted"] = [{
        "attack_id": "A", "attack_dimension": "COUNTEREXAMPLE_CONSTRUCTION",
        "target_claim_or_assumption": "candidate", "attack_method": "review",
        "counterexample_or_failure_scenario": "none", "evidence_examined": [],
        "result": "survived", "impact": "none",
    }]
    review["review_conclusions"] = ["SURVIVED_RECORDED_ADVERSARIAL_ATTACKS"]
    review["pass_results"] = ["SUITABLE_FOR_PROJECT_OWNER_DECISION"]
    text = "\n".join(validate_instance(root, write_instance(root, document))["diagnostics"])
    assert "adversarial attack lacks a specific target" in text
    assert "adversarial attack lacks evidence examined" in text


def test_discovers_synthetic_non_pass_02_or_pass_07_contract(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    contract = root / "governance/audits/GOV-AUD-001-gov7-enablement/passes/PASS-99/contract.yaml"
    contract.parent.mkdir()
    contract.write_text(yaml.safe_dump({"pass": {
        "id": "PASS-99", "contract_identity": {"contract_id": "SYNTHETIC-PASS-99", "version": "1.0.0"},
        "output_structure": {"format": "SYNTHETIC"},
        "review_contract": {"allowed_review_types": ["INDEPENDENT_SUBSTANTIVE_REVIEW"],
            "allowed_conclusions_by_review_type": {"INDEPENDENT_SUBSTANTIVE_REVIEW": ["INSUFFICIENT_EVIDENCE_FOR_SUBSTANTIVE_CONCLUSION"]},
            "conclusion_to_result": {}},
    }}, sort_keys=False))
    document = valid_pass_07_instance(root)
    review = document["methodology_instance"]["review"]
    review["pass_id"] = "PASS-99"
    review["contract_binding"] = {"contract_id": "SYNTHETIC-PASS-99", "version": "1.0.0", "sha256": hashlib.sha256(contract.read_bytes()).hexdigest()}
    review["pass_results"] = []
    assert validate_instance(root, write_instance(root, document))["result"] == "VALID"


def test_rejects_model_inference_instance_as_verified_fact(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    document = valid_pass_07_instance(root)
    finding = valid_finding()
    finding.update(
        finding_basis=["MODEL_INFERENCE_ONLY"],
        support_classification="MODEL_INFERENCE_ONLY",
        verified_fact=True,
        required_follow_up=["ADVERSARIAL_TESTING"],
    )
    document["methodology_instance"]["findings"] = [finding]
    path = write_instance(root, document)
    assert "MODEL_INFERENCE_ONLY cannot be represented as verified fact" in "\n".join(
        validate_instance(root, path)["diagnostics"]
    )


def test_rejects_invalidity_without_causal_authority_and_materiality_analysis(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    document = valid_pass_07_instance(root)
    review = document["methodology_instance"]["review"]
    review["review_conclusions"] = ["INVALID_EXECUTION_AFTER_ROOT_CAUSE_AND_MATERIALITY_ANALYSIS"]
    review["pass_results"] = ["INVALID_AUDIT_EXECUTION"]
    review["deviations"] = []
    path = write_instance(root, document)
    assert "invalidity conclusion requires causal, authority-impact and materiality analysis" in "\n".join(
        validate_instance(root, path)["diagnostics"]
    )


def test_rejects_multiple_pass_results(tmp_path: Path) -> None:
    root = isolated(tmp_path)
    document = valid_pass_07_instance(root)
    document["methodology_instance"]["review"]["pass_results"] = [
        "INSUFFICIENT_EVIDENCE_FOR_PASS_07_DISPOSITION",
        "RETURN_FOR_BOUNDED_VERSIONED_CORRECTION",
    ]
    path = write_instance(root, document)
    assert "review must declare exactly one pass result" in "\n".join(
        validate_instance(root, path)["diagnostics"]
    )


def test_validator_has_no_incident_specific_finding_ids() -> None:
    source = (ROOT / "governance/tools/validate_audit_methodology.py").read_text()
    assert "GAP-001" not in source
    assert "GOV-AUD-001-P02-F" not in source
