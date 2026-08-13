---
prompt_id: HP-PROMPT-009
version: 0.1.0
category: ORCHESTRATION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Import the KGR-005 completed result and apply one validated Controller transition
target_environment: Codex CLI
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: a2f8caa6c3b3497e8673c256e58c41877afd098f
authorization_scope:
  - create and immediately use governance-result-importer
  - validate and import the exact eight-member KGR-005 completed-output package
  - dry-run and apply at most one unambiguous Controller transition
  - update affected durable state, evidence, registries, views, and review artifacts
  - conditionally commit and push the complete validated Phase 2.4 delta
forbidden_actions:
  - pull request, merge, tag, release, deployment, or unrelated refactoring
  - Kernel substance modification or ratification
  - human ratification, risk acceptance, or Enforcement Engineering activation
  - more than one Controller transition or successor-run creation
exact_text_preserved: true
exact_text_sha256: dcc7458844de5913197da6a0633629c9ba0228dae7cc7a369bd2c3098b951b19
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/skills/governance-result-importer/SKILL.md
  - governance/runs/KGR-005-kernel-adversary-targeted-closure/outputs/
  - governance/runs/KGR-005-kernel-adversary-targeted-closure/controller/controller-transition.json
  - governance/reviews/phase-2-4-formal-result-import/implementation-report-v0.1.0.md
  - Phase 2.4 external review bundle
result_commit: null
supersedes: null
---

# Phase 2.4 Formal Result Import and Controller Transition Prompt

## Exact executed text

You are working inside the HugePlanning repository.

## Execution identity

```yaml
phase: PHASE_2_4
task: FORMAL_RESULT_IMPORT_AND_CONTROLLER_TRANSITION
repository: Sugar144/HugePlanning
branch: governance/kernel-designer-revision-v0.1
expected_head: a2f8caa6c3b3497e8673c256e58c41877afd098f
run: KGR-005
role_result: Kernel Adversary / TARGETED_CLOSURE
declared_result: CLOSURE_CONFIRMED
```

Use the repository instructions, governance contracts, existing tools, schemas, tests, skills, learning system, and prompt-custody system as authoritative context.

Do not restart project discovery.

## Authorized inputs

Use this exact completed-output package:

```text
/home/sugar/Downloads/HugePlanning-KGR-005-targeted-closure-v0.2-proposed.zip
```

Expected package facts:

```yaml
sha256: 4e8de3b72d0ac9d70b7f13d7a1768d18a1cd57c1af090f5593f3b40e534f198b
member_count: 8
package_classification: VALIDATED_COMPLETED_OUTPUT_PACKAGE
declared_result: CLOSURE_CONFIRMED
```

The package has already received an external independent review, but you must still validate it deterministically using repository tools before import.

## Owner authorization

The Project Owner explicitly authorizes this bounded Phase 2.4 execution to:

1. Create a repository-custodied skill named:

```text
governance-result-importer
```

2. Use that skill immediately for KGR-005.
3. Validate the completed-output package.
4. Import the eight immutable formal outputs into the canonical KGR-005 output location without rewriting any historical input, prompt, protocol, envelope, or prior run artifact.
5. Produce durable import-validation evidence.
6. Run the Controller transition first in dry-run mode.
7. Compare the proposed transition against:

   * GOV-PROTOCOL-002;
   * GOV-LOOP-001;
   * the current Controller state;
   * the KGR-005 result;
   * current counters and guards;
   * constitutional authority boundaries.
8. Apply exactly one real Controller transition only if:

   * deterministic package validation passes;
   * import validation passes;
   * dry-run produces no diagnostics;
   * the transition follows directly from `CLOSURE_CONFIRMED`;
   * no counter, guard, state, or authority ambiguity exists;
   * no scope drift is required.
9. Update affected durable state, registries, indexes, evidence records, and generated views.
10. Run affected validation.
11. Build the Phase 2.4 review bundle.
12. Commit and push the complete authorized delta if all validation passes and the worktree is clean.

This authorization does not authorize a pull request, merge, release, Kernel ratification, human ratification, Enforcement Engineering activation, risk acceptance, or unrelated refactoring.

## Skill requirements

Create `governance-result-importer` as a bounded orchestration skill.

It must:

* verify repository branch, HEAD, and clean starting state;
* bind an exact run, protocol, loop, package hash, role, mode, and result;
* use deterministic repository tools for ZIP safety, schema validation, hashes, inventories, state calculations, and Controller transitions;
* preserve historical immutability;
* distinguish validation, import, acceptance, transition, ratification, and operation;
* stop on diagnostics, ambiguity, missing authority, conflicting state, or package drift;
* never fabricate outputs or infer approval;
* never create a successor run;
* never modify Kernel substance;
* never ratify or activate Enforcement Engineering;
* never apply more than one transition;
* support dry-run before any write;
* emit a concise completion or blocker report.

