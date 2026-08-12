#!/usr/bin/env python3
"""Deterministically validate G6 B-04's reusable L6 helper boundary."""

from __future__ import annotations

import ast
import hashlib
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRE_B04_REVISION = "d920ccae403e6e3723c9053f9ca7d63bc024ca05"
HELPERS = ("__init__.py", "atomic.py", "canonical.py", "diagnostics.py", "safe_zip.py", "schemas.py", "strict_yaml.py")
CORE = ROOT / "governance/core/l6"
LEGACY = ROOT / "governance/tools/_lib"
INSTRUCTIONS = ("AGENTS.md", "governance/AGENTS.md", "CLAUDE.md")
FORBIDDEN_CORE_IMPORT_PREFIXES = ("governance.adopters", "governance.tools", "governance.methodology")


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, text=True, stdout=subprocess.PIPE).stdout


def source_at(revision: str, path: str) -> bytes:
    return subprocess.run(["git", "-C", str(ROOT), "show", f"{revision}:{path}"], check=True, stdout=subprocess.PIPE).stdout


def imported_modules(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module)
    return modules


def main() -> int:
    errors: list[str] = []
    moved_hashes: dict[str, str] = {}
    for name in HELPERS:
        core_path = CORE / name
        legacy_path = LEGACY / name
        if not core_path.is_file() or not legacy_path.is_file():
            errors.append(f"missing moved helper or compatibility export: {name}")
            continue
        original = source_at(PRE_B04_REVISION, f"governance/tools/_lib/{name}")
        current = core_path.read_bytes()
        if current != original:
            errors.append(f"moved helper differs from its pre-B04 source: {name}")
        moved_hashes[name] = hashlib.sha256(current).hexdigest()
        text = core_path.read_text(encoding="utf-8")
        if "HugePlanning" in text or "/home/sugar/" in text:
            errors.append(f"moved helper contains a project literal or path: {name}")
        if any(module.startswith(FORBIDDEN_CORE_IMPORT_PREFIXES) for module in imported_modules(core_path)):
            errors.append(f"moved helper imports a project-bound surface: {name}")
    for name in HELPERS[1:]:
        wrapper = (LEGACY / name).read_text(encoding="utf-8")
        if f"governance.core.l6.{name[:-3]}" not in wrapper:
            errors.append(f"legacy compatibility export does not resolve moved helper: {name}")
    if git("diff", "--name-only", PRE_B04_REVISION, "--", *INSTRUCTIONS).strip():
        errors.append("an active instruction surface changed during B-04")
    if errors:
        print("FAIL: " + "; ".join(errors), file=sys.stderr)
        return 1
    print("PASS: READY L6 helpers are byte-identical history-preserving moves")
    print("PASS: core L6 imports no project-bound surface or HugePlanning value")
    print("PASS: legacy callers retain compatible helper import paths")
    print("moved_helper_sha256=" + ",".join(f"{name}:{digest}" for name, digest in sorted(moved_hashes.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
