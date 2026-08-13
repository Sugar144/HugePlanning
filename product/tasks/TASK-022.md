# TASK-022 — Compact interview working state + deterministic resume/replay validation

Epic: EP-002 (S1) · Implements: FR-015 · Depends on: TASK-011

## Why

Scenario 03 (non-technical) cost far more than the other S1 scenarios
(~50 persisted turns, 2 sittings, ~218k context tokens reported by the
operator). Deterministic inspection of the three recorded interviews found the
recurring driver: `interview-state.json` is rewritten **in full** at every
module transition / register entry / 10 turns / pause (04 §6), yet ~43–53% of
that file is verbose per-node narrative in `coverage[].notes` (individual notes
up to ~2KB), while the cheap LITE scenario kept notes terse (max ~365B). The
working state (which changes every turn) is coupled to the consolidated
discovery record (which grows monotonically), so full-file checkpoints amplify
write cost with interview length. There was also no deterministic test guarding
bounded resume or state compactness.

This is a refinement of how the **existing** FR-015 persistence contract is
realized — not a new requirement, not a schema change, not a boundary change
(S1 still only collects and structures evidence). The ~218k token figure is
operator-reported and unmeasurable from artifacts; it is not restated as fact.

## Scope (bounded)

1. Working state stays compact: `coverage[].notes` and `resume_hints` are
   compact working annotations (open gap + pending probe + anchor ids). The
   verbatim record is the transcript; the consolidated per-topic narrative is
   the close-time completion-report. (SKILL text in
   `adaptive-interview-control`, `interview-evidence-capture`; template
   comments in `interview-state.template.yaml`.)
2. Deterministic replay/resume validation added to the existing harness (bash +
   plain Python + jsonschema; **no pytest, no Hypothesis, no new dependency**):
   `tests/lib/interview-replay-check.py` + `tests/interview-replay/` fixtures,
   driven by `tests/run-tests.sh` (T20).
3. Lightweight run metrics recorded in the completion-report
   (`completion-report.template.md`): turns, sittings, resumptions, final state
   size, playbacks, operator relays — observability only, never an estimated
   token count.

## Deliverables

- SKILL edits: `.claude/skills/adaptive-interview-control/SKILL.md`,
  `.claude/skills/interview-evidence-capture/SKILL.md`.
- Template edits: `templates/discovery/interview-state.template.yaml`
  (comment-only), `templates/discovery/completion-report.template.md`.
- `tests/lib/interview-replay-check.py`; `tests/interview-replay/valid-*` and
  `invalid-*` fixtures (fictitious client only); `tests/run-tests.sh` T20 +
  a structural leakage guarantee that the interview-state schema cannot carry
  S2/S3 output fields.

## Acceptance (all under FR-015)

- Resume does not require the complete transcript: state + a bounded recent
  transcript window is sufficient to choose the next question (FR-015-AC-01).
- Every persisted `source_refs` / `#turn-nnn` anchor resolves — no dangling
  references (FR-015-AC-03; traceability rule).
- Working-state notes stay within the compact ceiling; the consolidated
  narrative is not accumulated per-checkpoint.
- No fixed questionnaire introduced; adaptive next-question control preserved.
- No S1 → PRD/technical-design leakage (structural + fixture checks).
- No behavioural golden weakened; the 3/6 executed-scenario count is unchanged.

## Out of scope

- Any `interview-state.schema.json` version bump (locked at 1.0.0; a `notes`
  `maxLength` would force a client re-lock + CHANGELOG migration).
- Transcript-turn-convention standardisation (deferred).
- Any dedicated LLM-evaluation framework (rejected: the gap is deterministic and
  fully served by the existing harness; the behavioural gate stays with the
  golden + RESULT + operator review, TASK-015).
- Executing Scenario 02/05/06; reopening closed interviews; changing RESULT
  files, VERSION, or governance.
