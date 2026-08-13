---
prompt_id: GOV-AUD-PROMPT-050
version: 0.1.0
lifecycle: TEMPLATE
pass_id: PASS-05
status: PLANNED_NOT_EXECUTED
---

# PASS-05 Prompt Template — GOV-7 Strategy Comparison and Backlog Derivation

This is not an executable prompt. Instantiate only after explicit CHECKPOINT-B disposition and accepted or bounded predecessor evidence.

## Required instantiation bindings

`AUDIT_RUN_ID`, `AUTHORIZATION_RECORD/HASH`, `CHECKPOINT_B_RECORD/HASH`, `ACCEPTED_PREDECESSOR_SET/HASHES`, `INPUT_MANIFEST/PACKAGE_HASH`, `CONTRACT_VERSION`, `MODEL_IF_OBSERVABLE`, `OUTPUT_CONTRACT`, `STOP_CONDITIONS`.

## Role and boundary

Act as the GOV-7 Strategy and Backlog Auditor under `passes/PASS-05/contract.yaml`. Work read-only. Propose only; do not activate GOV-7, resolve OD-006, select an implementation without comparison, implement controls/tools, or accept the backlog.

## Task

Compare `TOP_DOWN_LAYER_COMPLETION`, `BOTTOM_UP_CONTROL_FIRST`, `HYBRID_VERTICAL_SLICES`, and evidence-supported alternatives across traceability, early evidence, rework, AI cycles, Owner/validation burden, defect discovery, layer preservation, scale, maintenance, stopping/recovery, migration and controlled self-hosting.

If vertical slicing wins, justify superiority, first representative slice, exercised capability, limits and change triggers. Treat the existing authorization-to-reconciliation flow as a candidate only.

Derive ER-001 through ER-020 into `component -> epic -> task -> acceptance criteria -> test/validator -> evidence contract -> gate -> dependency`. Allocate `P0_BEFORE_MATERIAL_GOV_7_WORK`, `P1_FIRST_APPROVED_IMPLEMENTATION_INCREMENT`, `P2_AFTER_INITIAL_EMPIRICAL_EVIDENCE`, `DEFER`, or `REJECT`. Define upward routing for product, requirement, task, agent, skill, procedure, control, policy, standard, methodology and possible Kernel defects; progressive self-hosting; independent functions; Owner-only decisions; and OD-006 boundaries.

## Validation and handoff

Validate strategy completeness, exact ER coverage, backlog chain fields, independence and OD-006 protection. Hand accepted/bounded evidence to PASS-06 without implementation authority.

## Anti-bloat review

- `KEEP`: genuine alternatives, criteria, ER traceability, evidence/gates, horizons, self-hosting/independence and Owner decisions.
- `REMOVE`: predetermined slices, story points/developer-weeks, implementation code, ceremonial backlog items.
- `MAKE_CONDITIONAL`: extra strategies and a first-slice recommendation only when evidence supports them.
- `MOVE_TO_FOLLOW_UP`: implementation contracts, tool pilots, runtime changes and OD-006 resolution.
