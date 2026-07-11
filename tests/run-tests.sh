#!/usr/bin/env bash
# run-tests.sh — S0a deterministic test suite (02 §10: schema tests + script
# tests on a scratch repo). Self-contained: builds a committed COPY of the
# methodology (in a path containing spaces), generates scratch clients (also
# in paths with spaces), and never mutates the real methodology repository.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REAL_METHOD="$(dirname "$SCRIPT_DIR")"
PYTHON="${PYTHON:-python3}"

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
  expect_ok "py-compile $(basename "$p")" "$PYTHON" -m py_compile "$p"
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
assert "$id" in schema and "/1." in schema["$id"], "$id must embed the version"
PYEOF
done

note "== T3: schema fixtures (valid pass, invalid fail for the intended reason) =="
declare -A SCHEMA_FOR=( [project]="project.schema.json" [methodology-lock]="methodology-lock.schema.json" )
for group in project methodology-lock; do
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
FAKE_HEAD="$(git -C "$FAKE" rev-parse --short=7 HEAD)"

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

B="$(break_client bad-lock)"; sed -i 's/version: "v0.1.0"/version: "0.1.0"/' "$B/methodology.lock.yaml"
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

echo
echo "== RESULT: $PASS passed, $FAIL failed =="
[[ "$FAIL" -eq 0 ]] || exit 1
