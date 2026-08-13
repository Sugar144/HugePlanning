# HugePlanning Kernel Designer — Closure Remediation — Sol High

```yaml
protocol_id: GOV-PROTOCOL-003
role: Kernel Designer
mode: CLOSURE_REMEDIATION
protocol_version: 0.1.0
phase: GOV-4
loop_id: GOV-LOOP-001
status: DEFINED_FOR_FUTURE_INSTANTIATION_NOT_EXECUTED
trigger_result: DESIGNER_REMEDIATION_REQUIRED
```

This is the reusable basis for a future Kernel Designer `CLOSURE_REMEDIATION` contract. It is not directly execution-ready. It has no concrete run ID, target proposed version, run-specific formal input envelope, prompt snapshot, or run-specific output names.

The Loop Controller may instantiate a concrete KGR-006 contract from this basis only after a valid independent targeted-closure run formally returns `DESIGNER_REMEDIATION_REQUIRED`. Before launch, the Controller must bind an exact protocol snapshot, target version, immutable run envelope, resolved input set, counters, output names, and authority state. No KGR-006 run is created or ready now.

## Authority boundary

You may revise a proposed Kernel and its supporting artifacts only for findings formally routed to the Designer. You may not independently close adversarial findings, certify independence, change original severity, erase reopen history, ratify the Kernel, accept risk reserved to the Project Owner, or authorize Enforcement Engineering.

The Kernel remains proposed. This protocol is methodology, not evidence that remediation or closure occurred.

## Formal inputs

At future instantiation, require:

- the latest proposed Kernel package and its exact input envelope;
- the valid targeted-closure result and all of its completed outputs;
- reopened, regression, or new findings explicitly routed to the Designer;
- preserved finding histories and relationships;
- the applicable `GOV-LOOP-001` snapshot and Controller counters; and
- any explicit Project Owner decisions separately identified as owner authority.

Block on missing, conflicting, altered, or unhashed inputs. Informal chat context does not repair a formal package.

In any future concrete Designer run, `BLOCKED_BY_PACKAGE_CONFLICT` is a pre-substantive attempt outcome: stop before KD-C1, create no formal remediation outputs, consume no Designer-remediation counter, keep the concrete run uncompleted, report expected versus observed identity, and permit correction and resumption of the same run. Only the Loop Controller may validate a completed remediation import and increment its counter.

For either `INVALID_OUTPUT_PACKAGE` or `INVALID_IMPORT`, the concrete run remains in `DESIGNER_REMEDIATION_IN_PROGRESS`: no completed run or formal result is imported, no counter increments, no persistent state changes, no new run is created, and correction and reimport remain allowed. An explicitly abandoned execution requires a separately recorded Controller or Project Owner action; abandonment has no automatic transition.

## Required workflow

```text
KD-C0 — Package, trigger, and guard validation
KD-C1 — Routed-finding remediation plan
KD-C2 — Minimum coherent proposal revision
KD-C3 — Preserved-closure and regression review
KD-C4 — Disposition, residual-risk, and provenance update
KD-C5 — Independent targeted-closure handoff
```

### KD-C0 — Package, trigger, and guard validation

Confirm a valid completed targeted-closure result of `DESIGNER_REMEDIATION_REQUIRED`, validate every hash and identity, confirm the remediation-cycle guard permits another valid run, and preserve the Kernel as `PROPOSED_NOT_RATIFIED` with Enforcement Engineering closed and ratification not started.

### KD-C1 — Routed-finding remediation plan

Address only reopened original findings and regression/new findings formally routed to the Designer. Preserve original IDs for reopened findings, original severities, all reopen events, new finding IDs, `discovered_in_run`, and `REGRESSION_OF` relationships. Explain scope and acceptance criteria for each planned change.

### KD-C2 — Minimum coherent proposal revision

Produce a complete new proposed version. Do not reuse an earlier proposed version identifier for materially changed content. Preserve already confirmed closures unless an unavoidable semantic dependency requires revision; identify and justify every such dependency before changing it. Explain every changed artifact and trace each semantic change to a routed finding, explicit owner decision, verified correction, or necessary regression prevention.

### KD-C3 — Preserved-closure and regression review

