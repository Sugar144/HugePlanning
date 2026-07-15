---
artifact_id: KA-C00
run: KGR-005
role: Kernel Adversary
mode: TARGETED_CLOSURE
protocol: GOV-PROTOCOL-002
protocol_version: 0.1.0
loop: GOV-LOOP-001
loop_version: 0.1.0
status: COMPLETE
language: English
kernel_version: 0.2.0-proposed
kernel_status: PROPOSED_NOT_RATIFIED
---

# KGR-005 Targeted Closure Basis

## Execution identity and boundary

The exact supplied execution contract matches `GOV-PROMPT-007`, `GOV-PROTOCOL-002` version `0.1.0`, run `KGR-005`, role `Kernel Adversary`, and mode `TARGETED_CLOSURE`. The separately supplied exact prompt snapshot has SHA-256 `171914d7d6ff7024330ecccc1d662055ee8b77c4402a0c4bcac4271cbc98f67a`, matching `GOV-INPUT-002`. The formal input ZIP has SHA-256 `26291b32594f2b73e12107bec9572b528e4ec3e32e4ca08f9746c5aba1adf9cf`.

The review was limited to the 19 formal transport members. It did not inspect repository provenance paths, runtime, S0a/S1/S2, CI, branch protection, providers, or enforcement implementation. Scenarios are constitutional thought experiments, not executed control fixtures.

## KA-C0 validation result

`PASSED`. Deterministic isolated-input validation found exactly 19 safe, readable members, no duplicates, no encryption or symlinks, no traversal or absolute paths, and no hash or identity mismatch. The package confirms:

- KGR-003 result: `DESIGNER_REVISION_REQUIRED`.
- KGR-004 result: `READY_FOR_TARGETED_ADVERSARIAL_CLOSURE`.
- Original findings: `KA-F-001` through `KA-F-015`, with the fixed severity map.
- Proposal: `0.2.0-proposed` / `PROPOSED_NOT_RATIFIED`.
- Enforcement Engineering gate: `CLOSED`.
- Human ratification: `NOT_STARTED`.
- Counters before execution: targeted closure `0`; Designer remediation `0`.

## Exact formal member manifest

| Package member | SHA-256 |
|---|---|
| `input-envelope.yaml` | `ef943325bdf6625fb6901990d80b3008c37f362458f0a5e4b9d9e1f181b2d6d2` |
| `control/kernel-design-closure-loop-v0.1.0.yaml` | `cf7855a85d4ab9f3d4bb42c14ebbb0e735abcde938796f88284160904031fbe1` |
| `inputs/current-proposal/00-kernel-design-basis-v0.2.md` | `114659b02efbd983afbdde37e66520a0a8d02d224b6bdf718c4f056ce12d81a5` |
| `inputs/current-proposal/01-kernel-admission-analysis-v0.2.md` | `f3154923a7aefee165fac387f617c343c2294751722e8bd27eb6e1b84576642e` |
| `inputs/current-proposal/02-kernel-v0.2-draft.md` | `0dba205609e0b3c2df2fdfa6ee5b393174a9bffb1b12c5a24a2eecd4820b8545` |
| `inputs/current-proposal/03-kernel-clauses-v0.2.yaml` | `0b48212543b54eb775e4bd5e6688dae3ff19eabb11f89ee4750b11faf7dd2ca1` |
| `inputs/current-proposal/04-designer-open-questions-v0.2.md` | `184e4345b390f9f91256565c508ebff8b80bfd0e7109d5e89614187cb79a85d4` |
| `inputs/current-proposal/05-lower-layer-routing-v0.2.md` | `6f62a56a56c57ba07a07125bd75fbcfe5a51db34f024f7f4ecdaec3ff2c1afee` |
| `inputs/current-proposal/06-targeted-adversarial-closure-handoff.md` | `a0ca01b5ac39827ad8725a7d3acdac5220564ef4f8e29b239ae6cfb454049f65` |
| `inputs/current-proposal/07-finding-disposition-register.yaml` | `c1b1aad7312c795131573d89a6c402e115ddb206abfb3a97a1d3d1687c4eacbd` |
| `inputs/original-review/00-adversarial-review-basis.md` | `5085b382ad6b7b33567ff07b049af447b6888dcaa69cf69bdfcb9140dbeeef9d` |
| `inputs/original-review/01-adversarial-findings.md` | `6bce1ec9d22ad68441980da2e22549787f0693c7fbee151978bc74129c64134b` |
| `inputs/original-review/02-adversarial-scenarios.md` | `29fec90c532423a2579ed810b618b65141feb73ef276660c4c59b9bb4ef6de1c` |
| `inputs/original-review/03-revision-directives.md` | `2cdbf4196a95112654f64606c0d52a68f6a3b7db5ee0219d48eaac20aee29669` |
| `inputs/original-review/04-owner-decision-register.md` | `e8333eca71a0a6a5a2560c27ce3e45e7e8df5fda9a5516173a1cd1c8c2a1bbb3` |
| `inputs/original-review/05-enforcement-concerns.md` | `d663f7228f259e126fdfb659152972b857e0fbcf314d0f490e71c8e66cad005c` |
| `inputs/original-review/06-adversarial-summary-and-handoff.md` | `d4917152a39d878f20b84d0885dbf1bf10045615a0eb1c210f6e6bd6677fa495` |
| `inputs/predecessor-kernel/02-kernel-v0.1-draft.md` | `cbd1bce2edb9a369b9de3f6b2466709d9c00c2952c69030424cca3f73ecb463d` |
| `inputs/predecessor-kernel/03-kernel-clauses.yaml` | `bcf5816162396ff4a99d3a42d20c1705ec2c80fe2dcd55976c9c31e2acdd053a` |

## Review method

KA-C1 compared each original exploit path, directive, scenario, Designer disposition, acceptance criterion, and affected revised clause. KA-C2 reran the 15 mandated scenarios and the required regression families. KA-C3 compared Markdown and YAML metadata, interpretation, all seven clause fields, amendment rules, and adoption states, then tested solo-owner proportionality. KA-C4 classified every residual risk without treating routing as capability evidence. KA-C5 applied the single ordered loop result matrix.

## Authority statement

This completed Adversary work product declares only bounded independent semantic closure. It does not mutate the Kernel, increment counters, create a Controller transition, accept risk, authorize Enforcement Engineering, ratify, adopt, or establish enforceability, implementation, operation, compliance, or maturity.
