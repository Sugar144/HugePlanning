# Bounded Correction — GOV-AUD-001 Methodology Findings

## Objective

Implement one bounded, versioned correction addressing exactly these three accepted review findings:

```text id="2vblp8"
MC3-GENERIC-CONTRACT-001
MC3-ADVERSARIAL-EVIDENCE-002
HP-MPROP-007-COMPLETENESS-003
```

Do not expand the audit methodology beyond what is necessary to resolve them.

After this correction, treat the audit methodology as frozen until CHECKPOINT-A unless a new critical defect affecting authority, immutability or valid execution is demonstrated.

## Repository and expected state

```yaml id="bfk3yo"
repository: Sugar144/HugePlanning
root: /home/sugar/Documents/HugePlanning-governance
branch: governance/kernel-designer-revision-v0.1
expected_committed_local_head: a4cbc500b2ca864b2eb35e9354df88c8c3d97a3e
expected_remote_head: a4cbc500b2ca864b2eb35e9354df88c8c3d97a3e
review_id: GOV-AUD-001-METHOD-001-IER-001
reviewed_candidate: GOV-AUD-001-METHOD-001/0.2.0
```

Before modification, verify:

- local and remote HEAD match the expected commit;
- local and remote are aligned;
- staging is empty;
- the uncommitted `GOV-AUD-001-METHOD-001/0.2.0` candidate is present;
- its existing focused validation state is recoverable;
- PASS-02 R1 remains immutable;
- PASS-02 R2 does not exist;
- CHECKPOINT-A remains pending;
- PASS-03 and PASS-04 remain unprepared and unexecuted;
- GOV-7 remains inactive;
- the Kernel remains unchanged.

Stop without modification on material mismatch.

## Identity resolution and custody

Resolve the next available versions and prompt identities from canonical repository registries.

Do not assume an unused `HP-PROMPT-*` or other identity from chat.

The correction must:

- supersede the current unaccepted methodology candidate prospectively;
- preserve all previous candidate and review evidence;
- preserve the complete received prompt verbatim;
- bind the correction to the exact three findings;
- create no new audit-pass run identity;
- create no fake review or acceptance result.

Use the smallest repository-compatible correction structure.

## Authorized scope

Authorized:

- version the current methodology correction;
- update the audit methodology protocol;
- update only the pass contracts/templates directly required for generic contract discovery;
- update methodology validators and focused tests;
- complete `HP-MPROP-007` prospectively;
- update directly dependent registries, state surfaces, proposal indexes, hashes and validation evidence;
- run required validation.

Not authorized:

- modify PASS-02 R1;
- prepare PASS-02 R2;
- accept PASS-02;
- execute CHECKPOINT-A;
- prepare or execute PASS-03 or PASS-04;
- implement the learning pipeline;
- select an observability framework;
- activate GOV-7;
- amend the Kernel;
- resolve OD-006;
- commit or push;
- open a PR, merge, tag, release or deploy.

## Finding 1 — Generic pass-contract resolution

Resolve `MC3-GENERIC-CONTRACT-001`.

The methodology validator must no longer depend on a hard-coded map limited to PASS-02 and PASS-07.

Implement data-first discovery or resolution of applicable pass contracts using canonical repository structure or registry evidence.

For every applicable structured review instance, validate:

- pass contract exists;
- contract ID matches;
- contract version matches;
- contract SHA-256 matches repository bytes;
- declared review type is allowed by that contract;
- declared conclusion/result is compatible with that contract;
- predecessor and supersession semantics are respected where applicable.

Requirements:

- validation must work for synthetic pass IDs not named PASS-02 or PASS-07;
- adding a valid future pass contract must not require editing a permanent hard-coded semantic allowlist;
- missing, ambiguous, duplicate or mismatched contracts must fail safely;
- historical PASS-02 R1 custody checks must remain separate and unchanged;
- do not change unrelated pass contracts merely to satisfy tests.

Add negative and positive tests using synthetic contract fixtures.

## Finding 2 — Genuine adversarial evidence

Resolve `MC3-ADVERSARIAL-EVIDENCE-002`.

An `ADVERSARIAL_REVIEW` must not pass merely because arbitrary non-empty strings are present.

Define and validate a structured adversarial-attack record containing at least:

```yaml id="4y5y4w"
attack_id:
attack_dimension:
target_claim_or_assumption:
attack_method:
counterexample_or_failure_scenario:
evidence_examined:
result:
impact:
```

Allowed attack dimensions must support materially different attacks such as:

