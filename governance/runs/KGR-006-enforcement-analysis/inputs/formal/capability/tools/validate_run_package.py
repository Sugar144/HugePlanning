#!/usr/bin/env python3
"""Validate formal governance packages with explicit stage semantics."""

from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
import tempfile
import sys
from typing import Any

from _lib import __version__
from _lib.canonical import compact_json, sha256_bytes, sha256_file
from _lib.diagnostics import Diagnostic, ordered
from _lib.safe_zip import inspect, normalize_member
from _lib.schemas import load_schema, validate as schema_validate
from _lib.strict_yaml import StrictYAMLError, load, load_bytes


ADVERSARY_OUTPUTS = [
    "00-targeted-closure-basis.md", "01-finding-closure-verdicts.yaml",
    "02-targeted-adversarial-scenarios.md", "03-regression-and-new-findings.md",
    "04-markdown-yaml-parity-review.md", "05-residual-risk-and-routing.md",
    "06-closure-result.yaml", "07-targeted-closure-summary-and-handoff.md",
]
ROLE_PROFILE = {
    "adversary": ("Kernel Adversary", "TARGETED_CLOSURE", "GOV-PROTOCOL-002", "0.1.0"),
    "designer": ("Kernel Designer", "CLOSURE_REMEDIATION", "GOV-PROTOCOL-003", "0.1.0"),
    "enforcement": ("Enforcement Engineer", "MINIMUM_ENFORCEMENT_ANALYSIS", "GOV-PROTOCOL-004", "0.1.0"),
}


def _diag(diags: list[Diagnostic], condition: bool, code: str, path: str, message: str) -> None:
    if not condition:
        diags.append(Diagnostic(code, path, message))


def _envelope_root(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict): return {}
    root = value.get("input_envelope", value.get("run_envelope", value))
    return root if isinstance(root, dict) else {}


def _artifact_entries(envelope: dict[str, Any]) -> list[dict[str, Any]]:
    result = []
    for key in ("current_proposal", "original_review", "predecessor_kernel", "formal_inputs"):
        section = envelope.get(key, {})
        if isinstance(section, dict):
            result.extend(x for x in section.get("artifacts", []) if isinstance(x, dict))
    loop = envelope.get("loop_control")
    if isinstance(loop, dict): result.append(loop)
    return result


def _read_directory(path: Path) -> tuple[dict[str, bytes], list[Diagnostic]]:
    members: dict[str, bytes] = {}
    diags: list[Diagnostic] = []
    if not path.is_dir():
        return {}, [Diagnostic("PACKAGE_UNREADABLE", "$", f"not a ZIP or directory: {path}")]
    for item in sorted(path.rglob("*")):
        if item.is_symlink() or (item.exists() and not item.is_file() and not item.is_dir()):
            diags.append(Diagnostic("PACKAGE_UNSAFE_FILE_TYPE", "$", str(item)))
            continue
        if item.is_dir(): continue
        name = item.relative_to(path).as_posix()
        try: normalize_member(name)
        except ValueError as exc:
            diags.append(Diagnostic("PACKAGE_UNSAFE_PATH", "$", f"{name}: {exc}")); continue
        try: members[name] = item.read_bytes()
        except OSError as exc: diags.append(Diagnostic("PACKAGE_MEMBER_UNREADABLE", name, str(exc)))
    return members, ordered(diags)


def _read_package(path: Path) -> tuple[dict[str, bytes], list[Diagnostic]]:
    return _read_directory(path) if path.is_dir() else inspect(path)


def _expected_input_members(envelope: dict[str, Any]) -> list[str]:
    result = [x.get("package_member") for x in _artifact_entries(envelope)]
    result.append(envelope.get("envelope_package_member", "input-envelope.yaml"))
    return sorted(x for x in result if isinstance(x, str))


