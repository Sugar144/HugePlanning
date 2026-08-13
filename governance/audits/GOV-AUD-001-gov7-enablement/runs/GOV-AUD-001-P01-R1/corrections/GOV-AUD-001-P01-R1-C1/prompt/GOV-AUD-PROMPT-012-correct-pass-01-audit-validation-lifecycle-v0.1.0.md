# GOV-AUD-PROMPT-012 — Correct PASS-01 Audit Validation Lifecycle

prompt_id: GOV-AUD-PROMPT-012
catalog_prompt_id: HP-PROMPT-025
version: 0.1.0
audit_id: GOV-AUD-001
source_run_id: GOV-AUD-001-P01-R1
correction_id: GOV-AUD-001-P01-R1-C1
role: Audit Validation Lifecycle Corrector
mode: BOUNDED_VERSIONED_VALIDATION_CORRECTION
authority: PROJECT_OWNER_EXPLICIT
repository: Sugar144/HugePlanning
expected_branch: governance/kernel-designer-revision-v0.1
expected_head: f4329d011e6006877b9a620fbd646f1c64815c30

## Objective

Perform one bounded, versioned correction of the PASS-01 validation lifecycle.

Correct the shared audit-scaffold validator and its directly affected regression tests so they validate both:

1. the original planning-only scaffold state; and
2. the legitimate state after one audit pass has been executed and registered.

Then correct the published PASS-01 validation evidence and only the directly affected audit status, run manifest, registry, checksum and learning records required by existing repository contracts.

Rerun the complete governance test suite.

Do not modify or re-execute the substantive PASS-01 analysis.

Do not execute PASS-02.

## Known defect

PASS-01 was executed and published in commit:

f4329d011e6006877b9a620fbd646f1c64815c30

The following substantive PASS-01 outputs were created:

- governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/output/01-verified-capability-inventory.yaml
- governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/output/02-repetition-waste-and-burden-analysis.md
- governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/output/03-ranked-gap-register.yaml
- governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/output/04-pass-01-findings-and-handoff.md

Targeted validation passed.

The complete governance suite produced:

141 passed
3 failed

The failures were reported in:

- validate_audit_scaffold.py
- test_gov_7_audit_scaffold.py

The existing validator and tests permanently assume:

- zero executed audit passes; and
- no audit run directory.

Those assumptions were valid only for the initial:

PLANNED_NOT_EXECUTED

scaffold state.

They are invalid after a legitimate PASS-01 execution.

This is a shared validation-contract lifecycle defect.

It is not evidence that the four substantive PASS-01 outputs are semantically correct or incorrect.

PASS-01 remains executed and published but not fully validated or accepted.

## Authority

This prompt authorizes:

- inspection of the current audit state;
- reproduction of the three reported failures;
- correction of the smallest shared validator logic responsible for the lifecycle defect;
- correction or extension of the directly affected tests;
- focused regression coverage for the planning-only and one-pass-executed states;
- correction of the published PASS-01 validation report;
- reconciliation of only the directly affected audit status, run manifest, registry, generated views and checksums required by current repository contracts;
- append-only learning capture for this material defect;
- exact prompt custody for this correction;
- required validation;
- one bounded correction commit;
- one non-force push.

This prompt does not authorize:

- changing the four substantive PASS-01 outputs;
- repeating PASS-01 analysis;
- accepting PASS-01 findings;
- completing CHECKPOINT-A;
- executing PASS-02 or any later pass;
- activating or implementing GOV-7;
- selecting architecture, graph technology, tools or GOV-7 strategy;
- modifying Kernel substance or ratification evidence;
- resolving OD-006;
- accepting recommendations or residual risk;
- opening a pull request;
- merging;
- tagging;
- releasing;
- deploying.

## Startup verification

Before modification:

1. Read the applicable root, governance and audit instructions.

