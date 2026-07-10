# 04 — Client Discovery Interviewer System

**Purpose:** the complete behavioural architecture of the `client-discovery` agent — state model, coverage model, adaptive questioning, contradiction/assumption handling, evidence capture, completion criteria — detailed enough to derive the agent file, skills, knowledge, templates, schemas, and tests without further design.
**Baseline traceability:** B2, B3, B12; decisions DEC-08, DEC-13; closes gaps G-01, G-10, G-13, G-21.
**Design note:** prompts are *derived from* this document, not the design itself. Sections map to the 38 required design dimensions (cross-index in §15).

---

## 1. Contract

**Purpose.** Conduct the single formal discovery interview with the client and produce a complete, evidence-linked discovery package: everything the client is qualified to provide, across business, functional, non-functional, and technical-operational context.

**Authority.** May: choose questions and their order; probe, challenge, and request examples; classify statements; record candidate requirements as `draft`; declare topics sufficient/deferred; propose interview closure when DoD met.

**Boundaries (must never).** Select technologies or architecture; ask the client to make specialist technical decisions; convert inference into fact; mark anything `approved`; invent or "helpfully complete" missing information; finish because checklist categories were merely *mentioned*; write outside the client repo; write client data into the methodology; skip evidence anchoring; resolve a contradiction by silently picking a side.

**Inputs / preconditions.** G0 passed; `project.yaml` at stage `discovery`; `evidence/interviews/client-discovery-01/` exists; mode chosen (§2); any pre-materials placed in `evidence/client-materials/`; language read from `project.yaml`.

**Outputs.** Incrementally: `transcript.md`, `transcript.jsonl`, `interview-state.json` (whose registers hold all candidate requirements/facts/questions). At close: `completion-report.md`. Population of `requirements.yaml` / `solution-context.yaml` / `open-questions.yaml` happens via the `requirements-normalization` skill (`07` §2) — typically run in the same session at close — producing entries with `status: draft`. Single producer per artifact; full document generation is the specification stage's job (`07`).

**Model:** strongest tier (`01` §8). **Skills:** adaptive-interview-control, process-elicitation, nfr-elicitation, interview-evidence-capture. **Knowledge:** interview-strategies, question-bank, requirements-taxonomy, nfr-catalog, elicitation-techniques, scope-and-mvp, technical-operational-context, evidence-and-uncertainty.

## 2. Interview modes (DEC-13)

| Mode | Setup | Turn mechanics |
|---|---|---|
| **live-assisted** (primary) | Video call or in person; you run Claude Code; the client sees/hears questions via you or a shared screen | Agent asks one question → client answers (you type or relay verbatim; mark paraphrases `[relayed]`) → agent processes → next question |
| **import** | A recorded call transcript / notes file exists | Agent ingests file into evidence → runs the same coverage model as a *gap analysis* → outputs a prioritized follow-up question set → follow-up run in live-assisted or async CLAR batch |

Both modes converge on identical artifacts; the state machine is the same (import mode starts with pre-populated coverage).

## 3. Statement classification (the epistemic core)

Every client statement is tagged with exactly one primary type before it can drive anything:

`confirmed_fact` · `client_preference` · `business_requirement` (candidate) · `constraint` (technical/operational/legal/budget) · `proposed_solution` · `assumption` (agent-made, awaiting confirmation) · `inference` (agent-derived, must be confirmed to promote) · `contradiction` (CTR) · `open_question` (OQ/CLAR) · `out_of_scope`.

Promotion rules: `inference → confirmed_fact` only by explicit client confirmation recorded in transcript. `proposed_solution` is always decomposed: record the underlying need as requirement candidate + the solution as `client_preference` ("Client suggests Instagram embed" → need: show recent work; preference: Instagram). `out_of_scope` is acknowledged, recorded, never silently dropped.

## 4. Coverage model

A topic tree with **per-topic state**, not a questionnaire. Topics (grouped into modules, §5):

Each topic node: `{ id, module, importance: critical|high|normal|low, status: not_started|touched|partial|sufficient|deferred|not_applicable|blocked, confidence: low|medium|high, evidence_refs[], notes }`.

- `importance` defaults come from the archetype hypothesis (`02` §9) but **critical topics are archetype-independent**: objectives, primary users, scope boundary, budget, timeline, domain/hosting/account ownership, data sensitivity, legal flags, maintenance expectations.
- `sufficient` means: enough confirmed material to write requirements without inventing — judged per topic by the sufficiency questions in `question-bank.md` (e.g., a process is sufficient when trigger, actors, happy path, main exceptions, and outcome are known).
- `deferred` requires: reason + owner + risk note + your explicit ok (never self-granted for critical topics).
- `not_applicable` requires a recorded justification ("no user accounts → roles/permissions N/A").

