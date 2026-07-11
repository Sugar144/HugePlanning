# 19 — V2 Revision Audit and Change Log

**Purpose:** the audited decision on every V2 proposal, plus additional findings. Every change applied on branch `plan-v2-robustness` traces to a decision here (`R2-xx`). V1's baseline-audit log (`16`) remains frozen as the historical V1 record; this file is the V2 equivalent.
**V1 reference:** tag `plan-v1.0` (commit `e0d93b5`). Baseline file untouched.

---

## 0. Claude Code distribution — verification results (input to R2-16)

Verified against official docs (code.claude.com) on **2026-07-11**:

| Capability | Status | Source statement |
|---|---|---|
| `.claude/agents/` in `--add-dir` dirs discovered | **VERIFIED — yes** | "Directories added with `--add-dir` are also scanned: a `.claude/agents/` folder inside an added directory loads alongside project subagents" (sub-agents doc) |
| `.claude/skills/` in `--add-dir` dirs loaded | **VERIFIED — yes, live reload** | "skills are an exception: `.claude/skills/` within an added directory is loaded automatically. This exception applies only to `--add-dir` and `/add-dir`" (skills doc) |
| `CLAUDE.md` + `.claude/rules/` + `CLAUDE.local.md` from added dirs | **VERIFIED — only with `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`** | permissions doc, exceptions table |
| Main-thread agent selection | **VERIFIED** — `claude --agent <name>` "Specify an agent for the current session" | cli-reference |
| Dynamic agent injection | **VERIFIED** — `--agents '<json>'` flag | cli-reference |
| Hooks / permission rules / other settings from added dirs | **VERIFIED — NOT loaded** (only `enabledPlugins`, `extraKnownMarketplaces` keys) | permissions doc |
| `permissions.additionalDirectories` setting | **VERIFIED — file access only, loads NO configuration** (skills/agents require the flag) | permissions doc |
| Absolute-path deny rules `Edit(//path/**)` / `Write(//path/**)` | **VERIFIED** syntax; deny rules are not affected by workspace trust | permissions doc |
| Deny-rule limits | **VERIFIED caveat:** Read/Edit deny rules do not bind arbitrary subprocesses (a script that writes files itself); OS-level enforcement requires sandboxing | permissions doc |

**Consequences:** the V1 primary mechanism is confirmed. `start-agent.sh` must always pass the methodology via `--add-dir` **flag** (never rely on `additionalDirectories` setting) and set the env var. SPK-01 is downgraded from load-bearing spike to a launch **smoke check** (S0a): confirms live behaviour on the installed CLI version and re-runs on CLI upgrades. Fallbacks retained dormant: (A) materialized agent/skill copies via `new-client.sh`; (B) `--agents` JSON injection; (C) plugin packaging. New hardening note: because deny rules don't bind subprocesses, the before/after `git status` check on the methodology remains mandatory, and scripts run in client sessions must never take the methodology path as a write target.

## 1. Proposal decisions

Format per entry: **Problem validated? / Decision / Reasoning / Affected files / Applied change / Second-order effects / Validation required.**

### R2-01 — Two-dimensional classification: archetype × process profile (§5)