2. Verify:

   - current branch is:
     governance/kernel-designer-revision-v0.1

   - current local HEAD is:
     f4329d011e6006877b9a620fbd646f1c64815c30

   - current remote HEAD is identical;

   - local and remote are aligned;

   - worktree is clean;

   - staging area is empty;

   - commit f4329d011e6006877b9a620fbd646f1c64815c30 is published;

   - GOV-AUD-001-P01-R1 exists;

   - GOV-AUD-AUTH-001 is consumed exactly 1/1;

   - GOV-AUD-PROMPT-011 and HP-PROMPT-024 remain preserved unchanged;

   - PASS-01 is executed and published but not accepted;

   - CHECKPOINT-A remains pending;

   - PASS-02 remains unexecuted;

   - GOV-7 remains inactive;

   - OD-006 remains unresolved and trigger-gated;

   - Kernel 0.2.0 remains RATIFIED, not implemented, enforceable or operational;

   - correction identities GOV-AUD-PROMPT-012, HP-PROMPT-025 and GOV-AUD-001-P01-R1-C1 do not already exist.

3. Reproduce the three reported full-suite failures before changing code.

4. Identify the exact validator paths, fixtures, tests and assertions that encode the planning-only assumptions.

Stop without modification if:

- branch or HEAD differs;
- local and remote diverge;
- worktree or staging is not clean;
- the three failures cannot be reproduced;
- the defect has already been corrected;
- correction identities conflict;
- PASS-01 substantive outputs have changed since publication;
- PASS-02 has been executed;
- GOV-7 has been activated;
- unrelated material failures make this bounded correction invalid.

Do not repair unrelated defects silently.

## Exact prompt custody

Preserve this complete received prompt verbatim under the existing prompt-custody system as:

GOV-AUD-PROMPT-012 / HP-PROMPT-025 / 0.1.0

Calculate and record its SHA-256 before substantive modification.

Do not modify or overwrite:

- GOV-AUD-PROMPT-011;
- HP-PROMPT-024;
- GOV-AUD-AUTH-001;
- completed PASS-01 inputs;
- completed PASS-01 outputs.

Use a new correction authorization record if required by current repository conventions.

Do not represent the already-consumed GOV-AUD-AUTH-001 as reusable authority.

## Required correction

### 1. Replace snapshot assumptions with lifecycle-aware validation

Correct the smallest applicable shared audit validator so it validates the audit according to its canonical current lifecycle state.

At minimum, support these valid states.

#### State A — Planning-only scaffold

- audit status:
  PLANNED_NOT_EXECUTED

- passes executed:
  0

- PASS-01:
  PLANNED_NOT_EXECUTED

- registered run directories:
  none

- checkpoints:
  all pending

- GOV-7:
  inactive

- recommendations:
  unaccepted

- implementation:
  unauthorized

#### State B — One pass executed

- overall audit:
  in progress, not completed

- passes executed:
  1

- PASS-01:
  EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION
  or the honest correction-pending equivalent while this correction is incomplete

- registered PASS-01 run directories:
  exactly one coherent registered run

- PASS-01 accepted:
  false

- CHECKPOINT-A:
  pending

- PASS-02:
  unexecuted

- GOV-7:
  inactive

- recommendations:
  unaccepted

- implementation:
  unauthorized

Do not weaken validation by merely deleting the zero-pass assertions.

Replace snapshot-specific assertions with lifecycle-aware invariants.

### 2. Required lifecycle invariants

The corrected validator must check, where represented canonically:

- executed-pass count equals the number of registered executed-pass records;
- each executed pass has a coherent registered run;
- the run identity matches its pass and audit identity;
- authorization, prompt, input manifest, outputs and validation identities are coherent;
- a pass represented as never executed does not have an executed run;
- the highest executed pass has not bypassed a required Owner checkpoint;
- later passes remain unexecuted unless predecessors and checkpoints are satisfied;
- overall audit status does not claim completion after PASS-01;
- PASS-01 execution does not imply PASS-01 acceptance;
- PASS-01 execution does not imply CHECKPOINT-A completion;
- PASS-01 execution does not imply GOV-7 activation;
- recommendations remain unaccepted;
- implementation remains unauthorized;
- OD-006 remains unresolved and trigger-gated;
- the original planning-only scaffold state remains valid.

Implement only the smallest lifecycle model required for:

- the original scaffold state;
- the current one-pass-executed state;
- direct invalid transitions associated with those states.

