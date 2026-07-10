# 03 — Client Repository Design

**Purpose:** implementation-ready design of the per-client repository: structure, creation process, `project.yaml`, client `CLAUDE.md`, privacy/secret defaults, and the G0 readiness gate.
**Baseline traceability:** B8, B23, B25 (refined by DEC-11); additions DEC-10, DEC-15.

---

## 1. Principles

- One private repository per client project (baseline §5.1: privacy, permissions, CI/CD, archival, deletion — retained).
- Created only from `freelance-methodology/templates/client-repo/` via `new-client.sh` — never by hand, so structure and lock are always consistent.
- The client repo is the **only** write target of any client session.

## 2. Directory structure (authoritative — template content)

```text
client-project/
├── README.md                    # project one-pager + how to launch sessions
├── CLAUDE.md                    # project pointer file (§5)
├── project.yaml                 # stage, approvals, config (§4)
├── methodology.lock.yaml        # 02 §7
├── .gitignore                   # node_modules, .env*, build outputs, OS junk
├── .env.example                 # names only, never values
│
├── .claude/
│   └── settings.json            # methodology write-deny (02 §6) + project permissions
│
├── evidence/                    # LAYER 1 — append-only
│   ├── interviews/
│   │   └── client-discovery-01/
│   │       ├── transcript.md            # human-readable, per-turn anchors (04 §8)
│   │       ├── transcript.jsonl         # machine turns (future app; baseline §9.1)
│   │       ├── interview-state.json     # state machine snapshot (04 §6)
│   │       ├── completion-report.md     # DoD evaluation at close (04 §12)
│   │       └── attachments/
│   ├── clarifications/          # CLAR-nnn question + answer records (DEC-08)
│   ├── client-materials/        # files the client provides (minimized, see §6)
│   └── confirmations/           # gate approvals: G2, G7, G9 records
│
├── docs/                        # LAYERS 2 & 3
│   ├── product/
│   │   ├── engagement.md        # onboarding record (DEC-15): parties, service,
│   │   │                        #   commercial terms pointer, communication channel
│   │   ├── PRD.md
│   │   └── validation-package.md  # client-facing G2 summary (07 §8)
│   ├── requirements/
│   │   ├── requirements.yaml
│   │   ├── solution-context.yaml
│   │   └── open-questions.yaml
│   ├── backlog/
│   │   ├── product-backlog.yaml
│   │   ├── delivery-backlog.yaml
│   │   └── jira-map.yaml
│   ├── architecture/
│   │   ├── SDD.md
│   │   ├── data-model.md
│   │   ├── api-contract.yaml    # OpenAPI when the project has an API
│   │   ├── design-session-state.json   # 05 §3
│   │   ├── decisions/ADR-nnn-<slug>.md
│   │   └── spikes/SPK-nnn.md    # 05 §6
│   ├── quality/
│   │   ├── test-strategy.md
│   │   ├── test-matrix.yaml
│   │   └── security-checklist.md
│   ├── traceability/
│   │   └── traceability.yaml
│   ├── task-context/            # TASK-nnn.md packages (09 §3), disposable
│   ├── changes/                 # CR-nnn.md change requests (12 §5)
│   ├── handoff.yaml             # stage-transition readiness record (06 §5)
│   └── releases/
│       ├── CHANGELOG.md
│       └── manifests/REL-nnn.yaml
│
├── ops/
│   ├── runbook.md               # deploy, rollback, incident quick actions (12)
│   ├── monitoring.md            # what is monitored, where, alert routing
│   └── incidents/               # INC-nnn.md reports (12 §3)
│
├── src/
├── tests/
└── .github/workflows/           # ci.yml, deploy-staging.yml, deploy-prod.yml (11)
```

**Minimum viable subset at each stage** — the template creates the full tree with placeholder files carrying `status: missing` semantics by absence; `status.sh` reports which artifacts each stage requires (per `06` §5 inventory). Baseline §5.3 minimal list retained as the discovery-stage requirement set.

## 3. Creation process (G0 path)

```text
new-client.sh ~/Clients/acme-web ACME-WEB
  1. copy template, substitute {{PROJECT_ID}}, {{METHOD_DIR}}, {{DATE}}
  2. git init; git add -A; git commit -m "chore: initialize ACME-WEB from methodology v0.3.0"
  3. write methodology.lock.yaml from current methodology tag
  4. print G0 checklist
Manual follow-up:
  5. create private GitHub repo; push; enable branch protection on main (11 §3)
  6. fill docs/product/engagement.md (client identity, service, terms, channel)
  7. set retention/privacy fields in project.yaml (§4)
  8. create .env from .env.example if secrets already exist (never committed)
  9. tick G0 checklist → set workflow: onboarding → done, discovery → not_started
```

