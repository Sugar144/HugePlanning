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
├── project.yaml                 # stage, approvals, profile, config (§4)
├── methodology.lock.yaml        # 02 §7
├── .gitignore                   # evidence-raw/, node_modules, .env*, build outputs, OS junk
├── .env.example                 # names only, never values
│
├── .claude/
│   └── settings.json            # methodology write-deny (02 §6) + project permissions
│
├── evidence-raw/                # LAYER 1 RAW — GITIGNORED, local only (R2-03)
│   │                            # recordings, original attachments/emails, unredacted
│   │                            # transcripts when redaction occurred; backed up only
│   │                            # to your encrypted backup location, never to Git remote
│   └── (mirrors evidence/ structure)
│
├── evidence/                    # LAYER 1 SANITIZED — committed, append-only (R2-03)
│   ├── interviews/
│   │   └── client-discovery-01/
│   │       ├── transcript.md            # SANITIZED, same turn numbering as raw;
│   │       │                            #   front matter: raw_ref + sha256 of raw (04 §8)
│   │       ├── transcript.jsonl         # sanitized machine turns (future app)
│   │       ├── interview-state.json     # state machine snapshot (04 §6)
│   │       ├── completion-report.md     # DoD evaluation at close (04 §12)
│   │       └── attachments/             # minimized/sanitized excerpts only
│   ├── clarifications/          # CLAR-nnn question + answer records (DEC-08)
│   ├── client-materials/        # minimized excerpts + provenance index (see §6)
│   └── confirmations/           # consent record (M0), gate approvals: G2, G7, G9
│
├── docs/                        # LAYERS 2 & 3
│   ├── product/
│   │   ├── engagement.md        # onboarding record (DEC-15): parties, service,
│   │   │                        #   commercial terms + maintenance tier pointer,
│   │   │                        #   communication channel, content-deadline clause (R2-18/19)
│   │   ├── PRD.md
│   │   ├── content-inventory.yaml  # CNT-nnn content/asset readiness (R2-18, 07 §9)
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
│   ├── task-context/            # TASK-nnn.md packages (09 §3), retained permanently (R2-08)
│   ├── changes/                 # CR-nnn.md change requests (12 §5)
│   ├── handoffs/                # append-only gate records (R2-05):
│   │   └── G<n>-<slug>-<seq>.yaml   #   e.g. G2-business-baseline-01.yaml
│   └── releases/
│       ├── CHANGELOG.md
│       ├── manifests/REL-nnn.yaml
│       └── verification/REL-nnn-verification.yaml  # execution evidence (R2-07, 10 §4b)
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
  archetype: [booking-system]   # 21 §1; hypothesis at discovery; confirmed at G3
  profile: standard          # lite | standard | high-risk (21 §2–4)
  profile_history:           # R2-01: every change logged; downgrades need reasoning
    - {value: standard, at: 2026-09-02, gate: G0, by: developer,
       reason: "booking + personal data, no HIGH-RISK trigger known"}
  status: active              # active | paused | archived
  repository_visibility: private

workflow:
  current_stage: discovery    # enum: 01 §4.1
  stage_status: in_progress
  stages_done: [onboarding]

tracking:
  jira: default               # none (LITE default) | default | waived {reason} (R2-06)

approvals:                    # latest gate records; full history in docs/handoffs/
  g0_readiness:      {date: 2026-09-02, by: developer, record: "docs/handoffs/G0-readiness-01.yaml"}
  g1_discovery_review: null
  g2_business_baseline: null
  g3_technical_baseline: null   # includes G3-V visual approval where required
  g7_client_acceptance: null
  g8_production_release: null

privacy:                      # DEC-10
  data_sensitivity: medium    # low | medium | high (drives review triggers, 10 §5)
  pii_in_evidence: minimized  # policy flag checked by evidence rule
  retention_after_close_months: 24
  deletion_contact: sugar144@uoc.edu

counters:                     # next free number per ID type (06 §4); single-writer
  { FR: 1, NFR: 1, INT: 1, CON: 1, DAT: 1, CNT: 1, BR: 1, OBJ: 1, OQ: 1, CLAR: 1,
    EP: 1, US: 1, UC: 1, TASK: 1, ADR: 1, SPK: 1, TEST: 1, CR: 1, BUG: 1, REL: 1, INC: 1 }
