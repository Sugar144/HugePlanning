#!/usr/bin/env bash
# start-agent.sh — unified client-session launcher (02 §8, verified mechanism
# 19 §0): validates the client repo, refuses a dirty methodology, warns on
# lock/checkout mismatch, then launches Claude Code with the methodology
# attached read-only, and checks for methodology drift afterwards.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
METHOD_DIR="${METHODOLOGY_DIR:-$(dirname "$SCRIPT_DIR")}"
PYTHON="${PYTHON:-python3}"
CLAUDE_BIN="${CLAUDE_BIN:-claude}"

usage() {
  cat <<'EOF'
Usage: start-agent.sh <client-dir> <agent> [--resume] [-- <extra claude args>]

Launches a Claude Code session in <client-dir> with the methodology loaded
read-only via --add-dir and the named methodology agent selected.

  --resume            resume the previous session for this client
  -- <args...>        passed through to the claude CLI verbatim (e.g.
                      -- -p "smoke prompt" for the SPK-01 non-interactive runs)

Preconditions enforced before launch: client repo passes validate.sh; the
methodology checkout is clean; the agent exists. Lock/checkout mismatch is a
warning (silent upgrades are impossible — 02 §7).

Environment: METHODOLOGY_DIR, PYTHON, CLAUDE_BIN override their defaults.

Exit codes: 0 session finished, no methodology drift · 1 precondition failed
or methodology drift detected · 2 usage/operational error.
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then usage; exit 0; fi
if [[ $# -lt 2 ]]; then echo "ERROR: expected <client-dir> <agent>" >&2; usage >&2; exit 2; fi

CLIENT_DIR="$1"; AGENT="$2"; shift 2
RESUME=0
EXTRA_ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --resume) RESUME=1; shift ;;
    --) shift; EXTRA_ARGS=("$@"); break ;;
    *) echo "ERROR: unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
done

if [[ ! "$AGENT" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
  echo "ERROR: invalid agent name: '$AGENT'" >&2; exit 2
fi
if [[ ! -d "$CLIENT_DIR" ]]; then
  echo "ERROR: client directory not found: $CLIENT_DIR" >&2; exit 2
fi
CLIENT_DIR="$(cd "$CLIENT_DIR" && pwd)"
if ! command -v "$CLAUDE_BIN" >/dev/null 2>&1; then
  echo "ERROR: claude CLI not found ('$CLAUDE_BIN'). Install Claude Code or set CLAUDE_BIN." >&2
  exit 2
fi

# Precondition 1: agent exists in the methodology.
AGENT_FILE="$METHOD_DIR/.claude/agents/$AGENT.md"
if [[ ! -f "$AGENT_FILE" ]]; then
  echo "ERROR: agent '$AGENT' not found at $AGENT_FILE" >&2
  echo "Available agents:" >&2
  ls "$METHOD_DIR/.claude/agents/" 2>/dev/null | sed 's/\.md$//; s/^/  - /' >&2 || true
  exit 1
fi

# Precondition 2: clean methodology (a dirty checkout is not the locked commit).
if ! METHODOLOGY_DIR="$METHOD_DIR" "$SCRIPT_DIR/check-methodology-clean.sh"; then
  echo "REFUSED: launch blocked by dirty methodology (02 §6)." >&2
  exit 1
fi

# Precondition 3: client repo validates (S0a scope grows with the validator).
if ! METHODOLOGY_DIR="$METHOD_DIR" "$SCRIPT_DIR/validate.sh" "$CLIENT_DIR"; then
  echo "REFUSED: client repository fails validate.sh — fix the errors above first." >&2
  exit 1
fi

# Precondition 4 (warning): lock matches the methodology checkout (02 §7).
LOCK_COMMIT="$("$PYTHON" "$SCRIPT_DIR/lib/read-yaml-value.py" \
  "$CLIENT_DIR/methodology.lock.yaml" methodology.commit)" || LOCK_COMMIT=""
LOCK_VERSION="$("$PYTHON" "$SCRIPT_DIR/lib/read-yaml-value.py" \
  "$CLIENT_DIR/methodology.lock.yaml" methodology.version)" || LOCK_VERSION=""
HEAD_COMMIT="$(git -C "$METHOD_DIR" rev-parse --short=7 HEAD)"
CHECKOUT_VERSION="$(head -n1 "$METHOD_DIR/VERSION" | tr -d '[:space:]')"
if [[ "$LOCK_COMMIT" != "$HEAD_COMMIT" || "$LOCK_VERSION" != "$CHECKOUT_VERSION" ]]; then
  echo "WARNING: lock/checkout mismatch — lock pins $LOCK_VERSION ($LOCK_COMMIT), checkout is $CHECKOUT_VERSION ($HEAD_COMMIT)." >&2
  echo "Use upgrade-lock.sh (later stage) or a git worktree of the locked tag (02 §7). Proceeding with the current checkout." >&2
fi

# Methodology drift guard: snapshot before/after (mandatory — 02 §6).
BEFORE="$(git -C "$METHOD_DIR" status --porcelain)"

CMD=("$CLAUDE_BIN" --add-dir "$METHOD_DIR" --agent "$AGENT")
[[ "$RESUME" -eq 1 ]] && CMD+=(--resume)
[[ ${#EXTRA_ARGS[@]} -gt 0 ]] && CMD+=("${EXTRA_ARGS[@]}")

echo "Launching in $CLIENT_DIR: ${CMD[*]}"
CLAUDE_STATUS=0
(
  cd "$CLIENT_DIR"
  export CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1
  "${CMD[@]}"
) || CLAUDE_STATUS=$?

AFTER="$(git -C "$METHOD_DIR" status --porcelain)"
if [[ "$BEFORE" != "$AFTER" ]]; then
  echo "ALERT: methodology changed during the session (02 §6) — investigate now:" >&2
  git -C "$METHOD_DIR" status --short >&2
  echo "Do not discard before understanding what wrote there." >&2
  exit 1
fi

if [[ "$CLAUDE_STATUS" -ne 0 ]]; then
  echo "NOTE: claude exited with status $CLAUDE_STATUS." >&2
fi
echo "Session ended. Methodology unchanged. Remember to commit client work in $CLIENT_DIR."
exit "$CLAUDE_STATUS"