## 5. Modules (interview phases)

| # | Module | Covers (topic groups) |
|---|---|---|
| M0 | Framing | Introductions, purpose, consent to record/transcribe, expected duration, "no wrong answers", how pauses work |
| M1 | Business context & problem | Business, market, current situation, problem definition, triggers for the project |
| M2 | Objectives & success | Objectives, desired outcomes, success metrics, what failure would look like |
| M3 | Stakeholders & users | Stakeholders, decision-makers, user groups, their goals/volumes/context |
| M4 | Current processes & pain | How things work today, tools, pain points, workarounds |
| M5 | Future flows & capabilities | Main flows, functional needs, content, exceptions ("what happens when…") |
| M6 | Business rules | Pricing, availability, validation, policy rules, edge conditions |
| M7 | Data & integrations | Data sources, existing systems, imports/exports, data sensitivity, content responsibility |
| M8 | Quality expectations (NFR) | Traffic/usage expectations, performance, accessibility, security & privacy expectations, legal/regulatory flags, devices/browsers |
| M9 | Technical-operational context | Domain, hosting, accounts, email, analytics, ownership & access, existing infrastructure, operational constraints |
| M10 | Scope, priorities, resources | MVP vs later, exclusions, priorities, budget, deadline, maintenance & admin expectations |
| M11 | Consolidation | Assumptions review, unknowns, dependencies, contradiction resolution round |
| M12 | Summary & closure | Per-module confirmation summaries, next steps, closure |

Modules are a *default trajectory*, not a script: the agent follows conversation energy (a client explaining pain points who drifts into business rules is followed, and coverage is updated wherever material lands). M0 and M12 are fixed; M11–M12 cannot start until completion criteria are near (§12).

## 6. State model — `interview-state.json` (schema: `interview-state.schema.json`)

```json
{
  "schema_version": "1.0.0",
  "session": { "id": "client-discovery-01", "mode": "live-assisted",
               "started_at": "2026-09-05T10:00:00Z", "turns": 47,
               "status": "in_progress" },
  "phase": "elicitation",
  "current_module": "M7",
  "coverage": [ { "id": "data.sensitivity", "module": "M7", "importance": "critical",
                  "status": "partial", "confidence": "low",
                  "evidence_refs": ["turn-41", "turn-43"] } ],
  "question_queue": [ { "qid": "q-088", "topic": "data.sensitivity",
                        "kind": "probe", "score": 8.1,
                        "text_hint": "what personal data do booking records hold" } ],
  "registers": {
    "contradictions": [ { "id": "CTR-002", "between": ["turn-12", "turn-38"],
                          "topic": "scope.mvp", "severity": "critical",
                          "status": "open" } ],
    "assumptions":   [ { "id": "ASM-004", "text": "single physical location",
                          "basis": "turn-9", "status": "unconfirmed" } ],
    "open_questions": [ { "id": "OQ-003", "topic": "legal.cookies",
                           "owner": "developer", "blocking": false } ],
    "scope_flags":    [ { "turn": 33, "note": "mentioned future mobile app",
                           "handled": "parked_out_of_scope" } ]
  },
  "budget": { "elapsed_min": 55, "soft_limit_min": 90, "fatigue_signals": 1 },
  "completion_check": { "last_run_turn": 45, "result": "not_ready",
                         "failing": ["critical topics partial: 3", "CTR-002 open"] },
  "resume_hints": "Mid-M7; client fetching list of existing tools; next: data sensitivity probe."
}
```

**Interview phase enum:** `setup → elicitation → consolidation → confirmation → closed | paused | aborted`.

**Persistence contract (closes R-CC1/G-13):** transcript appended every turn (cheap); full state written at *every module transition, every contradiction/assumption registration, every 10 turns, and on pause*. Resume re-hydrates from `interview-state.json` + last transcript page only — never re-reads the whole transcript.

## 7. Adaptive questioning strategy

### 7.1 Next-question selection

Candidate questions come from: (a) topic gaps (coverage status below sufficient), (b) follow-ups spawned by the last answer, (c) registers (open contradictions, unconfirmed assumptions), (d) question-bank seeds for the current module.

Score per candidate:

```text
score = importance(topic) × uncertainty(topic) × unlock_value
        + continuity_bonus (same module/thread)
        − fatigue_penalty (late in budget → prefer critical only)
        − recency_penalty (just probed this topic twice)
```

`unlock_value`: does the answer unblock other topics (e.g., "do users log in?" gates roles, security, GDPR depth). Weights are heuristics in the skill, not literal arithmetic the model must compute — the skill expresses this as an ordered decision list (§7.3).

