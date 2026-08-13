# TASK-023 — Bounded fresh-context interview segments (context-amplification fix)

Epic: EP-002 (S1) · Implements: FR-015 · Depends on: TASK-022

## Why

Scenario 05 (`05-trigger-escalation`, TASK-020) passed its functional golden
but left runtime cost uncertified. Deterministic inspection of the recorded
Claude Code session metadata (the interview subagent sidechain
`…/07125e43-…/subagents/agent-a1d1867a07ea486d1.jsonl`) found the driver:

- The interview ran as **one continuous subagent execution** (~14.6 min real
  wall-clock; `totalDurationMs 875596`) whose context grew **monotonically from
  ~17.8k to ~112.2k tokens with zero resets** and no compaction (peak < 200k).
- **28 tool uses** (Read×20, Write×7, Edit×1). The 20 Reads pulled ~74.5k chars
  of reference material into a context that was never evicted; every later turn
  re-read all earlier content (cumulative cache-read ≈ 2.98M, cache-creation
  ≈ 533k, output = 58,295).
- The `115,594` figure recorded in the Scenario 05 `RESULT.md` is the
  **final-turn context footprint** — arithmetic on the last recorded iteration:
  `input 2 + cache_creation 3876 + cache_read 108307 + output 3409 = 115,594` —
  **not** output tokens. **Measured cumulative output was 58,295.** The
  historical Scenario 05 `RESULT.md` **remains unchanged** (any correction to
  that approved evidence record is a separate change-control act).

TASK-022 fixed *write-amplification* (per-checkpoint state-file cost) and proved
bounded resume holds (replay checker: 264 bounded-resume cases, 0
`WINDOW-NOT-BOUNDED`). It never addressed *aggregate* session context cost,
because the already-contracted bounded-resume path was used only across the two
narrated sittings — the subagent was in fact one continuous instance that never
reset context.

This is a refinement of how the **existing** FR-015 persistence/resume contract
is realized (FR-015-AC-01 already requires "resume from state plus last
transcript page only … without re-reading the whole transcript"). It is **not**
a new requirement, **not** a schema change, **not** a boundary change (S1 still
only collects and structures evidence).

## Scope (bounded)

1. The interview runs as **bounded fresh interviewer segments** (one module or
   small module batch, or one sitting), not one continuously accumulating
   context. At each segment boundary the agent completes the module playback,
   checkpoints compact state + transcript page, and **returns control to the
   orchestrator**; the next segment starts a fresh `client-discovery` context
   re-hydrated **only** from `interview-state.json` + the bounded last
   transcript window + directly relevant current-module evidence + the segment
   objective. The prior segment's full internal history is never carried
   forward. (Contract text: `.claude/agents/client-discovery.md`;
   `.claude/skills/interview-evidence-capture/SKILL.md` — segment boundary;
   `.claude/skills/adaptive-interview-control/SKILL.md` — module close.)
2. A deterministic **seam checker** guards the segmentation invariants across a
   multi-segment run (bash + plain Python + PyYAML; **no pytest, no new
   dependency**): `tests/lib/interview-segment-seam-check.py` +
   `tests/interview-segment/` fixtures, driven by `tests/run-tests.sh` (T21).
3. Segment observability in the completion-report
   (`templates/discovery/completion-report.template.md`): segment count and
   per-segment context footprint / transcript-window size when the runtime
   exposes it — observability only, never an estimated token count.

## Deliverables

- Contract edits: `.claude/agents/client-discovery.md`,
  `.claude/skills/interview-evidence-capture/SKILL.md`,
  `.claude/skills/adaptive-interview-control/SKILL.md`; plan-of-record note in
  `planning/v2/04_client_discovery_interviewer_system.md` §6.
- Template edit: `templates/discovery/completion-report.template.md`.
- `tests/lib/interview-segment-seam-check.py`;
  `tests/interview-segment/valid-*` and `invalid-*` fixtures (fictitious client
  only); `tests/run-tests.sh` T21.
- Validation evidence: bounded M6→M9 re-hydration replay metrics
  (`product/tasks/TASK-023-validation.md`) — local-only replay, no client data
  committed.

## Acceptance (all under FR-015)

- More than one fresh interviewer segment is used; no segment depends on the
  full prior subagent context (FR-015-AC-01).
- Re-hydration uses the compact state + a bounded transcript window only — never
  the whole transcript (FR-015-AC-01).
- Turn IDs stay strictly monotonic and unique across seams; every persisted
  `source_refs` / `#turn-nnn` anchor resolves across segments — no dangling
  references (FR-015-AC-03; traceability rule).
- Adaptive next-question selection, cross-boundary playback, contradiction
  handling, and trigger/escalation behaviour are preserved.
- No fixed questionnaire introduced.
- No S1 → PRD/technical-design leakage (seam checker `no-leakage`).
- No behavioural golden weakened; the 4/6 executed-scenario count is unchanged;
  historical Scenario 05 evidence byte-identical.

## Out of scope

- Any `interview-state.schema.json` version bump (locked 1.0.0).
- Rerunning the complete 88-turn Scenario 05 interview; executing Scenario 02 or
  06; modifying Scenario 05 `RESULT.md`, VERSION, or governance.
- The optional transcript single-authorship-plus-deterministic-mirror adjunct
  (`transcript.md ⇄ transcript.jsonl` renderer) — a separate, smaller output-cost
  refinement; deferred, not implemented here.
- Any dedicated LLM-evaluation framework (rejected: the seam gap is deterministic
  and served by the existing harness; the behavioural gate stays with the golden
  + RESULT + operator review, TASK-015).
