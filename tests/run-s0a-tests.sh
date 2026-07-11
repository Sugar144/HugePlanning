#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: tests/run-s0a-tests.sh

Run the deterministic S0a schema, script, bootstrap, validation, and launcher
contract suite. The live Claude Code smoke check is reported separately.
EOF
}

if [[ ${1:-} == "--help" || ${1:-} == "-h" ]]; then
  usage
  exit 0
fi
if (( $# != 0 )); then
  usage >&2
  exit 2
fi

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
temp_root="$(mktemp -d "${TMPDIR:-/tmp}/s0a-tests.XXXXXX")"
trap 'rm -rf "$temp_root"' EXIT

pass_count=0
pass() {
  pass_count=$((pass_count + 1))
  echo "PASS: $1"
}
fail() {
  echo "FAIL: $1" >&2
  exit 1
}
expect_fail_contains() {
  local label="$1"
  local expected="$2"
  shift 2
  local output
  if output="$("$@" 2>&1)"; then
    fail "$label unexpectedly succeeded"
  fi
  if [[ "$output" != *"$expected"* ]]; then
    echo "$output" >&2
    fail "$label failed for the wrong reason; expected text: $expected"
  fi
  pass "$label"
}

while IFS= read -r -d '' script; do
  bash -n "$script"
done < <(find "$root/scripts" "$root/tests" -type f -name '*.sh' -print0)
pass "shell syntax for every Bash script"

schema_validator="$root/scripts/lib/schema_validate.py"
project_schema="$root/schemas/project.schema.json"
lock_schema="$root/schemas/methodology-lock.schema.json"
python3 "$schema_validator" "$project_schema" "$root/tests/schema-tests/project/valid/minimal.yaml" >/dev/null
python3 "$schema_validator" "$lock_schema" "$root/tests/schema-tests/methodology-lock/valid/minimal.yaml" >/dev/null
pass "valid project and methodology-lock fixtures"

expect_fail_contains "invalid project profile fixture" '$.project.profile' \
  python3 "$schema_validator" "$project_schema" "$root/tests/schema-tests/project/invalid/bad-profile.yaml"
expect_fail_contains "invalid project ID fixture" '$.project.id' \
  python3 "$schema_validator" "$project_schema" "$root/tests/schema-tests/project/invalid/bad-project-id.yaml"
expect_fail_contains "invalid methodology commit fixture" '$.methodology.commit' \
  python3 "$schema_validator" "$lock_schema" "$root/tests/schema-tests/methodology-lock/invalid/bad-commit.yaml"
expect_fail_contains "missing Claude version fixture" "missing required property 'claude_code_version'" \
  python3 "$schema_validator" "$lock_schema" "$root/tests/schema-tests/methodology-lock/invalid/missing-cli-version.yaml"

method_copy="$temp_root/Methodology With Spaces"
mkdir -p "$method_copy"
cp -a "$root/." "$method_copy/"
rm -rf "$method_copy/.git"
git -C "$method_copy" init -q -b experiment/chatgpt-s0a
git -C "$method_copy" add -A
git -C "$method_copy" -c user.name='S0a Tests' -c user.email='s0a@example.invalid' commit -q -m 'test fixture methodology'
"$method_copy/scripts/check-methodology-clean.sh" "$method_copy" >/dev/null
pass "clean methodology accepted"

touch "$method_copy/dirty-methodology.tmp"
expect_fail_contains "dirty methodology detected" "methodology checkout is dirty" \
  "$method_copy/scripts/check-methodology-clean.sh" "$method_copy"
expect_fail_contains "new-client rejects dirty methodology" "methodology checkout is dirty" \
  "$method_copy/scripts/new-client.sh" "$temp_root/Dirty Method Client" DIRTY-METHOD
rm "$method_copy/dirty-methodology.tmp"

client="$temp_root/Client Repository With Spaces"
"$method_copy/scripts/new-client.sh" "$client" ACME-WEB >/dev/null
"$method_copy/scripts/validate.sh" "$client" >/dev/null
pass "new client validates from a methodology path containing spaces"

[[ "$(git -C "$client" branch --show-current)" == "main" ]] || fail "generated client branch is not main"
[[ "$(git -C "$client" rev-list --count HEAD)" == "1" ]] || fail "generated client does not have exactly one initial commit"
[[ "$(git -C "$client" log -1 --pretty=%s)" == "chore: initialize ACME-WEB from methodology v0.1.0" ]] || fail "initial commit message is incorrect"
[[ -z "$(git -C "$client" status --porcelain)" ]] || fail "generated client worktree is dirty"
git -C "$client" check-ignore -q evidence-raw/ || fail "evidence-raw is not ignored"
if grep -R '{{[A-Z0-9_][A-Z0-9_]*}}' "$client" --exclude-dir=.git >/dev/null 2>&1; then
  fail "generated client contains unresolved placeholders"
fi
grep -Fq "Write(//${method_copy#/}/**)" "$client/.claude/settings.json" || fail "Write deny placeholder was not substituted"
grep -Fq "Edit(//${method_copy#/}/**)" "$client/.claude/settings.json" || fail "Edit deny placeholder was not substituted"
pass "placeholder substitution, Git initialization, and initial commit"

later_artifacts=(
  docs/requirements/requirements.yaml
  docs/requirements/solution-context.yaml
  docs/product/PRD.md
  docs/backlog/product-backlog.yaml
  docs/backlog/delivery-backlog.yaml
  docs/architecture/SDD.md
  docs/quality/test-matrix.yaml
)
for relative in "${later_artifacts[@]}"; do
  [[ ! -e "$client/$relative" ]] || fail "later-stage artifact leaked into S0a template: $relative"
done
pass "S0a template excludes S0b and later artifacts"

nonempty="$temp_root/Existing Nonempty Target"
mkdir -p "$nonempty"
touch "$nonempty/keep-me"
expect_fail_contains "new-client refuses a non-empty target" "refusing to overwrite" \
  "$method_copy/scripts/new-client.sh" "$nonempty" SECOND-CLIENT
[[ -f "$nonempty/keep-me" ]] || fail "overwrite refusal damaged the target"
expect_fail_contains "new-client rejects malformed project IDs" "invalid PROJECT-ID" \
  "$method_copy/scripts/new-client.sh" "$temp_root/Bad ID" 'bad id'

copy_case() {
  local name="$1"
  local destination="$temp_root/$name"
  mkdir -p "$destination"
  cp -a "$client/." "$destination/"
  printf '%s\n' "$destination"
}

case_dir="$(copy_case 'Missing Project')"
rm "$case_dir/project.yaml"
expect_fail_contains "validate rejects missing project.yaml" "required file is missing: project.yaml" \
  "$method_copy/scripts/validate.sh" "$case_dir"

case_dir="$(copy_case 'Invalid Project')"
sed -i 's/profile: lite/profile: impossible/' "$case_dir/project.yaml"
expect_fail_contains "validate rejects invalid project.yaml" "project.yaml is invalid" \
  "$method_copy/scripts/validate.sh" "$case_dir"

case_dir="$(copy_case 'Missing Lock')"
rm "$case_dir/methodology.lock.yaml"
expect_fail_contains "validate rejects missing methodology lock" "required file is missing: methodology.lock.yaml" \
  "$method_copy/scripts/validate.sh" "$case_dir"

case_dir="$(copy_case 'Invalid Lock')"
sed -i 's/commit: [0-9a-f]\{40\}/commit: invalid/' "$case_dir/methodology.lock.yaml"
expect_fail_contains "validate rejects invalid methodology lock" "methodology.lock.yaml is invalid" \
  "$method_copy/scripts/validate.sh" "$case_dir"

case_dir="$(copy_case 'Missing Structure')"
rm -rf "$case_dir/evidence/confirmations"
expect_fail_contains "validate rejects missing required repository path" "required directory is missing: evidence/confirmations/" \
  "$method_copy/scripts/validate.sh" "$case_dir"

case_dir="$(copy_case 'Lock Mismatch')"
sed -i 's/commit: [0-9a-f]\{40\}/commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/' "$case_dir/methodology.lock.yaml"
expect_fail_contains "start-agent rejects a lock/checkout mismatch before launch" "does not match methodology HEAD" \
  "$method_copy/scripts/start-agent.sh" "$case_dir" spk-01-fixture

touch "$method_copy/dirty-methodology.tmp"
expect_fail_contains "start-agent rejects dirty methodology before launch" "methodology checkout is dirty" \
  "$method_copy/scripts/start-agent.sh" "$client" spk-01-fixture
rm "$method_copy/dirty-methodology.tmp"

fake_bin="$temp_root/fake-bin"
fake_output="$temp_root/fake-claude-output.txt"
mkdir -p "$fake_bin"
cat > "$fake_bin/claude" <<'FAKE'
#!/usr/bin/env bash
set -euo pipefail
: "${SPK_FAKE_OUTPUT:?}"
{
  printf 'env=%s\n' "${CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD:-}"
  for argument in "$@"; do
    printf 'arg=%s\n' "$argument"
  done
} > "$SPK_FAKE_OUTPUT"
FAKE
chmod +x "$fake_bin/claude"
PATH="$fake_bin:$PATH" SPK_FAKE_OUTPUT="$fake_output" \
  "$method_copy/scripts/start-agent.sh" "$client" spk-01-fixture --resume >/dev/null
grep -Fqx 'env=1' "$fake_output" || fail "launcher did not export the additional-directory CLAUDE.md flag"
grep -Fqx 'arg=--add-dir' "$fake_output" || fail "launcher omitted --add-dir"
grep -Fqx "arg=$method_copy" "$fake_output" || fail "launcher passed the wrong methodology path"
grep -Fqx 'arg=--agent' "$fake_output" || fail "launcher omitted --agent"
grep -Fqx 'arg=spk-01-fixture' "$fake_output" || fail "launcher passed the wrong agent"
grep -Fqx 'arg=--resume' "$fake_output" || fail "launcher omitted --resume"
pass "start-agent validates preconditions and launches with required flags"

if "$root/tests/spk-01/run.sh" "$client" >/dev/null 2>&1; then
  fail "SPK-01 unexpectedly ran without the real Claude Code runtime"
else
  status=$?
  [[ "$status" == "77" ]] || fail "SPK-01 unavailable-runtime result should be exit 77, got $status"
fi
pass "SPK-01 reports unavailable runtime without claiming a pass"

python3 - "$root" "$client" <<'PY'
import json
import sys
from pathlib import Path
import yaml

root = Path(sys.argv[1])
client = Path(sys.argv[2])
for path in [*root.glob("schemas/*.json"), client / ".claude/settings.json"]:
    json.loads(path.read_text(encoding="utf-8"))
for path in [client / "project.yaml", client / "methodology.lock.yaml", client / "docs/requirements/open-questions.yaml"]:
    yaml.safe_load(path.read_text(encoding="utf-8"))
PY
pass "generated JSON and YAML syntax"

echo "PASS: all $pass_count S0a test groups completed"