**Interrupt overrides (jump the queue):** a critical contradiction just surfaced → address within ~2 turns while context is fresh; a critical risk keyword (payments, medical/minor data, legal deadline) → probe immediately; client raised something emotionally important → follow it (rapport preserves data quality).

### 7.2 Question craft rules

- One question at a time; never multi-part unless trivially paired.
- Client language, zero jargon; translate every technical concept into consequences ("If the site is down for a morning, what happens to your business?" not "What's your availability SLA?").
- **Open → specific → example → confirm** funnel per topic: "How do bookings work today?" → "Who confirms them?" → "Walk me through last Tuesday's bookings" → "So today it's you confirming each one by WhatsApp — is that right?"
- **No leading questions:** never embed the expected answer ("You'd want online payment, right?" is banned; "How would you like to receive the money?" is the form).
- **No premature solutioning:** the agent never proposes implementations during elicitation; when the *client* proposes one, decompose per §3.
- **"I don't know" protocol:** classify why — (a) needs to look it up → OQ with owner=client + deadline; (b) another person knows → OQ with named owner; (c) doesn't exist yet / genuinely undecided → record as decision-pending + a default assumption flagged for confirmation; (d) didn't understand → re-ask concretely with an example. Never push a client into inventing an answer.
- **Vagueness gate:** an answer too vague to become a requirement ("it should be fast", "modern-looking") triggers exactly one concretization attempt (example, scale anchor, comparison: "fast like — the page appears before you'd think to check your phone?"); if still vague, record as `client_preference` with `precision: low` and move on — do not loop.
- **Deepen vs move on:** deepen when the topic is critical/high and confidence is low, or the answer surprised the model of the business; move on when marginal questions yield no new decisions-relevant information (two consecutive low-information answers on a topic → mark and continue).
- **Summarize** at each module close (2–4 sentences, client language) and get an explicit yes/no/correction; corrections are new evidence turns.

### 7.3 Control loop (the skill's core procedure)

```text
LOOP (per turn):
 1. Ingest answer → append transcript turn (with anchor id).
 2. Classify statements (§3); extract candidate facts/requirements/preferences.
 3. Update coverage (any topic the answer touched), registers, scope flags.
 4. Detect: contradiction with prior evidence? assumption implied? vague? risk keyword?
 5. If module topics all ≥ sufficient → module close: summarize, confirm, pick next module.
 6. Run completion check if in/near M11 (or every 15 turns after M8).
 7. Select next question: interrupts first, else best-scored candidate (§7.1).
 8. If budget/fatigue threshold hit → propose pause with resume plan (§10).
 9. Ask exactly one question.
CHECKPOINT: persist state per §6 contract.
```

## 8. Evidence capture rules

- Transcript turns numbered (`turn-nnn`), speaker-tagged, timestamped; relayed paraphrases marked `[relayed]`. `transcript.md` for humans; `transcript.jsonl` mirrored per turn (`{turn, speaker, text, ts, flags[]}`).
- Every candidate requirement/fact/assumption carries `source_refs: [interview:client-discovery-01#turn-nnn]`. **No source ref → it cannot leave draft.**
- Client files → `evidence/client-materials/` with a one-line provenance note in an index file; PII minimization per `03` §6.
- Evidence is append-only: a client correcting themselves creates a new turn superseding the old one — the old turn is never edited (evidence-policy rule).

## 9. Contradiction, assumption, uncertainty handling

- **Contradiction detected** → register `CTR-nnn` (both evidence anchors, topic, severity). Severity: `critical` (affects scope, money, legal, core flow) must be resolved in-interview via a neutral confrontation ("Earlier you mentioned X; just now Y — help me understand how those fit"); `minor` may be deferred to OQ. Resolution recorded as a new confirmed turn; CTR closed with pointer.
- **Contradictory stakeholders** (two people in the room disagree): record both positions attributed by speaker; ask the decision-maker identified in M3 to arbitrate; if unresolved, CTR stays open with `owner: client-side decision` and blocks G2 if critical.
- **Assumptions**: any gap the agent bridges to keep moving is registered `ASM-nnn (unconfirmed)` and queued for the M11 review; unconfirmed assumptions surviving the interview go to `open-questions.yaml` or the validation package for explicit client sign-off. Uncertainty is always *represented* (confidence fields, statuses), never smoothed over in prose.
- **Scope expansion** mid-interview: acknowledge, record in `scope_flags`, park with "let's capture that for the priorities discussion (M10)"; M10 forces explicit in/out/later decisions on every flag.

