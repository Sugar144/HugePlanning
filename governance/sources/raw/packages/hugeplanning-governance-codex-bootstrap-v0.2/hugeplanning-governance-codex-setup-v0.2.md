# HugePlanning GOV-0 — Codex Setup v0.2

## 1. Create the governance worktree

Run from the current HugePlanning checkout:

```fish
cd "/home/sugar/Documents/Huge Planning"
git fetch origin

git worktree add   -b governance/bootstrap-v0.1   "/home/sugar/Documents/HugePlanning-governance"   origin/main
```

## 2. Prepare the inbox

```fish
cd "/home/sugar/Documents/HugePlanning-governance"
mkdir -p "_governance_inbox"
```

Copy all governance artifacts, prompts, ZIP packages, checkpoints, research documents, and the Codex prompt into `_governance_inbox/`.

In particular, copy:

```text
hugeplanning-governance-bootstrap-codex-prompt-v0.2.md
```

## 3. Install the temporary Codex instruction file

Copy the supplied file:

```text
HugePlanning-GOV0-AGENTS.override.md
```

to the worktree root using the exact active name:

```fish
cp "/path/to/HugePlanning-GOV0-AGENTS.override.md"   "/home/sugar/Documents/HugePlanning-governance/AGENTS.override.md"
```

This file is temporary and must not be committed.

## 4. Verify

```fish
cd "/home/sugar/Documents/HugePlanning-governance"

git branch --show-current
git status --short --branch
ls -l AGENTS.override.md
```

Expected branch:

```text
governance/bootstrap-v0.1
```

## 5. Start a fresh Codex session

```fish
codex
```

Codex reads `AGENTS.override.md` when the session starts. Paste the full contents of:

```text
_governance_inbox/hugeplanning-governance-bootstrap-codex-prompt-v0.2.md
```

Do not create the override after Codex is already running; restart the session if necessary.

## 6. After Codex finishes

Verify that the temporary override was removed:

```fish
test ! -e AGENTS.override.md
and echo "Temporary override removed"
or echo "ERROR: AGENTS.override.md still exists"
```

Then verify the scope:

```fish
git status --short
git diff --name-only origin/main...HEAD
```

Only `governance/**` should be committed.