def _validate_structured(members: dict[str, bytes], role: str, stage: str, root: Path, diags: list[Diagnostic]) -> None:
    for name, data in sorted(members.items()):
        if name.endswith((".yaml", ".yml")):
            try: load_bytes(data, name)
            except StrictYAMLError as exc: diags.append(Diagnostic("STRUCTURED_FILE_INVALID", name, str(exc)))
    if stage not in ("output", "import") or role != "adversary": return
    verdict_name = next((x for x in members if PurePosixPath(x).name == "01-finding-closure-verdicts.yaml"), None)
    result_name = next((x for x in members if PurePosixPath(x).name == "06-closure-result.yaml"), None)
    if verdict_name:
        try:
            value = load_bytes(members[verdict_name], verdict_name)
            diags.extend(schema_validate(value, load_schema(root / "schemas/protocols/GOV-PROTOCOL-002/0.1.0/finding-closure-verdicts.schema.json"), verdict_name))
        except StrictYAMLError: pass
    if result_name:
        try:
            value = load_bytes(members[result_name], result_name)
            diags.extend(schema_validate(value, load_schema(root / "schemas/protocols/GOV-PROTOCOL-002/0.1.0/closure-result.schema.json"), result_name))
        except StrictYAMLError: pass


def _validate_utf8(members: dict[str, bytes], diags: list[Diagnostic]) -> dict[str, str]:
    decoded: dict[str, str] = {}
    for name, data in sorted(members.items()):
        try:
            decoded[name] = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            diags.append(Diagnostic("PACKAGE_MEMBER_NOT_UTF8", name, str(exc)))
    return decoded


def _markdown_front_matter(name: str, text: str, diags: list[Diagnostic]) -> dict[str, Any]:
    if not text.startswith("---\n") or (boundary := text.find("\n---\n", 4)) < 0:
        diags.append(Diagnostic("MARKDOWN_FRONT_MATTER_INVALID", name, "strict YAML front matter required"))
        return {}
    try:
        value = load_bytes(text[4:boundary].encode("utf-8"), name)
    except StrictYAMLError as exc:
        diags.append(Diagnostic("MARKDOWN_FRONT_MATTER_INVALID", name, str(exc)))
        return {}
    if not isinstance(value, dict):
        diags.append(Diagnostic("MARKDOWN_FRONT_MATTER_INVALID", name, "front matter must be a mapping"))
        return {}
    return value


