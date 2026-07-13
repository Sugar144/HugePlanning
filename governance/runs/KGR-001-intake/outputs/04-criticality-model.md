---
artifact_id: KIP-04
title: HugePlanning Criticality Model
version: 0.1.0
date: 2026-07-13
status: READY_WITH_NON_BLOCKING_QUESTIONS
artifact_type: kernel-design-input
language: English
---

# HugePlanning Criticality Model

## 1. Purpose

This model determines the minimum control required for an action, task, stage, release, or related set of changes.

It prevents two opposite failures:

- treating everything as critical and creating permanent bureaucracy;
- treating small-looking actions as safe when their effects are sensitive, propagating, or constitutional.

## 2. Criticality levels

### `C0 — Informational`

- No state change.
- Typical examples: read, search, analysis, non-authoritative proposal.
- An error can be discarded without affecting canonical state.

**Minimum controls**

- Identify important sources.
- Distinguish fact, inference, proposal, and uncertainty.
- Confirm that no state-changing effect is authorized.

### `C1 — Local and reversible`

- Bounded change to a local artifact, task, or isolated branch.
- Easy to restore.
- No sensitive, external, architectural, or constitutional impact.

**Minimum controls**

- Brief contract.
- Bounded scope and paths.
- Automatic or deterministic validation where applicable.
- Simple rollback.
- Compact traceability.
- Automatic acceptance may be allowed by explicit standing policy.

### `C2 — Propagating`

- May affect multiple artifacts, decisions, agents, workflows, schemas, or later stages.
- The effect remains internal and recoverable but can influence substantial downstream work.

**Minimum controls**

- Full traceability.
- Explicit contract and affected-surface analysis.
- Proportional independent evaluation.
- Propagation and compatibility checks.
- Delegated acceptance by an evaluator or release reviewer.
- Known limitations recorded.

### `C3 — Sensitive or externally consequential`

- Affects production, users, clients, personal or confidential data, credentials, money, publication, legal obligations, security, or difficult recovery.
- May have an external blast radius or require significant human judgment.

**Minimum controls**

- Explicit authorization.
- Least privilege and bounded effects.
- Independent and, when relevant, specialist evaluation.
- Tested rollback or credible recovery/compensation plan.
- Human acceptance.
- Incident readiness and stronger observability.

### `C4 — Constitutional`

- Changes the kernel, authority hierarchy, ratification, maximum permissions, fundamental scope, or constitutional protections.
- May redefine who can decide, authorize, validate, accept, or amend the system.

**Minimum controls**

- Formal proposal.
- Evidence and alternatives analysis.
- Kernel admission analysis.
- Impact and compatibility analysis.
- Adversarial review.
- Enforcement analysis.
- Migration plan.
- Human ratification.
- Explicit versioning.

## 3. Classification factors

### HUMAN_DECISION

Criticality considers all of the following:

- whether state changes;
- protected assets affected;
- reversibility `R0–R4`;
- blast radius `B0–B4`;
- external effects;
- security, privacy, financial, and legal impact;
- authority and permissions;
- propagation to later stages or decisions;
- ambiguity and uncertainty;
- detectability `D0–D4`;
- recoverability;
- need for human judgment.

No single numerical score is required. False precision should be avoided.

## 4. Relationship among scales

Criticality is not identical to reversibility or blast radius.

Examples:

- A reversible permission change can still be `C3` because it temporarily grants a sensitive capability.
- A one-line kernel change is `C4` despite its size.
- A large local refactor may remain `C1` or `C2` when isolated, reversible, and behavior-preserving.
- A read-only analysis remains `C0` even if intellectually complex.

The classifier should consider:

```text
asset importance
+ actual effect
+ reversibility
+ blast radius
+ detectability
+ uncertainty
+ authority
+ externality
→ criticality
```

## 5. Deterministic floors

### STRONG_PROPOSAL FOR POLICY OR ENFORCEMENT

