# GOV-AUD-PROMPT-015 — Correct PASS-01 C2 Classification and Temporal Semantics

```yaml
prompt_id: GOV-AUD-PROMPT-015
version: 0.1.0
audit_id: GOV-AUD-001
correction_id: GOV-AUD-001-P01-R1-C3
corrects: GOV-AUD-001-P01-R1-C2
review_source: GOV-AUD-001-P01-C2-IER-001
finding_addressed: GOV-AUD-001-P01-C2-IER-F001
role: PASS-01 Evidence Correction Author
mode: BOUNDED_CLASSIFICATION_AND_TEMPORAL_SEMANTICS_CORRECTION
authority: PROJECT_OWNER_EXPLICIT
repository: Sugar144/HugePlanning
expected_branch: governance/kernel-designer-revision-v0.1
expected_head: 22b66c97851316b4c461077f057fc3f1bc2de851
```

## Objective

Create a bounded versioned correction `GOV-AUD-001-P01-R1-C3` that resolves only independent finding:

```text
GOV-AUD-001-P01-C2-IER-F001
```

Correct the PASS-01 classification contract and historical/current/conditional semantics without altering R1, C1 or C2.

Do not re-execute PASS-01.

Do not modify unaffected substantive conclusions.

Do not commit or push.

## Startup verification

Run from the repository root.

Before modification verify:

* branch is `governance/kernel-designer-revision-v0.1`;
* local and remote HEAD are `22b66c97851316b4c461077f057fc3f1bc2de851`;
* staging is empty;
* the validated uncommitted C2 candidate is present;
* R1, C1 and C2 match their recorded hashes;
* the independent review result is `RETURN_FOR_BOUNDED_VERSIONED_CORRECTION`;
* finding `GOV-AUD-001-P01-C2-IER-F001` exists exactly as reviewed;
* identity `GOV-AUD-001-P01-R1-C3` does not already exist;
* GOV-7 remains inactive;
* PASS-02 remains unauthorized;
* OD-006 remains unresolved.

Stop and report any mismatch. Do not repair conflicts silently.

## Authorized scope

Create a new immutable correction directory:

```text
governance/audits/GOV-AUD-001-gov7-enablement/runs/
GOV-AUD-001-P01-R1/corrections/GOV-AUD-001-P01-R1-C3/
```

Authorized changes are limited to:

* C3 authorization;
* exact C3 prompt custody;
* C3 input manifest;
* corrected gap register;
* directly affected corrected handoff;
* C3 validation report;
* C3 manifest;
* minimal lifecycle and registry updates;
* minimal validator and regression-test changes enforcing the closed classification vocabulary and temporal separation;
* append-only learning evidence only when required by the repository learning contract.

Do not modify R1, C1 or C2 files.

Do not modify unaffected capability inventory or repetition/burden analysis unless a direct reference must be corrected for consistency.

## Canonical classification vocabulary

Every material PASS-01 item must use exactly one canonical classification:

```text
EXISTING_CAPABILITY
PARTIAL_CAPABILITY
DEMONSTRATED_GAP
REQUIREMENT_WITHOUT_IMPLEMENTATION
RESEARCH_REQUIRED
OWNER_DECISION_REQUIRED
NOT_A_GAP
```

Do not add qualifiers to the classification field.

Represent other dimensions separately.

At minimum support fields equivalent to:

```yaml
classification: DEMONSTRATED_GAP
temporal_status: HISTORICAL_CORRECTED
current_residual_status: NOT_DEMONSTRATED
recurrence_status: UNKNOWN
future_extension_status: CONDITIONAL
```

Use the smallest vocabulary compatible with existing repository conventions.

Do not create a global schema unless necessary.

## Required correction

### 1. GAP-002 and GAP-003

Reassess GAP-002 and GAP-003 using the actual evidence.

Do not classify either as a current residual gap unless repository evidence demonstrates that the problem remains unresolved or recurred after the validated correction.

Distinguish:

```text
historical failure
historical correction
validated correction
known later recurrence
unknown later recurrence
current demonstrated residual gap
conditional future extension need
```

Where the cited failures have corrected and validated terminal evidence and no later failure sample exists, state explicitly:

```text
current residual gap: NOT_DEMONSTRATED
post-correction recurrence: UNKNOWN
historical significance: PRESERVED
```

Historical scores may be retained only when clearly labeled as historical and not used to claim current priority.

### 2. GAP-003 subproblems

Preserve the useful six-part decomposition.

For every subproblem:

