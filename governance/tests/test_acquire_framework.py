from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/acquire-framework.py"


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, text=True, capture_output=True
    ).stdout.strip()


@pytest.fixture()
def acquired_framework(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    source = tmp_path / "source"
    source.mkdir()
    git("init", "--initial-branch=main", cwd=source)
    git("config", "user.name", "framework test", cwd=source)
    git("config", "user.email", "framework-test@local.invalid", cwd=source)
    (source / ".gitignore").write_text("*.ignored\n", encoding="utf-8")
    manifest = source / "release-manifest.json"
    manifest.write_text('{"release":"test"}\n', encoding="utf-8")
    tracked = source / "framework/core/contract.txt"
    tracked.parent.mkdir(parents=True)
    tracked.write_text("locked framework bytes\n", encoding="utf-8")
    git("add", ".", cwd=source)
    git("commit", "-m", "framework fixture", cwd=source)
    commit = git("rev-parse", "HEAD", cwd=source)

    remote = tmp_path / "general-governance.git"
    git("clone", "--bare", str(source), str(remote))
    lock = tmp_path / "framework-lock.json"
    lock.write_text(
        json.dumps(
            {
                "framework": {
                    "repository": "Sugar144/general-governance",
                    "version": "0.1.0-rc.1",
                    "commit_sha": commit,
                    "release_manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest(),
                }
            }
        ),
        encoding="utf-8",
    )

    spec = importlib.util.spec_from_file_location("acquire_framework_test", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "LOCK", lock)
    monkeypatch.setattr(module, "REMOTE", str(remote))

    cache_root = tmp_path / "cache"

    def acquire() -> int:
        monkeypatch.setattr(sys, "argv", [str(SCRIPT), "--cache-root", str(cache_root)])
        return module.main()

    destination = cache_root / commit
    return module, acquire, destination, commit, lock


def clean_status(destination: Path) -> str:
    return git("status", "--porcelain", "--untracked-files=all", "--ignored", cwd=destination)


def test_existing_cache_is_restored_to_the_locked_clean_checkout(acquired_framework) -> None:
    _, acquire, destination, commit, _ = acquired_framework
    assert acquire() == 0
    tracked = destination / "framework/core/contract.txt"
    tracked.write_text("locally modified\n", encoding="utf-8")
    (destination / "injected.txt").write_text("untracked\n", encoding="utf-8")
    (destination / "ignored.ignored").write_text("ignored\n", encoding="utf-8")

    assert acquire() == 0
    assert tracked.read_text(encoding="utf-8") == "locked framework bytes\n"
    assert not (destination / "injected.txt").exists()
    assert not (destination / "ignored.ignored").exists()
    assert git("rev-parse", "HEAD", cwd=destination) == commit
    assert clean_status(destination) == ""


def test_wrong_origin_is_rejected_before_cache_use(acquired_framework) -> None:
    _, acquire, destination, _, _ = acquired_framework
    assert acquire() == 0
    git("remote", "set-url", "origin", "https://example.invalid/wrong.git", cwd=destination)
    assert acquire() == 1


def test_wrong_manifest_digest_is_rejected_after_exact_checkout(acquired_framework) -> None:
    _, acquire, destination, commit, lock = acquired_framework
    assert acquire() == 0
    identity = json.loads(lock.read_text(encoding="utf-8"))
    identity["framework"]["release_manifest_sha256"] = "0" * 64
    lock.write_text(json.dumps(identity), encoding="utf-8")

    assert acquire() == 1
    assert git("rev-parse", "HEAD", cwd=destination) == commit
    assert clean_status(destination) == ""