Certain actions should receive minimum criticality floors:

| Action | Minimum |
|---|---|
| Read-only analysis without canonical change | `C0` |
| Local documentation correction with no normative change | `C1` |
| Change to a shared schema, evaluator, workflow, or canonical requirement | `C2` |
| Production, credentials, personal data, money, public release, sensitive external system | `C3` |
| Kernel, authority hierarchy, ratification, maximum autonomy, constitutional exception | `C4` |

The Kernel Designer should decide whether any of these floors belong constitutionally or in policy.

## 6. Uncertainty rule

### HUMAN_DECISION

When uncertainty is material:

1. Assign the higher reasonable provisional level.
2. Continue read-only investigation where safe.
3. Identify the missing evidence.
4. Reclassify only after evidence supports reduction.

The implementer may challenge a classification but may not lower it.

- Lowering `C3` requires independent review.
- Lowering `C4` or deciding that a constitutional action is not constitutional requires human authority.
- Excessive classification should also be corrected when evidence shows lower risk.

## 7. Aggregation rule

### HUMAN_DECISION

Criticality is assessed over the **cumulative related effect**, not only each commit or task.

Raise classification when:

- several changes modify the same subsystem;
- the set changes behavior, architecture, authority, or acceptance;
- changes share one intent, release, or capability;
- multiple automerges create propagation not visible individually;
- fragmentation would avoid stronger controls;
- combined effects exceed a blast-radius or sensitivity threshold.

## 8. Classification procedure

A lightweight classification flow:

```text
1. Does it modify state?
   no → usually C0

2. Does it affect kernel, authority, ratification, or maximum permissions?
   yes → C4

3. Does it affect production, external systems, sensitive data, credentials,
   money, security, legal obligations, or difficult recovery?
   yes → at least C3

4. Can it propagate across multiple canonical artifacts, workflows,
   schemas, agents, or later stages?
   yes → at least C2

5. Is it truly local, bounded, observable, and easily reversible?
   yes → C1

6. Is any material effect uncertain?
   yes → provisionally raise one reasonable level or apply the relevant floor
```

## 9. Acceptance ownership

| Level | Acceptance |
|---|---|
| `C0` | No state-changing acceptance; proposal or analysis may be consumed by an authorized actor |
| `C1` | Authorized automatic gate or delegated reviewer |
| `C2` | Delegated evaluator or release reviewer |
| `C3` | Human owner with independent evidence |
| `C4` | Formal human ratification |

An executor never approves its own critical exception.

## 10. Validation independence

Minimum independence rises with criticality:

| Level | Minimum independence |
|---|---|
| `C1` | Separate automatic validation |
| `C2` | Separate evaluator execution and externally owned rubric |
| `C3` | Independent evaluation plus specialist or different method when relevant |
| `C4` | Designer, Adversary, Enforcement Engineer, and Ratification Owner separated functionally |

Separate chats alone do not prove independence.

## 11. Result states

Allowed validation outcomes:

- `PASS`
- `FAIL`
- `INCONCLUSIVE`
- `BLOCKED`

`INCONCLUSIVE` is not a pass.

For `C2–C4`, work cannot cross a gate when uncertainty affects a mandatory criterion.

## 12. Qualified acceptance

`ACCEPTED_WITH_LIMITATIONS` is allowed only when:

- limitations are explicit;
- mandatory constitutional controls are not violated;
- residual risk is evaluated;
- impact and scope are understood;
- deferral has a reason;
- an owner and review condition exist;
- the proper authority accepts it.

It is forbidden when essential evidence is absent, core purpose fails, downstream work becomes invalid, security/privacy risk is unacceptable, or fatigue is the real justification.

## 13. Calibration

This model is provisional and should be calibrated from real executions.

Calibration may change:

- policy thresholds;
- examples;
- automatic classification rules;
- required validation depth;
- scenario selection.

Calibration must not silently weaken constitutional protections.
