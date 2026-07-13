# HugePlanning Governance

This area preserves and organizes the governance-kernel history for HugePlanning. It contains immutable raw sources, reconstructed run records, candidate normative artifacts, provenance controls, and governance-specific adoption planning.

Start with:

1. `CURRENT_STATE.md` for the immediate state and next action.
2. `GOVERNANCE_MASTER_PLAN.md` for phase gates and dependencies.
3. The applicable `runs/*/run-manifest.yaml`.
4. `ARTIFACT_REGISTRY.yaml` and `SOURCE_CHECKSUMS.sha256` for provenance.

## Authority and status

Raw sources show what was received. Run directories reconstruct what a function used and produced. Canonical candidates provide stable review paths without increasing authority. A prompt is an execution contract, not proof that execution occurred. A proposed artifact is not ratified merely because it is complete or reviewable.

The current Kernel is `PROPOSED_NOT_RATIFIED`. KGR-001 Intake and KGR-002 Designer are recorded as completed from supplied evidence. KGR-003 Adversary is `NOT_STARTED`. No policy package, enforcement system, ratification record, or operational governance system exists yet.

## Relationship to the repository

The repository root and `.claude/`, `schemas/`, `scripts/`, `templates/`, and `tests/` contain or support the released methodology runtime. `product/` specifies in-flight methodology work, and `planning/v2/` is the existing product roadmap. This governance area complements those structures and does not replace or reorganize them.

Governance has not been projected into runtime. Runtime or planning changes require a later explicit integration or adoption task. Existing S1 work continues independently.

## Content classes

- `sources/raw/`: byte-exact, checksum-protected imports; never edit in place.
- `runs/`: prompts, inputs, outputs, and honest execution manifests.
- `kernel/proposed/`: stable candidate copies for review; no ratified authority.
- top-level controls: current state, registry, decisions, roadmap, import record, and future adoption traceability.
- `archive/`: reserved for superseded governance records that must remain accessible; currently empty.
