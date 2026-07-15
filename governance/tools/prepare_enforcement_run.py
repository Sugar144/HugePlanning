#!/usr/bin/env python3
"""Build and validate the bounded KGR-006 preparation and future output contract."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import sys
import zipfile

import jsonschema

from _lib.strict_yaml import load, loads, StrictYAMLError

FIXED_TIME = (1980, 1, 1, 0, 0, 0)
RUN = "KGR-006"
OUTPUTS = [
    "00-enforcement-analysis-basis.md", "01-clause-implication-matrix.yaml",
    "02-existing-capability-inventory.md", "03-feasibility-coverage-and-gap-assessment.md",
    "04-owner-decisions-and-residual-risks.md", "05-minimum-executable-package-recommendation.md",
    "06-ratification-decision-handoff.md",
]
CLAUSES = [f"K-{n:03d}" for n in range(1, 8)]
ROUTES = [f"LLR-{n:03d}" for n in range(1, 21)]
FORBIDDEN = ["RATIFIED", "ENFORCEABLE", "IMPLEMENTED", "OPERATIONAL", "MATURE", "COMPLIANT", "RISK_ACCEPTED"]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def repo_source(root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else root / path


def safe_member(value: str) -> None:
    pure = PurePosixPath(value)
    if pure.is_absolute() or "\\" in value or any(p in ("", ".", "..") for p in pure.parts):
        raise ValueError(f"unsafe member: {value}")


def write_zip(path: Path, members: dict[str, bytes]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(members.items()):
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)


def build(root: Path, inventory_path: Path, package: Path) -> dict:
    config = load(inventory_path)["input_inventory"]
    if config["run"] != RUN:
        raise ValueError("run mismatch")
    run_root = root / "governance/runs/KGR-006-enforcement-analysis"
    snapshot_root = run_root / "inputs/formal"
    if snapshot_root.exists():
        shutil.rmtree(snapshot_root)
    members: dict[str, bytes] = {}
    entries = []
    seen = set()
    for item in config["entries"]:
        member = item["member"]
        safe_member(member)
        if member in seen:
            raise ValueError(f"duplicate member: {member}")
        seen.add(member)
        source = repo_source(root, item["source"])
        data = source.read_bytes()
        snapshot = snapshot_root / member
        if item.get("repository_snapshot", True):
            snapshot.parent.mkdir(parents=True, exist_ok=True)
            snapshot.write_bytes(data)
            custody_path = snapshot.relative_to(root).as_posix()
        else:
            custody_path = str(source)
        members[member] = data
        entries.append({"group": item["group"], "package_member": member, "path": custody_path, "source_path": custody_path, "origin": item["source"], "sha256": sha(data), "size": len(data)})
    prompt = run_root / "prompt/06-enforcement-engineer-minimum-analysis-prompt-v0.1.0.md"
    envelope = {
        "input_envelope": {
            "schema_version": "0.1.0", "id": "GOV-INPUT-003", "target_run": RUN,
            "status": "PREPARED_NOT_EXECUTED", "baseline_head": config["baseline_head"],
            "envelope_package_member": "input-envelope.yaml",
            "execution_contract": {"target_run": RUN, "role": "Enforcement Engineer", "mode": "MINIMUM_ENFORCEMENT_ANALYSIS", "protocol_id": "GOV-PROTOCOL-004", "protocol_version": "0.1.0", "prompt_id": "GOV-PROMPT-008", "prompt_version": "0.1.0", "prompt_sha256": sha(prompt.read_bytes())},
            "formal_inputs": {"artifact_count": len(entries), "artifacts": entries},
            "expected_output_members": OUTPUTS,
            "authority": {"kernel_status": "PROPOSED_NOT_RATIFIED", "gov_5_execution": "NOT_STARTED", "enforcement_engineering_gate": "CLOSED", "human_ratification": "NOT_STARTED"},
        }
    }
    import yaml
    raw = yaml.safe_dump(envelope, sort_keys=False, allow_unicode=True).encode()
    envelope_path = run_root / "input-envelope.yaml"
    envelope_path.write_bytes(raw)
    members["input-envelope.yaml"] = raw
    write_zip(package, members)
    return {"result": "BUILT", "package": str(package), "package_sha256": sha(package.read_bytes()), "member_count": len(members), "input_artifact_count": len(entries)}


def strict_front(text: str, name: str) -> tuple[dict, str]:
    if not text.startswith("---\n") or (end := text.find("\n---\n", 4)) < 0:
        raise ValueError(f"{name}: strict YAML front matter required")
    return loads(text[4:end], name), text[end + 5:]


def validate_preparation(root: Path, package: Path) -> dict:
    run_root = root / "governance/runs/KGR-006-enforcement-analysis"
    envelope = load(run_root / "input-envelope.yaml")["input_envelope"]
    contract = load(run_root / "output-contract.yaml")
    schema = json.loads((root / "governance/schemas/protocols/GOV-PROTOCOL-004/0.1.0/enforcement-analysis-output-contract.schema.json").read_text())
    jsonschema.Draft202012Validator(schema).validate(contract)
    errors = []
    with zipfile.ZipFile(package) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate package member")
        expected = sorted([x["package_member"] for x in envelope["formal_inputs"]["artifacts"]] + ["input-envelope.yaml"])
        if sorted(names) != expected:
            errors.append("exact input inventory mismatch")
        for item in envelope["formal_inputs"]["artifacts"]:
            data = archive.read(item["package_member"])
            custody = Path(item["path"])
            custody = custody if custody.is_absolute() else root / custody
            if sha(data) != item["sha256"] or data != custody.read_bytes():
                errors.append(f"hash/custody mismatch: {item['package_member']}")
        if archive.read("input-envelope.yaml") != (run_root / "input-envelope.yaml").read_bytes():
            errors.append("envelope mismatch")
    if envelope["execution_contract"] != {"target_run": RUN, "role": "Enforcement Engineer", "mode": "MINIMUM_ENFORCEMENT_ANALYSIS", "protocol_id": "GOV-PROTOCOL-004", "protocol_version": "0.1.0", "prompt_id": "GOV-PROMPT-008", "prompt_version": "0.1.0", "prompt_sha256": sha((run_root / "prompt/06-enforcement-engineer-minimum-analysis-prompt-v0.1.0.md").read_bytes())}:
        errors.append("execution contract identity mismatch")
    route_doc = load(run_root / "control/lower-layer-routing-index.yaml")["routing_index"]
    ids = [x["id"] for x in route_doc["entries"]]
    if ids != ROUTES:
        errors.append("canonical routing index must be LLR-001 through LLR-020")
    disposition = route_doc["gov_5_disposition"].get("LLR-020", {})
    if disposition.get("applicability") != "NOT_APPLICABLE_TO_GOV_5_EXECUTION" or disposition.get("later_phase_destination") != "GOV-8" or not disposition.get("reason"):
        errors.append("LLR-020 disposition invalid")
    actual_outputs = sorted(p.name for p in (run_root / "outputs").iterdir() if p.is_file() and p.name != "README.md")
    if actual_outputs:
        errors.append("formal outputs present before execution")
    return {"result": "VALID" if not errors else "INVALID", "diagnostics": errors, "package_sha256": sha(package.read_bytes()), "member_count": len(envelope["formal_inputs"]["artifacts"]) + 1, "run": RUN, "execution_status": "NOT_STARTED", "readiness": "READY_FOR_EXPLICIT_FORMAL_EXECUTION_AUTHORIZATION" if not errors else "NOT_READY"}


def validate_output(root: Path, output_dir: Path) -> dict:
    names = sorted(p.name for p in output_dir.iterdir() if p.is_file() and p.name != "README.md")
    errors = []
    if names != sorted(OUTPUTS):
        errors.append("exact seven-output inventory mismatch")
        return {"result": "INVALID", "diagnostics": errors}
    matrix = load(output_dir / "01-clause-implication-matrix.yaml")
    schema = json.loads((root / "governance/schemas/protocols/GOV-PROTOCOL-004/0.1.0/clause-implication-matrix.schema.json").read_text())
    try:
        jsonschema.Draft202012Validator(schema).validate(matrix)
    except jsonschema.ValidationError as exc:
        errors.append(f"matrix schema: {exc.message}")
    analysis = matrix.get("enforcement_analysis", {})
    if [x.get("clause_id") for x in analysis.get("clauses", [])] != CLAUSES:
        errors.append("exact clause order/coverage mismatch")
    coverage = analysis.get("routing_coverage", [])
    if [x.get("route_id") for x in coverage] != ROUTES:
        errors.append("exact routing order/coverage mismatch")
    for item in coverage:
        if item.get("applicability") == "NOT_APPLICABLE_TO_GOV_5_EXECUTION" and (not item.get("justification") or not item.get("later_phase_destination")):
            errors.append(f"not-applicable route incomplete: {item.get('route_id')}")
    llr20 = next((x for x in coverage if x.get("route_id") == "LLR-020"), {})
    if llr20.get("applicability") != "NOT_APPLICABLE_TO_GOV_5_EXECUTION" or llr20.get("later_phase_destination") != "GOV-8":
        errors.append("LLR-020 output disposition mismatch")
    contract = load(root / "governance/runs/KGR-006-enforcement-analysis/output-contract.yaml")["output_contract"]
    for item in contract["outputs"]:
        if item["format"] != "MARKDOWN":
            continue
        meta, body = strict_front((output_dir / item["filename"]).read_text(), item["filename"])
        if meta.get("run") != RUN or meta.get("status") != "ANALYSIS_COMPLETE_PENDING_INDEPENDENT_EVALUATION":
            errors.append(f"Markdown identity/status mismatch: {item['filename']}")
        for heading in item["required_headings"]:
            if f"## {heading}" not in body:
                errors.append(f"missing heading {heading}: {item['filename']}")
        upper = body.upper()
        for claim in FORBIDDEN:
            if f"STATUS: {claim}" in upper or f"IS {claim}" in upper:
                errors.append(f"forbidden status claim {claim}: {item['filename']}")
    return {"result": "VALID" if not errors else "INVALID", "diagnostics": errors, "output_count": len(names)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build", "validate-preparation", "validate-output"])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--inventory", type=Path, default=Path("governance/runs/KGR-006-enforcement-analysis/input-inventory.yaml"))
    parser.add_argument("--package", type=Path, default=Path("/tmp/HugePlanning-KGR-006-formal-input-package.zip"))
    parser.add_argument("--output-dir", type=Path, default=Path("governance/runs/KGR-006-enforcement-analysis/outputs"))
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "build": result = build(root, root / args.inventory, args.package)
        elif args.command == "validate-preparation": result = validate_preparation(root, args.package)
        else: result = validate_output(root, root / args.output_dir)
    except (OSError, ValueError, KeyError, StrictYAMLError, jsonschema.ValidationError, zipfile.BadZipFile) as exc:
        result = {"result": "INVALID", "diagnostics": [str(exc)]}
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["result"] in ("VALID", "BUILT") else 1


if __name__ == "__main__":
    raise SystemExit(main())
