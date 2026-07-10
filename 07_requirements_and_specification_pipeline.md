# 07 — Requirements and Specification Pipeline

**Purpose:** the pipeline from raw interview evidence to an approved business baseline: normalization, audits, PRD generation, client validation, estimation checkpoint, and the G1/G2 gates.
**Baseline traceability:** B12, B14, §12 steps 4–6; decisions DEC-05, DEC-08, DEC-15, DEC-16; closes G-11, G-12.

---

## 1. Pipeline overview

```text
Interview evidence (04)                       stage: discovery → specification
   ↓ requirements-normalization (skill)
Candidate requirements.yaml + solution-context.yaml + open-questions.yaml (draft)
   ↓ requirements-auditor (agent) — 5 audits
Audit report → fixes (bounded: max 2 fix cycles, DEC-20)
   ↓ G1: your internal review
   ↓ doc-generator (agent): PRD + product-backlog + validation-package
   ↓ estimation checkpoint (you, DEC-16)
   ↓ Client validation session
G2: business baseline → evidence/confirmations/ → docs PR → merge to main
```

Everything runs on branch `docs/discovery-01`; G2 merges it (`11` §2).

## 2. Requirements normalization (skill contract)

**Input:** interview registers + transcript anchors. **Output:** populated `requirements.yaml` per schema `06` §7.1. Rules:

1. **Atomic:** one verifiable obligation per requirement; compound client statements split (each keeps the same source_ref).
2. **Testable wording:** active voice, measurable where quantitative; vague adjectives replaced by the concretization obtained in-interview or flagged (`precision: low` → OQ).
3. **Typed:** functional / nonfunctional (nfr-catalog category) / integration / constraint; business rules separated into `business_rules` (they parameterize FRs, they are not FRs).
4. **Deduplicated:** same obligation from two turns → one requirement, both source_refs.
5. **Solution-decomposed:** client-proposed solutions stored as `client_preference` notes on the underlying need, never as requirements (`04` §3).
6. **Sourced:** no source_ref → cannot exist. The skill may *propose* an obviously implied requirement only as `status: draft` + `assumptions: [ASM-nnn unconfirmed]` and it must appear in the validation package.
7. **Prioritized:** MoSCoW from M10 scope decisions; every `must` traces to an OBJ.
8. **Risk-rated:** high = money, auth, personal data, legal, or core business flow (drives review/test depth, `09`/`10`).

## 3. NFR completion

The nfr-catalog defines the floor per archetype (`02` §9): performance, accessibility (WCAG 2.2 AA as default target for public EU-market sites — recorded as NFR with source `methodology-default`, shown to client in validation package), security, privacy/GDPR, SEO basics, browser/device matrix, backup/recovery, maintainability. Missing floor NFRs are added as `draft` + flagged `origin: methodology_default` — the client confirms or adjusts them at G2 (never silently imposed, never silently omitted).

## 4. The five audits (requirements-auditor agent)

| Audit | Detects | Output |
|---|---|---|
| Ambiguity | Untestable wording, vague quantifiers, undefined terms (glossary check) | Findings list with severity + suggested rewrite |
| Contradiction | REQ↔REQ, REQ↔BR, REQ↔solution-context, REQ↔budget/deadline conflicts | CTR entries |
| Assumption | Unconfirmed ASMs load-bearing for `must` requirements; inferences posing as facts (source_ref spot-check against transcript) | Findings + required confirmations |
| Coverage | Every OBJ has ≥1 must FR; NFR floor present; every M-topic marked `sufficient` reflected in artifacts; every FR has ≥1 AC | Gap list |
| Schema & traceability | `validate.sh` + dangling IDs, orphan ACs | Machine report |

Auditor is a *different session/agent* than the producer (independence). Findings → fix cycle by normalization skill → re-audit only failed checks. Max 2 cycles, then G1 review decides (DEC-20).

## 5. G1 — internal review gate (you)

Checklist: audits clean or accepted-with-note · interview DoD report (`04` §12) reviewed · OQ list triaged (blocking vs G2-carry) · sensitivity/privacy flags handled · you actually read `requirements.yaml` (sampling is allowed for >100 items, `must`+`high-risk` read fully). Record: `handoff.yaml` (`gate: G1, approved_by: developer, commit`). Statuses move `draft → under_review`.

## 6. Contradiction resolution workflow

CTRs found post-interview: (a) resolvable from evidence → resolve with anchor refs; (b) needs client → CLAR; (c) genuine tension (e.g., budget vs NFR) → escalate to G2 discussion as an explicit decision item. `accepted_as_tension` requires your sign-off and a note in the validation package. No CTR is closed without a recorded basis.

## 7. Document generation (doc-generator agent)

Generates from layer 2 (`06` §5 rules): **PRD.md** (client language; cites IDs) · **product-backlog.yaml** (EP + provisional US mapped to FRs; no technical decomposition yet) · **validation-package.md** — the G2 instrument, plain language, per template `06` §6, including: what we understood · what will be built first (MVP list) · what is explicitly excluded · assumptions requiring confirmation (all unconfirmed ASMs + methodology-default NFRs) · open questions with owners · estimate & timeline vs stated budget · confirmation checklist. Doc-generator must not introduce any statement lacking a layer-2 ID — the auditor spot-checks this ("no invention" golden test, `02` §10).

## 8. Estimation checkpoint + G2 — business baseline (client)

**Estimation (DEC-16, you, manual at MVP):** rough effort from product backlog (T-shirt per epic → range in days/€) confronted with the client's budget/deadline from M10. Breach → scope negotiation *before* the validation session (options: cut moscow `should`s, phase, adjust budget). The validation package always shows the estimate — no silent scope-price mismatch survives G2.

**G2 session:** walk the client through the validation package (call or annotated email per client preference). Client confirms each section; corrections are evidence (new confirmation record or clarification), applied to layer 2, package regenerated if material (max 2 rounds, then a decision meeting). **Approval record** in `evidence/confirmations/` (baseline §11.3 format retained: date, person, artifacts, commit, result, observations). Then: requirement statuses → `approved` with `approved_in: <commit>`; docs PR merged to `main`; stage → `technical_design`. From this moment changes go through change control (`12` §5).

## 9. Failure paths

Client rejects large parts → back to targeted clarification/mini-interview (import mode gap analysis, `04` §2), not a full restart. Client unresponsive → project `paused` with dated note. Audits keep failing after 2 cycles → the interview was insufficient: reopen specific modules as a follow-up sitting (evidence dir `client-discovery-01`, new session), not a new interview.
