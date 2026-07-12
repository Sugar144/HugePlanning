# Artifact Contents Reference

Full required contents for each artifact in the pack. Only generate the files that apply for this project's scale (see the scaling rules in SKILL.md) — this file just defines what goes in each one when it's included.

## README.md
Purpose: index and usage guide for the whole pack.

Must include:
- project name
- short summary
- artifact index
- recommended reading order
- baseline sources
- artifact status
- known caveats
- how to use these documents for implementation
- notes for AI coding agents, if relevant

## 00-init.md
Purpose: project context and baseline assumptions.

Must include:
- project context
- business baseline summary
- technical baseline summary
- users
- MVP boundary
- non-goals
- constraints
- conventions
- assumptions
- risks
- open questions
- artifact status

## 01-proposal.md
Purpose: what should be built and why, at implementation-planning level.

Must include:
- intent
- problem summary
- proposed solution
- scope
- out of scope
- affected areas
- dependencies
- risks
- alternatives considered, if relevant
- success criteria
- rollback or fallback considerations, if relevant

## 02-spec.md
Purpose: testable product/system requirements and behavioral scenarios.

Must include:
- functional requirements
- user scenarios
- acceptance criteria
- business rules
- validation rules
- edge cases
- error states
- non-functional requirements
- explicit out-of-scope items
- open questions

Requirement format:
```
REQ-{area}-{number}: The system MUST/SHOULD ...
```

Scenario format:
```
Given ...
When ...
Then ...
```

## 03-design.md
Purpose: proposed UX and technical design.

Must include:
- design goals
- UX architecture
- screen/view structure
- main flows
- architecture overview
- frontend design
- backend design
- data model
- integrations
- authentication/authorization approach, if relevant
- privacy/security considerations
- error handling
- observability/operations
- testing strategy
- trade-offs
- alternatives considered
- open questions

## 04-tasks.md
Purpose: implementation tasks executable by humans or AI coding agents.

Must include:
- task groups
- ordered implementation sequence
- dependencies between tasks
- frontend tasks
- backend tasks
- data/model tasks
- integration tasks
- testing tasks
- validation tasks
- documentation tasks
- pre-launch checklist
- explicit verification steps

Use checkbox tasks with stable IDs, grouped by area. ID style: `T-init-01`, `T-fe-01`, `T-be-01`, `T-db-01`, `T-int-01`, `T-test-01`, `T-ops-01`, `T-doc-01`, `T-verify-01`.

Each task should include: objective, brief details, dependencies (if any), verification criteria.

Example:
```markdown
## Group: Frontend
- [ ] T-fe-01 Scaffold frontend application.
- [ ] T-fe-02 Build primary user flow.
- [ ] T-fe-03 Build confirmation/result screen.
```

## 05-validation.md
Purpose: readiness, consistency, assumptions, gaps, implementation risk.

Must include:
- coverage review
- consistency check
- traceability review
- readiness score
- assumption burden
- open questions
- risks
- client validation needs
- technical validation needs
- implementation blockers
- recommended next action

Readiness score scale:
```
1 = not ready
2 = weak, significant discovery needed
3 = usable with assumptions
4 = ready with minor clarifications
5 = ready for implementation
```

## 06-rollout.md
Purpose: release, rollout, migration, fallback, operational readiness.

Use when: an existing system is affected, users/data must migrate, payments are involved, external integrations are involved, staged release is needed, operational failure would have real business impact, or compliance/privacy risk is meaningful.

Must include:
- rollout strategy
- release phases
- migration plan, if relevant
- data transition, if relevant
- compatibility concerns
- fallback/rollback plan
- monitoring
- support process
- incident handling
- launch checklist
- post-launch validation

## Cross-Artifact Traceability Rules

Purpose: keep generated artifact packs internally consistent, traceable, and safe for implementation by humans or AI coding agents.

### 1. Feature traceability

Every major feature or capability should trace through the generated artifacts in this direction:

```
PRD / baseline need
→ 01-proposal.md scope item
→ 02-spec.md requirement
→ 03-design.md design decision
→ 04-tasks.md implementation task
→ 05-validation.md coverage check, if included
```

Do not create orphan requirements (not tied to a proposal scope item), orphan design decisions (not tied to a requirement), or orphan tasks (not tied to a requirement, design decision, risk mitigation, or setup need).

### 2. Requirement IDs

Use stable requirement IDs in `02-spec.md`.

Format: `REQ-{area}-{number}`

Examples: `REQ-order-001`, `REQ-payment-001`, `REQ-admin-001`, `REQ-auth-001`, `REQ-notification-001`

### 3. Scenario IDs

Use stable scenario IDs where useful.

Format: `SCN-{area}-{number}`

Examples: `SCN-order-001`, `SCN-payment-001`, `SCN-admin-001`

### 4. Task traceability

Each task in `04-tasks.md` should include a `Traceability` line pointing back to the requirement/scenario IDs it fulfills, whenever those IDs exist.

Example:

```markdown
- [ ] T-fe-01 Build menu browsing screen.
  - Objective: Allow customers to browse available products.
  - Details: Display categories, product names, descriptions, prices, and availability.
  - Dependencies: T-init-01, T-be-02
  - Traceability: REQ-menu-001, SCN-menu-001
  - Verification: User can view products grouped by category on mobile and desktop.
```

### 5. Assumption handling

Assumptions must remain visibly labeled wherever they appear — `00-init.md`, `01-proposal.md`, `02-spec.md`, `03-design.md`, and `05-validation.md` may all legitimately contain assumptions, but an assumption must never be written as a confirmed requirement unless it has actually been validated.

### 6. Open question handling

Open questions must not be silently resolved. Classify each one as:
- Client validation needed
- Technical validation needed
- Implementation decision needed
- Deferred to later phase

### 7. Out-of-scope consistency

Anything listed as out of scope in `01-proposal.md` or `02-spec.md` must not appear as a v1 task in `04-tasks.md`. If an out-of-scope item shows up in the design for context, label it clearly as Future phase, Deferred, or Not implemented in v1.

### 8. Risk propagation

Risks should propagate into the appropriate downstream artifact:

```
Business risk   → 01-proposal.md / 05-validation.md
UX risk         → 03-design.md / 05-validation.md
Technical risk  → 03-design.md / 04-tasks.md / 05-validation.md
Rollout risk    → 06-rollout.md
```

### 9. Validation document

If `05-validation.md` is included, it must explicitly check: baseline coverage, requirement coverage, design coverage, task coverage, assumption burden, open questions, client validation needs, technical validation needs, readiness score, and recommended next action.