Reuse the existing skill architecture and skill-creator tooling. Do not duplicate deterministic logic already present in repository scripts.

## Import requirements

The imported package members must remain byte-identical to the validated package members.

Verify and record:

```text
package SHA-256
member inventory
individual member hashes
UTF-8 validity
strict YAML parsing
schema validation
run identity
role and mode identity
protocol and loop identity
declared adversary result
Markdown/YAML parity
absence of extra members
absence of unsafe ZIP paths
```

The canonical imported outputs must contain exactly:

```text
00-targeted-closure-basis.md
01-finding-closure-verdicts.yaml
02-targeted-adversarial-scenarios.md
03-regression-and-new-findings.md
04-markdown-yaml-parity-review.md
05-residual-risk-and-routing.md
06-closure-result.yaml
07-targeted-closure-summary-and-handoff.md
```

Do not edit their content to make validation pass.

If any imported member differs from its package bytes, stop.

## Expected semantic result

The completed formal result declares:

```yaml
adversary_result: CLOSURE_CONFIRMED
original_findings:
  confirmed_closed: 14
  routed_confirmed: 1
  reopened: 0
new_findings: 0
regressions: 0
```

Treat this as formal run output pending deterministic import and Controller validation, not as self-applying authority.

Derive the valid Controller transition only from the current versioned loop and protocol contracts.

Do not assume the final state name, counter changes, or exact registry mutations from this prompt when repository contracts can determine them.

## Controller process

Perform:

```text
validate completed package
→ import immutable outputs
→ validate imported state
→ Controller dry-run
→ inspect diagnostics and proposed state/counters
→ apply exactly one transition if unambiguous and authorized
→ validate resulting durable state
```

Record both the dry-run facts and the applied transition evidence.

The formal run must no longer be represented as `NOT_STARTED` after a valid import and transition.

Do not claim the Kernel is ratified, adopted, enforceable, operational, or implemented unless an existing repository contract explicitly and validly produces that state. This authorization does not grant such authority.

## Learning and session review

Use `agent-session-reviewer` before completion.

If any material defect, near miss, ambiguity, tooling gap, unnecessary manual step, or reusable workflow lesson appears:

* preserve it through the learning system;
* classify and route it correctly;
* do not silently repair it;
* include validation evidence;
* stop if correcting it would exceed this authorization.

A material finding does not automatically invalidate the whole execution if it is corrected within the authorized scope, recorded, and fully validated.

## Validation

At minimum, run:

* completed-output package validation;
* imported-output byte/hash verification;
* strict YAML and JSON Schema validation;
* Controller dry-run validation;
* Controller applied-transition validation;
* counter and guard checks;
* affected pytest/Hypothesis tests;
* prompt-custody validation if a material prompt is added;
* learning-system validation;
* skill structure validation;
* registry/generated-view consistency checks;
* `git diff --check`;
* Phase 2.4 review-bundle validation.

Use proportional validation. Do not rerun unrelated expensive checks without evidence that they are affected.

## Prompt custody

Preserve this execution prompt under the next valid `HP-PROMPT-*` identifier and version according to the repository prompt-custody contract.

Do not create recursive publication authority.

## Publication authority

If all authorized work completes successfully, validation passes, no unresolved material blocker remains, and no scope drift occurs:

```text
commit the complete Phase 2.4 delta
push the current branch
verify local and remote HEAD alignment
verify a clean worktree
```

Do not open a pull request.

## Stop conditions

Stop without applying a real Controller transition or publishing if:

* branch or HEAD differs from the expected starting state;
* package hash or member inventory differs;
* schema or parity validation fails;
* repository evidence conflicts with `CLOSURE_CONFIRMED`;
* the valid transition is ambiguous;
* a guard is exhausted;
* counters cannot be calculated deterministically;
* more than one transition would be required;
* Kernel ratification or owner risk acceptance would be required;
* any correction would materially change Controller, loop, protocol, or Kernel semantics;
* validation remains failing.

Preserve blocker evidence and report the exact next action instead of bypassing the contract.

## Completion report

Return:

```text
Branch:
Previous HEAD:
Prompt ID/version:
Skill created:
Files created:
Files modified:
Input package SHA-256:
Imported member count:
Imported outputs byte-identical:
Package validation:
Import validation:
Declared formal result:
Controller dry-run result:
Controller transition applied:
Transition record:
Counters before:
Counters after:
Guards before:
Guards after:
Durable run status:
Kernel status:
Enforcement Engineering status:
Human ratification status:
Tests:
Session-review result:
Material findings:
Learning evidence:
Review bundle:
New commit:
Push:
Local/remote aligned:
Worktree:
Status:
Exact next action:
```
