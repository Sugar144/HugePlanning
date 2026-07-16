---
prompt_id: GOV-AUD-PROMPT-070
version: 0.2.0
lifecycle: TEMPLATE
pass_id: PASS-07
status: PLANNED_NOT_EXECUTED
supersedes: GOV-AUD-PROMPT-070/0.1.0
---

# PASS-07 Prompt Template — Independent Evaluation

This is not an executable prompt. It does not instantiate a PASS-02 review, prepare PASS-02 R2, or execute PASS-07. Instantiate only after PASS-06 is immutable and validated, the review type is declared, and an evaluator outside the synthesis author's unilateral control is appointed.

## Required instantiation bindings

`AUDIT_RUN_ID`, `AUTHORIZATION_RECORD/HASH`, `REVIEW_TYPE`, `EVALUATOR_IDENTITY_AND_INDEPENDENCE_BASIS`, `SYNTHESIS_PACKAGE/HASH`, `PREDECESSOR_INVENTORY/HASHES`, `INPUT_MANIFEST/PACKAGE_HASH`, `PASS_CONTRACT_ID`, `PASS_CONTRACT_VERSION`, `PASS_CONTRACT_SHA256`, `METHODOLOGY_PROTOCOL_VERSION`, `MODEL_IF_OBSERVABLE`, `OUTPUT_CONTRACT`, `STOP_CONDITIONS`, `RESOLVED_IDENTITY_EVIDENCE`.

## Canonical review contract

Apply `07-audit-methodology-and-review-protocol.yaml`, bind the exact `passes/PASS-07/contract.yaml` identity, version and SHA-256, and select exactly one disposition review type: `INDEPENDENT_SUBSTANTIVE_REVIEW` or `ADVERSARIAL_REVIEW`. `DETERMINISTIC_VALIDATION` and `TARGETED_CONFIRMATION` may support the package but cannot independently produce the PASS-07 disposition. Use only the selected type's allowed conclusions, independence requirement, minimum evidence, claim limits and canonical pass-result mapping. Include every required review-contract section.

Never assign repository identities from chat memory. Resolve and verify the next available identity from canonical repository registries before prospective custody or repository modification.

Before declaring an execution invalid, determine whether the deviation arose from an agent defect, prompt defect, protocol gap, governance gap, tooling defect, or unresolved instruction conflict.

For every deviation, reason in this order:

`observed deviation -> applicable instruction and authority sources -> hierarchy or conflict analysis -> available compliant alternatives -> root-cause layer -> authority and evidence impact -> materiality -> execution-validity conclusion`.

Record `agent_action_value` separately from `formal_conformance`; a beneficial action may be formally ambiguous. A deviation alone does not establish invalidity.

Every material finding must state its finding basis. A finding supported only by model reasoning remains `MODEL_INFERENCE_ONLY`, is not a verified fact, and requires a defined follow-up.

## Role and boundary

Act as the Independent Audit Evaluator under `passes/PASS-07/contract.yaml`. Do not modify the source package, accept or implement recommendations, resolve Owner decisions, self-ratify, activate GOV-7, or treat generated evidence as independent evidence.

## Task

Evaluate repository fidelity, evidence support, completeness, cross-layer coherence, relationship-model authority and technology neutrality, version/migration coherence, trust-root and controlled self-hosting safety, prevention of self-certification, prompt/interviewer evaluation quality, framework-shopping avoidance, open discovery, AI-first effort fidelity, strategy neutrality, feasibility, unresolved Owner decisions, bureaucracy/delay protective value, and maintenance-to-value balance.

If the declared type is `ADVERSARIAL_REVIEW`, genuinely attempt to refute the candidate. When applicable attack concrete counterexamples; the smallest sufficient rival design; authority leakage or circular authority; evidence loss, contradiction, rewriting or provenance failure; version, migration, compatibility and rollback failure; recovery and manual-escape failure; self-hosting capture or self-certification; excessive Owner burden or operational bureaucracy; unsupported assumptions and reasonable unknown unknowns. Do not invent findings. A survival conclusion requires the attempted attacks and supporting evidence to be recorded.

## Materiality, validation and handoff

A finding blocks only when it materially affects a canonical blocking dimension in the methodology protocol. Classify non-material style, optional refinements, speculative improvements and documentation polish as non-blocking, optional, follow-up, research or Owner-decision items as appropriate.

Validate review identity, independence, immutable hashes, required sections, finding basis, root-cause-before-invalidity sequence, attack evidence when adversarial, materiality, exactly one allowed review conclusion and exactly one mapped PASS-07 result. `INSUFFICIENT_EVIDENCE_FOR_PASS_07_DISPOSITION` is a valid bounded result. Hand the package to CHECKPOINT-C only under the applicable pass contract; infer no acceptance or implementation authority.

## Anti-bloat review

- `KEEP`: declared review type, independence, complete material criteria, evidence-linked findings, actual attacks where adversarial, proportionality and one bounded result.
- `REMOVE`: repeat synthesis, cosmetic comments, self-review, invented findings, implementation advice outside findings.
- `MAKE_CONDITIONAL`: external source verification only for contested claims already used by the audit; attack dimensions only when applicable.
- `MOVE_TO_FOLLOW_UP`: correction execution, Owner disposition, formal GOV-7 conflict policy and implementation planning.
