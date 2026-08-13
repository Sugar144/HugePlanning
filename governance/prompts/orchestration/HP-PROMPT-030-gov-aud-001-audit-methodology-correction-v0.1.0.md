---
prompt_id: HP-PROMPT-030
version: 0.1.0
category: CORRECTION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Implement the bounded Project Owner-authorized GOV-AUD-001 audit methodology correction before any PASS-02 R2 work.
target_environment: Codex
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: a4cbc500b2ca864b2eb35e9354df88c8c3d97a3e
authorization_scope:
  - inspect repository evidence
  - preserve PASS-02 R1 unchanged
  - correct audit methodology and directly affected controls prospectively
  - add deterministic validation and append-only learning evidence
forbidden_actions:
  - prepare or execute PASS-02 R2
  - modify PASS-02 R1 architectural outputs or evidence
  - execute CHECKPOINT-A or PASS-03
  - amend the Kernel
  - design, implement or activate GOV-7
  - modify product, runtime or S0a-S9 implementation
  - accept recommendations or risk
  - stage, commit, push, open a pull request, merge, release or ratify
exact_text_preserved: true
exact_text_sha256: 67cde6858c58d93d169d98f5867de2feb9591290610797c9e72de4aaac8073d6
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/audits/GOV-AUD-001-gov7-enablement/07-audit-methodology-and-review-protocol.yaml
  - governance/tools/validate_audit_methodology.py
  - governance/tests/test_audit_methodology_protocol.py
  - governance/audits/GOV-AUD-001-gov7-enablement/08-methodology-correction-validation.yaml
  - governance/learning/records/HP-FAIL-024.yaml
result_commit: null
supersedes: null
---

# HP-PROMPT-030 — GOV-AUD-001 Audit Methodology Correction

## Exact executed text

# HugePlanning — GOV-AUD-001 Audit Methodology Correction

You are implementing a bounded, Project Owner-authorized methodology correction for the existing `GOV-AUD-001` audit program.

This task corrects the audit methodology before any PASS-02 R2 preparation or execution.

## Repository identity

* Repository: `Sugar144/HugePlanning`
* Required branch: `governance/kernel-designer-revision-v0.1`
* Expected committed HEAD baseline: `a4cbc500b2ca864b2eb35e9354df88c8c3d97a3e`
* Expected worktree: validated but uncommitted PASS-02 R1 candidate may already be present
* PASS-01: accepted and completed
* PASS-02 R1: executed and independently reviewed, but not accepted
* CHECKPOINT-A: pending
* PASS-03: not executed
* GOV-7: inactive
* OD-006: unresolved

Do not assume that the working tree is clean.

## Owner authorization

The Project Owner authorizes this task to:

1. inspect the entire repository read-only where needed;
2. preserve all existing PASS-02 R1 files and evidence unchanged;
3. version and implement a bounded correction to the `GOV-AUD-001` audit methodology;
4. update directly affected audit scaffold, audit protocol, prompt-template, validation, registry, state, navigation, and learning surfaces when materially necessary;
5. create append-only learning evidence directly caused by this correction;
6. add or update deterministic tests and validators needed to enforce the correction.

The Owner does **not** authorize:

* PASS-02 R2 preparation or execution;
* correction of PASS-02 R1 architectural outputs;
* CHECKPOINT-A;
* PASS-03 or later passes;
* Kernel modification or amendment;
* formal GOV-7 policy design or implementation;
* activation of GOV-7;
* product, methodology-runtime, or S0a-S9 implementation changes;
* acceptance of recommendations or risk;
* commit, push, PR, merge, release, or ratification.

## Mandatory startup verification

Before modifying anything, verify and report:

```text
repository root
current branch
local HEAD
remote branch HEAD
staging state
unstaged and untracked files
PASS-02 R1 candidate presence
existing audit-methodology and review-protocol artifacts
current prompt, run, failure, learning, decision, and artifact registries
```

Do not reset, clean, stash, discard, overwrite, or normalize the existing worktree.

If the branch or committed HEAD is wrong, stop.

If uncommitted changes exist, determine whether they belong to PASS-02 R1 or are unrelated. Preserve all PASS-02 R1 evidence.

## Canonical ID resolution

Never assign an identifier from prompt memory or assumption.

Before creating any prompt, run, failure, learning, event, artifact, or other registered identity:

1. inspect the canonical registry or allocation source;
2. determine the next available valid identifier;
3. verify that it is unused across the repository;
4. record the resolution evidence;
5. then bind the identifier prospectively.

If the repository has no canonical allocation mechanism for a required identity, do not invent a competing convention. Record the gap and use the smallest existing compatible mechanism.

## Problem being corrected

The audit currently has strong repository-first and gap-driven principles, but recent PASS-02 work exposed several methodology weaknesses:

