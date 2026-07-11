#!/usr/bin/env bash
# new-client.sh — create a client repository from the methodology template
# (02 §8, 03 §3). Copies templates/client-repo/, substitutes placeholders,
# writes the methodology lock, git-inits with the initial commit, and prints
# the G0 checklist. Never overwrites a non-empty target.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
METHOD_DIR="${METHODOLOGY_DIR:-$(dirname "$SCRIPT_DIR")}"
PYTHON="${PYTHON:-python3}"

usage() {
  cat <<'EOF'
Usage: new-client.sh <target-dir> <PROJECT-ID>

Creates <target-dir> from the methodology client template.
PROJECT-ID: uppercase letters/digits with hyphens, starting with a letter
(e.g. ACME-WEB).

Environment: METHODOLOGY_DIR overrides the methodology location (defaults to
the repository containing this script). PYTHON overrides the python3 binary.

Exit codes: 0 created · 1 refused (target not empty, dirty inputs) · 2 usage
or operational error.
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then usage; exit 0; fi
if [[ $# -ne 2 ]]; then
  echo "ERROR: expected exactly 2 arguments, got $#" >&2; usage >&2; exit 2
fi

TARGET="$1"
PROJECT_ID="$2"
TEMPLATE_DIR="$METHOD_DIR/templates/client-repo"

if [[ ! "$PROJECT_ID" =~ ^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*$ ]]; then
  echo "ERROR: invalid PROJECT-ID '$PROJECT_ID' — use uppercase letters/digits and hyphens, e.g. ACME-WEB" >&2
  exit 2
fi
if [[ ! -d "$TEMPLATE_DIR" ]]; then
  echo "ERROR: client template not found: $TEMPLATE_DIR (wrong METHODOLOGY_DIR?)" >&2
  exit 2
fi
if ! command -v git >/dev/null 2>&1; then echo "ERROR: git is required" >&2; exit 2; fi
if ! command -v "$PYTHON" >/dev/null 2>&1; then echo "ERROR: python3 is required" >&2; exit 2; fi

# Refuse to touch a non-empty target (no destructive behavior).
if [[ -e "$TARGET" ]]; then
  if [[ ! -d "$TARGET" ]]; then
    echo "ERROR: target exists and is not a directory: $TARGET" >&2; exit 1
  fi
  if [[ -n "$(ls -A "$TARGET")" ]]; then
    echo "ERROR: target directory is not empty: $TARGET" >&2
    echo "new-client.sh never overwrites existing content. Choose a new path." >&2
    exit 1
  fi
fi

# Methodology facts for the lock.
if ! git -C "$METHOD_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: methodology is not a git repository: $METHOD_DIR (02 §1)" >&2; exit 2
fi
METHOD_VERSION="$(head -n1 "$METHOD_DIR/VERSION" | tr -d '[:space:]')"
if [[ ! "$METHOD_VERSION" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "ERROR: methodology VERSION file is malformed: '$METHOD_VERSION'" >&2; exit 2
fi
METHOD_COMMIT="$(git -C "$METHOD_DIR" rev-parse --short=7 HEAD)"
if [[ -n "$(git -C "$METHOD_DIR" status --porcelain)" ]]; then
  echo "WARNING: methodology working tree is dirty — the lock records commit $METHOD_COMMIT, which may not match what is on disk. Commit methodology changes first for a faithful lock." >&2
fi
if ! git -C "$METHOD_DIR" tag --points-at HEAD 2>/dev/null | grep -qx "$METHOD_VERSION"; then
  echo "WARNING: methodology HEAD is not at tag $METHOD_VERSION — lock records commit $METHOD_COMMIT instead of a released tag (02 §7 release procedure)." >&2
fi
CLAUDE_CODE_VERSION="unknown"
if command -v claude >/dev/null 2>&1; then
  CLAUDE_CODE_VERSION="$(claude --version 2>/dev/null | head -n1 | awk '{print $1}')" || CLAUDE_CODE_VERSION="unknown"
  [[ -n "$CLAUDE_CODE_VERSION" ]] || CLAUDE_CODE_VERSION="unknown"
fi
TODAY="$(date +%F)"

mkdir -p "$TARGET"
TARGET="$(cd "$TARGET" && pwd)"

echo "Creating client repository $PROJECT_ID at $TARGET"
echo "  methodology: $METHOD_VERSION ($METHOD_COMMIT) at $METHOD_DIR"

cp -R "$TEMPLATE_DIR/." "$TARGET/"
mv "$TARGET/gitignore" "$TARGET/.gitignore"

# Placeholder substitution — pure bash (safe with any path characters).
substitute_placeholders() {
  local file="$1" content
  content="$(cat "$file"; printf x)"; content="${content%x}"
  content="${content//"{{PROJECT_ID}}"/$PROJECT_ID}"
  content="${content//"{{METHOD_DIR}}"/$METHOD_DIR}"
  content="${content//"{{DATE}}"/$TODAY}"
  content="${content//"{{METHODOLOGY_VERSION}}"/$METHOD_VERSION}"
  content="${content//"{{METHODOLOGY_COMMIT}}"/$METHOD_COMMIT}"
  content="${content//"{{CLAUDE_CODE_VERSION}}"/$CLAUDE_CODE_VERSION}"
  printf '%s' "$content" > "$file"
}
while IFS= read -r -d '' f; do
  if grep -Iq '{{' "$f" 2>/dev/null; then substitute_placeholders "$f"; fi
done < <(find "$TARGET" -type f -print0)

if grep -RIl '{{' "$TARGET" >/dev/null 2>&1; then
  echo "ERROR: unsubstituted placeholders remain:" >&2
  grep -RIn '{{[A-Z_]*}}' "$TARGET" >&2 || true
  exit 2
fi

# Git initialization + initial commit (03 §3).
git -C "$TARGET" init --quiet --initial-branch=main
git -C "$TARGET" add -A
if ! git -C "$TARGET" commit --quiet -m "chore: initialize $PROJECT_ID from methodology $METHOD_VERSION"; then
  echo "ERROR: initial commit failed. Ensure git identity is configured:" >&2
  echo "  git config --global user.name 'Your Name'" >&2
  echo "  git config --global user.email 'you@example.org'" >&2
  exit 2
fi

echo "Created: $TARGET (initial commit on 'main', lock at $METHOD_VERSION/$METHOD_COMMIT)"
echo
cat <<EOF
G0 readiness checklist (03 §7) — tick every item, then record the gate:
  [ ] Repo created from template, private, pushed, 'main' protected (manual: GitHub)
  [ ] methodology.lock.yaml matches an existing methodology tag
  [ ] engagement.md filled: client identity, contact, service scope sketch,
      commercial terms + maintenance tier reference, content-deadline clause,
      agreed communication channel
  [ ] project.yaml: language, sensitivity, retention set; archetype + profile
      hypothesis recorded with rationale (21 §4)
  [ ] .gitignore covers evidence-raw/
  [ ] .claude/settings.json deny rules point at the real methodology path
  [ ] validate.sh passes on the fresh repo:
        "$METHOD_DIR/scripts/validate.sh" "$TARGET"
  [ ] Launch test: start-agent.sh loads the methodology (then exit):
        "$METHOD_DIR/scripts/start-agent.sh" "$TARGET" client-discovery
G0 approved -> commit, record in project.yaml approvals.g0_readiness and
docs/handoffs/G0-readiness-01.yaml; stage advances to 'discovery'.
EOF
