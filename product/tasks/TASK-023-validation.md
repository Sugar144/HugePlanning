# TASK-023 — validation evidence (bounded M6→M9 re-hydration replay)

Primary acceptance proof for the bounded fresh-context segmentation correction
(FR-015). Deterministic seam gate + a live, bounded model-assisted replay over
the **recorded** Scenario 05 evidence. The historical Scenario 05 `RESULT.md`,
golden artifacts, and the original scratch client are **unchanged / byte-identical**.

## Prospective record (context-metric correction)

- Scenario 05's `115,594` was the **final-turn context footprint** of one
  continuous subagent (last recorded iteration: `2 + 3876 + 108307 + 3409 =
  115,594`), **not** output tokens.
- **Measured cumulative output was `58,295`.**
- The historical Scenario 05 `RESULT.md` **remains unchanged**; correcting the
  "output tokens" phrasing in that approved record is a separate change-control
  act, not done here.

## Method

- Seed: a faithful **paused-at-M6/M7-boundary** snapshot (turns 1–46) built by
  deterministically pruning the recorded Scenario 05 final state to anchors ≤ 46
  and copying transcript turns 1–46 into a **local-only** validation client
  (`/home/sugar/tmp/s05-seam-replay`; not committed — client-data-separation).
  The seed passes the existing replay checker (`interview-replay-check.py`:
  `turns=46 state_bytes=6875 anchors=19`), i.e. it is an internally consistent
  pause snapshot. The M6/M7 boundary is the real pause recorded in Scenario 05.
- Two **fresh** `client-discovery` segments were then run, each re-hydrated
  **only** from `interview-state.json` + a bounded last-transcript window (6
  turns) + current-module persona facts + the segment objective — never the full
  transcript, never the prior segment's internal history. Segment 2 is a
  distinct fresh context with no memory of segment 1.

## Before / after (observable runtime metrics)

| Metric | BEFORE — Scenario 05 (1 continuous subagent) | AFTER — seg 1 (M7) | AFTER — seg 2 (M8–M9) |
|---|---|---|---|
| Fresh interviewer contexts | 1 | 1 (fresh) | 1 (fresh) |
| Initial context footprint | 17.8k | **18,169** | **18,262** |
| Peak context footprint | **112,185** | **49,640** | **56,856** |
| Agent `totalTokens` (final-turn footprint) | 115,594 | 50,746 | 58,163 |
| Tool uses | 28 | 8 | 9 |
| Persisted turns produced | 88 | 6 (47–52) | 18 (53–70) |
| Transcript window re-hydrated | n/a (whole context accumulated) | 6 turns | 6 turns |

**The decisive observation:** segment 2 started fresh at **18,262** tokens — it
did **not** inherit segment 1's ~50k context. Each segment reset to the ~18k
baseline (system prompt + agent def + skills + bounded re-hydration) and peaked
at roughly **half** the continuous run's 112,185. The context boundary is real,
not narrative.

**No total-token-saving claim is made:** the runtime exposes `totalTokens` as a
*final-turn footprint*, not a cumulative-cost figure, so the before/after totals
are not directly comparable. What is reported is what is observable — per-segment
initial/peak footprint and the fresh-context reset at each seam.

## Demonstrables (all met)

- **> 1 fresh segment:** 2 live fresh segments (+ the seed pause = 3 bounded
  segments in the seam package). ✓
- **No dependency on full prior context:** seg 2 initial footprint 18,262 (fresh). ✓
- **Bounded re-hydration:** 6-turn window vs 46/52 turns of prior transcript. ✓
- **Adaptive next-question, no fixed questionnaire:** seg 1 queued M8 by
  consequence (`q-053`); seg 2 queued M10 scope (`q-071`) — chosen from state. ✓
- **Cross-boundary playback correct:** both segments restated the proposed
  upgrade naming **high-risk** and citing both triggers, as an operator G1
  proposal. ✓
- **Turn IDs continuous/unique:** transcript is `1..70` contiguous. ✓
- **source_refs valid:** `interview-replay-check.py` on the produced final state
  → PASS (`turns=70 anchors=28`, 0 dangling, bounded resume). ✓
- **Trigger/escalation preserved:** both `risk_triggers[]` retained in
  `solution-context.yaml` (turn-024 `high-risk`, turn-030 `standard`, both
  `status: proposed`); the "¿me lo subís a alta seguridad y ya?" lure declined;
  `project.yaml.profile` untouched (`lite`). ✓
- **No S2/S3 leakage:** seam checker + replay checker `no-leakage` both clean. ✓
- **Historical evidence byte-identical:** original scratch client git status
  empty; `tests/golden-artifacts/05-*` and Scenario 05 `RESULT.md` absent from
  the diff. ✓

## Deterministic gates run

- `tests/lib/interview-segment-seam-check.py` (new, T21): 1 valid + 6 invalid
  fixtures — each invalid fails with its exact expected token. PASS.
- Seam checker on the **live** 3-segment package: `INTERVIEW-SEAM: PASS —
  segments=3 total_turns=70 max_window=6 registers=8 coverage_nodes=19`.
- `tests/lib/interview-replay-check.py` (existing, T20) on the produced final
  state: PASS.
- Full harness `tests/run-tests.sh`: **257 passed, 0 failed** (was 248 pre-fix:
  +9 from T21). Methodology tree left unchanged by the suite (T13).

## What remains unmeasured

- No cumulative-token comparison (runtime exposes only the final-turn footprint).
- The replay covered M6→M9 (~24 turns across 2 segments), not all 88; per the
  authorization, a full 88-turn rerun was not performed.
- Import-mode simulation still has the model voice persona answers; a
  live-assisted interview would not pay that output. No efficiency budget/target
  yet exists to judge "acceptable" against.
