---
name: spk-01-smoke
description: S0a-only fixture proving that a skill loads from an added methodology directory.
---

# SPK-01 Smoke Skill

## Purpose

Prove skill discovery from the methodology `--add-dir` without implementing any
production workflow.

## Trigger

The `spk-01-fixture` agent is asked to execute SPK-01.

## Preconditions

- Current working directory is a generated scratch client repository.
- The methodology directory is added read-only by `start-agent.sh`.

## Procedure

1. Create `spk-01-skill-marker.txt` in the client repository.
2. Write exactly `SPK01_SKILL_INVOKED` followed by one newline.
3. Read the marker back and confirm the exact content.

## Output

`spk-01-skill-marker.txt` in the client repository.

## Self-check

The marker exists inside the client repository and nowhere else.

## Failure modes

If the marker cannot be created or differs, report failure and stop.

## Must not

Do not write outside the client repository or perform production project work.
