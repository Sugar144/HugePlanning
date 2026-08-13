---
audit_id: GOV-AUD-001
run_id: GOV-AUD-001-P02-R1
pass_id: PASS-02
version: 0.1.0
status: PROPOSED_UNACCEPTED_ARCHITECTURE_MODEL
system_self_hosting_status: NOT_IMPLEMENTED
infrastructure_self_hosting_status: NOT_IMPLEMENTED_OR_SELECTED
---

# Controlled Self-Hosting and Trust Boundaries

## Status

**VERIFIED_FACT:** HugePlanning has used repository governance methods, agents, scripts and reviews to improve governance artifacts. This demonstrates bounded assisted work, not an implemented self-hosting architecture.

**VERIFIED_FACT:** No evidence in the bound inputs demonstrates an operational system that autonomously proposes, validates, independently evaluates, accepts, implements, releases and operates its own changes. No infrastructure self-hosting inventory, service level, graph infrastructure, secrets platform, backup regime or disaster-recovery evidence is established.

**REJECTED:** Describing the current repository workflow as implemented system self-hosting or infrastructure self-hosting.

## System self-hosting definition

**PROPOSAL:** System self-hosting means HugePlanning uses a governed version of its own methodology and controls to propose or execute changes to HugePlanning. It remains controlled only when the trust root, decision authority, evaluation independence, release boundary and recovery path remain outside the changed component's unilateral control.

## Bootstrap trust root

**PROPOSAL:** The minimum immutable or independently controlled trust root contains:

1. the last ratified Kernel version and constitutional decision record;
2. competent human Owner identity and reserved authority;
3. the authority hierarchy and prohibition on self-ratification;
4. exact source-control history and immutable run/evidence custody;
5. a known-good minimal validator and its independently reviewable source;
6. release signing or equivalent release identity when later implemented;
7. recovery instructions that do not depend solely on the failing generated system;
8. offline-readable records of current versions, locks, decisions and rollback boundaries.

**INFERENCE:** Not every file must be physically immutable. The trust requirement is that a proposed self-modification cannot both alter a trust-root element and unilaterally certify the altered element as valid.

**OWNER_DECISION_REQUIRED:** The Project Owner must later identify the exact bootstrap trust-root inventory before any self-hosting implementation.

## Seed versus generated artifacts

| Class | Examples | Authority | Change rule |
|---|---|---|---|
| Seed constitutional artifacts | ratified Kernel, Owner decision, authority hierarchy | Human constitutional authority | versioned amendment, independent challenge and human ratification |
| Seed execution contracts | run authorization, role/mode, prompt, input manifest, release contract | Explicit competent owner | prospective versioned change before execution |
| Generated proposals | architecture candidate, policy draft, code patch, migration proposal | none until accepted | may be regenerated; must identify sources and limitations |
| Generated deterministic views | indexes, relationship projection, status, impact report | derived, non-authoritative | discard and regenerate from canonical sources |
| Generated validation evidence | validator result | bounded claim only | valid only for exact subject, validator and criteria versions |
| Independent evaluation | separate review result | evaluation authority only | produced outside beneficiary's unilateral control |
| Owner decision | acceptance, rejection, return, ratification, risk disposition | competent human authority | explicit append-only decision |
| Released implementation | adopted release bytes and manifest | release authority within scope | separate release gate, rollback and operational evidence |

**REJECTED:** Promoting generated artifacts into seed authority merely because the system produced and validated them successfully.

## Controlled self-hosting sequence

```text
1. proposal generation
2. deterministic validation
3. independent evaluation
4. Project Owner acceptance or return
5. separately authorized implementation
6. separately authorized release
7. bounded operation and evidence collection
```

**PROPOSAL:** No step grants authority for the next. The same model, session, agent, tool, context or beneficiary may participate in multiple low-risk functions only when the contract shows that decisive criteria, evidence, interpretation and acceptance remain outside its unilateral control.

## Independence boundaries