- assumption refutation;
- counterexample construction;
- authority-circularity attack;
- failure-mode attack;
- minimality challenge;
- migration or rollback attack;
- evidence-loss or contradiction attack;
- independence or self-certification attack;
- Owner-burden or bureaucracy challenge;
- rival-architecture challenge.

Do not require every review to perform every dimension.

Require enough structured evidence to demonstrate an actual attempted refutation appropriate to the reviewed scope.

Validation must reject:

- generic criticism without a target;
- “reviewed adversarially” declarations without attack evidence;
- empty or nominal attack descriptions;
- restated acceptance criteria presented as attacks;
- assertions without evidence or a counterexample/failure scenario;
- survival conclusions when no meaningful attack was attempted.

An adversarial review may conclude that the artifact survives, but only after recording actual attack attempts and their results.

Add synthetic negative tests for nominal compliance and positive tests for genuine structured attacks.

Do not retrospectively reclassify historical reviews.

## Finding 3 — Complete learning-pipeline proposal

Resolve `HP-MPROP-007-COMPLETENESS-003`.

Preserve `HP-MPROP-007` as a prospective methodology proposal with:

```text id="ll3vc1"
status:
OWNER_ACCEPTED_FOR_FUTURE_AUDIT_CLARIFICATION

implementation:
NOT_STARTED

incorporation:
AFTER_CHECKPOINT_A_BEFORE_PASS_03
```

It must preserve the complete proposed lifecycle:

```text id="lxx79d"
observable execution event
→ visible execution insight
→ hypothesis
→ planned verification
→ confirmed, refuted, partially confirmed or unresolved conclusion
→ learning candidate
→ evidence-aware triage
→ durable destination
→ procedural promotion
→ relevance-based retrieval
→ effectiveness measurement
```

### Required boundaries

Explicitly distinguish:

- hidden chain-of-thought, which must not be collected;
- visible model updates, hypotheses and conclusions;
- operational telemetry;
- model inference;
- verified repository evidence;
- durable learning;
- methodology proposals;
- Owner decisions;
- implemented procedural controls.

Repository evidence remains canonical.

Operational traces remain non-authoritative.

Executor self-assertion is not sufficient verification.

### Observable-data design requirements

Preserve prospective consideration of:

- run and session identity;
- prompt ID, version and hash;
- input-package hash;
- model and reasoning mode when observable;
- visible model updates;
- tool calls and results;
- commands and validations;
- changed files;
- retries and correction cycles;
- Owner interventions;
- stop reason;
- artifact inventory;
- tokens, cost and duration only when observable;
- explicit unavailable-data markers.

Include privacy, redaction, retention, rollback, telemetry disablement and manual-fallback boundaries.

### Verification states

Preserve explicit states equivalent to:

```text id="x4w6a9"
HYPOTHESIS_PENDING_VERIFICATION
CONFIRMED
REFUTED
PARTIALLY_CONFIRMED
UNRESOLVED
```

Refuted and unresolved items must not become accepted procedural learning.

### Candidate destinations

Preserve routes for:

- operational observation;
- formal-run evidence;
- failure or lesson record;
- methodology proposal;
- Owner decision candidate;
- tooling candidate;
- prompt candidate;
- skill candidate;
- validator candidate;
- regression-test candidate;
- control candidate;
- research required;
- duplicate/link to existing record;
- discard.

Candidate extraction must not decide authority, risk acceptance, ratification, phase transitions or implementation approval.

### Procedural promotion

Preserve potential promotion into:

- repository instructions;
- prompt contracts;
- schemas;
- validators;
- regression tests;
- scripts;
- hooks;
- skills;
- routing rules;
- deterministic queries;
- model-selection rules;
- formal-run protocols;
- adversarial-review attack cases;
- Owner checklists.

Represent distinctly:

```text id="68flq1"
captured
implemented
validated
shown effective
```

### Selective retrieval

Preserve selective retrieval using relevant dimensions such as:

- phase or pass;
- role;
- component;
- operation;
- artifact type;
- failure class;
- risk class;
- authority boundary;
- validation type;
- model or execution mode where relevant.

Do not inject all learning records into every run.

Require small, justified context packages linked to durable evidence.

### Effectiveness

Preserve prospective metrics such as:

- recurrence rate;
- repeated Owner corrections;
- repeated manual repairs;
- correction cycles;
- lessons promoted into controls;
- promoted controls independently validated;
- relevant lessons retrieved;
- irrelevant-context rate;
- false-learning rate;
- duplicate-learning rate;
- added token burden;
- added Owner burden;
- failures prevented;
- candidates discarded as noise.

Record volume alone must not count as successful learning.

### Tooling boundary

Explicitly distinguish:

