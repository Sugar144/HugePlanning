---
name: agent-session-reviewer
description: Close a material implementation, formal-run, interruption, failure, or repeated-workflow session by reviewing only observable session evidence for durable improvements. Use when temporary scripts, repeated validation, workflow repetition, ambiguity, near misses, missing controls, or chat-only decisions may be material.
---

# Agent Session Reviewer

Contract version: `0.1.0`.

## Evidence boundary

Review only observable evidence supplied in the transcript or preserved artifacts: commands, tool outputs, files, diffs, test results, explicit corrections, interruptions, and recorded decisions. Never claim access to hidden reasoning or infer facts that the evidence does not support.

## Review

1. Identify only material instances of:
   - temporary scripts worth preserving;
   - repeated workflows or validation;
   - deterministic tool or reusable skill candidates;
   - model work that a deterministic method could replace;
   - prompt ambiguity;
   - failures or near misses;
   - missing tests, schemas, or controls;
   - decisions left only in chat.
2. Cite the observable evidence for each finding and state its impact and evidence limit.
3. Route each finding to exactly one primary durable destination:
   - failure or near miss → learning system;
   - future work → methodology backlog;
   - deterministic repetition → tool proposal;
   - reusable workflow → skill proposal;
   - contract defect → versioned correction.
4. Use one outcome only:
   - `MATERIAL_FINDINGS_IDENTIFIED`;
   - `SESSION_REVIEW_COMPLETE_NO_MATERIAL_FINDINGS`;
   - `INSUFFICIENT_OBSERVABLE_EVIDENCE`.
5. Stop after reporting. Repository modification requires explicit authorization.

## Output

```text
Outcome: <allowed outcome>
Evidence reviewed: <concise scope>
Findings:
- <finding; evidence; impact; evidence limit; destination>
Decisions only in chat: <none or concise list>
Exact next action: <bounded action or none>
```

For a no-findings outcome, write `Findings: none`. For insufficient evidence, name the missing observable evidence without inventing a lesson.

## Must not

- Do not manufacture findings, validate your own findings, preserve trivial transcript details, or treat a transcript as repository truth.
- Do not accept risk, approve, ratify, stage, commit, push, publish, execute a formal run, or modify the repository without explicit authority.
