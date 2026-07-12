# Meeting Pack Format Reference

Full detail for classifying the meeting and structuring the output. Load this before generating any meeting pack.

## Meeting types

Classify the meeting as one of these — it shapes what belongs in the pack:

1. **Discovery follow-up** — clarify open business questions after initial discovery.
2. **MVP validation** — confirm v1 scope, phase 2 items, and out-of-scope items.
3. **UX validation** — validate screens, flows, wording, and the user journey.
4. **Technical risk validation** — validate business-impacting technical decisions (payments, integrations, privacy, operational fallback, rollout).
5. **Scope reduction / negotiation** — explain trade-offs and agree what can wait.
6. **Change request validation** — confirm impact, acceptance criteria, and priority of a requested change.
7. **Demo / approval meeting** — show progress, get feedback, obtain approval for the next step.
8. **Pre-implementation sign-off** — confirm enough decisions are settled to begin implementation.

## Output format

```markdown
# Client Meeting Pack — {Project Name}

## 1. Meeting Goal
The single main goal of the meeting.

## 2. Meeting Type
Classify (from the list above) and explain briefly.

## 3. Recommended Agenda
Time-boxed. Scale the agenda's breadth to the meeting length:
- **≤30 min** — one primary goal only, ≤3 key decisions/questions.
- **45–60 min** — one primary goal + one secondary goal, 5–7 key questions.
- **≥90 min** — broader agenda acceptable, but still cap client-facing questions at 10 unless the user explicitly asked for more.

| Time | Topic | Purpose |
|---|---|---|

## 4. What to Show
Only materials that help the client make decisions. For each:
- What to show
- Why show it
- How to explain it simply

## 5. What Not to Show Yet
Internal or premature materials to avoid. For each:
- What not to show
- Why not yet
- Safer alternative

## 6. Decisions Needed
| Decision | Why it matters | Recommended framing |
|---|---|---|

## 7. Questions to Ask
Maximum 10, prioritized.

| Priority | Question | Why it matters |
|---|---|---|

## 8. Assumptions to Confirm
Assumptions that need client confirmation.

## 9. Risks to Validate
Client-friendly translation of risk.

| Risk | Business impact | Client-friendly wording |
|---|---|---|

## 10. Suggested Talking Points
Practical wording the user can actually say:
- Opening
- Scope framing
- How to present trade-offs
- How to ask for decisions
- Closing

## 11. If the Client Pushes Back
Calm responses for likely objections.

| Client objection | Suggested response |
|---|---|

## 12. Follow-up Outputs After the Meeting
What should be updated afterward — PRD, Business Handoff YAML, Technical + UX Summary, Artifact pack, Scope reduction, Change delta, Tasks, Client approval notes.

## 13. Recommended Next Action
One of:
A) Run business discovery follow-up
B) Run technical/UX discovery
C) Reduce MVP scope
D) Generate artifact pack
E) Update docs with change delta
F) Proceed to implementation planning
G) Send summary email to client
```

## Optional follow-up email draft

Include when useful:

```markdown
# Follow-up Email Draft

Subject:
Body:
```

Rules for the follow-up email: keep it short, confirm decisions, list pending questions, state the next step, avoid technical overload.

## Tone

Client-friendly, clear, calm, pragmatic. Not defensive, not overly technical, not overwhelming.
