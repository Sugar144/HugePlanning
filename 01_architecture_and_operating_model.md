# 01 — Architecture and Operating Model

**Purpose:** the definitive system-level architecture: components, authority, information layers, lifecycle stages, gates, and execution model. All other files detail subsystems of this model.
**Baseline traceability:** retains B1–B11 (see `16` §1); deviations DEC-02, DEC-06, DEC-11, DEC-13, DEC-17. **V2:** adaptive process model (R2-01, `21`), evidence privacy split (R2-03), handoff history (R2-05), Git/Jira authority Model B (R2-06), verified distribution mechanism (R2-16, `19` §0).

---

## 1. System in one picture

```text
┌────────────────────────────────────────────────────────────────────┐
│ METHODOLOGY REPOSITORY  (how work is done — versioned, tested)     │
│  CLAUDE.md · rules · agents · skills · knowledge · templates ·     │
│  schemas · scripts · methodology tests                             │
└──────────────┬─────────────────────────────────────────────────────┘
               │  --add-dir (read-only; version pinned by lock)
               ▼
┌────────────────────────────────────────────────────────────────────┐
│ CLIENT REPOSITORY  (what work is about — one per client project)   │
│  project.yaml · methodology.lock.yaml · evidence/ · docs/ ·        │
│  src/ · tests/ · .github/workflows/                                │
└──────┬───────────────┬───────────────┬────────────────┬────────────┘
       │               │               │                │
       ▼               ▼               ▼                ▼
   Claude Code      GitHub          Jira           Hosting provider
   (agents work    (PRs, checks,   (operational    (staging + prod
    here)           protection)     board, view)     via adapter)
                          ▲
                    YOU: orchestrator, gate approver, final authority
```

Execution model (baseline §6, retained):

```bash
cd ~/Clients/<client-repo>
CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 \
claude --add-dir ~/Projects/freelance-methodology --agent <agent-name>
```

- Session, memory, and all writes belong to the client repo.
- Agents, skills, rules, knowledge, templates, schemas come from the methodology repo, pinned by `methodology.lock.yaml`.
- The methodology repo is read-only during client work, enforced by permission deny rules + launch-script check (DEC-02, detail in `02` §6).
- The `--add-dir` discovery mechanism is **verified official behaviour** (`19` §0); SPK-01 is a launch smoke check, with dormant fallbacks (`02` §5).

**Adaptive process model (V2, R2-01):** every project carries an archetype (what is being built) and a process profile (`LITE | STANDARD | HIGH-RISK` — how much assurance is required). The profile is hypothesized at G0, confirmed at G1, re-verified at G3, auto-upgraded on risk triggers, and downgraded only by explicit human decision. All floors — modules, artifacts, gates, reviewers, tests, deployment, operations — resolve through the single requirement matrix in `21` §5. Subsystem files describe full (STANDARD/HIGH-RISK) behaviour; LITE reductions come only from that matrix.

## 2. Authority model (who decides what)

| Domain | Authority | Everyone else |
|---|---|---|
| Business needs, scope, priorities, budget, acceptance | Client (recorded as evidence + approvals) | May propose, never assert |
| Requirements wording, classification, structure | Requirements pipeline (`07`), approved by you at G1, by client at G2 | Agents draft only |
| Technical decisions (stack, architecture, UX patterns) | You, via ADRs at G3 | Technical agent recommends |
| Task scope and DoR | Delivery backlog + G4 | Implementer must not expand scope |
| Merge to `main` | You, at G5 (PR review) | Agents never merge |
| Deploy to staging / production | You, at G6 / G8 | Pipeline executes, never initiates |
| Methodology content and version | You, in the methodology repo only | Client sessions never modify it |
| Conflict between artifacts | Precedence order (§4 below) + explicit resolution record | No silent choice |

## 3. Information layers and precedence (baseline §8, retained verbatim in substance)

| Layer | Contains | Lives in | Mutability |
|---|---|---|---|
| 1. Evidence | Sanitized transcripts, minimized client materials, confirmations, clarification answers — committed. Raw sensitive evidence (recordings, originals, unredacted transcripts) lives in gitignored `evidence-raw/` (R2-03, `03` §6) | `evidence/` (+ local `evidence-raw/`) | Append-only; never rewritten retroactively |
| 2. Canonical data | requirements.yaml, solution-context.yaml, open-questions.yaml, backlogs, ADRs, traceability, project.yaml | `docs/**/*.yaml`, `docs/architecture/decisions/` | Change-controlled after approval |
| 3. Human documents | PRD, SDD, reports, release notes, client validation package | `docs/**/*.md` | Regenerated/edited from layer 2; must cite layer-2 IDs |
| 4. Operational views | Jira board, dashboards, status report | Jira, generated files | Disposable; regenerable from layers 1–3 |