## 4. `project.yaml` (example — full schema `project.schema.json`)

```yaml
schema_version: 1.0.0
project:
  id: ACME-WEB
  name: Acme Web
  client_display_name: Acme S.L.
  language: es               # DEC-14: statements & client docs in this language
  archetype: booking-or-forms   # hypothesis at discovery; confirmed at G3
  status: active              # active | paused | archived
  repository_visibility: private

workflow:
  current_stage: discovery    # enum: 01 §4.1
  stage_status: in_progress
  stages_done: [onboarding]

approvals:                    # gate records; value = null | {date, by, record}
  g0_readiness:      {date: 2026-09-02, by: developer, record: "commit 1a2b3c"}
  g2_business_baseline: null
  g3_technical_baseline: null
  g7_client_acceptance: null
  g8_production_release: null

privacy:                      # DEC-10
  data_sensitivity: medium    # low | medium | high (drives review triggers, 10 §5)
  pii_in_evidence: minimized  # policy flag checked by evidence rule
  retention_after_close_months: 24
  deletion_contact: sugar144@uoc.edu

counters:                     # next free number per ID type (06 §4)
  { FR: 1, NFR: 1, INT: 1, CON: 1, BR: 1, OBJ: 1, OQ: 1, CLAR: 1, EP: 1,
    US: 1, UC: 1, TASK: 1, ADR: 1, SPK: 1, TEST: 1, CR: 1, BUG: 1, REL: 1, INC: 1 }
```

**What it deliberately does NOT contain (DEC-11):** per-artifact statuses (they live in each artifact), requirement counts, open-question counts. `status.sh` derives those live — one source of truth per fact.

## 5. Client `CLAUDE.md` (template — baseline §6.2 retained, tightened)

```markdown
# Project {{PROJECT_ID}}

This repository is the source of truth. The added methodology directory is
READ-ONLY reference: never write there, never copy client data into it.

## Session start (always)
1. Read `project.yaml` (stage, approvals, language) and `methodology.lock.yaml`.
2. Run the stage's entry check before doing work (docs/handoff.yaml if present).
3. Never overwrite artifacts with status `approved` — use change control.
4. Never write outside this repository.

## Canonical paths
Evidence `evidence/` · PRD `docs/product/PRD.md` · Requirements
`docs/requirements/requirements.yaml` · Context `docs/requirements/solution-context.yaml`
· Questions `docs/requirements/open-questions.yaml` · Product backlog
`docs/backlog/product-backlog.yaml` · SDD `docs/architecture/SDD.md` · Delivery
backlog `docs/backlog/delivery-backlog.yaml` · Traceability
`docs/traceability/traceability.yaml` · Releases `docs/releases/`

## Project notes
(project-specific constraints added as they arise — keep short)
```

No methodology duplication; pointers + invariants only.

## 6. Privacy, secrets, access (DEC-10 + baseline §18 retained)

- **Secrets:** never in Git. Local: `.env` (gitignored) + `.env.example` with names. CI/deploy: GitHub Actions secrets + provider secret stores (`11` §8). Client-provided credentials recorded *that they exist* in `solution-context.yaml` (`access_status`), stored in your password manager, never in the repo.
- **PII minimization:** transcripts capture what was said, but attachments and examples are pruned to what requirements need; full customer datasets are never committed — a sample schema or synthetic sample is committed instead (evidence rule enforces this).
- **Access:** repo private; collaborators only by engagement need; client gets read access only if contractually agreed.
- **Retention:** on project close → `status: archived`, retention clock starts (`retention_after_close_months`); deletion runbook in `12` §8.

## 7. G0 readiness gate — checklist (printed by `new-client.sh`)

- [ ] Repo created from template, private, pushed, `main` protected
- [ ] `methodology.lock.yaml` matches an existing methodology tag
- [ ] `engagement.md` filled: client identity, contact, service scope sketch, commercial terms reference, agreed communication channel
- [ ] `project.yaml`: language, sensitivity, retention set
- [ ] `.claude/settings.json` deny rules point at the real methodology path
- [ ] `validate.sh` passes on the fresh repo
- [ ] Launch test: `start-agent.sh <dir> client-discovery` starts and loads methodology (then exit)

G0 approved → commit, record in `project.yaml.approvals.g0_readiness`, stage advances to `discovery`.
