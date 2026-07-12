#!/usr/bin/env bash
# status.sh — derived, read-only client-project dashboard (02 §8, DEC-11).
#
# v0 (S0b): stage + stage status, latest gate state per gate (from the
# append-only docs/handoffs/ records, R2-05), requirement status histogram,
# open question / contradiction counts, profile + pending risk triggers.
# Later stages extend the same script (LITE task board arrives with the
# delivery backlog at S3; --methodology staleness flags with knowledge, 17 §E).
#
# This script derives everything live and WRITES NOTHING — per-artifact
# statuses live in the artifacts; project.yaml deliberately stores none of
# what is printed here (one source of truth per fact).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"

usage() {
  cat <<'EOF'
Usage: status.sh [client-dir]

Prints the derived project dashboard. client-dir defaults to the current
working directory. Read-only: no file is created or modified.

Environment: PYTHON overrides the python3 binary.
Exit codes: 0 report printed · 2 usage/operational error.
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then usage; exit 0; fi
if [[ $# -gt 1 ]]; then echo "ERROR: too many arguments" >&2; usage >&2; exit 2; fi

CLIENT_DIR="${1:-$PWD}"
if [[ ! -d "$CLIENT_DIR" ]]; then
  echo "ERROR: client directory not found: $CLIENT_DIR" >&2; exit 2
fi
CLIENT_DIR="$(cd "$CLIENT_DIR" && pwd)"

if ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "ERROR: python3 is required. Install python3." >&2
  exit 2
fi

exec "$PYTHON" "$SCRIPT_DIR/lib/derive-status.py" "$CLIENT_DIR"
