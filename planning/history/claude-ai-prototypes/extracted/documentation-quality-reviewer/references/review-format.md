# Review Format Reference

Full detail for how to structure a documentation quality review. Load this before producing any review output.

## Input types this skill may receive

Functional PRD, Business Handoff YAML, Technical + UX Discovery Summary, Technical UX Handoff YAML, README.md, 00-init.md, 01-proposal.md, 02-spec.md, 03-design.md, 04-tasks.md, 05-validation.md, 06-rollout.md, client notes, technical notes, existing docs, rough requirements — one or several at once.

## Review dimensions

Check against whichever of these are relevant to what was provided:

1. Baseline clarity
2. Problem and value clarity
3. User and use-case clarity
4. MVP scope clarity
5. Out-of-scope clarity
6. Requirement testability
7. UX readiness
8. Technical readiness
9. Data model readiness
10. Integration readiness
11. Security/privacy/compliance readiness
12. Operational readiness
13. Task coverage
14. Traceability
15. Assumption burden
16. Open question visibility
17. Risk coverage
18. Implementation readiness
19. AI coding agent readiness, when relevant

## Severity levels

- **Critical** — blocks implementation or client validation.
- **High** — likely to cause rework, wrong implementation, or client mismatch.
- **Medium** — should be clarified soon but doesn't fully block progress.
- **Low** — improvement, polish, or documentation quality issue.

## Readiness score

```
1 = not ready
2 = weak, significant discovery or documentation work needed
3 = usable with assumptions and caution
4 = ready with minor clarifications
5 = ready for implementation
```

## Cross-document checks (when reviewing an artifact pack)

- Every major feature in `02-spec.md` appears in `03-design.md` and `04-tasks.md`.
- Every task in `04-tasks.md` traces back to a requirement, design decision, setup need, or risk mitigation.
- Out-of-scope items don't appear as v1 tasks.
- Assumptions aren't written as confirmed requirements.
- Open questions aren't silently resolved between files.
- Risks are reflected in validation and/or rollout documents where relevant.
- Client validation questions and technical validation questions are kept separate.
- Payments, privacy, authentication, migrations, integrations, and operational risks are explicitly addressed when relevant to the project.

## Output format

```markdown
# Documentation Quality Review — {Project Name or Document Set}

## 1. Summary Verdict
Plain-language verdict.

## 2. Readiness Score
Score: X/5
Brief explanation of the score.

## 3. Strengths
What's working well.

## 4. Critical Issues
Blockers or serious risks only.

| Issue | Why it matters | Recommended fix |
|---|---|---|

## 5. High-Priority Gaps
| Gap | Impact | Recommended fix |
|---|---|---|

## 6. Medium/Low Improvements
Practical improvements that are useful but not blocking, grouped.

## 7. Contradictions or Ambiguities
Inconsistencies, conflicting statements, vague wording, unclear decisions.

## 8. Hidden Assumptions
Assumptions that are implied but not clearly labeled as such.

## 9. Open Questions to Resolve
Separate into:
- Client validation needed
- Technical validation needed
- Implementation decision needed
- Deferred to later phase

## 10. Traceability Review
If relevant, check the chain:
PRD/baseline → proposal → spec → design → tasks → verification

## 11. Risk Review
Business, UX, technical, operational, rollout, privacy/security, and integration risks as applicable.

## 12. AI Coding Agent Readiness
Only include when relevant. Check:
- explicit requirements
- clear task IDs
- stable task sequence
- verification criteria
- setup instructions
- dependency clarity
- open questions separated from confirmed work

## 13. Recommended Next Action
One of:
A) Ready to implement
B) Ready with minor clarifications
C) Ask focused questions first
D) Run technical/UX discovery
E) Reduce MVP scope
F) Regenerate artifact pack
G) Return to business discovery
```
