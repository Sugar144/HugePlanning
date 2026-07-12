# TASK-012 — Skills: nfr-elicitation + process-elicitation

Epic: EP-002 (S1) · Implements: FR-016, FR-017 · Depends on: TASK-010

## Goal
The two topic-specialist procedures exist: M8 quality-expectation elicitation
with measurable anchors, and M4/M5 process reconstruction with exception
hunting.

## Files
- `.claude/skills/nfr-elicitation/SKILL.md`
- `.claude/skills/process-elicitation/SKILL.md`

## Acceptance criteria (verbatim)
- FR-016-AC-01 (consequence-framed probes, vague→measurable concretization or
  explicit low-precision record)
- FR-016-AC-02 (floor NFRs as methodology-default proposals, R2-10)
- FR-017-AC-01 (missing exception paths block topic sufficiency)

## Contract sources
`04` §4 (sufficiency), `04` §5 (M4/M5/M8) · `07` §3 (NFR floor semantics) ·
knowledge: nfr-catalog, process-elicitation (TASK-010).

## Validation
Scenario-verified (clear + non-technical scenarios exercise both; LITE
exercises the M8 floor-confirmation variant).

## Out of scope
NFR normalization into requirements.yaml (S2); profile floor enforcement
(validate.sh, done at S0b).