1. the audit basis used to identify a finding is not always explicit;
2. model inference can be presented beside stronger evidence without a uniform support classification;
3. reviewers may classify a deviation as invalid before checking whether its root cause is an agent defect, prompt defect, protocol gap, governance gap, tooling defect, or unresolved instruction conflict;
4. validation, targeted confirmation, independent substantive review, and adversarial review are not sufficiently distinguished;
5. adversarial review requirements do not consistently require genuine attempts to refute the candidate;
6. materiality thresholds are insufficiently explicit, which can cause unnecessary correction loops;
7. repository identifiers have previously been proposed from chat memory rather than resolved from canonical registries;
8. a conflict was exposed between mandatory durable learning capture and bounded run write authority.

The instruction-conflict case is not to be resolved now through a Kernel amendment or formal GOV-7 policy. It must be:

* preserved as evidence;
* classified as a candidate governance-policy or operating-protocol gap;
* routed as a proposal for later GOV-7 derivation;
* temporarily controlled through a compact prompt-level rule.

## Required methodology corrections

Implement the smallest coherent durable correction covering the following requirements.

### 1. Explicit audit basis

Every material audit finding must identify one or more bases from a canonical taxonomy equivalent to:

```yaml
finding_basis:
  - NORMATIVE_REQUIREMENT
  - ACCEPTED_OWNER_DIRECTION
  - REPOSITORY_FACT_OR_CONTRADICTION
  - OBSERVED_FAILURE_OR_BURDEN
  - ARCHITECTURAL_INVARIANT
  - EXTERNAL_EVIDENCE
  - ADVERSARIAL_COUNTEREXAMPLE
  - MODEL_INFERENCE_ONLY
```

You may refine names to match repository conventions, but preserve the semantic distinctions.

A finding supported only by model reasoning must be visibly classified as such and must not be represented as a verified fact.

Define the required follow-up for `MODEL_INFERENCE_ONLY`, such as adversarial testing, external validation, empirical evidence, or Project Owner disposition.

Do not require external evidence for every finding. Repository facts, normative requirements, observed failures, and valid architectural reasoning remain legitimate bases.

### 2. Root cause before invalidity

A reviewer must not classify an execution as invalid merely because a deviation exists.

Require this reasoning sequence:

```text
observed deviation
→ applicable instruction and authority sources
→ hierarchy or conflict analysis
→ available compliant alternatives
→ root-cause layer
→ authority and evidence impact
→ materiality
→ execution-validity conclusion
```

Use or derive a canonical root-cause taxonomy equivalent to:

```yaml
root_cause_layer:
  - AGENT_EXECUTION_DEFECT
  - RUN_PROMPT_DEFECT
  - OPERATING_PROTOCOL_GAP
  - GOVERNANCE_POLICY_GAP
  - TOOLING_DEFECT
  - AMBIGUOUS_OR_CONFLICTING_AUTHORITY
  - INSUFFICIENT_EVIDENCE
```

A beneficial action may still be formally ambiguous. The review model must be able to distinguish:

```yaml
agent_action_value:
  - BENEFICIAL
  - NEUTRAL
  - HARMFUL

formal_conformance:
  - CONFORMANT
  - NONCONFORMANT
  - AMBIGUOUS
```

Do not make these exact field names mandatory if the repository already has a better canonical schema, but preserve the concepts.

### 3. Review-type separation

Define and distinguish at least:

```text
DETERMINISTIC_VALIDATION
TARGETED_CONFIRMATION
INDEPENDENT_SUBSTANTIVE_REVIEW
ADVERSARIAL_REVIEW
```

For each type, define:

* purpose;
* allowed conclusions;
* required independence;
* minimum evidence;
* what it must not claim.

An adversarial review must attempt to refute the candidate rather than merely confirm correction or compliance.

Its required attack dimensions must include, when applicable:

* concrete counterexamples;
* smallest sufficient rival design;
* authority leakage or circular authority;
* evidence loss, contradiction, rewriting, or provenance failure;
* version, migration, compatibility, and rollback failure;
* recovery and manual-escape failure;
* self-hosting capture or self-certification;
* excessive Owner burden or operational bureaucracy;
* unsupported assumptions and reasonable unknown unknowns.

Do not force invented findings. A reviewer may conclude that a candidate survived an attack only after recording the attempted attack and the supporting evidence.

### 4. Materiality threshold

Define a bounded materiality rule.

A finding is blocking only when it materially affects at least one of:

```text
authority
trust root
evidence integrity
canonical ownership
traceability
decision validity
compatibility or migration
recovery or rollback
independent evaluation
scope discipline
a required contracted output
a Project Owner checkpoint decision
```

Stylistic preferences, optional refinements, speculative improvements, and non-material documentation polish must not automatically block a pass.

Require non-blocking items to be classified as appropriate, such as:

