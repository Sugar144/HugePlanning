---
prompt_id: HP-PROMPT-052
version: 0.1.0
category: ORCHESTRATION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Define and execute GOV-GEN G5-A (Physical Architecture Synthesis) as one bounded governed unit -- compare materially distinct physical architectures for General Governance using the accepted G3 logical architecture and the accepted G4 consumer requirements delta, map the L0-L7 model to physical ownership per option, test every requirements-delta entry (explicitly every BLOCKS_REUSE entry) against each option, and record tradeoffs, migration/provenance implications, a recommendation, unresolved Owner decisions, and explicit non-decisions -- without selecting or implementing a target architecture, creating any repository, moving/extracting/migrating any file, or performing the independent/adversarial G5 review, its correction, or G5/GR/G6 authorization.
target_environment: Claude Code
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: e62040b3c137204f105e8b5f23686d5d190a2c93
authorization_scope: [verify repository identity/branch/HEAD/clean working tree/canonical G4-accepted-G5-not-started state before any write, canonically define G5-A as one contract under governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/, execute that contract in the same governed unit with no further Owner authorization gate for primary synthesis only, compare at minimum the four named physical-architecture families plus any materially better evidence-supported alternative discovered during synthesis without manufacturing non-distinct options, map the accepted G3 L0-L7 model to physical ownership per option, assess repository/package boundaries/HugePlanning future relationship/config and projection boundaries/L4 adapter placement/L5 evidence custody/L6 tooling and query ownership/L7 bounded-context delivery/namespacing/concurrent-safe identity allocation/Delegated Operational Authority enforcement location/provider-neutrality/migration and extraction complexity/backwards compatibility and provenance/operational and context cost per option, explicitly test every G4 BLOCKS_REUSE requirement against every option, record tradeoffs and failure modes/migration and provenance implications/a recommended candidate if evidence supports one/unresolved Owner decisions/explicit non-decisions, create the minimum decision/state/index reconciliation artifacts required by existing GOV-GEN conventions, run governance/tools/validate_prompts.py and governance/tools/validate_governance_state.py, one bounded local commit]
forbidden_actions: [select or implement the final physical architecture on behalf of the Project Owner, create general-governance or any other repository, move or extract or migrate any file, implement any architecture, modify AGENTS.md or CLAUDE.md, implement any G4 requirement, perform the independent or adversarial G5 review, correct the resulting G5 candidate, accept G5 on the Project Owner's behalf, authorize GR or G6, manufacture physical-architecture options that are not materially distinct, reclassify any G2 capability, redispose any G2 gap, reallocate any G3 capability or redesign the eight-layer model, push, pull request, merge, tag, release, deployment]
exact_text_preserved: true
exact_text_sha256: 7dc6c6b9219a010dd0f96c46907f50071d6f5d36fa0ccb47e172bd64eb907979
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-CONTRACT-001-v0.1.0.md
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001.md
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001.manifest.sha256
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/decisions/GOV-GEN-DECISION-014-g5a-contract-authorization-and-execution-v0.1.0.yaml
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/decisions/README.md
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/01-program-status.yaml
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/00-program-charter.md
  - governance/CURRENT_STATE.md
  - governance/DECISION_LOG.md
  - governance/ARTIFACT_REGISTRY.yaml
  - governance/README.md
result_commit: null
supersedes: null
---

# HP-PROMPT-052 — GOV-GEN G5-A Physical Architecture Synthesis

## Exact executed text

# GOV-GEN G5-A — Physical Architecture Synthesis

Define and execute the primary G5 physical-architecture synthesis only.

Use canonical repository state and applicable instructions as the source of truth. Load prior GOV-GEN evidence only by targeted lookup.

Expected branch:

`governance/kernel-designer-revision-v0.1`

Expected starting HEAD prefix:

`e62040b`

Verify exact repository identity, HEAD, clean worktree, and canonical state first.

Expected state:

`G4 ACCEPTED_BY_PROJECT_OWNER`
`G5 NOT_STARTED_NOT_AUTHORIZED`

This instruction authorizes G5 definition and primary synthesis, required custody/state reconciliation, validation, and one bounded local commit.

## Objective

Compare materially distinct physical architectures for General Governance using:

* the accepted G3 logical architecture;
* the accepted G4 consumer requirements delta;
* unresolved architecture pressures carried forward from G2–G4.

Determine which physical architectures remain credible and which best satisfy the accepted requirements.

Do not select or implement the final architecture on behalf of the Project Owner.

## Required comparison

Evaluate at minimum the previously contemplated families where still credible:

* governance remains physically inside HugePlanning;
* reusable core separated while HugePlanning remains an adopter/lab;
* independent `general-governance` repository;
* minimal/bounded extraction;
* any materially better evidence-supported alternative discovered during synthesis.

Do not manufacture options that are not materially distinct.

For every credible option assess:

* mapping of L0–L7 to physical ownership;
* repository/package boundaries;
* HugePlanning's future relationship to the reusable governance;
* configuration and project-specific projection boundaries;
* L4 adapter placement;
* L5 evidence/history custody;
* L6 tooling/query/index ownership;
* L7 bounded-context delivery;
* multi-project and multi-program namespacing;
* concurrent-safe identity allocation;
* Delegated Operational Authority enforcement location;
* provider-neutrality;
* migration/extraction complexity;
* backwards compatibility and provenance preservation;
* operational/context cost.

Explicitly test every G4 `BLOCKS_REUSE` requirement against each option.

## Deliverable

Produce one principal G5 architecture-synthesis candidate containing:

1. physical architecture options;
2. option-by-option L0–L7 mapping;
3. requirements compliance matrix;
4. tradeoffs and failure modes;
5. migration/provenance implications;
6. recommended candidate, if evidence supports one;
7. unresolved Owner decisions;
8. explicit non-decisions.

A recommendation is allowed.

Final Project Owner selection is not.

## Boundaries

Do not:

* create `general-governance`;
* move/extract/migrate files;
* implement any architecture;
* modify `AGENTS.md` or `CLAUDE.md`;
* implement G4 requirements;
* perform the independent/adversarial G5 review;
* correct the resulting G5 candidate;
* accept G5;
* authorize GR/G6;
* push, PR, merge, tag, release, or deploy.

Run applicable validators and create the required manifest/custody records.

One bounded local commit is authorized.

## Stop

Terminal state:

`G5_PRIMARY_SYNTHESIS_READY_FOR_INDEPENDENT_REVIEW`

Report:

1. contract/result IDs;
2. architectures compared;
3. recommended candidate, if any;
4. decisive G4 requirements/tradeoffs;
5. unresolved Owner decisions;
6. files changed;
7. validation results;
8. commit SHA.

Stop immediately. Do not start review.
