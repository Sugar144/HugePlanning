#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: tests/spk-01/run.sh <generated-client-dir>

Run the live SPK-01 fixture through Claude Code. Exit 77 means the runtime is
unavailable and the behavioural result remains explicitly unverified.
EOF
}

if [[ ${1:-} == "--help" || ${1:-} == "-h" ]]; then
  usage
  exit 0
fi
if (( $# != 1 )); then
  usage >&2
  exit 2
fi
if ! command -v claude >/dev/null 2>&1; then
  echo "SKIP: Claude Code is unavailable; SPK-01 was not executed live." >&2
  exit 77
fi

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd -P)"
client_arg="$1"
if [[ ! -d "$client_arg" ]]; then
  echo "ERROR: generated client directory does not exist: $client_arg" >&2
  exit 1
fi
client_dir="$(cd "$client_arg" && pwd -P)"

cat <<'EOF'
When the session opens, enter:

  Execute the complete SPK-01 fixture checklist now.

Exit only after the agent reports SPK01_COMPLETE.
EOF

"$root/scripts/start-agent.sh" "$client_dir" spk-01-fixture

marker="$client_dir/spk-01-skill-marker.txt"
if [[ ! -f "$marker" ]] || [[ "$(tr -d '\r\n' < "$marker")" != "SPK01_SKILL_INVOKED" ]]; then
  echo "ERROR: SPK-01 skill marker is missing or incorrect: $marker" >&2
  exit 1
fi
if [[ -e "$root/.spk-01-deny-probe" ]]; then
  echo "ERROR: methodology write was not denied; probe exists: $root/.spk-01-deny-probe" >&2
  exit 1
fi
"$root/scripts/check-methodology-clean.sh" "$root"

cat <<'EOF'
PASS (filesystem checks): skill marker exists, deny probe is absent, and the
methodology is clean. Confirm the session output also contained:
  SPK01_AGENT_RESOLVED
  the Git-truth invariant and <TYPE>-<NNN> grammar
  an explicit denied-write report
  SPK01_COMPLETE
Record the Claude Code version with the release result.
EOF
