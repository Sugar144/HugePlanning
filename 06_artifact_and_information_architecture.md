# 06 — Artifact and Information Architecture

**Purpose:** the complete artifact inventory (producer/consumer/lifecycle), ID grammar, status models, schema definitions for the core structured artifacts, template inventory, and anti-duplication rules.
**Baseline traceability:** B11, B12, B14, B19; deviations DEC-03, DEC-04, DEC-05, DEC-09, DEC-11, DEC-14. **V2:** ownership corrections (R2-04), handoff history (R2-05), test definitions vs execution evidence (R2-07), requirements model v2 — origins, structured NFRs, DAT (R2-10), content inventory (R2-18), evidence split (R2-03).

---

## 1. Artifact inventory (every artifact has a purpose and a consumer)

**Ownership contract (R2-04, refined R2-31):** each canonical artifact has **one owner** (the role/mechanism accountable for its integrity and the only authority for its structure), a defined set of **authorized mutators** (with field-level authority where fields have different masters), **one mutation procedure** per controlled change, and **one approval authority** for controlled transitions. The `Owner` column below names exactly one owner per artifact; **all authorized mutators, field-level authority, mutation procedures, and approval authorities live only in §1a**. **The client never edits repository files:** client input arrives as evidence (email, call, delivered files) and an authorized role incorporates it with an evidence reference.

