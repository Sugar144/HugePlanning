from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import zipfile

import yaml


REPO = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO / "governance/tools/build_review_bundle.py"
SCHEMA_PATH = REPO / "governance/schemas/review-bundle-config.schema.json"
sys.path.insert(0, str(TOOL_PATH.parent))
SPEC = importlib.util.spec_from_file_location("build_review_bundle", TOOL_PATH)
assert SPEC and SPEC.loader
bundle_tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bundle_tool)


def command(*argv: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(argv, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


def repository(tmp_path: Path) -> tuple[Path, str]:
    root = tmp_path / "repository"
    root.mkdir()
    command("git", "init", "--quiet", "--initial-branch=test-review", cwd=root)
    command("git", "config", "user.name", "Review Tests", cwd=root)
    command("git", "config", "user.email", "review-tests@local.invalid", cwd=root)
    (root / "governance/schemas").mkdir(parents=True)
    (root / "governance/schemas/review-bundle-config.schema.json").write_bytes(SCHEMA_PATH.read_bytes())
    (root / "tracked.txt").write_text("before\n")
    assert command("git", "add", ".", cwd=root).returncode == 0
    assert command("git", "commit", "--quiet", "-m", "base", cwd=root).returncode == 0
    head = command("git", "rev-parse", "HEAD", cwd=root).stdout.strip()
    return root, head


def configuration(root: Path, head: str, paths: list[str], argv: list[str] | None = None) -> Path:
    data = {
        "schema_version": "0.1.0",
        "repository": {
            "expected_branch": "test-review",
            "base_head": head,
            "require_changes": True,
            "require_empty_staging": True,
        },
        "scope": {"paths": paths, "enforce_exact": True},
        "validations": [{
            "id": "required-check",
            "argv": argv or [sys.executable, "-c", "print('validated')"],
            "cwd": ".",
            "required": True,
            "timeout_seconds": 30,
        }],
        "dependencies": [{
            "id": "python-version",
            "argv": [sys.executable, "--version"],
            "cwd": ".",
            "required": True,
            "timeout_seconds": 30,
        }],
        "bundle": {"root_directory": "review"},
    }
    path = root / "review-config.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False))
    return path


def test_inventory_tracks_modified_and_new_files(tmp_path: Path) -> None:
    root, head = repository(tmp_path)
    (root / "tracked.txt").write_text("after\n")
    (root / "new.bin").write_bytes(b"\x00\xffreview")
    records = bundle_tool.inventory(root, head)
    assert records == [
        {"status": "??", "path": "new.bin"},
        {"status": "M", "path": "tracked.txt"},
    ]


def test_safe_paths_reject_traversal_symlink_duplicate_and_case_ambiguity(tmp_path: Path) -> None:
    root, _ = repository(tmp_path)
    for value in ("../escape", "/absolute", "ambiguous\\path", "control\npath"):
        try:
            bundle_tool.checked_path(root, value, "test")
        except bundle_tool.BundleError:
            pass
        else:
            raise AssertionError(f"unsafe path accepted: {value!r}")
    (root / "link").symlink_to("tracked.txt")
    try:
        bundle_tool.checked_path(root, "link", "test")
    except bundle_tool.BundleError:
        pass
    else:
        raise AssertionError("symlink accepted")
    for paths in (["same", "same"], ["Case", "case"]):
        try:
            bundle_tool.validate_unique_paths(paths, "test")
        except bundle_tool.BundleError:
            pass
        else:
            raise AssertionError("duplicate or ambiguous paths accepted")


def test_required_validation_failure_creates_no_bundle(tmp_path: Path) -> None:
    root, head = repository(tmp_path)
    (root / "tracked.txt").write_text("after\n")
    config = configuration(root, head, ["review-config.yaml", "tracked.txt"], [sys.executable, "-c", "raise SystemExit(7)"])
    output = tmp_path / "failed.zip"
    try:
        bundle_tool.build(root, config, output)
    except bundle_tool.BundleError as exc:
        assert "required commands failed" in str(exc)
    else:
        raise AssertionError("required validation failure was accepted")
    assert not output.exists()


def test_duplicate_configuration_key_is_rejected(tmp_path: Path) -> None:
    root, head = repository(tmp_path)
    config = root / "duplicate.yaml"
    config.write_text(
        "schema_version: 0.1.0\n"
        "schema_version: 0.1.0\n"
        f"repository: {{expected_branch: test-review, base_head: {head}, require_changes: true, require_empty_staging: true}}\n"
        "scope: {paths: [duplicate.yaml], enforce_exact: true}\n"
        "validations: []\n"
        "dependencies: []\n"
        "bundle: {root_directory: review}\n"
    )
    try:
        bundle_tool.load_config(root, config)
    except bundle_tool.BundleError as exc:
        assert "duplicate mapping key" in str(exc)
    else:
        raise AssertionError("duplicate YAML configuration key accepted")


def test_bundle_order_hashes_and_integrity(tmp_path: Path) -> None:
    root, head = repository(tmp_path)
    (root / "tracked.txt").write_text("after\n")
    (root / "new.bin").write_bytes(b"\x00\xffreview")
    config = configuration(root, head, ["new.bin", "review-config.yaml", "tracked.txt"])
    output = tmp_path / "review.zip"
    result = bundle_tool.build(root, config, output)
    assert result["sha256"] == hashlib.sha256(output.read_bytes()).hexdigest()

    with zipfile.ZipFile(output) as archive:
        names = archive.namelist()
        assert names == sorted(names)
        assert len(names) == len(set(names))
        assert archive.read("review/files/new.bin") == b"\x00\xffreview"
        assert b"GIT binary patch" in archive.read("review/changes.diff")
        manifest_lines = archive.read("review/SHA256SUMS").decode().splitlines()
        manifest_names = []
        for line in manifest_lines:
            digest, name = line.split("  ", 1)
            manifest_names.append(name)
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
        assert manifest_names == sorted(name for name in names if name != "review/SHA256SUMS")
        validation = json.loads(archive.read("review/evidence/validations.json"))
        assert validation[0]["exit_code"] == 0
        assert validation[0]["argv"][-1] == "print('validated')"
        assert isinstance(validation[0]["duration_ms"], int)


def test_bundle_rejects_scope_drift_and_repository_output(tmp_path: Path) -> None:
    root, head = repository(tmp_path)
    (root / "tracked.txt").write_text("after\n")
    config = configuration(root, head, ["review-config.yaml"])
    try:
        bundle_tool.build(root, config, tmp_path / "scope.zip")
    except bundle_tool.BundleError as exc:
        assert "scope mismatch" in str(exc)
    else:
        raise AssertionError("scope drift accepted")
    config = configuration(root, head, ["review-config.yaml", "tracked.txt"])
    try:
        bundle_tool.build(root, config, root / "forbidden.zip")
    except bundle_tool.BundleError as exc:
        assert "outside the repository" in str(exc)
    else:
        raise AssertionError("repository output accepted")
