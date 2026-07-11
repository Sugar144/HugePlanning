#!/usr/bin/env python3
"""Check that a client .claude/settings.json denies writes to the methodology.

Usage: check-deny-rules.py <settings.json> <methodology-dir>

Verifies the file is valid JSON and that permissions.deny contains both
"Write(/<methodology-dir>/**)" and "Edit(/<methodology-dir>/**)" (absolute-path
deny rule syntax verified in plan 19 §0). The rule may name the methodology
directory either as given (logical path, what new-client.sh writes) or fully
resolved (physical path) — both are accepted so a symlinked methodology
location does not false-fail.

Exit codes: 0 ok · 1 rule missing or wrong path · 2 operational error.
"""
import json
import os
import sys


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    settings_path = argv[1]
    given = os.path.abspath(argv[2])
    candidates = {given, os.path.realpath(argv[2])}
    try:
        with open(settings_path, encoding="utf-8") as fh:
            settings = json.load(fh)
    except FileNotFoundError:
        print(f"ERROR: settings file not found: {settings_path}",
              file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: {settings_path} is not valid JSON: {exc}",
              file=sys.stderr)
        return 2

    deny = settings.get("permissions", {}).get("deny", [])
    if not isinstance(deny, list):
        print(f"ERROR: {settings_path}: permissions.deny is not a list",
              file=sys.stderr)
        return 1

    ok = True
    for tool in ("Write", "Edit"):
        accepted = {f"{tool}(/{c}/**)" for c in candidates}
        if not accepted & set(deny):
            print(f"MISSING deny rule in {settings_path}: "
                  f"{tool}(/{given}/**)", file=sys.stderr)
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