| Artifact | Layer | Format | Owner | Consumers | Lifecycle owner |
|---|---|---|---|---|---|
| `evidence-raw/**` (gitignored) | 1-raw | any | you (capture) | you only (manual) | retention-controlled, deletable (R2-03) |
| `transcript.md/.jsonl` (sanitized) | 1 | md/jsonl | client-discovery (evidence-capture skill) | auditor, you, future app | append-only |
| `interview-state.json` | 1 | json | client-discovery | resume, completion check | interview |
| `completion-report.md` | 3 | md | client-discovery | you (G1 input) | interview close |
| `evidence/clarifications/` | 1 | md | you (§1a) | all downstream | append-only |
| `evidence/confirmations/` | 1 | md | you (§1a) | gates, audits | append-only |
| `engagement.md` | 2 | md | you | G0, ops | onboarding |
| `requirements.yaml` | 2 | yaml | requirements-normalization skill (§1a) | everything downstream | change control after G2 |
| `solution-context.yaml` | 2 | yaml | discovery | technical design, ops | change control after G2 |
| `open-questions.yaml` | 2 | yaml | specification pipeline (§1a) | gates block on it | rolling |
| `PRD.md` | 3 | md | doc-generator | client (via validation pkg), you | regenerated from layer 2 |
| `validation-package.md` | 3/4 | md | doc-generator | client (G2) | per baseline round |
| `content-inventory.yaml` (V2) | 2 | yaml | client-discovery (§1a) | story DoR (`08`), G4/G7, ops | rolling until release |
| `product-backlog.yaml` | 2 | yaml | **backlog-refinement skill, product mode (R2-04)** | technical design, estimation | superseded by delivery backlog |
| `SDD.md` | 3 | md | technical architect | implementer, reviewers | change control after G3 |
| `ADR-nnn.md` | 2 | md | technical architect | implementer, future you | immutable once accepted (supersede, don't edit) |
| `data-model.md`, `api-contract.yaml` | 2 | md/OpenAPI | technical architect | implementer, contract tests | change control |
| `delivery-backlog.yaml` | 2 | yaml | backlog-refinement skill, delivery mode (§1a) | Jira export, implementation | rolling under change control |
| `jira-map.yaml` | 4 | yaml | export-jira.sh | reconciliation | regenerable |
| `test-strategy.md`, `test-matrix.yaml` (**definitions only, R2-07**) | 2/3 | md/yaml | test-planning | implementation, G6 | rolling |
| `verification/REL-nnn-verification.yaml` (V2) | 2 | yaml | deployment-readiness-review (release-manager) | G6/G8, requirement `verified` derivation, audit | immutable per release (R2-07) |
| `security-checklist.md` | 2 | md | technical architect | risk-specialist (verification), G6/G8 | per release |
| `traceability.yaml` | 2 | yaml | traceability-validation | audits, impact analysis | derived + validated (`08` §6) |
| `docs/handoffs/G<n>-<slug>-<seq>.yaml` | 2 | yaml | **you at each gate, script-assisted (R2-04/05)** | next stage's precondition check, status.sh, audit | **append-only history; no pointer file — current state derived** |
| `task-context/TASK-nnn.md` | 3 | md | task-context-package | implementer, reviewers, future audit/debug | **retained permanently; changes = commits on the task branch (R2-08)** |
| `release manifest REL-nnn.yaml` | 2 | yaml | release-manager | deploy, rollback, audit | immutable |
| `runbook.md`, `monitoring.md` | 3 | md | release-manager | operations | rolling |
| `ops/incidents/INC-nnn.md`, `docs/changes/CR-nnn.md` | 2 | md | you (§1a) | change cycle | per event |
| `project.yaml` | 2 | yaml | scripts (§1a) | every session start | rolling |
| `methodology.lock.yaml` | 2 | yaml | scripts (`new-client.sh`/`upgrade-lock.sh`) | launcher, validate | upgrade-controlled |

Anything not in this table is not an artifact of the system (no files "just in case" — mission anti-pattern).

## 1a. Ownership detail — artifacts with multiple authorized mutators (R2-31)

| Artifact | Owner | Authorized mutators (field-level authority) | Mutation procedure | Approval authority |
|---|---|---|---|---|
| `project.yaml` | scripts (structure) | `new-client.sh`/`upgrade-lock.sh` (creation, lock pointer); any agent (**counters only**, at ID allocation); you (**stage, approvals, profile, config** — only via gate procedures) | Gate procedure / script; free-hand edits prohibited | You at the owning gate |
| `open-questions.yaml` | specification pipeline | Any agent may **append** new OQ/CLAR entries (append is always safe); the stage-owning role sets `answer`/status with an evidence ref; nobody deletes — terminal statuses only | Append freely; answer/close via the owning stage's procedure | You (blocking items: at the gate they block) |
| `content-inventory.yaml` | client-discovery (seed) | client-discovery (seeding); you (**status transitions** when client content arrives, with evidence ref); backlog-refinement (`needed_by` links) | Status change requires the delivery evidence (file/email) recorded first | You; client sign-off for `placeholder_approved` at G7 |
| `evidence/clarifications/`, `evidence/confirmations/` | you | **You only** — client input is transcribed/attached by you; agents read, never write | Append-only; one file per event | — (evidence, not approvals) |
| `docs/changes/CR-nnn.md`, `ops/incidents/INC-nnn.md` | you | Agents may write **draft proposals** (marked `draft`); you create/finalize the record | CR: `12` §5; INC: `12` §3 | You at G9 (CR); you at INC close |
| `requirements.yaml` | requirements-normalization skill | Normalization (pre-approval edits); after `approved`: **change control only** (supersede, never rewrite) | `07` §2 pre-baseline; `12` §5 post-baseline | Client at G2/G9 (scope); you at G1 |
| `delivery-backlog.yaml` | backlog-refinement (delivery mode) | Refinement (content, after CR/baseline changes); task loop (**`status`, `branch`, `jira` fields only**, at defined lifecycle events `08` §4) | Content via refinement; status via task-loop events | You at G4/G5 |

Everything else in §1 has exactly one mutator (its owner) and needs no field-level split.

## 2. Status models

**Documents/artifacts (baseline §11.1 retained):** `draft → under_review → changes_requested → approved` (+ terminal `superseded | deprecated`). Status lives in the artifact (YAML field or md front-matter), never in `project.yaml` (DEC-11).

**Requirements (DEC-05):** `draft → under_review → changes_requested → approved → implemented → verified` (+ `rejected | superseded | deprecated`). `implemented` set when all linked tasks merge; `verified` when all linked tests pass on an integrated build (`10` §4).

**Tasks:** `backlog → ready → in_progress → in_review → changes_requested → approved → merged → verified → done` (+ `blocked`, `cancelled`). Where Jira is used it mirrors a simplified view and owns only the in-flight workflow status, reconciled into Git at PR/batch events (Model B, `08` §4); on LITE projects the field in `delivery-backlog.yaml` is the sole operational status (R2-06).

**Stories (V2, R2-11):** `draft → ready → in_progress → done` — a story is `done` only when all its tasks are `done` **and** its end-to-end AC demonstration passed on an integrated build (`08` §3a); task completion never auto-completes a story.

**Content items (V2, R2-18):** `missing → promised → received → approved` (+ `placeholder_approved`).

**Open questions:** `open → answered → incorporated` (+ `expired`, `withdrawn`). Contradictions: `open → resolved | accepted_as_tension`.

## 3. Front-matter convention (markdown layer-2/3 artifacts)

```yaml
---
id: ADR-003            # when the artifact is an identified item
status: draft
schema_version: 1.0.0  # structured artifacts only
based_on: [FR-004, NFR-005]   # upstream IDs
generated_from: docs/requirements/requirements.yaml@<commit>  # layer-3 docs
language: es           # client-facing docs only (DEC-14)
---
```

## 4. ID grammar (DEC-09)

```text
<TYPE>-<NNN>            zero-padded 3 digits, per-project sequence, never reused,
                        never renumbered. Allocation: project.yaml counters
                        (03 §4), incremented at creation; validate.sh enforces
                        uniqueness and no gaps ahead of counter.
Scoped children:  <PARENT>-AC-<nn>   acceptance criteria
                  <PARENT>-T-<nn>    micro-subtasks inside a task context
```

| Prefix | Meaning | Lives in |
|---|---|---|
| OBJ | Business objective | requirements.yaml |
| FR / NFR / INT / CON / **DAT** | Functional / non-functional / integration / constraint / **data (V2, R2-10)** requirement | requirements.yaml |
| **CNT** | Content/asset item (V2, R2-18) | content-inventory.yaml |
| BR | Business rule | requirements.yaml |
| ASM | Assumption | requirements.yaml (register) |
| OQ / CLAR | Open question / client clarification | open-questions.yaml |
| CTR | Contradiction | open-questions.yaml (register) |
| EP / US / UC | Epic / user story / use case | backlogs |
| TASK / BUG / CR | Task / defect / change request | delivery backlog |
| ADR / SPK / RSK | Decision / spike / risk | architecture docs |
| TEST | Test case (matrix row) | test-matrix.yaml |
| REL / INC | Release / incident | releases, ops |

Jira keys are additive labels, never replacements (baseline §15.1 retained).

**Allocation (V2, R2-10):** counters in `project.yaml` allocate at creation; the MVP assumes a **single writer** (one session at a time); `validate.sh` detects duplicate/colliding IDs; parallel-branch allocation is a documented deferred limitation (`15`) — migration requirements use `category: migration` on FR/DAT/CON rather than a new prefix.

## 5. Anti-duplication and generation rules (closes G-22)

1. Every fact has exactly one authoring home (layer 2). PRD/SDD/validation-package **cite IDs and explain**; they never restate a requirement in new normative words.
2. Layer-3 docs record `generated_from: <file>@<commit>`; `validate.sh` warns when the source has moved ≥ N commits ahead (drift detector).
3. Gate handoff records (`docs/handoffs/`) declare artifact paths + readiness, duplicating nothing (baseline §9.7 retained; append-only per R2-05).
4. Jira content is an export projection; edits to meaning happen in Git and re-export (`08` §5).
5. `traceability.yaml` stores only ID-to-ID links, no text.

## 6. Template inventory (methodology `templates/`)

| Template | Notes |
|---|---|
| `client-repo/` | Whole repo skeleton (`03` §2) |
| `discovery/PRD.template.md` | Sections: context & problem (OBJ refs) · objectives & metrics · users & stakeholders · scope & MVP (FR refs by phase) · exclusions · business rules (BR refs) · risks · open items. Client language |
| `discovery/validation-package.template.md` | Plain-language G2 summary: what we understood, what we'll build first, what's excluded, assumptions to confirm (incl. `proposed_default` NFRs), content list + deadlines, estimate vs budget, questions; per-section confirm checkboxes. **LITE variant: 1-page brief used in the compact G1+G2 validation workflow — distinct gate records retained (R2-19/R2-29)** |
| `discovery/content-inventory.template.yaml` (V2) | §7.6 skeleton with field comments |
| `discovery/clarification-request.template.md` | CLAR email/message shape (`05` §7) |
| `technical/SDD.template.md` | Sections: overview & archetype · architecture & components · data model ref · API ref · UX flows · accessibility implementation · authN/Z & security · privacy · infrastructure & environments · deployment & rollback outline · observability · testing summary (ref) · risks · decision index (ADR refs). **LITE variant: design note (1–2 pages) — stack/hosting, sitemap/page structure, visual direction, applicable floors (`05` §1, `21` §5)** |
| `technical/ADR.template.md` | MADR-style: context, options, decision, consequences, decider, driving REQs, overrides |
| `technical/ux-outline.template.md` (V2) | Sitemap/IA, flows, wireframe descriptions, component & state inventory, visual direction — sectioned by profile depth (`05` §8) |
| `delivery/task-context.template.md` | `09` §3 |
| `delivery/pr-body.template.md` | `11` §4 |
| `delivery/release-manifest.template.yaml` | `11` §7 |
| `delivery/verification-snapshot.template.yaml` (V2) | `10` §4b |
| `delivery/incident-report.template.md`, `change-request.template.md` | `12` |
| YAML templates for every schema'd artifact | Pre-filled skeleton + inline field comments |

## 7. Core schema definitions (normative field sets; full JSON Schemas generated stage-by-stage at first consumer, R2-02)

### 7.1 `requirements.yaml`

```yaml
schema_version: 1.1.0
objectives:
  - id: OBJ-001
    statement: Reducir la gestión manual de reservas.   # client language
    metric: "≥80% de reservas sin intervención manual a los 3 meses"
    source_refs: [interview:client-discovery-01#turn-14]
requirements:
  - id: FR-004
    type: functional            # functional|nonfunctional|integration|constraint|data (R2-10)
    category: booking           # project taxonomy; NFR uses nfr-catalog categories;
                                #   'migration' is a category, not a type
    statement: El visitante puede solicitar una reserva indicando fecha, hora y nº de personas.
    rationale: null
    origin: client_evidence     # client_evidence | stakeholder_preference |
                                #   methodology_default | legal_or_regulatory |
                                #   technical_derived  (R2-10; defaults enter as
                                #   status proposed_default until confirmed)
    status: approved            # lifecycle 06 §2 (+ proposed_default pre-confirmation)
    priority: must              # MoSCoW
    risk: high                  # drives review/test depth
    objectives: [OBJ-001]
    source_refs: [interview:client-discovery-01#turn-24]
    acceptance_criteria:
      - id: FR-004-AC-01
        given: fecha con plazas libres
        when: el visitante envía el formulario
        then: la reserva queda registrada como pendiente y el cliente recibe aviso
    business_rules: [BR-002]
    depends_on: []
    conflicts_with: []
    assumptions: [ASM-002]
    approved_in: null           # MERGE COMMIT of the G2 baseline docs PR on main
                                #   (immutable; same commit in the G2 handoff) (R2-10)
    verification: { tests: [TEST-011, TEST-012] }   # pass/fail lives in the
                                #   release verification snapshot, not here (R2-07)

  - id: NFR-002                 # structured NFR (V2, R2-10) — "fast" is not a requirement
    type: nonfunctional
    category: performance
    statement: Las páginas públicas cargan rápido en móvil.
    metric: LCP
    target: "<= 2.5 s"
    conditions: "4G, gama media, caché fría"
    measurement: { method: "Lighthouse móvil", environment: staging }
    verification_level: pre-release   # matrix row TEST-0xx
    tolerance: "p75"
    origin: methodology_default
    status: approved            # confirmed by client at G2 (was proposed_default)
    client_confirmation: clarification:CLAR-001   # evidence/clarifications/CLAR-001.md
    source_refs: [methodology:nfr-catalog#performance]

  - id: DAT-001                 # data requirement (V2, R2-10)
    type: data
    category: migration
    statement: Las 340 reservas históricas del Excel actual deben importarse sin pérdida.
    origin: client_evidence
    status: approved
    source_refs: [interview:client-discovery-01#turn-52]
    acceptance_criteria:
      - id: DAT-001-AC-01
        given: el Excel actual
        when: se ejecuta la importación
        then: recuento y campos clave coinciden 1:1 con un informe de verificación
business_rules:
  - id: BR-002
    statement: No se aceptan reservas con menos de 12 h de antelación.
    source_refs: [interview:client-discovery-01#turn-31]
    status: approved
assumptions:
  - id: ASM-002
    statement: Una única ubicación física.
    basis: interview:client-discovery-01#turn-9
    status: confirmed           # unconfirmed|confirmed|invalidated
```

### 7.2 `solution-context.yaml` (facts, never decisions — baseline §9.4 retained)

Sections: `domain{provider, ownership, access_status}` · `hosting` · `email` · `existing_systems[]{name, purpose, integration_required, access_status}` · `accounts[]` · `expected_usage{monthly_visitors, peak_events, simultaneous_admins}` · `data{entities_mentioned[], sensitivity, personal_data_types[], retention_expectations}` · `operational{maintainer_after_delivery, content_editors, technical_skill_level}` · `legal_flags[]` · **`risk_triggers[]{trigger, evidence_ref, profile_implication, status}` (V2, R2-24 — machine-readable input to profile confirmation, `21` §4)**. Every leaf: `value | unknown` + `source_refs`.

### 7.3 `open-questions.yaml`

**Always present (R2-30):** the registry is created empty by the client template for **every** profile — agents never face a missing-file branch. The profile changes only its allowed depth and whether unresolved items block gates (`21` §5), never its existence.

```yaml
questions:
  - id: CLAR-002
    type: client_clarification   # internal|client_clarification
    question: ¿Es aceptable un coste mensual de ~9 € por el sistema de reservas?
    context: Decisión de arquitectura ADR-003
    impact: bloquea elección de proveedor de reservas
    blocks: [ADR-003, TASK-014]
    owner: client
    channel: email
    deadline: 2026-09-20
    status: open
    answer: null                # + evidence ref when answered
contradictions:
  - id: CTR-002
    between: [interview:client-discovery-01#turn-12, "#turn-38"]
    topic: scope.mvp
    severity: critical
    status: resolved
    resolution_ref: interview:client-discovery-01#turn-39
```

### 7.4 `delivery-backlog.yaml`

```yaml
epics:
  - id: EP-002
    title: Reservas online
    objective_refs: [OBJ-001]
stories:
  - id: US-014
    epic: EP-002
    title: Solicitud de reserva por el visitante
    implements: [FR-004]
    acceptance_criteria: [FR-004-AC-01, FR-004-AC-02]
    priority: must
    risk: high
    status: ready
stories_note: >   # V2 (R2-11): stories are vertically sliced outcomes (08 §1a);
  phase: (product backlog) and release_target: (stories/tasks) are the only
  V2 field additions — owner/enables/blocked_by/business_value rejected (19)
tasks:
  - id: TASK-031
    story: US-014
    title: Booking request endpoint + validation
    type: feature               # feature|chore|fix|spike|docs
    depends_on: [TASK-029]
    code_areas: [src/booking]   # V2: guides review + worktree disjointness
    tests_required: [unit, integration, a11y]
    estimate: M                 # XS/S/M/L/XL — sizing rule: one reviewable outcome (08 §3)
    release_target: REL-001     # V2 (R2-11)
    status: ready
    jira: null                  # filled by export where Jira is used (WEB-42)
    branch: null                # filled at implementation
```

### 7.5 Gate handoff records (V2, R2-05) — `docs/handoffs/G<n>-<slug>-<seq>.yaml`

Baseline §9.7 content retained inside an append-only per-gate file:

```yaml
schema_version: 2.0.0
gate: G2
sequence: 1
date: 2026-09-19
approved_by: client            # via email; confirmation ref below
result: approved               # approved | approved_with_observations | rejected
commit: 9f1c2d3                # the immutable baseline commit (= approved_in)
confirmation_ref: evidence/confirmations/2026-09-19-g2.md
artifacts: { prd: docs/product/PRD.md, requirements: docs/requirements/requirements.yaml }
quality: { critical_questions_remaining: 0, unresolved_contradictions: 0 }
profile_check: { profile: standard, new_triggers: [] }
# G3 records additionally carry the nested visual checkpoint (01 §4.2b):
# visual_approval: { required: true, confirmed: 2026-09-25,
#                    record: evidence/confirmations/2026-09-25-g3v.md }
next_stage: technical_design
```

No pointer file exists; `status.sh` derives current gate state from the latest sequence per gate.

### 7.6 `content-inventory.yaml` (V2, R2-18)

```yaml
schema_version: 1.0.0
items:
  - id: CNT-007
    item: Fotos de los 8 platos principales
    type: image                # copy|image|logo|video|translation|legal_text|data|metadata
    owner: client
    source: "sesión con fotógrafo prevista"
    license: client-owned      # provenance/usage rights (HIGH-RISK: mandatory)
    needed_by: [US-006]
    deadline: 2026-10-01
    status: promised           # missing|promised|received|approved|placeholder_approved
    fallback: "fotos de stock temporales, aprobadas como placeholder"
```

### 7.7 Others

`interview-state` (`04` §6) · `traceability` (`08` §6) · `test-matrix` — definitions only (`10` §4) · `verification-snapshot` (`10` §4b) · `jira-map` (`08` §5) · `release-manifest` (`11` §7) · `project` (`03` §4) · `methodology-lock` (`02` §7).

## 8. Requirement / story / use-case / BDD usage rule (baseline §10 retained verbatim)

Every functionality: requirement + user story + ACs. Complex flows only: use case + critical BDD scenarios. No Gherkin for trivial detail. ACs written Given/When/Then when behavioural, plain checklist when not (e.g., content or visual criteria).