def _validate_adversary_output_semantics(
    members: dict[str, bytes], decoded: dict[str, str], expected_run: Any, diags: list[Diagnostic]
) -> None:
    try:
        verdict_doc = load_bytes(members["01-finding-closure-verdicts.yaml"], "01-finding-closure-verdicts.yaml")
        result_doc = load_bytes(members["06-closure-result.yaml"], "06-closure-result.yaml")
    except (KeyError, StrictYAMLError):
        return
    verdicts = verdict_doc.get("finding_closure_verdicts", {}) if isinstance(verdict_doc, dict) else {}
    result = result_doc.get("closure_result", {}) if isinstance(result_doc, dict) else {}
    for name, value in (("01-finding-closure-verdicts.yaml", verdicts), ("06-closure-result.yaml", result)):
        _diag(diags, value.get("run") == expected_run, "OUTPUT_RUN_IDENTITY_MISMATCH", name, f"expected run {expected_run}")
        _diag(diags, value.get("protocol") == "GOV-PROTOCOL-002", "OUTPUT_PROTOCOL_IDENTITY_MISMATCH", name, "expected GOV-PROTOCOL-002")
    loop = result.get("loop", {})
    _diag(diags, loop == {"id": "GOV-LOOP-001", "version": "0.1.0"}, "OUTPUT_LOOP_IDENTITY_MISMATCH", "06-closure-result.yaml", "expected GOV-LOOP-001 0.1.0")

    original = verdicts.get("original_findings", [])
    if not isinstance(original, list): original = []
    by_id = {item.get("finding_id"): item for item in original if isinstance(item, dict)}
    expected_ids = {f"KA-F-{number:03d}" for number in range(1, 16)}
    _diag(diags, len(by_id) == len(original) and set(by_id) == expected_ids, "FINDING_INVENTORY_MISMATCH", "01-finding-closure-verdicts.yaml", "expected unique KA-F-001 through KA-F-015")
    categorized = {
        "confirmed_closed": sorted(fid for fid, item in by_id.items() if item.get("adversary_verdict") == "CONFIRMED_CLOSED"),
        "reopened": sorted(fid for fid, item in by_id.items() if item.get("adversary_verdict") == "REOPENED"),
        "routed_confirmed": sorted(fid for fid, item in by_id.items() if item.get("adversary_verdict") == "ROUTED_CONFIRMED"),
        "new": sorted(item.get("finding_id") for item in verdicts.get("new_findings", []) if isinstance(item, dict)),
        "regressions": sorted(item.get("finding_id") for item in verdicts.get("regression_findings", []) if isinstance(item, dict)),
    }
    declared = result.get("findings", {})
    for key, values in categorized.items():
        _diag(diags, sorted(declared.get(key, [])) == values, "RESULT_VERDICT_PARITY_MISMATCH", f"06-closure-result.yaml:$.findings.{key}", "result finding IDs differ from verdict YAML")
    status = result.get("adversary_result", {}).get("status")
    matrix = result.get("decision_matrix", {})
    _diag(diags, matrix.get("selected_result") == status, "RESULT_MATRIX_PARITY_MISMATCH", "06-closure-result.yaml", "selected result differs from adversary result")
    if status == "CLOSURE_CONFIRMED":
        closure_ok = (
            categorized["confirmed_closed"] == sorted(f"KA-F-{number:03d}" for number in range(1, 15))
            and categorized["routed_confirmed"] == ["KA-F-015"]
            and not categorized["reopened"] and not categorized["new"] and not categorized["regressions"]
            and all(not item.get("failed_criteria") and item.get("reopen_event") is None for item in original if isinstance(item, dict))
        )
        _diag(diags, closure_ok, "CLOSURE_CONFIRMED_FACTS_INVALID", "01-finding-closure-verdicts.yaml", "closure requires 14 confirmed, KA-F-015 routed, and zero reopened/new/regression findings")

    front_matter: dict[str, dict[str, Any]] = {}
    for name in ADVERSARY_OUTPUTS:
        if name.endswith(".md") and name in decoded:
            front_matter[name] = _markdown_front_matter(name, decoded[name], diags)
            metadata = front_matter[name]
            _diag(diags, metadata.get("run") == expected_run, "OUTPUT_RUN_IDENTITY_MISMATCH", name, f"expected run {expected_run}")
            if "protocol" in metadata:
                _diag(diags, metadata.get("protocol") == "GOV-PROTOCOL-002", "OUTPUT_PROTOCOL_IDENTITY_MISMATCH", name, "expected GOV-PROTOCOL-002")
    parity = front_matter.get("04-markdown-yaml-parity-review.md", {})
    _diag(diags, parity.get("parity_result") == "PASSED", "MARKDOWN_YAML_PARITY_NOT_PASSED", "04-markdown-yaml-parity-review.md", "parity_result must be PASSED")
    summary = front_matter.get("07-targeted-closure-summary-and-handoff.md", {})
    _diag(diags, summary.get("role") == "Kernel Adversary" and summary.get("mode") == "TARGETED_CLOSURE", "OUTPUT_ROLE_MODE_MISMATCH", "07-targeted-closure-summary-and-handoff.md", "expected Kernel Adversary / TARGETED_CLOSURE")
    _diag(diags, summary.get("declared_adversary_result") == status, "RESULT_MARKDOWN_PARITY_MISMATCH", "07-targeted-closure-summary-and-handoff.md", "summary result differs from result YAML")


def _validate_import_root(members: dict[str, bytes], import_root: Path, diags: list[Diagnostic]) -> None:
    if not import_root.is_dir():
        diags.append(Diagnostic("IMPORT_CUSTODY_MISMATCH", str(import_root), "import root is absent"))
        return
    actual = sorted(item.name for item in import_root.iterdir() if item.is_file() and item.name != "README.md")
    expected = sorted(members)
    for name in sorted(set(expected) - set(actual)):
        diags.append(Diagnostic("IMPORT_CUSTODY_MISMATCH", str(import_root / name), "imported member absent"))
    for name in sorted(set(actual) - set(expected)):
        diags.append(Diagnostic("IMPORT_CUSTODY_EXTRA", str(import_root / name), "undeclared imported output present"))
    for name in sorted(set(actual) & set(expected)):
        candidate = import_root / name
        if candidate.is_symlink() or candidate.read_bytes() != members[name]:
            diags.append(Diagnostic("IMPORT_CUSTODY_MISMATCH", str(candidate), "imported bytes differ from package"))
