# S0a–S1 Honest Adoption Plan

Status: `PLAN_ONLY`
Current compliance determination: `NOT_PERFORMED`

This document defines a future audit and adoption workflow. It does not audit S0a or S1, project the proposed Kernel into runtime, or claim present compliance.

## Preconditions

- A Kernel version has been adversarially closed and humanly ratified.
- Minimum derived policies, criteria, and executable controls needed for assessment exist.
- Assessment scope, evidence sufficiency, evaluator independence, and decision authority are explicit.
- S1 work may continue independently until a separately authorized adoption task begins.

## Allowed classifications

| Classification | Meaning for the future assessment |
|---|---|
| `COMPLIANT` | Real evidence supports all applicable assessed requirements. |
| `PARTIALLY_COMPLIANT` | Some applicable requirements are evidenced; bounded gaps remain. |
| `NON_COMPLIANT` | Evidence shows an applicable requirement is not met. |
| `UNVERIFIABLE` | Available evidence cannot establish the historical or current claim. |
| `NOT_APPLICABLE` | The requirement does not apply, with recorded rationale. |
| `REQUIRES_MIGRATION` | Existing state must be converted or superseded before adoption. |
| `TEMPORARILY_EXEMPT` | Competent authority records scope, rationale, risk, controls, and expiry/review. |

## Future workflow

1. Inventory actual S0a–S1 artifacts, commits, decisions, task contracts, validations, releases, reports, and relevant external evidence without modifying them.
2. Reconstruct the contracts and intent that actually governed each historical action. Keep later expectations distinct from historical requirements.
3. Identify evidence that really exists. Link to canonical records; do not manufacture transcripts, approvals, independence, or checks that did not occur.
4. Run pending validation that is safe, authorized, and still meaningful. Label new validation by its real execution date rather than presenting it as historical.
5. Build an assessment matrix against the ratified Kernel and minimum governance package, including applicability, claim, evidence, evaluator, limitations, and classification.
6. Classify each item using only the allowed classifications above. `UNVERIFIABLE` is an honest result, not an automatic failure or pass.
7. Prioritize material gaps by cumulative effect, criticality, propagation, and impact on S2 inheritance.
8. Remediate proportionally through an explicit task contract. Prefer the smallest change that restores the required protection and preserve superseded state/history.
9. Route exceptions and residual risks to competent authority with scope, controls, owner, and review/expiry conditions.
10. Produce an adoption decision for each assessed surface and a bounded readiness decision for S2.

## Required future records

- Scope and frozen assessment criteria.
- Historical-contract reconstruction with sources and uncertainty.
- Artifact/evidence inventory.
- Requirement-by-requirement assessment matrix.
- New validation records distinguished from historical evidence.
- Gap and remediation register.
- Exception/residual-risk records.
- Independent evaluation and owner adoption decision.

## Guardrails

- Do not rewrite old artifacts merely to appear compliant.
- Do not infer approval from file existence, merge, release, or absence of a reported failure.
- Do not claim S0a or S1 compliance now.
- Do not require full reimplementation when a narrower evidence-based remedy is sufficient.
- Do not begin runtime changes from this plan; a later task must authorize exact paths and effects.
