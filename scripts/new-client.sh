#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: new-client.sh <target-dir> <PROJECT-ID>

Create a new S0a client repository from the versioned template. PROJECT-ID must
be uppercase words/digits separated by hyphens (for example ACME-WEB). The
target must not exist or must be empty.
EOF
}

if [[ ${1:-} == "--help" || ${1:-} == "-h" ]]; then
  usage
  exit 0
fi
if (( $# != 2 )); then
  usage >&2
  exit 2
fi

target_arg="$1"
project_id="$2"
if [[ ! "$project_id" =~ ^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*$ ]]; then
  echo "ERROR: invalid PROJECT-ID '$project_id'; expected uppercase hyphenated tokens such as ACME-WEB." >&2
  exit 2
fi
if [[ -e "$target_arg" && ! -d "$target_arg" ]]; then
  echo "ERROR: target exists and is not a directory: $target_arg" >&2
  exit 1
fi
if [[ -d "$target_arg" ]] && [[ -n "$(find "$target_arg" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  echo "ERROR: refusing to overwrite non-empty target directory: $target_arg" >&2
  exit 1
fi

method_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
template_dir="$method_dir/templates/client-repo"
[[ -d "$template_dir" ]] || { echo "ERROR: client template is missing: $template_dir" >&2; exit 1; }
[[ -f "$method_dir/VERSION" ]] || { echo "ERROR: methodology VERSION file is missing." >&2; exit 1; }
git -C "$method_dir" rev-parse --is-inside-work-tree >/dev/null 2>&1 || {
  echo "ERROR: methodology directory is not a Git worktree: $method_dir" >&2
  exit 1
}
"$method_dir/scripts/check-methodology-clean.sh" "$method_dir" >/dev/null

method_version="$(tr -d '[:space:]' < "$method_dir/VERSION")"
if [[ ! "$method_version" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "ERROR: VERSION must contain one v-prefixed SemVer; got '$method_version'." >&2
  exit 1
fi
method_commit="$(git -C "$method_dir" rev-parse HEAD)"
date_utc="$(date -u +%F)"
project_name="${project_id//-/ }"
if command -v claude >/dev/null 2>&1; then
  claude_version="$(claude --version 2>/dev/null | head -n 1)"
  claude_version="${claude_version:-unverified}"
else
  claude_version="unverified"
fi

mkdir -p "$target_arg"
target_dir="$(cd "$target_arg" && pwd -P)"
cp -a "$template_dir/." "$target_dir/"
mkdir -p "$target_dir/evidence-raw"

deny_root="//${method_dir#/}"
deny_root_json="$(python3 - "$deny_root" <<'PY'
import json
import sys
print(json.dumps(sys.argv[1])[1:-1])
PY
)"
python3 "$method_dir/scripts/lib/render_template.py" "$target_dir" \
  --replace PROJECT_ID "$project_id" \
  --replace PROJECT_NAME "$project_name" \
  --replace METHOD_DIR "$method_dir" \
  --replace METHOD_DENY_ROOT_JSON "$deny_root_json" \
  --replace METHOD_VERSION "$method_version" \
  --replace METHOD_COMMIT "$method_commit" \
  --replace CLAUDE_CODE_VERSION "$claude_version" \
  --replace DATE "$date_utc"

git -C "$target_dir" init -q -b main
"$method_dir/scripts/validate.sh" "$target_dir"
git -C "$target_dir" add -A
commit_message="chore: initialize $project_id from methodology $method_version"
if [[ -n "$(git -C "$target_dir" config user.name || true)" && -n "$(git -C "$target_dir" config user.email || true)" ]]; then
  git -C "$target_dir" commit -q -m "$commit_message"
else
  git -C "$target_dir" -c user.name='Methodology Bootstrap' -c user.email='bootstrap@local.invalid' commit -q -m "$commit_message"
fi

cat <<EOF
Created $project_id at: $target_dir
Initial commit: $(git -C "$target_dir" rev-parse HEAD)

G0 checklist (human/external items remain explicit):
[ ] Complete docs/product/engagement.md and replace onboarding defaults.
[ ] Confirm language, sensitivity, retention, archetype, and profile rationale.
[ ] Create a private GitHub remote, push main, and protect main.
[x] methodology.lock.yaml pins $method_version at $method_commit.
[x] evidence-raw/ is gitignored.
[x] methodology Write/Edit deny rules use the real absolute path.
[x] S0a structural and schema validation passes.
[ ] Run start-agent.sh and the SPK-01 live smoke check with Claude Code.
EOF
