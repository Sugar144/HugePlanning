# TASK-010 — Ten S1 knowledge files (provisional) + INDEX activation tags

Epic: EP-002 (S1) · Implements: FR-018 · Depends on: TASK-006 (S0b green)

## Goal
The interviewer's knowledge floor exists: ten status-provisional files per the
`17` §K minimum specs, retrievable through `knowledge/INDEX.md`.

## Files
- `knowledge/shared/`: requirements-taxonomy, elicitation-techniques,
  nfr-catalog, evidence-and-uncertainty, glossary
- `knowledge/client-discovery/`: interview-strategies, question-bank,
  process-elicitation, scope-and-mvp, technical-operational-context
- `knowledge/INDEX.md` (rows: id · consult_when · profile/archetype tags ·
  status; removes the "none at S0a" placeholder row)

## Acceptance criteria (verbatim from product/requirements.yaml)
- FR-018-AC-01 (front-matter subset + authoring pattern; 17 §J grep scan clean)
- FR-018-AC-02 (scope-and-mvp imports prototype multipliers/strategies with
  prototype-prefixed source refs)
- FR-018-AC-03 (question-bank: every 04 §5 module, ≥3 seeds/topic, sufficiency
  checks, risk keywords, one leading-form anti-example per module)

## Contract sources
`17` §A–§K (taxonomy, front matter, formats, source policy, activation) ·
`04` §5 (module/topic tree) · preserved prototypes (secondary source, R2-36).

## Validation
Suite green (INDEX/front-matter checks if added); manual §K spot-check per
file; `17` §J item 6 grep: no "must never" policy phrasing inside knowledge/.

## Decision (recorded)
All ten files land in one PR — they are provisional and reviewed as a set.

## Out of scope
Technical-solution and legal knowledge groups (S3 / research-gated per `18`);
external research (RES-01/02 run later; content stays model-generated
provisional).
