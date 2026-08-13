# Kernel Designer Protocols

Each materially different Kernel Designer workflow has its own versioned execution protocol. A protocol defines required inputs, role boundaries, stages, outputs, interaction rules, blockers, and handoff conditions. A run must preserve an exact prompt snapshot and may not retroactively alter an earlier run's contract.

Available protocols:

- `adversarial-revision/04-kernel-designer-adversarial-revision-prompt-sol-high-v0.1.0.md` — `ADVERSARIAL_REVISION`, protocol version `0.1.0`, executed for KGR-004.
- `closure-remediation/06-kernel-designer-closure-remediation-prompt-sol-high-v0.1.0.md` — `CLOSURE_REMEDIATION`, protocol version `0.1.0`, defined as a reusable future-instantiation basis. It is not directly execution-ready; a valid targeted-closure result and Controller-created run-specific contract/envelope are required. Its ordered four-result contract routes readiness, owner decision, research, or structural redesign through the Controller; it never permits Designer-declared closure.

`KERNEL_AMENDMENT` remains planned without a protocol or instantiated run.
