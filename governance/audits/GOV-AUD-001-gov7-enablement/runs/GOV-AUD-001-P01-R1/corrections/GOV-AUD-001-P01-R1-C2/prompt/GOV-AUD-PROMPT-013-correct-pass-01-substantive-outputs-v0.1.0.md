# HugePlanning — GOV-AUD-001 PASS-01 Bounded Substantive Correction

```yaml
repository: Sugar144/HugePlanning
branch: governance/kernel-designer-revision-v0.1
expected_head: 22b66c97851316b4c461077f057fc3f1bc2de851

source_audit: GOV-AUD-001
source_pass: PASS-01
source_run: GOV-AUD-001-P01-R1
prior_correction: GOV-AUD-001-P01-R1-C1

target_correction: GOV-AUD-001-P01-R1-C2
target_prompt: GOV-AUD-PROMPT-013
catalog_prompt: HP-PROMPT-026
prompt_version: 0.1.0
target_authorization: GOV-AUD-CORR-AUTH-002
authorization_version: 0.1.0

role: Repository Capability and Gap Audit Corrector
mode: BOUNDED_SUBSTANTIVE_OUTPUT_CORRECTION
```

## Project Owner authorization

The Project Owner has authorized a bounded substantive correction of the validated but unaccepted GOV-AUD-001 PASS-01 outputs.

This authorization permits:

* read-only inspection of the repository;
* creation of correction `GOV-AUD-001-P01-R1-C2`;
* bounded corrective analysis;
* creation of new corrected outputs;
* deterministic validation;
* directly necessary audit lifecycle, registry, state, learning, validator and regression-test updates;
* modification of the local worktree.

This authorization does **not** permit:

* modifying any immutable PASS-01 R1 or C1 evidence;
* accepting PASS-01;
* authorizing or executing PASS-02;
* completing CHECKPOINT-A;
* activating, designing or implementing GOV-7;
* selecting architecture, graph technology, provider, framework, workflow engine or GOV-7 strategy;
* resolving OD-006;
* accepting residual risk;
* modifying Kernel substance or ratification evidence;
* modifying planning, product or released runtime substance;
* committing;
* pushing;
* opening or updating a pull request;
* merging, tagging, releasing or deploying.

Stop after presenting the validated uncommitted candidate.

## 1. Initial repository verification

Before modifying anything:

1. Read every applicable `AGENTS.md`.
2. Read:

   * `governance/README.md`
   * `governance/CURRENT_STATE.md`
   * `governance/GOVERNANCE_MASTER_PLAN.md`
   * `governance/methodology/project-operating-contract.md`
   * the GOV-AUD-001 charter, plan, status, custody contract and PASS-01 contract.
3. Verify:

   * current branch;
   * local HEAD;
   * remote branch HEAD;
   * local/remote alignment;
   * clean worktree;
   * empty staging area.
4. Verify the expected branch and HEAD exactly.
5. Verify that none of these identities already exists:

   * `GOV-AUD-001-P01-R1-C2`
   * `GOV-AUD-CORR-AUTH-002`
   * `GOV-AUD-PROMPT-013`
   * `HP-PROMPT-026`
   * `HP-FAIL-022`

Stop without modification on any mismatch, collision, divergence, dirty worktree, authority conflict or material ambiguity.

## 2. Immutable evidence

Do not modify, normalize, replace or regenerate anything under:

```text
governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/output/
governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/prompt/
governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/authorization/
governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/input/
governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/evaluation/
governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/corrections/GOV-AUD-001-P01-R1-C1/
```

Before substantive work, calculate and preserve the SHA-256 hashes of the four original PASS-01 outputs and verify that they remain byte-identical at the end.

The correction must link, not overwrite:

* PASS-01 R1;
* correction C1;
* the four original outputs;
* the original validation report;
* the current repository HEAD;
* the Project Owner evidence-review disposition that returned PASS-01 for bounded correction.

## 3. Applicable defect basis

The correction must address only these reviewed defects.

