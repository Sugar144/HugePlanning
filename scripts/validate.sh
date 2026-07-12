#!/usr/bin/env bash
# validate.sh — THE single progressive client-repository validator (R2-26).
#
# This script is extended at every methodology stage and is NEVER replaced by
# a second validator. Current scope: S0b — the S0a checks (required structure,
# project.yaml, methodology.lock.yaml, gitignore, deny rules) plus the
# discovery artifacts: schema validation for open-questions, requirements,
# solution-context, interview-state files, and handoff records; ID/reference
# integrity (06 §4); and the profile-aware requirement matrix v0 (R2-21,
# discovery-stage rows only).
#
# ── How to extend at S2 and later (R2-26, 02 §8) ────────────────────────────
#  1. Add "artifact-path|schema-file" entries to SCHEMA_CHECKS as each schema
#     gains its first consumer (S2: content-inventory, product-backlog;
#     S3: delivery-backlog, test-matrix; …).
#  2. Extend the profile matrix section with the new stage's 21 §5 rows.
#  3. Extend scripts/lib/check-ids.py with each new registry's IDs and links.
# ────────────────────────────────────────────────────────────────────────────
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
METHOD_DIR="${METHODOLOGY_DIR:-$(dirname "$SCRIPT_DIR")}"
PYTHON="${PYTHON:-python3}"

usage() {
  cat <<'EOF'
Usage: validate.sh [client-dir]

Validates a client repository against the methodology contracts.
S0b scope: required structure, project.yaml, methodology.lock.yaml, discovery
artifact schemas (open-questions, requirements, solution-context,
interview-state, handoffs), ID/reference integrity, profile matrix v0.
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

# ── §5: schema validation (S0a schemas + S0b discovery schemas) ────────────
# Extend here: one "instance-path|schema-file" per schema at its first
# consumer's stage (R2-26). Never remove entries; never fork this script.
# Absent instances are skipped here — presence requirements live in the
# profile-matrix section (§8), not in the schema checks.
SCHEMA_CHECKS=(
  "project.yaml|project.schema.json"
  "methodology.lock.yaml|methodology-lock.schema.json"
  "docs/requirements/open-questions.yaml|open-questions.schema.json"
  "docs/requirements/requirements.yaml|requirements.schema.json"
  "docs/requirements/solution-context.yaml|solution-context.schema.json"
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

# ── S0b §6: per-instance schema checks with dynamic paths ───────────────────
# Interview state files (one per interview directory, 04 §6).
for state in "$CLIENT_DIR"/evidence/interviews/*/interview-state.json; do
  [[ -f "$state" ]] || continue
  rel="${state#"$CLIENT_DIR/"}"
  if "$PYTHON" "$SCRIPT_DIR/lib/schema-validate.py" \
      "$METHOD_DIR/schemas/interview-state.schema.json" "$state"; then
    ok "$rel valid against interview-state.schema.json"
  else
    error "$rel fails interview-state.schema.json (details above)"
  fi
done
# Gate handoff records (append-only, R2-05): every record must validate.
for record in "$CLIENT_DIR"/docs/handoffs/*.yaml; do
  [[ -f "$record" ]] || continue
  rel="${record#"$CLIENT_DIR/"}"
  if "$PYTHON" "$SCRIPT_DIR/lib/schema-validate.py" \
      "$METHOD_DIR/schemas/handoff.schema.json" "$record"; then
    ok "$rel valid against handoff.schema.json"
  else
    error "$rel fails handoff.schema.json (details above)"
  fi
done

# ── S0b §7: ID and reference integrity (06 §4, 08 §6) ──────────────────────
if OUT="$("$PYTHON" "$SCRIPT_DIR/lib/check-ids.py" "$CLIENT_DIR" 2>&1)"; then
  ok "ID/reference integrity (uniqueness, counters, links, handoff names)"
else
  printf '%s\n' "$OUT" >&2
  error "ID/reference integrity violations (06 §4) — details above"
fi

# ── S0b §8: profile-aware requirement matrix v0 (R2-21; 21 §5) ──────────────
# Discovery-stage rows only: once the project passes the G1 boundary (a G1
# handoff record exists, or the stage moved beyond discovery), the discovery
# registries must exist for every profile. Before that boundary their absence
# is informational. Later stages add their own rows here.
profile="$("$PYTHON" "$SCRIPT_DIR/lib/read-yaml-value.py" \
    "$CLIENT_DIR/project.yaml" project.profile 2>/dev/null || echo unknown)"
stage="$("$PYTHON" "$SCRIPT_DIR/lib/read-yaml-value.py" \
    "$CLIENT_DIR/project.yaml" workflow.current_stage 2>/dev/null || echo unknown)"
past_g1=0
compgen -G "$CLIENT_DIR/docs/handoffs/G1-*.yaml" > /dev/null && past_g1=1
case "$stage" in
  specification|technical_design|planning|implementation|validation|release|operation) past_g1=1 ;;
esac
DISCOVERY_REQUIRED=(
  "docs/requirements/requirements.yaml"
  "docs/requirements/solution-context.yaml"
)
for f in "${DISCOVERY_REQUIRED[@]}"; do
  if [[ -f "$CLIENT_DIR/$f" ]]; then
    ok "matrix: $f present"
  elif [[ "$past_g1" == 1 ]]; then
    error "matrix: $f required for profile '$profile' past the G1 boundary (21 §5, R2-21)"
  else
    info "matrix: $f not present yet (not required before the G1 boundary)"
  fi
done
info "profile: $profile · stage: $stage (matrix v0 covers discovery rows; later stages extend it)"

echo
if [[ "$ERRORS" -gt 0 ]]; then
  echo "validate.sh: FAIL — $ERRORS error(s) in $CLIENT_DIR (S0b scope)" >&2
  exit 1
fi
echo "validate.sh: PASS — $CLIENT_DIR (S0b scope)"