- **Validated?** Yes. V1 applied near-uniform process weight; archetypes only tuned NFR floors and test depth. A landing page and an e-commerce build got the same gates, artifacts, and reviews — commercially untenable and methodologically wrong.
- **Decision:** **ACCEPT.** Three profiles `LITE / STANDARD / HIGH-RISK` (names kept; a 4th level rejected — no evidence it pays for a solo operator). **Nine archetypes** (revised from V1's five; count corrected from "eight" in the review pass, R2-28). New file `21_process_profiles_and_archetypes.md` holds the full model; subsystem files hold their own floors.
- **Reasoning:** orthogonal dimensions — archetype = what capabilities/domain concerns exist (activates modules, knowledge packs, decision categories); profile = how much assurance is required (activates gates, artifacts, reviews, test layers). Profile is derived from **risk triggers**, not from archetype, so a booking site with healthcare data escalates while a brochure stays light.
- **Affected files:** new `21`; `01` (stages/gates get profile column), `02` (archetype knowledge file scope), `03` (`project.yaml` profile fields), `04` (module floors per profile), `05` (decision-category floors), `06` (artifact requirement matrix), `07` (profile confirmation at G1; LITE combined gates), `08` (Jira optionality), `10`–`12` (floors), `13` (roadmap), `14` (profile-proposal duty), `17` (knowledge activation).
- **Applied change:** profile hypothesized at G0, **confirmed at G1** (after discovery, when triggers are observable), re-verified at G3; auto-upgrade on trigger at any time (logged in `profile_history`); downgrade only by you with recorded reasoning; agents propose with trigger evidence, never select. Anti-gaming rule: when triggers are ambiguous, default up.
- **Second-order effects:** scripts (`validate.sh`, `status.sh`) become profile-aware; golden scenarios need one LITE and one HIGH-RISK case; more branching in checklists (accepted cost).
- **Validation:** consistency checks #11–13, #32–33; S1/S2 scenarios per profile.

### R2-02 — Split Stage S0 (§6)

- **Validated?** Partially. With AI-first generation the *authoring* cost of 13 schemas is small, but the *validation* cost is real, and V1's S0 delayed interviewer testing behind artifacts with no consumer until S3–S7.
- **Decision:** **ACCEPT WITH MODIFICATIONS.** S0 splits into **S0a (runtime bootstrap + distribution smoke check)** and **S0b (discovery infrastructure: 4 discovery-facing schemas + fixtures + minimal CI)**. Remaining schemas are created at their first consumer's stage (delivery-backlog & test-matrix at S3, jira-map at S5, release-manifest & verification at S7). No S0c as a stage — it's a build-when-consumed rule, not a stage.
- **Reasoning:** shortest path to the highest-uncertainty subsystem (interviewer) without structural debt; the schema *namespace* (ID grammar, status enums, `schema_version` convention) is still fixed at S0a so later schemas slot in without rework.
- **Affected files:** `13` (rewritten), `02` (§ scripts/tests timing), `20` (target stages).
- **Applied change:** roadmap restructured; `validate.sh` grows per-schema as schemas land.
- **Second-order effects:** early client repos (pilot) lack later schemas — acceptable, `validate.sh` validates only what exists; risk of schema-convention drift mitigated by the S0a conventions rule.
- **Validation:** consistency check #30.

### R2-03 — Evidence privacy: raw vs sanitized split (§7)

- **Validated?** Yes. Git cannot truly delete; V1 committed full transcripts/attachments, conflicting with GDPR erasure and its own retention design.
- **Decision:** **ACCEPT WITH MODIFICATIONS** (MVP-safe, no encrypted platform).
- **Reasoning:** the system's traceability needs *anchors that resolve*, not raw PII in history. Sanitized transcripts preserve turn numbering, so all `#turn-nnn` anchors keep working.
- **Affected files:** `03` (tree + .gitignore + retention), `04` (§8 capture rules + M0 consent), `06` (inventory/layers), `12` (deletion runbook), `14` (evidence-policy rule, interview-evidence-capture skill).
- **Applied change:** `evidence-raw/` (gitignored; recordings, original attachments, unredacted transcript when redaction occurred, raw email exports) vs `evidence/` (committed; sanitized transcript with identical turn numbering, minimized excerpts, confirmations, clarification records). Each sanitized file carries `raw_ref` + SHA-256 of its raw counterpart; sanitization procedure (names→roles, contact data removed, business facts kept) is part of `interview-evidence-capture`; consent to record/transcribe captured at M0 and stored as a confirmation; backup rule: `evidence-raw/` backed up only to your encrypted backup location, never to the Git remote; deletion runbook covers both stores.
- **Second-order effects:** agents in later stages read sanitized evidence only (raw access is a you-only manual act — prevents PII leaking into generated artifacts); golden-test fixtures are fictitious so raw=sanitized there; slight interview-close overhead (redaction pass).
- **Validation:** consistency check #14; S1 scenario includes a PII-bearing fixture.

### R2-04 — Artifact ownership contradictions (§8)

- **Validated?** Yes. Confirmed defect: `product-backlog.yaml` (layer 2) was produced by `doc-generator`, whose contract forbids editing layer 2. Full ownership audit found two more soft spots: `handoff.yaml` producer was "stage-closing agent" (ambiguous), and `security-checklist.md` had been fixed in V1's own review but the doc-generator issue was missed.
- **Decision:** **ACCEPT.**
- **Applied change:** `product-backlog.yaml` producer = **`backlog-refinement` skill (product mode)**, run in the specification-stage session after normalization; `doc-generator` produces layer 3/4 only (PRD, validation package, status report). Handoff records are produced by **you at each gate**, script-assisted (see R2-05). Ownership table in `06` §1 updated; every artifact now names one owner (the "one producer" simplification was later refined into the full ownership contract — R2-31, `06` §1a).
- **Affected files:** `06`, `07`, `14`.
- **Second-order effects:** `backlog-refinement` gains two documented modes (product / delivery) with different inputs and floors — one skill, two contracts, kept in one file to avoid near-duplicate skills.
- **Validation:** consistency checks #1–4.

### R2-05 — Handoff history (§9)

- **Validated?** Yes. Single `docs/handoff.yaml` would be overwritten at each transition, destroying gate-decision history.
- **Decision:** **ACCEPT** — simplest history-preserving model: `docs/handoffs/G<n>-<slug>-<seq>.yaml`, append-only, one file per gate event (repeat gate passes get `-02`…). **No current-pointer file** — current state is derived (`status.sh` reads the latest handoff per gate + `project.yaml.approvals`), so no competing source of truth.
- **Affected files:** `03` (tree), `06` (inventory + schema note), `07` (G1/G2 records), `05` (G3), `01` (gate record column).
- **Second-order effects:** `handoff.schema.json` gains `gate`, `sequence`; V1's single-path references replaced everywhere.
- **Validation:** consistency check #23.

### R2-06 — Git/Jira authority by field class (§10)

- **Validated?** Yes. V1's "Jira wins WIP status until PR time" was directionally right but informal.
- **Decision:** **ACCEPT — Model B**, formalized: Git owns identity, definition, requirements, ACs, dependencies, priority, estimate, release target, implementation history; Jira owns **operational workflow status only**, reconciled into Git at defined events (PR open, PR merge, batch close, release close). Assignee: Jira (irrelevant solo). Editing task *meaning* in Jira is prohibited; divergence detection = reconciliation script (S9) + manual spot check at batch close (MVP).
- **Jira optionality by profile:** LITE — no Jira (statuses live in `delivery-backlog.yaml`; Git is sole authority); STANDARD — Jira by default, may be waived for very small backlogs (recorded in `project.yaml`); HIGH-RISK — Jira used. **This is a logged deviation from baseline B5's universal Jira role**, justified by commercial practicality (§23); the Jira design itself is unchanged where Jira is used.
- **Affected files:** `08` (authority table), `01` (§ responsibilities), `21` (profile floors), `13` (S5 conditional).
- **Second-order effects:** when Jira is absent the task-status field in `delivery-backlog.yaml` becomes the operational board — `status.sh` renders it.
- **Validation:** consistency check #20.

### R2-07 — Test definitions vs execution evidence (§11)

- **Validated?** Yes. V1's `test-matrix.yaml` mixed stable definitions with `status`/`last_run` — Git noise and a second truth competing with CI.
- **Decision:** **ACCEPT.** `test-matrix.yaml` = definitions only (`id, verifies, level, automation, location|manual_procedure, required_for_profile, risk, environment`). Execution evidence lives in: CI runs (linked by run id), **verification snapshots** at release readiness (`docs/releases/verification/REL-nnn-verification.yaml`: per matrix row → result, commit, workflow run, environment, timestamp, artifact ref; manual rows → evidence note/screenshot ref), and release manifests referencing the snapshot.
- **Affected files:** `10`, `06`, `08` (trace edges), `11` (manifest reference), `03` (tree).
- **Second-order effects:** requirement `verified` status derivation moves from matrix rows to the latest verification snapshot; `validate.sh` checks snapshot coverage at G6 instead of matrix statuses.
- **Validation:** consistency check #21.

### R2-08 — Task-context retention (§12)

- **Validated?** Yes. V1 marked packages "disposable after merge" — destroys the record of what scope the implementer was actually given (audit/debug value).
- **Decision:** **ACCEPT WITH MODIFICATIONS** — simpler than proposed: packages stay permanently at `docs/task-context/TASK-nnn.md`, committed with the task's PR (Git history = the permanent pointer; no hash bookkeeping needed beyond the commit). **Rejected:** `active/`+`archive/` split (move-churn without benefit). Context changes during implementation are commits on the task branch; scope-affecting changes additionally require the task update per change control.
- **Affected files:** `09`, `06`, `03`.
- **Validation:** consistency check #22.

### R2-09 — AI-first roadmap revision (§13)

- **Validated?** Yes. V1 effort assumed manual authoring; the real bottleneck is specification → generation → integration → behavioural validation → correction.
- **Decision:** **ACCEPT.** `13` rewritten: per stage, effort decomposed into spec-prep / AI generation / integration / deterministic validation / behavioural validation / correction / approval; three scenarios (optimistic ≈ 20 focused days, realistic ≈ 36, contingency ≈ 60); explicit list of where AI compresses (generation, schemas, templates, scripts, boilerplate ≈ 70–90% saving) and where it doesn't (behavioural scenario runs, interview-quality judgment, integration defects, real-client latency ≈ 0–30%).
- **Affected files:** `13` (rewrite), `00`.
- **Second-order effects:** correction cycles become the visible unit of planning; the "generated ≠ correct" rule is stated as a stage acceptance principle.
- **Validation:** consistency check #35 (matrix vs S0a).

### R2-10 — Requirements model audit (§14)

- **Validated?** Yes on origins, NFR structure, approval identity, ID allocation; partially on new types.
- **Decision:** **ACCEPT WITH MODIFICATIONS.**
  - **Origins (accepted):** `origin: client_evidence | stakeholder_preference | methodology_default | legal_or_regulatory | technical_derived` on every requirement. **Rejected:** `business_rule` as an origin — BRs are a *kind* of item with their own collection, not a provenance. Methodology defaults and legal items enter as `status: proposed_default` until confirmed at G2 or consciously adopted (recorded) — a default can never impersonate the client.
  - **NFR fields (accepted, pragmatic subset):** `metric, target, conditions, measurement { method, environment }, verification_level, tolerance?, origin, client_confirmation`. "Fast" without a target fails ambiguity audit or is recorded as an explicitly waived NFR.
  - **Data/content/migration (modified):** new requirement type `data` (prefix `DAT-`: entities, quality, import/export, retention obligations). Content obligations go to the **content inventory** (`CNT-`, R2-18), not requirements.yaml. Migration needs are `category: migration` on FR/DAT/CON — a dedicated `MIG-` prefix rejected (archetype `migration-or-replatforming` + category covers it without another counter).
  - **`approved_in` (clarified):** the **merge commit of the baseline docs PR on `main`** — immutable, reachable, and equals what the client saw (the validation package is regenerated from that branch head before G2). Handoff record stores the same commit.
  - **ID allocation (documented):** MVP is single-writer (you/one session at a time); counters in `project.yaml` allocated at creation; `validate.sh` detects collisions/duplicates; parallel-branch allocation (ranges or merge-time assignment) explicitly **deferred and documented as a limitation** — revisit when worktrees activate.
- **Affected files:** `06` (§2, §4, §7), `07` (§2–3), `15` (limitation note).
- **Second-order effects:** requirements schema bumps to 2.0.0 semantics at S0b (breaking vs V1 draft — costless, nothing generated yet); audits gain an origin-integrity check.
- **Validation:** consistency checks #15–16.

### R2-11 — Backlog architecture (§15)

- **Validated?** Yes. V1's "usually 1 FR → 1 US" produces renamed requirements, not stories; story vs task lifecycles were conflated; "≤ ~1 day" task sizing was arbitrary.
- **Decision:** **ACCEPT WITH MODIFICATIONS.**
  - Distinct contracts: product backlog = value/capability view (epics, stories, phases, priorities, acceptance intent); delivery backlog = architecture-aware implementable work (tasks, dependencies, code areas, tests, sequencing). Transformation contract `approved REQs → product backlog → (technical baseline) → delivery backlog` with producer/consumer/loss rules and regeneration triggers.
  - **Vertical slicing (accepted):** strategies by workflow, role, happy-path-vs-exceptions, value increment, risk, BR cluster, integration boundary, phase, walking skeleton; a story must be a demonstrable user/business outcome.
  - **Story DoR/DoD separate from task DoR/DoD (accepted):** story done = all tasks merged **and** end-to-end AC demonstration on an integrated build.
  - **Sizing (accepted):** outcome-based reviewability replaces "~1 day": one coherent reviewable outcome, one PR; split when the diff mixes independent outcomes or review confidence drops; don't split below independently verifiable outcomes. Explicit cases: spikes, separate refactors, cross-cutting NFR tasks.
  - **Fields:** accept `release_target` (tasks/stories) and `phase` (product backlog). **Rejected:** `owner` (solo), `enables` (inverse of `depends_on`, derivable), `blocked_by` (duplicate of `depends_on`), numeric `business_value` and split `delivery_risk`/`technical_risk` (single `risk` + priority rationale suffice; unmaintained fields rot).
- **Affected files:** `08` (rewritten core), `06` (§7.4), `07` (§7).
- **Validation:** consistency checks #17–19.

### R2-12 — Specification completeness matrix (§16)

- **Decision:** **ACCEPT.** New file `20`; every implementation element classified (`fully specified / sufficient to generate / partially specified / underspecified`) with missing pieces, blocking flags, and target stage. Representative examples added in-plan only where interpretation errors are expensive and none existed (NFR example, verification snapshot, handoff record); the rest are required at generation time via template+schema.
- **Validation:** consistency check #35.

### R2-13 / R2-14 — Knowledge architecture standard + per-file minimum content (§17–18)

- **Validated?** Yes. V1 listed knowledge filenames with one-line scopes — insufficient to generate consistent, sourced, testable knowledge.
- **Decision:** **ACCEPT.** New file `17` with sections A–J (taxonomy, metadata, authoring patterns, specialized formats, source policy, retrieval design, anti-duplication, profile/archetype activation, lifecycle, testing) **plus §K**: minimum content specification for all 19 initial knowledge files (purpose, consumers, triggers, minimum topics, examples, source types, exclusions, maintenance, provisional-generation allowed?, research-mandatory?). Inventory audited: 19 files confirmed (V1's 18 + `web-project-archetypes` moves under `21`'s governance but stays a knowledge file).
- **Affected files:** new `17`; `02` §4.5 points to it; `14` §5 points to it.
- **Validation:** consistency checks #24–26.

### R2-15 — Knowledge research and evidence plan (§19)

- **Decision:** **ACCEPT.** New file `18`: research backlog (`RES-nnn`) separating provisional-model-generated content from research-mandatory content, each item with question, priority, target file, risk-if-unverified, sources, freshness, jurisdiction, evidence standard, completion criterion, integration procedure, review date. Executable next week without redesign. No research performed now except the Claude Code verification (§0), which the mandate required.
- **Validation:** consistency check #26.

### R2-16 — Claude Code distribution revalidation (§20)

- **Decision:** **RESOLVED — verified** (see §0). Primary mechanism (`--add-dir` + env var + `--agent`) is confirmed official behaviour. SPK-01 becomes a launch smoke check at S0a and re-runs on CLI upgrades (version recorded in the lock). Fallbacks A (materialized copies), B (`--agents` JSON), C (plugin) documented, dormant. New constraints propagated: never rely on `additionalDirectories` setting for loading; subprocess caveat keeps the git-status guard mandatory.
- **Affected files:** `02` §5–6, `13` (S0a), `15` (RSK-A1 downgraded), `16` untouched (historical).
- **Validation:** consistency check #27.

### R2-17 — UX/UI design and client visual approval (§21)

- **Validated?** Yes. V1 §05.8 covered flow outlines but had no visual-direction workflow and no client visual approval anywhere — a top source of freelance rework.
- **Decision:** **ACCEPT WITH MODIFICATIONS.** Profile-mapped UX deliverables (LITE: sitemap + page outlines + visual direction + responsive acceptance; STANDARD: + user flows, low-fi wireframes, component/state inventory, client visual approval; HIGH-RISK: + detailed flows incl. role/error/empty states, interactive prototype where useful, accessibility design review, formal design baseline). Producer: `technical-solution-architect` with new skill `ux-design-outline` (skill #18). **Client visual approval is a recorded sub-approval of G3** ("G3-V") for STANDARD/HIGH-RISK — no new gate number; for LITE the visual direction rides in the G2 validation package. Post-approval visual changes go through change control. **Rejected:** a separate UX agent (role fits the technical architect; a new agent would split one coherent design conversation).
- **Affected files:** `05` §8 (rewritten), `01` (G3 row), `21`, `06` (design artifacts), `08` (UX→story/test mapping), `14` (skill).
- **Validation:** consistency check #28.

### R2-18 — Content and asset readiness (§22)

- **Validated?** Yes. Content delay is a dominant real-world stall cause and V1 only captured "content responsibility" as an interview topic.
- **Decision:** **ACCEPT.** New canonical artifact `docs/product/content-inventory.yaml` (`CNT-nnn`: item, type, owner, source, license/provenance, needed_by story/task refs, deadline, status `missing|promised|received|approved|placeholder_approved`, fallback). Seeded during discovery (M5/M7), completed at specification, tracked through delivery. Content readiness joins **story DoR** (stories touching pages need content `received/approved` or an explicitly approved placeholder); release with placeholders requires client sign-off at G7. Client delay handling: engagement record gains a content-deadline clause; delays are handled as schedule/scope CRs, not silent waiting. Profile depth: LITE = one-page inventory; HIGH-RISK adds provenance/licensing rigor. **Not built:** any content-management tooling.
- **Affected files:** `03`, `06`, `07` (new §), `08` (DoR), `04` (M7 topics), `12` (delay handling), `21`.
- **Validation:** consistency check #29.

### R2-19 — Commercial and delivery practicality (§23)

- **Validated?** Yes, audit finding: V1 was commercially viable for STANDARD-class work but made small sites unprofitable (full gate chain, Jira, full artifact set).
- **Decision:** **ACCEPT** — realized principally *through* R2-01: LITE fast path (G1+G2 as one compact validation workflow and G6+G7+G8 as one compact release workflow — **each gate retaining its own decision, approver, and record** (refined R2-29); no Jira; minimal artifact floor; dry-run in `21` §7 shows a landing page carrying ≈ 6–10 hours of total process overhead). Plus: maintenance expectations become named billable tiers in `engagement.md` (`12`); client-facing touchpoints remain plain-language email/call — the client never touches Git/Jira/Claude (already V1 policy, now stated as an explicit invariant); estimates price phases from the product backlog.
- **Affected files:** `21` §7, `03` (engagement), `12` (tiers), `07` (validation package brevity rule).
- **Validation:** consistency checks #12, #32, #34.

## 2. Additional audit findings (beyond the proposals)

| ID | Finding | Decision & change |
|---|---|---|
| R2-20 | `16` (V1 audit log) must not be retro-edited to reflect V2 | Frozen as historical; V2 decisions live here. Cross-reference added in `00` only |
| R2-21 | Scripts were profile-blind | `validate.sh` / `status.sh` read `project.profile` and apply the requirement matrix from `21` (e.g., missing SDD is an error for STANDARD, not for LITE) |
| R2-22 | V1 `project.yaml` example omitted G1 from approvals and had no profile fields | Fixed in `03` §4: full gate list + `profile`, `profile_history` |
| R2-23 | V1 golden scenarios covered no profile variance | S1/S2 scenario set now includes one LITE and one trigger-escalation case (`13`) |
| R2-24 | `solution-context.yaml` had no home for detected **risk triggers** | Added `risk_triggers[]` section — the machine-readable input to profile confirmation at G1 (`06` §7.2, `21` §4) |
| R2-25 | Statement-classification example missing (expensive to misinterpret) | Compact worked example added to `04` §3 |

## 3. Decision summary

**Accepted:** R2-01, R2-04, R2-05, R2-06 (Model B), R2-07, R2-09, R2-12, R2-13/14, R2-15, R2-18, R2-19. **Accepted with modifications:** R2-02, R2-03, R2-08, R2-10, R2-11, R2-17. **Resolved by verification:** R2-16. **Rejected (sub-items, with reasons above):** 4th profile level; `business_rule` as origin; `MIG-` prefix; task-context archive split; `owner/enables/blocked_by/business_value/split-risk` backlog fields; separate UX agent. **Deferred (documented):** parallel-branch ID allocation; encrypted evidence platform; Jira reconciliation automation (S9).

## 3b. PR #1 review correction pass (2026-07-11)

Three reviewer findings (all validated) plus consistency findings from the mandated audit and LITE dry-run. Each applied across all affected files.

| ID | Finding & decision | Applied change |
|---|---|---|
| **R2-26** | **`validate.sh` deferred past G0** (reviewer, valid): S0a acceptance required a scratch client to pass G0, but G0 requires validation and the script was scheduled at S0b — self-blocking milestone. **Accepted: progressive validator.** | S0a creates the **minimal `validate.sh`** (project.yaml, lock, repo structure — enough for G0); every later stage **extends the same script** as each schema gains its first consumer; never a second validator. Updated: `02` §8, `13` S0a/S0b, `00` actions 6/11/13, `20` |
| **R2-27** | **Unconditional technical-design inputs** (reviewer, valid): `05` §1 required `PRD.md` and `product-backlog.yaml`, which the LITE floor omits — LITE path failed at technical-design startup. **Accepted: profile-resolved inputs.** | Always-present core registries (requirements, solution-context, open-questions (may be empty), content-inventory where applicable, G2 handoff) vs profile-conditional (PRD, product backlog). LITE session semantics made explicit: **one short internal technical session → design-note SDD → G3-lite**; "no separate session" = no client-facing meeting. Updated: `05` §1/§9, `21` §5, `06` §6 (design-note template variant) |
| **R2-28** | **G3 hardcoded the STANDARD package** (reviewer, valid) + **archetype count said eight, listed nine**. **Accepted.** | `01` §4.2 G3 row now resolves through the profile matrix, defining G3-lite explicitly. Archetype count fixed to **nine** everywhere (`00`, `19` R2-01, `21` §1, PR body); no archetype deleted |
| **R2-29** | **"Combined" LITE gates risked losing decision identity.** **Accepted: compact workflows, distinct decisions.** | G1+G2 and G6+G7+G8 run as compact workflows on LITE, but each gate keeps its own decision, approver, and append-only handoff record. Updated: `01` §4.2, `21` §5/§7, `07` §1, R2-19 wording |
| **R2-30** | **`open-questions.yaml` optionality created conditional-input complexity.** **Accepted: always present.** | Registry created empty by the template for every profile; profile governs depth and gate-blocking only. Updated: `21` §5, `05` §1, `06` §7.3, `13` S0b, `00` action 7 |
| **R2-31** | **"Exactly one producer" conflicted with multi-mutator artifacts** (project.yaml counters, OQ appends, content statuses, CRs). **Accepted: explicit ownership contract.** | Owner + authorized mutators (field-level where needed) + one mutation procedure + one approval authority; client never edits repo files — input becomes evidence, an authorized role incorporates it. New `06` §1a details the seven multi-mutator artifacts |
| **R2-32** | **RES-01 priority too low for a requirements-quality product.** **Accepted.** | RES-01 → **high**; does not block S0–S3 generation/scenario validation; **blocks the first real paid discovery interview**; scope broadened (quality, validation, NFR treatment, stakeholder/conflict handling, traceability, completion criteria). Updated: `18`, `17` §K.2, `00` action 19 |
| **R2-33** | **LITE dry-run findings** (`21` §7 executed step-by-step): (a) LITE G1 required "audits clean" but the auditor agent wasn't in the LITE roster; (b) the 1-page brief had no producer on LITE (doc-generator not in roster). **Fixed.** | (a) LITE G1 = `validate.sh` + compact audit checklist run by you (independence preserved — you are not the producer); (b) brief generated via the artifact-generation **skill** in-session. HIGH-RISK contrast check confirmed no weakening of the full path. Updated: `21` §5/§7, `07` §1/§4 |

## 4. Consolidated second-order risks introduced by V2

1. **Profile branching complexity** — more conditional paths in checklists/scripts; mitigated by one requirement matrix (`21` §6) as the single lookup, and scenario coverage per profile.
2. **Sanitization becomes a correctness dependency** — a bad redaction pass could distort evidence; mitigated: sanitization only removes/aliases identifiers, never paraphrases statements; raw retained locally for dispute resolution.
3. **Under-classification pressure** (choosing LITE to save work) — mitigated by trigger-based auto-upgrade, default-up rule, and the agent's duty to propose with evidence.
4. **Stage-driven schema creation** could fragment conventions — mitigated by the S0a conventions rule (ID grammar, enums, `schema_version` policy fixed once).
5. **Verification snapshots add a release-time step** — accepted; it replaces continuous matrix-status churn with one auditable record per release.

## 5. Post-S0a maintenance decisions (2026-07-11, branch `chore/planning-assurance-organization`)

Recorded after the `v0.1.0` release, from the verified S0a execution (experiment report + integration audit + operator evaluation). Append-only continuation of this log.

### R2-34 — Proportional implementation-assurance loop (new file `22`)

- **Validated?** Yes. S0a surfaced five verified lessons the plan did not encode: (F1) an example silently shrank closed normative sets (6 gates vs G0–G9; 21 counters vs the full namespace) and the generated schema inherited the example; (F2/F3) the material defects were refusal-path gaps (dirty-bootstrap warning instead of refusal; no validation before the initial client commit); (F4) a verification oracle produced a false negative (SPK sentinel) that naive process would have "fixed" as a product bug; (F5) one candidate's Skill fixture failed only under the real runtime while its own environment reported `UNVERIFIED`.
- **Decision:** **ACCEPT.** New file `22_implementation_assurance_and_adversarial_validation.md` defines the stage-level assurance sequence (contract reconciliation → risk-based adversarial test design → implementation → bounded independent review → deterministic validation → real-runtime validation where relevant → failure classification → release evidence), the review policy (one principal implementer; no default subagents; ChatGPT-class models as targeted gate auditors only; parallel duplicate implementation demoted to an explicit experiment), the `CODE | TEST | CONTRACT | PROCESS | ENVIRONMENT` failure classes with the four runtime-result classes, proportionality factors, and the concise release-evidence set. A new file (rather than growing `13` or `10`) keeps one authority: `13` stays the roadmap/effort model, `10` stays client-product testing, `02` §10 stays methodology test layers — all three now reference `22` instead of restating process.
- **Affected files:** new `22`; `00` (index, count 21→22 files, §5 loop pointer); `13` §2 (loop executes inside `22`); `15` (RSK-A14 pointer, new RSK-A16, validation-plan items 5–6); `10` §8 (cross-reference).
- **Validation:** documentation-only change per `22` §6 (no runtime surface); deterministic suite re-run green; no live SPK-01 required.
