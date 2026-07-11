#!/usr/bin/env python3
"""Validate YAML/JSON with the JSON Schema subset used by S0a.

The progressive shell entrypoint remains scripts/validate.sh. This dependency-
light adapter is extended only when a later-stage schema needs another draft
2020-12 keyword.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - exercised as an environment error
    raise SystemExit("PyYAML is required: install it with 'python3 -m pip install PyYAML'.") from exc


class JsonCompatibleSafeLoader(yaml.SafeLoader):
    """Keep ISO dates as strings so YAML instances map cleanly to JSON types."""


JsonCompatibleSafeLoader.yaml_implicit_resolvers = {
    key: [
        (tag, pattern)
        for tag, pattern in resolvers
        if tag != "tag:yaml.org,2002:timestamp"
    ]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


class ValidationError(Exception):
    pass


def load_document(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValidationError(f"cannot read {path}: {exc}") from exc
    try:
        if path.suffix.lower() == ".json":
            return json.loads(text)
        return yaml.load(text, Loader=JsonCompatibleSafeLoader)
    except (json.JSONDecodeError, yaml.YAMLError) as exc:
        raise ValidationError(f"syntax error in {path}: {exc}") from exc


def type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    raise ValidationError(f"schema uses unsupported type {expected!r}")


class Validator:
    def __init__(self, root_schema: dict[str, Any]) -> None:
        self.root = root_schema
        self.errors: list[str] = []

    def resolve_ref(self, reference: str) -> dict[str, Any]:
        if not reference.startswith("#/"):
            raise ValidationError(f"only local $ref values are supported at S0a: {reference}")
        node: Any = self.root
        for raw_part in reference[2:].split("/"):
            part = raw_part.replace("~1", "/").replace("~0", "~")
            if not isinstance(node, dict) or part not in node:
                raise ValidationError(f"unresolvable $ref: {reference}")
            node = node[part]
        if not isinstance(node, dict):
            raise ValidationError(f"$ref does not select a schema object: {reference}")
        return node

    def check(self, value: Any, schema: dict[str, Any], path: str = "$") -> None:
        if "$ref" in schema:
            self.check(value, self.resolve_ref(schema["$ref"]), path)

        if "oneOf" in schema:
            matches = 0
            branch_errors: list[list[str]] = []
            for branch in schema["oneOf"]:
                child = Validator(self.root)
                child.check(value, branch, path)
                if not child.errors:
                    matches += 1
                branch_errors.append(child.errors)
            if matches != 1:
                detail = "; ".join(errors[0] for errors in branch_errors if errors)
                self.errors.append(f"{path}: must match exactly one allowed shape ({detail})")
                return

        if "const" in schema and value != schema["const"]:
            self.errors.append(f"{path}: expected constant {schema['const']!r}, got {value!r}")
        if "enum" in schema and value not in schema["enum"]:
            self.errors.append(f"{path}: {value!r} is not one of {schema['enum']!r}")

        expected = schema.get("type")
        if expected is not None:
            allowed = [expected] if isinstance(expected, str) else expected
            if not any(type_matches(value, item) for item in allowed):
                self.errors.append(f"{path}: expected type {allowed!r}, got {type(value).__name__}")
                return

        if isinstance(value, dict):
            required = schema.get("required", [])
            for key in required:
                if key not in value:
                    self.errors.append(f"{path}: missing required property {key!r}")
            properties = schema.get("properties", {})
            for key, item in value.items():
                child_path = f"{path}.{key}"
                if key in properties:
                    self.check(item, properties[key], child_path)
                elif schema.get("additionalProperties") is False:
                    self.errors.append(f"{child_path}: additional property is not allowed")
                elif isinstance(schema.get("additionalProperties"), dict):
                    self.check(item, schema["additionalProperties"], child_path)
            if len(value) < schema.get("minProperties", 0):
                self.errors.append(f"{path}: has fewer than {schema['minProperties']} properties")

        if isinstance(value, list):
            if len(value) < schema.get("minItems", 0):
                self.errors.append(f"{path}: has fewer than {schema['minItems']} items")
            if "maxItems" in schema and len(value) > schema["maxItems"]:
                self.errors.append(f"{path}: has more than {schema['maxItems']} items")
            if schema.get("uniqueItems"):
                encoded = [json.dumps(item, sort_keys=True, ensure_ascii=False) for item in value]
                if len(encoded) != len(set(encoded)):
                    self.errors.append(f"{path}: items must be unique")
            if isinstance(schema.get("items"), dict):
                for index, item in enumerate(value):
                    self.check(item, schema["items"], f"{path}[{index}]")

        if isinstance(value, str):
            if len(value) < schema.get("minLength", 0):
                self.errors.append(f"{path}: string is shorter than {schema['minLength']}")
            if "maxLength" in schema and len(value) > schema["maxLength"]:
                self.errors.append(f"{path}: string is longer than {schema['maxLength']}")
            if "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
                self.errors.append(f"{path}: {value!r} does not match /{schema['pattern']}/")
            if schema.get("format") == "date":
                try:
                    dt.date.fromisoformat(value)
                except ValueError:
                    self.errors.append(f"{path}: {value!r} is not an ISO date")

        if isinstance(value, (int, float)) and not isinstance(value, bool):
            if "minimum" in schema and value < schema["minimum"]:
                self.errors.append(f"{path}: {value} is below minimum {schema['minimum']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a YAML/JSON instance against an S0a JSON Schema.")
    parser.add_argument("schema", type=Path)
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()

    try:
        schema = load_document(args.schema)
        instance = load_document(args.instance)
        if not isinstance(schema, dict):
            raise ValidationError("schema root must be an object")
        validator = Validator(schema)
        validator.check(instance, schema)
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if validator.errors:
        for error in validator.errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"PASS: {args.instance} conforms to {args.schema.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
