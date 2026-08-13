---
prompt_id: GOV-AUD-PROMPT-070
version: 0.1.0
lifecycle: TEMPLATE
pass_id: PASS-07
status: PLANNED_NOT_EXECUTED
---

# PASS-07 Prompt Template — Independent Evaluation

This is not an executable prompt. Instantiate only after PASS-06 is immutable, validated, and an evaluator outside the synthesis author's unilateral control is appointed.

## Required instantiation bindings

`AUDIT_RUN_ID`, `AUTHORIZATION_RECORD/HASH`, `EVALUATOR_IDENTITY_AND_INDEPENDENCE_BASIS`, `SYNTHESIS_PACKAGE/HASH`, `PREDECESSOR_INVENTORY/HASHES`, `INPUT_MANIFEST/PACKAGE_HASH`, `CONTRACT_VERSION`, `MODEL_IF_OBSERVABLE`, `OUTPUT_CONTRACT`, `STOP_CONDITIONS`.

## Role and boundary

Act as the Independent Audit Evaluator under `passes/PASS-07/contract.yaml`. Do not modify the source package, accept/implement recommendations, resolve Owner decisions, self-ratify, activate GOV-7, or treat generated evidence as independent evidence.

## Task

Evaluate repository fidelity, evidence support, completeness, cross-layer coherence, relationship-model authority/technology neutrality, version/migration coherence, trust-root and controlled self-hosting safety, prevention of self-certification, prompt/interviewer evaluation quality, framework-shopping avoidance, open discovery, AI-first effort fidelity, strategy neutrality, feasibility, unresolved Owner decisions, bureaucracy/delay protective value, and maintenance-to-value balance.

Produce evidence-linked findings, complete criterion matrix, unresolved decisions, limitations and exactly one result: `SUITABLE_FOR_PROJECT_OWNER_DECISION`, `RETURN_FOR_BOUNDED_VERSIONED_CORRECTION`, or `INVALID_AUDIT_EXECUTION`.

## Validation and handoff

Validate independence, criterion coverage, finding evidence, immutable hashes and exactly one result. Hand the package to CHECKPOINT-C; infer no acceptance or implementation authority.

## Anti-bloat review

- `KEEP`: independence, complete material criteria, evidence-linked findings, proportionality and one bounded result.
- `REMOVE`: repeat synthesis, cosmetic comments, self-review, implementation advice outside findings.
- `MAKE_CONDITIONAL`: external source verification only for contested claims already used by the audit.
- `MOVE_TO_FOLLOW_UP`: correction execution, Owner disposition and any implementation planning.
