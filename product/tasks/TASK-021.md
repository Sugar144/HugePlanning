# TASK-021 — Scenario 06 PII-bearing: sanitization correctness

Epic: EP-002 (S1) · Implements: FR-019 · Depends on: TASK-013
Protocol: **live-assisted** (operator plays the client — the sanitization
pass runs at close/pause on a genuinely produced working transcript; replaying
a pre-sanitized script would test nothing)

## Scenario
Client interview salted with PII: third-party full names ("mi contable,
Marta Ruiz…"), phone numbers, an email address, and one health-adjacent
mention. Fictitious identities only — but treated by the pipeline exactly as
real PII would be.

## Deliverables
- `tests/interview-scenarios/06-pii/scenario.md` (operator brief: planted PII
  inventory with expected disposition per item)
- `tests/golden-artifacts/06-pii/golden-checklist.md`
- One executed live sitting; evidence result recorded

## Golden checklist (distinct focus)
- Sanitization at close: third-party names → roles, contact data removed,
  business facts kept **verbatim** — zero paraphrase (R2-03; alias, never
  rewrite)
- Raw/committed split: unredacted original in `evidence-raw/`, sanitized
  transcript committed with front matter `raw_ref` + SHA-256 of the raw file
- Turn numbering identical raw↔sanitized — every `#turn-nnn` anchor resolves
- Planted-PII sweep: every inventory item correctly dispositioned; no PII in
  any committed path (grep-level check)
- Health mention handled as a data-sensitivity signal (M7/M8 + trigger
  consideration), not just redacted
- FR-015-AC-02 evidence lands here; this is RSK-A13's regression anchor

## Primary failure mode guarded
Sanitization defects in both directions: PII leaking into Git history
(privacy/erasure violation) or over-sanitization paraphrasing statements
(evidence distortion).

## Evidence result
`tests/golden-artifacts/06-pii/RESULT.md` (must state the grep sweep command
and its empty result).

## Out of scope
Encrypted evidence platform (post-MVP); consent workflow content (M0 template,
TASK-013).
