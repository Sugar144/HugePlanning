# Kernel Designer Protocols

Each materially different Kernel Designer workflow has its own versioned execution protocol. A protocol defines required inputs, role boundaries, stages, outputs, interaction rules, blockers, and handoff conditions. A run must preserve an exact prompt snapshot and may not retroactively alter an earlier run's contract.

Available protocol:

- `adversarial-revision/04-kernel-designer-adversarial-revision-prompt-sol-high-v0.1.0.md` — `ADVERSARIAL_REVISION`, protocol version `0.1.0`, prepared for KGR-004.

Planned modes have no protocol directory or execution contract until a concrete run requires one.
