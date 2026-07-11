#!/usr/bin/env python3
"""Validate a YAML instance against a JSON Schema (draft 2020-12).

Usage:
  schema-validate.py <schema.json> <instance.yaml>   # full validation
  schema-validate.py --parse-only <instance.yaml>    # YAML well-formedness +
                                                     # top-level mapping check

Exit codes: 0 valid · 1 invalid · 2 operational error (missing file, unreadable
YAML/JSON, invalid schema).

YAML dates/datetimes are converted to ISO strings before validation, because
JSON Schema has no date type and YAML parses bare dates as date objects.
"""
import datetime
import json
import sys


def _dates_to_strings(node):
    if isinstance(node, dict):
        return {k: _dates_to_strings(v) for k, v in node.items()}
    if isinstance(node, list):
        return [_dates_to_strings(v) for v in node]
    if isinstance(node, (datetime.date, datetime.datetime)):
        return node.isoformat()
    return node


def _load_yaml(path):
    import yaml
    try:
        with open(path, encoding="utf-8") as fh:
            return _dates_to_strings(yaml.safe_load(fh))
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        sys.exit(2)
    except yaml.YAMLError as exc:
        print(f"ERROR: {path} is not well-formed YAML: {exc}", file=sys.stderr)
        sys.exit(2)


def main(argv):
    if len(argv) == 3 and argv[1] == "--parse-only":
        data = _load_yaml(argv[2])
        if not isinstance(data, dict):
            print(f"INVALID: {argv[2]}: top level must be a mapping",
                  file=sys.stderr)
            return 1
        return 0

    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2

    schema_path, instance_path = argv[1], argv[2]
    try:
        import jsonschema
    except ImportError:
        print("ERROR: python module 'jsonschema' is not installed.\n"
              "Fix: pacman -S python-jsonschema  (or: python3 -m pip install "
              "--user --break-system-packages jsonschema)", file=sys.stderr)
        return 2

    try:
        with open(schema_path, encoding="utf-8") as fh:
            schema = json.load(fh)
    except FileNotFoundError:
        print(f"ERROR: schema not found: {schema_path}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: schema {schema_path} is not valid JSON: {exc}",
              file=sys.stderr)
        return 2

    validator_cls = jsonschema.validators.validator_for(schema)
    try:
        validator_cls.check_schema(schema)
    except jsonschema.SchemaError as exc:
        print(f"ERROR: schema {schema_path} is not a valid JSON Schema: "
              f"{exc.message}", file=sys.stderr)
        return 2

    instance = _load_yaml(instance_path)
    errors = sorted(validator_cls(schema).iter_errors(instance),
                    key=lambda e: list(e.absolute_path))
    if errors:
        for err in errors:
            path = "/".join(str(p) for p in err.absolute_path) or "(root)"
            print(f"INVALID: {instance_path}: at {path}: {err.message}",
                  file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
