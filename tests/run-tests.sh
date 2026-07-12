#!/usr/bin/env bash
# run-tests.sh — S0a deterministic test suite (02 §10: schema tests + script
# tests on a scratch repo). Self-contained: builds a committed COPY of the
# methodology (in a path containing spaces), generates scratch clients (also
# in paths with spaces), and never mutates the real methodology repository.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REAL_METHOD="$(dirname "$SCRIPT_DIR")"
PYTHON="${PYTHON:-python3}"

# Cleanliness contract (02 §6): the suite must leave the real methodology
# exactly as it found it — asserted at the end (T13), not merely cleaned up.
REAL_BEFORE="$(git -C "$REAL_METHOD" status --porcelain)"

PASS=0; FAIL=0
note() { printf '%s\n' "$*"; }
t_pass() { PASS=$((PASS + 1)); note "  PASS: $*"; }
t_fail() { FAIL=$((FAIL + 1)); note "  FAIL: $*" >&2; }

# expect_ok "label" cmd...   / expect_fail "label" cmd...
OUT=""
expect_ok() {
  local label="$1"; shift
  if OUT="$("$@" 2>&1)"; then t_pass "$label"; else
    t_fail "$label (expected success; output follows)"; printf '%s\n' "$OUT" >&2; fi
}
expect_fail() {
  local label="$1"; shift
  if OUT="$("$@" 2>&1)"; then
    t_fail "$label (expected failure but succeeded; output follows)"; printf '%s\n' "$OUT" >&2
  else t_pass "$label"; fi
}
expect_out() { # expect_out "label" "needle" — check $OUT from the previous call
  local label="$1" needle="$2"
  if grep -qF -- "$needle" <<<"$OUT"; then t_pass "$label"; else
    t_fail "$label (missing '$needle'; output follows)"; printf '%s\n' "$OUT" >&2; fi
}

WORK_BASE="$(mktemp -d "${TMPDIR:-/tmp}/s0a-tests.XXXXXX")"
WORK="$WORK_BASE/work area"   # spaces on purpose (S0a contract)
mkdir -p "$WORK"
cleanup() { rm -rf "$WORK_BASE"; }
trap cleanup EXIT

