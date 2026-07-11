# 07 — Requirements and Specification Pipeline

**Purpose:** the pipeline from raw interview evidence to an approved business baseline: normalization, audits, product backlog, content inventory, PRD generation, client validation, estimation checkpoint, and the G1/G2 gates.
**Baseline traceability:** B12, B14, §12 steps 4–6; decisions DEC-05, DEC-08, DEC-15, DEC-16; closes G-11, G-12. **V2:** ownership fix — product backlog by backlog-refinement (R2-04); origins & structured NFRs (R2-10); profile confirmation at G1 (R2-01); content inventory (R2-18); LITE combined gates (R2-19).

---

## 1. Pipeline overview

```text
Sanitized interview evidence (04)             stage: discovery → specification
   ↓ requirements-normalization (skill)
requirements.yaml + solution-context.yaml (+risk_triggers) + open-questions.yaml (draft)
   ↓ requirements-auditor (agent) — 5 audits + origin-integrity check
Audit report → fixes (bounded: max 2 fix cycles, DEC-20)
   ↓ G1: your internal review + PROFILE CONFIRMATION (21 §4)
   ↓ backlog-refinement (product mode): product-backlog.yaml   [layer 2]
   ↓ content inventory completed (§9)                          [layer 2]
   ↓ doc-generator: PRD + validation-package                   [layer 3]
   ↓ estimation checkpoint (you, DEC-16)
   ↓ Client validation session
G2: business baseline → evidence/confirmations/ + docs/handoffs/G2-*.yaml
    → docs PR → merge to main (merge commit = approved_in)
```

Everything runs on branch `docs/discovery-01`; G2 merges it (`11` §2). **LITE path (`21` §5):** G1+G2 combine — internal check, then one 1-page validation email; product backlog may be skipped (task list derives directly at G3-lite).

## 2. Requirements normalization (skill contract)

**Input:** interview registers + transcript anchors. **Output:** populated `requirements.yaml` per schema `06` §7.1. Rules:

1. **Atomic:** one verifiable obligation per requirement; compound client statements split (each keeps the same source_ref).
2. **Testable wording:** active voice, measurable where quantitative; vague adjectives replaced by the concretization obtained in-interview or flagged (`precision: low` → OQ).
3. **Typed:** functional / nonfunctional (nfr-catalog category) / integration / constraint; business rules separated into `business_rules` (they parameterize FRs, they are not FRs).
4. **Deduplicated:** same obligation from two turns → one requirement, both source_refs.
5. **Solution-decomposed:** client-proposed solutions stored as `client_preference` notes on the underlying need, never as requirements (`04` §3).
6. **Sourced:** no source_ref → cannot exist. The skill may *propose* an obviously implied requirement only as `status: draft` + `assumptions: [ASM-nnn unconfirmed]` and it must appear in the validation package.
7. **Origin-tagged (V2, R2-10):** every requirement carries `origin`; a `methodology_default` or `legal_or_regulatory` item enters as `status: proposed_default` and can never read as if the client said it — it is confirmed at G2 or consciously adopted with a record.
8. **NFRs structured (V2, R2-10):** metric/target/conditions/measurement/verification_level per `06` §7.1; an unquantifiable quality statement either gets a concretized target, or is recorded as an explicitly waived NFR with your sign-off — never left as prose.
9. **Data typed (V2):** data/import/migration obligations become `DAT-` requirements; content obligations go to the content inventory (§9), not requirements.yaml.
10. **Prioritized:** MoSCoW from M10 scope decisions; every `must` traces to an OBJ.
11. **Risk-rated:** high = money, auth, personal data, legal, or core business flow (drives review/test depth, `09`/`10`).

## 3. NFR completion

The NFR floor comes from the profile matrix (`21` §5), explained by the nfr-catalog (`17` §K.3): performance, accessibility (WCAG 2.2 AA as default target for public EU-market sites), security, privacy/GDPR, SEO basics, browser/device matrix, backup/recovery, maintainability. Missing floor NFRs are added as `status: proposed_default` with `origin: methodology_default` — the client confirms or adjusts them at G2 (never silently imposed, never silently omitted; R2-10).

## 4. The five audits (requirements-auditor agent)