**Precedence on conflict (highest wins):**
1. Confirmed evidence
2. Approved requirements and decisions
3. Structured contracts (schemas, API contracts)
4. Explanatory documents (PRD/SDD prose)
5. Jira
6. Agent memory / session context
7. Unrecorded conversation

A detected conflict is never resolved silently: it becomes a `CTR-nnn` (contradiction) or `CR-nnn` (change request) with an explicit resolution record (`07` §6, `12` §5).

**Generation direction (anti-duplication, closes G-22):** layer 2 is authored; layer 3 cites and explains layer 2 (PRD lists `FR-001` by ID, doesn't restate it in different words); layer 4 is exported from layer 2. Never edit meaning in layers 3–4.

## 4. Project lifecycle: stages and gates (DEC-06, DEC-17)

### 4.1 Stages (`project.yaml → workflow.current_stage`)

```text
onboarding → discovery → specification → technical_design → planning
→ implementation → validation → release → operation
```

`operation` loops back into `implementation`/`validation`/`release` per change request. Stage status enum: `not_started | in_progress | blocked | in_review | approved | done`.

### 4.2 Gates

| Gate | Name | Approver | Checks (summary — full checklists in the owning file) | Record |
|---|---|---|---|---|
| G0 | Project readiness | You | Repo from template, private, lock set, engagement record, access/privacy defaults (`03` §7) | commit + `project.yaml` |
| G1 | Discovery package internal review | You | Audits clean (ambiguity, contradiction, assumption, NFR, schema); interview DoD met (`04` §12); **profile confirmed against risk triggers (`21` §4)** | `docs/handoffs/G1-*.yaml` |
| G2 | Business baseline approval | Client | Validation package confirmed: scope, behavior, priorities, exclusions, assumptions, estimate vs budget (DEC-16) (`07` §8) | `evidence/confirmations/` + merge to `main` |
| G3 | Technical baseline approval | You | **Per the profile matrix (`21` §5).** LITE = **G3-lite**: design note (stack/hosting, sitemap/page structure, visual direction, applicable NFR/test/deployment floors) + delivery task list DoR-ready. STANDARD/HIGH-RISK = full technical package (`05` §9: SDD, ADRs, UX deliverables, test strategy, deployment outline, delivery backlog). Includes the nested **G3-V** visual checkpoint where the profile requires it (§4.2b); profile re-verified | `docs/handoffs/G3-*.yaml` + merge |
| G4 | Task ready (DoR) | You | Per task/batch: goal, linked REQs, ACs, dependencies, tests declared, scope bounded (`08` §7) | task status `ready` |
| G5 | Task merge (DoD) | You | Tests green, spec + adversarial review resolved, traceability updated, PR approved (`09` §7) | merged PR |
| G6 | Staging release | You | Integration/regression/a11y/security suites green, smoke on staging (`11` §6) | release branch + staging deploy record |
| G7 | Client acceptance | Client | Acceptance walkthrough on staging against ACs (`10` §6) | `evidence/confirmations/` |
| G8 | Production release | You | Release manifest, rollback plan, migrations rehearsed, monitoring armed (`11` §7) | tag + release manifest |
| G9 | Change approval | You (+client if scope/€) | CR classified, impact analyzed, estimate accepted (`12` §5) | CR record |

No gate is ever auto-approved. Every gate produces a written record in the client repo: an append-only handoff file in `docs/handoffs/` (R2-05) plus, for client gates, a confirmation in `evidence/confirmations/`. **The lifecycle has exactly ten gates, G0–G9.** Gate *workflows* are profile-scoped (`21` §5): on LITE, G1+G2 run as one compact validation workflow and G6+G7+G8 as one compact release workflow — **each gate keeps its own decision, approver, and append-only record**; combining compresses ceremony, never decision identity. STANDARD/HIGH-RISK combine nothing.

### 4.2b G3-V — nested visual-approval checkpoint (not an eleventh gate)

G3-V is a **profile-dependent checkpoint inside G3**: it applies on STANDARD (wireframes + visual direction confirmation) and HIGH-RISK (formal design baseline); on LITE the visual direction is confirmed within G2 instead. **Approver: the client.** Record: confirmation in `evidence/confirmations/` + a `visual_approval` entry inside the G3 handoff record. Relationship to G3: where required, **G3 cannot close without G3-V** — it is a precondition of your G3 approval, not a separate lifecycle stage. Visual changes after G3-V are change requests (`12` §5); nothing visual that the client approved may be silently redesigned.

### 4.3 Stage × gate map

```text
onboarding ──G0──▶ discovery ──G1──▶ specification ──G2──▶ technical_design
──G3──▶ planning ──G4──▶ implementation ──G5(per task)──▶ validation
──G6──▶ (client) ──G7──▶ release ──G8──▶ operation ──G9──▶ (loop)
```

## 5. Component responsibilities (baseline §3.1, extended)

| Component | Responsibility | Detailed in |
|---|---|---|
| Methodology repository | Defines how work is done; versioned, tested product | `02` |
| Client repository | Holds all project truth; write target of every session | `03` |
| Agent | Role identity, authority, limits, completion conditions | `14` |
| Skill | Repeatable procedure with inputs/outputs/checks | `14` |
| Rule | Modular policy loaded always or by path | `02` §4, `14` |
| Knowledge | Consultable reference, loaded on demand | `02` §4, `14` |
| Template | Expected human shape of an artifact | `06` |
| Schema | Deterministic structural validation | `06` |
| `project.yaml` | Stage, approvals, **profile + history**, pointers, config — not artifact statuses (DEC-11) | `03` §4 |
| Requirement matrix (profiles × floors) | Single lookup scaling process weight to project complexity | `21` §5 |
| `methodology.lock.yaml` | Pins methodology version/commit/schemas per project | `02` §7 |
| Scripts | Deterministic glue: launch, validate, status, export, deploy | `02` §8 |
| Git/GitHub | Canonical history, review, protection, CI; owns task identity/definition/priority/estimate (R2-06) | `11` |
| Jira | Operational workflow status only, reconciled into Git at PR/batch events; **not used on LITE projects** (R2-06) | `08` §4 |
| You | Orchestrator, gate approver, final responsibility | everywhere |

## 6. Agent roster (DEC-12 — fixed at 9 for MVP)

| Agent | Interviews / acts on | Stage | File |
|---|---|---|---|
| `client-discovery` | The client | discovery | `04` |
| `technical-solution-architect` | You (the developer) | technical_design | `05` |
| `requirements-auditor` | Discovery artifacts | specification | `07` §4–5 |
| `doc-generator` | Canonical data → documents | specification/technical_design | `07` §7 |
| `implementer` | One task at a time | implementation | `09` §4 |
| `spec-reviewer` | Diff vs requirements/ACs | implementation | `09` §5 |
| `adversarial-reviewer` | Diff vs failure modes | implementation | `09` §5 |
| `risk-specialist-reviewer` | Security/a11y/payments/migrations diffs (triggered by risk table) | implementation/validation | `09` §5, `10` §5 |
| `release-manager` | Release prep, manifest, rollback plan | release | `11` §7 |

Everything else (audits, normalization, backlog refinement, UX outlining, Jira export, test planning) is a **skill**, invocable by an agent or by you directly. Full contracts in `14`. On LITE projects the spec and adversarial reviews run as one merged reviewer session (`21` §5) — same contracts, one pass.

## 7. Session and recovery model (closes R-CC1, G-13)

1. **Every session starts** by reading `project.yaml` + `methodology.lock.yaml`, determining stage and next action (client `CLAUDE.md` mandates this, `03` §5).
2. **Every session writes incrementally**: agents persist state to files at defined checkpoints (interview: each module close; implementation: each loop step). Chat memory is never the only copy of anything (baseline risk table, retained).
3. **Interruption recovery:** relaunch the same agent; it re-hydrates from state files (`interview-state.json`, task status, latest `docs/handoffs/` record), not from transcript re-reading.
4. **Commits as checkpoints:** work-in-progress commits on stage branches are normal and cheap; `main` stays baseline-only.

## 8. Cost and model policy (closes G-15)

| Work class | Model tier | Rationale |
|---|---|---|
| Client interview, technical design, adversarial review | Strongest available (Opus/Fable class) | Judgment-heavy, error cost highest |
| Implementation, spec review, doc generation | Strong default (Sonnet class) | Good code quality, bounded scope |
| Formatting, export, schema-fix loops | Small (Haiku class) | Mechanical |

Set per agent in frontmatter (`model:` field). Skills/knowledge loaded on demand keep context lean (baseline risk "contexto excesivo", retained).

## 9. Anti-patterns explicitly designed out (baseline §25 + mission)

No autonomous full-cycle orchestrator; no bidirectional Jira sync; no SaaS/multi-tenancy; no agent memory as truth; no giant single agent or single mega-prompt; no auto-approval; no silent mutation of approved artifacts; no unbounded loops (DEC-20: max 2 corrective cycles per review stage, then human); no requirements hidden in prose (layer 2 is the only place requirements are authored); no duplicated documents (generation direction, §3).

## 10. Future runtime compatibility (baseline §23, retained)

Portability rule: **schemas, templates, state models, and skill procedures are runtime-neutral**; only agent frontmatter and launch scripts are Claude-Code-specific. A future API runtime reuses layer-2 artifacts and skill procedure text with a different invocation shell. No plan file may embed Claude-Code-only assumptions inside an artifact schema.
