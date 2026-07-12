# 22 — Implementation Assurance and Adversarial Validation

**Purpose:** the stage-level assurance process for building the methodology itself — how a stage's normative contract is reconciled before generation, how tests are derived from risk, who implements and who reviews, how failures are classified, and what evidence a release requires. Distilled from the verified S0a experience (S0a experiment report, integration audit, live SPK-01 runs).
**Scope boundary:** this file governs **methodology implementation stages** (the `13` loop and post-release maintenance work on this repository). The client-product task loop stays in `09`; client-product testing stays in `10`; methodology test layers stay in `02` §10. Decision: R2-34 (`19` §5).

---

## 1. The assurance sequence (per implementation stage, proportional)

```text
1. Contract reconciliation        compile the normative set; resolve contradictions (§2)
2. Risk-based adversarial test design   derive checks from material failure risks (§3)
3. Implementation                 one principal implementer (§4)
4. Bounded independent review     only where risk justifies it (§4)
5. Deterministic validation       schemas, fixtures, script tests — repeatable offline
6. Real-runtime validation        live CLI behaviour, where the change touches it (§5)
7. Failure classification         every red result gets a class before a fix (§5)
8. Release evidence               concise, per release (§7)
```

The sequence is fixed; its **depth is not** (§6). A documentation-only change legitimately runs 1 → 3 → 5 → 8 with steps at checklist weight. A runtime-bootstrap or security-sensitive change runs all eight at full weight. Steps never reorder: tests are designed before implementation (S0a's red/green discipline), and no failure is fixed before it is classified.

## 2. Contract reconciliation (step 1)

Before implementing, compile the normative requirements affecting the stage and reconcile them across every place they are stated: closed normative sets (enums, gate lists, counter namespaces), examples, schemas, templates, scripts, acceptance criteria, and previous decisions (`16`, `19`). On conflict, the four-layer precedence applies and the conflict is **recorded, never resolved silently** (CLAUDE.md invariant 2).

- **Examples never silently shrink a closed set defined normatively elsewhere.** S0a lesson F1: `03` §4's *example* `project.yaml` showed 6 approval gates, and the generated schema inherited that subset instead of the normative G0–G9 list (`01` §4.2) — likewise 21 counters instead of the full `06` §4 namespace. Reconciliation would have caught both before implementation; the integration audit caught them after.
- The result is **proportional to the change**: a compact matrix or checklist (normative source → implementing artifact → agree/conflict) kept in the working notes or the stage PR description. It becomes a permanent artifact only when the stage's blast radius warrants it; most stages need no new committed file for this.
- An unresolved contradiction is a stage blocker, handled per the open-question discipline — never an implementer's silent choice.

## 3. Risk-based adversarial test design (step 2)

Tests are derived from **material failure risks**, not from a desire to maximize test count. For each risk the stage plausibly carries, pick the cheapest check class that would actually catch it:

| Check class | Catches | S0a examples |
|---|---|---|
| Static / document checks | Contradictions, stale references, count/enum drift in prose | gate-list and counter completeness vs the conventions rule |
| Schema & contract checks | Instances violating the locked contract; fixtures asserting each declared failure reason | valid/invalid fixtures; `# expect-error:` assertions |
| Script failure-path checks | Refusal and no-partial-output behaviour, not just happy paths | dirty-methodology refusal (F2), validate-before-commit (F3), no-partial-target |
| Runtime integration checks | Behaviour only the real harness exhibits | SPK-01 live checks a–d; deny rules under a path with spaces |
| Regression checks | A classified past failure staying dead | drift-alert firing; methodology-unchanged assertion after a test run |

Failure paths deserve at least the attention of happy paths — S0a's material defects (F2, F3) were refusal-path gaps. **Not** the default: multiple exhaustive parallel implementations, repository-wide adversarial audits, or test-count targets. Those are deliberate, budgeted exceptions (§4).

## 4. Implementation and review policy (steps 3–4)

- **One principal implementer** per stage or change — one accountable author of code and tests, in the main session.
- **Bounded independent review only when risk justifies it** (§6 factors). There is **no minimum number of subagents, and no general-purpose Fable subagents by default.** When a subagent or external auditor is used, its brief states explicitly: scope, model, tool access, turn/token budget, and stopping criterion. An unbounded "review everything" delegation is a process defect.
- **Correction cycles are bounded:** at most 2 per defect class, then escalate to the operator and re-examine the design contract, not the output (consistent with DEC-20 and `13` §2).
- **ChatGPT or another model may serve as a targeted gate auditor** — a bounded second opinion on a specific gate artifact or diff. The S0a **parallel duplicate implementation** (two full candidates, one selected) was an experiment; it produced value once (F2's fix was adopted from the non-selected candidate) but it is **experimental, not the default lifecycle** — invoke it only by explicit decision with recorded rationale.

## 5. Failure classification (step 7) and runtime-result classes

Every failing check is classified **before** it is fixed; the class determines what gets changed (seven classes since R2-39, which added `DATA` and `OPERATOR` when S1 scenario execution made them material; `SPEC`, where it appears in operator-side notes, normalizes to `CONTRACT`; records predating R2-39 used the original five classes, which map unchanged):

| Class | Meaning | Fix target | Instance |
|---|---|---|---|
| `CODE` | Implementation wrong against an agreed contract | The implementation | committed `__pycache__` bytecode dirtying the tree (S0a) |
| `TEST` | The check itself is wrong or asserts the wrong thing — incl. oracles, fixtures, golden checklists as scoring instruments | The test/oracle | fixture declaring a token jsonschema never emits (S0a) |
| `CONTRACT` | Sources of truth disagree; implementation followed the wrong one (aka `SPEC`) | The contract + reconciliation record | 6-gate schema vs normative G0–G9 (F1, S0a) |
| `DATA` | Scenario/input material malformed, incomplete, contaminated, or unsuitable for what the run must test (R2-39) | The scenario data / import material | an import transcript missing the planted material its golden scores |
| `OPERATOR` | A human executed, relayed, or scored a sound procedure incorrectly during a run (R2-39) | Re-run the affected portion; correct the human step | persona fact volunteered unasked in a live sitting; golden item mis-scored |
| `PROCESS` | The prescribed workflow itself allowed a preventable defect through | The process (this file, checklists) | validation not required before the initial client commit (F3, S0a) |
| `ENVIRONMENT` | Harness/CLI/tooling limitation, not the product | Recorded limitation or compensating control | deny rules not binding subprocesses (S0a); CLI session limit mid-run (S1) |

`OPERATOR` vs `PROCESS`: if the human erred following a sound procedure, it is `OPERATOR` (fix the execution, re-run); if the procedure itself permitted the defect, it is `PROCESS` (fix the procedure). Conflating them mis-targets the fix.

**A failing oracle is never automatically a product failure.** S0a lesson F4: SPK-01's sentinel matching produced a false negative on a genuinely working session — a `TEST`-class defect; treating it as `CODE` would have "fixed" working behaviour. Runtime verification results therefore always distinguish four outcomes:

1. **Deterministic fake-runtime validation** — the offline suite's simulated runtime (repeatable, cheap, runs everywhere);
2. **Actual live-runtime validation** — the real CLI exercised (SPK-01-class evidence; required whenever runtime loading paths or runtime configuration changed);
3. **Environment unavailable / inconclusive** — recorded as exactly that (like the ChatGPT candidate's `SPK-01 UNVERIFIED, exit 77`), never converted into a pass *or* a fail;
4. **Genuine functional failure** — confirmed against the contract after classes 1–3 are excluded (F5: the Skill fixture that failed under the real runtime).

## 6. Proportionality

Assurance depth is decided per change from these factors — the same risk logic the client-side process uses (`21`), applied to the methodology itself:

- **Blast radius** — how many artifacts, stages, or client repos inherit the change (schemas and templates replicate into every future client);
- **Reversibility** — a doc edit reverts trivially; a released schema or a generated client repo does not;
- **Replication risk** — defects copied outward by `new-client.sh` before detection;
- **Security/privacy impact** — deny rules, evidence handling, PII paths;
- **External-tool integration** — behaviour owned by the CLI/harness, verifiable only live;
- **Contract ambiguity** — how much §2 reconciliation found to disagree.

Low on all factors (typo fixes, navigation, planning prose): steps 2/4/6 collapse to near-zero — **small documentation-only changes must not inherit the runtime-bootstrap process.** High on any factor: full sequence, live runtime validation, and independent review of the affected surface.

## 7. Release evidence (step 8)

Before a release (tag), record concisely — in the CHANGELOG entry, release notes, or an experiment/verification report, **never as duplicated full logs inside planning files**:

- the exact **tested commit**;
- **deterministic results** relevant to the change (suite totals, e.g. `122 passed / 0 failed`, and reruns);
- **real-runtime results** where relevant (SPK-01 outcome + CLI version), or the explicit statement that no runtime surface changed;
- **repository cleanliness** (clean tree after the test run — the suite's methodology-unchanged assertion);
- **known limitations** carried into the release;
- the exact **release/tag state** (tag ↔ commit).

The S0a records (`README.md` SPK-01 log, `CHANGELOG.md` 0.1.0, the S0a experiment report) are the reference examples of this weight: complete enough to audit, small enough to read.

## 8. Traceable basis — S0a lessons

| Lesson | Source | Lands in |
|---|---|---|
| F1 — examples shrank closed normative sets (gates, counters) | integration audit | §2 reconciliation rule |
| F2 — dirty-bootstrap warning instead of refusal | both S0a candidates' reviews | §3 failure-path checks |
| F3 — validation not enforced before initial client commit | operator evaluation | §3, `PROCESS` class in §5 |
| F4 — SPK sentinel false negative (oracle defect) | operator evaluation | §5 oracle rule + runtime classes |
| F5 — candidate Skill failed only under the real runtime | operator evaluation | §5 class 2 vs 3 distinction |
