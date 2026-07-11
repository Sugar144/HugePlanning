# 08 — Backlog, Jira, and Traceability

**Purpose:** the two-backlog architecture (product/delivery), the transformation contract, vertical slicing, story/task lifecycles, Git↔Jira authority (Model B), and the traceability model.
**Baseline traceability:** B5, B19, §15; closes G-09, G-14. **V2:** distinct backlog contracts + slicing + separated DoR/DoD + outcome-based sizing (R2-11), field-class authority + profile-scoped Jira (R2-06), content readiness in DoR (R2-18).

---

## 1. Two backlogs, two contracts (R2-11)

### 1a. Product backlog — the value view (layer 2)

**Producer:** `backlog-refinement` skill, product mode, during specification (`07` §7). **Consumers:** technical design, estimation, client phase conversations. **Contains:** epics (per objective), **vertically sliced stories**, use cases where flows are complex, scope **phases**, priorities, acceptance intent (AC references). **Excludes:** technical decomposition, code areas, task sequencing.

**Vertical slicing strategies** (choose per epic; a story must be a demonstrable user/business outcome, never a renamed requirement):
by **workflow** (request booking / manage booking) · by **user role** (visitor vs owner sides) · by **happy path vs exceptions** (US-1: standard booking; US-2: conflicts & cancellations) · by **value increment** (view availability before book online) · by **risk** (riskiest slice first) · by **business-rule cluster** (pricing rules as their own story) · by **integration boundary** (works standalone / syncs to calendar) · by **release phase** · by **walking skeleton** (thinnest end-to-end slice, always first).

### 1b. Delivery backlog — the work view (layer 2)

**Producer:** `backlog-refinement` skill, delivery mode, during technical design (`05`), and per approved CR afterwards. **Consumers:** Jira export (where used), task loop (`09`), release planning. **Contains:** tasks per story with dependencies, code areas, tests required, estimates, risk, `release_target`; spike/chore/fix/docs tasks. Sequencing: walking skeleton first, then risk-descending, then value order (retained from V1).

## 2. Transformation contract (R2-11)

```text
approved requirements ──(product mode: slicing + phasing)──▶ product backlog
product backlog + technical baseline (SDD/ADRs/UX)
                  ──(delivery mode: decomposition)──▶ delivery backlog
```

- **Allowed information loss:** product backlog may omit requirement detail (it references IDs); delivery backlog may omit value narrative (it references stories). Nothing else is dropped — every `must` FR reaches ≥1 story; every story reaches ≥1 task.
- **Traceability:** story `implements: [FR…]`; task `story: US-…`; validated by `validate.sh`.
- **Regeneration triggers:** approved CR touching scope → product backlog first, then delivery backlog for affected stories; technical baseline change (ADR superseded) → delivery backlog re-derivation for affected stories only. Regeneration never renumbers existing IDs.
- **Propagation:** changes flow one direction (requirements → product → delivery → Jira). A discovery made at task level flows back as a CR proposal, never as a direct backlog edit.

## 3. Sizing and lifecycles (R2-11)

**Task sizing — outcome-based reviewability replaces "~1 day":** a task is one coherent, independently reviewable outcome landing as one PR. **Too large:** the diff would mix independent outcomes, review confidence drops, or it can't fail/succeed as a unit — split. **Too small:** its outcome isn't independently verifiable — merge into its sibling. **Belongs together:** changes only correct in combination (schema + code + test for one behaviour). **Always separate:** spikes (`type: spike`, timeboxed), refactors beyond the touched files, cross-cutting NFR work (its own task, e.g. "a11y pass on public flows"). Estimates stay XS–XL as effort signals; XL still forces a split.

### 3a. Story lifecycle