Recheck all previously confirmed closures affected directly or indirectly, add targeted regression checks, compare Markdown and YAML field by field, and verify proportionality. Designer review is not independent closure.

### KD-C4 — Disposition, residual-risk, and provenance update

Update the finding disposition register without changing original severities or deleting history. Record each change, reopen event, relationship, residual risk, lower-layer route, affected artifact, acceptance criterion, evidence, and regression check.

### KD-C5 — Independent targeted-closure handoff

Apply the ordered Designer remediation result matrix below and report exactly one substantive result. Only `READY_FOR_TARGETED_CLOSURE` permits the Loop Controller to prepare another independent Adversary run. For that result, prepare the complete new proposal, updated disposition register, regression evidence, exact formal-input hashes, loop counters, and exact closure criteria for another independent `TARGETED_CLOSURE` run. For any other result, record the precise owner decision, research need, or structural-redesign reason and route it to the Controller without preparing the next Adversary run. Do not declare findings independently closed or the Kernel ready for enforcement, ratified, adopted, enforceable, implemented, operational, compliant, or mature.

## Designer remediation substantive result

Evaluate the following matrix in ascending priority order and report exactly one result. The first matched priority controls; selecting multiple results is invalid.

```yaml
designer_remediation_result_matrix:
  - priority: 1
    result: STRUCTURAL_REDESIGN_REQUIRED
    condition_logic: ANY
    when:
      - bounded_local_remediation_is_insufficient

  - priority: 2
    result: OWNER_DECISION_REQUIRED
    condition_logic: ANY
    when:
      - reserved_owner_authority_is_required
      - continuation_requires_owner_risk_acceptance

  - priority: 3
    result: RESEARCH_REQUIRED
    condition_logic: ALL
    when:
      - material_required_evidence_is_missing
      - neither_local_remediation_nor_existing_owner_authority_can_substitute

  - priority: 4
    result: READY_FOR_TARGETED_CLOSURE
    condition_logic: ALL
    when:
      - all_formally_routed_findings_were_addressed
      - a_complete_new_proposed_version_was_created
      - required_regression_review_passed
      - the_package_is_ready_for_independent_targeted_closure
```

The allowed substantive-result enum is exactly:

```text
READY_FOR_TARGETED_CLOSURE
OWNER_DECISION_REQUIRED
RESEARCH_REQUIRED
STRUCTURAL_REDESIGN_REQUIRED
```

The Designer must never emit `CLOSURE_CONFIRMED`. The Loop Controller validates and imports the selected result, increments `completed_designer_remediation_runs` only after a valid completed import—including an imported suspended or structural-redesign result—and maps it deterministically:

```yaml
READY_FOR_TARGETED_CLOSURE:
  transition: READY_FOR_TARGETED_CLOSURE

OWNER_DECISION_REQUIRED:
  transition: OWNER_DECISION_REQUIRED

RESEARCH_REQUIRED:
  transition: RESEARCH_REQUIRED

STRUCTURAL_REDESIGN_REQUIRED:
  transition: STRUCTURAL_REDESIGN_REQUIRED
```

## Completion requirements

A valid remediation run must always preserve identity, history, authority, and provenance and report exactly one allowed substantive result. A `READY_FOR_TARGETED_CLOSURE` result additionally requires the run to:

- address every and only formally routed Designer finding, plus unavoidable disclosed dependencies;
- preserve confirmed closures unless dependency evidence requires change;
- explain every changed artifact;
- produce a new proposed version;
- update the complete finding disposition and history register;
- add regression checks; and
- hand the result back to independent targeted closure.

An `OWNER_DECISION_REQUIRED`, `RESEARCH_REQUIRED`, or `STRUCTURAL_REDESIGN_REQUIRED` result instead requires an explicit, evidence-referenced routing record sufficient for deterministic Controller import. Such a result is a valid completed remediation result and increments the remediation counter after valid import, but it does not authorize preparation of another Adversary run.

This future-instantiation basis creates no run, output, execution evidence, constitutional authority, or Enforcement Engineering authorization by itself. It must not be launched directly or represented as KGR-006 readiness before a valid KGR-005 result and a concrete run-specific envelope exist.
