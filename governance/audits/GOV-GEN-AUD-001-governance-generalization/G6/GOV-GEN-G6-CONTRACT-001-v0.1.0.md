---
document_id: GOV-GEN-G6-CONTRACT-001
title: HugePlanning Governance Generalization — G6 Bounded Extraction Planning Contract
program_id: GOV-GEN-AUD-001
phase: G6
status: EXECUTED_READY_FOR_PROJECT_OWNER_REVIEW
version: 0.1.0
authority: BOUNDED_EXTRACTION_PLANNING_NOT_EXTRACTION_EXECUTION
execution_authority: GRANTED_BY_PROJECT_OWNER_DIRECT_TASK_GOV_GEN_G6
repository_modification_authority: SCOPED_TO_G6_CUSTODY_AND_MINIMUM_STATUS_RECONCILIATION
extraction_authority: NONE
implementation_authority: NONE
acceptance_authority: NONE_RESERVED_TO_PROJECT_OWNER
parent_decision: GOV-GEN-DECISION-019/0.1.0
expected_repository: Sugar144/HugePlanning
expected_branch: governance/kernel-designer-revision-v0.1
expected_starting_commit: 888535ce329d04e2f26280b28d5ac665b9acf972
---

# GOV-GEN-G6 — Bounded Extraction Planning Contract

## Objective and controlling evidence

Produce one dependency-ordered, clean-session-executable extraction plan for
the Project Owner's adopted Option B: a reusable core separated in place,
with HugePlanning remaining the first adopter and lab. The plan is controlled
by `GOV-GEN-DECISION-019/0.1.0` and uses only targeted projections of the
accepted G3 R2, G4 R1, G5 R1, and GR results.

## Authorized result and write surface

The only principal result is
`GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001/0.1.0`, with its SHA-256 manifest.
Minimum reconciliation is limited to this contract, that plan, its manifest,
the GOV-GEN program status, `governance/CURRENT_STATE.md`, and the artifact
registry. One bounded local commit is authorized; no push or other publication
is authorized.

## Invariants and exclusions

The plan must retain L3 projections and L5 evidence/history as project-owned,
preserve historical identities and provenance, retain HugePlanning's current
governance authority while it becomes the first adopter, defer Option C, and
treat Option D solely as a separately authorized optional pilot. It must
account for AP-1 through AP-6 without representing any as implemented.

This contract authorizes neither extraction nor migration; creating a target
directory or repository; moving, copying, or normalizing implementation
artifacts; modifying `AGENTS.md` or `CLAUDE.md`; implementing AP-1–AP-6;
executing Option D; reopening the architecture decision; accepting the plan;
or pushing, opening a PR, merging, tagging, releasing, or deploying.

## Validation and terminal state

Validation must prove manifest integrity, required packet-field completeness,
dependency validity, bounded-context declarations, and no forbidden surface
change. The terminal state is
`G6_EXTRACTION_PLAN_READY_FOR_PROJECT_OWNER_REVIEW`. The executor stops at
that Owner review boundary.
