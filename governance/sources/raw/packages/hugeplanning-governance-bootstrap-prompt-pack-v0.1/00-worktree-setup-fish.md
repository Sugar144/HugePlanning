# HugePlanning Governance Worktree Setup

**Shell:** fish  
**Repository:** `Sugar144/HugePlanning`  
**New branch:** `governance/bootstrap-v0.1`  
**New worktree:** `/home/sugar/Documents/HugePlanning-governance`

This worktree is based on `origin/main`, not on the active S1 branch. S1 continues independently in `feat/s1-discovery-interviewer`.

## 1. Run from the current HugePlanning checkout

```fish
cd "/home/sugar/Documents/Huge Planning"

git fetch origin

git status --short --branch
git worktree list
```

Confirm that the current S1 worktree is clean before continuing.

## 2. Create the governance branch and worktree

```fish
git worktree add \
  -b governance/bootstrap-v0.1 \
  "/home/sugar/Documents/HugePlanning-governance" \
  origin/main
```

This command:

- creates the local branch `governance/bootstrap-v0.1`;
- bases it on the current `origin/main`;
- creates an independent checkout;
- does not modify the S1 worktree.

## 3. Verify the new worktree

```fish
cd "/home/sugar/Documents/HugePlanning-governance"

git branch --show-current
git rev-parse --short HEAD
git status --short --branch
git remote get-url origin
```

Expected branch:

```text
governance/bootstrap-v0.1
```

Expected status:

```text
clean
```

## 4. Create a simple input inbox

```fish
mkdir -p "_governance_inbox"
```

Copy all governance material into:

```text
/home/sugar/Documents/HugePlanning-governance/_governance_inbox/
```

Put everything there without manually organizing it:

- research documents;
- interviewer prompt;
- intake artifacts;
- intake checkpoint;
- Designer prompt;
- Designer artifacts or ZIP;
- Adversary prompt;
- any relevant process notes;
- this prompt pack.

Codex will inventory, classify, checksum, preserve, and organize it.

## 5. Launch Codex from the governance worktree

```fish
cd "/home/sugar/Documents/HugePlanning-governance"
codex
```

Paste the complete contents of:

```text
hugeplanning-governance-bootstrap-codex-prompt-v0.1.md
```

## 6. Safety rule

Until the bootstrap is reviewed:

```text
Codex may modify only governance/** and consume _governance_inbox/**.
```

It must not modify the existing runtime, planning corpus, product backlog, tests, scripts, root documentation, or the active S1 branch.