### DEFECT-01 — Stale post-C1 capability description

The original PASS-01 handoff states that `validate_audit_scaffold.py` is planning-only and rejects instantiated runs.

That statement is no longer true at the current HEAD. Correction C1 extended the validator to support both:

* the planning-only lifecycle;
* the lifecycle with one executed PASS-01 run and its correction evidence.

Re-baseline CAP-005, GAP-002, the burden analysis and the handoff against the current implementation.

Do not erase the historical fact that the planning-only limitation existed during the original execution.

Clearly distinguish:

```text
historical capability at PASS-01 R1 execution
current capability after C1
remaining demonstrated residual gap
```

### DEFECT-02 — Materially incomplete capability scope

The original input manifest excluded most released runtime and product-support surfaces.

Inspect implemented or execution-backed repository capabilities materially relevant to PASS-01, including as applicable:

```text
README.md
VERSION
CHANGELOG.md
CLAUDE.md
.claude/
schemas/
scripts/
templates/
tests/
knowledge/
reports/experiments/
product/ verification and implementation evidence only
```

At minimum inspect and classify the implemented evidence for:

* client-repository creation;
* methodology-lock binding;
* clean-checkout guards;
* session launch guards;
* the progressive client validator;
* schema validation;
* ID/reference integrity;
* profile-aware required-artifact checks;
* derived status reporting;
* smoke checks;
* deny-rule protection;
* runtime test and scenario evidence.

Do not inventory every file individually.

Aggregate related mechanisms into capability families.

A plan, roadmap, task description or unexecuted template is not implementation evidence.

### DEFECT-03 — GAP-001 overgeneralization

Preserve the demonstrated KGR-006 prospective-custody failure.

Separate:

1. the demonstrated failure;
2. the specialized KGR-006-R1 correction capability;
3. the unproven proposition that HugePlanning currently requires one generic execution-lifecycle gate.

Recalculate confidence, residual scope, evidence priority and preliminary leverage.

Do not classify genericization itself as a verified fact unless multiple materially distinct workflows demonstrate the need.

### DEFECT-04 — GAP-003 overaggregation

The original GAP-003 combines distinct problem classes:

* incomplete package/import validation profiles;
* brittle assertions tied to mutable wording;
* canonical counts copied from prose;
* omitted canonical relationship anchors;
* duplicated meaning-bearing safety boundaries;
* validation-profile conflicts between immutable and authored files.

Preserve the demonstrated pattern, but represent its subproblems explicitly.

Do not imply that one generic “parity enforcement” mechanism is already demonstrated as the smallest sufficient response.

Retain bounded semantic or independent review for facts not machine-settleable.

### DEFECT-05 — Ranking and trigger semantics

Correct the following:

* `NOT_A_GAP` entries must not use `preliminary_leverage: HIGH`.
* Use `UNKNOWN` plus an explicit `NOT_APPLICABLE_NOT_A_GAP` leverage status where required by the existing value vocabulary.
* Trigger-gated legal, provider, recovery and high-consequence usability needs must not appear as unconditional universal P0 work.
* Use the existing allowed priority value plus a separate explicit conditional priority such as:

```yaml
priority: DEFER
conditional_priority: P0_IF_TRIGGER_ACTIVATES_FOR_SELECTED_SCOPE
```

* Requirement coverage must never imply implementation coverage.
* State prominently that KGR-006-R1 found zero of ER-001 through ER-020 fully supported by implementation evidence.

### DEFECT-06 — Overbroad stop-rereading recommendation

Retain the recommendation against indiscriminate historical rereading, but qualify it.

Validated manifests, indexes and decision records may settle an unchanged exact claim.

Source inspection remains required when:

* the claim is new;
* repository implementation changed;
* a generated view may be stale;
* a contradiction exists;
* provenance is disputed;
* semantic fidelity is under review;
* the new audit scope differs materially from the previous one.

## 4. Required correction structure

Create:

