# Claude.ai prototypes — historical baseline

> **HISTORICAL PROTOTYPE — NOT ACTIVE RUNTIME — NOT BEHAVIORALLY VALIDATED.**
> Nothing in this directory is loaded by client sessions or by the methodology
> runtime. Active skills live in `.claude/skills/` only. These files predate
> the V2 architecture and have never been exercised under the Claude Code
> runtime this repository targets.

## Provenance

Exported from the operator's Claude.ai project ("Requirements & Delivery OS"),
recovered 2026-07-12 from `~/Documents/HugePlanning-import/`. Preservation
decision: R2-36 (`planning/v2/19_revision_audit_and_change_log.md` §5).
Contents are methodology material only — no client data (verified during the
recovery inspection).

| File | SHA-256 |
|---|---|
| `PROJECT_INSTRUCTIONS.md` | `2f6c7c4ae138aa83c77925d8a43e77b7618b2c61dd9dc202496db46a50c8d372` |
| `archives/artifact-pack-generator.skill` | `a28dff83180de0449dfab21be9333e013871c793fe83f8c2ae924e86620eb4a2` |
| `archives/business-discovery-interviewer.skill` | `d399235b685d71b33ac2a07fbdb2cd8a4393705f20e4e20840fabebcc5705f0e` |
| `archives/change-delta-interviewer.skill` | `4ec6fb9e13d678833b0cc6d30d2ab705ad1ec4184754e1a31c72990d2d64b6f0` |
| `archives/client-meeting-pack-preparer.skill` | `730e583305efcafb256ca79ba9a26c7ba4347ad7b7cac3d4022c6f0ff386e0d4` |
| `archives/documentation-quality-reviewer.skill` | `5b88c9eadaab14d3d45026c256279c18711b2269c4bfc00c26e316ba7dab8b36` |
| `archives/mvp-scope-reducer.skill` | `da0426a00823820f79b42c678c8a722947ec9e35d8869a37b529a86d23fa2703` |
| `archives/technical-ux-interviewer.skill` | `470684e7acd7184bcb40d519ce6a7fb3b231dbb990e87001042d7fb05703e259` |

`archives/` holds the original `.skill` zip packages, byte-identical to the
export. `extracted/` holds their unzipped contents verbatim (for reading and
grepping) — never edit either; corrections to method belong in the V2 plan and
the active runtime, not here.

## Reuse assessment (input to S0b/S1 per the product plan)

Classification: `REUSE` compatible as written · `ADAPT` useful with changes ·
`HARDEN` concept needs persistence/schemas/validation/privacy/tests ·
`SUPERSEDE` replaced by a stronger V2 mechanism · `DISCARD` preserved but not
entering the runtime · `MISSING` required by V2, absent here.

