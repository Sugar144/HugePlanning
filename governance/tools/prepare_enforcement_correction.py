#!/usr/bin/env python3
"""Build and deterministically validate the KGR-006-R1 correction contract."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile
import zipfile

import jsonschema
import yaml

from _lib.strict_yaml import load, loads, StrictYAMLError

FIXED_TIME = (1980, 1, 1, 0, 0, 0)
RUN = "KGR-006-R1"
BASE_RUN = "KGR-006"
RUN_REL = "governance/runs/KGR-006-R1-enforcement-analysis-correction"
OUTPUTS = [
    "00-enforcement-analysis-basis.md",
    "01-clause-implication-matrix.yaml",
    "02-existing-capability-inventory.md",
    "03-feasibility-coverage-and-gap-assessment.md",
    "04-owner-decisions-and-residual-risks.md",
    "05-minimum-executable-package-recommendation.md",
    "06-ratification-decision-handoff.md",
]
EVALUATION_OUTPUTS = [
    "00-independent-evaluation-basis.md",
    "01-independent-evaluation-findings.yaml",
    "02-independent-evaluation-report.md",
]
SOURCE_PACKAGE_SHA256 = "0f496b5b17feb724977f189413f485100b9a66d98b1f79dc05cf45fb60aee66b"
EVALUATION_PACKAGE_SHA256 = "ab133dc6e92b0a51f9911f5dd39bf65f3b2e244f97b023d98ea06a695f5fbe62"
CLAUSES = [f"K-{n:03d}" for n in range(1, 8)]
ROUTES = [f"LLR-{n:03d}" for n in range(1, 21)]
OWNER_DECISIONS = [f"OD-{n:03d}" for n in range(1, 7)]
DEPENDENCIES = {
    "SD-001": "ER-007",
    "SD-002": "ER-012",
    "SD-003": "ER-015",
    "SD-004": "ER-019",
}
ER012_BOUNDARY = (
    "Do not process sensitive, regulated, confidential, or actively harmful "
    "real data until the applicable boundary is established."
)
PACKAGE_HASHES = {
    "packages/HugePlanning-KGR-006-formal-input-package.zip": "d7a92ed0d617bc61d01868e020a4ea9b5237aef6bb8bd569202f0eed2dd6a5d7",
    "packages/HugePlanning-KGR-006-minimum-enforcement-analysis-v0.1.0.zip": "10f41f15cb8d76eb91d625b47f200d114efca746ad6a28b26555e8f5b26de07a",
    "packages/HugePlanning-KGR-006-independent-evaluation-v0.1.0.zip": "1c2167a093ec5d7bf636fe2ab25202e714e5375389ec4464653b0eefd45ed39e",
}
OMITTED_PAIRS = {
    "K-002/LLR-017", "K-003/LLR-017", "K-003/LLR-018",
    "K-004/LLR-011", "K-004/LLR-017", "K-004/LLR-018",
    "K-005/LLR-004", "K-005/LLR-007", "K-005/LLR-008",
    "K-005/LLR-016", "K-005/LLR-017", "K-006/LLR-017",
    "K-007/LLR-001", "K-007/LLR-008", "K-007/LLR-009",
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_path(root: Path, value: str) -> Path:
    candidate = Path(value)
    return candidate if candidate.is_absolute() else root / candidate


def safe_member(value: str) -> None:
    pure = PurePosixPath(value)
    if pure.is_absolute() or "\\" in value or any(p in ("", ".", "..") for p in pure.parts):
        raise ValueError(f"unsafe package member: {value}")


def write_zip(path: Path, members: dict[str, bytes]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(members.items()):
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)


def canonical_pairs(control: dict) -> set[str]:
    return {
        f"{clause}/{route}"
        for route, clauses in control["applicable_pairs"].items()
        for clause in clauses
    }


def build(root: Path, inventory_path: Path, package: Path) -> dict:
    inventory = load(inventory_path)["input_inventory"]
    if inventory["run"] != RUN:
        raise ValueError("input inventory run mismatch")
    run_root = root / RUN_REL
    snapshots = run_root / "inputs/formal"
    if snapshots.exists():
        shutil.rmtree(snapshots)
    members: dict[str, bytes] = {}
    artifacts = []
    for item in inventory["entries"]:
        member = item["member"]
        safe_member(member)
        if member in members:
            raise ValueError(f"duplicate member: {member}")
        origin = source_path(root, item["source"])
        data = origin.read_bytes()
        expected = item.get("expected_sha256")
        if expected and sha(data) != expected:
            raise ValueError(f"authoritative hash mismatch: {member}")
        snapshot = snapshots / member
        snapshot.parent.mkdir(parents=True, exist_ok=True)
        snapshot.write_bytes(data)
        members[member] = data
        artifacts.append({
            "group": item["group"],
            "package_member": member,
            "custody_path": snapshot.relative_to(root).as_posix(),
            "origin": item["source"],
            "sha256": sha(data),
            "size": len(data),
        })
    prompt = run_root / "prompt/07-enforcement-engineer-minimum-analysis-correction-prompt-v0.2.0.md"
    envelope = {
        "input_envelope": {
            "schema_version": "0.2.0",
            "id": "GOV-INPUT-004",
            "target_run": RUN,
            "base_run": BASE_RUN,
            "status": "VALIDATED_PREPARED_NOT_EXECUTED",
            "baseline_head": inventory["baseline_head"],
            "envelope_package_member": "input-envelope.yaml",
            "execution_contract": {
                "target_run": RUN,
                "role": "Enforcement Engineer",
                "mode": "MINIMUM_ENFORCEMENT_ANALYSIS",
                "protocol_id": "GOV-PROTOCOL-004",
                "protocol_version": "0.2.0",
                "prompt_id": "GOV-PROMPT-009",
                "prompt_version": "0.1.0",
                "prompt_sha256": sha(prompt.read_bytes()),
            },
            "correction": {
                "identity_convention": "<BASE_RUN_ID>-R<N>",
                "owner_authorization": "HP-PROMPT-015/0.1.0",
                "base_input_package_sha256": PACKAGE_HASHES["packages/HugePlanning-KGR-006-formal-input-package.zip"],
                "base_output_package_sha256": PACKAGE_HASHES["packages/HugePlanning-KGR-006-minimum-enforcement-analysis-v0.1.0.zip"],
                "evaluation_package_sha256": PACKAGE_HASHES["packages/HugePlanning-KGR-006-independent-evaluation-v0.1.0.zip"],
                "evaluation_result": "RETURN_FOR_VERSIONED_CORRECTION",
                "material_challenges": ["IE-MC-001", "IE-MC-002", "IE-MC-003"],
            },
            "formal_inputs": {"artifact_count": len(artifacts), "artifacts": artifacts},
            "expected_output_members": OUTPUTS,
            "authorization_gate": {
                "required_before_execution": True,
                "record_path": f"{RUN_REL}/authorization/execution-authorization.yaml",
                "current_status": "NOT_AUTHORIZED",
            },
            "independent_evaluation": {
                "required_after_completed_output_validation": True,
                "outside_corrected_engineer_unilateral_control": True,
                "current_status": "NOT_STARTED",
            },
            "authority": {
                "gov_5": "IN_PROGRESS",
                "gov_6_through_gov_9": "INACTIVE",
                "kernel": "PROPOSED_NOT_RATIFIED",
                "risk_accepted": False,
            },
        }
    }
    raw = yaml.safe_dump(envelope, sort_keys=False, allow_unicode=True).encode()
    (run_root / "input-envelope.yaml").write_bytes(raw)
    members["input-envelope.yaml"] = raw
    write_zip(package, members)
    return {
        "result": "BUILT",
        "run": RUN,
        "package": str(package),
        "package_sha256": sha(package.read_bytes()),
        "member_count": len(members),
        "input_artifact_count": len(artifacts),
    }


def strict_front(text: str, name: str) -> tuple[dict, str]:
    if not text.startswith("---\n") or (end := text.find("\n---\n", 4)) < 0:
        raise ValueError(f"{name}: strict YAML front matter required")
    return loads(text[4:end], name), text[end + 5:]


def validate_preparation(root: Path, package: Path) -> dict:
    run_root = root / RUN_REL
    errors: list[str] = []
    manifest = load(run_root / "run-manifest.yaml")
    envelope = load(run_root / "input-envelope.yaml")["input_envelope"]
    contract_doc = load(run_root / "output-contract.yaml")
    schema = json.loads((root / "governance/schemas/protocols/GOV-PROTOCOL-004/0.2.0/enforcement-analysis-correction-output-contract.schema.json").read_text())
    for issue in jsonschema.Draft202012Validator(schema).iter_errors(contract_doc):
        errors.append(f"output contract schema: {issue.message}")
    if not re.fullmatch(r"KGR-[0-9]{3}-R[1-9][0-9]*", RUN):
        errors.append("correction identity does not follow BASE_RUN_ID-RN")
    if manifest["run"].get("base_run") != BASE_RUN or manifest["run"].get("correction_index") != 1:
        errors.append("correction identity/base binding mismatch")
    authorized = manifest["execution"].get("authorized")
    if authorized not in (False, True) or manifest["execution"].get("started") is not False:
        errors.append("correction execution state is invalid")
    if authorized is True:
        authorization = validate_authorization(root, package)
        if authorization["result"] != "VALID":
            errors.extend(f"authorization: {item}" for item in authorization["diagnostics"])
    prompt = run_root / "prompt/07-enforcement-engineer-minimum-analysis-correction-prompt-v0.2.0.md"
    canonical = root / "governance/methodology/roles/enforcement-engineer/protocols/minimum-analysis/07-enforcement-engineer-minimum-analysis-correction-prompt-v0.2.0.md"
    if prompt.read_bytes() != canonical.read_bytes():
        errors.append("run prompt differs from canonical correction protocol")
    control = load(run_root / "control/canonical-clause-route-anchors.yaml")["canonical_clause_route_anchors"]
    pairs = canonical_pairs(control)
    if len(pairs) != 46 or control.get("applicable_pair_count") != 46:
        errors.append("canonical applicable pair count must be 46")
    if set(control.get("evaluation_omissions_requiring_explicit_preservation", [])) != OMITTED_PAIRS:
        errors.append("exact 15 evaluated omissions are not preserved")
    if control.get("llr_020_disposition") != {
        "applicability": "NOT_APPLICABLE_TO_GOV_5_EXECUTION",
        "later_phase_destination": "GOV-8",
        "reason": "GOV-5 analyzes enforcement implications and derived requirements; it does not perform historical S0a-S1 audit or regularization.",
    }:
        errors.append("LLR-020 deferral is not exact")
    findings = load(run_root / "control/correction-findings.yaml")["correction_findings"]
    if [x["id"] for x in findings["findings"]] != ["IE-MC-001", "IE-MC-002", "IE-MC-003"]:
        errors.append("three material challenges are not exact")
    if findings.get("er_012_safe_interim_boundary") != ER012_BOUNDARY:
        errors.append("ER-012 canonical boundary mismatch")
    actual_outputs = sorted(p.name for p in (run_root / "outputs").iterdir() if p.is_file() and p.name != "README.md")
    if actual_outputs:
        errors.append("formal corrected outputs exist before execution")
    try:
        with zipfile.ZipFile(package) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)):
                errors.append("duplicate input package member")
            expected_names = sorted([x["package_member"] for x in envelope["formal_inputs"]["artifacts"]] + ["input-envelope.yaml"])
            if sorted(names) != expected_names:
                errors.append("exact formal input package inventory mismatch")
            for item in envelope["formal_inputs"]["artifacts"]:
                data = archive.read(item["package_member"])
                custody = root / item["custody_path"]
                if data != custody.read_bytes() or sha(data) != item["sha256"]:
                    errors.append(f"package/custody mismatch: {item['package_member']}")
                expected_hash = PACKAGE_HASHES.get(item["package_member"])
                if expected_hash and sha(data) != expected_hash:
                    errors.append(f"authoritative package hash mismatch: {item['package_member']}")
            if archive.read("input-envelope.yaml") != (run_root / "input-envelope.yaml").read_bytes():
                errors.append("input envelope package/custody mismatch")
    except (OSError, zipfile.BadZipFile, KeyError) as exc:
        errors.append(f"formal input package: {exc}")
    return {
        "result": "VALID" if not errors else "INVALID",
        "diagnostics": errors,
        "run": RUN,
        "execution_status": "NOT_STARTED",
        "authorization_status": "AUTHORIZED_FOR_EXACTLY_ONE_EXECUTION" if authorized is True else "NOT_AUTHORIZED",
        "readiness": ("READY_FOR_ONE_AUTHORIZED_EXECUTION" if authorized is True else "READY_FOR_SEPARATE_EXECUTION_AUTHORIZATION") if not errors else "NOT_READY",
        "package_sha256": sha(package.read_bytes()) if package.exists() else None,
        "member_count": len(envelope["formal_inputs"]["artifacts"]) + 1,
    }


def validate_authorization(root: Path, package: Path) -> dict:
    path = root / RUN_REL / "authorization/execution-authorization.yaml"
    errors = []
    if not path.exists():
        errors.append("repository-side execution authorization record is absent")
    else:
        doc = load(path).get("execution_authorization", {})
        expected = {
            "id": "GOV-AUTH-001",
            "status": "AUTHORIZED_NOT_EXECUTED",
            "evidence_class": "CONTEMPORANEOUS_PROJECT_OWNER_EXECUTION_AUTHORIZATION",
            "project_owner_prompt_id": "HP-PROMPT-016/0.1.0",
            "run": RUN,
            "base_run": BASE_RUN,
            "role": "Enforcement Engineer",
            "mode": "MINIMUM_ENFORCEMENT_ANALYSIS",
            "correction_purpose": "Versioned correction of the evaluated KGR-006 outputs.",
            "protocol": "GOV-PROTOCOL-004/0.2.0",
            "formal_input_package_path": "/home/sugar/Documents/HugePlanning-workspace/formal-runs/KGR-006-R1/input/HugePlanning-KGR-006-R1-formal-input-package.zip",
            "formal_input_package_sha256": sha(package.read_bytes()),
            "execution_count_limit": 1,
            "execution_count_consumed": 0,
            "authorized": True,
        }
        for key, value in expected.items():
            if doc.get(key) != value:
                errors.append(f"execution authorization mismatch: {key}")
        if doc.get("required_output_filenames") != OUTPUTS:
            errors.append("execution authorization output inventory mismatch")
        expected_boundaries = {
            "canonical_route_count": 20,
            "explicitly_preserved_evaluated_anchor_count": 15,
            "canonical_specialist_dependency_count": 4,
            "er_012_boundary_count": 1,
            "llr_020_later_phase_destination": "GOV-8",
            "owner_decision_count": 6,
            "minimum_gov_7_package": "RECOMMENDATION_ONLY",
            "new_independent_evaluation_required": True,
        }
        if doc.get("required_correction_boundaries") != expected_boundaries:
            errors.append("execution authorization correction boundaries mismatch")
        state = doc.get("execution_state", {})
        if state != {"started": False, "completed": False, "outputs_created": False, "independent_evaluation_invoked": False}:
            errors.append("execution authorization state must remain not started")
    return {
        "result": "VALID" if not errors else "INVALID",
        "diagnostics": errors,
        "run": RUN,
        "role": "Enforcement Engineer",
        "mode": "MINIMUM_ENFORCEMENT_ANALYSIS",
        "correction_purpose": "Versioned correction of the evaluated KGR-006 outputs.",
        "execution_count_limit": 1,
        "execution_count_consumed": 0,
        "gate": "OPEN_FOR_EXACTLY_ONE_EXECUTION" if not errors else "EXECUTION_AUTHORIZATION",
    }


def validate_output(root: Path, output_dir: Path) -> dict:
    errors: list[str] = []
    names = sorted(p.name for p in output_dir.iterdir() if p.is_file() and p.name != "README.md")
    if names != sorted(OUTPUTS):
        return {"result": "INVALID", "diagnostics": ["exact seven-output inventory mismatch"], "output_count": len(names)}
    matrix = load(output_dir / "01-clause-implication-matrix.yaml")
    schema = json.loads((root / "governance/schemas/protocols/GOV-PROTOCOL-004/0.2.0/corrected-clause-implication-matrix.schema.json").read_text())
    for issue in jsonschema.Draft202012Validator(schema).iter_errors(matrix):
        errors.append(f"matrix schema: {issue.message}")
    analysis = matrix.get("enforcement_analysis", {})
    clauses = analysis.get("clauses", [])
    if [x.get("clause_id") for x in clauses] != CLAUSES:
        errors.append("exact seven-clause order/coverage mismatch")
    coverage = analysis.get("routing_coverage", [])
    if [x.get("route_id") for x in coverage] != ROUTES:
        errors.append("exact 20-route order/coverage mismatch")
    llr20 = next((x for x in coverage if x.get("route_id") == "LLR-020"), {})
    if llr20.get("applicability") != "NOT_APPLICABLE_TO_GOV_5_EXECUTION" or llr20.get("later_phase_destination") != "GOV-8" or not llr20.get("justification"):
        errors.append("LLR-020 must remain justified and deferred to GOV-8")
    actual_pairs = {
        f"{clause.get('clause_id')}/{route}"
        for clause in clauses
        for family in clause.get("effect_families", [])
        for route in family.get("routing_ids", [])
    }
    control = load(root / RUN_REL / "control/canonical-clause-route-anchors.yaml")["canonical_clause_route_anchors"]
    missing = sorted(canonical_pairs(control) - actual_pairs)
    if missing:
        errors.append("missing canonical applicable clause-route pairs: " + ", ".join(missing))
    dependencies = analysis.get("specialist_dependencies", [])
    actual_dependencies = {x.get("id"): x.get("requirement_id") for x in dependencies}
    if actual_dependencies != DEPENDENCIES or len(dependencies) != 4:
        errors.append("exact four canonical specialist dependencies mismatch")
    er12 = next((x for x in dependencies if x.get("requirement_id") == "ER-012"), {})
    if er12.get("safe_interim_boundary") != ER012_BOUNDARY:
        errors.append("ER-012 safe interim boundary mismatch")
    requirements = [item for clause in clauses for item in clause.get("requirements", [])]
    refs = {item.get("specialist_dependency_id"): item.get("id") for item in requirements if item.get("specialist_dependency_id")}
    if refs != DEPENDENCIES:
        errors.append("specialist dependency references must be exact and canonical")
    decisions = analysis.get("owner_decisions", [])
    if [x.get("id") for x in decisions] != OWNER_DECISIONS:
        errors.append("exact six Owner decisions are not preserved")
    if any(x.get("status") != "UNRESOLVED" for x in decisions if x.get("id") in OWNER_DECISIONS[1:]):
        errors.append("OD-002 through OD-006 must remain unresolved")
    if analysis.get("minimum_gov_7_package", {}).get("posture") != "RECOMMENDATION_ONLY":
        errors.append("minimum GOV-7 package must remain recommendation-only")
    contract = load(root / RUN_REL / "output-contract.yaml")["output_contract"]
    for item in contract["outputs"]:
        if item["format"] != "MARKDOWN":
            continue
        meta, body = strict_front((output_dir / item["filename"]).read_text(), item["filename"])
        if meta.get("run") != RUN or meta.get("status") != "CORRECTION_COMPLETE_PENDING_INDEPENDENT_EVALUATION":
            errors.append(f"Markdown identity/status mismatch: {item['filename']}")
        for heading in item["required_headings"]:
            if f"## {heading}" not in body:
                errors.append(f"missing heading {heading}: {item['filename']}")
        if "under a governed pilot" in body.lower():
            errors.append(f"obsolete narrowed ER-012 boundary: {item['filename']}")
    return {"result": "VALID" if not errors else "INVALID", "diagnostics": errors, "output_count": len(names), "canonical_pair_count": len(actual_pairs & canonical_pairs(control))}


def read_exact_archive(path: Path, expected_names: list[str], expected_hash: str) -> tuple[dict[str, bytes], list[str]]:
    errors: list[str] = []
    members: dict[str, bytes] = {}
    if sha(path.read_bytes()) != expected_hash:
        errors.append(f"package SHA-256 mismatch: {path}")
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [item.filename for item in infos]
        if names != expected_names:
            errors.append(f"exact package inventory mismatch: {path}")
        if len(names) != len(set(names)):
            errors.append(f"duplicate package member: {path}")
        for info in infos:
            try:
                safe_member(info.filename)
            except ValueError as exc:
                errors.append(str(exc))
                continue
            mode = info.external_attr >> 16
            if info.is_dir() or (mode and (mode & 0o170000) not in (0, 0o100000)):
                errors.append(f"non-regular package member: {info.filename}")
            if info.flag_bits & 0x1:
                errors.append(f"encrypted package member: {info.filename}")
            data = archive.read(info)
            try:
                data.decode("utf-8")
            except UnicodeDecodeError:
                errors.append(f"non-UTF-8 package member: {info.filename}")
            members[info.filename] = data
    return members, errors


def validate_reconciliation(root: Path, source_package: Path, evaluation_package: Path) -> dict:
    errors: list[str] = []
    source_members, source_errors = read_exact_archive(source_package, OUTPUTS, SOURCE_PACKAGE_SHA256)
    evaluation_members, evaluation_errors = read_exact_archive(
        evaluation_package, EVALUATION_OUTPUTS, EVALUATION_PACKAGE_SHA256
    )
    errors.extend(source_errors)
    errors.extend(evaluation_errors)
    run_root = root / RUN_REL

    if not source_errors:
        with tempfile.TemporaryDirectory(prefix="kgr-006-r1-output-validation-") as name:
            output_dir = Path(name)
            for member, data in source_members.items():
                (output_dir / member).write_bytes(data)
            output_result = validate_output(root, output_dir)
            errors.extend(f"output: {item}" for item in output_result["diagnostics"])

    for member, data in source_members.items():
        custody = run_root / "outputs" / member
        if not custody.is_file() or custody.read_bytes() != data:
            errors.append(f"source import byte mismatch: {member}")
    for member, data in evaluation_members.items():
        custody = run_root / "evaluation" / member
        if not custody.is_file() or custody.read_bytes() != data:
            errors.append(f"evaluation import byte mismatch: {member}")

    if evaluation_members:
        try:
            findings = loads(
                evaluation_members["01-independent-evaluation-findings.yaml"].decode("utf-8"),
                "01-independent-evaluation-findings.yaml",
            )["independent_evaluation"]
            expected = {
                "run": RUN,
                "base_run": BASE_RUN,
                "source_role": "Enforcement Engineer",
                "source_mode": "MINIMUM_ENFORCEMENT_ANALYSIS",
                "source_authorization": "GOV-AUTH-001",
                "source_declared_result": "CORRECTION_COMPLETE_PENDING_INDEPENDENT_EVALUATION",
                "status": "EVALUATION_COMPLETE",
                "declared_result": "SUITABLE_FOR_CONTROLLED_REPOSITORY_IMPORT_AND_PROJECT_OWNER_DECISION_REVIEW",
            }
            for key, value in expected.items():
                if findings.get(key) != value:
                    errors.append(f"evaluation identity mismatch: {key}")
            if findings.get("diagnostics") != [] or findings.get("blockers") != []:
                errors.append("evaluation diagnostics or blockers are not empty")
            owner = findings.get("owner_decisions_assessment", {})
            if owner.get("unresolved_and_reserved") != OWNER_DECISIONS[1:] or owner.get("resolved_by_evaluator") != []:
                errors.append("evaluation Owner-decision reservation mismatch")
            for name in ("00-independent-evaluation-basis.md", "02-independent-evaluation-report.md"):
                meta, _ = strict_front(evaluation_members[name].decode("utf-8"), name)
                if meta.get("run") != RUN or meta.get("status") != "EVALUATION_COMPLETE":
                    errors.append(f"evaluation Markdown identity mismatch: {name}")
        except (KeyError, UnicodeDecodeError, StrictYAMLError, ValueError) as exc:
            errors.append(f"evaluation record invalid: {exc}")

    authorization = load(run_root / "authorization/execution-authorization.yaml").get("execution_authorization", {})
    consumption = authorization.get("consumption_events", [])
    if authorization.get("status") != "CONSUMED":
        errors.append("authorization status must be CONSUMED")
    if authorization.get("execution_count_limit") != 1 or authorization.get("execution_count_consumed") != 1:
        errors.append("authorization execution count must be exactly 1 of 1")
    if authorization.get("execution_available") is not False:
        errors.append("authorization must have no remaining execution")
    if authorization.get("consumed_by_output_package_sha256") != SOURCE_PACKAGE_SHA256:
        errors.append("authorization consumed output package mismatch")
    if len(consumption) != 1 or consumption[0].get("sequence") != 1 or consumption[0].get("output_package_sha256") != SOURCE_PACKAGE_SHA256:
        errors.append("authorization must contain exactly one bound consumption event")
    state = authorization.get("execution_state", {})
    expected_state = {
        "started": True,
        "completed": True,
        "outputs_created": True,
        "independent_evaluation_invoked": True,
        "independent_evaluation_completed": True,
    }
    if state != expected_state:
        errors.append("authorization terminal execution state mismatch")

    return {
        "result": "VALID" if not errors else "INVALID",
        "diagnostics": errors,
        "run": RUN,
        "source_package_sha256": sha(source_package.read_bytes()),
        "evaluation_package_sha256": sha(evaluation_package.read_bytes()),
        "source_member_count": len(source_members),
        "evaluation_member_count": len(evaluation_members),
        "execution_count_limit": authorization.get("execution_count_limit"),
        "execution_count_consumed": authorization.get("execution_count_consumed"),
        "remaining_execution_available": authorization.get("execution_available"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build", "validate-preparation", "validate-authorization", "validate-output", "validate-reconciliation"])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--inventory", type=Path, default=Path(f"{RUN_REL}/input-inventory.yaml"))
    parser.add_argument("--package", type=Path, default=Path("/tmp/HugePlanning-KGR-006-R1-formal-input-package.zip"))
    parser.add_argument("--output-dir", type=Path, default=Path(f"{RUN_REL}/outputs"))
    parser.add_argument("--source-package", type=Path, default=Path("/home/sugar/Documents/HugePlanning-workspace/formal-runs/KGR-006-R1/output/HugePlanning-KGR-006-R1-minimum-enforcement-analysis-correction-v0.1.0.zip"))
    parser.add_argument("--evaluation-package", type=Path, default=Path("/home/sugar/Documents/HugePlanning-workspace/formal-runs/KGR-006-R1/evaluation/HugePlanning-KGR-006-R1-independent-evaluation-v0.1.0.zip"))
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "build":
            result = build(root, root / args.inventory, args.package)
        elif args.command == "validate-preparation":
            result = validate_preparation(root, args.package)
        elif args.command == "validate-authorization":
            result = validate_authorization(root, args.package)
        elif args.command == "validate-output":
            result = validate_output(root, root / args.output_dir)
        else:
            result = validate_reconciliation(root, args.source_package, args.evaluation_package)
    except (OSError, ValueError, KeyError, StrictYAMLError, jsonschema.ValidationError, zipfile.BadZipFile) as exc:
        result = {"result": "INVALID", "diagnostics": [str(exc)]}
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["result"] in ("BUILT", "VALID") else 1


if __name__ == "__main__":
    raise SystemExit(main())
