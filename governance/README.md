# HugePlanning Governance

This area preserves and organizes the governance-kernel history for HugePlanning. It contains immutable raw sources, reusable governance methodology, reconstructed and prepared run records, candidate normative artifacts, provenance controls, and governance-specific adoption planning.

Start with:

1. `CURRENT_STATE.md` for the immediate state and next action.
2. `GOVERNANCE_MASTER_PLAN.md` for phase gates and dependencies.
3. The applicable `runs/*/run-manifest.yaml`.
4. `ARTIFACT_REGISTRY.yaml` and `SOURCE_CHECKSUMS.sha256` for provenance.
5. `methodology/` for current reusable role and protocol contracts.
6. `audits/GOV-AUD-001-gov7-enablement/07-audit-methodology-and-review-protocol.yaml` for the prospective GOV-AUD-001 finding and review controls.

## Authority and status

Raw sources show what was received. Run directories reconstruct what a function used and produced. Canonical candidates provide stable review paths without increasing authority. A prompt is an execution contract, not proof that execution occurred. A proposed artifact is not ratified merely because it is complete or reviewable.

The current Kernel is `0.2.0 / RATIFIED` for HugePlanning level 3 under the Kernel scope rules. GOV-0 through GOV-6 are complete; KGR-005 completed with `CLOSURE_CONFIRMED`, and KGR-006-R1 is `ACCEPTED_BY_PROJECT_OWNER`. OD-002 is resolved as `CONFIRM_EXACT_SCOPE`, OD-003 as `PACKET_SUFFICIENT` for the current context, OD-004 as `RATIFY_EXACT_KERNEL_0_2_0`, and OD-005 as `ACCEPT_MINIMUM_GOV_7_DIRECTION`; OD-006 remains unresolved trigger-gated. GOV-7 is `INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY`; GOV-8 and GOV-9 are inactive. The minimum GOV-7 package is `DIRECTION_ACCEPTED_NOT_IMPLEMENTED`; no risk is accepted and no enforcement implementation has occurred.

GOV-AUD-001 remains in progress: PASS-01 is `PASS_01_ACCEPTED_COMPLETED` after the independently confirmed C3 evidence; PASS-02 is `EXECUTED_VALIDATED_PENDING_INDEPENDENT_EVALUATION_AND_PROJECT_OWNER_DISPOSITION`; exactly two passes are executed, CHECKPOINT-A is pending Project Owner disposition, and PASS-03 remains unauthorized and unexecuted. The Project Owner accepted `GOV-AUD-001-METHOD-001/0.3.0` prospectively after focused independent confirmation, preserving the prior finding, review, invalidity, adversarial, materiality, conflict and identity controls and leaving PASS-02 R1 unchanged. `HP-MPROP-007` is Owner-accepted only as a future audit clarification after CHECKPOINT-A and before PASS-03; implementation has not started. The Project Owner reports that PASS-02 was independently reviewed, but no exact review artifact is in repository custody, so the review result is not reconstructed or treated as formal evaluation evidence. The audit program is incomplete. No architecture, technology, implementation recommendation or residual risk is accepted. PASS-01 R1, C1, C2 and C3 and PASS-02 R1 remain immutable.

<!-- GOVERNANCE_STATE_V1 -->
```yaml
governance_state:
  phase: GOV-6_CLOSED
  gov_5_status: COMPLETED_CLOSED
  gov_5_closure_review: EXECUTED_READY_FOR_PROJECT_OWNER_DECISION
  kgr_006_r1_status: ACCEPTED_BY_PROJECT_OWNER
  authorization_status: CONSUMED_1_OF_1_NONE_REMAINING
  od_002: RESOLVED_CONFIRM_EXACT_SCOPE
  od_003: RESOLVED_PACKET_SUFFICIENT
  od_004: RESOLVED_RATIFY_EXACT_KERNEL_0_2_0
  od_005: RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION
  od_006: UNRESOLVED_TRIGGER_GATED
  gov_6_status: COMPLETED_CLOSED
  gov_7_status: INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY
  gov_8_through_gov_9: INACTIVE
  kernel: 0.2.0/RATIFIED
  minimum_gov_7_package: DIRECTION_ACCEPTED_NOT_IMPLEMENTED
  risk_accepted: false
  enforcement_implementation: NOT_PERFORMED
```

Methodology describes how governance work is performed; `runs/` records actual executions and honest non-executed preparation. A methodology artifact or prompt is not execution evidence. Every run preserves the exact contract and formal inputs it uses. Historical prompts remain in their original run records and are not silently replaced by current methodology.

## Relationship to the repository

The repository root and `.claude/`, `schemas/`, `scripts/`, `templates/`, and `tests/` contain or support the released methodology runtime. `product/` specifies in-flight methodology work, and `planning/v2/` is the existing product roadmap. This governance area complements those structures and does not replace or reorganize them.

Governance has not been projected into runtime. C2 inspected the released runtime as evidence but did not modify or adopt it into governance. Runtime or planning changes require a later explicit integration or adoption task. Existing S1 work continues independently.

## Content classes

- `sources/raw/`: byte-exact, checksum-protected imports; never edit in place.
- `methodology/`: reusable role boundaries, mode registries, versioned protocols, rubrics, and interaction methods; not execution evidence.
- `runs/`: prompts, inputs, outputs, control snapshots, and honest completed or prepared execution manifests.
- `kernel/proposed/`: stable candidate copies for review; no ratified authority.
- top-level controls: current state, registry, decisions, roadmap, import record, and future adoption traceability.
- `archive/`: reserved for superseded governance records that must remain accessible; currently empty.