* use a canonical classification;
* declare temporal status;
* declare whether a current residual gap is demonstrated;
* declare whether the score is historical, current or conditional;
* preserve evidence and confidence;
* avoid aggregating corrected historical incidents into a current heterogeneous residual pattern without current evidence.

### 3. Gap register

Create:

```text
output/03-corrected-ranked-gap-register.yaml
```

The C3 version must:

* contain only canonical classification values;
* separate classification from temporal and recurrence status;
* preserve historical evidence;
* avoid current-gap claims unsupported by post-correction evidence;
* retain `UNKNOWN` where recurrence is not observable;
* keep priority conditional when current evidence is absent;
* preserve all unaffected validated C2 conclusions.

### 4. Handoff

Create:

```text
output/04-corrected-pass-01-findings-and-handoff.md
```

Update only the conclusions affected by F001.

The handoff must let the Owner distinguish:

* current demonstrated gaps;
* historical corrected failures;
* partial capabilities;
* conditional future-extension needs;
* unknown recurrence.

Do not imply that historical correction removes learning value.

Do not imply that unknown recurrence proves closure universally.

### 5. Validation report

Create:

```text
evaluation/correction-validation-report.yaml
```

It must not declare the correction valid unless:

* all classifications use the closed vocabulary;
* no historical corrected item is represented as a current residual gap without evidence;
* temporal and recurrence fields are present where required;
* ranking semantics match their declared time basis;
* handoff and gap register agree;
* R1, C1 and C2 remain immutable.

## Validator and test correction

Modify only the smallest validator and test support required to detect F001 prospectively.

Validation must reject:

* classifications outside the canonical seven-value vocabulary;
* compound classification values containing temporal qualifiers;
* current residual-gap claims with only historical corrected evidence;
* current rankings based solely on historical scores without an explicit historical or conditional label;
* disagreement between the gap register and handoff.

Do not encode C3 conclusions as fixed truth.

The validator should validate structure and evidence semantics, not decide whether a specific future gap exists.

## Required validation

Run:

1. C3-specific validator checks;
2. affected GOV-7 audit scaffold tests;
3. prompt-custody validation;
4. learning validation if learning artifacts change;
5. governance-state validation;
6. source checksum validation;
7. YAML, Markdown, IDs, links, evidence paths and arithmetic checks;
8. `git diff --check`.

Because executable validator/test support will be modified, run:

```text
full governance suite
published runtime suite
```

Both must pass.

Preserve any supported isolated environment used to run `pytest`.

Do not claim the system Python contains `pytest` if it does not.

## Required status

If validation succeeds, set C3 to an honest equivalent of:

```text
EXECUTED_VALIDATED_PENDING_INDEPENDENT_EVALUATION_AND_PROJECT_OWNER_DISPOSITION
```

Keep:

```text
PASS-01: NOT_ACCEPTED
PASS-02: NOT_AUTHORIZED
GOV-7: INACTIVE
OD-006: UNRESOLVED_TRIGGER_GATED
```

Do not mark the independent finding closed by self-assessment.

Record it as addressed by C3 pending independent confirmation.

## Prohibited actions

Do not:

* alter R1, C1 or C2;
* re-run PASS-01;
* reconsider the 14 capability families;
* reopen GAP-001;
* change ER-001–ER-020 treatment;
* add new substantive gaps;
* research tools;
* design architecture;
* select GOV-7 strategy;
* execute PASS-02;
* accept PASS-01;
* resolve OD-006;
* activate or implement GOV-7;
* accept risk;
* commit;
* push;
* open a PR;
* merge, tag, release or deploy.

## Required return

Return only:

```text
Repository:
Branch:
HEAD:
Startup verification:
Correction ID:
Corrected finding:
R1 immutability:
C1 immutability:
C2 immutability:
Canonical classification vocabulary:
GAP-002 final treatment:
GAP-003 final treatment:
Historical/current separation:
Files created:
Files modified:
Validator changes:
Test changes:
Learning changes:
Validation:
Focused tests:
Full governance suite:
Published runtime suite:
Staging:
Worktree:
PASS-01 status:
PASS-02 status:
GOV-7 status:
OD-006 status:
Commit:
Push:
Status:
Blockers:
Exact next action:
```

Expected status:

```text
C3_EXECUTED_VALIDATED_PENDING_INDEPENDENT_CONFIRMATION_AND_PROJECT_OWNER_DISPOSITION
```

Expected next action:

```text
Conduct a separately controlled independent review limited to confirmation that C3 resolved GOV-AUD-001-P01-C2-IER-F001 without introducing a material regression.
```
