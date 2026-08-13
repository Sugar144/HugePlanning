---
prompt_id: HP-PROMPT-006
version: 0.1.0
category: ORCHESTRATION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Implement Phase 2.2 durable review packaging and session supervision
target_environment: Codex CLI
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 71c753152598aa76a18fa8b34f3629a1c76c4c14
authorization_scope:
  - preserve HP-PROMPT-006 and implement the configurable durable review-bundle tool
  - create governance-review-packager and agent-session-reviewer as bounded versioned governance skills
  - update methodology backlog, registrations, current-state evidence, and Phase 2.2 implementation report
  - run only affected validations and build the Phase 2.2 review bundle with the durable tool
  - conditionally stage, commit, and push the authorized Phase 2.2 delta
forbidden_actions:
  - Controller, loop, protocol, Kernel, run, or governance authority semantic changes
  - pull request
  - merge
  - tag or release
  - KGR-005 execution
  - real Controller transition
  - risk acceptance or ratification
exact_text_preserved: true
exact_text_sha256: 3c13863bf916ac629dd3dd545534527a896d87612800c9ddab2a1bec9a52d4d3
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/tools/build_review_bundle.py
  - governance/skills/governance-review-packager/SKILL.md
  - governance/skills/agent-session-reviewer/SKILL.md
  - governance/reviews/phase-2-2-durable-review-packaging/implementation-report-v0.1.0.md
  - Phase 2.2 external review bundle
result_commit: null
supersedes: null
---

# Phase 2.2 Durable Review Packaging and Session Supervision Prompt

## Exact executed text

Implement Phase 2.2: durable review packaging and session supervision.

## Checkpoint

```text
repository: /home/sugar/Documents/HugePlanning-governance
branch: governance/kernel-designer-revision-v0.1
required_head: 71c753152598aa76a18fa8b34f3629a1c76c4c14
expected_worktree: clean
```

Read applicable `AGENTS.md` files and methodology proposals:

```text
HP-MPROP-002
HP-MPROP-003
HP-MPROP-004
```

Preserve this exact prompt as the next available `HP-PROMPT-### / 0.1.0`.

## Objective

Replace repeatedly generated temporary review-packaging scripts with one durable deterministic tool, then create two bounded reusable skills:

```text
governance-review-packager
agent-session-reviewer
```

Do not change Controller, loop, protocol, Kernel, run, or governance authority semantics.

## 1. Durable review-bundle tool

Create:

```text
governance/tools/build_review_bundle.py
```

It must support configurable inputs rather than phase-specific hardcoded paths.

Required capabilities:

* verify repository, branch, base HEAD, worktree, and staging state;
* inventory changed/new files;
* copy exact changed files;
* produce a unified binary-safe diff;
* execute a configurable list of validation commands;
* capture command, exit code, duration, and output;
* record dependency versions when configured;
* generate repository-status and scope evidence;
* create a SHA-256 manifest;
* build a safe ZIP with deterministic member ordering;
* reject unsafe, duplicate, ambiguous, or out-of-root paths;
* fail if any required validation fails;
* never stage, commit, push, extract into the repository, or mutate project state.

Use a small versioned configuration schema or profile format under an appropriate governance path.

Avoid hardcoded phase names, `/home/sugar`, temporary virtualenv names, or fixed test commands.

Add bounded tests for inventory, hashes, safe paths, validation failure, deterministic ordering, and bundle integrity.

## 2. Skill: governance-review-packager

Create the first versioned governance skill using the repository’s existing or most appropriate skill convention.

It must:

* activate when material repository work needs a review bundle;
* collect required inputs and bundle configuration;
* call `build_review_bundle.py` for deterministic work;
* inspect the result and report failures;
* produce or update a concise implementation/review report;
* stop before publication unless publication authority already exists.

It must not independently commit, push, open a PR, accept risk, ratify, or execute a formal run.

Do not reimplement ZIP, hashing, inventory, or validation logic in natural-language instructions.

## 3. Skill: agent-session-reviewer

Create a bounded session-closing skill that reviews only observable session evidence.

It must identify material:

* temporary scripts worth preserving;
* repeated workflows;
* tooling or skill candidates;
* unnecessary model work;
* repeated validation;
* prompt ambiguity;
* failures or near misses;
* missing tests, schemas, or controls;
* decisions left only in chat.

Its output must be concise and structured.

Allowed outcomes:

```text
MATERIAL_FINDINGS_IDENTIFIED
SESSION_REVIEW_COMPLETE_NO_MATERIAL_FINDINGS
INSUFFICIENT_OBSERVABLE_EVIDENCE
```

It must route findings to the appropriate durable destination:

```text
failure → learning system
future work → methodology backlog
deterministic repetition → tool proposal
reusable workflow → skill proposal
contract defect → versioned correction
```

It must not claim access to hidden reasoning, manufacture lessons, validate its own findings, or modify the repository without authorization.

## Documentation

Update the methodology backlog honestly:

```text
HP-MPROP-002
HP-MPROP-003
HP-MPROP-004
```

Use `IMPLEMENTED_LOCALLY_PENDING_REVIEW` or the closest valid status. Do not mark them accepted or operational.

Register the tool and skills according to repository conventions.

Create a concise Phase 2.2 implementation report.

Create learning evidence only if a material defect or near miss actually occurs.

## Validation

Run only affected and relevant suites:

* new review-bundle tool tests;
* skill structure/contract validation;
* prompt-custody tests;
* learning/backlog validation;
* strict YAML/schema validation;
* `git diff --check`.

Run broader suites only if shared infrastructure changes create real dependency risk.

Use the new durable tool to build the Phase 2.2 review bundle. Do not create another temporary bundle-builder script.

## Conditional publication authority

If all required validations pass, no scope drift or material defect appears, and the worktree contains only authorized Phase 2.2 changes, the Project Owner authorizes:

```text
stage
commit
push current branch
```

Commit message:

```text
feat(governance): add review packaging and session skills
```

Do not open a PR, merge, release, execute KGR-005, or apply a real Controller transition.

## Return

```text
Branch:
Previous HEAD:
Prompt ID/version:
Tool created:
Skills created:
Files created:
Files modified:
Tests:
Material findings:
Learning evidence:
Review bundle:
New commit:
Push:
Local/remote aligned:
Worktree:
KGR-005 status:
Status:
Exact next action:
```

Finish with:

```text
Status: PHASE_2_2_COMMITTED_AND_PUSHED
Exact next action: Return the commit and review evidence to orchestration.
```
