#!/usr/bin/env python3
"""Build deterministic, program-scoped projections of immutable L5 learning evidence."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

PROGRAM = re.compile(r"^[a-z][a-z0-9-]{0,62}$")

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def tokens(text: str) -> int:
    """Pinned deterministic lexical measurement for bounded task projections."""
    return len(re.findall(r"\S+", text))

def build(root: Path, program: str, task: str, output: Path) -> dict:
    if not PROGRAM.fullmatch(program): raise ValueError("invalid program namespace")
    if not task.strip(): raise ValueError("task is required")
    records = sorted((root / "governance/learning/records").glob("*.yaml"))
    sources = [{"path": str(p.relative_to(root)), "sha256": digest(p)} for p in records]
    # The record identity and stable path order are the only retrieval rule.
    entries = [{"source": item["path"], "sha256": item["sha256"]} for item in sources]
    index = {"document_id": "GOV-GEN-G6-B-07-INDEX-001", "program": program, "state_namespace": f"{program}:l7", "sources": sources, "entries": entries, "retrieval": "lexicographic_source_path_only", "federation": "NOT_CLAIMED"}
    projection = {"document_id": "GOV-GEN-G6-B-07-PROJECTION-001", "program": program, "state_namespace": f"{program}:l7", "task": task, "entry_sources": [e["source"] for e in entries], "source_hashes": {e["source"]: e["sha256"] for e in entries}, "retrieval": index["retrieval"]}
    encoded = json.dumps(projection, sort_keys=True, separators=(",", ":")) + "\n"
    projection["token_measurement"] = {"method": "whitespace-token-v1", "count": tokens(encoded), "limit": 4000}
    if projection["token_measurement"]["count"] > 4000: raise ValueError("bounded projection exceeds token limit")
    output.mkdir(parents=True, exist_ok=True)
    (output / "index.json").write_text(json.dumps(index, sort_keys=True, separators=(",", ":")) + "\n")
    (output / "projection.json").write_text(json.dumps(projection, sort_keys=True, separators=(",", ":")) + "\n")
    return projection

def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("--program", required=True); p.add_argument("--task", required=True); p.add_argument("--output", required=True)
    a = p.parse_args(); root = Path(__file__).resolve().parents[2]
    result = build(root, a.program, a.task, Path(a.output)); print(json.dumps(result["token_measurement"], sort_keys=True)); return 0
if __name__ == "__main__": raise SystemExit(main())
