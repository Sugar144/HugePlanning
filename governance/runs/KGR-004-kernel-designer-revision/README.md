# KGR-004 — Kernel Designer Adversarial Revision

Execution status: `COMPLETED`
Result: `READY_FOR_TARGETED_ADVERSARIAL_CLOSURE`
Mode: `ADVERSARIAL_REVISION`
Kernel: `PROPOSED_NOT_RATIFIED`
Kernel version: `0.2.0-proposed`

## Purpose and provenance

KGR-004 revised the complete KGR-002 `0.1.0-proposed` baseline against the independent KGR-003 result `DESIGNER_REVISION_REQUIRED`. The formal input was the machine-readable input envelope plus seven byte-exact KGR-002 output aliases and seven byte-exact KGR-003 output aliases. All 14 hashes claimed by the output package were independently checked against the envelope and preserved files.

The imported package contains exactly the eight required outputs. It records 15 dispositions: 14 `RESOLVED` and one `ROUTED`, with `KA-F-015` as the routed provider-capability observation. No owner decision is required. The Markdown and YAML Kernel representations were independently parsed and compared for semantic alignment.

The exact ZIP and its eight extracted members are preserved under `governance/sources/raw/packages/`. The run outputs are byte-identical to those members. The package was imported after execution; the exact execution transcript is not preserved. Exact model identity, reasoning setting, execution timestamps, token usage, interaction count, and chat-session identity are `UNKNOWN` or `UNVERIFIED`.

## Outputs

The completed run produced exactly:

1. `00-kernel-design-basis-v0.2.md`
2. `01-kernel-admission-analysis-v0.2.md`
3. `02-kernel-v0.2-draft.md`
4. `03-kernel-clauses-v0.2.yaml`
5. `04-designer-open-questions-v0.2.md`
6. `05-lower-layer-routing-v0.2.md`
7. `06-targeted-adversarial-closure-handoff.md`
8. `07-finding-disposition-register.yaml`

The next gate is independent `TARGETED_ADVERSARIAL_CLOSURE`. These outputs remain Designer work product and are not independent closure evidence. The Enforcement Engineering gate remains `CLOSED`.

## Authority boundary

KGR-004 did not overwrite the v0.1 proposal, perform targeted adversarial closure, begin Enforcement Engineering, ratify the Kernel, or authorize runtime adoption. No claim of enforceability, compliance, operation, or maturity follows from Designer completion. A later duplicate attempt that stopped at `BLOCKED_BY_PACKAGE_CONFLICT` was not imported and did not replace this package.
