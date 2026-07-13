# HugePlanning Governance Role Prompts — Index v0.1

## Purpose

This file records the prompts currently available for the HugePlanning governance-kernel process and prevents planned roles from being mistaken for completed executions.

| Order | Role / execution | Prompt file | Prompt provenance | Execution status | Output status |
|---:|---|---|---|---|---|
| 1 | Kernel Intake Interviewer | `01-kernel-intake-interviewer-prompt-canonical-v0.1.md` | Owner-supplied source plus explicitly marked reconstructed completion | `COMPLETED` | Intake package: `READY_WITH_NON_BLOCKING_QUESTIONS` |
| 2 | Kernel Designer | `02-kernel-designer-prompt-sol-high-v0.1.md` | Exact prompt created for the Designer execution | `COMPLETED` | Designer package: `READY_FOR_ADVERSARIAL_REVIEW` |
| 3 | Kernel Adversary | `03-kernel-adversary-prompt-sol-high-v0.1.md` | Exact prompt created for independent adversarial review | `NOT_STARTED` | No adversarial outputs yet |
| 4 | Enforcement Engineer | No final prompt yet | A short seed exists inside the methodology research document | `PLANNED` | Must be designed after adversarial closure |
| 5 | Human Ratification Owner | No agent prompt required yet | Human constitutional authority | `PLANNED` | Must follow enforcement analysis |
| 6 | Governance Bootstrap / repository organizer | `05-governance-bootstrap-codex-prompt-v0.1.md` | Repository-bootstrap execution contract | `READY_TO_RUN` | Must create only the governance project structure |

## Authority warning

A prompt is an execution instruction, not a ratified governance artifact.

The current Kernel remains:

```text
PROPOSED_NOT_RATIFIED
```

The Adversary prompt existing does not mean that adversarial review has occurred.

The Enforcement Engineer seed must not be treated as a final operational contract.

## Provenance rule

Preserve:

- the prompt actually used;
- its version;
- the execution environment and model when known;
- the exact input package;
- the produced outputs;
- the completion status;
- human interventions;
- limitations.

Do not rely on hidden chain-of-thought as validation evidence. Preserve explicit rationales, decisions, findings, artifacts, transcripts when justified, and execution manifests.
