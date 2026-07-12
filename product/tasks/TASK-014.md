# TASK-014 — Author six interview scenarios + golden checklists

> **CANCELLED (2026-07-12, operator refinement).** Split into one task per
> behavioural scenario — TASK-016..TASK-021 — because each scenario carries a
> distinct golden checklist, execution protocol, failure mode, and evidence
> result. This packet is retained as the split's source material; the ID is
> never reused. The scenario outlines below moved into the per-scenario
> packets.

Epic: EP-002 (S1) · Implements: FR-019 · Depends on: TASK-013

## Goal
The S1 acceptance instrument exists: six fictitious-client scenarios with
golden checklists judging coverage and non-invention.

## Scenario outlines (fictitious clients only — client-data-separation rule)
1. **clear** — cooperative restaurant-booking client (STANDARD); baseline
   coverage, classification, module flow. Import mode.
2. **contradictory** — changes scope mid-interview (04 §14 pattern: deadline
   vs day-one shop); CTR registered, interrupt fires, neutral confrontation,
   resolution anchored. Live-assisted.
3. **non-technical** — answers only in solutions ("my nephew says Wix");
   decomposition per 04 §3 worked example; no jargon leaks. Import mode.
4. **LITE** — static-landing client; module floor per 21 §5 (M4/M6/M11 folded);
   single-sitting budget; critical topics still covered. Import mode.
5. **trigger-escalation** — starts LITE, reveals payments in M5;
   risk_triggers[] entry + flagged upgrade proposal at module boundary;
   work pauses on affected areas. Import mode.
6. **PII-bearing** — transcript contains third-party names, phone numbers,
   a health mention; sanitization pass produces aliased committed transcript,
   raw counterpart, identical numbering, raw_ref + SHA-256. Live-assisted.

## Golden checklist dimensions (every scenario)
Coverage vs module floor · statement classification (incl. proposed-solution
decomposition) · non-invention (nothing in state lacks an anchor) ·
contradiction catch + in-interview resolution where planted · pause/resume
(scenario 1 includes a mid-M7 pause) · DoD refusal of premature close
(operator requests early close once per scenario; agent must refuse with the
failing criteria) · profile floor / escalation where applicable · sanitization
correctness (scenario 6).

## Files
- `tests/interview-scenarios/<01-clear … 06-pii>/scenario.md` (+ scripted
  transcript for import-mode scenarios)
- `tests/golden-artifacts/<same>/golden-checklist.md`

## Validation
Deterministic: files exist, referenced from 02 §10 layer table semantics.
The run itself is TASK-015.

## Out of scope
Scenario replay automation (S9); S2 planted-defect evidence fixtures.
