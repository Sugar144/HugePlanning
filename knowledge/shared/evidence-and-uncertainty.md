---
id: kn-evidence-and-uncertainty
title: Evidence anchoring, confidence, and the inference/fact boundary
type: concept
status: provisional
version: 0.1.0
language: en
source_quality: model-generated
reviewed_at: null
review_due: null
consult_when: "unsure how to anchor a record, which confidence to assign, whether something is inference or fact, or why sanitization works the way it does"
do_not_use_for: "the sanitization procedure itself (interview-evidence-capture skill owns the steps)"
used_by: [client-discovery, requirements-auditor, requirements-normalization]
related: [kn-requirements-taxonomy, kn-glossary]
supersedes: null
---

# Evidence and uncertainty

## Purpose

The concepts behind the evidence discipline: why anchors exist, how
confidence is expressed, where the inference/fact boundary runs, and the
rationale for the raw/sanitized split — so agents apply the rules with
judgment instead of cargo-culting them.

## Core concepts

**Anchors.** Every recorded fact points at the exact turn that produced it
(`interview:client-discovery-01#turn-24`). The anchor is what makes a record
auditable: anyone can read the turn and judge whether the record is faithful.
A record whose anchor doesn't resolve is indistinguishable from an invention —
which is why unanchored candidates can't leave `draft`.

**Confidence is represented, not smoothed.** Uncertainty lives in explicit
fields (coverage `confidence`, assumption `status`, `precision: low`) rather
than in hedged prose. Prose hedges ("probably", "seems") disappear when text
is summarized; fields survive.

**Inference vs fact.** A fact was stated; an inference was derived. The
boundary test: *could you quote the turn?* If reproducing the claim requires
combining turns or adding world-knowledge, it is an inference and stays one
until the client confirms it in a new turn. Derivations are useful — they
drive good follow-up questions — they just aren't evidence.

**Corrections append.** When the client corrects themselves, the correction
is a new turn superseding the old one; the old turn stays. History that can
be edited can't be trusted; history that only grows can.

**The state file is the memory.** Under long-interview context pressure, the
registers and coverage in `interview-state.json` outrank the model's
recollection of the conversation. Trusting "what I remember the client said"
over the recorded anchors is how drift starts.

**Why raw/sanitized (R2-03).** Git cannot truly delete, and privacy law
requires erasure to be possible. So raw sensitive material stays out of Git
(`evidence-raw/`, local only) and the committed transcript is sanitized —
with *identical turn numbering*, so every anchor still resolves, and a
SHA-256 link to its raw counterpart, so integrity is checkable. Sanitization
removes or aliases identifiers only; paraphrase is off the table because a
reworded statement is new evidence nobody gave.

## Examples

1. Client (turn 31): "no aceptamos reservas con menos de 12 horas". Record:
   BR candidate, anchor `#turn-31`, confidence high — quotable directly.
2. Client mentions a gestor handling invoices (turn 40) and later says "todo
   lo llevamos nosotros" (turn 55). Neither statement is discarded: CTR
   registered with both anchors; resolution will be a new turn.
3. The client's tone suggests the budget is tight but no figure was given.
   "Budget is tight" is an inference; the honest record is the M10 budget
   topic staying `partial`, confidence low, with a queued direct question.
4. Transcript says "mi contable, Marta Ruiz, usa el Excel". Sanitized turn:
   "mi contable, [contable], usa el Excel" — same turn number, business fact
   intact, identifier aliased to the role; raw original in `evidence-raw/`.

## Failure modes

- Anchor rot: reorganizing or renumbering evidence files silently breaks
  every downstream `source_refs` — the append-only rule exists for this.
- Confidence laundering: copying a low-confidence fact into a document
  without its qualifier, where it reads as established.
- Paraphrase-as-sanitization: "cleaning up" client wording changes meaning;
  aliasing identifiers is the entire licensed operation.
- Memory over registers: answering "did we cover X?" from recollection
  instead of the coverage table.

## Limitations

Model-generated, provisional; conceptual content, low volatility. The legal
grounding of the erasure rationale belongs to the legal/ files (research-
gated), not here.

## References

- Plan `04` §6/§8 (state and capture rules), `03` §6 (privacy design),
  `19` R2-03; evidence-policy rule (the normative statement).

## Related

[[kn-requirements-taxonomy]] (what each record type claims) ·
[[kn-glossary]].