**Story DoR:** implements named approved FRs · sliced to a demonstrable outcome · ACs identified · UX artifacts exist for its flows (per profile, `05` §8) · **content readiness: CNT items `needed_by` this story are `received/approved` or `placeholder_approved` (R2-18)** · phase/release target set.
**Story DoD:** all its tasks `done` · **end-to-end AC demonstration on an integrated build** (E2E test or scripted walkthrough recorded) · story-level docs updated. A completed task set without the demonstration leaves the story `in_progress` — task-done ≠ story-works.

### 3b. Task lifecycle (baseline §13 retained, tightened)

**Task DoR (G4):** goal + linked US/FR/AC ids · ACs concrete and verifiable at the declared level · dependencies merged or scheduled · design refs exist (SDD §, ADR, contract, UX state) · constraints & out-of-scope stated · `tests_required` declared · no open blocking OQ/CLAR · sized per §3.
**Task DoD (G5):** code implemented · declared tests written and green · full relevant suite green · spec + adversarial findings resolved (merged pass on LITE) · risk-triggered specialist review done · docs touched updated · traceability updated · PR approved by you · merged · operational status reconciled (§4). "The agent finished writing code" ≠ done (baseline, verbatim).

## 4. Git ↔ Jira authority — Model B (R2-06)

| Field class | Authority | Jira-editable? | Enters Git history when |
|---|---|---|---|
| Task/story identity (canonical ID), definition, description | **Git** | No — Jira text is a projection; meaning edits happen in Git and re-export | at creation |
| Requirements, ACs | **Git** | No | at creation/approval |
| Dependencies, priority, estimate, release target | **Git** | No | at backlog refinement / CR |
| **Operational workflow status** (To Do/In Progress/In Review/Done) | **Jira while in flight** | Yes — the one Jira-owned field | **Reconciled into the task's `status` field at: PR open, PR merge, batch close, release close** |
| Assignee | Jira (irrelevant solo) | Yes | never (not project truth) |

- **Divergence detection:** MVP = manual spot check at each batch close (statuses in Jira vs `delivery-backlog.yaml`); S9 = reconciliation script listing mismatches. Conflict resolution: for the status field, Jira wins until the defined reconciliation event writes it to Git; for every other field, Git wins unconditionally and the Jira item is re-exported.
- **When Jira is absent (LITE; waived STANDARD):** the `status` field in `delivery-backlog.yaml` is the sole operational authority, updated at the same lifecycle events; `status.sh` renders the board. No behaviour elsewhere in the system may depend on Jira's existence.

## 5. Jira model and export (unchanged mechanics, profile-scoped)

Mapping table retained from V1: EP→Epic, US→Story, TASK/BUG/CR→Task/Bug/Task; canonical ID leads the summary; description carries links + snapshot; labels carry risk/priority. `export-jira.sh` reads `delivery-backlog.yaml` → CSV (REST in S9) → keys captured into `jira-map.yaml` (`canonical ↔ jira key ↔ exported_commit`); re-export is idempotent — mapped items are skipped or flagged "changed since export" with an update list applied manually at MVP.

## 6. Traceability model

`traceability.yaml` stores ID→ID edges only; artifacts hold their own upstream links; the file materializes derived chains + implementation-side facts:

```yaml
links:
  - task: TASK-031
    story: US-014
    implements: [FR-004]
    branch: feature/US-014-booking-endpoint
    pr: 17
    commits: [a1b2c3d]
    tests: [TEST-011, TEST-012]          # definitions (10 §4)
    verified_in: REL-001                  # verification snapshot reference (R2-07)
```

`traceability-validation` (+ `validate.sh`): every `approved` FR reaches ≥1 story, ≥1 task, ≥1 test definition · every merged PR maps to a task · every release manifest lists its tasks and references its verification snapshot · dangling refs = error. Updated at each task merge (part of DoD) and at release close. CR impact analysis = reverse walk (`12` §5).

## 7. G4 batch gate

Before an implementation batch (weekly at MVP; per-task on LITE): pick next tasks by dependency+risk order → story DoR check for newly started stories (incl. content readiness) → task DoR per task → mark `ready` → export/update Jira where used. Record: commit touching backlog (+ jira-map).