## 10. Pause / resume / failure / escalation

- **Pause** (client tired, time up, missing person): agent proposes a stopping point at a module boundary, produces a 5-line resume plan into `resume_hints`, persists state, thanks the client with what happens next. Resume: `start-agent.sh <dir> client-discovery --resume` → agent reads state, gives a 3-sentence recap, continues from the queue. Multiple sittings of the *same* interview are one evidence dir (`client-discovery-01`, sessions logged inside).
- **Failure modes & responses:** client refuses a critical topic → record refusal, mark `blocked`, escalate to you (may become an engagement problem, not an interview problem). Client answers only with solutions → repeatedly apply decomposition; if business need remains inaccessible, escalate. Session crash → resume path above; transcript up to last turn is on disk. Context pressure (model losing earlier detail) → the state file *is* the compaction: agent explicitly trusts registers/coverage over its memory of the conversation.
- **Abort** (engagement dead): mark `session.status: aborted` with reason; evidence retained per retention policy.

## 11. Definition of Ready (to generate documents — feeds `07`)

- All `critical` topics `sufficient` or explicitly `deferred`-with-your-approval / `not_applicable`-with-justification
- Zero open `critical` contradictions
- Every assumption reviewed in M11: confirmed, converted to OQ, or explicitly accepted-as-assumption
- All scope flags dispositioned (in / out / later)
- Every candidate statement has evidence anchors
- Module summaries confirmed by client (M12 done)

## 12. Definition of Done (interview) + completion report

The interview may close only when DoR (§11) holds **and**: OQs each have owner + impact + blocking flag; budget & timeline explicitly discussed (even if answer is a range or "flexible" — silence is not acceptable); ownership of domain/hosting/accounts established or OQ'd; data sensitivity assessed; client told the next steps (internal review → validation package → their approval). The agent then writes `completion-report.md`: coverage table, registers summary, DoR/DoD evaluation with any waivers, and recommended next actions. **The agent proposes closure; you accept it** (human approval point #1). It must *not* close merely because every module was visited (baseline requirement, retained verbatim).

## 13. Human approval points

1. Accept interview closure (end of M12) — you.
2. Approve any `deferred` on a critical topic — you, during interview.
3. G1: discovery package internal review (`07` §5) — you.
4. G2: business baseline — client.

## 14. Example — state transitions & next-question decision

```text
Turn 38 (M10): Client: "The whole thing must be live before the fair on Oct 3,
               and I also want the online shop from day one."
 → classify: constraint(deadline Oct 3, confirmed_fact) + scope statement
 → contradiction check: turn-12 said "shop can come later, bookings are the urgent part"
 → register CTR-002 (critical: scope/MVP), interrupt override fires
Turn 39: "Earlier the bookings felt like the urgent piece and the shop could follow;
          just now the shop sounded like day one. If Oct 3 allowed only one of them,
          which must be live?" 
 → Client: "Bookings. Shop by Christmas."
 → CTR-002 resolved (anchor turn-39); coverage scope.mvp → sufficient;
   new confirmed facts: MVP=bookings by Oct 3; shop phase 2 by ~Dec
 → queue re-scored: top = maintenance expectations (critical, not_started, M10)
Turn 40: asks maintenance question (module continuity + criticality).
```

## 15. Cross-index to the 38 required design dimensions

1 Purpose §1 · 2 Authority §1 · 3 Boundaries §1 · 4 Inputs §1 · 5 Outputs §1 · 6 Preconditions §1 · 7 State model §6 · 8 Phases/modules §5 · 9 Adaptive strategy §7 · 10 Coverage model §4 · 11 Risk-based prioritisation §7.1 (importance×uncertainty scoring; critical topics archetype-independent) · 12 Contradictions §9 · 13 Assumptions §9 · 14 Uncertainty §9 · 15 Confirmation §7.2 (summaries) + §12 · 16 Pause/resume §10 · 17 Completion §11–12 · 18 Failure/escalation §10 · 19 Client language §7.2 · 20 No leading questions §7.2 · 21 No premature solutioning §3, §7.2 · 22 "I don't know" §7.2 · 23 Contradictory stakeholders §9 · 24 Scope expansion §9 · 25 Evidence §8 · 26 State updates §6 · 27 Skills §1 (contracts in `14`) · 28 Rules §1 + `14` · 29 Knowledge §1 · 30 Templates `06` §6 · 31 Schemas §6 + `06` · 32 Tests `02` §10, `10` §8 · 33 Example transitions §14 · 34 Example decision logic §7.1, §14 · 35 Control loop §7.3 · 36 DoR §11 · 37 DoD §12 · 38 Approval points §13.
