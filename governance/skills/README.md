---
document_id: GOV-SKILL-CONVENTION-001
version: 0.1.0
status: IMPLEMENTED_LOCALLY_PENDING_REVIEW
authority: skill_custody_convention_not_runtime_or_governance_authority
---

# Governance Skills

Each first-version governance skill lives at `governance/skills/<skill-name>/SKILL.md`, uses lowercase hyphenated identity, declares only `name` and `description` in skill front matter, and is registered with its semantic contract version in `governance/ARTIFACT_REGISTRY.yaml`. Optional `agents/openai.yaml` carries only interface metadata.

This path is repository custody, not active `.claude/skills/` runtime projection. A locally implemented skill is not accepted, operational, formal-run authority, publication authority, or constitutional authority. Contract changes require a semantic version update in the registry and prospective correction; preserved review and execution evidence is never rewritten.
