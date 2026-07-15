---
prompt_id: GOV-AUD-PROMPT-020
version: 0.1.0
lifecycle: TEMPLATE
pass_id: PASS-02
status: PLANNED_NOT_EXECUTED
---

# PASS-02 Prompt Template — Cross-Layer Architecture and Controlled Self-Hosting

This is not an executable prompt. Instantiate only after PASS-01 is accepted or explicitly bounded and separate execution authorization is in custody.

## Required instantiation bindings

`AUDIT_RUN_ID`, `AUTHORIZATION_RECORD/HASH`, `PASS_01_OUTPUT/HASH`, `CONTRACT_VERSION`, `INPUT_MANIFEST/PACKAGE_HASH`, `REPOSITORY_HEAD`, `MODEL_IF_OBSERVABLE`, `OUTPUT_CONTRACT`, `STOP_CONDITIONS`.

## Role and boundary

Act as the Cross-Layer Architecture Auditor under `passes/PASS-02/contract.yaml`. Work read-only. Do not select or implement graph, projection, service, controller, self-hosting, GOV-7 strategy or runtime change.

## Task

Map governance derivation, S0a-S9 methodology construction, client lifecycle and information layers. Define bounded contexts, canonical ownership, interfaces, exchanged artifacts, failure/stopping/recovery boundaries, cross-layer application contracts, version compatibility/migration/supersession, and upward feedback routing.

Produce the required typed relationship model and query contract while keeping it derived, regenerable, provenance-rich and non-authoritative. Compare modular artifact-driven, layered, event-driven, controller-led, service-oriented, microservices, repository-native and hybrid styles. Define explicit adoption criteria for distribution.

Assess system self-hosting and infrastructure self-hosting separately. Protect the bootstrap trust root, seed/generated distinction, version/release/migration boundaries, independence, rollback, manual fallback and recovery. Prevent self-modification, self-certification, self-ratification, circular authority and retrospective rewriting.

## Validation and handoff

Validate types/endpoints, source paths, required queries, compatibility coverage and authority boundaries. Stop before technology selection or implementation. Hand PASS-01/PASS-02 to CHECKPOINT-A; infer no approval.

## Anti-bloat review

- `KEEP`: four axes, ownership/interfaces, typed relationships, version/migration, feedback, architecture comparison, trust root and both self-hosting types.
- `REMOVE`: speculative service decomposition, product catalogues, exhaustive diagrams, implementation code.
- `MAKE_CONDITIONAL`: external architecture precedent only for an unresolved defined question.
- `MOVE_TO_FOLLOW_UP`: technology selection, persistent graph, projection, MCP and runtime integration.
