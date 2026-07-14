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


def validate_package(stage: str, role: str, package_path: Path, envelope_path: Path, prompt: Path | None, loop_snapshot: Path | None) -> tuple[dict[str, Any], list[Diagnostic]]:
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
    inventory = [{"member": name, "sha256": sha256_bytes(data), "size": len(data)} for name, data in sorted(members.items())]
    result = {"classification":"VALIDATED_PACKAGE" if not diags else "BLOCKED_BY_PACKAGE_CONFLICT" if stage in ("preparation","isolated-input") else "INVALID_OUTPUT_PACKAGE" if stage == "output" else "INVALID_IMPORT", "constitutional_authority":"NONE", "member_count":len(members), "members":inventory, "package_sha256":sha256_file(package_path) if package_path.is_file() else None, "role":role, "run":run, "stage":stage}
    return result, ordered(diags)


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--stage", choices=["preparation","isolated-input","output","import"], required=True)
    p.add_argument("--role", choices=sorted(ROLE_PROFILE), required=True)
    p.add_argument("--package", required=True); p.add_argument("--envelope", required=True)
    p.add_argument("--prompt-snapshot"); p.add_argument("--loop-snapshot"); p.add_argument("--json", action="store_true")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        with tempfile.TemporaryDirectory(prefix="governance-package-validation-"):
            facts, diagnostics = validate_package(args.stage, args.role, Path(args.package), Path(args.envelope), Path(args.prompt_snapshot) if args.prompt_snapshot else None, Path(args.loop_snapshot) if args.loop_snapshot else None)
        report = {**facts, "diagnostics":[d.as_dict() for d in diagnostics], "result":"VALID" if not diagnostics else "INVALID", "tool":{"name":"validate_run_package.py","version":__version__}}
        print(compact_json(report) if args.json else f"{report['result']}: {len(diagnostics)} diagnostic(s)")
        return 0 if not diagnostics else 1
    except (OSError, StrictYAMLError, ValueError) as exc:
        print(f"operational failure: {exc}", file=sys.stderr); return 2


if __name__ == "__main__": raise SystemExit(main())
