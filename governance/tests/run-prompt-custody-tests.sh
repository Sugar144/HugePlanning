#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

python3 - "$REPO_ROOT" <<'PY'
from __future__ import annotations

import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import yaml

repo = Path(sys.argv[1])
temporary = Path(tempfile.mkdtemp(prefix="hp-prompt-tests."))
passed = 0
failed = 0


def check(condition, label, detail=""):
    global passed, failed
    if condition:
        passed += 1
        print(f"PASS: {label}")
    else:
        failed += 1
        print(f"FAIL: {label} {detail}", file=sys.stderr)


def make_root(name):
    root = temporary / name
    (root / "governance/tools/_lib").mkdir(parents=True)
    (root / "governance/prompts/orchestration").mkdir(parents=True)
    shutil.copy2(repo / "governance/tools/validate_prompts.py", root / "governance/tools")
    shutil.copy2(repo / "governance/tools/_lib/strict_yaml.py", root / "governance/tools/_lib")
    (root / "governance/tools/_lib/__init__.py").write_text("")
    return root


def metadata(**changes):
    data = {
        "prompt_id": "HP-PROMPT-001",
        "version": "0.1.0",
        "category": "ORCHESTRATION",
        "status": "EXECUTED",
        "purpose": "Synthetic prompt custody test",
        "target_environment": "offline test",
        "repository_branch": "test",
        "repository_base_head": "0" * 40,
        "authorization_scope": ["temporary fixture"],
        "forbidden_actions": ["external effect"],
        "exact_text_preserved": True,
        "exact_text_sha256": hashlib.sha256(b"hello").hexdigest(),
        "execution_interrupted": False,
        "execution_resumed": False,
        "result_artifacts": ["synthetic result"],
        "result_commit": None,
        "supersedes": None,
    }
    data.update(changes)
    return data


def write_record(root, name="HP-PROMPT-001-v0.1.0.md", data=None, exact="hello"):
    data = data or metadata()
    body = "# Synthetic prompt\n"
    if exact is not None:
        body += f"\n## Exact executed text\n\n{exact}\n"
    target = root / "governance/prompts/orchestration" / name
    target.write_text("---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n\n" + body)
    return target


def run(root):
    return subprocess.run(
        [sys.executable, "governance/tools/validate_prompts.py", "--root", str(root)],
        cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )


try:
    actual = subprocess.run(
        [sys.executable, "governance/tools/validate_prompts.py", "--root", str(repo)],
        cwd=repo, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    check(actual.returncode == 0 and '"prompts":2' in actual.stdout, "1 repository prompt front matter and exact text", actual.stderr)

    duplicate = make_root("duplicate")
    write_record(duplicate)
    write_record(duplicate, "duplicate.md")
    result = run(duplicate)
    check(result.returncode == 1 and "duplicate prompt identity" in result.stderr, "2 prompt identity uniqueness")

    invalid = make_root("invalid-status")
    write_record(invalid, data=metadata(status="UNKNOWN"))
    result = run(invalid)
    check(result.returncode == 1 and "invalid lifecycle status" in result.stderr, "3 lifecycle status enum")

    missing = make_root("missing-exact")
    write_record(missing, exact=None)
    result = run(missing)
    check(result.returncode == 1 and "missing exact prompt text" in result.stderr, "4 missing exact text rejection")

    refs = make_root("missing-results")
    write_record(refs, data=metadata(result_artifacts=[]))
    result = run(refs)
    check(result.returncode == 1 and "requires result references" in result.stderr, "5 executed prompt result references")

    historical = make_root("historical")
    historical_data = metadata(
        status="NOT_PRESERVED", exact_text_preserved=False, result_artifacts=[],
        evidence_limitation="The historical exact text was not preserved.",
    )
    historical_data.pop("exact_text_sha256")
    write_record(historical, data=historical_data, exact=None)
    check(run(historical).returncode == 0, "6 honest NOT_PRESERVED record")

    false_history = make_root("false-history")
    write_record(false_history, data=historical_data)
    result = run(false_history)
    check(result.returncode == 1 and "NOT_PRESERVED cannot claim or contain exact text" in result.stderr, "7 historical reconstruction refusal")

    formal = make_root("formal-reference")
    authoritative = formal / "governance/runs/KGR-TEST/prompt/exact.md"
    authoritative.parent.mkdir(parents=True)
    authoritative.write_text("authoritative formal run prompt\n")
    formal_data = metadata(
        category="FORMAL_RUN", custody="FORMAL_RUN_REFERENCE",
        authoritative_prompt_path="governance/runs/KGR-TEST/prompt/exact.md",
        exact_text_preserved=False,
    )
    formal_data.pop("exact_text_sha256")
    write_record(formal, data=formal_data, exact=None)
    check(run(formal).returncode == 0, "8 formal run authoritative reference without duplication")

    duplicated_formal = make_root("duplicated-formal")
    authoritative = duplicated_formal / "governance/runs/KGR-TEST/prompt/exact.md"
    authoritative.parent.mkdir(parents=True)
    authoritative.write_text("authoritative formal run prompt\n")
    write_record(duplicated_formal, data=formal_data)
    result = run(duplicated_formal)
    check(result.returncode == 1 and "must not duplicate exact prompt text" in result.stderr, "9 formal run duplication refusal")

    immutable = make_root("immutable")
    prompt = write_record(immutable)
    subprocess.run(["git", "init", "--quiet", "--initial-branch=main"], cwd=immutable, check=True)
    subprocess.run(["git", "add", "."], cwd=immutable, check=True)
    subprocess.run(["git", "-c", "user.name=Prompt Tests", "-c", "user.email=prompt-tests@local.invalid", "commit", "--quiet", "-m", "fixture"], cwd=immutable, check=True)
    prompt.write_text(prompt.read_text().replace("Synthetic prompt custody test", "Mutated executed prompt"))
    result = run(immutable)
    check(result.returncode == 1 and "executed prompt is immutable" in result.stderr, "10 executed prompt immutability")

    owner_publication = make_root("owner-publication-authorization")
    write_record(
        owner_publication,
        data=metadata(evidence_type="OWNER_PUBLICATION_AUTHORIZATION"),
    )
    result = run(owner_publication)
    check(
        result.returncode == 1
        and "publication evidence, not a material prompt custody record" in result.stderr,
        "11 owner publication authorization is not material prompt custody",
        result.stderr,
    )

    unknown_evidence = make_root("unknown-evidence-type")
    write_record(unknown_evidence, data=metadata(evidence_type="UNKNOWN"))
    result = run(unknown_evidence)
    check(
        result.returncode == 1 and "invalid evidence_type" in result.stderr,
        "12 unknown evidence type rejection",
        result.stderr,
    )
finally:
    shutil.rmtree(temporary, ignore_errors=True)

print(f"RESULT: {passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
PY
