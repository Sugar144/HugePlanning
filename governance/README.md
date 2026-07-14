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

The current Kernel is `PROPOSED_NOT_RATIFIED`. KGR-001 Intake, KGR-002 Designer, KGR-003 Adversary, and the KGR-004 Designer revision are recorded as completed. KGR-004 produced the current `0.2.0-proposed` package with `READY_FOR_TARGETED_ADVERSARIAL_CLOSURE`: 14 findings are Designer-dispositioned as `RESOLVED` and `KA-F-015` is `ROUTED`. The bounded `GOV-LOOP-001` methodology and KGR-005 targeted-closure package are prepared for initial trial. KGR-005 is `NOT_STARTED`, preparation is `COMPLETED`, and readiness is `READY_FOR_EXECUTION`. GOV-4 remains `IN_PROGRESS` because independent targeted closure has not occurred. Enforcement Engineering remains gated; no policy package, enforcement system, ratification record, or operational governance system exists.

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
