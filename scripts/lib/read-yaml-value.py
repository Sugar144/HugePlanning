#!/usr/bin/env python3
"""Print a scalar value from a YAML file by dotted path.

Usage: read-yaml-value.py <file.yaml> <dotted.path>
Example: read-yaml-value.py methodology.lock.yaml methodology.commit

Exit codes: 0 found · 1 path missing or not a scalar · 2 operational error.
"""
import datetime
import sys

import yaml


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    path, dotted = argv[1], argv[2]
    try:
        with open(path, encoding="utf-8") as fh:
            node = yaml.safe_load(fh)
    except (OSError, yaml.YAMLError) as exc:
        print(f"ERROR: cannot read {path}: {exc}", file=sys.stderr)
        return 2
    for key in dotted.split("."):
        if not isinstance(node, dict) or key not in node:
            print(f"ERROR: path '{dotted}' not found in {path}",
                  file=sys.stderr)
            return 1
        node = node[key]
    if isinstance(node, (dict, list)):
        print(f"ERROR: path '{dotted}' in {path} is not a scalar",
              file=sys.stderr)
        return 1
    if isinstance(node, (datetime.date, datetime.datetime)):
        node = node.isoformat()
    print(node)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
