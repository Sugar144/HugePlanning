from __future__ import annotations
import hashlib, json, shutil
from pathlib import Path
from governance.tools.build_g6_b07_projection import build

ROOT = Path(__file__).resolve().parents[2]
def copy_l5(tmp_path: Path) -> Path:
    root = tmp_path / "repo"; shutil.copytree(ROOT / "governance/learning/records", root / "governance/learning/records"); return root
def files(path: Path) -> dict[str, bytes]: return {p.name: p.read_bytes() for p in path.iterdir()}
def test_deterministic_traceable_and_bounded(tmp_path: Path) -> None:
    root = copy_l5(tmp_path); before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (root / "governance/learning/records").glob("*.yaml")}
    build(root, "program-a", "bounded task", root / "out-a1"); build(root, "program-a", "bounded task", root / "out-a2")
    assert files(root / "out-a1") == files(root / "out-a2")
    index = json.loads((root / "out-a1/index.json").read_text()); projection = json.loads((root / "out-a1/projection.json").read_text())
    assert {x["path"].split("/")[-1]: x["sha256"] for x in index["sources"]} == before
    assert projection["token_measurement"]["count"] <= projection["token_measurement"]["limit"]
    assert {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (root / "governance/learning/records").glob("*.yaml")} == before
def test_program_namespaces_are_isolated(tmp_path: Path) -> None:
    root = copy_l5(tmp_path); build(root, "program-a", "task", root / "a"); build(root, "program-b", "task", root / "b")
    a, b = (json.loads((root / x / "index.json").read_text()) for x in ("a", "b"))
    assert a["state_namespace"] != b["state_namespace"] and a["program"] != b["program"]