```text
NON_BLOCKING
OPTIONAL_IMPROVEMENT
FOLLOW_UP_CANDIDATE
RESEARCH_REQUIRED
OWNER_DECISION_REQUIRED
```

Do not create an exhaustive bureaucracy of severity levels. Reuse existing classifications where sufficient.

### 5. Compact temporary instruction-conflict rule

Until GOV-7 derives a formal policy, standard, and procedure, add a compact reusable rule to the appropriate audit run and review prompt template or canonical prompt guidance.

Use this semantic rule, adjusting wording only for clarity and repository style:

```text
Instruction conflicts: Durable instructions do not silently expand run authority,
and run prompts do not silently suppress durable obligations. Append-only learning
evidence caused by the current run may be preserved when it changes no authority,
accepted state, prior evidence, implementation, or risk; record the exception.
Otherwise stop before acting and request Project Owner authority.
```

Add the corresponding reviewer rule:

```text
Before declaring an execution invalid, determine whether the deviation arose from
an agent defect, prompt defect, protocol gap, governance gap, tooling defect, or
unresolved instruction conflict.
```

Keep these rules compact. Do not duplicate a large policy in every prompt.

Document that this is a temporary operating control and a candidate input for future GOV-7 policy derivation, not an adopted policy or Kernel amendment.

### 6. Canonical ID-resolution rule

Add a compact durable rule equivalent to:

```text
Never assign repository identities from chat memory. Resolve and verify the next
available identity from canonical repository registries before prospective custody
or repository modification.
```

Reuse existing registry mechanisms. Do not create a second identity authority.

### 7. Finding traceability

Each material methodology correction must trace:

```text
observed event or problem
→ methodology requirement
→ changed canonical artifact
→ validator or review control where applicable
→ evidence of validation
→ future GOV-7 proposal or deferral where applicable
```

The instruction-conflict finding must be routed to the existing proposal, learning, or future-work mechanism without activating GOV-7.

## Scope discipline

Prefer editing existing canonical artifacts over creating new layers or parallel frameworks.

Do not:

* create a new governance layer;
* redesign the entire audit;
* rewrite immutable completed-run evidence;
* retroactively change PASS-02 R1 authority;
* silently reclassify the independent review;
* declare PASS-02 R1 accepted or corrected;
* change the Kernel;
* implement the future conflict policy;
* add broad external research;
* introduce tools or graph technology;
* prepare PASS-02 R2.

If an existing artifact already covers a requirement, strengthen it rather than creating a duplicate.

## PASS-02 R1 preservation

PASS-02 R1 and its review are historical evidence.

Do not modify their completed prompts, inputs, outputs, manifests, authorization, validation reports, review text, or recorded hashes.

If the independent review is not durably custodied in the repository:

* report that fact;
* do not fabricate or reconstruct its exact contents;
* create only a prospective placeholder or follow-up record if an existing protocol requires one and the current authorization permits it;
* preserve the Project Owner-provided disposition as an Owner statement only when a canonical mechanism supports doing so without rewriting history.

## Validation requirements

Add or update deterministic validation only where it provides real control.

At minimum validate, where technically feasible:

1. allowed audit finding-basis values;
2. required explicit marking of model-inference-only findings;
3. review-type identity and required contract sections;
4. root-cause classification before invalidity for new review artifacts;
5. presence of the compact instruction-conflict rule in the canonical template or guidance;
6. canonical ID-resolution requirement;
7. absence of modifications to immutable PASS-02 R1 custody;
8. no accidental activation of CHECKPOINT-A, PASS-03, GOV-7, OD-006, or Kernel amendment;
9. state and navigation consistency for files changed by this task.

Tests must be generic and semantic where possible. Do not hardcode this one incident or specific future finding IDs as the only accepted behavior.

Run:

```text
focused tests for this correction
existing governance validation suite
prompt/state validators
git diff --check
repository status inspection
```

Run broader tests only when the modified surfaces make them relevant.

## Required final report

Return a concise report containing:

```text
Repository
Branch
Committed HEAD
Initial worktree state
Resolved new identities and evidence
Files created
Files modified
Immutable files verified unchanged
Methodology corrections implemented
Temporary conflict rule location
Future GOV-7 proposal routing
Learning records created or updated
Validation commands and exact results
Remaining limitations
PASS-02 R2 prepared: NO
CHECKPOINT-A executed: NO
Commit authorized: NO
Push authorized: NO
Exact next action
```

Also classify every changed file as one of:

```text
AUDIT_METHODOLOGY
PROMPT_OR_REVIEW_CONTROL
VALIDATION_OR_TEST
STATE_OR_REGISTRY
LEARNING_OR_PROPOSAL_CUSTODY
NAVIGATION
```

Stop after validation. Do not commit or push.
