# TASK-011 — Skills: interview-evidence-capture + adaptive-interview-control

Epic: EP-002 (S1) · Implements: FR-014, FR-015 · Depends on: TASK-010

## Goal
The interviewer's two core procedures exist as skills: the per-turn control
loop (with the prototype-adapted conversational craft) and the evidence/
persistence/sanitization contract.

## Files
- `.claude/skills/adaptive-interview-control/SKILL.md`
- `.claude/skills/interview-evidence-capture/SKILL.md`
  (+ `references/` subfiles where a section exceeds skill-body weight, e.g.
  the sanitization procedure checklist)

## Acceptance criteria (verbatim)
- FR-014-AC-01/02/03 (one question per turn; playback + confirmation; interrupt
  re-scoring; fatigue ladder with ASM-recorded defaults; module-boundary
  progress, no fixed block counts)
- FR-015-AC-01/02/03 (mid-M7 pause/resume from state only; PII sanitization
  with identical turn numbering + raw_ref/SHA-256; every candidate anchored)

## Contract sources
`04` §6/§7/§8 (state, control loop, evidence rules) · `02` §4.4 (SKILL.md
structure: purpose/trigger/preconditions/procedure/self-checks/must-not) ·
prototypes: business-discovery-interviewer core behavior, PROJECT_INSTRUCTIONS
§2/§8 (R2-36 — adapt phrasing, keep V2 discipline).

## Validation
Deterministic: skill files load (SPK-01 check b class); suite green.
Behavioural: exercised by the six scenarios (TASK-014/015) — these skills'
ACs are scenario-verified, not file-reviewed.

## Out of scope
Requirements-normalization (S2 pipeline skill, `07` §2); any layer-3 output.