**PROPOSAL:** For a material self-change, record distinct owners for:

- problem and claim definition;
- proposal generation;
- execution or implementation;
- criteria and fixture ownership;
- deterministic validation;
- evaluator appointment and context;
- independent interpretation;
- exception approval;
- acceptance;
- release;
- ratification when constitutional.

**VERIFIED_FACT:** The current governance loop already demonstrates a narrow form of this separation: Designer, Adversary, deterministic Controller and Project Owner have different permitted functions. The Controller cannot decide constitutional substance, and closure is not ratification.

**RECOMMENDATION:** Reuse that functional-separation principle, not the KGR-005 Controller's exact state machine, for later self-hosting design.

## Prohibited circular authority

**REJECTED:** The component being changed selects the only evaluator, controls the decisive evidence set, changes the gate criteria, approves its exception and accepts or releases itself.

**REJECTED:** A generated relationship projection becomes the canonical authority for the sources from which it was generated.

**REJECTED:** A self-hosted validator modifies its own criteria or fixtures and treats previously failing subjects as valid without independent review.

**REJECTED:** Operational success automatically updates policy, methodology, Kernel, risk acceptance or adoption state.

**REJECTED:** A new prompt, model, agent, service or local deployment is treated as independent solely because it has a different name or runtime.

## Self-modification classes

| Class | Example | Proposed minimum control |
|---|---|---|
| Non-normative projection | regenerate an index or impact report | deterministic validation; no source write-back |
| Documentation with no contract change | clarify explanatory prose | source link, drift check and ordinary review |
| Methodology procedure change | modify skill steps or stage contract | versioned change, scenarios, migration and release review |
| Validator or schema change | alter accepted inputs or claims | positive/negative fixtures, old-result impact, independent review proportional to consequence |
| Agent authority or permission change | expand tools, write scope or governed effects | new authority contract, capability evidence and independent evaluation |
| Governance control change | alter prevention, evidence, stopping or recovery | clause/ER traceability, effect-class testing, migration and Owner adoption |
| Constitutional change | alter Kernel meaning or reserved authority | independent challenge and human ratification; no autonomous path |

## Failure, stopping and loop exhaustion

**PROPOSAL:** Self-hosted work stops when:

- authority, canonical input or required context is missing or contradictory;
- a trust-root element is changed without separate review;
- source and projection diverge materially;
- validator, model, tool or provider capability is unavailable for a required claim;
- the correction limit, time, cost, compute or attention budget is exhausted;
- the same blocking finding repeats without net reduction;
- recovery evidence is missing for a potentially irreversible effect;
- independent evaluation cannot be established;
- a lower layer attempts to approve its own authority change.

**PROPOSAL:** A stopped run records owner, reason, affected dependencies, residual effects, evidence state and exact resumption or terminal condition. Starting a new run does not reset cumulative loop exhaustion or related effects.

## Corrupted or contradictory state

**PROPOSAL:** On detected corruption or contradiction:

1. stop dependent governed effects;
2. preserve the maximum safe evidence;
3. identify the last known-good ratified, released and locked versions;
4. compare canonical sources, not generated summaries;
5. classify affected decisions and external effects;
6. restore software/state only when evidence supports restoration;
7. compensate or disposition irreversible effects separately;
8. obtain independent validation and Owner authorization before resumption.

**VERIFIED_FACT:** HP-FAIL-008, HP-FAIL-009, HP-FAIL-020 and HP-FAIL-021 demonstrate that canonical path, replay and cross-surface lifecycle consistency are material recovery concerns.

## Rollback and recovery

**PROPOSAL:** A self-hosting release must preserve:

- prior known-good release and lock;
- exact migration and changed trust-root inventory;
- backup or immutable source history;
- rollback command or manual procedure tested before release;
- residual-effect detection;
- compensation path for non-reversible disclosure, communication, cost or decision effects;
- post-rollback validation and independent review;
- a terminal record if rollback cannot restore the prior condition.

