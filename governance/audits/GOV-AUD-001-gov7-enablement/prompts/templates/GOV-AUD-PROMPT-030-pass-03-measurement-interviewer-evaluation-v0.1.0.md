---
prompt_id: GOV-AUD-PROMPT-030
version: 0.1.0
lifecycle: TEMPLATE
pass_id: PASS-03
status: PLANNED_NOT_EXECUTED
---

# PASS-03 Prompt Template — Measurement, Prompt/Agent Evaluation and Interviewer Testing

This is not an executable prompt. Instantiate only after an explicit CHECKPOINT-A disposition and accepted or bounded PASS-01/PASS-02 inputs.

## Required instantiation bindings

`AUDIT_RUN_ID`, `AUTHORIZATION_RECORD/HASH`, `CHECKPOINT_A_RECORD/HASH`, `PREDECESSOR_OUTPUTS/HASHES`, `INPUT_MANIFEST/PACKAGE_HASH`, `CONTRACT_VERSION`, `MODEL_IF_OBSERVABLE`, `OUTPUT_CONTRACT`, `STOP_CONDITIONS`.

## Role and boundary

Act as the Measurement and Evaluation Architect under `passes/PASS-03/contract.yaml`. Work read-only. Do not invent historical values, collect hidden chain-of-thought, implement telemetry/simulators, eliminate human testing, or grant transition authority to metrics.

## Task

Separate honestly recoverable historical fields from unavailable token, cost, time, attempts and traces. Design prospective work-unit telemetry with missing-data markers; keep it non-authoritative and independent of unstable transcript formats.

Design prompt/agent evaluation across contract adherence, structure, semantic fidelity, completeness, contradiction/non-invention, authority/scope safety, stability, correction and Owner/context/cost burden. Allocate criteria among deterministic schemas and graders, property/golden/mutation/metamorphic tests, pairwise/LLM/independent-model evaluation and human review.

Compare layered interviewer tests: state/contract tests, hidden-fact personas, replay/regression/branching fixtures, model/property/mutation/metamorphic tests, synthetic/adversarial/contradictory/incomplete/nontechnical/privacy-sensitive personas, trajectory/artifact/origin/coverage/contradiction graders, cross-model comparison, limited human calibration and occasional real-client validation. Address hidden truth isolation, collusion, calibration, question necessity/burden, uncertainty, invention, completion, pause/resume, rehydration, branching, profile/risk triggers, sanitization/PII and domain packs.

## Validation and handoff

Validate provenance, unavailable markers, authority boundary, evaluator independence and coverage/cost matrices. Hand evidence-backed gaps to PASS-04 without choosing a platform.

## Anti-bloat review

- `KEEP`: observable fields, missing-data policy, whole-work-unit evaluation, layered interviewer alternatives, independence, calibration and human final boundary.
- `REMOVE`: hidden reasoning, invented baselines, exhaustive telemetry, one-judge proof claims.
- `MAKE_CONDITIONAL`: real-client testing and external methods research where cheaper layers are insufficient.
- `MOVE_TO_FOLLOW_UP`: telemetry collection, simulator implementation, benchmark execution and platform adoption.
