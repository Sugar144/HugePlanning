# KGR-004 — Kernel Designer Adversarial Revision

Execution status: `NOT_STARTED`
Preparation status: `READY_FOR_EXECUTION`
Mode: `ADVERSARIAL_REVISION`
Kernel: `PROPOSED_NOT_RATIFIED`

## Purpose and provenance

KGR-004 is prepared to revise the complete KGR-002 `0.1.0-proposed` baseline against the independent KGR-003 result `DESIGNER_REVISION_REQUIRED`. The formal input is the machine-readable input envelope plus seven byte-exact KGR-002 output aliases and seven byte-exact KGR-003 output aliases.

This is a new run because adversarial revision is materially different from initial constitutional design. It uses workflow `KD-R0` through `KD-R5`, produces a proposed `0.2.0-proposed` package, and must disposition every KGR-003 finding. The historical KGR-002 prompt remains immutable because it is evidence of the contract actually used for `INITIAL_DESIGN`; this run preserves a separate, versioned prompt snapshot.

The run may execute in the original Designer chat for continuity or in a fresh isolated Designer chat, but chat memory is not formal provenance. The input envelope and attached artifacts control routing and identity.

## Expected outputs

If no blocker prevents package completion, execution must produce exactly:

1. `00-kernel-design-basis-v0.2.md`
2. `01-kernel-admission-analysis-v0.2.md`
3. `02-kernel-v0.2-draft.md`
4. `03-kernel-clauses-v0.2.yaml`
5. `04-designer-open-questions-v0.2.md`
6. `05-lower-layer-routing-v0.2.md`
7. `06-targeted-adversarial-closure-handoff.md`
8. `07-finding-disposition-register.yaml`

The expected next gate is `TARGETED_ADVERSARIAL_CLOSURE`. Independent closure must occur before Enforcement Engineering can be considered.

## Non-goals

Preparation does not execute the Designer, revise or overwrite the v0.1 proposal, create KGR-004 outputs, perform adversarial closure, begin Enforcement Engineering, ratify the Kernel, or authorize runtime adoption. No claim of validation, enforceability, compliance, operation, or maturity follows from this run structure.
