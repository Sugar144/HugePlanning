#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

python3 - "$REPO_ROOT" <<'PY'
from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import yaml

repo = Path(sys.argv[1])
fixtures = repo / "governance/tests/fixtures/learning"
source_tool = repo / "governance/tools/manage_learning.py"
source_schemas = repo / "governance/schemas"
temporary = Path(tempfile.mkdtemp(prefix="hp-learning-tests."))
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


def make_env(name):
    root = temporary / name
    (root / "governance/tools").mkdir(parents=True)
    (root / "governance/schemas").mkdir(parents=True)
    (root / "governance/learning/records").mkdir(parents=True)
    (root / "governance/learning/events").mkdir(parents=True)
    shutil.copy2(source_tool, root / "governance/tools/manage_learning.py")
    shutil.copy2(source_schemas / "failure-record.schema.json", root / "governance/schemas")
    shutil.copy2(source_schemas / "failure-record-event.schema.json", root / "governance/schemas")
    return root


def run(root, *args, env=None):
    command = [sys.executable, str(root / "governance/tools/manage_learning.py"), *map(str, args)]
    merged = os.environ.copy()
    if env:
        merged.update(env)
    return subprocess.run(command, cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=merged)


def seed(root, draft=None):
    source = draft or fixtures / "new-record-draft.yaml"
    result = run(root, "record", "--input", source, "--apply")
    assert result.returncode == 0, result.stderr
    return root / "governance/learning/records/HP-FAIL-001.yaml"


