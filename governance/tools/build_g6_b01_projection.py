#!/usr/bin/env python3
"""Construct deterministic, sharded bounded projections for GOV-GEN G6 B-01.

The accepted B-01 source set is built once, with exact path provenance.  It
is then partitioned without omitting sources or truncating text: coherent
seed/capability families are first-fit packed below an operational 18k target;
an oversized coherent unit is split only at Markdown headings, paragraphs, or
lines, in that order.  The resulting machine-readable manifests are evidence,
not a substitute for the semantic baseline executed for every shard.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

TOOL_VERSION = "0.2.0"
PROGRAM = "governance/audits/GOV-GEN-AUD-001-governance-generalization"
G6 = f"{PROGRAM}/G6"
HARD_LIMIT = 20_000
OPERATIONAL_TARGET = 18_000
PATH_RE = re.compile(r"(?<![A-Za-z0-9._/-])([A-Za-z0-9][A-Za-z0-9._/-]*\.(?:md|py|yaml|yml|json))(?![A-Za-z0-9._/-])")
SEEDS = (
    (f"{PROGRAM}/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md", ("§4", "§6", "§7", "§8", "§10")),
    (f"{PROGRAM}/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1.md", ("all",)),
    (f"{PROGRAM}/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R2.md", ("all",)),
    (f"{PROGRAM}/G4/GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001.md", ("§9",)),
    (f"{PROGRAM}/G4/GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001-R1.md", ("§4", "§7", "§8")),
    (f"{PROGRAM}/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md", ("§3", "§7", "§8")),
    (f"{PROGRAM}/G5/GOV-GEN-GR-INDEPENDENT-ARCHITECTURE-REVIEW-001.md", ("§3", "§4", "§5")),
    (f"{G6}/GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001.md", ("§1", "§2", "§3:B-01", "§4")),
    (f"{G6}/GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R1.md", ("all",)),
    (f"{G6}/GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R2.md", ("all",)),
)
GENERATED = {"B-01-input-projection-manifest.yaml"}


@dataclass(frozen=True)
class Unit:
    id: str
    path: str
    selection_rule: str
    text: str
    kind: str
    family: str
    layers: tuple[str, ...]
    source_sha256: str
    byte_count: int
    importing_parent_path: str | None = None
    subdivision: str | None = None


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(root), *args], check=True, text=True, stdout=subprocess.PIPE).stdout.strip()


def tracked_files(root: Path) -> set[str]:
    return set(git(root, "ls-files").splitlines())


def heading_fragment(text: str, selector: str, source: str) -> str:
    if selector == "all":
        return text
    if selector == "§3:B-01":
        match = re.search(r"(?ms)^- packet_id: B-01\n.*?(?=^- packet_id: |\Z)", text)
        if not match:
            raise ValueError(f"{source}: B-01 YAML mapping is unavailable")
        return match.group(0)
    number = re.escape(selector.removeprefix("§"))
    match = re.search(rf"(?m)^(#+)\s+{number}(?:[.\s:].*)?$", text)
    if not match:
        raise ValueError(f"{source}: selector {selector} is unavailable")
    level, start = len(match.group(1)), match.start()
    following = re.compile(r"(?m)^#{1," + str(level) + r"}\s+").search(text, match.end())
    return text[start:following.start() if following else len(text)]


def canonical_candidate(value: str) -> str | None:
    candidate = PurePosixPath(value)
    return None if candidate.is_absolute() or ".." in candidate.parts else candidate.as_posix()


def classify(root: Path, tracked: set[str], declarer: str, original: str) -> dict:
    normalized = canonical_candidate(original)
    result = {"original_textual_reference": original, "declaring_artifact": declarer}
    if original in GENERATED:
        return result | {"classification": "DECLARED_GENERATED_OUTPUT", "resolution_rule": "B01_PACKET_LOCAL_GENERATED_OUTPUT", "normalized_canonical_path": None, "source_sha256": None}
    if normalized is None:
        return result | {"classification": "UNRESOLVED_OR_AMBIGUOUS", "resolution_rule": "REJECTED_UNSAFE_PATH", "normalized_canonical_path": None, "source_sha256": None}
    root_path = normalized if normalized in tracked and (root / normalized).is_file() else None
    local_path = (PurePosixPath(declarer).parent / normalized).as_posix()
    declarer_path = local_path if local_path in tracked and (root / local_path).is_file() else None
    candidates = sorted({candidate for candidate in (root_path, declarer_path) if candidate})
    if len(candidates) == 1:
        path = candidates[0]
        rule = "REPOSITORY_ROOT" if path == root_path else "DECLARER_DIRECTORY"
        return result | {"classification": f"EXISTING_{'REPO' if rule == 'REPOSITORY_ROOT' else 'DECLARER'}_RELATIVE_INPUT", "resolution_rule": rule, "normalized_canonical_path": path, "source_sha256": sha256_bytes((root / path).read_bytes())}
    return result | {"classification": "UNRESOLVED_OR_AMBIGUOUS", "resolution_rule": "AMBIGUOUS_ROOT_AND_DECLARER" if candidates else "NO_SUPPORTED_EXISTING_RESOLUTION", "normalized_canonical_path": None, "source_sha256": None, **({"candidate_paths": candidates} if candidates else {})}


def direct_imports(root: Path, path: str, tracked: set[str]) -> list[str]:
    tree = ast.parse((root / path).read_text(encoding="utf-8"), filename=path)
    package, targets = PurePosixPath(path).parent, set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for item in node.names:
                candidate = PurePosixPath(*item.name.split(".")).with_suffix(".py").as_posix()
                if candidate in tracked: targets.add(candidate)
        elif isinstance(node, ast.ImportFrom):
            base = package
            for _ in range(max(node.level - 1, 0)): base = base.parent
            candidates = [(base / PurePosixPath(*node.module.split("."))).with_suffix(".py")] if node.module else [(base / item.name).with_suffix(".py") for item in node.names]
            targets.update(candidate.as_posix() for candidate in candidates if candidate.as_posix() in tracked)
    return sorted(targets)


def family_and_layers(path: str, kind: str) -> tuple[str, tuple[str, ...]]:
    if kind == "seed_fragment":
        if "/G3/" in path: return "architecture-and-allocation", ("L0", "L1", "L2", "L3", "L4", "L5", "L6", "L7")
        if "/G4/" in path: return "consumer-requirements", ("L0", "L1", "L2", "L3", "L4", "L5", "L6", "L7")
        if "/G5/" in path and "GR-" not in path: return "option-b-physical-architecture", ("L0", "L1", "L2", "L3", "L4", "L5", "L6", "L7")
        if "GR-" in path: return "architecture-review", ("L0", "L1", "L2", "L3", "L4", "L5", "L6", "L7")
        return "b01-execution-contract", ("L0", "L1", "L2", "L3", "L4", "L5", "L6", "L7")
    if path.startswith("governance/methodology/") or path == "governance/AGENTS.md": return "governance-contract", ("L0", "L1", "L2")
    if path.startswith("governance/schemas/") or path.startswith("governance/validation/"): return "schema-and-validation", ("L6",)
    if path.startswith("governance/tools/"): return "deterministic-tooling", ("L6",)
    if path.startswith("governance/prompts/"): return "provider-adapter", ("L4",)
    if path.startswith("governance/loops/"): return "closure-and-state", ("L7",)
    return "boundary-context", ("L0", "L1", "L2", "L6")


def token_count(encoding, text: str) -> int:
    return len(encoding.encode(text, disallowed_special=()))


def split_text(encoding, unit: Unit) -> list[Unit]:
    if token_count(encoding, unit.text) <= OPERATIONAL_TARGET:
        return [unit]
    # Preserve semantic structure before any lexical fallback.
    pieces = re.split(r"(?m)(?=^#{1,6}\s+)", unit.text) if unit.path.endswith(".md") else re.split(r"(?m)(?=^\s*$)", unit.text)
    pieces = [piece for piece in pieces if piece]
    if len(pieces) == 1:
        pieces = re.split(r"(?m)(?=^\s*$)", unit.text)
    chunks, current = [], ""
    for piece in pieces:
        if token_count(encoding, piece) > OPERATIONAL_TARGET:
            lines = piece.splitlines(keepends=True)
            sub, piece_current = [], ""
            for line in lines:
                if piece_current and token_count(encoding, piece_current + line) > OPERATIONAL_TARGET:
                    sub.append(piece_current); piece_current = ""
                piece_current += line
            if piece_current: sub.append(piece_current)
            pieces[pieces.index(piece):pieces.index(piece) + 1] = sub
            return split_text(encoding, Unit(unit.id, unit.path, unit.selection_rule, "".join(pieces), unit.kind, unit.family, unit.layers, unit.source_sha256, unit.byte_count, unit.importing_parent_path, "LINE_BOUNDARY"))
        if current and token_count(encoding, current + piece) > OPERATIONAL_TARGET:
            chunks.append(current); current = ""
        current += piece
    if current: chunks.append(current)
    return [Unit(f"{unit.id}#part-{index:02d}", unit.path, unit.selection_rule, text, unit.kind, unit.family, unit.layers, unit.source_sha256, unit.byte_count, unit.importing_parent_path, "STRUCTURAL_BOUNDARY") for index, text in enumerate(chunks, 1)]


def render_shard_header(frozen_revision: str, shard_id: str, members: list[Unit], edges: list[dict]) -> str:
    return json.dumps({"frozen_revision": frozen_revision, "projection": "GOV-GEN-G6-B-01-SHARDED", "shard_id": shard_id, "logical_layers": sorted({layer for unit in members for layer in unit.layers}), "cross_shard_relationships": edges}, sort_keys=True) + "\n"


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--root", type=Path, default=Path.cwd()); parser.add_argument("--output-dir", type=Path, default=Path(f"{G6}/B-01")); args = parser.parse_args()
    root, output = args.root.resolve(), (args.root / args.output_dir).resolve()
    if root not in output.parents: raise ValueError("output directory must be within the repository")
    try:
        import tiktoken
    except ModuleNotFoundError as exc: raise RuntimeError("tiktoken 0.12.0 is required for B-01 measurement") from exc
    if tiktoken.__version__ != "0.12.0": raise RuntimeError(f"tiktoken 0.12.0 is required, found {tiktoken.__version__}")
    encoding, tracked, frozen_revision = tiktoken.get_encoding("cl100k_base"), tracked_files(root), git(root, "rev-parse", "HEAD")
    units, references = [], []
    for path, selectors in SEEDS:
        if path not in tracked: raise ValueError(f"fixed seed is not a tracked file: {path}")
        raw_bytes, raw = (root / path).read_bytes(), (root / path).read_text(encoding="utf-8")
        for selector in selectors:
            text = heading_fragment(raw, selector, path); family, layers = family_and_layers(path, "seed_fragment")
            units.append(Unit(f"seed:{path}:{selector}", path, selector, text, "seed_fragment", family, layers, sha256_bytes(raw_bytes), len(raw_bytes)))
            for match in PATH_RE.finditer(text):
                reference = classify(root, tracked, path, match.group(1))
                reference["declaring_unit_id"] = f"seed:{path}:{selector}"
                references.append(reference)
    unique_refs = {(item["declaring_unit_id"], item["original_textual_reference"], item["classification"], item.get("normalized_canonical_path")): item for item in references}
    classifications = sorted(unique_refs.values(), key=lambda item: (item["declaring_artifact"], item["original_textual_reference"], item["classification"]))
    allowed = ("governance/AGENTS.md", "governance/methodology/", "governance/tools/", "governance/schemas/", "governance/validation/", "governance/prompts/", "governance/loops/")
    roots = sorted({item["normalized_canonical_path"] for item in classifications if item["classification"].startswith("EXISTING_") and item["normalized_canonical_path"] and item["normalized_canonical_path"].startswith(allowed)})
    closure, queue = {}, [path for path in roots if path.endswith(".py")]
    while queue:
        parent = queue.pop(0)
        for target in direct_imports(root, parent, tracked):
            if target not in roots and target not in closure: closure[target] = parent; queue.append(target)
    for path in sorted(set(roots) | set(closure)):
        raw_bytes, text = (root / path).read_bytes(), (root / path).read_text(encoding="utf-8"); kind = "source_root" if path in roots else "import_closure"; family, layers = family_and_layers(path, kind)
        units.append(Unit(f"source:{path}", path, "EXACT_CLASSIFIED_PATH" if kind == "source_root" else "PYTHON_IMPORT", text, kind, family, layers, sha256_bytes(raw_bytes), len(raw_bytes), closure.get(path)))
    atoms = [atom for unit in units for atom in split_text(encoding, unit)]
    groups = {family: [atom for atom in atoms if atom.family == family] for family in sorted({atom.family for atom in atoms})}
    shards: list[list[Unit]] = []
    for family in groups:
        for atom in groups[family]:
            trial = "\n".join(unit.text for unit in (shards[-1] if shards else []) + [atom])
            if not shards or token_count(encoding, trial) > OPERATIONAL_TARGET: shards.append([])
            shards[-1].append(atom)
    edges = []
    unit_shard = {unit.id: f"B-01-S{index:02d}" for index, shard in enumerate(shards, 1) for unit in shard}
    for reference in classifications:
        target = reference.get("normalized_canonical_path")
        source_id, target_id = reference.get("declaring_unit_id"), f"source:{target}" if target else None
        if not source_id or not target_id or target_id not in unit_shard:
            continue
        source_shards = sorted({unit_shard[key] for key in unit_shard if key.startswith(source_id)})
        target_shards = sorted({unit_shard[key] for key in unit_shard if key.startswith(target_id)})
        edges.append({"relationship": "CLASSIFIED_SEED_REFERENCE", "from_path": reference["declaring_artifact"], "from_unit_id": source_id, "to_path": target, "to_unit_id": target_id, "from_shards": source_shards, "to_shards": target_shards})
    for child, parent in sorted(closure.items()):
        source_id, target_id = f"source:{parent}", f"source:{child}"
        source_shards = sorted({unit_shard[key] for key in unit_shard if key.startswith(source_id)})
        target_shards = sorted({unit_shard[key] for key in unit_shard if key.startswith(target_id)})
        edges.append({"relationship": "PYTHON_IMPORT", "from_path": parent, "from_unit_id": source_id, "to_path": child, "to_unit_id": target_id, "from_shards": source_shards, "to_shards": target_shards})
    output.mkdir(parents=True, exist_ok=True)
    shard_records = []
    for index, shard in enumerate(shards, 1):
        shard_id = f"B-01-S{index:02d}"; shard_edges = [edge for edge in edges if (shard_id in edge["from_shards"] or shard_id in edge["to_shards"]) and edge["from_shards"] != edge["to_shards"]]
        rendered = render_shard_header(frozen_revision, shard_id, shard, shard_edges) + "".join(f"\n--- {unit.kind} {unit.path} {unit.selection_rule} {unit.id} ---\n{unit.text}" for unit in shard)
        tokens = token_count(encoding, rendered)
        if tokens > HARD_LIMIT: raise ValueError(f"{shard_id} exceeds hard limit: {tokens}")
        name = f"{shard_id.lower()}-projection.md"; (output / name).write_text(rendered, encoding="utf-8")
        shard_records.append({"shard_id": shard_id, "projection": name, "sha256": sha256_bytes(rendered.encode()), "token_count": tokens, "limit": HARD_LIMIT, "operational_target": OPERATIONAL_TARGET, "logical_layers": sorted({layer for unit in shard for layer in unit.layers}), "capability_families": sorted({unit.family for unit in shard}), "members": [{"unit_id": unit.id, "kind": unit.kind, "path": unit.path, "selection_rule": unit.selection_rule, "source_sha256": unit.source_sha256, "source_byte_count": unit.byte_count, "subdivision": unit.subdivision, "importing_parent_path": unit.importing_parent_path} for unit in shard], "cross_shard_relationships": shard_edges})
    inventory = [{"unit_id": unit.id, "kind": unit.kind, "path": unit.path, "selection_rule": unit.selection_rule, "source_sha256": unit.source_sha256, "source_byte_count": unit.byte_count, "family": unit.family, "logical_layers": list(unit.layers), "subdivision": unit.subdivision} for unit in atoms]
    reconciliation = json.dumps({"document_id": "GOV-GEN-G6-B-01-CROSS-SHARD-RECONCILIATION-001", "frozen_revision": frozen_revision, "accepted_canonical_unit_ids": [item["unit_id"] for item in inventory], "shards": [{"shard_id": shard["shard_id"], "member_unit_ids": [member["unit_id"] for member in shard["members"]], "token_count": shard["token_count"]} for shard in shard_records], "cross_shard_relationships": [edge for edge in edges if edge["from_shards"] != edge["to_shards"]]}, indent=2, sort_keys=True) + "\n"
    reconciliation_tokens = token_count(encoding, reconciliation)
    if reconciliation_tokens > HARD_LIMIT: raise ValueError(f"cross-shard reconciliation exceeds hard limit: {reconciliation_tokens}")
    reconciliation_name = "B-01-cross-shard-reconciliation-projection.md"
    (output / reconciliation_name).write_text(reconciliation, encoding="utf-8")
    manifest = {"document_id": "GOV-GEN-G6-B-01-SHARDED-BASELINE-MANIFEST-001", "status": "B-01_SHARDED_PROJECTIONS_CONSTRUCTED", "tool_version": TOOL_VERSION, "frozen_revision": frozen_revision, "measurement": {"package": "tiktoken", "version": tiktoken.__version__, "encoding": "cl100k_base", "hard_limit": HARD_LIMIT, "operational_target": OPERATIONAL_TARGET}, "path_resolution": {"order": ["DECLARED_GENERATED_OUTPUT", "REPOSITORY_ROOT", "DECLARER_DIRECTORY", "UNRESOLVED_OR_AMBIGUOUS"], "classifications": classifications}, "source_roots": roots, "import_closure": closure, "canonical_inventory": inventory, "provenance_graph": {"relationships": edges, "cross_shard_relationship_count": sum(edge["from_shards"] != edge["to_shards"] for edge in edges)}, "shards": shard_records, "reconciliation_projection": {"path": reconciliation_name, "sha256": sha256_bytes(reconciliation.encode()), "token_count": reconciliation_tokens, "limit": HARD_LIMIT}, "coverage": {"accepted_canonical_unit_count": len(inventory), "covered_canonical_unit_count": sum(len(shard["members"]) for shard in shard_records), "uncovered_unit_ids": [], "coverage_equality": True}}
    write_json(output / "B-01-sharded-baseline-manifest.yaml", manifest)
    print(json.dumps({"result": manifest["status"], "shard_count": len(shard_records), "tokens": [shard["token_count"] for shard in shard_records], "coverage": manifest["coverage"]}, sort_keys=True))
    return 0


if __name__ == "__main__": sys.exit(main())
