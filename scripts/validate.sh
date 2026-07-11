#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: validate.sh [client-dir]

Validate the S0a project.yaml and methodology.lock.yaml contracts plus the
required G0 client-repository structure. This is the single progressive
validator; later stages extend this file rather than replace it.
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

method_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
client_arg="${1:-.}"
if [[ ! -d "$client_arg" ]]; then
  echo "ERROR: client directory does not exist: $client_arg" >&2
  exit 1
fi
client_dir="$(cd "$client_arg" && pwd -P)"

errors=0
fail() {
  echo "ERROR: $*" >&2
  errors=$((errors + 1))
}

required_files=(
  README.md
  CLAUDE.md
  project.yaml
  methodology.lock.yaml
  .gitignore
  .env.example
  .claude/settings.json
  docs/product/engagement.md
  docs/requirements/open-questions.yaml
)
required_dirs=(
  evidence-raw
  evidence/interviews
  evidence/clarifications
  evidence/client-materials
  evidence/confirmations
  docs/product
  docs/requirements
  docs/handoffs
  src
  tests
)

for relative in "${required_files[@]}"; do
  [[ -f "$client_dir/$relative" ]] || fail "required file is missing: $relative"
done
for relative in "${required_dirs[@]}"; do
  [[ -d "$client_dir/$relative" ]] || fail "required directory is missing: $relative/"
done

if [[ -f "$client_dir/project.yaml" ]]; then
  if ! output="$(python3 "$method_dir/scripts/lib/schema_validate.py" "$method_dir/schemas/project.schema.json" "$client_dir/project.yaml" 2>&1)"; then
    fail "project.yaml is invalid: $output"
  fi
fi
if [[ -f "$client_dir/methodology.lock.yaml" ]]; then
  if ! output="$(python3 "$method_dir/scripts/lib/schema_validate.py" "$method_dir/schemas/methodology-lock.schema.json" "$client_dir/methodology.lock.yaml" 2>&1)"; then
    fail "methodology.lock.yaml is invalid: $output"
  fi
fi

if [[ -f "$client_dir/.gitignore" ]] && ! grep -Fqx 'evidence-raw/' "$client_dir/.gitignore"; then
  fail ".gitignore must contain the exact evidence-raw/ rule"
fi

if [[ -f "$client_dir/docs/requirements/open-questions.yaml" ]]; then
  if ! output="$(python3 - "$client_dir/docs/requirements/open-questions.yaml" <<'PY'
import sys
from pathlib import Path
try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required: python3 -m pip install PyYAML")
path = Path(sys.argv[1])
try:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
except Exception as exc:
    raise SystemExit(f"YAML syntax error: {exc}")
if data != {"schema_version": "1.0.0", "questions": [], "contradictions": []}:
    raise SystemExit("S0a registry must contain schema_version 1.0.0 and empty questions/contradictions arrays")
PY
  2>&1)"; then
    fail "open-questions.yaml is not the empty S0a registry: $output"
  fi
fi

if [[ -f "$client_dir/.claude/settings.json" ]]; then
  deny_root="//${method_dir#/}"
  if ! output="$(python3 - "$client_dir/.claude/settings.json" "$deny_root" <<'PY'
import json
import sys
from pathlib import Path
path = Path(sys.argv[1])
root = sys.argv[2]
try:
    data = json.loads(path.read_text(encoding="utf-8"))
except Exception as exc:
    raise SystemExit(f"JSON syntax error: {exc}")
deny = data.get("permissions", {}).get("deny")
expected = [f"Write({root}/**)", f"Edit({root}/**)"]
if deny != expected:
    raise SystemExit(f"permissions.deny must equal {expected!r}; got {deny!r}")
PY
  2>&1)"; then
    fail ".claude/settings.json does not enforce the real methodology path: $output"
  fi
fi

if git -C "$client_dir" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if ! git -C "$client_dir" check-ignore -q evidence-raw/; then
    fail "Git does not ignore evidence-raw/"
  fi
fi

if (( errors > 0 )); then
  echo "FAIL: S0a validation found $errors error(s) in $client_dir" >&2
  exit 1
fi

echo "PASS: S0a project, lock, and required structure are valid: $client_dir"