**REJECTED:** Treating repository reset, service rollback or model replacement as proof that all governed effects were reversed.

## Manual fallback

**PROPOSAL:** Every self-hosted function declares a manual fallback that can operate using the offline trust-root records:

- direct inspection of canonical files;
- manual Project Owner authorization and decision record;
- manual validation checklist with preserved evidence;
- release pinning to the previous supported version;
- manual containment, project pause or terminal disposition.

The fallback may be slower and narrower. It may not lower constitutional or evidence floors.

## Tool or model unavailability

**PROPOSAL:** Tool/model unavailability results in one of:

- use a separately validated compatible substitute;
- reduce scope to harmless analysis;
- use the manual fallback;
- remain blocked.

**REJECTED:** Quietly switching model, provider, validator, graph/query infrastructure or execution environment when capability evidence and compatibility are material.

## Infrastructure self-hosting assessment

**VERIFIED_FACT:** The following are infrastructure concerns, not proof of system governance. Their adoption requires a demonstrated gap, separate research, ownership, security, operations and disaster-recovery evidence.

| Infrastructure area | Current evidence | Could be self-hosted later | Required boundary before recommendation | PASS-02 disposition |
|---|---|---|---|---|
| Local models | No bound operational inventory or capability evaluation | yes | model capability, data boundary, update, fallback, evaluation independence | `DEFERRED_RESEARCH_REQUIRED_IF_TRIGGERED` |
| Local runners | Local scripts exist; no governed runner service | yes | identity, permissions, isolation, queue/state recovery and logs | `DEFERRED` |
| Local artifact storage | Git repository custody exists; no general artifact service | yes | retention, integrity, access, backup and recovery objective | `NO_NEW_SERVICE_JUSTIFIED` |
| Databases | No selected architecture database | yes | canonical ownership, migration, backup, security and operator burden | `DEFERRED_NO_DEMONSTRATED_GAP` |
| Graph/query infrastructure | Typed model is proposed; no implementation exists | yes | query need, scale, regeneration, authorization boundary and tool research | `DEFERRED_NO_GRAPH_SELECTION` |
| CI/runtime infrastructure | GitHub-oriented planned runtime exists; no self-hosted CI evidence | yes | availability, secrets, isolation, patching, logs, backup and manual release path | `DEFERRED` |
| Secrets and credentials | Planned external stores; no self-hosted secrets service | yes | threat model, rotation, recovery, least privilege and breach response | `DEFERRED_HIGH_RISK_RESEARCH` |
| Telemetry | No governance telemetry system is implemented | yes | data minimization, purpose, retention, authority and no automatic policy mutation | `DEFERRED` |
| Backups and disaster recovery | Project-level plans exist; no system infrastructure evidence | yes | RPO/RTO, restore test, offsite independence and trust-root recovery | `REQUIRED_BEFORE_ANY_INFRA_SELF_HOSTING` |

**RECOMMENDATION:** The current evidence supports repository-native custody and manual recovery as the baseline, not adoption of self-hosted databases, graph systems, CI, secrets or model infrastructure.

## Separation of system and infrastructure self-hosting

**PROPOSAL:** Evaluate them independently:

- system self-hosting asks whether HugePlanning may safely use its own governed method to change itself;
- infrastructure self-hosting asks who operates models, runners, stores, databases, CI, secrets, telemetry and backups.

A system can use external infrastructure and still be controlled. Infrastructure can be self-hosted while the system remains unable to accept or ratify its own changes.

## Owner decisions

**OWNER_DECISION_REQUIRED:** OD-P02-013 — define the bootstrap trust-root inventory before later self-hosting design.

**OWNER_DECISION_REQUIRED:** OD-P02-014 — define independence requirements by change class and criticality.

**OWNER_DECISION_REQUIRED:** OD-P02-015 — decide whether any future system self-hosting pilot is desirable after independent PASS-02 review; this run does not recommend implementation.

**DEFERRED:** All infrastructure adoption or product selection until a demonstrated gap and later evidence-led tool research.
