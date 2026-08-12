#!/usr/bin/env python3
"""Deterministically construct the GOV-GEN G6 B-01 input projection.

The tool deliberately resolves only exact repository-root and declaring-file
relative references.  It never searches by basename or repairs a reference.
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

TOOL_VERSION = "0.1.0"
PROGRAM = "governance/audits/GOV-GEN-AUD-001-governance-generalization"
G6 = f"{PROGRAM}/G6"
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
class Fragment:
    path: str
    selector: str
    text: str


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
    if candidate.is_absolute() or ".." in candidate.parts:
        return None
    return candidate.as_posix()


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
    candidates = sorted(set(candidate for candidate in (root_path, declarer_path) if candidate))
    if len(candidates) == 1:
        path = candidates[0]
        rule = "REPOSITORY_ROOT" if path == root_path else "DECLARER_DIRECTORY"
        return result | {"classification": f"EXISTING_{'REPO' if rule == 'REPOSITORY_ROOT' else 'DECLARER'}_RELATIVE_INPUT", "resolution_rule": rule, "normalized_canonical_path": path, "source_sha256": sha256_bytes((root / path).read_bytes())}
    if len(candidates) > 1:
        return result | {"classification": "UNRESOLVED_OR_AMBIGUOUS", "resolution_rule": "AMBIGUOUS_ROOT_AND_DECLARER", "normalized_canonical_path": None, "source_sha256": None, "candidate_paths": candidates}
    return result | {"classification": "UNRESOLVED_OR_AMBIGUOUS", "resolution_rule": "NO_SUPPORTED_EXISTING_RESOLUTION", "normalized_canonical_path": None, "source_sha256": None}


def direct_imports(root: Path, path: str, tracked: set[str]) -> list[str]:
    tree = ast.parse((root / path).read_text(encoding="utf-8"), filename=path)
    package = PurePosixPath(path).parent
    targets: set[str] = set()
    for node in ast.walk(tree):
        module = None
        if isinstance(node, ast.Import):
            for item in node.names:
                module = item.name
                candidate = PurePosixPath(*module.split(".")).with_suffix(".py").as_posix()
                if candidate in tracked:
                    targets.add(candidate)
        elif isinstance(node, ast.ImportFrom):
            base = package
            for _ in range(max(node.level - 1, 0)):
                base = base.parent
            if node.module:
                candidate = (base / PurePosixPath(*node.module.split("."))).with_suffix(".py").as_posix()
                if candidate in tracked:
                    targets.add(candidate)
            else:
                for item in node.names:
                    candidate = (base / item.name).with_suffix(".py").as_posix()
                    if candidate in tracked:
                        targets.add(candidate)
    return sorted(targets)


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, default=Path(f"{G6}/B-01"))
    args = parser.parse_args()
    root = args.root.resolve()
    output = (root / args.output_dir).resolve()
    if root not in output.parents:
        raise ValueError("output directory must be within the repository")
    tracked = tracked_files(root)
    frozen_revision = git(root, "rev-parse", "HEAD")
    fragments: list[Fragment] = []
    references: list[dict] = []
    for path, selectors in SEEDS:
        if path not in tracked:
            raise ValueError(f"fixed seed is not a tracked file: {path}")
        raw = (root / path).read_text(encoding="utf-8")
        for selector in selectors:
            selected = heading_fragment(raw, selector, path)
            fragments.append(Fragment(path, selector, selected))
            references.extend(classify(root, tracked, path, match.group(1)) for match in PATH_RE.finditer(selected))
    unique_refs = {(item["declaring_artifact"], item["original_textual_reference"], item["classification"], item.get("normalized_canonical_path")): item for item in references}
    classifications = sorted(unique_refs.values(), key=lambda item: (item["declaring_artifact"], item["original_textual_reference"], item["classification"]))
    # Source roots are only exact canonical paths found in rendered seed fragments.
    # The layer filter is conservative: paths must be explicit L0/L1/L2/L6 source
    # artifacts in G3 §4, never inferred from an unresolved bare reference.
    allowed_prefixes = ("governance/AGENTS.md", "governance/methodology/", "governance/tools/", "governance/schemas/", "governance/validation/", "governance/prompts/", "governance/loops/")
    roots = sorted({item["normalized_canonical_path"] for item in classifications if item["classification"].startswith("EXISTING_") and item["normalized_canonical_path"] and item["normalized_canonical_path"].startswith(allowed_prefixes)})
    closure: dict[str, str] = {}
    queue = [path for path in roots if path.endswith(".py")]
    while queue:
        parent = queue.pop(0)
        for target in direct_imports(root, parent, tracked):
            if target not in roots and target not in closure:
                closure[target] = parent
                queue.append(target)
    members = []
    rendered = [json.dumps({"frozen_revision": frozen_revision, "projection": "GOV-GEN-G6-B-01"}, sort_keys=True)]
    for fragment in fragments:
        source = (root / fragment.path).read_bytes()
        members.append({"kind": "seed_fragment", "path": fragment.path, "selection_rule": fragment.selector, "byte_count": len(source), "sha256": sha256_bytes(source)})
        rendered.extend((f"\n--- seed {fragment.path} {fragment.selector} ---\n", fragment.text))
    for path in sorted(set(roots) | set(closure)):
        source = (root / path).read_text(encoding="utf-8")
        item = {"kind": "source_root" if path in roots else "import_closure", "path": path, "selection_rule": "EXACT_CLASSIFIED_PATH" if path in roots else "PYTHON_IMPORT", "byte_count": len(source.encode()), "sha256": sha256_bytes(source.encode())}
        if path in closure:
            item["importing_parent_path"] = closure[path]
        members.append(item)
        rendered.extend((f"\n--- source {path} ---\n", source))
    rendered_text = "".join(rendered)
    try:
        import tiktoken
    except ModuleNotFoundError as exc:
        raise RuntimeError("tiktoken 0.12.0 is required for B-01 measurement") from exc
    if tiktoken.__version__ != "0.12.0":
        raise RuntimeError(f"tiktoken 0.12.0 is required, found {tiktoken.__version__}")
    tokens = len(tiktoken.get_encoding("cl100k_base").encode(rendered_text, disallowed_special=()))
    manifest = {"document_id": "GOV-GEN-G6-B-01-INPUT-PROJECTION-MANIFEST-001", "status": "B-01_INPUT_PROJECTION_CONSTRUCTED" if tokens <= 20000 else "B-01_INPUT_PROJECTION_REFUSED", "frozen_revision": frozen_revision, "path_resolution": {"order": ["DECLARED_GENERATED_OUTPUT", "REPOSITORY_ROOT", "DECLARER_DIRECTORY", "UNRESOLVED_OR_AMBIGUOUS"], "classifications": classifications}, "members": members, "rendered_projection_sha256": sha256_bytes(rendered_text.encode()), "measurement": {"package": "tiktoken", "version": tiktoken.__version__, "encoding": "cl100k_base", "token_count": tokens, "limit": 20000}}
    output.mkdir(parents=True, exist_ok=True)
    write_json(output / "B-01-input-projection-manifest.yaml", manifest)
    (output / "B-01-input-projection.md").write_text(rendered_text, encoding="utf-8")
    print(json.dumps({"result": manifest["status"], "token_count": tokens, "source_roots": roots, "import_closure": closure}, sort_keys=True))
    return 0 if tokens <= 20000 else 2


if __name__ == "__main__":
    sys.exit(main())
