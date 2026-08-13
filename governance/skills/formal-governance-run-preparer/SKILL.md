---
name: formal-governance-run-preparer
description: Prepare or validate custody for a formal governance run without executing it. Use when Codex must verify repository and governance state, bind a requested run to its exact role, mode, prompt, protocol, loop, envelope, sources, hashes, and package, produce readiness evidence, or report a pre-execution blocker.
---

# Formal Governance Run Preparer

Contract version: `0.1.0`.

## Establish the boundary

1. Read every applicable `AGENTS.md`, the project operating contract, durable state and registry records, the requested run manifest, envelope, prompt snapshot, protocol, loop snapshot, and source declarations.
2. Confirm explicit authority for preparation or validation and for every repository write. Treat staging, commit, push, formal execution, import, and transition as separate permissions.
3. Record the requested run, role, mode, protocol and version, loop and version, prompt identity, envelope, package, repository, branch, expected HEAD, worktree expectation, input sources, evidence path, and output status.
4. Stop on a repository, authority, provenance, identity, custody, or scope conflict. Report the missing or conflicting fact and the exact correction or authorization required.

## Verify deterministically

Use `git` read-only commands for repository root, branch, HEAD, status, and changed-path inventory. Read governance status from durable repository artifacts; conversation is not status evidence.

Route formal package work through:

```text
python3 governance/tools/validate_run_package.py \
  --stage preparation \
  --role <adversary-or-designer> \
  --package <input-zip-or-directory> \
  --envelope <envelope> \
  --prompt-snapshot <exact-run-prompt> \
  --loop-snapshot <exact-loop-snapshot> \
  --json
```

Use the tool result for ZIP safety, exact members, member counts, hashes, strict structured-file parsing, schema checks, repository custody/source comparisons, and prompt/envelope/role/mode/run/protocol/loop bindings. Do not duplicate those checks in prose or ad hoc code. Use `validate_closure_loop.py`, `validate_prompts.py`, `manage_learning.py validate`, or `build_review_bundle.py` when their declared contracts apply. Prefer existing repository tools for serialization, inventories, evidence, and packaging.

If a required deterministic capability is absent, report the gap. Do not substitute an unreviewed natural-language assertion for validation.

## Prepare or validate custody

1. Preserve immutable historical artifacts. Create or update only explicitly authorized prospective custody and readiness evidence.
2. Reconcile deterministic results with the run manifest, envelope, registry, and current-state records. Confirm that each status describes preparation rather than execution.
3. Verify whether expected formal outputs, completed-output packages, execution evidence, imports, and Controller transitions are absent or present from durable evidence. Never infer execution from placeholders, protocols, readiness, or package existence.
4. Emit a concise readiness record or report with repository identity, run bindings, package classification, package SHA-256, member count, diagnostics, execution status, output status, transition status, authority limits, and exact next action.
5. Use `READY_FOR_EXPLICIT_FORMAL_EXECUTION_AUTHORIZATION` only after all preparation checks pass. It means prepared and validated only; it does not mean executed, accepted, imported, ratified, operational, or authorized to start.

## Non-completion

Use an honest blocked or not-ready result when inputs are missing, deterministic validation fails, identities conflict, scope drifts, governance status is incompatible, outputs are ambiguously present, or authority is insufficient. Preserve tool diagnostics and keep execution status unchanged.

## Stop boundary

Stop before formal execution. Do not invoke an LLM role, fabricate role outputs, apply a Controller transition, increment counters, create a successor run, import or accept findings, modify the Kernel, accept risk, ratify, open a pull request, merge, release, or bypass Project Owner authority.

## Handoff

Return:

```text
Run / role / mode:
Protocol / loop / prompt:
Repository / branch / HEAD / worktree:
Input package result / SHA-256 / member count:
Execution evidence / output package / Controller transition:
Readiness result:
Evidence created or updated:
Authority boundary:
Exact next action:
```
