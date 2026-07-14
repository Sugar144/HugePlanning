#!/usr/bin/env python3
"""Build a bounded, deterministic-order review ZIP without mutating the repository."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import unicodedata
import zipfile

import jsonschema

from _lib.strict_yaml import StrictYAMLError, loads as strict_yaml_loads


SCHEMA_VERSION = "0.1.0"
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)


class BundleError(ValueError):
    """A configuration, repository, scope, validation, or bundle error."""


def run(command: list[str], cwd: Path, *, timeout: int | None = None) -> subprocess.CompletedProcess[bytes]:
    try:
        return subprocess.run(
            command,
            cwd=cwd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise BundleError(f"command failed to execute: {command!r}: {exc}") from exc


def git(root: Path, *args: str, allow: tuple[int, ...] = (0,)) -> bytes:
    result = run(["git", *args], root)
    if result.returncode not in allow:
        detail = result.stdout.decode("utf-8", "replace").strip()
        raise BundleError(f"git {' '.join(args)} failed ({result.returncode}): {detail}")
    return result.stdout


def safe_relative(value: str, label: str) -> str:
    if not isinstance(value, str) or not value or unicodedata.normalize("NFC", value) != value:
        raise BundleError(f"{label}: empty or non-canonical Unicode path")
    if "\\" in value or any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise BundleError(f"{label}: ambiguous or control-character path")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts) or pure.as_posix() != value:
        raise BundleError(f"{label}: unsafe or non-canonical repository path")
    return value


def checked_path(root: Path, value: str, label: str, *, must_exist: bool = False) -> Path:
    relative = safe_relative(value, label)
    candidate = root.joinpath(*PurePosixPath(relative).parts)
    current = root
    for part in PurePosixPath(relative).parts:
        current = current / part
        if current.is_symlink():
            raise BundleError(f"{label}: symbolic links are not allowed: {value}")
    try:
        candidate.resolve(strict=False).relative_to(root.resolve())
    except ValueError as exc:
        raise BundleError(f"{label}: path escapes repository root: {value}") from exc
    if must_exist and not candidate.is_file():
        raise BundleError(f"{label}: regular file does not exist: {value}")
    return candidate


def validate_unique_paths(values: list[str], label: str) -> list[str]:
    normalized = [safe_relative(value, label) for value in values]
    if len(set(normalized)) != len(normalized):
        raise BundleError(f"{label}: duplicate path")
    folded: dict[str, str] = {}
    for value in normalized:
        key = value.casefold()
        if key in folded and folded[key] != value:
            raise BundleError(f"{label}: case-ambiguous paths: {folded[key]!r}, {value!r}")
        folded[key] = value
    return normalized


def load_config(root: Path, path: Path) -> tuple[dict, bytes]:
    try:
        raw = path.read_bytes()
        config = strict_yaml_loads(raw.decode("utf-8"), str(path))
        schema = json.loads((root / "governance/schemas/review-bundle-config.schema.json").read_text())
        jsonschema.Draft202012Validator(schema).validate(config)
    except (OSError, UnicodeDecodeError, StrictYAMLError, json.JSONDecodeError, jsonschema.ValidationError) as exc:
        raise BundleError(f"invalid review-bundle configuration: {exc}") from exc
    config["scope"]["paths"] = validate_unique_paths(config["scope"]["paths"], "scope.paths")
    ids = [item["id"] for group in (config["validations"], config["dependencies"]) for item in group]
    if len(ids) != len(set(ids)):
        raise BundleError("command identifiers must be unique")
    for group_name in ("validations", "dependencies"):
        for item in config[group_name]:
            checked_path(root, item["cwd"], f"{group_name}.{item['id']}.cwd")
    return config, raw


def parse_name_status(raw: bytes) -> list[dict[str, str]]:
    fields = raw.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    records: list[dict[str, str]] = []
    index = 0
    while index < len(fields):
        status = fields[index].decode("ascii", "strict")
        index += 1
        count = 2 if status.startswith(("R", "C")) else 1
        if index + count > len(fields):
            raise BundleError("malformed git name-status output")
        paths = [fields[index + offset].decode("utf-8", "strict") for offset in range(count)]
        index += count
        record = {"status": status, "path": paths[-1]}
        if count == 2:
            record["source_path"] = paths[0]
        records.append(record)
    return records


def inventory(root: Path, base_head: str) -> list[dict[str, str]]:
    records = parse_name_status(git(root, "diff", "--name-status", "-z", "--find-renames", base_head, "--"))
    tracked_paths = {record["path"] for record in records}
    untracked = git(root, "ls-files", "--others", "--exclude-standard", "-z").split(b"\0")
    for raw_path in untracked:
        if not raw_path:
            continue
        path = raw_path.decode("utf-8", "strict")
        if path in tracked_paths:
            raise BundleError(f"ambiguous changed and untracked path: {path}")
        records.append({"status": "??", "path": path})
    all_paths: list[str] = []
    for record in records:
        all_paths.append(record["path"])
        if "source_path" in record:
            all_paths.append(record["source_path"])
    validate_unique_paths(all_paths, "inventory")
    return sorted(records, key=lambda item: (item["path"], item["status"], item.get("source_path", "")))


def inventory_paths(records: list[dict[str, str]]) -> list[str]:
    paths: set[str] = set()
    for record in records:
        paths.add(record["path"])
        if "source_path" in record:
            paths.add(record["source_path"])
    return sorted(paths)


def copy_paths(records: list[dict[str, str]]) -> list[str]:
    return sorted(record["path"] for record in records if not record["status"].startswith("D"))


def unified_diff(root: Path, base_head: str, records: list[dict[str, str]]) -> bytes:
    tracked = [record["path"] for record in records if record["status"] != "??"]
    output = bytearray()
    if tracked:
        output.extend(git(root, "diff", "--binary", "--full-index", base_head, "--", *sorted(tracked)))
    for path in sorted(record["path"] for record in records if record["status"] == "??"):
        result = run(["git", "diff", "--no-index", "--binary", "--full-index", "--", "/dev/null", path], root)
        if result.returncode not in (0, 1):
            raise BundleError(f"failed to create diff for untracked path {path}: {result.returncode}")
        output.extend(result.stdout)
    return bytes(output)


def make_validation_copy(root: Path, records: list[dict[str, str]], temporary: Path) -> Path:
    sandbox = temporary / "validation-repository"
    clone = run(["git", "clone", "--quiet", "--no-hardlinks", str(root), str(sandbox)], temporary)
    if clone.returncode != 0:
        raise BundleError(f"unable to create isolated validation copy: {clone.stdout.decode('utf-8', 'replace')}")
    for record in records:
        target = sandbox.joinpath(*PurePosixPath(record["path"]).parts)
        source = root.joinpath(*PurePosixPath(record["path"]).parts)
        if record["status"].startswith("D"):
            if target.exists():
                target.unlink()
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return sandbox


def execute_commands(sandbox: Path, commands: list[dict]) -> list[dict]:
    evidence: list[dict] = []
    for item in commands:
        cwd = checked_path(sandbox, item["cwd"], f"command {item['id']} cwd")
        started = time.monotonic_ns()
        result = run(item["argv"], cwd, timeout=item["timeout_seconds"])
        duration_ms = (time.monotonic_ns() - started) // 1_000_000
        evidence.append({
            "id": item["id"],
            "argv": item["argv"],
            "cwd": item["cwd"],
            "required": item["required"],
            "exit_code": result.returncode,
            "duration_ms": duration_ms,
            "output": result.stdout.decode("utf-8", "replace"),
        })
    return evidence


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def add_member(members: dict[str, bytes], name: str, content: bytes) -> None:
    safe_relative(name, "bundle member")
    if name in members or name.casefold() in {existing.casefold() for existing in members}:
        raise BundleError(f"duplicate or ambiguous bundle member: {name}")
    members[name] = content


def build(root: Path, config_path: Path, output: Path) -> dict:
    root = root.resolve()
    output = output.resolve()
    try:
        output.relative_to(root)
    except ValueError:
        pass
    else:
        raise BundleError("output ZIP must be outside the repository")
    if output.exists() and not output.is_file():
        raise BundleError("output path exists and is not a regular file")

    config, config_raw = load_config(root, config_path)
    repository = config["repository"]
    top = Path(git(root, "rev-parse", "--show-toplevel").decode().strip()).resolve()
    if top != root:
        raise BundleError(f"repository root mismatch: expected {root}, found {top}")
    branch = git(root, "branch", "--show-current").decode().strip()
    head = git(root, "rev-parse", "HEAD").decode().strip()
    if branch != repository["expected_branch"]:
        raise BundleError(f"branch mismatch: expected {repository['expected_branch']}, found {branch}")
    if head != repository["base_head"]:
        raise BundleError(f"base HEAD mismatch: expected {repository['base_head']}, found {head}")
    git(root, "cat-file", "-e", f"{repository['base_head']}^{{commit}}")
    staged = git(root, "diff", "--cached", "--name-only", "-z")
    if repository["require_empty_staging"] and staged:
        raise BundleError("staging area is not empty")

    records = inventory(root, repository["base_head"])
    actual_paths = inventory_paths(records)
    if repository["require_changes"] and not records:
        raise BundleError("worktree has no changed or untracked files")
    expected_paths = sorted(config["scope"]["paths"])
    if config["scope"]["enforce_exact"] and actual_paths != expected_paths:
        missing = sorted(set(expected_paths) - set(actual_paths))
        unexpected = sorted(set(actual_paths) - set(expected_paths))
        raise BundleError(f"scope mismatch; missing={missing}, unexpected={unexpected}")
    for path in copy_paths(records):
        checked_path(root, path, "changed file", must_exist=True)

    status_before = git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all")
    diff = unified_diff(root, repository["base_head"], records)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="hp-review-bundle.", dir=output.parent) as temporary_name:
        temporary = Path(temporary_name)
        sandbox = make_validation_copy(root, records, temporary)
        validations = execute_commands(sandbox, config["validations"])
        dependencies = execute_commands(sandbox, config["dependencies"])
        failed = [item["id"] for item in validations if item["required"] and item["exit_code"] != 0]
        failed += [item["id"] for item in dependencies if item["required"] and item["exit_code"] != 0]
        status_after = git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all")
        if status_after != status_before:
            raise BundleError("repository state changed while building bundle")
        if failed:
            raise BundleError(f"required commands failed: {', '.join(failed)}")

        prefix = config["bundle"]["root_directory"]
        members: dict[str, bytes] = {}
        add_member(members, f"{prefix}/config.yaml", config_raw)
        add_member(members, f"{prefix}/changes.diff", diff)
        for path in copy_paths(records):
            add_member(members, f"{prefix}/files/{path}", checked_path(root, path, "changed file", must_exist=True).read_bytes())
        repository_evidence = {
            "repository_root_name": root.name,
            "branch": branch,
            "base_head": repository["base_head"],
            "head": head,
            "staging_empty": not bool(staged),
            "worktree_change_count": len(records),
            "status_porcelain_sha256": hashlib.sha256(status_before).hexdigest(),
        }
        scope_evidence = {"inventory": records, "actual_paths": actual_paths, "configured_paths": expected_paths, "exact_match": actual_paths == expected_paths}
        add_member(members, f"{prefix}/evidence/repository-status.json", json_bytes(repository_evidence))
        add_member(members, f"{prefix}/evidence/scope.json", json_bytes(scope_evidence))
        add_member(members, f"{prefix}/evidence/validations.json", json_bytes(validations))
        add_member(members, f"{prefix}/evidence/dependencies.json", json_bytes(dependencies))
        manifest_name = f"{prefix}/SHA256SUMS"
        manifest = "".join(f"{hashlib.sha256(members[name]).hexdigest()}  {name}\n" for name in sorted(members))
        add_member(members, manifest_name, manifest.encode("utf-8"))

        temporary_zip = temporary / "bundle.zip"
        with zipfile.ZipFile(temporary_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for name in sorted(members):
                info = zipfile.ZipInfo(name, FIXED_ZIP_TIME)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = (stat.S_IFREG | 0o644) << 16
                archive.writestr(info, members[name], compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        os.replace(temporary_zip, output)
    return {
        "bundle": str(output),
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "changed_paths": len(actual_paths),
        "validations": len(config["validations"]),
        "dependencies": len(config["dependencies"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    config = args.config if args.config.is_absolute() else root / args.config
    try:
        result = build(root, config.resolve(), args.output)
    except BundleError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