try:
    repository_result = subprocess.run(
        [sys.executable, str(source_tool), "validate"],
        cwd=repo, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    check(repository_result.returncode == 0 and '"events":1' in repository_result.stdout, "1 repository HP-FAIL-004 event schema and numbering", repository_result.stderr)
    repository_event = yaml.safe_load((repo / "governance/learning/events/HP-FAIL-004/HP-FAIL-004-E001.yaml").read_text())["failure_record_event"]
    repository_index = (repo / "governance/learning/FAILURE_AND_LESSONS_INDEX.md").read_text()
    check(
        repository_event["event_type"] == "CORRECTION"
        and repository_event["status_from"] is None
        and repository_event["status_to"] is None
        and "HP-FAIL-004" in repository_index
        and "CORRECTED" in next(line for line in repository_index.splitlines() if "HP-FAIL-004" in line),
        "2 HP-FAIL-004 remains CORRECTED in generated index",
    )

    base = make_env("base")
    result = run(base, "validate", "--record", fixtures / "valid-base-record.yaml")
    check(result.returncode == 0, "3 valid base record", result.stderr)
    data = yaml.safe_load((fixtures / "valid-base-record.yaml").read_text())
    expected_classes = {"FAILURE", "NEAR_MISS", "AMBIGUITY", "PROCESS_DEFECT", "TOOLING_GAP", "COST_WASTE", "OWNER_CORRECTION"}
    check(set(data["failure_record"]["classification"]) == expected_classes, "4 every classification enum")

    result = run(base, "validate", "--record", fixtures / "missing-required-field.yaml")
    check(result.returncode == 1 and "schema validation failed" in result.stderr, "3 missing required field")
    result = run(base, "validate", "--record", fixtures / "duplicate-key.yaml")
    check(result.returncode == 1 and "duplicate YAML key" in result.stderr, "4 duplicate YAML key")

    duplicate_id = make_env("duplicate-id")
    original = seed(duplicate_id)
    shutil.copy2(original, duplicate_id / "governance/learning/records/duplicate.yaml")
    result = run(duplicate_id, "index", "--apply")
    check(result.returncode == 1 and "duplicate record ID" in result.stderr, "5 duplicate record ID")

    duplicate_fp = make_env("duplicate-fingerprint")
    original = seed(duplicate_fp)
    second = yaml.safe_load(original.read_text())
    second["failure_record"]["id"] = "HP-FAIL-002"
    (duplicate_fp / "governance/learning/records/HP-FAIL-002.yaml").write_text(yaml.safe_dump(second, sort_keys=False))
    result = run(duplicate_fp, "index", "--apply")
    check(result.returncode == 1 and "fingerprint collision" in result.stderr, "6 exact fingerprint duplicate")

    valid_event = make_env("valid-event")
    seed(valid_event)
    result = run(valid_event, "event", "--input", fixtures / "valid-status-event.yaml", "--apply")
    check(result.returncode == 0 and "\"applied\":true" in result.stdout, "7 valid status event", result.stderr)

    invalid_event = make_env("invalid-event")
    seed(invalid_event)
    result = run(invalid_event, "event", "--input", fixtures / "invalid-status-event.yaml")
    check(result.returncode == 1 and "invalid status transition" in result.stderr, "8 invalid status transition")

    numbering = make_env("numbering")
    seed(numbering)
    event = yaml.safe_load((fixtures / "valid-status-event.yaml").read_text())
    event["failure_record_event"]["id"] = "HP-FAIL-001-E002"
    target = numbering / "governance/learning/events/HP-FAIL-001/HP-FAIL-001-E002.yaml"
    target.parent.mkdir(parents=True)
    target.write_text(yaml.safe_dump(event, sort_keys=False))
    result = run(numbering, "index", "--apply")
    check(result.returncode == 1 and "invalid event numbering" in result.stderr, "9 invalid event numbering")

    immutable = make_env("immutable")
    validated = yaml.safe_load((fixtures / "valid-base-record.yaml").read_text())
    validated["failure_record"]["id"] = "HP-FAIL-001"
    validated["failure_record"]["status"] = "VALIDATED"
    validated_path = immutable / "governance/learning/records/HP-FAIL-001.yaml"
    validated_path.write_text(yaml.safe_dump(validated, sort_keys=False))
    check(run(immutable, "index", "--apply").returncode == 0, "10a validated fixture index setup")
    subprocess.run(["git", "init", "--quiet", "--initial-branch=main"], cwd=immutable, check=True)
    subprocess.run(["git", "add", "."], cwd=immutable, check=True)
    subprocess.run(["git", "-c", "user.name=Learning Tests", "-c", "user.email=learning-tests@local.invalid", "commit", "--quiet", "-m", "fixture"], cwd=immutable, check=True)
    changed = yaml.safe_load(validated_path.read_text())
    changed["failure_record"]["title"] = "Mutated validated title"
    validated_path.write_text(yaml.safe_dump(changed, sort_keys=False))
    result = run(immutable, "validate")
    check(result.returncode == 1 and "direct mutation of validated base record" in result.stderr, "10 mutation of validated base record")

    risk = make_env("risk")
    seed(risk)
    result = run(risk, "event", "--input", fixtures / "accepted-risk-missing-owner.yaml")
    check(result.returncode == 1 and "accepted-risk event lacks owner" in result.stderr, "11 accepted-risk event missing owner evidence")

    ordering = make_env("ordering")
    seed(ordering)
    second_draft = yaml.safe_load((fixtures / "new-record-draft.yaml").read_text())
    second_draft["failure_record"]["title"] = "Second ordered record"
    second_draft["failure_record"]["observed_behavior"] = "A distinct second record exercises ordering."
    second_draft["failure_record"]["root_cause"]["systemic"] = "Distinct second systemic cause."
    second_draft["failure_record"]["evidence_refs"][0]["locator"] = "synthetic-second-draft"
    second_path = ordering / "second-draft.yaml"
    second_path.write_text(yaml.safe_dump(second_draft, sort_keys=False))
    assert run(ordering, "record", "--input", second_path, "--apply").returncode == 0
    assert run(ordering, "index", "--apply").returncode == 0
    index = ordering / "governance/learning/FAILURE_AND_LESSONS_INDEX.md"
    index_text = index.read_text()
    check(index_text.index("HP-FAIL-001") < index_text.index("HP-FAIL-002"), "12 deterministic index ordering")
    index.write_text(index_text + "manual drift\n")
    result = run(ordering, "validate")
    check(result.returncode == 1 and "generated index drift" in result.stderr, "13 index drift detection")

    dry = make_env("dry-run")
    before = sorted(path.relative_to(dry).as_posix() for path in dry.rglob("*"))
    result = run(dry, "record", "--input", fixtures / "new-record-draft.yaml")
    after = sorted(path.relative_to(dry).as_posix() for path in dry.rglob("*"))
    check(result.returncode == 0 and before == after and "\"applied\":false" in result.stdout, "14 dry-run produces no writes")
    before_files = {path.relative_to(dry).as_posix() for path in dry.rglob("*") if path.is_file()}
    result = run(dry, "record", "--input", fixtures / "new-record-draft.yaml", "--apply")
    after_files = {path.relative_to(dry).as_posix() for path in dry.rglob("*") if path.is_file()}
    check(result.returncode == 0 and after_files - before_files == {"governance/learning/records/HP-FAIL-001.yaml"}, "15 --apply creates only expected file")

    atomic = make_env("atomic")
    result = run(atomic, "record", "--input", fixtures / "new-record-draft.yaml", "--apply", env={"HP_LEARNING_TEST_FAIL_ATOMIC": "before_replace"})
    residue = list((atomic / "governance/learning/records").iterdir())
    check(result.returncode == 2 and not residue, "16 atomic-write failure leaves no partial target", result.stderr)

    traversal = make_env("traversal")
    escape = yaml.safe_load((fixtures / "new-record-draft.yaml").read_text())
    escape["failure_record"]["evidence_refs"][0].update({"type": "REPOSITORY_PATH", "locator": "../../escape", "availability": "PRESERVED"})
    escape_path = traversal / "escape.yaml"
    escape_path.write_text(yaml.safe_dump(escape, sort_keys=False))
    result = run(traversal, "record", "--input", escape_path)
    check(result.returncode == 1 and "escapes root" in result.stderr, "17 path traversal or output escape refusal")

    metrics = data["failure_record"]["metrics"]
    unavailable = all(metrics[key] is None for key in ("exact_token_usage", "model_runs", "human_time_minutes", "correction_cycles", "deterministic_rework_count", "package_rebuild_count"))
    check(metrics["measurement_quality"] == "UNAVAILABLE" and unavailable, "18 metrics unavailable without fabricated values")
    evidence = data["failure_record"]["evidence_refs"][0]
    check(evidence["availability"] == "NOT_PRESERVED", "19 evidence marked NOT_PRESERVED")

    reproducible = make_env("reproducible")
    seed(reproducible)
    assert run(reproducible, "index", "--apply").returncode == 0
    generated = reproducible / "governance/learning/FAILURE_AND_LESSONS_INDEX.md"
    first = generated.read_bytes()
    assert run(reproducible, "index", "--apply").returncode == 0
    second = generated.read_bytes()
    check(first == second, "20 two index generations are byte-identical")
finally:
    shutil.rmtree(temporary, ignore_errors=True)

print(f"RESULT: {passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
PY