```text
governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/corrections/GOV-AUD-001-P01-R1-C2/
├── authorization/
│   └── GOV-AUD-CORR-AUTH-002-v0.1.0.yaml
├── prompt/
│   └── GOV-AUD-PROMPT-013-correct-pass-01-substantive-outputs-v0.1.0.md
├── input/
│   └── input-manifest.yaml
├── output/
│   ├── 01-corrected-verified-capability-inventory.yaml
│   ├── 02-corrected-repetition-waste-and-burden-analysis.md
│   ├── 03-corrected-ranked-gap-register.yaml
│   └── 04-corrected-pass-01-findings-and-handoff.md
├── evaluation/
│   └── correction-validation-report.yaml
└── manifest.yaml
```

The correction manifest must state:

```yaml
source_run_id: GOV-AUD-001-P01-R1
prior_correction_id: GOV-AUD-001-P01-R1-C1
original_outputs_modified: false
pass_01_accepted: false
independent_evaluation_completed: false
checkpoint_a_completed: false
pass_02_authorized_or_executed: false
gov_7_activated: false
recommendations_accepted: false
implementation_authorized: false
od_006_status: UNRESOLVED_TRIGGER_GATED
```

Use an honest terminal status equivalent to:

```text
EXECUTED_VALIDATED_PENDING_INDEPENDENT_EVALUATION_AND_PROJECT_OWNER_DISPOSITION
```

Do not call the correction accepted, independently evaluated or ready for PASS-02.

## 5. Input manifest

Bind only materially used evidence.

It must include:

* exact branch and starting HEAD;
* exact correction prompt and authorization;
* PASS-01 contract and custody contract;
* PASS-01 R1 manifest, input manifest and validation report;
* correction C1 manifest, prompt, authorization and affected validator/test evidence;
* the four immutable R1 outputs;
* applicable current governance state and decision records;
* relevant learning records;
* current runtime implementation evidence;
* current runtime validation or execution evidence;
* explicit exclusions;
* missing-data markers.

For every input, record:

* repository path;
* SHA-256;
* evidentiary role.

Do not bind broad directories without an exact member inventory.

## 6. Corrected output requirements

### 01 — Corrected capability inventory

Record:

* implemented or execution-backed capability families;
* owning components;
* exact evidence paths;
* current use;
* limitations;
* reuse boundaries;
* whether the capability existed at R1 execution or was added by C1;
* which apparent gaps it already solves;
* whether it is governance-local, runtime-local or cross-layer.

Clearly distinguish:

```text
EXISTING_IMPLEMENTED_CAPABILITY
EXISTING_EXECUTED_CAPABILITY
PARTIAL_CAPABILITY
PLANNED_ONLY_NOT_CAPABILITY
HISTORICAL_CAPABILITY_SUPERSEDED_BY_CURRENT_IMPLEMENTATION
```

Do not claim GOV-7 implementation.

### 02 — Corrected repetition, waste and burden analysis

Preserve supported historical counts and unknown markers.

Correct:

* the current validator description;
* the overly broad rereading recommendation;
* repeated work already addressed by C1;
* runtime mechanisms that already prevent duplicate work;
* historical versus residual burden.

Do not fabricate tokens, time, cost, tool calls or Owner minutes.

### 03 — Corrected ranked gap register

For every original GAP-001 through GAP-014:

* preserve traceability;
* record whether it is retained, narrowed, split, reclassified, conditionally deferred or rejected;
* explain the correction;
* recalculate affected scoring and confidence;
* distinguish historical failure from current residual gap;
* include missing-data markers;
* retain strategy neutrality.

GAP-003 may contain a structured subproblem register, but do not silently discard the original identity.

Do not force the original number of demonstrated gaps if current evidence supports a different count.

### 04 — Corrected findings and handoff

Keep it concise.

Include:

* correction result;
* capabilities newly recognized or re-baselined;
* current residual demonstrated gaps;
* corrected stop-doing conclusions;
* ranking limitations;
* trigger conditions;
* explicit PASS-02 reservations;
* unchanged authority boundaries;
* requirement for independent evaluation and Project Owner disposition before any PASS-02 use.

