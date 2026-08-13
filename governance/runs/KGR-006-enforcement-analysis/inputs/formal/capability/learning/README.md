---
document_id: GOV-LEARNING-CONTRACT-001
version: 0.1.0
status: IMPLEMENTED_LOCALLY_PENDING_PROJECT_OWNER_REVIEW
---

# Governance Failure and Learning Records

This directory is the canonical professional learning surface for material governance failures, near misses, ambiguities, corrections, defects, tooling gaps, and cost waste. Base YAML records and append-only YAML events are source truth. `FAILURE_AND_LESSONS_INDEX.md` is a deterministic generated view.

## Record-class boundaries

| Class | Use | Canonical surface |
|---|---|---|
| Failure and lesson record | Durable causal learning with correction and prevention | `learning/records/` and `learning/events/` |
| Formal run record | Exact run contract, inputs, execution status, outputs, result, and provenance | `governance/runs/` |
| Operational session log | Transient chronology, resume context, and non-material local observations | Approved operational-log surface, not this index |
| Decision record | Explicit competent authority choice and consequences | `governance/DECISION_LOG.md` |
| Security or governance incident | Realized or credible material security, privacy, authority, integrity, or mandatory-gate breach requiring containment or forensic response | Separate incident record; link learning after containment |
| Methodology parking-lot proposal | Prospective improvement without an observed material event | Approved methodology backlog/proposal surface |

Records may link across classes but never replace one another.

## Exact triage

Create a new failure record when a distinct causal chain, severity, owner, containment, acceptance decision, or validation path exists; when authority, provenance, cost, quality, time, or execution risk was materially affected; when the Project Owner corrected a proposed or attempted action; when a control/schema/test/protocol/instruction/model route/workflow may change; or when recurrence must be independently detectable.

Use a subfinding only when it shares the same systemic cause, corrective control, compatible status, and owner, and needs no independent severity, containment, risk acceptance, or validation decision. Preserve its own description and evidence.

Create an incident when a realized or credibly attempted security, privacy, governance-authority, integrity, external-effect, or mandatory-gate violation requires containment, notification, forensic preservation, recovery, or explicit risk acceptance. Incident routing takes precedence; the learning record may follow and link it.

Use an operational log only when the event is transient, non-material, locally corrected, non-recurring, has no control gap or owner correction, and exists solely for session continuity.

Use only a methodology proposal when the item is prospective and no failure, near miss, ambiguity, correction, waste, or defect has been observed. Later evidence requires a linked failure record.

## Evidence, metrics, and duplicate handling

Evidence references are structured. Repository paths are relative; external/local material is labeled as such. Missing conversation evidence uses `availability: NOT_PRESERVED` with a factual paraphrase, never a reconstructed quote. Never invent dates, timestamps, model identity, token usage, monetary cost, elapsed time, or validation.

Metrics distinguish historic baseline data, future measurable fields, and unavailable historical values through `measurement_quality` and `basis`. `null` is required when a value is unavailable.

The tool blocks exact ID and normalized-fingerprint collisions. It warns, but does not auto-merge, when component, systemic cause, and evidence overlap. Semantic merge, incident classification, and owner decisions remain human responsibilities.

## Status, immutability, and events

Allowed transitions are:

```text
OPEN -> CONTAINED -> CORRECTED -> VALIDATED
OPEN|CONTAINED|CORRECTED -> ACCEPTED_RISK
ACCEPTED_RISK -> OPEN
```

After `VALIDATED`, the base record is immutable. All later status transitions, recurrence, correction, new evidence, risk acceptance, risk expiry/reopening, supersession, owner decision, and validation evidence use numbered append-only files at `events/<record-id>/<record-id>-E###.yaml`. Effective status is derived by replay. Accepted risk requires competent owner evidence, bounded scope, residual impact, review date or rationale, triggers, and continuing controls. Tooling never decides risk acceptance.

Use `python3 governance/tools/manage_learning.py --help` for the dry-run-first CLI. Automatic category summarization is deferred to v0.2.