| Audit | Detects | Output |
|---|---|---|
| Ambiguity | Untestable wording, vague quantifiers, undefined terms (glossary check) | Findings list with severity + suggested rewrite |
| Contradiction | REQ↔REQ, REQ↔BR, REQ↔solution-context, REQ↔budget/deadline conflicts | CTR entries |
| Assumption | Unconfirmed ASMs load-bearing for `must` requirements; inferences posing as facts (source_ref spot-check against transcript); **origin integrity: no `methodology_default`/`technical_derived` item reading as client evidence (R2-10)** | Findings + required confirmations |
| Coverage | Every OBJ has ≥1 must FR; NFR floor present; every M-topic marked `sufficient` reflected in artifacts; every FR has ≥1 AC | Gap list |
| Schema & traceability | `validate.sh` + dangling IDs, orphan ACs | Machine report |

Auditor is a *different session/agent* than the producer (independence). Findings → fix cycle by normalization skill → re-audit only failed checks. Max 2 cycles, then G1 review decides (DEC-20).

## 5. G1 — internal review gate (you)

Checklist: audits clean or accepted-with-note · interview DoD report (`04` §12) reviewed · OQ list triaged (blocking vs G2-carry) · sensitivity/privacy flags handled · **profile confirmed against `risk_triggers[]` (`21` §4) — recorded in `profile_history`** · content inventory seeded and owners assigned · you actually read `requirements.yaml` (sampling is allowed for >100 items, `must`+`high-risk` read fully). Record: `docs/handoffs/G1-discovery-review-<seq>.yaml`. Statuses move `draft → under_review`.

## 6. Contradiction resolution workflow

CTRs found post-interview: (a) resolvable from evidence → resolve with anchor refs; (b) needs client → CLAR; (c) genuine tension (e.g., budget vs NFR) → escalate to G2 discussion as an explicit decision item. `accepted_as_tension` requires your sign-off and a note in the validation package. No CTR is closed without a recorded basis.

## 7. Product backlog and document generation (V2 ownership, R2-04)

**Product backlog** — `backlog-refinement` skill, **product mode** (layer 2): epics from objectives; **vertically sliced stories** (`08` §1a — outcomes, not renamed FRs); scope phases; priorities; acceptance intent by AC reference. No technical decomposition yet.

**Documents** — `doc-generator` agent (layer 3 only): **PRD.md** (client language; cites IDs) · **validation-package.md** — the G2 instrument, plain language, per template `06` §6, including: what we understood · what will be built first (MVP list) · what is explicitly excluded · assumptions requiring confirmation (all unconfirmed ASMs + every `proposed_default` item) · content list with owners and deadlines · open questions with owners · estimate & timeline vs stated budget · confirmation checklist. Doc-generator must not introduce any statement lacking a layer-2 ID — the auditor spot-checks this ("no invention" golden test, `02` §10). **Brevity rule (R2-19):** the client-facing package targets ≤4 pages (LITE: 1 page); depth lives in the repo, not in the client's inbox.

## 8. Estimation checkpoint + G2 — business baseline (client)

**Estimation (DEC-16, you, manual at MVP):** rough effort from product backlog (T-shirt per epic → range in days/€) confronted with the client's budget/deadline from M10. Breach → scope negotiation *before* the validation session (options: cut moscow `should`s, phase, adjust budget). The validation package always shows the estimate — no silent scope-price mismatch survives G2.

**G2 session:** walk the client through the validation package (call or annotated email per client preference). Client confirms each section; corrections are evidence (new confirmation record or clarification), applied to layer 2, package regenerated if material (max 2 rounds, then a decision meeting). **Approval record** in `evidence/confirmations/` (baseline §11.3 format retained) **+ `docs/handoffs/G2-business-baseline-<seq>.yaml`**. Then: docs PR merged to `main`; requirement statuses → `approved` with `approved_in: <merge commit>` (R2-10); `proposed_default` items → `approved` or removed per client decision; stage → `technical_design`. From this moment changes go through change control (`12` §5).

## 9. Content and asset readiness (V2, R2-18)

`content-inventory.yaml` (`06` §7.6) is completed here: every page/asset from the PRD scope gets a CNT item with owner, deadline, license/provenance (rigor per profile), and `needed_by` story refs. Rules: content deadlines are set against the delivery sequence (content for early stories lands first); the engagement's content clause makes deadlines contractual; **story DoR consumes this** (`08` §7); placeholders are allowed for structure work when explicitly `placeholder_approved`, and any release shipping placeholders needs client sign-off at G7. A passed deadline is escalated as a CR (`12` §5), never silently absorbed. The inventory is a checklist artifact — no content-management tooling is built (rejected scope).

## 10. Failure paths

Client rejects large parts → back to targeted clarification/mini-interview (import mode gap analysis, `04` §2), not a full restart. Client unresponsive → project `paused` with dated note. Audits keep failing after 2 cycles → the interview was insufficient: reopen specific modules as a follow-up sitting (evidence dir `client-discovery-01`, new session), not a new interview.
