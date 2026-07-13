# Temporary Codex Override — HugePlanning GOV-0

This file applies only to the current `governance/bootstrap-v0.1` bootstrap run.

## Identity

- Repository: `Sugar144/HugePlanning`
- Required branch: `governance/bootstrap-v0.1`
- Task: GOV-0 repository and governance-history bootstrap
- Detailed execution contract: `_governance_inbox/hugeplanning-governance-bootstrap-codex-prompt-v0.2.md`

## Hard boundaries

- Write only under `governance/**`.
- Read `_governance_inbox/**` as import input.
- Do not modify runtime, planning, product, tests, scripts, schemas, root documentation, CI, or the active S1 branch.
- Do not push, merge, tag, release, or open a PR.
- Do not design policies, enforcement, or new Kernel clauses.
- Do not claim validation, acceptance, ratification, independence, or execution that did not occur.
- Preserve raw inputs byte-for-byte and record SHA-256 checksums.
- Ask only when provenance or destructive ambiguity truly blocks safe preservation.

## Required behavior

1. Verify repository, branch, HEAD, worktree, and status before changes.
2. Inspect the actual inbox before deciding organization.
3. Follow the detailed GOV-0 execution contract.
4. Create `governance/AGENTS.md` for future governance sessions.
5. Validate YAML, links, checksums, artifact counts, run states, and changed paths.
6. Remove this temporary `AGENTS.override.md` before the final scope check.
7. Commit only `governance/**` using:
   `chore(governance): bootstrap governance project history`
8. Do not push.

## Communication

- Speak to the operator in Spanish.
- Write repository artifacts in English.
- Keep progress reports concise and surface blocking problems immediately.