| Prototype component | Class | Where it lands |
|---|---|---|
| Project Instructions §2: progressive small blocks, 1–4 questions, lettered options, progress display, explain-and-return | ADAPT | S1 `adaptive-interview-control` skill + `interview-strategies` knowledge |
| §8 fatigue-handling heuristics | ADAPT | S1 skill (V2 `04` §6 has `fatigue_signals`; behavior ladder comes from here) |
| §4 uncertainty labels (Confirmed/Assumed/…) | SUPERSEDE | V2 statement classification (`04` §3) + status enums; mapping table below |
| §3 source-of-truth ladder | SUPERSEDE | Four-layer precedence (methodology invariant 2) |
| §5 business/technical boundary + `technical_parking_lot` | ADAPT | Boundary in `04` §1; parking-lot *presentation* → S1 skill; storage = open-questions (`type: internal`) / solution-context |
| §9 MVP pragmatism + complexity-multiplier feature list | ADAPT (content reuse) | S1 `scope-and-mvp` knowledge (M10); also S3 architecture knowledge |
| §10 UX philosophy | ADAPT | S3 `ux-design-framework` knowledge |
| §12–13 artifact pack standard + output scaling | SUPERSEDE | `06` artifact architecture + `21` profiles |
| §14 quality-review criteria; documentation-quality-reviewer | SUPERSEDE / ADAPT | `07` §4 five audits at S2; severity calibration + dimension list feed auditor checklists |
| §17 language policy | REUSE | Matches DEC-14 / `project.yaml.language` |
| business-discovery-interviewer: block pacing, playback per module, framing block, short-answer permission | ADAPT | Primary S1 input for skill/knowledge wording |
| — new-vs-improvement path branching | ADAPT | Archetype `migration-or-replatforming` + import mode (`04` §2) |
| — Functional PRD + Business Handoff YAML outputs | SUPERSEDE | Layer-2 registries via `requirements-normalization` (`07` §2); PRD is S2 layer 3. The handoff field list is a review checklist for the S0b `solution-context` schema (expected_volume, primary_device, brand_assets, decision_makers, stakeholder_profile) |
| — evidence anchoring, persistence/resume, sanitization/PII, IDs, statuses, CTR handling, DoD, consent, coverage model | MISSING | Required by V2, absent in the prototypes — the gap S0b/S1 close |
| technical-ux-interviewer (blocks, screen map, functional data model, labeled recommendations) | ADAPT at S3 | `05` design session; `origin: technical_derived` discipline is stronger in V2 |
| artifact-pack-generator (+ readiness check, cross-artifact traceability rules) | SUPERSEDE | `06`/`07` + templates/schemas + `validate.sh`; readiness check ≈ G1; consistency rules feed S2 auditor checks |
| mvp-scope-reducer (scope categories, reduction strategies, dependency check) | ADAPT (content reuse) | S1 `scope-and-mvp` knowledge + S2 backlog-refinement phasing |
| change-delta-interviewer | ADAPT (deferred) | CR workflow (`12` §5) / import-mode gap analysis; post-S8 skill candidate |
| client-meeting-pack-preparer | ADAPT (deferred) | G2/G7 session-preparation aid at S2+; optional |
| The packages as runtime skills | DISCARD | No persistence, evidence, schema, or privacy model; historical only |

## Label mapping (prototype → V2)

| Prototype label | V2 mechanism |
|---|---|
| Confirmed | `confirmed_fact` / requirement with evidence `source_refs` |
| Assumed | `ASM-nnn` register entry, `status: unconfirmed` |
| Needs client validation | `OQ`/`CLAR` (owner: client) or `status: proposed_default` awaiting G2 |
| Technical recommendation | `origin: technical_derived`; decisions → ADR at S3 |
| Open question | `OQ-nnn` in `open-questions.yaml` |
| Deferred | scope flag dispositioned `later` (M10) / `phase` field |
| Risk | `RSK`/`risk_triggers[]` in solution-context (profile input, `21` §3) |
| Technical parking lot | scope flag / `OQ (type: internal)` + solution-context facts |

## What stays historical vs. feeds forward

- **Source material for S0b:** the Business Handoff YAML field inventory
  (solution-context schema review checklist).
- **Source material for S1:** conversational craft (pacing, playback, fatigue,
  explain-and-return, parking-lot phrasing) and the scope/complexity content —
  admissible as secondary source in S1 knowledge files per `17` §E.
- **Belongs to S2/S3 or later:** quality-review dimensions (S2 auditor),
  technical/UX interview craft (S3), change-delta and meeting-pack concepts
  (S8+/CR workflow).
- **Eventually an active skill?** Only through the V2 pipeline: any revived
  behavior must be re-authored against plan `04`/`05`/`14` contracts with
  schemas, evidence discipline, and scenario validation — never by unpacking
  these archives into `.claude/skills/`.

Conflicts with V2 (recorded so nobody "fixes" them backwards): prototypes emit
final documents at interview close (V2 separates evidence → normalization →
generation); prototypes offer unlabeled defaults under fatigue (V2 requires
`proposed_default`/ASM discipline); prototype block numbering is presentation
only (V2 modules M0–M12 govern coverage).
