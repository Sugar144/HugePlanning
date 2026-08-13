---
prompt_id: HP-PROMPT-007
version: 0.1.0
category: ORCHESTRATION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Implement and exercise the Phase 2.3 formal governance run preparation skill
target_environment: Codex CLI
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 74c5ea76c5b2f6ae2fe51ea683fed55b0b5cf759
authorization_scope:
  - preserve HP-PROMPT-007 and create formal-governance-run-preparer
  - validate the prepared KGR-005 custody workflow without executing KGR-005
  - update HP-MPROP-002, registrations, current-state evidence, and the Phase 2.3 report
  - run affected validations and build the Phase 2.3 review bundle
  - conditionally stage, commit, and push the authorized Phase 2.3 delta
forbidden_actions:
  - execute KGR-005 or invoke the Kernel Adversary
  - fabricate or import formal outputs
  - apply a Controller transition or create KGR-006
  - modify or ratify the Kernel or accept risk
  - pull request, merge, tag, release, or deployment
exact_text_preserved: true
exact_text_sha256: 92b36b851c0c97b8922ff1adb21c519a94d38118f9ccc725c277df6df5531ab5
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/skills/formal-governance-run-preparer/SKILL.md
  - governance/reviews/phase-2-3-formal-run-preparation/kgr-005-readiness-v0.1.0.yaml
  - governance/reviews/phase-2-3-formal-run-preparation/implementation-report-v0.1.0.md
  - Phase 2.3 external review bundle
result_commit: null
supersedes: null
---

# Phase 2.3 Formal Governance Run Preparer Prompt

## Exact executed text

Implement Phase 2.3: create and exercise the `formal-governance-run-preparer` skill.

## Checkpoint

```text
repository: /home/sugar/Documents/HugePlanning-governance
branch: governance/kernel-designer-revision-v0.1
required_head: 74c5ea76c5b2f6ae2fe51ea683fed55b0b5cf759
expected_worktree: clean
```

Read applicable `AGENTS.md` files, the project operating contract, `HP-MPROP-002`, the KGR-005 run artifacts, `GOV-PROTOCOL-002`, `GOV-LOOP-001`, and the existing deterministic governance tools.

Preserve this exact prompt as the next available `HP-PROMPT-### / 0.1.0`.

Complete all Phase 2.3 work in this single execution unless a material contract conflict, scope drift, failed validation, or authority conflict appears.

## Objective

Create the first reusable formal-run preparation skill:

```text
formal-governance-run-preparer
```

Then exercise it against the already prepared KGR-005 materials to verify that the skill can reproduce or validate the preparation workflow without executing KGR-005.

## Skill responsibilities

The skill must:

* verify repository, branch, HEAD, worktree, and governance status;
* identify the requested run, role, mode, protocol, loop, and input sources;
* verify prompt, envelope, manifest, member, hash, role, mode, run, and protocol bindings;
* call deterministic repository tools for hashes, schemas, ZIP inspection, package validation, inventories, and evidence generation;
* prepare or validate formal run custody artifacts;
* produce concise readiness and review evidence;
* stop before formal execution;
* identify missing inputs, conflicts, or non-completion conditions honestly.

The skill must not:

* execute a formal run;
* invoke an LLM role automatically;
* fabricate outputs;
* apply a Controller transition;
* create KGR-006;
* ratify or accept findings;
* modify the Kernel;
* accept risk;
* open a PR, merge, release, or bypass Project Owner authority.

Do not reimplement deterministic validation logic in natural-language instructions. Route it through the existing tools.

## Exercise against KGR-005

Use the skill in a controlled dry preparation/validation exercise for:

```text
run: KGR-005
role: Kernel Adversary
mode: TARGETED_CLOSURE
protocol: GOV-PROTOCOL-002
loop: GOV-LOOP-001
```

The exercise must:

* inspect the canonical repository run tree;
* validate the existing KGR-005 formal input package;
* confirm the exact package SHA-256 and member count;
* verify that KGR-005 remains `NOT_STARTED`;
* verify that no output package or execution evidence is treated as present;
* verify that no real Controller transition exists;
* produce a skill-generated readiness record or report;
* distinguish preparation validation from formal execution.

Do not rewrite valid historical KGR-005 artifacts merely to make the skill appear productive.

If the existing package is already valid, the correct result may be:

```text
READY_FOR_EXPLICIT_FORMAL_EXECUTION_AUTHORIZATION
```

This status must not mean executed, accepted, imported, ratified, or operational.

## Validation

Run only affected and relevant checks:

* skill structure and contract tests;
* deterministic validation of the KGR-005 input package;
* prompt-custody tests;
* learning/backlog validation;
* strict YAML/schema validation;
* review-bundle tool tests if shared packaging integration changes;
* `git diff --check`.

Use `governance/tools/build_review_bundle.py` for the Phase 2.3 review bundle.

Run broader Controller or repository suites only if shared executable infrastructure changes create real dependency risk.

Create learning evidence only if a material defect, ambiguity, repeated manual gap, or authority problem actually occurs.

Run `agent-session-reviewer` before closure and preserve only material findings.

## Documentation

Update `HP-MPROP-002` honestly to reflect local implementation pending review or committed implementation, according to the final state.

Register the skill and its validation evidence using repository conventions.

Create a concise Phase 2.3 implementation report including:

* skill design and authority boundary;
* deterministic tools invoked;
* KGR-005 readiness result;
* package hash and member count;
* tests and validation;
* confirmation that KGR-005 was not executed;
* session-review outcome.

## Conditional publication authority

If all required validations pass, no material defect or scope drift appears, and the worktree contains only authorized Phase 2.3 changes, the Project Owner authorizes:

```text
stage
commit
push current branch
```

Commit message:

```text
feat(governance): add formal run preparation skill
```

Do not open a PR, merge, release, execute KGR-005, invoke the Kernel Adversary, import results, or apply a Controller transition.

## Return

```text
Branch:
Previous HEAD:
Prompt ID/version:
Skill created:
Files created:
Files modified:
Deterministic tools used:
KGR-005 package result:
KGR-005 package SHA-256:
KGR-005 member count:
KGR-005 execution status:
Controller transitions:
Skill readiness result:
Tests:
Session-review result:
Material findings:
Learning evidence:
Review bundle:
Implementation report:
New commit:
Push:
Local/remote aligned:
Worktree:
Status:
Exact next action:
```

Finish with:

```text
Status: PHASE_2_3_COMMITTED_AND_PUSHED
Exact next action: Request explicit Project Owner authorization before executing KGR-005.
```
