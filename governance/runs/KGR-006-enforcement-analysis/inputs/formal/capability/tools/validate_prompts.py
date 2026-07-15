#!/usr/bin/env python3
"""Validate durable material-prompt custody without proving execution."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

from _lib.strict_yaml import StrictYAMLError, loads


STATUSES = {
    "DRAFT", "APPROVED_NOT_EXECUTED", "EXECUTED", "SUPERSEDED",
    "ABORTED", "INVALID_EXECUTION", "NOT_PRESERVED",
}
CATEGORIES = {"ORCHESTRATION", "FORMAL_RUN", "REVIEW", "CORRECTION", "PUBLICATION", "ARCHITECTURE"}
MATERIAL_PROMPT = "MATERIAL_PROMPT"
OWNER_PUBLICATION_AUTHORIZATION = "OWNER_PUBLICATION_AUTHORIZATION"
PROMPT_RE = re.compile(r"^HP-PROMPT-(\d{3})$")
VERSION_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
EXACT_MARKER = "\n## Exact executed text\n\n"
REQUIRED = {
    "prompt_id", "version", "category", "status", "purpose", "target_environment",
    "repository_branch", "repository_base_head", "authorization_scope", "forbidden_actions",
    "exact_text_preserved", "execution_interrupted", "execution_resumed", "result_artifacts",
    "result_commit", "supersedes",
}


class PromptError(ValueError):
    pass


def parse_file(path: Path) -> tuple[dict, str, bytes]:
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise PromptError(f"{path}: unreadable UTF-8: {exc}") from exc
    if not text.startswith("---\n"):
        raise PromptError(f"{path}: YAML front matter is required")
    boundary = text.find("\n---\n", 4)
    if boundary < 0:
        raise PromptError(f"{path}: unterminated YAML front matter")
    try:
        metadata = loads(text[4:boundary], str(path))
    except StrictYAMLError as exc:
        raise PromptError(str(exc)) from exc
    if not isinstance(metadata, dict):
        raise PromptError(f"{path}: front matter must be a mapping")
    return metadata, text[boundary + 5 :], raw


def safe_repo_path(root: Path, value: str, label: str) -> Path:
    pure = PurePosixPath(value)
    if pure.is_absolute() or "\\" in value or any(part in ("", ".", "..") for part in pure.parts):
        raise PromptError(f"{label}: unsafe repository path")
    candidate = (root / Path(*pure.parts)).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise PromptError(f"{label}: repository path escapes root") from exc
    return candidate


def validate_metadata(root: Path, path: Path, metadata: dict, body: str) -> None:
    missing = sorted(REQUIRED - metadata.keys())
    if missing:
        raise PromptError(f"{path}: missing front matter fields: {', '.join(missing)}")
    prompt_id = metadata["prompt_id"]
    version = metadata["version"]
    if not isinstance(prompt_id, str) or not PROMPT_RE.fullmatch(prompt_id):
        raise PromptError(f"{path}: invalid prompt_id")
    if not isinstance(version, str) or not VERSION_RE.fullmatch(version):
        raise PromptError(f"{path}: invalid semantic version")
    if metadata["status"] not in STATUSES:
        raise PromptError(f"{path}: invalid lifecycle status")
    if metadata["category"] not in CATEGORIES:
        raise PromptError(f"{path}: invalid category")
    evidence_type = metadata.get("evidence_type", MATERIAL_PROMPT)
    if evidence_type == OWNER_PUBLICATION_AUTHORIZATION:
        raise PromptError(
            f"{path}: OWNER_PUBLICATION_AUTHORIZATION is publication evidence, not a material prompt custody record"
        )
    if evidence_type != MATERIAL_PROMPT:
        raise PromptError(f"{path}: invalid evidence_type")
    for field in ("authorization_scope", "forbidden_actions", "result_artifacts"):
        if not isinstance(metadata[field], list) or any(not isinstance(item, str) or not item for item in metadata[field]):
            raise PromptError(f"{path}: {field} must be a string list")
    for field in ("exact_text_preserved", "execution_interrupted", "execution_resumed"):
        if not isinstance(metadata[field], bool):
            raise PromptError(f"{path}: {field} must be boolean")
    if metadata["status"] == "EXECUTED" and not metadata["result_artifacts"]:
        raise PromptError(f"{path}: executed prompt requires result references")

    custody = metadata.get("custody", "EXACT_TEXT")
    if custody == "FORMAL_RUN_REFERENCE":
        authoritative = metadata.get("authoritative_prompt_path")
        if not isinstance(authoritative, str) or not authoritative.startswith("governance/runs/") or "/prompt/" not in authoritative:
            raise PromptError(f"{path}: formal run reference requires an authoritative run prompt path")
        if not safe_repo_path(root, authoritative, str(path)).is_file():
            raise PromptError(f"{path}: authoritative formal run prompt is unavailable")
        if metadata["exact_text_preserved"] or EXACT_MARKER in body:
            raise PromptError(f"{path}: formal run reference must not duplicate exact prompt text")
    elif custody != "EXACT_TEXT":
        raise PromptError(f"{path}: invalid custody mode")
    elif metadata["status"] == "NOT_PRESERVED":
        if metadata["exact_text_preserved"] or EXACT_MARKER in body:
            raise PromptError(f"{path}: NOT_PRESERVED cannot claim or contain exact text")
        if not isinstance(metadata.get("evidence_limitation"), str) or not metadata["evidence_limitation"].strip():
            raise PromptError(f"{path}: NOT_PRESERVED requires an evidence limitation")
    else:
        if not metadata["exact_text_preserved"]:
            raise PromptError(f"{path}: preserved prompt must declare exact_text_preserved")
        if EXACT_MARKER not in body:
            raise PromptError(f"{path}: missing exact prompt text")
        exact = body.split(EXACT_MARKER, 1)[1]
        if exact.endswith("\n"):
            exact = exact[:-1]
        if not exact:
            raise PromptError(f"{path}: missing exact prompt text")
        expected = metadata.get("exact_text_sha256")
        if not isinstance(expected, str) or not SHA_RE.fullmatch(expected):
            raise PromptError(f"{path}: exact_text_sha256 is required")
        actual = hashlib.sha256(exact.encode("utf-8")).hexdigest()
        if actual != expected:
            raise PromptError(f"{path}: exact prompt text hash mismatch")


def validate_immutability(root: Path, path: Path, raw: bytes) -> None:
    try:
        relative = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return
    result = subprocess.run(
        ["git", "-C", str(root), "show", f"HEAD:{relative}"],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False,
    )
    if result.returncode != 0:
        return
    try:
        committed, _, _ = parse_bytes(result.stdout, relative)
    except PromptError:
        return
    if committed.get("status") == "EXECUTED" and result.stdout != raw:
        raise PromptError(f"{path}: executed prompt is immutable after commit")


def parse_bytes(raw: bytes, label: str) -> tuple[dict, str, bytes]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise PromptError(f"{label}: unreadable UTF-8") from exc
    if not text.startswith("---\n") or (boundary := text.find("\n---\n", 4)) < 0:
        raise PromptError(f"{label}: invalid front matter")
    try:
        metadata = loads(text[4:boundary], label)
    except StrictYAMLError as exc:
        raise PromptError(str(exc)) from exc
    return metadata, text[boundary + 5 :], raw


def validate(root: Path) -> dict:
    prompt_root = root / "governance/prompts"
    paths = sorted(path for path in prompt_root.rglob("*.md") if path.name != "README.md")
    identities: dict[tuple[str, str], Path] = {}
    lineage_versions: dict[str, set[str]] = {}
    for path in paths:
        metadata, body, raw = parse_file(path)
        validate_metadata(root, path, metadata, body)
        identity = (metadata["prompt_id"], metadata["version"])
        if identity in identities:
            raise PromptError(f"duplicate prompt identity {identity[0]} v{identity[1]}: {identities[identity]} and {path}")
        identities[identity] = path
        lineage_versions.setdefault(metadata["prompt_id"], set()).add(metadata["version"])
        validate_immutability(root, path, raw)
    if not paths:
        raise PromptError("no material prompt custody records found")
    return {"prompts": len(paths), "lineages": len(lineage_versions), "valid": True}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    try:
        result = validate(args.root.resolve())
    except PromptError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