Do not design a complete future audit workflow engine.

### 3. Regression tests

Preserve valid coverage for the original planning-only scaffold.

Add or update the smallest regression coverage proving:

1. a coherent zero-pass planning state passes;
2. a coherent one-pass-executed state passes;
3. executed-pass count without a matching registered run fails;
4. a registered executed run without coherent pass status fails;
5. PASS-02 execution before CHECKPOINT-A fails;
6. PASS-01 execution does not permit PASS-01 acceptance automatically;
7. PASS-01 execution does not permit GOV-7 activation;
8. PASS-01 execution does not permit recommendation acceptance or implementation authority.

Use existing fixtures and test patterns where possible.

Do not create a new general-purpose testing framework.

### 4. Preserve the original validation failure honestly

Correct:

governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/evaluation/pass-01-validation-report.yaml

Do not rewrite history as though the original complete-suite failure never occurred.

Represent the sequence honestly using the existing schema or closest repository-valid structure.

The meaning must be equivalent to:

initial_validation:
  targeted_checks: PASSED
  full_governance_suite: FAILED
  passed_tests: 141
  failed_tests: 3
  result: INCOMPLETE_VALIDATION
  cause: PLANNING_ONLY_VALIDATOR_LIFECYCLE_DEFECT

correction:
  correction_id: GOV-AUD-001-P01-R1-C1
  validator_corrected: true
  regression_tests_updated: true
  substantive_outputs_changed: false
  corrected_full_suite: <actual result>
  final_validation_result: <actual result>

Do not delete the initial failure evidence.

Do not alter the four substantive PASS-01 outputs.

Before and after the correction, calculate their hashes and prove they are byte-unchanged.

If a deterministic validation failure shows that a substantive output itself must change, stop and report because this prompt does not authorize substantive output correction.

### 5. Reconcile only directly affected state

Update only directly affected records required by current repository contracts, such as:

- PASS-01 run manifest;
- PASS-01 validation status;
- audit status;
- audit pass count;
- artifact or prompt registry entries;
- generated audit views;
- checksum records;
- correction authorization record;
- correction prompt custody.

Do not modify unrelated governance state.

The successful corrected meaning must remain equivalent to:

PASS-01:
  status: EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION
  accepted: false

CHECKPOINT-A:
  status: PENDING_OWNER_DISPOSITION

PASS-02:
  status: NOT_EXECUTED

GOV-7:
  status: INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY

OD-006:
  status: UNRESOLVED_TRIGGER_GATED

recommendations_accepted:
  false

implementation_authorized:
  false

overall_audit:
  status: IN_PROGRESS
  completed: false
  passes_executed: 1

Use existing repository-valid terminology while preserving this meaning.

Do not mark PASS-01 accepted.

Do not complete CHECKPOINT-A.

Do not authorize PASS-02.

### 6. Learning capture

Record this as a material validation-lifecycle defect using the existing append-only learning mechanism.

Capture:

- expectation:
  the audit scaffold validator would remain valid as the audit progressed;

- event:
  the complete governance suite failed after PASS-01 publication because shared validator tests encoded the initial zero-pass scaffold snapshot as a permanent invariant;

- impact:
  PASS-01 was published with incomplete full-suite validation and could not be treated as fully validated input;

- immediate cause:
  hard-coded planning-only assumptions in shared validator and tests;

- systemic cause:
  the scaffold validation contract modeled the initial state but not the next legitimate lifecycle transition;

- correction:
  lifecycle-aware invariants and regression tests covering the planning-only and one-pass-executed states;

- prevention:
  validators for staged systems must test applicable valid transitions and at least the next reachable state, not only the bootstrap snapshot;

- reusable lesson:
  state validation must derive expectations from canonical lifecycle status rather than permanently encode one phase snapshot;

- affected areas:
  audit scaffold, PASS-01 execution, future audit passes and shared validation methodology;

- evidence:
  original failing tests, published PASS-01 commit, correction prompt, correction commit and final test results.

Do not rewrite an existing learning record.

Create a new record or append-only event according to current repository conventions.

## Validation

Run in this order:

