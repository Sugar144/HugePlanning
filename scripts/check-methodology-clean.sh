#!/usr/bin/env bash
# check-methodology-clean.sh — refuse to work from a dirty methodology (02 §6).
#
# A dirty methodology means the locked commit is NOT what client sessions are
# actually loading; it can also indicate that a client session wrote into the
# methodology (deny rules do not bind arbitrary subprocesses — 02 §6).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
METHOD_DIR="${METHODOLOGY_DIR:-$(dirname "$SCRIPT_DIR")}"

usage() {
  cat <<'EOF'
Usage: check-methodology-clean.sh

Exits 0 when the methodology repository has no uncommitted changes; exits 1
(with the offending paths) when it is dirty. Run it any time; start-agent.sh
runs it before every launch.

Environment: METHODOLOGY_DIR overrides the methodology location (defaults to
the repository containing this script).
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then usage; exit 0; fi
if [[ $# -gt 0 ]]; then echo "ERROR: unexpected argument: $1" >&2; usage >&2; exit 2; fi

if ! command -v git >/dev/null 2>&1; then
  echo "ERROR: git is required" >&2; exit 2
fi
if ! git -C "$METHOD_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: not a git repository: $METHOD_DIR" >&2
  echo "The methodology must be a git checkout (02 §1)." >&2
  exit 2
fi

status="$(git -C "$METHOD_DIR" status --porcelain)"
if [[ -n "$status" ]]; then
  echo "DIRTY: methodology at $METHOD_DIR has uncommitted changes:" >&2
  printf '%s\n' "$status" >&2
  cat >&2 <<'EOF'
Do not launch client sessions from a dirty methodology. Fix:
  - if these are your own methodology edits: commit or stash them, then retry;
  - if you did NOT make these changes: a client session may have written into
    the methodology — investigate before discarding anything (02 §6).
EOF
  exit 1
fi

echo "CLEAN: methodology at $METHOD_DIR ($(git -C "$METHOD_DIR" rev-parse --short=7 HEAD))"