```text id="bt54vb"
trace capture
≠ insight extraction
≠ evidence verification
≠ candidate triage
≠ procedural promotion
≠ selective retrieval
≠ effectiveness evaluation
```

Preserve future comparison of:

```text id="y7rmul"
REPOSITORY_NATIVE_MVP
PILOT_EXTERNAL_FRAMEWORK
HYBRID_REPOSITORY_AND_FRAMEWORK
NO_ACTION
DEFER_PENDING_RUNTIME_CONTROL
```

Candidate technologies may include repository-native JSONL, Codex hooks/events, OpenTelemetry, OpenInference, Phoenix, Langfuse, Braintrust, PromptLayer, Promptfoo, Opik and other evidence-supported alternatives.

No framework is selected or adopted by this correction.

### Audit allocation

Preserve:

```text id="yv2bfx"
PASS-03:
telemetry, insight representation, verification, metrics and retrieval requirements

PASS-04:
repository-native and external tooling comparison

PASS-06:
synthesis, minimum scope and adoption sequence

PASS-07:
independent evaluation of usefulness, safety, burden and bureaucracy risk
```

Do not modify the current PASS-03 or PASS-04 contracts.

Preserve the requirement for a later bounded clarification after CHECKPOINT-A and before PASS-03.

## Validation

Create or update only the minimum validation support necessary.

Run:

```text id="aamefz"
python3 governance/tools/validate_audit_methodology.py
python3 governance/tools/validate_audit_scaffold.py
python3 governance/tools/validate_prompts.py --root .
python3 governance/tools/validate_governance_state.py
python3 governance/tools/validate_pass_02.py
```

Run:

- focused tests for generic contract discovery;
- focused tests for adversarial evidence;
- focused tests for `HP-MPROP-007`;
- all existing methodology/scaffold focused tests;
- complete governance test suite;
- deterministic PASS-02 R1 custody comparison;
- YAML and Markdown validation;
- reference and checksum validation;
- `git diff --check`.

Do not run the published runtime suite unless runtime-facing files are modified or an existing contract requires it.

Tests must be generic.

Do not hard-code the expected approval of this correction, production finding IDs, preferred conclusions or named pass outcomes as permanent semantic truth.

## Required terminal state

If valid:

```text id="wxsl0z"
methodology correction:
IMPLEMENTED_VALIDATED_PENDING_INDEPENDENT_CONFIRMATION_AND_PROJECT_OWNER_DISPOSITION

PASS-01:
PASS_01_ACCEPTED_COMPLETED

PASS-02:
EXECUTED_VALIDATED_PENDING_INDEPENDENT_EVALUATION_AND_PROJECT_OWNER_DISPOSITION

CHECKPOINT-A:
PENDING_PROJECT_OWNER_DISPOSITION

PASS-03:
PLANNED_NOT_EXECUTED_UNAUTHORIZED

PASS-04:
PLANNED_NOT_EXECUTED_UNAUTHORIZED

GOV-7:
INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY

OD-006:
UNRESOLVED_TRIGGER_GATED
```

The methodology remains frozen pending confirmation and Owner disposition.

## Publication boundary

Do not commit or push.

Leave staging empty.

Return the validated uncommitted candidate for one focused independent confirmation.

## Required return

Return only:

```text id="lr7db0"
Repository:
Root:
Branch:
Committed local HEAD:
Remote HEAD:
Startup verification:
Resolved correction identity:
Resolved prompt identity:
Prompt custody:
Findings addressed:
Generic contract resolution:
Synthetic non-PASS-02/PASS-07 tests:
Adversarial evidence schema:
Nominal-adversarial negative tests:
HP-MPROP-007 lifecycle:
Observable-data and privacy boundaries:
Verification states:
Candidate destinations:
Procedural promotion:
Selective retrieval:
Effectiveness measurement:
Tooling boundary:
PASS-03/04/06/07 allocation:
PASS-02 R1 immutability:
Files created:
Files modified:
Focused validators:
Focused tests:
Full governance suite:
Runtime suite:
Git diff check:
Commit:
Push:
Final HEAD:
Worktree:
Staging:
PASS-02 status:
CHECKPOINT-A status:
PASS-03 status:
GOV-7 status:
OD-006 status:
Status:
Blockers:
Exact next action:
```

Expected successful status:

```text id="bkwadi"
IMPLEMENTED_VALIDATED_PENDING_INDEPENDENT_CONFIRMATION_AND_PROJECT_OWNER_DISPOSITION
```

Expected next action:

```text id="k6q411"
Conduct one focused read-only independent confirmation of the three corrected findings. Do not reopen methodology scope, execute CHECKPOINT-A, prepare PASS-03, commit or push.
```
