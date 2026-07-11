#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: start-agent.sh <client-dir> <agent> [--resume]

Validate the client and locked methodology, then launch Claude Code with the
methodology passed via --add-dir and its CLAUDE.md/rules loading enabled.
EOF
}

if [[ ${1:-} == "--help" || ${1:-} == "-h" ]]; then
  usage
  exit 0
fi
if (( $# < 2 || $# > 3 )); then
  usage >&2
  exit 2
fi

client_arg="$1"
agent="$2"
resume="${3:-}"
if [[ -n "$resume" && "$resume" != "--resume" ]]; then
  echo "ERROR: third argument must be --resume when provided; got '$resume'." >&2
  exit 2
fi
if [[ ! "$agent" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
  echo "ERROR: invalid agent name '$agent'; use lowercase letters, digits, and hyphens." >&2
  exit 2
fi
if [[ ! -d "$client_arg" ]]; then
  echo "ERROR: client directory does not exist: $client_arg" >&2
  exit 1
fi

method_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
client_dir="$(cd "$client_arg" && pwd -P)"
if [[ "$client_dir" == "$method_dir" ]]; then
  echo "ERROR: client directory cannot be the methodology repository." >&2
  exit 1
fi
git -C "$client_dir" rev-parse --is-inside-work-tree >/dev/null 2>&1 || {
  echo "ERROR: client directory is not a Git worktree: $client_dir" >&2
  exit 1
}
if [[ ! -f "$method_dir/.claude/agents/$agent.md" ]]; then
  echo "ERROR: agent '$agent' is not defined at $method_dir/.claude/agents/$agent.md" >&2
  exit 1
fi

"$method_dir/scripts/validate.sh" "$client_dir"
"$method_dir/scripts/check-methodology-clean.sh" "$method_dir"

lock_values="$(python3 - "$client_dir/methodology.lock.yaml" <<'PY'
import sys
try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required: python3 -m pip install PyYAML")
with open(sys.argv[1], encoding="utf-8") as handle:
    lock = yaml.safe_load(handle)
method = lock["methodology"]
print(method["version"])
print(method["commit"])
PY
)"
locked_version="$(sed -n '1p' <<<"$lock_values")"
locked_commit="$(sed -n '2p' <<<"$lock_values")"
current_version="$(tr -d '[:space:]' < "$method_dir/VERSION")"
current_commit="$(git -C "$method_dir" rev-parse HEAD)"
if [[ "$locked_version" != "$current_version" ]]; then
  echo "ERROR: lock version $locked_version does not match checkout VERSION $current_version." >&2
  exit 1
fi
if [[ "$locked_commit" != "$current_commit" ]]; then
  echo "ERROR: lock commit $locked_commit does not match methodology HEAD $current_commit." >&2
  echo "Checkout the locked commit or intentionally upgrade the lock before launch." >&2
  exit 1
fi
if ! command -v claude >/dev/null 2>&1; then
  echo "ERROR: Claude Code executable 'claude' is not available; all preconditions passed, but launch cannot continue." >&2
  exit 1
fi

claude_args=(--add-dir "$method_dir" --agent "$agent")
if [[ "$resume" == "--resume" ]]; then
  claude_args+=(--resume)
fi

echo "Launching '$agent' in $client_dir with methodology $current_version ($current_commit)."
set +e
(
  cd "$client_dir"
  export CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1
  claude "${claude_args[@]}"
)
claude_status=$?
set -e

post_status=0
if ! "$method_dir/scripts/check-methodology-clean.sh" "$method_dir"; then
  echo "ERROR: methodology drift was detected after the client session." >&2
  post_status=1
fi
if (( claude_status != 0 )); then
  echo "ERROR: Claude Code exited with status $claude_status." >&2
  post_status=1
fi
if (( post_status != 0 )); then
  exit 1
fi

echo "Session complete. Review and commit intended client-repository changes."
