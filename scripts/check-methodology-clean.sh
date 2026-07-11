#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: check-methodology-clean.sh [methodology-dir]

Exit non-zero when the methodology checkout has staged, unstaged, or untracked
changes. Defaults to the repository containing this script.
EOF
}

if [[ ${1:-} == "--help" || ${1:-} == "-h" ]]; then
  usage
  exit 0
fi
if (( $# > 1 )); then
  usage >&2
  exit 2
fi

default_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
method_arg="${1:-$default_dir}"
if [[ ! -d "$method_arg" ]]; then
  echo "ERROR: methodology directory does not exist: $method_arg" >&2
  exit 1
fi
method_dir="$(cd "$method_arg" && pwd -P)"
if ! git -C "$method_dir" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: methodology directory is not a Git worktree: $method_dir" >&2
  exit 1
fi

state="$(git -C "$method_dir" status --porcelain --untracked-files=all)"
if [[ -n "$state" ]]; then
  echo "ERROR: methodology checkout is dirty; client sessions would not match the locked commit:" >&2
  printf '%s\n' "$state" >&2
  echo "Commit, stash, or intentionally remove these changes before launch." >&2
  exit 1
fi

echo "PASS: methodology checkout is clean: $method_dir"