1. reproduce the three original failures;
2. run focused validator tests after correction;
3. run the new lifecycle regression tests;
4. validate the original planning-only scaffold fixture or equivalent;
5. validate the current one-pass-executed repository state;
6. validate PASS-01 run custody and outputs;
7. validate prompt custody;
8. validate authorization custody;
9. validate registry and checksums;
10. validate governance and audit state;
11. run authored-file git diff --check;
12. run the complete governance test suite.

The complete governance test suite must pass before commit.

The previous total was:

144 tests
141 passed
3 failed

Report the actual new total because authorized regression tests may increase it.

Also verify deterministically:

- all four substantive PASS-01 outputs are byte-unchanged;
- Kernel artifacts are unchanged;
- Kernel remains 0.2.0 / RATIFIED;
- GOV-5 remains COMPLETED_CLOSED;
- GOV-6 remains COMPLETED_CLOSED;
- GOV-7 remains inactive;
- OD-006 remains unresolved;
- PASS-02 remains unexecuted;
- CHECKPOINT-A remains pending;
- PASS-01 remains unaccepted;
- recommendations remain unaccepted;
- implementation remains unauthorized.

Run isolated-copy validation or create a review bundle only if an existing mandatory repository contract requires it for this correction.

Do not create new validation infrastructure, schemas or bundle profiles merely by habit.

## Stopping conditions

Stop before commit and push if:

- startup verification fails;
- original failures cannot be reproduced;
- correction requires changes outside the directly affected validator, tests, prompt/authorization custody, PASS-01 validation evidence, audit status, run manifest, registries, checksums or learning mechanism;
- a substantive PASS-01 output requires modification;
- an unrelated material failure appears;
- the complete governance suite still fails;
- Kernel or phase state changes;
- PASS-02 execution is detected;
- GOV-7 activation or implementation is detected;
- the correction cannot preserve the original validation failure honestly.

Preserve diagnostics and report the blocker.

Do not claim success when complete validation has not passed.

## Publication authority

The Project Owner authorizes exactly one bounded correction commit and one non-force push if and only if:

- startup verification passes;
- original failures are reproduced;
- the correction remains within authorized scope;
- substantive PASS-01 outputs remain byte-unchanged;
- all required validation passes;
- the complete governance suite passes;
- no unrelated blocker remains.

Suggested commit message:

fix(governance): support executed audit pass validation

Do not:

- create or switch branches;
- force push;
- open a pull request;
- merge;
- tag;
- release;
- deploy.

If validation fails:

- do not commit;
- do not push;
- preserve diagnostics;
- report the blocker.

## Required return

Return concisely:

Repository:
Branch:
Starting local HEAD:
Starting remote HEAD:
Startup verification:
Original failures reproduced:

Correction ID:
Correction authorization:
Prompt custody:
Prompt SHA-256:

Root cause:
Validator paths changed:
Test paths changed:
Regression cases:
Planning-only state validation:
One-pass-executed state validation:

PASS-01 substantive outputs byte-unchanged:
Original validation failure preserved:
Validation report corrected:
Learning record or event:
Status and registry reconciliation:

Focused tests:
Lifecycle regression tests:
PASS-01 validation:
Full governance suite:
Final test total:
Git diff check:
Isolated-copy validation:
Review bundle:

Commit:
Push:
Final local HEAD:
Final remote HEAD:
Local/remote aligned:
Worktree:

PASS-01 status:
PASS-01 accepted:
CHECKPOINT-A:
PASS-02 executed:
GOV-7 status:
OD-006 status:
Recommendations accepted:
Implementation authorized:
Kernel status:

Status:
Blockers:
Exact next action:

Expected successful status:

PASS_01_VALIDATION_LIFECYCLE_CORRECTED_AND_PUSHED_PENDING_PROJECT_OWNER_DISPOSITION

Expected exact next action:

The Project Owner reviews the corrected PASS-01 validation evidence and the four byte-unchanged PASS-01 outputs, then separately decides whether to accept PASS-01 as bounded input and authorize PASS-02. Do not execute PASS-02, complete CHECKPOINT-A, activate GOV-7 or implement any recommendation through this correction.
