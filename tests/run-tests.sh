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
)
for group in project methodology-lock product-requirements product-backlog \
             open-questions handoff solution-context interview-state; do
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