note "== T1: script syntax =="
for s in "$REAL_METHOD"/scripts/*.sh "$SCRIPT_DIR/run-tests.sh"; do
  expect_ok "bash -n $(basename "$s")" bash -n "$s"
done
for p in "$REAL_METHOD"/scripts/lib/*.py; do
  # ast.parse, not py_compile: a syntax check must not write __pycache__
  # into the methodology tree (it would trip check-methodology-clean.sh)
  expect_ok "py-syntax $(basename "$p")" "$PYTHON" -c \
    'import ast, sys; ast.parse(open(sys.argv[1], encoding="utf-8").read(), sys.argv[1])' "$p"
done
if command -v shellcheck >/dev/null 2>&1; then
  for s in "$REAL_METHOD"/scripts/*.sh; do
    if OUT="$(shellcheck -S warning "$s" 2>&1)"; then t_pass "shellcheck $(basename "$s")"
    else t_fail "shellcheck $(basename "$s")"; printf '%s\n' "$OUT" >&2; fi
  done
else
  note "  INFO: shellcheck not installed — skipping lint layer"
fi

note "== T2: schemas are valid JSON Schema (draft 2020-12) =="
for schema in "$REAL_METHOD"/schemas/*.schema.json; do
  expect_ok "meta-check $(basename "$schema")" "$PYTHON" - "$schema" <<'PYEOF'
import json, sys
import jsonschema
with open(sys.argv[1], encoding="utf-8") as fh:
    schema = json.load(fh)
cls = jsonschema.validators.validator_for(schema)
cls.check_schema(schema)
assert "2020-12" in schema.get("$schema", ""), "must declare draft 2020-12"
import re
assert "$id" in schema and re.search(r"/[0-9]+\.[0-9]+\.[0-9]+/", schema["$id"]), \
    "$id must embed the version"
PYEOF
done

note "== T3: schema fixtures (valid pass, invalid fail for the intended reason) =="
declare -A SCHEMA_FOR=(
  [project]="project.schema.json"
  [methodology-lock]="methodology-lock.schema.json"
  [product-requirements]="product-requirements.schema.json"
  [product-backlog]="product-backlog.schema.json"
  [open-questions]="open-questions.schema.json"
  [handoff]="handoff.schema.json"
  [solution-context]="solution-context.schema.json"
  [interview-state]="interview-state.schema.json"
  [requirements]="requirements.schema.json"
)
for group in project methodology-lock product-requirements product-backlog \
             open-questions handoff solution-context interview-state \
             requirements; do
  schema="$REAL_METHOD/schemas/${SCHEMA_FOR[$group]}"
  for f in "$SCRIPT_DIR/schema-tests/$group"/valid-*.yaml; do
    expect_ok "valid fixture $(basename "$f")" \
      "$PYTHON" "$REAL_METHOD/scripts/lib/schema-validate.py" "$schema" "$f"
  done
  for f in "$SCRIPT_DIR/schema-tests/$group"/invalid-*.yaml; do
    token="$(head -n1 "$f" | sed 's/^# expect-error: //')"
    if [[ "$token" == "$(head -n1 "$f")" ]]; then
      t_fail "$(basename "$f") lacks an '# expect-error:' first line"; continue
    fi
    if OUT="$("$PYTHON" "$REAL_METHOD/scripts/lib/schema-validate.py" "$schema" "$f" 2>&1)"; then
      t_fail "invalid fixture $(basename "$f") unexpectedly passed"
    elif grep -qF -- "$token" <<<"$OUT"; then
      t_pass "invalid fixture $(basename "$f") fails with expected reason"
    else
      t_fail "invalid fixture $(basename "$f") failed for the WRONG reason (wanted '$token')"
      printf '%s\n' "$OUT" >&2
    fi
  done
done

note "== T4: fake methodology copy + new-client.sh (paths with spaces) =="
FAKE="$WORK/method copy A"
mkdir -p "$FAKE"
cp -R "$REAL_METHOD/." "$FAKE/"
rm -rf "$FAKE/.git"
git -C "$FAKE" init --quiet --initial-branch=main
git -C "$FAKE" add -A
git -C "$FAKE" commit --quiet -m "test: fake methodology snapshot"
FAKE_HEAD="$(git -C "$FAKE" rev-parse HEAD)"

CLIENT="$WORK/scratch client A"
expect_ok "new-client.sh creates scratch client" \
  "$FAKE/scripts/new-client.sh" "$CLIENT" TEST-CLIENT
expect_out "G0 checklist printed" "G0 readiness checklist"
[[ -f "$CLIENT/.gitignore" ]] && t_pass "gitignore renamed to .gitignore" || t_fail "missing .gitignore"
[[ -d "$CLIENT/evidence-raw" ]] && t_pass "evidence-raw/ exists locally" || t_fail "missing evidence-raw/"
if grep -RIl '{{' "$CLIENT" >/dev/null 2>&1; then
  t_fail "unsubstituted placeholders remain"; grep -RIn '{{' "$CLIENT" >&2
else t_pass "all placeholders substituted"; fi
[[ "$(git -C "$CLIENT" rev-list --count HEAD)" == "1" ]] \
  && t_pass "exactly one initial commit" || t_fail "initial commit count != 1"
[[ "$(git -C "$CLIENT" branch --show-current)" == "main" ]] \
  && t_pass "branch is main" || t_fail "branch is not main"
git -C "$CLIENT" ls-files --error-unmatch "evidence-raw/.gitkeep" >/dev/null 2>&1 \
  && t_fail "evidence-raw/ content is TRACKED (must be gitignored)" \
  || t_pass "evidence-raw/ untracked in client git"
LOCK_COMMIT="$("$PYTHON" "$FAKE/scripts/lib/read-yaml-value.py" "$CLIENT/methodology.lock.yaml" methodology.commit)"
[[ "$LOCK_COMMIT" == "$FAKE_HEAD" ]] \
  && t_pass "lock records methodology HEAD ($FAKE_HEAD)" \
  || t_fail "lock commit '$LOCK_COMMIT' != methodology HEAD '$FAKE_HEAD'"
[[ "$LOCK_COMMIT" =~ ^[0-9a-f]{40}$ ]] \
  && t_pass "generated lock uses the full 40-char SHA" \
  || t_fail "generated lock commit is not a full 40-char SHA: '$LOCK_COMMIT'"
expect_ok "validate.sh PASSES on fresh client" "$FAKE/scripts/validate.sh" "$CLIENT"
expect_out "validator reports S0a PASS" "validate.sh: PASS"

note "== T5: validate.sh red cases (every S0a failure class) =="
break_client() { # break_client <name> — copy $CLIENT to a variant dir, print path
  local dir="$WORK/broken $1"
  rm -rf "$dir"; cp -R "$CLIENT" "$dir"; printf '%s' "$dir"
}
V="$FAKE/scripts/validate.sh"

B="$(break_client no-project)"; rm "$B/project.yaml"
expect_fail "missing project.yaml" "$V" "$B"; expect_out "  actionable" "missing required file: project.yaml"

B="$(break_client bad-project)"; sed -i 's/current_stage: onboarding/current_stage: development/' "$B/project.yaml"
expect_fail "invalid project.yaml (bad stage enum)" "$V" "$B"; expect_out "  names the field" "current_stage"

B="$(break_client no-lock)"; rm "$B/methodology.lock.yaml"
expect_fail "missing methodology.lock.yaml" "$V" "$B"

# Strip the leading v from whatever version the lock records (version-agnostic
# mutation — a literal "v0.1.0" match silently became a no-op after a bump).
B="$(break_client bad-lock)"; sed -i 's/^  version: "v/  version: "/' "$B/methodology.lock.yaml"
expect_fail "invalid lock (version missing v)" "$V" "$B"; expect_out "  names the field" "methodology/version"

B="$(break_client no-handoffs)"; rm -rf "$B/docs/handoffs"
expect_fail "missing docs/handoffs/" "$V" "$B"; expect_out "  actionable" "docs/handoffs"

B="$(break_client bad-ignore)"; sed -i 's|^evidence-raw/$|# evidence-raw/|' "$B/.gitignore"
expect_fail ".gitignore without evidence-raw/" "$V" "$B"; expect_out "  cites R2-03" "evidence-raw"

B="$(break_client no-oq)"; rm "$B/docs/requirements/open-questions.yaml"
expect_fail "missing open-questions.yaml (R2-30)" "$V" "$B"

B="$(break_client bad-deny)"; printf '{"permissions": {"deny": []}}\n' > "$B/.claude/settings.json"
expect_fail "settings.json without methodology deny rules" "$V" "$B"; expect_out "  cites 02 §6" "deny rules"

B="$(break_client no-raw)"; rm -rf "$B/evidence-raw"
expect_ok "missing evidence-raw/ is INFO only (clone case)" "$V" "$B"
expect_out "  info emitted" "evidence-raw/ missing"

note "== T15: validate.sh S0b discovery checks (green + red) =="
D="$WORK/discovery client"
rm -rf "$D"; cp -R "$CLIENT" "$D"
cp "$SCRIPT_DIR/schema-tests/requirements/valid-02-drafts-and-defaults.yaml" \
   "$D/docs/requirements/requirements.yaml"
cp "$SCRIPT_DIR/schema-tests/solution-context/valid-02-filled.yaml" \
   "$D/docs/requirements/solution-context.yaml"
mkdir -p "$D/evidence/interviews/client-discovery-01"
# .json extension with YAML content is fine: schema-validate.py parses YAML,
# a strict superset of JSON, regardless of extension.
cp "$SCRIPT_DIR/schema-tests/interview-state/valid-01-plan-example.yaml" \
   "$D/evidence/interviews/client-discovery-01/interview-state.json"
cp "$SCRIPT_DIR/schema-tests/handoff/valid-03-g0-minimal.yaml" \
   "$D/docs/handoffs/G0-readiness-01.yaml"
# Allocate the planted IDs (FR-001, NFR-003, CON-002) in the counters.
sed -i 's/ FR: 1,/ FR: 2,/; s/NFR: 1,/NFR: 4,/; s/ CON: 1,/ CON: 3,/' "$D/project.yaml"
expect_ok "valid planted discovery artifacts PASS" "$V" "$D"
expect_out "  S0b scope reported" "S0b scope"
expect_out "  interview-state checked" "interview-state.schema.json"
expect_out "  handoff checked" "handoff.schema.json"

expect_ok "pre-boundary absence of registries stays PASS" "$V" "$CLIENT"
expect_out "  absence is INFO before G1" "not required before the G1 boundary"

B="$(break_client s0b-dup-id)"
sed -i 's/ FR: 2,/ FR: 3,/; s/NFR: 1,/NFR: 4,/; s/ CON: 1,/ CON: 3,/' "$B/project.yaml"
cat > "$B/docs/requirements/requirements.yaml" <<'EOF'
schema_version: 2.0.0
requirements:
  - id: FR-001
    type: functional
    statement: Primera.
    origin: client_evidence
    status: draft
    source_refs: ["interview:client-discovery-01#turn-10"]
  - id: FR-001
    type: functional
    statement: Duplicada.
    origin: client_evidence
    status: draft
    source_refs: ["interview:client-discovery-01#turn-11"]
EOF
expect_fail "duplicate requirement ID detected" "$V" "$B"
expect_out "  names the id" "duplicate ID FR-001"

B="$(break_client s0b-dangling)"
sed -i 's/ FR: 1,/ FR: 2,/' "$B/project.yaml"
cat > "$B/docs/requirements/requirements.yaml" <<'EOF'
schema_version: 2.0.0
requirements:
  - id: FR-001
    type: functional
    statement: Válida.
    origin: client_evidence
    status: draft
    source_refs: ["interview:client-discovery-01#turn-10"]
EOF
cat > "$B/docs/requirements/open-questions.yaml" <<'EOF'
schema_version: 1.0.0
questions:
  - id: OQ-001
    type: internal
    question: Bloquea un requisito inexistente.
    owner: developer
    status: open
    blocks: [FR-099]
contradictions: []
EOF
sed -i 's/ OQ: 1,/ OQ: 2,/' "$B/project.yaml"
expect_fail "dangling blocks reference detected" "$V" "$B"
expect_out "  names the ref" "dangling reference to FR-099"

B="$(break_client s0b-counter)"
cat > "$B/docs/requirements/requirements.yaml" <<'EOF'
schema_version: 2.0.0
requirements:
  - id: FR-001
    type: functional
    statement: Usada sin asignar el contador.
    origin: client_evidence
    status: draft
    source_refs: ["interview:client-discovery-01#turn-10"]
EOF
expect_fail "counter collision detected (FR-001 used, counter FR=1)" "$V" "$B"
expect_out "  cites the contract" "counter collision"

B="$(break_client s0b-handoff-mismatch)"
cp "$SCRIPT_DIR/schema-tests/handoff/valid-01-g2-example.yaml" \
   "$B/docs/handoffs/G3-technical-baseline-01.yaml"
expect_fail "handoff gate/filename mismatch detected" "$V" "$B"
expect_out "  names the mismatch" "gate field"

B="$(break_client s0b-handoff-name)"
cp "$SCRIPT_DIR/schema-tests/handoff/valid-03-g0-minimal.yaml" \
   "$B/docs/handoffs/g0_readiness.yaml"
expect_fail "bad handoff filename detected" "$V" "$B"
expect_out "  cites R2-05" "does not match"

B="$(break_client s0b-post-g1-missing)"
cat > "$B/docs/handoffs/G1-discovery-review-01.yaml" <<'EOF'
schema_version: 2.0.0
gate: G1
sequence: 1
date: 2026-09-10
approved_by: developer
result: approved
commit: 9f1c2d3
EOF
expect_fail "missing registries past the G1 boundary" "$V" "$B"
expect_out "  cites the matrix" "required for profile"

B="$(break_client s0b-bad-state)"
mkdir -p "$B/evidence/interviews/client-discovery-01"
cp "$SCRIPT_DIR/schema-tests/interview-state/invalid-01-bad-phase.yaml" \
   "$B/evidence/interviews/client-discovery-01/interview-state.json"
expect_fail "invalid interview-state detected" "$V" "$B"
expect_out "  names the artifact" "interview-state.schema.json"

note "== T16: status.sh v0 — derived read-only dashboard =="
S="$FAKE/scripts/status.sh"
BEFORE_STATE="$(git -C "$D" status --porcelain)"
expect_ok "status.sh runs on planted discovery client" "$S" "$D"
expect_out "  derives latest gate state" "G0: approved (seq 1"
expect_out "  reports unrecorded gates" "G1: no record"
expect_out "  requirement histogram" "draft: 2"
expect_out "  question/contradiction counts" "contradictions: 0 open of 0"
expect_out "  pending trigger surfaced" "PENDING"
AFTER_STATE="$(git -C "$D" status --porcelain)"
[[ "$BEFORE_STATE" == "$AFTER_STATE" ]] \
  && t_pass "status.sh wrote nothing (read-only contract)" \
  || t_fail "status.sh modified the client tree"
expect_ok "status.sh runs on a bare fresh client" "$S" "$CLIENT"
expect_out "  absent registries render, not error" "requirements: none recorded"
expect_fail "status.sh rejects a missing directory" "$S" "$WORK/does not exist"

note "== T17: discovery templates are themselves schema-valid (FR-010) =="
declare -A TEMPLATE_SCHEMA=(
  [requirements.template.yaml]="requirements.schema.json"
  [solution-context.template.yaml]="solution-context.schema.json"
  [interview-state.template.yaml]="interview-state.schema.json"
  [handoff.template.yaml]="handoff.schema.json"
)
for tmpl in "${!TEMPLATE_SCHEMA[@]}"; do
  expect_ok "template $tmpl passes its schema" \
    "$PYTHON" "$REAL_METHOD/scripts/lib/schema-validate.py" \
    "$REAL_METHOD/schemas/${TEMPLATE_SCHEMA[$tmpl]}" \
    "$REAL_METHOD/templates/discovery/$tmpl"
done
# The client template's registry and lock stay valid with the S0b entries.
expect_ok "client template open-questions.yaml passes its schema" \
  "$PYTHON" "$REAL_METHOD/scripts/lib/schema-validate.py" \
  "$REAL_METHOD/schemas/open-questions.schema.json" \
  "$REAL_METHOD/templates/client-repo/docs/requirements/open-questions.yaml"
LOCK_SCHEMAS="$(grep -A8 '^schemas:' "$CLIENT/methodology.lock.yaml")"
for name in open-questions requirements solution-context interview-state handoff; do
  if grep -q "^  $name:" <<<"$LOCK_SCHEMAS"; then
    t_pass "generated lock pins $name"
  else
    t_fail "generated lock missing S0b schema entry: $name"
  fi
done

note "== T6: new-client.sh refusals =="
expect_fail "refuses non-empty target" "$FAKE/scripts/new-client.sh" "$CLIENT" TEST-CLIENT
expect_out "  actionable" "not empty"
expect_fail "rejects bad PROJECT-ID" "$FAKE/scripts/new-client.sh" "$WORK/x1" "bad id"
expect_out "  actionable" "invalid PROJECT-ID"
expect_fail "rejects missing arguments" "$FAKE/scripts/new-client.sh" "$WORK/x2"
[[ ! -e "$WORK/x1" && ! -e "$WORK/x2" ]] && t_pass "no partial targets left behind" \
  || t_fail "refusal left partial target dirs"

note "== T7: check-methodology-clean.sh =="
expect_ok "clean methodology passes" "$FAKE/scripts/check-methodology-clean.sh"
touch "$FAKE/dirty-marker.tmp"
expect_fail "dirty methodology detected" "$FAKE/scripts/check-methodology-clean.sh"
expect_out "  lists offending path" "dirty-marker.tmp"
rm "$FAKE/dirty-marker.tmp"
NOT_GIT="$WORK/not a repo"; mkdir -p "$NOT_GIT"
expect_fail "non-git methodology rejected" \
  env METHODOLOGY_DIR="$NOT_GIT" "$FAKE/scripts/check-methodology-clean.sh"

note "== T8: start-agent.sh preconditions and launch contract =="
STUB="$WORK_BASE/claude-stub"
RECORD="$WORK_BASE/stub-record.txt"
cat > "$STUB" <<EOF
#!/usr/bin/env bash
{ echo "cwd=\$PWD"
  echo "env=\${CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD:-unset}"
  for a in "\$@"; do echo "arg=\$a"; done
} > "$RECORD"
exit 0
EOF
chmod +x "$STUB"
SA="$FAKE/scripts/start-agent.sh"

rm -f "$RECORD"
expect_fail "unknown agent refused" env CLAUDE_BIN="$STUB" "$SA" "$CLIENT" no-such-agent
expect_out "  lists available agents" "client-discovery"
[[ ! -e "$RECORD" ]] && t_pass "no launch on unknown agent" || t_fail "launched despite unknown agent"

rm -f "$RECORD"
expect_fail "missing client dir refused" env CLAUDE_BIN="$STUB" "$SA" "$WORK/nowhere" client-discovery
[[ ! -e "$RECORD" ]] && t_pass "no launch on missing client" || t_fail "launched despite missing client"

rm -f "$RECORD"
B="$(break_client sa-invalid)"; rm "$B/project.yaml"
expect_fail "invalid client repo refused" env CLAUDE_BIN="$STUB" "$SA" "$B" client-discovery
[[ ! -e "$RECORD" ]] && t_pass "no launch on invalid client" || t_fail "launched despite invalid client"

rm -f "$RECORD"
touch "$FAKE/dirty-marker.tmp"
expect_fail "dirty methodology blocks launch" env CLAUDE_BIN="$STUB" "$SA" "$CLIENT" client-discovery
rm "$FAKE/dirty-marker.tmp"
[[ ! -e "$RECORD" ]] && t_pass "no launch on dirty methodology" || t_fail "launched despite dirty methodology"

rm -f "$RECORD"
expect_ok "valid preconditions launch" env CLAUDE_BIN="$STUB" "$SA" "$CLIENT" client-discovery -- -p "smoke"
if [[ -f "$RECORD" ]]; then
  OUT="$(cat "$RECORD")"
  expect_out "  cwd is the client repo" "cwd=$CLIENT"
  expect_out "  env var exported" "env=1"
  expect_out "  --add-dir passed" "arg=--add-dir"
  expect_out "  methodology dir passed" "arg=$FAKE"
  expect_out "  --agent passed" "arg=client-discovery"
  expect_out "  passthrough args forwarded" "arg=smoke"
else
  t_fail "launch record missing"
fi

DRIFT_STUB="$WORK_BASE/claude-drift-stub"
cat > "$DRIFT_STUB" <<EOF
#!/usr/bin/env bash
touch "$FAKE/drift-file.tmp"
exit 0
EOF
chmod +x "$DRIFT_STUB"
expect_fail "post-session methodology drift raises ALERT" \
  env CLAUDE_BIN="$DRIFT_STUB" "$SA" "$CLIENT" client-discovery
expect_out "  alert message" "ALERT: methodology changed"
rm -f "$FAKE/drift-file.tmp"

note "== T9: closed-set contracts — counters (06 §4) and gates (01 §4.2, DEC-06) =="
CONTRACT_PY="$WORK_BASE/contract-check.py"
cat > "$CONTRACT_PY" <<'PYEOF'
"""contract-check.py <schema.json> <client-project.yaml> <counters|gates> <canonical,csv>
Asserts schema.required == schema.properties == generated-client keys == the
canonical closed set. Exit 1 with a diff on any divergence."""
import json, sys, yaml
schema_path, instance_path, which, canon_csv = sys.argv[1:5]
canon = set(canon_csv.split(","))
key = "counters" if which == "counters" else "approvals"
schema = json.load(open(schema_path, encoding="utf-8"))
node = schema["properties"][key]
instance = yaml.safe_load(open(instance_path, encoding="utf-8"))
problems = []
for name, got in (("schema.required", set(node.get("required", []))),
                  ("schema.properties", set(node.get("properties", {}))),
                  ("instance", set(instance[key]))):
    if got != canon:
        problems.append(f"{key} {name}: missing={sorted(canon - got)} extra={sorted(got - canon)}")
if problems:
    print("\n".join(problems), file=sys.stderr)
    sys.exit(1)
PYEOF
CANON_COUNTERS="OBJ,FR,NFR,INT,CON,DAT,CNT,BR,ASM,OQ,CLAR,CTR,EP,US,UC,TASK,BUG,CR,ADR,SPK,RSK,TEST,REL,INC"
CANON_GATES="g0_readiness,g1_discovery_review,g2_business_baseline,g3_technical_baseline,g4_task_ready,g5_task_merge,g6_staging_release,g7_client_acceptance,g8_production_release,g9_change_approval"
expect_ok "counter namespace is exactly the 24-prefix set (06 §4)" \
  "$PYTHON" "$CONTRACT_PY" "$REAL_METHOD/schemas/project.schema.json" \
  "$CLIENT/project.yaml" counters "$CANON_COUNTERS"
expect_ok "approvals are exactly the ten gates G0-G9 (01 §4.2)" \
  "$PYTHON" "$CONTRACT_PY" "$REAL_METHOD/schemas/project.schema.json" \
  "$CLIENT/project.yaml" gates "$CANON_GATES"

note "== T10: new-client.sh refuses a dirty methodology (lock faithfulness, 02 §7) =="
echo "test-dirty-line" >> "$FAKE/README.md"
expect_fail "dirty methodology (tracked change) refused" \
  "$FAKE/scripts/new-client.sh" "$WORK/dirty client A" DIRTY-A
expect_out "  actionable" "dirty"
[[ ! -e "$WORK/dirty client A" ]] && t_pass "no target left behind (tracked change)" \
  || { t_fail "target created from dirty methodology (tracked change)"; rm -rf "$WORK/dirty client A"; }
git -C "$FAKE" checkout --quiet -- README.md
touch "$FAKE/untracked-dirty-marker.tmp"
expect_fail "dirty methodology (untracked file) refused" \
  "$FAKE/scripts/new-client.sh" "$WORK/dirty client B" DIRTY-B
[[ ! -e "$WORK/dirty client B" ]] && t_pass "no target left behind (untracked file)" \
  || { t_fail "target created from dirty methodology (untracked file)"; rm -rf "$WORK/dirty client B"; }
rm -f "$FAKE/untracked-dirty-marker.tmp"

note "== T11: safe bootstrap sequence (validate before commit; no partial targets) =="
FAKE2="$WORK/method copy B"
mkdir -p "$FAKE2"
cp -R "$REAL_METHOD/." "$FAKE2/"
rm -rf "$FAKE2/.git"
sed -i 's/current_stage: onboarding/current_stage: development/' \
  "$FAKE2/templates/client-repo/project.yaml"
git -C "$FAKE2" init --quiet --initial-branch=main
git -C "$FAKE2" add -A
git -C "$FAKE2" commit --quiet -m "test: methodology snapshot with broken template"
expect_fail "invalid generated client refused before any commit" \
  "$FAKE2/scripts/new-client.sh" "$WORK/invalid client" BAD-TPL
expect_out "  validator names the field" "current_stage"
[[ ! -e "$WORK/invalid client" ]] && t_pass "validation failure leaves no target" \
  || { t_fail "validation failure left a target behind"; rm -rf "$WORK/invalid client"; }
STAGING_LEFT="$(find "$WORK" -maxdepth 1 -name '.new-client*' 2>/dev/null || true)"
[[ -z "$STAGING_LEFT" ]] && t_pass "no staging residue after failure" \
  || t_fail "staging residue left behind: $STAGING_LEFT"

PRE="$WORK/pre existing"
mkdir -p "$PRE"; echo keep > "$PRE/keep.txt"
expect_fail "non-empty target refused" "$FAKE/scripts/new-client.sh" "$PRE" PRE-X
[[ "$(cat "$PRE/keep.txt")" == "keep" && "$(ls -A "$PRE")" == "keep.txt" ]] \
  && t_pass "existing target content untouched" || t_fail "existing target was damaged"

EMPTYT="$WORK/empty target"
mkdir -p "$EMPTYT"
expect_ok "pre-existing EMPTY directory accepted as target" \
  "$FAKE/scripts/new-client.sh" "$EMPTYT" EMPTY-OK
[[ "$(git -C "$EMPTYT" rev-list --count HEAD 2>/dev/null)" == "1" ]] \
  && t_pass "exactly one initial commit in empty-dir target" \
  || t_fail "empty-dir target has no single initial commit"

note "== T11b: bootstrap works without any git identity (fallback identity) =="
NOHOME="$WORK_BASE/nohome"; mkdir -p "$NOHOME"
# Overriding HOME hides pip --user site-packages from python; keep them
# reachable so this test exercises the missing GIT identity, not a broken env.
USER_SITE="$("$PYTHON" -c 'import site; print(site.getusersitepackages())' 2>/dev/null || true)"
expect_ok "client created with no git identity configured" \
  env -u GIT_AUTHOR_NAME -u GIT_AUTHOR_EMAIL -u GIT_COMMITTER_NAME -u GIT_COMMITTER_EMAIL \
      HOME="$NOHOME" XDG_CONFIG_HOME="$NOHOME/xdg" \
      GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null GIT_CONFIG_NOSYSTEM=1 \
      PYTHONPATH="$USER_SITE${PYTHONPATH:+:$PYTHONPATH}" \
  "$FAKE/scripts/new-client.sh" "$WORK/no id client" NO-ID
if [[ -d "$WORK/no id client/.git" ]]; then
  AUTHOR="$(git -C "$WORK/no id client" log -1 --format='%an <%ae>')"
  [[ "$AUTHOR" == "Methodology Bootstrap <bootstrap@local.invalid>" ]] \
    && t_pass "fallback identity on the initial commit ($AUTHOR)" \
    || t_fail "unexpected initial-commit identity: '$AUTHOR'"
else
  t_fail "no-identity client was not created"
fi
CONFIGURED_EMAIL="$(git -C "$CLIENT" log -1 --format='%ae')"
[[ "$CONFIGURED_EMAIL" != "bootstrap@local.invalid" ]] \
  && t_pass "configured identity still used when present" \
  || t_fail "fallback identity overrode the configured one"

note "== T12: SPK-01 oracle robustness (deterministic fake runtime) =="
FAKE_VERSION="$(head -n1 "$FAKE/VERSION" | tr -d '[:space:]')"
make_fake_claude() { # $1 = path, $2 = agent-reply mode
  local path="$1" mode="$2" agent_reply
  case "$mode" in
    sentinel)
      agent_reply='echo "SPK01-AGENT-OK"; echo "Project TEST-CLIENT, stage onboarding, profile standard, methodology __VER__."' ;;
    semantic)
      agent_reply='echo "The client project id is TEST-CLIENT at stage onboarding, profile standard; the locked methodology version is __VER__."; echo "Discovery is not implemented until methodology S1. This is the S0a stub."' ;;
    partial)
      agent_reply='echo "The client project id is TEST-CLIENT at stage onboarding."; echo "Discovery is not implemented until methodology S1. This is the S0a stub."' ;;
    unrelated)
      agent_reply='echo "Hello! I am a helpful assistant. How can I help you today?"' ;;
  esac
  cat > "$path" <<FAKEEOF
#!/usr/bin/env bash
if [[ "\${1:-}" == "--version" ]]; then echo "0.0.0-fake"; exit 0; fi
prompt=""; prev=""
for a in "\$@"; do [[ "\$prev" == "-p" ]] && prompt="\$a"; prev="\$a"; done
case "\$prompt" in
  *"agent instructions"*) ${agent_reply//__VER__/$FAKE_VERSION} ;;
  *"methodology-smoke-check"*) echo "SPK01-SKILL-OK $FAKE_VERSION" ;;
  *"Two questions"*) printf 'SPK01-CLAUDEMD-OK\nSPK01-RULES-OK\n' ;;
  *"Permissions test"*) : > spk01-client-write.txt; echo "client write ok; methodology write blocked by permission settings" ;;
  *) echo "unhandled prompt" ;;
esac
exit 0
FAKEEOF
  chmod +x "$path"
}
spk_case() { # $1 = mode, $2 = expected exit (0|1), $3 = expected (a) line
  local mode="$1" want_status="$2" want_line="$3" st=0
  make_fake_claude "$WORK_BASE/fake-claude-$mode" "$mode"
  OUT="$(CLAUDE_BIN="$WORK_BASE/fake-claude-$mode" SPK01_TIMEOUT=30 \
    "$FAKE/scripts/spk-01-smoke-check.sh" "$CLIENT" 2>&1)" || st=$?
  if [[ "$st" -eq "$want_status" ]]; then t_pass "spk $mode: exit $st"; else
    t_fail "spk $mode: exit $st (wanted $want_status); output follows"; printf '%s\n' "$OUT" >&2; fi
  expect_out "  spk $mode: check (a) verdict" "$want_line"
}
spk_case sentinel  0 "PASS (a)"
spk_case semantic  0 "PASS (a)"
spk_case partial   1 "FAIL (a)"
spk_case unrelated 1 "FAIL (a)"
ST=0
OUT="$(CLAUDE_BIN="$WORK_BASE/no-such-claude-bin" \
  "$FAKE/scripts/spk-01-smoke-check.sh" "$CLIENT" 2>&1)" || ST=$?
[[ "$ST" -eq 2 ]] && t_pass "runtime unavailable is exit 2 (not a fake FAIL)" \
  || t_fail "runtime-unavailable exit was $ST (wanted 2)"
expect_out "  manual-procedure pointer" "manual"

note "== T14: product spec — live instances valid + link integrity (R2-37) =="
# product/ is methodology-internal (never validate.sh, never the client lock);
# its live instances are validated here, in the suite, against their schemas.
expect_ok "product/requirements.yaml valid against its schema" \
  "$PYTHON" "$REAL_METHOD/scripts/lib/schema-validate.py" \
  "$REAL_METHOD/schemas/product-requirements.schema.json" \
  "$REAL_METHOD/product/requirements.yaml"
expect_ok "product/backlog.yaml valid against its schema" \
  "$PYTHON" "$REAL_METHOD/scripts/lib/schema-validate.py" \
  "$REAL_METHOD/schemas/product-backlog.schema.json" \
  "$REAL_METHOD/product/backlog.yaml"
expect_ok "product spec link integrity (IDs unique, links resolve, counters ahead)" \
  "$PYTHON" - "$REAL_METHOD/product/requirements.yaml" "$REAL_METHOD/product/backlog.yaml" <<'PYEOF'
import re, sys
import yaml

with open(sys.argv[1], encoding="utf-8") as fh:
    reqs = yaml.safe_load(fh)
with open(sys.argv[2], encoding="utf-8") as fh:
    bl = yaml.safe_load(fh)

errors = []
req_ids = [r["id"] for r in reqs["requirements"]]
if len(req_ids) != len(set(req_ids)):
    errors.append("duplicate requirement IDs")
for r in reqs["requirements"]:
    ac_ids = [a["id"] for a in r.get("acceptance_criteria", [])]
    if len(ac_ids) != len(set(ac_ids)):
        errors.append(f"{r['id']}: duplicate AC IDs")
    for a in ac_ids:
        if not a.startswith(r["id"] + "-AC-"):
            errors.append(f"{r['id']}: AC '{a}' not scoped to its parent")

epic_ids = [e["id"] for e in bl["epics"]]
task_ids = [t["id"] for t in bl["tasks"]]
if len(epic_ids) != len(set(epic_ids)):
    errors.append("duplicate epic IDs")
if len(task_ids) != len(set(task_ids)):
    errors.append("duplicate task IDs")
for t in bl["tasks"]:
    if t["epic"] not in epic_ids:
        errors.append(f"{t['id']}: epic '{t['epic']}' does not exist")
    for ref in t["implements"]:
        if ref not in req_ids:
            errors.append(f"{t['id']}: implements dangling requirement '{ref}'")
    for dep in t.get("depends_on", []):
        if dep not in task_ids:
            errors.append(f"{t['id']}: depends_on dangling task '{dep}'")
        if dep == t["id"]:
            errors.append(f"{t['id']}: depends on itself")

used = {}
for ident in req_ids + epic_ids + task_ids:
    prefix, num = ident.rsplit("-", 1)
    used[prefix] = max(used.get(prefix, 0), int(num))
counters = bl["counters"]
for prefix, high in used.items():
    if prefix not in counters:
        errors.append(f"counter missing for used prefix '{prefix}'")
    elif counters[prefix] <= high:
        errors.append(
            f"counter {prefix}={counters[prefix]} not ahead of highest used {high}")

if errors:
    print("PRODUCT-SPEC INTEGRITY FAILURES:", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)
PYEOF

note "== T18: knowledge files — front matter, INDEX, authoring-policy scan (17 §B/§F/§J) =="
expect_ok "knowledge front matter + INDEX consistency" \
  "$PYTHON" - "$REAL_METHOD" <<'PYEOF'
import os, re, sys
root = os.path.join(sys.argv[1], "knowledge")
errors = []
required_keys = ("id:", "title:", "type:", "status:", "version:",
                 "source_quality:", "consult_when:", "used_by:")
index = open(os.path.join(root, "INDEX.md"), encoding="utf-8").read()
files = []
for dirpath, _, names in os.walk(root):
    for name in names:
        if name.endswith(".md") and name != "INDEX.md":
            files.append(os.path.join(dirpath, name))
if len(files) < 10:
    errors.append(f"expected >= 10 knowledge files, found {len(files)}")
for path in files:
    rel = os.path.relpath(path, root)
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{rel}: missing front matter"); continue
    fm = m.group(1)
    for key in required_keys:
        if not re.search(rf"^{re.escape(key)}", fm, re.M):
            errors.append(f"{rel}: front matter missing '{key}'")
    kid = re.search(r"^id: (kn-[a-z0-9-]+)$", fm, re.M)
    if not kid:
        errors.append(f"{rel}: id missing or not kn- prefixed")
    elif f"`{kid.group(1)}`" not in index:
        errors.append(f"{rel}: id {kid.group(1)} not listed in INDEX.md")
    if not re.search(r"^status: provisional$", fm, re.M):
        errors.append(f"{rel}: status is not provisional (S1 files start provisional)")
    # 17 §J item 6: critical policy phrasing does not live in knowledge.
    body = text[m.end():]
    if re.search(r"must never", body, re.I):
        errors.append(f"{rel}: contains 'must never' policy phrasing (17 §G/§J)")
for e in errors:
    print(f"KNOWLEDGE-ERROR: {e}", file=sys.stderr)
sys.exit(1 if errors else 0)
PYEOF

note "== T13: suite leaves the real methodology unchanged =="
REAL_AFTER="$(git -C "$REAL_METHOD" status --porcelain)"
if [[ "$REAL_BEFORE" == "$REAL_AFTER" ]]; then
  t_pass "real methodology git status unchanged by the suite"
else
  t_fail "real methodology git status drifted during the suite:"
  diff <(printf '%s\n' "$REAL_BEFORE") <(printf '%s\n' "$REAL_AFTER") >&2 || true
fi
BYTECODE="$(find "$REAL_METHOD/scripts" "$REAL_METHOD/tests" \
  \( -name '__pycache__' -o -name '*.pyc' \) 2>/dev/null || true)"
[[ -z "$BYTECODE" ]] && t_pass "no bytecode or cache residue in the methodology" \
  || t_fail "bytecode residue left behind: $BYTECODE"

echo
echo "== RESULT: $PASS passed, $FAIL failed =="
[[ "$FAIL" -eq 0 ]] || exit 1
