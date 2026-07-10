# 06 — Artifact and Information Architecture

**Purpose:** the complete artifact inventory (producer/consumer/lifecycle), ID grammar, status models, schema definitions for the core structured artifacts, template inventory, and anti-duplication rules.
**Baseline traceability:** B11, B12, B14, B19; deviations DEC-03, DEC-04, DEC-05, DEC-09, DEC-11, DEC-14.

---

## 1. Artifact inventory (every artifact has a purpose and a consumer)

| Artifact | Layer | Format | Producer | Consumers | Lifecycle owner |
|---|---|---|---|---|---|
| `transcript.md/.jsonl` | 1 | md/jsonl | client-discovery | auditor, you, future app | append-only |
| `interview-state.json` | 1 | json | client-discovery | resume, completion check | interview |
| `completion-report.md` | 3 | md | client-discovery | you (G1 input) | interview close |
| `evidence/clarifications/` | 1 | md | you + agents | all downstream | append-only |
| `evidence/confirmations/` | 1 | md | you | gates, audits | append-only |
| `engagement.md` | 2 | md | you | G0, ops | onboarding |
| `requirements.yaml` | 2 | yaml | discovery→normalization | everything downstream | change control after G2 |
| `solution-context.yaml` | 2 | yaml | discovery | technical design, ops | change control after G2 |
| `open-questions.yaml` | 2 | yaml | any agent | gates block on it | rolling |
| `PRD.md` | 3 | md | doc-generator | client (via validation pkg), you | regenerated from layer 2 |
| `validation-package.md` | 3/4 | md | doc-generator | client (G2) | per baseline round |
| `product-backlog.yaml` | 2 | yaml | doc-generator | technical design | superseded by delivery backlog |
| `SDD.md` | 3 | md | technical architect | implementer, reviewers | change control after G3 |
| `ADR-nnn.md` | 2 | md | technical architect | implementer, future you | immutable once accepted (supersede, don't edit) |
| `data-model.md`, `api-contract.yaml` | 2 | md/OpenAPI | technical architect | implementer, contract tests | change control |
| `delivery-backlog.yaml` | 2 | yaml | backlog-refinement | Jira export, implementation | rolling under change control |
| `jira-map.yaml` | 4 | yaml | export-jira.sh | reconciliation | regenerable |
| `test-strategy.md`, `test-matrix.yaml` | 2/3 | md/yaml | test-planning | implementation, G6 | rolling |
| `security-checklist.md` | 2 | md | technical architect (instantiates), risk-specialist (verifies) | G6/G8 | per release |
| `traceability.yaml` | 2 | yaml | traceability-validation | audits, impact analysis | derived + validated (`08` §6) |
| `handoff.yaml` | 2 | yaml | stage-closing agent | next stage's precondition check | per stage transition |
| `task-context/TASK-nnn.md` | 3 | md | task-context-package | implementer | disposable after merge |
| `release manifest REL-nnn.yaml` | 2 | yaml | release-manager | deploy, rollback, audit | immutable |
| `runbook.md`, `monitoring.md` | 3 | md | release-manager | operations | rolling |
| `ops/incidents/INC-nnn.md`, `docs/changes/CR-nnn.md` | 2 | md | you + agents | change cycle | per event |
| `project.yaml` | 2 | yaml | scripts + you | every session start | rolling |
| `methodology.lock.yaml` | 2 | yaml | new-client/upgrade-lock | launcher, validate | upgrade-controlled |

Anything not in this table is not an artifact of the system (no files "just in case" — mission anti-pattern).

## 2. Status models

**Documents/artifacts (baseline §11.1 retained):** `draft → under_review → changes_requested → approved` (+ terminal `superseded | deprecated`). Status lives in the artifact (YAML field or md front-matter), never in `project.yaml` (DEC-11).

**Requirements (DEC-05):** `draft → under_review → changes_requested → approved → implemented → verified` (+ `rejected | superseded | deprecated`). `implemented` set when all linked tasks merge; `verified` when all linked tests pass on an integrated build (`10` §4).

**Tasks:** `backlog → ready → in_progress → in_review → changes_requested → approved → merged → verified → done` (+ `blocked`, `cancelled`). Jira mirrors a simplified view (`08` §5).

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
| FR / NFR / INT / CON | Functional / non-functional / integration / constraint requirement | requirements.yaml |
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

## 5. Anti-duplication and generation rules (closes G-22)

1. Every fact has exactly one authoring home (layer 2). PRD/SDD/validation-package **cite IDs and explain**; they never restate a requirement in new normative words.
2. Layer-3 docs record `generated_from: <file>@<commit>`; `validate.sh` warns when the source has moved ≥ N commits ahead (drift detector).
3. `handoff.yaml` declares artifact paths + readiness, duplicating nothing (baseline §9.7 retained).
4. Jira content is an export projection; edits to meaning happen in Git and re-export (`08` §5).
5. `traceability.yaml` stores only ID-to-ID links, no text.

## 6. Template inventory (methodology `templates/`)

| Template | Notes |
|---|---|
| `client-repo/` | Whole repo skeleton (`03` §2) |
| `discovery/PRD.template.md` | Sections: context & problem (OBJ refs) · objectives & metrics · users & stakeholders · scope & MVP (FR refs by phase) · exclusions · business rules (BR refs) · risks · open items. Client language |
| `discovery/validation-package.template.md` | Plain-language G2 summary: what we understood, what we'll build first, what's excluded, assumptions to confirm, estimate vs budget, questions; per-section confirm checkboxes |
| `discovery/clarification-request.template.md` | CLAR email/message shape (`05` §7) |
| `technical/SDD.template.md` | Sections: overview & archetype · architecture & components · data model ref · API ref · UX flows · accessibility implementation · authN/Z & security · privacy · infrastructure & environments · deployment & rollback outline · observability · testing summary (ref) · risks · decision index (ADR refs) |
| `technical/ADR.template.md` | MADR-style: context, options, decision, consequences, decider, driving REQs, overrides |
| `delivery/task-context.template.md` | `09` §3 |
| `delivery/pr-body.template.md` | `11` §4 |
| `delivery/release-manifest.template.yaml` | `11` §7 |
| `delivery/incident-report.template.md`, `change-request.template.md` | `12` |
| YAML templates for every schema'd artifact | Pre-filled skeleton + inline field comments |

## 7. Core schema definitions (normative field sets; full JSON Schema written at Stage 0 from these)

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
    type: functional            # functional|nonfunctional|integration|constraint
    category: booking           # project taxonomy; NFR uses nfr-catalog categories
    statement: El visitante puede solicitar una reserva indicando fecha, hora y nº de personas.
    rationale: null
    status: approved            # lifecycle 06 §2
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
    approved_in: null           # commit of G2 baseline once approved
    verification: { tests: [TEST-011, TEST-012], status: pending }
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

Sections: `domain{provider, ownership, access_status}` · `hosting` · `email` · `existing_systems[]{name, purpose, integration_required, access_status}` · `accounts[]` · `expected_usage{monthly_visitors, peak_events, simultaneous_admins}` · `data{entities_mentioned[], sensitivity, personal_data_types[], retention_expectations}` · `operational{maintainer_after_delivery, content_editors, technical_skill_level}` · `legal_flags[]`. Every leaf: `value | unknown` + `source_refs`.

### 7.3 `open-questions.yaml`

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
tasks:
  - id: TASK-031
    story: US-014
    title: Booking request endpoint + validation
    type: feature               # feature|chore|fix|spike|docs
    depends_on: [TASK-029]
    tests_required: [unit, integration, a11y]
    estimate: M                 # XS/S/M/L/XL
    status: ready
    jira: null                  # filled by export (WEB-42)
    branch: null                # filled at implementation
```

### 7.5 `handoff.yaml` — baseline §9.7 example retained as-is, plus `schema_version`, `gate`, `approved_by`, `commit`.

### 7.6 Others

`interview-state` (`04` §6) · `traceability` (`08` §6) · `test-matrix` (`10` §4) · `jira-map` (`08` §5) · `release-manifest` (`11` §7) · `project` (`03` §4) · `methodology-lock` (`02` §7).

## 8. Requirement / story / use-case / BDD usage rule (baseline §10 retained verbatim)

Every functionality: requirement + user story + ACs. Complex flows only: use case + critical BDD scenarios. No Gherkin for trivial detail. ACs written Given/When/Then when behavioural, plain checklist when not (e.g., content or visual criteria).
