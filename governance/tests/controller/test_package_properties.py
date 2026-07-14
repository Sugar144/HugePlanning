"""Bounded package, structured-data, serialization, and dry-run properties."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import warnings

from hypothesis import given, strategies as st
import pytest

from _lib.canonical import json_bytes
from _lib.safe_zip import inspect
from _lib.strict_yaml import StrictYAMLError, load_bytes
from conftest import GOV, LOOP, PACKAGE_CASES, TOOLS
from validate_run_package import validate_package


SAFE_PART = st.text(alphabet="abcdefghijklmnopqrstuvwxyz0123456789_-", min_size=1, max_size=12)
SAFE_NAME = st.lists(SAFE_PART, min_size=1, max_size=3).map(lambda parts: "/".join(parts) + ".txt")
HOSTILE_NAME = st.one_of(
    SAFE_PART.map(lambda value: "../" + value),
    SAFE_PART.map(lambda value: "/" + value),
    st.tuples(SAFE_PART, SAFE_PART).map(lambda parts: parts[0] + "\\" + parts[1]),
    SAFE_PART.map(lambda value: "./" + value),
)


@given(name=SAFE_NAME, content=st.binary(max_size=256))
def test_bounded_safe_zip_members_round_trip(name: str, content: bytes, tmp_path: Path) -> None:
    archive = PACKAGE_CASES.write_zip(tmp_path / "safe.zip", [(name, content)])
    members, diagnostics = inspect(archive)
    assert diagnostics == []
    assert members == {name: content}


@given(name=HOSTILE_NAME, content=st.binary(max_size=64))
def test_hostile_or_ambiguous_zip_paths_are_rejected(name: str, content: bytes, tmp_path: Path) -> None:
    archive = PACKAGE_CASES.write_zip(tmp_path / "hostile.zip", [(name, content)])
    _, diagnostics = inspect(archive)
    assert "ZIP_UNSAFE_PATH" in {item.code for item in diagnostics}


@given(name=SAFE_NAME, content=st.binary(min_size=1, max_size=128))
def test_duplicate_members_are_rejected(name: str, content: bytes, tmp_path: Path) -> None:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message="Duplicate name:", category=UserWarning)
        archive = PACKAGE_CASES.write_zip(tmp_path / "duplicate.zip", [(name, content), (name, content[::-1])])
    _, diagnostics = inspect(archive)
    assert "ZIP_DUPLICATE_MEMBER" in {item.code for item in diagnostics}


@given(st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1, max_size=12), st.integers())
def test_structured_data_mutations_and_integrity_mismatches_are_detectable(key: str, value: int) -> None:
    with pytest.raises(StrictYAMLError):
        load_bytes(f"{key}: {value}\n{key}: {value + 1}\n".encode())
    expected = hashlib.sha256(f"{key}:{value}".encode()).hexdigest()
    mutated = hashlib.sha256(f"{key}:{value + 1}".encode()).hexdigest()
    assert expected != mutated


@given(content=st.binary(min_size=1, max_size=128), mutation=st.binary(min_size=1, max_size=32))
def test_package_validator_rejects_integrity_mismatch(content: bytes, mutation: bytes, tmp_path: Path) -> None:
    mutated = content + mutation
    custody = tmp_path / "result.yaml"
    custody.write_bytes(content)
    expected_hash = hashlib.sha256(content).hexdigest()
    envelope = tmp_path / "input-envelope.yaml"
    envelope.write_text(
        "execution_contract:\n"
        "  role: Kernel Designer\n"
        "  mode: CLOSURE_REMEDIATION\n"
        "  protocol_id: GOV-PROTOCOL-003\n"
        "  protocol_version: 0.1.0\n"
        "  target_run: KGR-006\n"
        "expected_output_members: [result.yaml]\n"
        "formal_inputs:\n"
        "  artifacts:\n"
        "    - package_member: result.yaml\n"
        f"      sha256: {expected_hash}\n"
        f"      import_path: {custody}\n",
        encoding="utf-8",
    )
    package = PACKAGE_CASES.write_zip(tmp_path / "mismatch.zip", [("result.yaml", mutated)])
    _, diagnostics = validate_package("import", "designer", package, envelope, None, None)
    assert "PACKAGE_MEMBER_HASH_MISMATCH" in {item.code for item in diagnostics}

@given(st.dictionaries(SAFE_PART, st.one_of(st.integers(), st.booleans(), st.text(max_size=32)), max_size=12))
def test_canonical_json_output_is_deterministic(value: dict) -> None:
    reversed_items = dict(reversed(list(value.items())))
    assert json_bytes(value, trailing_newline=True) == json_bytes(reversed_items, trailing_newline=True)
    assert json.loads(json_bytes(value)) == value


def test_dry_run_does_not_write_repository_transition_records(tmp_path: Path) -> None:
    fixture = GOV / "tests/fixtures/transitions/01-valid-kgr-005-closure-confirmed.yaml"
    command = [
        sys.executable, str(TOOLS / "apply_loop_transition.py"), "import",
        "--loop", str(LOOP), "--source-run", "KGR-005", "--input", str(fixture),
        "--history-root", str(tmp_path), "--json",
    ]
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout)["applied"] is False
    assert not list(tmp_path.rglob("controller-transition.json"))
