# Delta Output Format Reference

Full detail for Block 7 output. Load this before generating the Change Delta.

## Output set by change size

**Small changes:**
- Change Request Summary
- Acceptance Criteria
- Task Delta

**Medium changes:**
- Change Request Summary
- Change Impact Assessment
- PRD Delta
- Spec Delta
- Design Delta
- Tasks Delta
- Validation Notes

**Major changes:**
- Change Request Summary
- Change Impact Assessment
- PRD Delta
- Spec Delta
- Design Delta
- Tasks Delta
- Migration/Rollout Notes
- Validation Report

## Output scaling rule

For **small** changes, don't output the full 13-section Change Delta template unless the user actually asks for a full impact assessment. Use only:
- Change Request Summary
- Acceptance Criteria
- Task Delta
- Recommended Next Action

For **medium** and **major** changes, use the full Change Delta template below.

For a change that was classified small but turns out, during the interview, to unexpectedly affect data, integrations, security/privacy, rollout, or multiple workflows — reclassify it as medium or major *before* generating output, and use the corresponding fuller template rather than the small-change shortcut.

## Change Delta template

```markdown
# Change Delta — {Project Name or Change Name}

## 1. Baseline Summary
Describe the current known state.

## 2. Change Summary
Describe what is changing and why.

## 3. Change Classification
Small / Medium / Major. Explain the classification.

## 4. Affected Areas

| Area | Affected? | Notes |
|---|---|---|
| Business requirements | Yes/No | |
| Users | Yes/No | |
| UX/screens | Yes/No | |
| Workflows | Yes/No | |
| Data model | Yes/No | |
| Integrations | Yes/No | |
| Security/privacy | Yes/No | |
| Operations | Yes/No | |
| Rollout/migration | Yes/No | |
| Tests/tasks | Yes/No | |

## 5. Requirements Delta
### Added
### Changed
### Removed
### Unchanged but affected

## 6. Acceptance Criteria
Requirement/scenario style where useful:
- Given...
- When...
- Then...

## 7. UX / Flow Delta
Affected user journeys, screens, states, and edge cases.

## 8. Data / Technical Impact
Separate:
- Confirmed impact
- Assumptions
- Technical recommendations
- Needs client validation
- Open questions

## 9. Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|

## 10. Documentation Updates Needed
Which documents should be updated — PRD, Business Handoff YAML, Technical + UX Summary, README.md, 00-init.md, 01-proposal.md, 02-spec.md, 03-design.md, 04-tasks.md, 05-validation.md, 06-rollout.md. For each: update needed (yes/no), reason, update type (small edit / section update / regenerate).

## 11. Task Delta
Checkbox tasks with stable IDs. Example:
```markdown
- [ ] T-delta-01 Update requirement REQ-order-002.
  - Traceability: REQ-order-002
  - Verification: Updated behavior is covered by scenario SCN-order-003.
```

## 12. Client Validation Questions
Top 5–10 questions, prioritized.

## 13. Recommended Next Action
One of:
A) Apply small documentation update
B) Generate delta docs
C) Regenerate affected artifact files
D) Run technical/UX discovery for this change
E) Reduce scope before accepting the change
F) Validate with client first
G) Proceed to implementation planning
```

## Optional YAML handoff

Include when useful — only fill what actually came up, leave the rest as empty strings/arrays:

```yaml
change_delta_handoff:
  project_name: ""
  change_name: ""
  date: ""
  change_classification: "small | medium | major | unknown"
  baseline_sources: []
  baseline_summary: ""
  change_summary: ""
  change_reason: ""
  requested_by: ""
  affected_users: []
  affected_workflows: []
  affected_screens: []
  requirements_delta:
    added: []
    changed: []
    removed: []
    unchanged_but_affected: []
  acceptance_criteria: []
  data_technical_impact:
    confirmed: []
    assumptions: []
    technical_recommendations: []
    needs_client_validation: []
    open_questions: []
  risks:
    - risk: ""
      impact: ""
      mitigation: ""
  docs_to_update:
    - document: ""
      update_needed: true
      reason: ""
      update_type: "small edit | section update | regenerate"
  task_delta: []
  client_validation_questions: []
  recommended_next_action: ""
```
