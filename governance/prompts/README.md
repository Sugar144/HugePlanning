---
document_id: GOV-PROMPT-CUSTODY-001
version: 0.1.0
status: IMPLEMENTED_LOCALLY_PENDING_PROJECT_OWNER_REVIEW
authority: prompt_custody_and_orchestration_evidence_only
---

# Material Prompt Custody

This directory preserves material orchestration prompts as durable execution-contract evidence. It prevents the only exact copy of a repository-affecting instruction from remaining in chat, terminal history, or another transient session. Custody is evidence of the prompt and its stated boundary; it is not execution proof, constitutional authority, ratification, or Enforcement Engineering authorization.

## Materiality

A prompt is material when it does any of the following:

- authorizes material repository modifications;
- defines implementation or review scope;
- defines affected files or validation requirements;
- prepares or executes formal runs;
- corrects material defects;
- authorizes staging, commit, push, pull request, merge, tag, release, deployment, or publication;
- changes governance methodology, tooling, or authority boundaries;
- produces formal architecture, implementation, review, or other durable artifacts.

Brief questions, minor clarifications, formatting-only requests, status checks, and messages without repository, execution, authority, or durable-artifact effect do not require preservation.

## Identity, categories, and lifecycle

Assign each prompt lineage a monotonically allocated stable `HP-PROMPT-###` ID and semantic version. Corrections retain the ID, increment the version, and name the version they supersede. Never reuse an ID for a different lineage or reuse a version.

Use a functional category such as `ORCHESTRATION`, `FORMAL_RUN`, `REVIEW`, `CORRECTION`, `PUBLICATION`, or `ARCHITECTURE`. Categories describe purpose and grant no authority.

Allowed lifecycle states are:

```text
DRAFT
APPROVED_NOT_EXECUTED
EXECUTED
SUPERSEDED
ABORTED
INVALID_EXECUTION
NOT_PRESERVED
```

`EXECUTED` records that execution began under that exact text; it does not claim correctness, completion, validation, acceptance, or any authorized external action. `NOT_PRESERVED` records an honest historical evidence gap and must not contain reconstructed text presented as original.

## Exact text, immutability, and supersession

For preserved prompts, store front matter followed by the complete exact text without editorial insertion, deletion, or retroactive discussion. Record the authorization scope, forbidden actions, target environment, repository checkpoint, execution status, interruption/recovery facts, result references, validation/report references when available, result commit when available, and supersession.

An executed prompt file is immutable. A correction is a new semantic version with an explicit `supersedes` reference; the prior file remains unchanged. A material prompt must enter repository custody before or as part of the commit containing the work it authorized or defined.

## Historical gaps and formal runs

When the exact historical text is unavailable, create only a `NOT_PRESERVED` catalogue record with an evidence-limitation statement. Do not reconstruct it as original evidence.

Formal run prompts already stored under `governance/runs/<run>/prompt/` have authoritative custody there. A catalogue record may reference the authoritative path, prompt identity, run, and hash; it must not duplicate the prompt merely to satisfy this directory convention. The reference and the run manifest remain distinct from proof that the run executed.

## Interrupted execution and recovery

After interruption, identify the exact custodied prompt version, verify the repository checkpoint and partial worktree, compare durable result evidence, record interruption and resumption honestly, and resume only within the original authorization boundary. If prompt identity cannot be established, stop rather than silently selecting or reconstructing a version.

## Authority limitation

Prompt custody preserves orchestration evidence only. It does not prove correct execution, validated output, commit, push, publication, adoption, ratification, or operation. It cannot create constitutional authority, authorize Enforcement Engineering, or enlarge an authorization boundary.