```

**What it deliberately does NOT contain (DEC-11):** per-artifact statuses (they live in each artifact), requirement counts, open-question counts. `status.sh` derives those live — one source of truth per fact.

## 5. Client `CLAUDE.md` (template — baseline §6.2 retained, tightened)

```markdown
# Project {{PROJECT_ID}}

This repository is the source of truth. The added methodology directory is
READ-ONLY reference: never write there, never copy client data into it.

## Session start (always)
1. Read `project.yaml` (stage, approvals, profile, language) and `methodology.lock.yaml`.
2. Run the stage's entry check before doing work (latest gate record in docs/handoffs/).
3. Never overwrite artifacts with status `approved` — use change control.
4. Never write outside this repository.

## Canonical paths
Evidence `evidence/` (sanitized; never write to `evidence-raw/`) · PRD `docs/product/PRD.md`
· Content inventory `docs/product/content-inventory.yaml` · Requirements
`docs/requirements/requirements.yaml` · Context `docs/requirements/solution-context.yaml`
· Questions `docs/requirements/open-questions.yaml` · Product backlog
`docs/backlog/product-backlog.yaml` · SDD `docs/architecture/SDD.md` · Delivery
backlog `docs/backlog/delivery-backlog.yaml` · Traceability
`docs/traceability/traceability.yaml` · Gate records `docs/handoffs/` · Releases `docs/releases/`

## Project notes
(project-specific constraints added as they arise — keep short)
```

No methodology duplication; pointers + invariants only.

## 6. Privacy, secrets, access (DEC-10 + baseline §18 retained; V2 raw/sanitized split R2-03)

- **Two evidence stores:** `evidence-raw/` (gitignored, local): recordings, original attachments and email exports, unredacted transcripts when redaction occurred. `evidence/` (committed): sanitized transcripts (identical turn numbering, so all `#turn-nnn` anchors resolve), minimized excerpts, confirmations, clarification records. Sanitized files carry `raw_ref` + SHA-256 of their raw counterpart (integrity + stable linkage). What may never be committed: recordings, credentials, full customer datasets, unredacted personal data beyond what a requirement needs.
- **Sanitization:** performed by the `interview-evidence-capture` skill at interview close (procedure in `04` §8): third-party names → roles, contact data removed, business facts kept verbatim. It removes/aliases identifiers only — it never paraphrases statements (evidence integrity).
- **Raw access rule:** agents in later stages read sanitized evidence only; consulting raw evidence is a manual, you-only act (prevents PII leaking into generated artifacts). Backup of `evidence-raw/` only to your encrypted backup location.
- **Consent:** recording/transcription consent obtained at interview M0, stored in `evidence/confirmations/`.
- **Secrets:** never in Git. Local: `.env` (gitignored) + `.env.example` with names. CI/deploy: GitHub Actions secrets + provider secret stores (`11` §8). Client-provided credentials recorded *that they exist* in `solution-context.yaml` (`access_status`), stored in your password manager, never in the repo.
- **Access:** repo private; collaborators only by engagement need; client gets read access only if contractually agreed. The client never needs to touch Git/Jira/Claude — all client touchpoints are email/call artifacts (R2-19 invariant).
- **Retention:** on project close → `status: archived`, retention clock starts (`retention_after_close_months`); deletion runbook (`12` §8) covers **both** stores and backups.

## 7. G0 readiness gate — checklist (printed by `new-client.sh`)

- [ ] Repo created from template, private, pushed, `main` protected
- [ ] `methodology.lock.yaml` matches an existing methodology tag
- [ ] `engagement.md` filled: client identity, contact, service scope sketch, commercial terms + maintenance tier reference, content-deadline clause, agreed communication channel
- [ ] `project.yaml`: language, sensitivity, retention set; **archetype + profile hypothesis recorded with rationale (`21` §4)**
- [ ] `.gitignore` covers `evidence-raw/`
- [ ] `.claude/settings.json` deny rules point at the real methodology path
- [ ] `validate.sh` passes on the fresh repo
- [ ] Launch test: `start-agent.sh <dir> client-discovery` starts and loads methodology (then exit)

G0 approved → commit, record in `project.yaml.approvals.g0_readiness`, stage advances to `discovery`.