Do not state that PASS-02 may use the correction as an accepted input.

## 7. Learning record

Create `HP-FAIL-022` unless that identity already exists.

Suggested title:

```text
PASS-01 outputs became stale after lifecycle correction and omitted material implemented runtime capabilities
```

The record must capture:

* expectation;
* observed event;
* impact on PASS-01 acceptance;
* immediate cause;
* systemic cause;
* correction;
* prevention;
* reusable lesson;
* affected phases;
* exact evidence;
* unavailable metrics.

Use subfindings if necessary to distinguish:

1. stale post-C1 claims;
2. incomplete capability scope;
3. insufficient separation of demonstrated failure from generalized solution.

Do not mark the learning record validated until the correction and all declared validation pass.

Regenerate learning views only through the canonical learning tool.

## 8. Directly affected repository surfaces

Update only where required:

```text
governance/audits/GOV-AUD-001-gov7-enablement/**
governance/tools/validate_audit_scaffold.py
governance/tests/test_gov_7_audit_scaffold.py
governance/prompts/orchestration/**
governance/ARTIFACT_REGISTRY.yaml
governance/learning/**
governance/CURRENT_STATE.md
governance/GOVERNANCE_MASTER_PLAN.md
governance/README.md
directly affected governance state/checksum surfaces
```

Do not modify released runtime files merely because they are inspected as evidence.

Extend lifecycle validation only as necessary to represent C2.

Do not weaken existing planning-only, R1, C1, authority, immutability or PASS-02 guards.

## 9. Required deterministic validation

Run and preserve exact results for:

```bash
python3 governance/tools/validate_audit_scaffold.py
python3 governance/tools/validate_prompts.py --root repository
bash governance/tests/run-prompt-custody-tests.sh
python3 governance/tools/manage_learning.py validate
python3 governance/tools/validate_governance_state.py
sha256sum -c governance/SOURCE_CHECKSUMS.sha256
```

Run focused audit lifecycle tests.

Run the complete governance suite using the repository-supported environment:

```bash
python -m pytest -q -p no:cacheprovider governance/tests
```

Run the released methodology runtime suite because current runtime capabilities are used as evidence:

```bash
tests/run-tests.sh
```

Also verify:

* all four original R1 output hashes remain unchanged;
* all C1 artifacts remain unchanged;
* every C2 input hash matches;
* every evidence path exists;
* corrected YAML parses strictly;
* Markdown fences and local links are valid;
* IDs are unique;
* ranking arithmetic is correct;
* rejected or unknown items do not receive fabricated scores;
* no planning, product or runtime file was modified;
* PASS-02 remains unexecuted;
* CHECKPOINT-A remains pending;
* GOV-7 remains inactive;
* OD-006 remains unresolved;
* Kernel remains ratified but not implemented, enforceable or operational;
* no recommendation or risk was accepted.

Run `git diff --check` over authored correction paths.

Do not normalize or modify immutable evidence to satisfy formatting checks.

## 10. Independent-evaluation boundary

This correction task performs source correction and deterministic validation only.

It must not create an independent substantive evaluation of its own outputs.

The manifest and handoff must state that a separately controlled evidence review is required before Project Owner disposition.

## 11. Stop before publication

Do not stage, commit or push.

At completion, return:

1. verified starting branch, HEAD and clean state;
2. concise correction summary;
3. exact files created and modified;
4. original immutable hashes and final comparison result;
5. focused validation results;
6. full governance suite result;
7. released runtime suite result;
8. remaining uncertainties and reservations;
9. `git status --short`;
10. `git diff --stat`;
11. a concise diff review guide;
12. explicit confirmation that no commit, push, PR, merge, tag, release or deployment occurred.

Use honest status language.

The final response must end with:

```text
Current phase:
Current run:
Status:
Open blockers:
Owner decisions required:
Repository changes:
Exact next action:
```
