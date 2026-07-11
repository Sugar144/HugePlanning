#!/usr/bin/env bash
# new-client.sh — create a client repository from the methodology template
# (02 §8, 03 §3). Builds the client in a staging directory: copies
# templates/client-repo/, substitutes placeholders, writes the methodology
# lock (full commit SHA), VALIDATES the result, then git-inits with the
# initial commit and moves it to the target. A failure at any step leaves no
# partial target behind. Never overwrites a non-empty target; refuses a dirty
# methodology (the lock must record what is actually on disk — 02 §7).
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
METHOD_COMMIT="$(git -C "$METHOD_DIR" rev-parse HEAD)"
if [[ -n "$(git -C "$METHOD_DIR" status --porcelain)" ]]; then
  echo "ERROR: methodology working tree is dirty — the lock would record commit ${METHOD_COMMIT:0:7}, which does not match what is on disk (02 §7):" >&2
  git -C "$METHOD_DIR" status --short >&2
  echo "Commit (or stash) the methodology changes yourself, then retry." >&2
  echo "new-client.sh never cleans, stashes, or resets the methodology." >&2
  exit 1
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

# Stage the client next to the target: every step below happens in STAGING,
# and only a fully validated, committed client is moved to TARGET. Any failure
# removes the staging directory and leaves no partial target behind.
PARENT="$(dirname "$TARGET")"
mkdir -p "$PARENT"
PARENT="$(cd "$PARENT" && pwd)"
TARGET="$PARENT/$(basename "$TARGET")"
STAGING="$(mktemp -d "$PARENT/.new-client-tmp.XXXXXX")"
cleanup_staging() { if [[ -d "$STAGING" ]]; then rm -rf "$STAGING"; fi; }
trap cleanup_staging EXIT

echo "Creating client repository $PROJECT_ID at $TARGET"
echo "  methodology: $METHOD_VERSION (${METHOD_COMMIT:0:7}) at $METHOD_DIR"

cp -R "$TEMPLATE_DIR/." "$STAGING/"
mv "$STAGING/gitignore" "$STAGING/.gitignore"

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
done < <(find "$STAGING" -type f -print0)

if grep -RIl '{{' "$STAGING" >/dev/null 2>&1; then
  echo "ERROR: unsubstituted placeholders remain — no target created:" >&2
  grep -RIn '{{[A-Z_]*}}' "$STAGING" >&2 || true
  exit 2
fi

# Validate BEFORE the initial commit: an invalid client is never committed.
if ! METHODOLOGY_DIR="$METHOD_DIR" "$SCRIPT_DIR/validate.sh" "$STAGING"; then
  echo "ERROR: generated client fails validate.sh — no commit created, no target left behind." >&2
  exit 1
fi

# Git initialization + initial commit (03 §3). When no git identity is
# configured, the initial commit uses a command-local fallback identity;
# the user's git configuration is never modified.
git -C "$STAGING" init --quiet --initial-branch=main
git -C "$STAGING" add -A
GIT_ID_ARGS=()
if ! git -C "$STAGING" config user.name >/dev/null 2>&1 || \
   ! git -C "$STAGING" config user.email >/dev/null 2>&1; then
  GIT_ID_ARGS=(-c "user.name=Methodology Bootstrap" -c "user.email=bootstrap@local.invalid")
  echo "NOTE: no git identity configured — initial commit uses the fallback identity 'Methodology Bootstrap <bootstrap@local.invalid>' (your git config is untouched)."
fi
if ! git "${GIT_ID_ARGS[@]}" -C "$STAGING" commit --quiet \
    -m "chore: initialize $PROJECT_ID from methodology $METHOD_VERSION"; then
  echo "ERROR: initial commit failed — no target left behind." >&2
  exit 2
fi
if [[ "$(git -C "$STAGING" rev-list --count HEAD)" != "1" ]]; then
  echo "ERROR: expected exactly one initial commit — no target left behind." >&2
  exit 2
fi
if [[ -n "$(git -C "$STAGING" status --porcelain)" ]]; then
  echo "ERROR: generated client tree is not clean after the initial commit — no target left behind:" >&2
  git -C "$STAGING" status --short >&2
  exit 2
fi

# Publish: move the finished client into place (target emptiness re-checked).
if [[ -d "$TARGET" ]]; then
  if ! rmdir "$TARGET" 2>/dev/null; then
    echo "ERROR: target is no longer empty: $TARGET — nothing published, staging removed." >&2
    exit 1
  fi
fi
mv "$STAGING" "$TARGET"

echo "Created: $TARGET (initial commit on 'main', lock at $METHOD_VERSION/${METHOD_COMMIT:0:7})"
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