def validate_package(stage: str, role: str, package_path: Path, envelope_path: Path, prompt: Path | None, loop_snapshot: Path | None, import_root: Path | None = None) -> tuple[dict[str, Any], list[Diagnostic]]:
    diags: list[Diagnostic] = []
    envelope_data = load(envelope_path)
    envelope = _envelope_root(envelope_data)
    members, package_diags = _read_package(package_path)
    diags.extend(package_diags)
    root = Path(__file__).resolve().parents[1]
    expected_role, expected_mode, expected_protocol, expected_version = ROLE_PROFILE[role]
    contract = envelope.get("execution_contract", {})
    declared_role = contract.get("role", envelope.get("target_role"))
    declared_mode = contract.get("mode", envelope.get("target_mode"))
    declared_protocol = contract.get("protocol_id", envelope.get("protocol", {}).get("id"))
    declared_version = contract.get("protocol_version", envelope.get("protocol", {}).get("version"))
    _diag(diags, declared_role == expected_role, "ROLE_IDENTITY_MISMATCH", "$.execution_contract.role", f"expected {expected_role}")
    _diag(diags, declared_mode == expected_mode, "MODE_IDENTITY_MISMATCH", "$.execution_contract.mode", f"expected {expected_mode}")
    _diag(diags, declared_protocol == expected_protocol and declared_version == expected_version, "PROTOCOL_IDENTITY_MISMATCH", "$.execution_contract", f"expected {expected_protocol} {expected_version}")
    run = contract.get("target_run", envelope.get("target_run"))
    _diag(diags, isinstance(run, str) and run.startswith("KGR-"), "RUN_IDENTITY_MISSING", "$.execution_contract.target_run", "target run required")
    if stage in ("preparation", "isolated-input"):
        expected = _expected_input_members(envelope)
    else:
        configured = envelope.get("completed_output_package", {}).get("expected_members") or envelope.get("expected_output_members")
        expected = sorted(configured if isinstance(configured, list) else (ADVERSARY_OUTPUTS if role == "adversary" else []))
        _diag(diags, bool(expected), "OUTPUT_MEMBER_PROFILE_MISSING", "$.expected_output_members", "exact output member profile required")
    actual = sorted(members)
    missing = sorted(set(expected) - set(actual)); extra = sorted(set(actual) - set(expected))
    for name in missing: diags.append(Diagnostic("PACKAGE_MEMBER_MISSING", name, "required member absent"))
    for name in extra: diags.append(Diagnostic("PACKAGE_MEMBER_EXTRA", name, "undeclared member present"))
    envelope_member = envelope.get("envelope_package_member", "input-envelope.yaml")
    if stage in ("preparation", "isolated-input") and envelope_member in members:
        _diag(diags, members[envelope_member] == envelope_path.read_bytes(), "ENVELOPE_CUSTODY_MISMATCH", envelope_member, "package envelope differs from supplied envelope")
    for entry in _artifact_entries(envelope):
        member = entry.get("package_member"); expected_hash = entry.get("sha256")
        if member in members and isinstance(expected_hash, str):
            _diag(diags, sha256_bytes(members[member]) == expected_hash, "PACKAGE_MEMBER_HASH_MISMATCH", member, "member SHA-256 differs from envelope")
        if stage == "preparation":
            for field in ("path", "source_path"):
                value = entry.get(field)
                _diag(diags, isinstance(value, str), "PREPARATION_PATH_MISSING", f"$.{field}", f"{field} required")
                if isinstance(value, str):
                    candidate = root.parent / value
                    _diag(diags, candidate.is_file(), "PREPARATION_PATH_MISSING", value, "repository file absent")
                    if candidate.is_file() and isinstance(expected_hash, str):
                        _diag(diags, sha256_file(candidate) == expected_hash, "PREPARATION_CUSTODY_HASH_MISMATCH", value, "repository custody/provenance hash differs")
        if stage == "import":
            custody = entry.get("import_path")
            if custody:
                candidate = root.parent / custody
                _diag(diags, candidate.is_file(), "IMPORT_CUSTODY_MISMATCH", custody, "import custody file absent")
                if candidate.is_file() and member in members:
                    _diag(diags, candidate.read_bytes() == members[member], "IMPORT_CUSTODY_MISMATCH", custody, "import custody differs from package")
    prompt_hash = contract.get("prompt_sha256")
    if prompt is not None:
        _diag(diags, isinstance(prompt_hash, str) and sha256_file(prompt) == prompt_hash, "PROMPT_ENVELOPE_IDENTITY_MISMATCH", str(prompt), "prompt hash differs from envelope")
    elif stage in ("preparation", "import") and contract.get("prompt_id"):
        diags.append(Diagnostic("PROMPT_SNAPSHOT_REQUIRED", "$.execution_contract.prompt_sha256", "preparation/import requires supplied prompt snapshot"))
    loop_entry = envelope.get("loop_control", {})
    if loop_snapshot is not None:
        _diag(diags, sha256_file(loop_snapshot) == loop_entry.get("sha256"), "LOOP_SNAPSHOT_MISMATCH", str(loop_snapshot), "loop snapshot differs from envelope")
    if loop_entry.get("package_member") in members:
        try:
            loop_data = load_bytes(members[loop_entry["package_member"]], loop_entry["package_member"])
            _diag(diags, loop_data.get("loop", {}).get("id") == "GOV-LOOP-001" and loop_data.get("loop", {}).get("version") == "0.1.0", "LOOP_IDENTITY_MISMATCH", loop_entry["package_member"], "unsupported loop identity")
        except (StrictYAMLError, AttributeError): pass
    _validate_structured(members, role, stage, root, diags)
    decoded = _validate_utf8(members, diags)
    if stage in ("output", "import") and role == "adversary":
        _validate_adversary_output_semantics(members, decoded, run, diags)
    if stage == "import" and import_root is not None:
        _validate_import_root(members, import_root, diags)
    inventory = [{"member": name, "sha256": sha256_bytes(data), "size": len(data)} for name, data in sorted(members.items())]
    valid_classification = "VALIDATED_COMPLETED_OUTPUT_PACKAGE" if stage in ("output", "import") else "VALIDATED_PACKAGE"
    result = {"classification":valid_classification if not diags else "BLOCKED_BY_PACKAGE_CONFLICT" if stage in ("preparation","isolated-input") else "INVALID_OUTPUT_PACKAGE" if stage == "output" else "INVALID_IMPORT", "constitutional_authority":"NONE", "member_count":len(members), "members":inventory, "package_sha256":sha256_file(package_path) if package_path.is_file() else None, "role":role, "run":run, "stage":stage}
    return result, ordered(diags)


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--stage", choices=["preparation","isolated-input","output","import"], required=True)
    p.add_argument("--role", choices=sorted(ROLE_PROFILE), required=True)
    p.add_argument("--package", required=True); p.add_argument("--envelope", required=True)
    p.add_argument("--prompt-snapshot"); p.add_argument("--loop-snapshot"); p.add_argument("--import-root"); p.add_argument("--json", action="store_true")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        with tempfile.TemporaryDirectory(prefix="governance-package-validation-"):
            facts, diagnostics = validate_package(args.stage, args.role, Path(args.package), Path(args.envelope), Path(args.prompt_snapshot) if args.prompt_snapshot else None, Path(args.loop_snapshot) if args.loop_snapshot else None, Path(args.import_root) if args.import_root else None)
        report = {**facts, "diagnostics":[d.as_dict() for d in diagnostics], "result":"VALID" if not diagnostics else "INVALID", "tool":{"name":"validate_run_package.py","version":__version__}}
        print(compact_json(report) if args.json else f"{report['result']}: {len(diagnostics)} diagnostic(s)")
        return 0 if not diagnostics else 1
    except (OSError, StrictYAMLError, ValueError) as exc:
        print(f"operational failure: {exc}", file=sys.stderr); return 2


if __name__ == "__main__": raise SystemExit(main())
