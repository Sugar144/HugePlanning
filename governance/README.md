# HugePlanning Governance

This area preserves and organizes the governance-kernel history for HugePlanning. It contains immutable raw sources, reusable governance methodology, reconstructed and prepared run records, candidate normative artifacts, provenance controls, and governance-specific adoption planning.

Start with:

1. `CURRENT_STATE.md` for the immediate state and next action.
2. `GOVERNANCE_MASTER_PLAN.md` for phase gates and dependencies.
3. The applicable `runs/*/run-manifest.yaml`.
4. `ARTIFACT_REGISTRY.yaml` and `SOURCE_CHECKSUMS.sha256` for provenance.
5. `methodology/` for current reusable role and protocol contracts.

## Authority and status

Raw sources show what was received. Run directories reconstruct what a function used and produced. Canonical candidates provide stable review paths without increasing authority. A prompt is an execution contract, not proof that execution occurred. A proposed artifact is not ratified merely because it is complete or reviewable.

The current Kernel is `0.2.0-proposed / PROPOSED_NOT_RATIFIED`. GOV-0 through GOV-5 are complete; KGR-005 completed with `CLOSURE_CONFIRMED`, and KGR-006-R1 is `ACCEPTED_BY_PROJECT_OWNER`. OD-002 is resolved as `CONFIRM_EXACT_SCOPE`, OD-003 as `PACKET_SUFFICIENT` for the current context, and OD-004 through OD-006 remain unresolved. GOV-6 through GOV-9 are inactive. The minimum GOV-7 package remains `RECOMMENDATION_ONLY`; no risk is accepted and no enforcement implementation has occurred.

<!-- GOVERNANCE_STATE_V1 -->
```yaml
governance_state:
  phase: GOV-5_CLOSED
  gov_5_status: COMPLETED_CLOSED
  gov_5_closure_review: EXECUTED_READY_FOR_PROJECT_OWNER_DECISION
  kgr_006_r1_status: ACCEPTED_BY_PROJECT_OWNER
  authorization_status: CONSUMED_1_OF_1_NONE_REMAINING
  od_002: RESOLVED_CONFIRM_EXACT_SCOPE
  od_003: RESOLVED_PACKET_SUFFICIENT
  od_004_through_od_006: UNRESOLVED
  gov_6_through_gov_9: INACTIVE
  kernel: 0.2.0-proposed/PROPOSED_NOT_RATIFIED
  minimum_gov_7_package: RECOMMENDATION_ONLY
  risk_accepted: false
  enforcement_implementation: NOT_PERFORMED
```

Methodology describes how governance work is performed; `runs/` records actual executions and honest non-executed preparation. A methodology artifact or prompt is not execution evidence. Every run preserves the exact contract and formal inputs it uses. Historical prompts remain in their original run records and are not silently replaced by current methodology.

## Relationship to the repository

The repository root and `.claude/`, `schemas/`, `scripts/`, `templates/`, and `tests/` contain or support the released methodology runtime. `product/` specifies in-flight methodology work, and `planning/v2/` is the existing product roadmap. This governance area complements those structures and does not replace or reorganize them.

Governance has not been projected into runtime. Runtime or planning changes require a later explicit integration or adoption task. Existing S1 work continues independently.

## Content classes

- `sources/raw/`: byte-exact, checksum-protected imports; never edit in place.
- `methodology/`: reusable role boundaries, mode registries, versioned protocols, rubrics, and interaction methods; not execution evidence.
- `runs/`: prompts, inputs, outputs, control snapshots, and honest completed or prepared execution manifests.
- `kernel/proposed/`: stable candidate copies for review; no ratified authority.
- top-level controls: current state, registry, decisions, roadmap, import record, and future adoption traceability.
- `archive/`: reserved for superseded governance records that must remain accessible; currently empty.
