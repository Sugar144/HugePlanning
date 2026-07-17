---
prompt_id: GOV-AUD-PROMPT-031
catalog_prompt_id: HP-PROMPT-035
version: 0.1.0
lifecycle: EXECUTED
audit_id: GOV-AUD-001
run_id: GOV-AUD-001-P03-R1
pass_id: PASS-03
role: Observable Learning Requirements Auditor
mode: EVIDENCE_AWARE_REQUIREMENTS_SYNTHESIS
authority: PROJECT_OWNER_EXPLICIT
contract_binding: GOV-AUD-001-PASS-03-CONTRACT/0.2.0
template_binding: GOV-AUD-PROMPT-030/0.2.0
repository: Sugar144/HugePlanning
expected_branch: governance/kernel-designer-revision-v0.1
expected_head: e5bdeeafdc2278a2baef67c659eef4a8eab5d867
---

# GOV-AUD-PROMPT-031 — Execute PASS-03 Observable Learning Requirements

## Exact execution binding

Execute exactly one `GOV-AUD-001` PASS-03 source run as
`GOV-AUD-001-P03-R1`. Apply
`GOV-AUD-001-PASS-03-CONTRACT/0.2.0`, the exact template
`GOV-AUD-PROMPT-030/0.2.0`, the Project Owner authorization
`GOV-AUD-AUTH-003/0.1.0`, and the complete hash-bound execution input
manifest `GOV-AUD-001-P03-R1-INPUT-001/0.1.0`.

The repository, branch, local and remote starting HEAD, clean worktree, clean
staging, prerequisite decisions, package identities and hashes must match the
manifest before substantive analysis. Stop without substantive output on a
material mismatch.

## Objective and output contract

Define technology-neutral requirements and evaluation criteria for observable
execution data, evidence-aware learning, controlled promotion, selective
retrieval, effectiveness and burden measurement, privacy, retention, rollback,
disablement and a later PASS-04 comparison. Produce exactly these nine source
artifacts:

1. `output/01-observable-event-requirements.yaml`
2. `output/02-evidence-and-authority-model.yaml`
3. `output/03-learning-lifecycle-and-state-machine.yaml`
4. `output/04-candidate-routing-and-promotion-model.yaml`
5. `output/05-selective-retrieval-requirements.yaml`
6. `output/06-effectiveness-and-burden-metrics.yaml`
7. `output/07-privacy-retention-and-rollback-requirements.yaml`
8. `output/08-tooling-neutral-capability-model.yaml`
9. `output/09-risks-open-questions-and-pass-04-handoff.md`

Use the canonical artifact identities `GOV-AUD-P03-OUT-001` through
`GOV-AUD-P03-OUT-009`. Each material statement must be typed as
`VERIFIED_FACT`, `INFERENCE`, `REQUIREMENT`, `PROPOSAL`,
`OPEN_QUESTION`, or `OWNER_DECISION_REQUIRED`, carry repository evidence where
applicable, and preserve explicit unavailable-data markers.

## Mandatory requirements

- Define required, optional, derived and unavailable observable fields for run
  and session identity, role and mode, prompt and input identities and hashes,
  model and reasoning mode, visible updates, tools, commands, validations,
  changed files, retries, corrections, Owner interventions, stop reason,
  outputs, duration, tokens and cost.
- Prohibit hidden chain-of-thought capture. Visible model statements are
  observable only when actually emitted and remain non-authoritative.
- Keep repository evidence canonical. Separate operational trace, visible model
  statement, model inference, hypothesis, planned verification, verification
  result, repository evidence, formal-run evidence, learning candidate,
  accepted durable learning, procedural control, independently validated
  control, demonstrated effectiveness and Owner decision.
- Define the complete lifecycle, valid and invalid transitions, guards,
  responsible actor or mechanism, required evidence, correction/rollback,
  terminal and non-terminal states, and the five required verification states.
- Refuted and unresolved items cannot become accepted procedural learning.
  Partial confirmation must preserve unsupported portions as unresolved.
- Define evidence-aware routing, durable destinations, procedural-promotion
  targets and distinct `CAPTURED`, `ACCEPTED`, `IMPLEMENTED`, `VALIDATED` and
  `SHOWN_EFFECTIVE` states. Frequency and capture alone cannot authorize
  promotion.
- Define compact selective retrieval by relevant dimensions, with evidence
  links, justification, context limits, duplicate suppression, conflict,
  contradiction, staleness, validity, no-result fallback and irrelevant-context
  measurement. Global injection of all learning is prohibited.
- Define recurrence, correction, repair, promotion, independent validation,
  prevention, retrieval, false/duplicate/stale learning, noise discard,
  rollback, token, execution-time and Owner-burden metrics plus anti-gaming
  controls. Volume is not success.
- Define minimization, redaction, sensitive-data classes, access, retention,
  deletion, correction, rollback, auditability, telemetry disablement, manual
  fallback, export, portability, unavailable data and failure-safe behavior.
- Separate trace capture, insight extraction, evidence verification, candidate
  triage, procedural promotion, selective retrieval and effectiveness
  evaluation through explicit interfaces and evaluation criteria.
- Preserve `NO_ACTION` and deferred options for later comparison.

## Prohibited selections and authority

Do not choose or adopt a repository-native implementation, external
observability platform, tracing framework, vector store, database, agent
framework, hosted service, model provider or retrieval architecture. Do not
implement telemetry or a learning pipeline. Do not prepare, execute or
authorize PASS-04. Do not activate GOV-7, amend or implement the Kernel,
resolve OD-006, accept risk, ratify policy, alter PASS-01/PASS-02 history,
execute the independent review, or accept PASS-03.

Candidate extraction and triage may not decide scope, constitutional matters,
risk acceptance, ratification, phase transition, implementation approval,
release or adoption. Deterministic validation may establish conformance only;
the source executor may not independently accept, close or adversarially review
its own outputs.

## Self-critique, validation and handoff

Perform bounded source self-critique for unsupported authority, hidden-reasoning
capture, premature tool selection, overcollection, unverifiable learning,
invalid transitions, global context injection, metric gaming, privacy/deletion
gaps, excessive Owner burden and disproportionate bureaucracy. Correct direct
defects before final validation and record the critique in the validation
evidence.

Run the prepared validators and the execution validator, focused PASS-03 tests,
the complete governance suite and `git diff --check`. Do not weaken checks to
obtain a pass. Do not run runtime tests unless a runtime-facing file changes;
stop on such a scope mismatch.

Create a hash-bound immutable review-package manifest containing the contract,
prompt, authorization, input manifest, all outputs, validation evidence,
artifact inventory and all thirteen prepared attack dimensions. Do not perform
the review.

On successful deterministic validation, set only:

`EXECUTED_VALIDATED_PENDING_INDEPENDENT_ADVERSARIAL_REVIEW_AND_PROJECT_OWNER_DISPOSITION`

The exact next action is: conduct one independent adversarial review of PASS-03
using the prepared immutable review package; do not execute PASS-04.
