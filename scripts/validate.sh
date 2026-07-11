#!/usr/bin/env bash
# validate.sh — THE single progressive client-repository validator (R2-26).
#
# This script is extended at every methodology stage and is NEVER replaced by
# a second validator. Current scope: S0a (enough for a scratch client to pass
# G0): project.yaml, methodology.lock.yaml, required repository structure.
#
# ── How to extend at S0b and later (R2-26, 02 §8) ──────────────────────────
#  1. Add "artifact-path|schema-file" entries to SCHEMA_CHECKS as each schema
#     gains its first consumer (S0b: interview-state, requirements,
#     solution-context, open-questions, handoff).
#  2. Replace the open-questions parse-only check with its real schema check.
#  3. Add the profile-aware requirement matrix (21 §5, R2-21): artifacts
#     required for the project's profile are ERRORS when missing; optional
#     ones are INFO.
#  4. Add ID uniqueness / dangling-reference checks across structured
#     artifacts (06 §4).
# ────────────────────────────────────────────────────────────────────────────
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
METHOD_DIR="${METHODOLOGY_DIR:-$(dirname "$SCRIPT_DIR")}"
PYTHON="${PYTHON:-python3}"

usage() {
  cat <<'EOF'
Usage: validate.sh [client-dir]

Validates a client repository against the methodology contracts.
S0a scope: required structure, project.yaml, methodology.lock.yaml.
client-dir defaults to the current working directory.

Environment: METHODOLOGY_DIR overrides the methodology location (defaults to
the repository containing this script). PYTHON overrides the python3 binary.

Exit codes: 0 all checks pass · 1 validation errors · 2 usage/operational error.
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
  echo "ERROR: python3 is required (schema validation). Install python3." >&2
  exit 2
fi

ERRORS=0
error() { echo "ERROR: $*" >&2; ERRORS=$((ERRORS + 1)); }
info()  { echo "INFO:  $*"; }
ok()    { echo "ok:    $*"; }

# ── S0a §1: required files (03 §2 template contract) ───────────────────────
REQUIRED_FILES=(
  "CLAUDE.md"
  "README.md"
  "project.yaml"
  "methodology.lock.yaml"
  ".gitignore"
  ".env.example"
  ".claude/settings.json"
  "docs/requirements/open-questions.yaml"
  "docs/product/engagement.md"
)
for f in "${REQUIRED_FILES[@]}"; do
  if [[ -f "$CLIENT_DIR/$f" ]]; then ok "file $f"
  else error "missing required file: $f (create the repo with new-client.sh)"; fi
done

# ── S0a §2: required directories (03 §2 tree) ──────────────────────────────
REQUIRED_DIRS=(
  "evidence/interviews" "evidence/clarifications"
  "evidence/client-materials" "evidence/confirmations"
  "docs/product" "docs/requirements" "docs/backlog"
  "docs/architecture/decisions" "docs/architecture/spikes"
  "docs/quality" "docs/traceability" "docs/task-context" "docs/changes"
  "docs/handoffs" "docs/releases/manifests" "docs/releases/verification"
  "ops/incidents" "src" "tests" ".github/workflows"
)
for d in "${REQUIRED_DIRS[@]}"; do
  if [[ -d "$CLIENT_DIR/$d" ]]; then ok "dir  $d"
  else error "missing required directory: $d"; fi
done
# evidence-raw/ is gitignored, so it cannot survive a clone — informational.
if [[ -d "$CLIENT_DIR/evidence-raw" ]]; then ok "dir  evidence-raw (local-only)"
else info "evidence-raw/ missing (gitignored, expected after clone) — fix: mkdir '$CLIENT_DIR/evidence-raw'"; fi

# ── S0a §3: .gitignore must exclude evidence-raw/ (R2-03) ──────────────────
if [[ -f "$CLIENT_DIR/.gitignore" ]]; then
  if grep -qE '^[[:space:]]*evidence-raw/' "$CLIENT_DIR/.gitignore"; then
    ok ".gitignore covers evidence-raw/"
  else
    error ".gitignore does not exclude evidence-raw/ — raw evidence would be committed (R2-03)"
  fi
fi

# ── S0a §4: methodology write-deny rules (02 §6) ───────────────────────────
if [[ -f "$CLIENT_DIR/.claude/settings.json" ]]; then
  if "$PYTHON" "$SCRIPT_DIR/lib/check-deny-rules.py" \
      "$CLIENT_DIR/.claude/settings.json" "$METHOD_DIR"; then
    ok "deny rules point at the methodology path"
  else
    error ".claude/settings.json deny rules missing or pointing away from '$METHOD_DIR' (02 §6)"
  fi
fi

# ── S0a §5: schema validation (schemas locked at S0a) ──────────────────────
# Extend here: one "instance-path|schema-file" per schema at its first
# consumer's stage (R2-26). Never remove entries; never fork this script.
SCHEMA_CHECKS=(
  "project.yaml|project.schema.json"
  "methodology.lock.yaml|methodology-lock.schema.json"
)
for pair in "${SCHEMA_CHECKS[@]}"; do
  instance="${pair%%|*}"; schema="${pair##*|}"
  [[ -f "$CLIENT_DIR/$instance" ]] || continue  # absence reported in §1
  if [[ ! -f "$METHOD_DIR/schemas/$schema" ]]; then
    error "methodology schema not found: $METHOD_DIR/schemas/$schema (wrong METHODOLOGY_DIR?)"
    continue
  fi
  if "$PYTHON" "$SCRIPT_DIR/lib/schema-validate.py" \
      "$METHOD_DIR/schemas/$schema" "$CLIENT_DIR/$instance"; then
    ok "$instance valid against $schema"
  else
    error "$instance fails $schema (details above)"
  fi
done

# ── S0a §6: open-questions registry parses (full schema lands at S0b) ──────
if [[ -f "$CLIENT_DIR/docs/requirements/open-questions.yaml" ]]; then
  if "$PYTHON" "$SCRIPT_DIR/lib/schema-validate.py" --parse-only \
      "$CLIENT_DIR/docs/requirements/open-questions.yaml"; then
    ok "open-questions.yaml parses (schema check lands at S0b)"
  else
    error "docs/requirements/open-questions.yaml is not a YAML mapping"
  fi
fi

# ── S0a §7: profile visibility (matrix enforcement lands at S0b, R2-21) ────
if [[ -f "$CLIENT_DIR/project.yaml" ]]; then
  if profile="$("$PYTHON" "$SCRIPT_DIR/lib/read-yaml-value.py" \
      "$CLIENT_DIR/project.yaml" project.profile 2>/dev/null)"; then
    info "profile: $profile (S0a checks are profile-independent; matrix checks arrive at S0b)"
  fi
fi

echo
if [[ "$ERRORS" -gt 0 ]]; then
  echo "validate.sh: FAIL — $ERRORS error(s) in $CLIENT_DIR (S0a scope)" >&2
  exit 1
fi
echo "validate.sh: PASS — $CLIENT_DIR (S0a scope)"
