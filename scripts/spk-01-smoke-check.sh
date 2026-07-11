#!/usr/bin/env bash
# spk-01-smoke-check.sh — SPK-01 launch smoke check (02 §5, R2-16).
#
# Confirms, on the installed Claude Code CLI and from a real client repo, that
# the verified distribution mechanism works:
#   (a) agent resolution from the --add-dir methodology
#   (b) skill invocation from the --add-dir methodology
#   (c) methodology CLAUDE.md + rules loading with
#       CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1
#   (d) deny rules block writes into the methodology (client writes stay allowed)
#
# Run at S0a and again after EVERY Claude Code upgrade; record the result and
# CLI version in the methodology README and the client lock (R-CC3).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
METHOD_DIR="${METHODOLOGY_DIR:-$(dirname "$SCRIPT_DIR")}"
CLAUDE_BIN="${CLAUDE_BIN:-claude}"
PYTHON="${PYTHON:-python3}"
TIMEOUT_S="${SPK01_TIMEOUT:-600}"

usage() {
  cat <<'EOF'
Usage: spk-01-smoke-check.sh <client-dir>

Runs the four SPK-01 checks (a-d) non-interactively (claude -p) from
<client-dir>, which must be a valid client repository (run new-client.sh
first). Prints PASS/FAIL per check.

Environment: METHODOLOGY_DIR, CLAUDE_BIN, SPK01_TIMEOUT (seconds per check,
default 600) override their defaults.

Exit codes: 0 all checks pass · 1 at least one check failed · 2 preconditions
not met (then follow the manual procedure in the methodology README).
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then usage; exit 0; fi
if [[ $# -ne 1 ]]; then echo "ERROR: expected <client-dir>" >&2; usage >&2; exit 2; fi

CLIENT_DIR="$1"
if [[ ! -d "$CLIENT_DIR" || ! -f "$CLIENT_DIR/project.yaml" ]]; then
  echo "ERROR: not a client repository: $CLIENT_DIR (run new-client.sh first)" >&2
  exit 2
fi
CLIENT_DIR="$(cd "$CLIENT_DIR" && pwd)"
if ! command -v "$CLAUDE_BIN" >/dev/null 2>&1; then
  echo "ERROR: claude CLI not found ('$CLAUDE_BIN') — SPK-01 cannot run live here." >&2
  echo "Follow the manual SPK-01 procedure in the methodology README." >&2
  exit 2
fi

CLI_VERSION="$("$CLAUDE_BIN" --version 2>/dev/null | head -n1 || echo unknown)"
BEFORE="$(git -C "$METHOD_DIR" status --porcelain)"
LOG_DIR="$(mktemp -d "${TMPDIR:-/tmp}/spk01.XXXXXX")"
PASS=0; FAIL=0

# run_check <letter> <logfile> <expected-token> [claude args...]
run_check() {
  local letter="$1" log="$2" token="$3"; shift 3
  local out status=0
  out="$(cd "$CLIENT_DIR" && \
    CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 \
    timeout "$TIMEOUT_S" "$CLAUDE_BIN" --add-dir "$METHOD_DIR" \
      --output-format text "$@" 2>&1)" || status=$?
  printf '%s\n' "$out" > "$LOG_DIR/$log"
  if [[ "$status" -ne 0 ]]; then
    echo "FAIL (${letter}): claude exited $status — log: $LOG_DIR/$log" >&2
    FAIL=$((FAIL + 1)); return 1
  fi
  if grep -q "$token" <<<"$out"; then
    echo "PASS (${letter}): found $token"
    PASS=$((PASS + 1)); return 0
  fi
  echo "FAIL (${letter}): token $token not in output — log: $LOG_DIR/$log" >&2
  FAIL=$((FAIL + 1)); return 1
}

echo "SPK-01 smoke check — CLI: $CLI_VERSION"
echo "  methodology: $METHOD_DIR"
echo "  client:      $CLIENT_DIR"
echo "  logs:        $LOG_DIR"
echo

# (a) agent resolution — the S0a client-discovery stub prints SPK01-AGENT-OK.
# Sentinel generation is probabilistic, so the exact token is not the sole
# oracle: complete semantic evidence (the ACTUAL client project id + the
# ACTUAL locked methodology version + the stub's exact closing statement, all
# read back from the client repo, never leaked into the prompt) also passes.
# Partial or unrelated output fails.
EXPECT_ID="$("$PYTHON" "$SCRIPT_DIR/lib/read-yaml-value.py" \
  "$CLIENT_DIR/project.yaml" project.id)" || EXPECT_ID=""
EXPECT_VERSION="$("$PYTHON" "$SCRIPT_DIR/lib/read-yaml-value.py" \
  "$CLIENT_DIR/methodology.lock.yaml" methodology.version)" || EXPECT_VERSION=""
STUB_STATEMENT="Discovery is not implemented until methodology S1. This is the S0a stub."
AGENT_STATUS=0
AGENT_OUT="$(cd "$CLIENT_DIR" && \
  CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 \
  timeout "$TIMEOUT_S" "$CLAUDE_BIN" --add-dir "$METHOD_DIR" \
    --output-format text --agent client-discovery \
    -p "Follow your agent instructions now." 2>&1)" || AGENT_STATUS=$?
printf '%s\n' "$AGENT_OUT" > "$LOG_DIR/agent.log"
if [[ "$AGENT_STATUS" -ne 0 ]]; then
  echo "FAIL (a): claude exited $AGENT_STATUS — log: $LOG_DIR/agent.log" >&2
  FAIL=$((FAIL + 1))
elif grep -q "SPK01-AGENT-OK" <<<"$AGENT_OUT"; then
  echo "PASS (a): found SPK01-AGENT-OK"
  PASS=$((PASS + 1))
elif [[ -n "$EXPECT_ID" && -n "$EXPECT_VERSION" ]] \
    && grep -qF -- "$EXPECT_ID" <<<"$AGENT_OUT" \
    && grep -qF -- "$EXPECT_VERSION" <<<"$AGENT_OUT" \
    && grep -qF -- "$STUB_STATEMENT" <<<"$AGENT_OUT"; then
  echo "PASS (a): semantic evidence (project id + lock version + stub statement)"
  PASS=$((PASS + 1))
else
  echo "FAIL (a): neither SPK01-AGENT-OK nor complete semantic evidence in output — log: $LOG_DIR/agent.log" >&2
  FAIL=$((FAIL + 1))
fi

# (b) skill invocation — methodology-smoke-check prints SPK01-SKILL-OK <version>.
run_check b skill.log "SPK01-SKILL-OK" \
  -p "Invoke the methodology-smoke-check skill and follow its procedure exactly." || true

# (c) CLAUDE.md + rules loading via the env var.
run_check c claudemd.log "SPK01-CLAUDEMD-OK" \
  -p "Two questions about configuration LOADED INTO THIS SESSION from the added methodology directory (do not open files with tools; answer only from loaded context). 1) If a methodology CLAUDE.md with numbered invariants is loaded and it states that IDs are never renumbered, print SPK01-CLAUDEMD-OK. 2) If a rule named id-and-status-conventions is loaded and it defines the ID grammar, print SPK01-RULES-OK. If either is not loaded, print SPK01-NOT-LOADED instead and say which." || true
if [[ -f "$LOG_DIR/claudemd.log" ]] && grep -q "SPK01-RULES-OK" "$LOG_DIR/claudemd.log"; then
  echo "PASS (c2): found SPK01-RULES-OK"; PASS=$((PASS + 1))
else
  echo "FAIL (c2): SPK01-RULES-OK not in output — log: $LOG_DIR/claudemd.log" >&2; FAIL=$((FAIL + 1))
fi

# (d) deny rules: methodology write blocked while client writes are allowed.
DENY_STATUS=0
(cd "$CLIENT_DIR" && \
  CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 \
  timeout "$TIMEOUT_S" "$CLAUDE_BIN" --add-dir "$METHOD_DIR" \
    --output-format text --permission-mode acceptEdits \
    -p "Permissions test, follow literally: (1) Use the Write tool to create file spk01-client-write.txt with content ok in the current directory. (2) Use the Write tool to attempt to create file spk01-deny-test.txt with content x inside the directory: $METHOD_DIR . Report the outcome of both attempts, then stop." \
    > "$LOG_DIR/deny.log" 2>&1) || DENY_STATUS=$?
D_OK=1
if [[ -e "$METHOD_DIR/spk01-deny-test.txt" ]]; then
  echo "FAIL (d): DENY RULE DID NOT HOLD — $METHOD_DIR/spk01-deny-test.txt was created. Remove it and investigate settings.json." >&2
  D_OK=0
fi
AFTER="$(git -C "$METHOD_DIR" status --porcelain)"
if [[ "$BEFORE" != "$AFTER" ]]; then
  echo "FAIL (d): methodology git status changed during the check — investigate:" >&2
  git -C "$METHOD_DIR" status --short >&2
  D_OK=0
fi
if [[ ! -e "$CLIENT_DIR/spk01-client-write.txt" ]]; then
  echo "FAIL (d): client-side control write did not happen (permission mode issue or claude exit $DENY_STATUS) — deny result inconclusive. Log: $LOG_DIR/deny.log" >&2
  D_OK=0
fi
rm -f "$CLIENT_DIR/spk01-client-write.txt"
if [[ "$D_OK" -eq 1 ]]; then
  echo "PASS (d): client write allowed, methodology write blocked, no drift"
  PASS=$((PASS + 1))
else
  FAIL=$((FAIL + 1))
fi

echo
echo "SPK-01 result: $PASS passed, $FAIL failed (CLI: $CLI_VERSION; logs: $LOG_DIR)"
echo "Record this result and the CLI version in the methodology README (02 §5)"
echo "and keep claude_code_version current in the client lock (R-CC3)."
[[ "$FAIL" -eq 0 ]] || exit 1
