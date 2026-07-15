#!/usr/bin/env python3
"""Manage HugePlanning governance learning records (v0.1.0).

Read-only dry-run is the default. Only ``record``, ``event``, and ``index``
accept ``--apply``. The tool is offline, deterministic, and never mutates Git.

Exit codes: 0 valid/success; 1 contract failure; 2 usage/operational failure;
3 incident or explicit owner-decision routing required.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
import unicodedata

try:
    import jsonschema
    import yaml
except ImportError as exc:  # pragma: no cover - operational environment
    print(f"ERROR: required existing dependency unavailable: {exc}", file=sys.stderr)
    raise SystemExit(2)

TOOL_VERSION = "0.1.0"
RECORD_RE = re.compile(r"^HP-FAIL-(\d{3})$")
EVENT_RE = re.compile(r"^(HP-FAIL-(\d{3}))-E(\d{3})$")
STATUS_EDGES = {
    "OPEN": {"CONTAINED", "ACCEPTED_RISK"},
    "CONTAINED": {"CORRECTED", "ACCEPTED_RISK"},
    "CORRECTED": {"VALIDATED", "ACCEPTED_RISK"},
    "VALIDATED": set(),
    "ACCEPTED_RISK": {"OPEN"},
}
STATUS_EVENTS = {"STATUS_TRANSITION", "RISK_ACCEPTANCE", "RISK_EXPIRY_OR_REOPENING", "VALIDATION_EVIDENCE"}


class ContractError(Exception):
    """A deterministic contract violation (exit 1)."""


class RoutingRequired(Exception):
    """Human incident/owner routing is required (exit 3)."""


class StrictLoader(yaml.SafeLoader):
    pass


def _construct_mapping(loader: StrictLoader, node: yaml.nodes.MappingNode, deep: bool = False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping", node.start_mark,
                f"duplicate YAML key: {key!r}", key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)


def dates_to_strings(value):
    if isinstance(value, dict):
        return {key: dates_to_strings(item) for key, item in value.items()}
    if isinstance(value, list):
        return [dates_to_strings(item) for item in value]
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()
    return value


def load_yaml(path: Path):
    try:
        with path.open(encoding="utf-8") as handle:
            return dates_to_strings(yaml.load(handle, Loader=StrictLoader))
    except FileNotFoundError as exc:
        raise OSError(f"file not found: {path}") from exc
    except UnicodeDecodeError as exc:
        raise ContractError(f"UTF-8 required: {path}: {exc}") from exc
    except yaml.YAMLError as exc:
        raise ContractError(f"invalid YAML: {path}: {exc}") from exc


def load_schema(path: Path):
    try:
        with path.open(encoding="utf-8") as handle:
            schema = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise OSError(f"cannot load schema {path}: {exc}") from exc
    validator_cls = jsonschema.validators.validator_for(schema)
    try:
        validator_cls.check_schema(schema)
    except jsonschema.SchemaError as exc:
        raise OSError(f"invalid JSON Schema {path}: {exc.message}") from exc
    return validator_cls(schema, format_checker=jsonschema.FormatChecker())


def schema_validate(validator, data, label: str):
    errors = sorted(validator.iter_errors(data), key=lambda err: [str(x) for x in err.absolute_path])
    if errors:
        details = []
        for error in errors:
            path = "/".join(str(part) for part in error.absolute_path) or "(root)"
            details.append(f"{label}: {path}: {error.message}")
        raise ContractError("schema validation failed:\n" + "\n".join(details))


def canonical_json(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def normalized(value: str) -> str:
    text = unicodedata.normalize("NFKC", value).casefold()
    return " ".join(text.split())


def fingerprint(record: dict) -> str:
    evidence = sorted(normalized(item["locator"]) for item in record["evidence_refs"])
    material = {
        "component": normalized(record["context"]["component"]),
        "primary_classification": record["primary_classification"],
        "expected_behavior": normalized(record["expected_behavior"]),
        "observed_behavior": normalized(record["observed_behavior"]),
        "systemic": normalized(record["root_cause"]["systemic"]),
        "evidence": evidence,
    }
    return hashlib.sha256(canonical_json(material)).hexdigest()


def safe_repository_locator(root: Path, locator: str) -> Path:
    if "\\" in locator:
        raise ContractError(f"ambiguous repository evidence path: {locator}")
    pure = PurePosixPath(locator)
    if pure.is_absolute() or not pure.parts or any(part in ("", ".", "..") for part in pure.parts):
        raise ContractError(f"repository evidence path escapes root: {locator}")
    candidate = (root / Path(*pure.parts)).resolve(strict=False)
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ContractError(f"repository evidence path escapes root: {locator}") from exc
    return candidate


def validate_evidence(root: Path, evidence_refs: list[dict], label: str):
    for pos, evidence in enumerate(evidence_refs):
        if evidence["type"] == "REPOSITORY_PATH":
            candidate = safe_repository_locator(root, evidence["locator"])
            if evidence["availability"] == "PRESERVED" and not candidate.exists():
                raise ContractError(f"{label} evidence {pos} is not preserved at {evidence['locator']}")
        if evidence["type"] == "COMMIT" and not re.fullmatch(r"[0-9a-f]{40}", evidence["locator"]):
            raise ContractError(f"{label} evidence {pos} commit locator must be a full SHA")


def root_paths():
    root = Path(__file__).resolve().parents[2]
    governance = root / "governance"
    return {
        "root": root,
        "governance": governance,
        "records": governance / "learning" / "records",
        "events": governance / "learning" / "events",
        "index": governance / "learning" / "FAILURE_AND_LESSONS_INDEX.md",
        "record_schema": governance / "schemas" / "failure-record.schema.json",
        "event_schema": governance / "schemas" / "failure-record-event.schema.json",
    }


def validated_base_mutation(root: Path, path: Path, data: dict):
    try:
        rel = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return
    result = subprocess.run(
        ["git", "-C", str(root), "show", f"HEAD:{rel}"],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False,
    )
    if result.returncode == 0:
        try:
            committed = dates_to_strings(yaml.load(result.stdout.decode("utf-8"), Loader=StrictLoader))
        except (UnicodeDecodeError, yaml.YAMLError) as exc:
            raise ContractError(f"cannot inspect committed base record for immutability: {rel}: {exc}") from exc
        committed_status = committed.get("failure_record", {}).get("status") if isinstance(committed, dict) else None
        if committed_status == "VALIDATED" and result.stdout != path.read_bytes():
            raise ContractError(f"direct mutation of validated base record detected: {rel}")


def validate_record_semantics(root: Path, record: dict, label: str):
    if record["primary_classification"] not in record["classification"]:
        raise ContractError(f"primary classification absent from classification: {label}")
    validate_evidence(root, record["evidence_refs"], label)
    for pos, subfinding in enumerate(record["subfindings"]):
        validate_evidence(root, subfinding["evidence_refs"], f"{label} subfinding {pos}")
    if record["metrics"]["measurement_quality"] == "UNAVAILABLE":
        numeric = ("exact_token_usage", "model_runs", "human_time_minutes", "correction_cycles", "deterministic_rework_count", "package_rebuild_count")
        if any(record["metrics"][field] is not None for field in numeric) or record["metrics"]["model_and_reasoning"]:
            raise ContractError(f"UNAVAILABLE metrics must not contain fabricated values: {label}")
    if record["status"] == "ACCEPTED_RISK":
        if record["accepted_risk"] is None:
            raise ContractError(f"accepted-risk record lacks bounded risk data: {label}")
        owner_refs = [e for e in record["evidence_refs"] if e["type"] in ("OWNER_STATEMENT", "DECISION") and e["availability"] == "PRESERVED"]
        if not owner_refs:
            raise ContractError(f"accepted-risk record lacks preserved owner evidence: {label}")
        risk = record["accepted_risk"]
        if risk["review_on"] is None and not risk["no_review_date_rationale"]:
            raise ContractError(f"accepted-risk record lacks review date rationale: {label}")
    elif record["accepted_risk"] is not None:
        raise ContractError(f"accepted_risk details require ACCEPTED_RISK status: {label}")


def load_all(paths: dict, record_validator, event_validator):
    records: dict[str, dict] = {}
    record_files: dict[str, Path] = {}
    for path in sorted(paths["records"].glob("*.yaml")):
        data = load_yaml(path)
        schema_validate(record_validator, data, str(path))
        record = data["failure_record"]
        record_id = record["id"]
        if record_id in records:
            raise ContractError(f"duplicate record ID: {record_id}")
        if path.name != f"{record_id}.yaml":
            raise ContractError(f"record filename/ID mismatch: {path}")
        validate_record_semantics(paths["root"], record, record_id)
        validated_base_mutation(paths["root"], path, data)
        records[record_id] = record
        record_files[record_id] = path

    fingerprints: dict[str, str] = {}
    for record_id, record in records.items():
        value = fingerprint(record)
        if value in fingerprints:
            raise ContractError(f"exact normalized fingerprint collision: {fingerprints[value]} and {record_id}")
        fingerprints[value] = record_id

    events: dict[str, list[dict]] = {record_id: [] for record_id in records}
    seen_event_ids = set()
    for path in sorted(paths["events"].glob("*/*.yaml")):
        data = load_yaml(path)
        schema_validate(event_validator, data, str(path))
        event = data["failure_record_event"]
        event_id = event["id"]
        match = EVENT_RE.fullmatch(event_id)
        if not match or event["record_id"] != match.group(1):
            raise ContractError(f"event ID/record ID mismatch: {event_id}")
        if path.parent.name != event["record_id"] or path.name != f"{event_id}.yaml":
            raise ContractError(f"event path/ID mismatch: {path}")
        if event["record_id"] not in records:
            raise ContractError(f"event references missing record: {event_id}")
        if event_id in seen_event_ids:
            raise ContractError(f"duplicate event ID: {event_id}")
        seen_event_ids.add(event_id)
        validate_evidence(paths["root"], event["evidence_refs"], event_id)
        events[event["record_id"]].append(event)

    effective = {}
    for record_id, record_events in events.items():
        ordered = sorted(record_events, key=lambda event: int(EVENT_RE.fullmatch(event["id"]).group(3)))
        for expected, event in enumerate(ordered, 1):
            actual = int(EVENT_RE.fullmatch(event["id"]).group(3))
            if actual != expected:
                raise ContractError(f"invalid event numbering for {record_id}: expected E{expected:03d}, got E{actual:03d}")
        effective[record_id] = replay(records[record_id], ordered)
        events[record_id] = ordered
    return records, events, effective, fingerprints


def replay(record: dict, events: list[dict]) -> str:
    status = record["status"]
    for event in events:
        source = event["status_from"]
        target = event["status_to"]
        event_type = event["event_type"]
        if target is None:
            if source is not None:
                raise ContractError(f"non-transition event has status_from: {event['id']}")
            continue
        if event_type not in STATUS_EVENTS:
            raise ContractError(f"event type cannot change status: {event['id']}")
        if source != status:
            raise ContractError(f"status replay mismatch for {event['id']}: expected {status}, got {source}")
        if target not in STATUS_EDGES[status]:
            raise ContractError(f"invalid status transition for {event['id']}: {status} -> {target}")
        if target == "ACCEPTED_RISK":
            require_owner_risk_evidence(event)
        if event_type == "RISK_EXPIRY_OR_REOPENING" and not (status == "ACCEPTED_RISK" and target == "OPEN"):
            raise ContractError(f"risk reopening event must transition ACCEPTED_RISK -> OPEN: {event['id']}")
        status = target
    return status


def require_owner_risk_evidence(event: dict):
    if not event["owner_decision_ref"] or event["accepted_risk"] is None:
        raise ContractError(f"accepted-risk event lacks owner decision or risk bounds: {event['id']}")
    owner_refs = [e for e in event["evidence_refs"] if e["type"] in ("OWNER_STATEMENT", "DECISION") and e["availability"] == "PRESERVED"]
    if not owner_refs:
        raise ContractError(f"accepted-risk event lacks preserved owner evidence: {event['id']}")
    risk = event["accepted_risk"]
    if risk["review_on"] is None and not risk["no_review_date_rationale"]:
        raise ContractError(f"accepted-risk event lacks review date rationale: {event['id']}")


def input_digest(records: dict, events: dict) -> str:
    source = {
        "records": [records[key] for key in sorted(records, key=id_number)],
        "events": [event for key in sorted(events, key=id_number) for event in events[key]],
    }
    return hashlib.sha256(canonical_json(source)).hexdigest()


def id_number(record_id: str) -> int:
    return int(RECORD_RE.fullmatch(record_id).group(1))


def index_bytes(records: dict, events: dict, effective: dict) -> bytes:
    digest = input_digest(records, events)
    lines = [
        "# Failure and Lessons Index",
        "",
        "> GENERATED FILE — source of truth: `records/` plus append-only `events/`.",
        f"> Tool version: `{TOOL_VERSION}`. Deterministic input digest: `{digest}`.",
        "> Manual edits will be overwritten by `--apply` or rejected as generated-view drift.",
        "",
        "| ID | Date | Title | Primary classification | Severity | Effective status | Component | Phase/run | Owner decision required | Measurement quality | Reusable lesson |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for record_id in sorted(records, key=id_number):
        record = records[record_id]
        values = [
            record_id, record["date"], record["title"], record["primary_classification"],
            record["severity"], effective[record_id], record["context"]["component"],
            f"{record['context']['phase']}/{record['context']['run'] or 'none'}",
            "yes" if record["owner_decision_required"] else "no",
            record["metrics"]["measurement_quality"], record["learning"]["reusable_lesson"],
        ]
        escaped = [str(value).replace("|", "\\|").replace("\n", " ") for value in values]
        lines.append("| " + " | ".join(escaped) + " |")
    return ("\n".join(lines) + "\n").encode("utf-8")


def atomic_write(target: Path, content: bytes, *, immutable: bool):
    target.parent.mkdir(parents=True, exist_ok=True)
    if immutable and target.exists():
        raise ContractError(f"immutable target exists: {target}")
    descriptor = None
    temporary = None
    try:
        descriptor, name = tempfile.mkstemp(prefix=f".{target.name}.", suffix=".tmp", dir=target.parent)
        temporary = Path(name)
        with os.fdopen(descriptor, "wb") as handle:
            descriptor = None
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        if os.environ.get("HP_LEARNING_TEST_FAIL_ATOMIC") == "before_replace":
            raise OSError("injected atomic-write failure")
        if immutable and target.exists():
            raise ContractError(f"immutable target appeared during write: {target}")
        os.replace(temporary, target)
        temporary = None
        directory_fd = os.open(target.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def yaml_bytes(data: dict) -> bytes:
    text = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False)
    return text.encode("utf-8")


def report(action: str, applied: bool, **extra):
    payload = {"action": action, "applied": applied, "tool_version": TOOL_VERSION}
    payload.update(extra)
    sys.stdout.buffer.write(canonical_json(payload))


def command_validate(args, paths, record_validator, event_validator):
    if args.record:
        path = Path(args.record).resolve()
        data = load_yaml(path)
        schema_validate(record_validator, data, str(path))
        record = data["failure_record"]
        validate_record_semantics(paths["root"], record, record["id"])
        report("validate-record", False, valid=True, record_id=record["id"])
        return
    records, events, effective, _ = load_all(paths, record_validator, event_validator)
    expected = index_bytes(records, events, effective)
    if not paths["index"].exists() or paths["index"].read_bytes() != expected:
        raise ContractError("generated index drift detected")
    report("validate", False, valid=True, records=len(records), events=sum(map(len, events.values())), input_digest=input_digest(records, events))


def next_record_id(records: dict) -> str:
    highest = max((id_number(record_id) for record_id in records), default=0)
    if highest >= 999:
        raise ContractError("record ID space exhausted")
    return f"HP-FAIL-{highest + 1:03d}"


def command_record(args, paths, record_validator, event_validator):
    records, events, effective, fingerprints = load_all(paths, record_validator, event_validator)
    data = load_yaml(Path(args.input).resolve())
    if not isinstance(data, dict) or not isinstance(data.get("failure_record"), dict):
        raise ContractError("record draft must contain failure_record mapping")
    record = data["failure_record"]
    allocated = next_record_id(records)
    supplied = record.get("id")
    if supplied not in (None, allocated):
        raise ContractError(f"new record ID must be null/omitted or next monotonic ID {allocated}")
    record["id"] = allocated
    schema_validate(record_validator, data, str(args.input))
    validate_record_semantics(paths["root"], record, allocated)
    if record["owner_decision_required"]:
        raise RoutingRequired("explicit owner decision required before record mutation")
    value = fingerprint(record)
    if value in fingerprints:
        raise ContractError(f"exact normalized fingerprint collision with {fingerprints[value]}")
    overlaps = []
    candidate_evidence = {normalized(item["locator"]) for item in record["evidence_refs"]}
    for record_id, current in records.items():
        same_component = normalized(current["context"]["component"]) == normalized(record["context"]["component"])
        same_systemic = normalized(current["root_cause"]["systemic"]) == normalized(record["root_cause"]["systemic"])
        shared = candidate_evidence & {normalized(item["locator"]) for item in current["evidence_refs"]}
        if same_component and same_systemic and shared:
            overlaps.append(record_id)
    target = paths["records"] / f"{allocated}.yaml"
    if args.apply:
        atomic_write(target, yaml_bytes(data), immutable=True)
    report("record", args.apply, record_id=allocated, path=target.relative_to(paths["root"]).as_posix(), fingerprint=value, overlap_warnings=overlaps)


def next_event_id(record_id: str, events: dict) -> str:
    return f"{record_id}-E{len(events[record_id]) + 1:03d}"


def command_event(args, paths, record_validator, event_validator):
    records, events, effective, _ = load_all(paths, record_validator, event_validator)
    data = load_yaml(Path(args.input).resolve())
    if not isinstance(data, dict) or not isinstance(data.get("failure_record_event"), dict):
        raise ContractError("event draft must contain failure_record_event mapping")
    event = data["failure_record_event"]
    record_id = event.get("record_id")
    if record_id not in records:
        raise ContractError(f"event references missing record: {record_id}")
    allocated = next_event_id(record_id, events)
    supplied = event.get("id")
    if supplied not in (None, allocated):
        raise ContractError(f"new event ID must be null/omitted or next event ID {allocated}")
    event["id"] = allocated
    schema_validate(event_validator, data, str(args.input))
    validate_evidence(paths["root"], event["evidence_refs"], allocated)
    replay(records[record_id], events[record_id] + [event])
    target = paths["events"] / record_id / f"{allocated}.yaml"
    if args.apply:
        atomic_write(target, yaml_bytes(data), immutable=True)
    report("event", args.apply, event_id=allocated, record_id=record_id, path=target.relative_to(paths["root"]).as_posix())


def command_index(args, paths, record_validator, event_validator):
    records, events, effective, _ = load_all(paths, record_validator, event_validator)
    content = index_bytes(records, events, effective)
    drift = not paths["index"].exists() or paths["index"].read_bytes() != content
    if args.apply:
        atomic_write(paths["index"], content, immutable=False)
    elif drift:
        report("index", False, drift=True, input_digest=input_digest(records, events))
        raise ContractError("generated index drift detected; review then use index --apply")
    report("index", args.apply, drift=drift, input_digest=input_digest(records, events), records=len(records))


def parser():
    main = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = main.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate", help="validate all records/events/index or one record")
    validate.add_argument("--record", metavar="PATH")
    record = sub.add_parser("record", help="validate/allocate a new immutable base record")
    record.add_argument("--input", required=True, metavar="DRAFT.yaml")
    record.add_argument("--apply", action="store_true")
    event = sub.add_parser("event", help="validate/allocate a new append-only event")
    event.add_argument("--input", required=True, metavar="EVENT.yaml")
    event.add_argument("--apply", action="store_true")
    index = sub.add_parser("index", help="check or deterministically regenerate the Markdown index")
    index.add_argument("--apply", action="store_true")
    return main


def main(argv=None):
    args = parser().parse_args(argv)
    paths = root_paths()
    try:
        record_validator = load_schema(paths["record_schema"])
        event_validator = load_schema(paths["event_schema"])
        if args.command == "validate":
            command_validate(args, paths, record_validator, event_validator)
        elif args.command == "record":
            command_record(args, paths, record_validator, event_validator)
        elif args.command == "event":
            command_event(args, paths, record_validator, event_validator)
        elif args.command == "index":
            command_index(args, paths, record_validator, event_validator)
        return 0
    except RoutingRequired as exc:
        print(f"ROUTING_REQUIRED: {exc}", file=sys.stderr)
        return 3
    except ContractError as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
