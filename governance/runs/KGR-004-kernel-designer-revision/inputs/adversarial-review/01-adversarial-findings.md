---
artifact_id: KA-01
project: HugePlanning
version: 0.1.0-adversarial
status: DESIGNER_REVISION_REQUIRED
adversarial_stage: KA-A5
language: English
date: 2026-07-14
kernel_status: PROPOSED_NOT_RATIFIED
repository_inspection: NOT_PERFORMED
scenario_execution: THOUGHT_EXPERIMENTS_ONLY
---

# HugePlanning Adversarial Findings

## 1. Executive severity table

| Severity | Count | Progression effect |
|---|---:|---|
| CRITICAL | 1 | Blocks Enforcement Engineering until revised and closed. |
| HIGH | 7 | Blocks Enforcement Engineering because the findings would distort control design. |
| MEDIUM | 5 | Requires revision or explicit closure rationale before ratification; current set is included in the Designer return. |
| LOW | 1 | Editorial normalization. |
| OBSERVATION | 1 | Route to enforcement/research; not a wording defect. |


### Blocking conclusion

The proposal is coherent enough to revise, but it is **not ready for Enforcement Engineering**. KA-F-001 permits a lower layer to remove a stated human-only risk-acceptance boundary. Seven HIGH findings create material authority, evidence, liveness, or false-enforceability paths. The correct route is back to the Kernel Designer, followed by a targeted adversarial closure review.

## 2. Complete finding register

| ID | Severity | Short title | Primary disposition |
|---|---|---|---|
| KA-F-001 | CRITICAL | Conditional human-risk reservation permits lower-layer removal of human judgment | DESIGNER_REVISION_REQUIRED |
| KA-F-002 | HIGH | Consequential non-state-changing effects can escape bounded authorization | DESIGNER_REVISION_REQUIRED |
| KA-F-003 | HIGH | The benefiting executor can control the decisive evaluation chain without being the named evaluator | DESIGNER_REVISION_REQUIRED |
| KA-F-004 | HIGH | Claim-specific evidence can validate a narrowed claim while the authorized purpose fails | DESIGNER_REVISION_REQUIRED |
| KA-F-005 | HIGH | Absolute source-evidence preservation conflicts with privacy, security, and required deletion | DESIGNER_REVISION_REQUIRED |
| KA-F-006 | HIGH | Temporary deviations and emergency containment can persist as de facto permanent governance | DESIGNER_REVISION_REQUIRED |
| KA-F-007 | HIGH | BLOCKED and higher-provisional states lack an accountable closure obligation | DESIGNER_REVISION_REQUIRED |
| KA-F-008 | HIGH | ENFORCEABLE can be declared from one weak mechanism because the adoption definition is disjunctive | DESIGNER_REVISION_REQUIRED |
| KA-F-009 | MEDIUM | Markdown and YAML are structurally aligned but not fully semantically equivalent | DESIGNER_REVISION_REQUIRED |
| KA-F-010 | MEDIUM | The requirement to prove every governance burden is recursively burdensome and can be weaponized | DESIGNER_REVISION_REQUIRED |
| KA-F-011 | MEDIUM | A competent human can formally accept without being demonstrably informed | DESIGNER_REVISION_REQUIRED |
| KA-F-012 | MEDIUM | Material assumptions are distinguishable but need not remain current or be revalidated | DESIGNER_REVISION_REQUIRED |
| KA-F-013 | MEDIUM | Fundamental architecture is constitutionally listed but absent from K-001’s operative reservation | DESIGNER_REVISION_REQUIRED |
| KA-F-014 | LOW | FAILED is used as a state without normalization in the declared honest-state vocabulary | EDITORIAL_NORMALIZATION |
| KA-F-015 | OBSERVATION | Technology independence remains contingent on real provider control capabilities | ROUTE_TO_ENFORCEMENT |

## 3. Detailed findings

### KA-F-001 — Conditional human-risk reservation permits lower-layer removal of human judgment

```yaml
finding:
  id: KA-F-001
  title: Conditional human-risk reservation permits lower-layer removal of human judgment
  severity: CRITICAL
  type:
  - ambiguity
  - authority_bypass
  - lower_layer_bypass
  - self_certification
  affected:
    clauses:
    - K-001
    - K-003
    - K-005
    artifacts:
    - 00-kernel-design-basis.md
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 05-lower-layer-routing.md
    hazards:
    - HZ-002
    - HZ-008
    - HZ-012
    - HZ-018
    scenarios:
    - REF-KERNEL-001
    - REF-EVOLUTION-001
    - REF-CORE-004
    - KA-S-017
  exploit_or_failure_path:
    preconditions:
    - A lower-layer policy or evaluator is allowed to decide whether a decision requires human judgment.
    - Automated functions can classify, evaluate, or accept some work.
    steps:
    - Define serious or critical residual-risk acceptance as deterministic because thresholds are encoded.
    - Declare that no human judgment is required for that action family.
    - Use automated evaluation and a non-human acceptance function, while retaining nominal separation between executor
      and evaluator.
    - Represent the result as accepted because K-001 reserves human authority only where human judgment has first
      been declared necessary.
    result: Serious, critical, or constitutional residual risk can be accepted without the competent human authority
      that the design basis says must remain final.
  constitutional_consequence: Human constitutional sovereignty and the stated human C3/C4 acceptance floor can be
    bypassed by a lower-layer definition rather than amended formally.
  confidence: high
  evidence:
  - '00-kernel-design-basis.md §5: “C3/C4 acceptance remains human”.'
  - '02-kernel-v0.1-draft.md, K-001 normative statement: “accept ... residual risk where human judgment is required”.'
  - '05-lower-layer-routing.md, detailed acceptance ownership: preserve human authority for C3/C4.'
  revision_direction: Remove the lower-layer predicate from the human reservation. State the risk/criticality categories
    whose acceptance is always human, and make any narrower automated acceptance boundary explicit, non-self-expanding,
    and amendment-controlled.
  owner_decision_required: false
  enforcement_engineer_note: Do not encode acceptance routing until the constitutional human-only boundary is unambiguous.
    A policy classifier must not be able to decide that the constitutional human gate does not apply.
  disposition_gate:
  - designer_revision
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-002 — Consequential non-state-changing effects can escape bounded authorization

```yaml
finding:
  id: KA-F-002
  title: Consequential non-state-changing effects can escape bounded authorization
  severity: HIGH
  type:
  - omission
  - authority_bypass
  - lower_layer_bypass
  affected:
    clauses:
    - K-002
    - K-006
    - K-007
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 05-lower-layer-routing.md
    - 06-kernel-adversary-handoff.md
    hazards:
    - HZ-008
    - HZ-012
    - HZ-016
    scenarios:
    - REF-CORE-003
    - REF-EXT-001
    - KA-S-009
  exploit_or_failure_path:
    preconditions:
    - An action is technically read-only with respect to a repository or external system.
    - The action can still disclose sensitive data, consume material budget, influence a canonical decision, or
      create irreversible provider exposure.
    steps:
    - Classify the action as read-only and therefore outside K-002’s mandatory authorization sentence.
    - Invoke K-007’s permission for safe read-only investigation.
    - Send data to a provider, generate authoritative advice, or incur material cost without a K-002-quality bound
      on target, effects, criticality, validation, and stop boundary.
    result: A constitutionally significant effect occurs while literal compliance is claimed because no state mutation
      occurred at the target.
  constitutional_consequence: Authority can outrun control for disclosure, access, cost, lock-in, and de facto canonical
    influence even though K-002’s scope lists sensitive data and resource commitments.
  confidence: high
  evidence:
  - '02-kernel-v0.1-draft.md, K-002: “Every state-changing action MUST...”'
  - '02-kernel-v0.1-draft.md, K-007: “Safe read-only investigation MAY continue...”'
  - 06-kernel-adversary-handoff.md §5 identifies read-only exposure, cost, and canonical advice as likely loopholes.
  revision_direction: Apply bounded authorization to constitutionally significant effects, not only target-state
    mutation. Preserve lightweight treatment for genuinely harmless reads, but explicitly include sensitive access/disclosure,
    material resource commitment, external transmission, and outputs that acquire governed authority.
  owner_decision_required: false
  enforcement_engineer_note: The effect taxonomy must distinguish syntactic read-only operations from consequential
    effects. Read-only must not be a blanket allow class.
  disposition_gate:
  - designer_revision
  - enforcement_analysis
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-003 — The benefiting executor can control the decisive evaluation chain without being the named evaluator

```yaml
finding:
  id: KA-F-003
  title: The benefiting executor can control the decisive evaluation chain without being the named evaluator
  severity: HIGH
  type:
  - self_certification
  - specification_gaming
  - authority_bypass
  - lower_layer_bypass
  affected:
    clauses:
    - K-003
    - K-005
    - K-006
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 05-lower-layer-routing.md
    - 06-kernel-adversary-handoff.md
    hazards:
    - HZ-002
    - HZ-003
    - HZ-007
    - HZ-008
    scenarios:
    - REF-CORE-002
    - REF-EVALUATOR-001
    - KA-S-002
    - KA-S-003
  exploit_or_failure_path:
    preconditions:
    - A separate evaluator or accepting human exists nominally.
    - The implementer can choose the evaluator, context, evidence subset, test data, method, prompt, or claim framing.
    steps:
    - The executor leaves the blocking rubric text unchanged.
    - The executor selects a correlated evaluator and supplies only favorable evidence or a constrained context.
    - The separate evaluator produces the decisive report.
    - The final authority accepts based on that report, allowing all actors to claim functional separation.
    result: The executor does not literally “provide” the independent evaluation but still controls its decisive
      inputs and selection.
  constitutional_consequence: Critical work can self-certify through an evaluation proxy, defeating the intended
    independence property.
  confidence: high
  evidence:
  - 02-kernel-v0.1-draft.md, K-003 prohibits the executor from “provid[ing] the decisive independent evaluation”.
  - K-003 says independence dimensions “MUST consider” shared context, criteria, evidence, methods, tools, incentives,
    and authority, but does not prohibit beneficiary control of the chain.
  - 05-lower-layer-routing.md routes evaluator selection and conflict tests below the Kernel.
  revision_direction: 'For critical or materially conflicted work, prohibit unilateral beneficiary control over
    the decisive evaluation chain: evaluator appointment, claim/rubric ownership, evidence set, context, method,
    and interpretation. Keep exact separation mechanisms below the Kernel.'
  owner_decision_required: false
  enforcement_engineer_note: Capture and test control provenance for evaluator selection, evidence inclusion, context
    construction, criteria changes, and final interpretation—not only evaluator identity.
  disposition_gate:
  - designer_revision
  - enforcement_analysis
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-004 — Claim-specific evidence can validate a narrowed claim while the authorized purpose fails

```yaml
finding:
  id: KA-F-004
  title: Claim-specific evidence can validate a narrowed claim while the authorized purpose fails
  severity: HIGH
  type:
  - specification_gaming
  - omission
  - lower_layer_bypass
  affected:
    clauses:
    - K-004
    - K-005
    - K-006
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 05-lower-layer-routing.md
    hazards:
    - HZ-001
    - HZ-003
    - HZ-018
    scenarios:
    - REF-CORE-004
    - REF-EVID-001
    - KA-S-004
    - KA-S-010
  exploit_or_failure_path:
    preconditions:
    - The executor or evaluation policy can define the claim under review.
    - The canonical objective contains broader purpose or downstream obligations.
    steps:
    - Define a narrow claim such as “the file is structurally valid” instead of “the artifact satisfies its intended
      operational purpose”.
    - Provide strong evidence for the narrow claim.
    - Record the narrow claim as passed.
    - Use the passed result to support completion, release, or qualified acceptance of the broader work.
    result: Evidence is sufficient for the stated claim but the claim is not sufficient for the actual gate.
  constitutional_consequence: K-005’s evidence requirement can be satisfied while purpose satisfaction and roadmap
    integrity are lost.
  confidence: high
  evidence:
  - '02-kernel-v0.1-draft.md, K-005: evidence must be sufficient “for the specific claim”.'
  - K-005 rejects structural validity alone but does not require every acceptance/release claim to be traceable
    to canonical purpose and mandatory dependencies.
  - K-005 exception posture uses “core purpose” without defining how it is derived.
  revision_direction: Require acceptance, release, completion, and compliance claims to be traceable to the canonical
    authorized objective, mandatory criteria, and material dependencies. A scoped claim may pass only with an equally
    scoped state that cannot imply broader acceptance.
  owner_decision_required: false
  enforcement_engineer_note: Implement claim-to-objective and claim-to-gate traceability. Prevent a local PASS from
    automatically satisfying a broader state transition.
  disposition_gate:
  - designer_revision
  - enforcement_analysis
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-005 — Absolute source-evidence preservation conflicts with privacy, security, and required deletion

```yaml
finding:
  id: KA-F-005
  title: Absolute source-evidence preservation conflicts with privacy, security, and required deletion
  severity: HIGH
  type:
  - contradiction
  - liveness_failure
  - lower_layer_bypass
  affected:
    clauses:
    - K-004
    - K-007
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 04-designer-open-questions.md
    - 05-lower-layer-routing.md
    hazards:
    - HZ-006
    - HZ-012
    - HZ-018
    scenarios:
    - REF-EMERGENCY-001
    - KA-S-012
  exploit_or_failure_path:
    preconditions:
    - Material source evidence contains secrets, personal data, harmful payloads, or data subject to a valid deletion
      obligation.
    - Preserving the raw evidence increases ongoing harm or violates an applicable obligation.
    steps:
    - 'K-004 is applied literally: no exception permits deletion of material source evidence.'
    - 'K-007 containment is applied: preserve evidence “where possible”.'
    - The operator must either retain dangerous/forbidden material and violate containment/privacy, or delete it
      and violate K-004.
    result: The Kernel produces contradictory duties at the moment of highest sensitivity.
  constitutional_consequence: Enforcement can become impossible, illegal, or unsafe; actors may hide deletion or
    ignore provenance to escape the contradiction.
  confidence: high
  evidence:
  - '02-kernel-v0.1-draft.md, K-004 exception posture: “No exception permits ... deletion of material source evidence”.'
  - K-007 emergency posture requires preserving evidence “where possible”.
  - 04-designer-open-questions.md OQ-010 leaves privacy, retention, and consent obligations unresolved.
  revision_direction: Protect evidentiary integrity rather than unconditional raw retention. Permit competent, documented,
    least-loss redaction, isolation, cryptographic attestation, or deletion when required by law, privacy, security,
    or active-harm containment, while preserving the decision record and maximum safe provenance.
  owner_decision_required: false
  enforcement_engineer_note: Retention controls need conflict handling, data minimization, legal/security holds,
    deletion attestations, and safe provenance substitutes. Wording alone cannot determine applicable law.
  disposition_gate:
  - designer_revision
  - research
  - enforcement_analysis
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-006 — Temporary deviations and emergency containment can persist as de facto permanent governance

```yaml
finding:
  id: KA-F-006
  title: Temporary deviations and emergency containment can persist as de facto permanent governance
  severity: HIGH
  type:
  - lower_layer_bypass
  - self_amendment
  - liveness_failure
  - specification_gaming
  affected:
    clauses:
    - K-001
    - K-002
    - K-006
    - K-007
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 05-lower-layer-routing.md
    hazards:
    - HZ-008
    - HZ-012
    - HZ-016
    - HZ-018
    scenarios:
    - REF-EXCEPTION-001
    - REF-EMERGENCY-001
    - KA-S-007
    - KA-S-008
  exploit_or_failure_path:
    preconditions:
    - A deviation has a review condition instead of a hard expiry, or an emergency containment is periodically reviewed.
    - Each individual continuation is documented and approved.
    steps:
    - Authorize a temporary deviation with a monthly review condition.
    - At each review, renew or replace it with a substantially equivalent deviation.
    - Alternatively, keep a component isolated or an emergency authority path active indefinitely because review
      continues.
    - Treat each period as temporary and avoid evaluating the cumulative governance effect.
    result: Temporary machinery becomes the normal operating constitution without a policy replacement or amendment.
  constitutional_consequence: Lower layers can create enduring authority, control, or liveness changes while formally
    denying that any permanent change occurred.
  confidence: high
  evidence:
  - K-002 permits “expiry or review condition”, allowing review to substitute for expiry.
  - K-007 requires record and review but no bounded continuation or cumulative-renewal rule.
  - K-001 prohibits permanent weakening and indefinite risk acceptance, but not all indefinite emergency operating
    states.
  revision_direction: Treat repeated renewal and continued emergency state as cumulative material effect. Require
    a bounded continuation decision, explicit non-emergency disposition, and formal amendment when the continuing
    state changes constitutional authority or protections. A new record must not reset the cumulative clock.
  owner_decision_required: false
  enforcement_engineer_note: Track exception lineage and aggregate duration/effect. Block expired or endlessly renewed
    exceptions from being treated as fresh isolated approvals.
  disposition_gate:
  - designer_revision
  - enforcement_analysis
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-007 — BLOCKED and higher-provisional states lack an accountable closure obligation

```yaml
finding:
  id: KA-F-007
  title: BLOCKED and higher-provisional states lack an accountable closure obligation
  severity: HIGH
  type:
  - liveness_failure
  - omission
  - disproportionate_burden
  affected:
    clauses:
    - K-006
    - K-007
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 04-designer-open-questions.md
    - 05-lower-layer-routing.md
    hazards:
    - HZ-004
    - HZ-005
    - HZ-013
    scenarios:
    - REF-CORE-001
    - REF-CORE-005
    - KA-S-014
  exploit_or_failure_path:
    preconditions:
    - A material uncertainty or conflict causes a legitimate BLOCKED state.
    - No actor is constitutionally required to own resolution, review, abandonment, or supersession.
    steps:
    - Raise uncertainty and apply the higher reasonable provisional level.
    - Block the dependent transition.
    - Escalate once, satisfying the general handling rule.
    - Leave the item blocked indefinitely, with no next review, terminal disposition, or responsibility record.
    result: Safe stopping becomes silent abandonment or a permanent high-control state.
  constitutional_consequence: The Kernel can protect safety by making useful action impossible while remaining literally
    compliant.
  confidence: high
  evidence:
  - K-007 lists repeated pause/block without progress only as a review trigger.
  - The general violation rule requires escalation but not accountable closure.
  - 05-lower-layer-routing.md asks lower layers to avoid turning uncertainty into permanent blocking, showing the
    unresolved liveness dependency.
  revision_direction: Require every material BLOCKED, PAUSED, or higher-provisional state to have an accountable
    owner, reason, dependency, next review or explicit terminal disposition, and preserved authority to remain blocked
    when safety still requires it. Do not impose an unsafe automatic deadline to proceed.
  owner_decision_required: false
  enforcement_engineer_note: The state machine must reject unowned or stale blocked states and distinguish safe
    continued blocking from forgotten work.
  disposition_gate:
  - designer_revision
  - enforcement_analysis
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-008 — ENFORCEABLE can be declared from one weak mechanism because the adoption definition is disjunctive

```yaml
finding:
  id: KA-F-008
  title: ENFORCEABLE can be declared from one weak mechanism because the adoption definition is disjunctive
  severity: HIGH
  type:
  - ambiguity
  - specification_gaming
  - cross_artifact_mismatch
  affected:
    clauses:
    - K-005
    - K-007
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    hazards:
    - HZ-003
    - HZ-008
    - HZ-018
    scenarios:
    - KA-S-017
  exploit_or_failure_path:
    preconditions:
    - At least one control category exists, such as logging.
    - Other necessary prevention, stopping, authorization, or recovery controls are missing.
    steps:
    - 'Point to the definition: ENFORCEABLE means minimum prevention, detection, evidence, stopping, “or” recovery
      mechanisms exist.'
    - Demonstrate one minimal logging mechanism.
    - Declare the Kernel ENFORCEABLE and use that state to justify a governed pilot.
    result: A status that implies executable governance is achieved without a constitutionally adequate control
      set.
  constitutional_consequence: False enforceability can propagate into operation, acceptance, and external effects
    despite K-005’s evidence language.
  confidence: high
  evidence:
  - 02-kernel-v0.1-draft.md §7 defines ENFORCEABLE using “prevention, detection, evidence, stopping, or recovery”.
  - 03-kernel-clauses.yaml repeats the same disjunctive definition.
  revision_direction: Define ENFORCEABLE as the minimum constitutionally necessary combination of prevention, detection,
    evidence, stopping, and recovery capabilities applicable to the governed effect classes, supported by independent
    evidence. Avoid requiring every mechanism where inapplicable.
  owner_decision_required: false
  enforcement_engineer_note: Do not build a boolean enforceable flag from the presence of any single control family.
    Use clause/effect coverage and capability evidence.
  disposition_gate:
  - designer_revision
  - enforcement_analysis
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-009 — Markdown and YAML are structurally aligned but not fully semantically equivalent

```yaml
finding:
  id: KA-F-009
  title: Markdown and YAML are structurally aligned but not fully semantically equivalent
  severity: MEDIUM
  type:
  - cross_artifact_mismatch
  - contradiction
  - editorial
  affected:
    clauses:
    - K-006
    - K-007
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    hazards:
    - HZ-004
    - HZ-006
    - HZ-018
    scenarios:
    - REF-CORE-005
  exploit_or_failure_path:
    preconditions:
    - A human reviewer relies on Markdown while tooling relies on YAML.
    steps:
    - Apply the Markdown general violation rule, which preserves demonstrably independent unrelated work.
    - Apply the YAML rule, which omits that carve-out and may over-block.
    - 'Apply K-006: Markdown says burdensome governance SHOULD be simplified, while YAML states it is simplified.'
    - 'Apply K-007 emergency wording: Markdown requires the least effect reasonably available; YAML says the “least
      reasonable effect”.'
    result: Different authoritative forms can produce different blocking, simplification, and containment behavior.
  constitutional_consequence: The registry cannot safely serve as a machine-readable equivalent until kernel-wide
    semantics and modal force are normalized.
  confidence: high
  evidence:
  - 03-kernel-clauses.yaml general_violation_rule omits the Markdown sentence preserving independent unrelated work.
  - 'K-006 violation: Markdown uses SHOULD; YAML uses an unconditional present-tense outcome.'
  - 'K-007 exception: “least effect reasonably available” versus “least reasonable effect”.'
  - YAML also omits the Markdown same-level supersession rule and several interpretation details.
  revision_direction: Create an explicit semantic parity checklist and align all kernel-wide rules, modal force,
    exception language, and adoption definitions. Either encode omitted interpretation rules in YAML or declare
    the registry intentionally non-authoritative and constrain its use.
  owner_decision_required: false
  enforcement_engineer_note: Do not generate enforcement solely from YAML until parity is verified. Tooling must
    know which representation is authoritative if divergence reappears.
  disposition_gate:
  - designer_revision
  - editorial_normalization
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-010 — The requirement to prove every governance burden is recursively burdensome and can be weaponized

```yaml
finding:
  id: KA-F-010
  title: The requirement to prove every governance burden is recursively burdensome and can be weaponized
  severity: MEDIUM
  type:
  - disproportionate_burden
  - liveness_failure
  - specification_gaming
  affected:
    clauses:
    - K-003
    - K-006
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 05-lower-layer-routing.md
    hazards:
    - HZ-004
    - HZ-005
    - HZ-010
    scenarios:
    - REF-BUREAUCRACY-001
    - KA-S-020
  exploit_or_failure_path:
    preconditions:
    - Every added governance component must demonstrate value over a simpler alternative.
    - Producing that demonstration itself adds an artifact, review, or metric.
    steps:
    - Add a small safety control.
    - Create evidence to justify the control.
    - Demand justification for the evidence artifact and its review process.
    - Alternatively, let the beneficiary challenge a necessary control as unjustified and become the effective simplification
      authority.
    result: The anti-bureaucracy clause creates proof recursion or a route to pressure controls downward.
  constitutional_consequence: 'Solo-owner maintainability can fail in either direction: governance inflation or
    unsafe simplification.'
  confidence: high
  evidence:
  - 'K-006: “Every added governance component or burden MUST demonstrate protective value over a simpler adequate
    alternative”.'
  - 05-lower-layer-routing.md routes complexity metrics and governance reviews, adding further machinery to prove
    the clause.
  revision_direction: Apply the demonstration duty proportionally to material, recurring, or permanent burdens and
    to contested controls. Clarify that the proponent of a burden supplies proportional rationale, while removal
    of a protection must independently show the simpler alternative remains adequate.
  owner_decision_required: false
  enforcement_engineer_note: Cost and protective-value evidence should be sampled and risk-based, not required as
    a bespoke proof artifact for every minor control.
  disposition_gate:
  - designer_revision
  - policy
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-011 — A competent human can formally accept without being demonstrably informed

```yaml
finding:
  id: KA-F-011
  title: A competent human can formally accept without being demonstrably informed
  severity: MEDIUM
  type:
  - omission
  - specification_gaming
  - self_certification
  affected:
    clauses:
    - K-001
    - K-003
    - K-005
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 06-kernel-adversary-handoff.md
    hazards:
    - HZ-002
    - HZ-003
    - HZ-018
    scenarios:
    - REF-CORE-004
    - KA-S-018
  exploit_or_failure_path:
    preconditions:
    - The accepting human has the correct role or identity.
    - Evidence, limitations, or residual risk are too voluminous, hidden, or summarized misleadingly.
    steps:
    - Present an approval button or short summary.
    - Record the human click as competent acceptance.
    - Retain detailed evidence elsewhere without showing that the human received or understood the material decision
      basis.
    result: Human presence becomes ceremonial rather than meaningful authority.
  constitutional_consequence: The system can claim human sovereignty and independent acceptance while the decisive
    judgment was effectively made by the producing system.
  confidence: medium
  evidence:
  - K-005 requires acceptance by competent authority but does not require an informed, attributable decision based
    on material evidence.
  - 06-kernel-adversary-handoff.md warns that a click or brief approval may be recorded as informed acceptance.
  revision_direction: 'Require high-consequence human acceptance to be informed and attributable: material evidence,
    known limitations, residual risk, claim scope, and dissent must be presented in a comprehensible form. Keep
    interface and record details below the Kernel.'
  owner_decision_required: false
  enforcement_engineer_note: Capture the decision packet shown to the human and the exact scope accepted; do not
    infer comprehension solely from identity or a click.
  disposition_gate:
  - designer_revision
  - enforcement_analysis
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-012 — Material assumptions are distinguishable but need not remain current or be revalidated

```yaml
finding:
  id: KA-F-012
  title: Material assumptions are distinguishable but need not remain current or be revalidated
  severity: MEDIUM
  type:
  - omission
  - liveness_failure
  - lower_layer_bypass
  affected:
    clauses:
    - K-004
    - K-005
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 05-lower-layer-routing.md
    hazards:
    - HZ-001
    - HZ-015
    - HZ-018
    scenarios:
    - REF-CORE-001
    - REF-INTENT-001
    - KA-S-001
  exploit_or_failure_path:
    preconditions:
    - A material assumption is correctly labeled as an assumption.
    - No expiry, owner, or revalidation condition is assigned.
    steps:
    - Use the labeled assumption to continue dependent planning.
    - Never promote it to a fact or human decision, preserving literal epistemic labels.
    - Allow it to persist across time or repeated local work without a stage transition.
    result: A stale assumption remains the de facto basis of the system indefinitely without violating the prohibition
      on silent promotion.
  constitutional_consequence: Intent and requirements can drift while the package remains formally honest about
    epistemic type.
  confidence: high
  evidence:
  - K-004 requires assumptions to remain distinguishable but not current.
  - K-004 lists assumption expiry as a review trigger without requiring a material assumption to have expiry or
    revalidation conditions.
  - 05-lower-layer-routing.md expects expiry fields, but a lower layer could omit them without a direct constitutional
    breach.
  revision_direction: Require material assumptions that support state-changing or acceptance decisions to have accountable
    ownership and a validity/revalidation condition, and to block dependent gates when materially stale or contradicted.
  owner_decision_required: false
  enforcement_engineer_note: Track assumption dependencies and staleness. Do not treat a correctly labeled but expired
    assumption as safe input.
  disposition_gate:
  - designer_revision
  - policy
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-013 — Fundamental architecture is constitutionally listed but absent from K-001’s operative reservation

```yaml
finding:
  id: KA-F-013
  title: Fundamental architecture is constitutionally listed but absent from K-001’s operative reservation
  severity: MEDIUM
  type:
  - cross_artifact_mismatch
  - ambiguity
  - authority_bypass
  affected:
    clauses:
    - K-001
    artifacts:
    - 01-kernel-admission-analysis.md
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 06-kernel-adversary-handoff.md
    hazards:
    - HZ-008
    - HZ-017
    scenarios:
    - REF-EVOLUTION-001
    - KA-S-019
  exploit_or_failure_path:
    preconditions:
    - A lower-layer architecture change is described as not changing purpose, scope, authority hierarchy, maximum
      permissions, or an explicitly named protection.
    - The change nonetheless restructures control concentration, canonical flow, or evaluation topology.
    steps:
    - Point to K-001’s scope and review triggers, which mention fundamental architecture.
    - Point to the normative reservation, which does not expressly reserve architecture changes.
    - Proceed as an ordinary architecture decision after conducting a review but without constitutional amendment.
    result: The package can claim the review trigger was observed while the operative prohibition never applied.
  constitutional_consequence: The constitutional boundary depends on non-normative scope text and an undefined adjective
    “fundamental”.
  confidence: high
  evidence:
  - 01-kernel-admission-analysis.md includes fundamental architecture in K-001’s admitted family.
  - 02-kernel-v0.1-draft.md K-001 scope/review triggers include architecture; its normative statement reserves purpose
    or scope but not architecture.
  - 03-kernel-clauses.yaml reproduces the same structure.
  revision_direction: Either add a narrowly defined architecture-effect category to the operative reservation or
    remove architecture as an independent constitutional category and state that architecture is constitutional
    only when it changes authority, autonomy, protected effects, or guarantees.
  owner_decision_required: false
  enforcement_engineer_note: Do not gate every architecture change as constitutional. The Designer must first make
    the semantic boundary enforceable.
  disposition_gate:
  - designer_revision
  disposition: DESIGNER_REVISION_REQUIRED
```

### KA-F-014 — FAILED is used as a state without normalization in the declared honest-state vocabulary

```yaml
finding:
  id: KA-F-014
  title: FAILED is used as a state without normalization in the declared honest-state vocabulary
  severity: LOW
  type:
  - editorial
  - traceability
  - cross_artifact_mismatch
  affected:
    clauses:
    - K-005
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 03-kernel-clauses.yaml
    - 05-lower-layer-routing.md
    hazards:
    - HZ-003
    scenarios: []
  exploit_or_failure_path:
    preconditions:
    - A lower-layer state machine is derived from the listed honest states.
    steps:
    - Derive allowed states from §4.5 or YAML honest_states.
    - Encounter K-005’s violation effect, which returns a result to FAILED.
    - Choose inconsistent local meanings or reject the transition.
    result: State vocabulary is needlessly ambiguous.
  constitutional_consequence: Localized implementation inconsistency, not an independent constitutional bypass.
  confidence: high
  evidence:
  - FAILED appears in K-005’s violation effect.
  - FAILED does not appear in the kernel-wide honest_states list.
  revision_direction: Normalize FAILED as an illustrative lower-layer non-accepted state, add it to the declared
    vocabulary, or remove it from the constitutional example.
  owner_decision_required: false
  enforcement_engineer_note: Resolve before implementing the state machine.
  disposition_gate:
  - editorial_normalization
  disposition: EDITORIAL_NORMALIZATION
```

### KA-F-015 — Technology independence remains contingent on real provider control capabilities

```yaml
finding:
  id: KA-F-015
  title: Technology independence remains contingent on real provider control capabilities
  severity: OBSERVATION
  type:
  - technology_assumption
  - enforceability_dependency
  affected:
    clauses:
    - K-002
    - K-003
    - K-004
    - K-007
    artifacts:
    - 02-kernel-v0.1-draft.md
    - 04-designer-open-questions.md
    - 05-lower-layer-routing.md
    - 06-kernel-adversary-handoff.md
    hazards:
    - HZ-005
    - HZ-007
    - HZ-012
    - HZ-013
    - HZ-017
    scenarios:
    - KA-S-013
  exploit_or_failure_path:
    preconditions:
    - A provider lacks reliable stopping, context export, permission scoping, audit logs, deletion guarantees, or
      evaluator isolation.
    steps:
    - Keep constitutional wording provider-neutral.
    - Substitute the provider without validating capability parity.
    - Attempt to enforce stopping, provenance, independence, or recovery that the provider cannot expose.
    result: The Kernel remains semantically valid but cannot be made enforceable for that environment.
  constitutional_consequence: This is a capability evidence gap, not a reason to add provider names to the constitution.
  confidence: high
  evidence:
  - 02-kernel-v0.1-draft.md §4.4 allows substitution unless guarantees change.
  - 04-designer-open-questions.md OQ-014 and 06 handoff identify provider capability gaps.
  revision_direction: No constitutional expansion is required. Preserve the substitution trigger and require capability
    evidence before claiming equivalent enforcement or portability.
  owner_decision_required: false
  enforcement_engineer_note: Build a provider capability profile and fail closed for effect classes whose constitutional
    controls cannot be demonstrated.
  disposition_gate:
  - enforcement_analysis
  - research
  disposition: ROUTE_TO_ENFORCEMENT
```


## 4. Clause-level attack summary

### K-001 — Constitutional Sovereignty and Governed Amendment

- **Failure:** KA-F-001. The phrase `where human judgment is required` lets a lower layer decide whether the human constitutional gate exists.
- **Weakness:** KA-F-006. Emergency or temporary machinery can persist through repeated review.
- **Internal inconsistency:** KA-F-013. Fundamental architecture is in scope and triggers but not in the operative reservation.
- **Retained strength:** ordinary instructions, system outputs, and emergency action are expressly denied amendment authority; the prior valid constitutional state remains controlling.

### K-002 — Bounded Authority and Effects

- **Failure:** KA-F-002. The operative boundary is state change, not all constitutionally significant effects.
- **Weakness:** broad standing authorization remains enforceability-sensitive, but the clause does require objective, target, effects, criticality, validation, and stop boundaries and rejects authorization by silence or credentials.
- **Retained strength:** material basis change and cumulative classification provide a credible constitutional basis against task fragmentation when enforced.

### K-003 — Functional Independence and Non-Self-Certification

- **Failure:** KA-F-003. A beneficiary can control evaluator selection and the decisive inputs while another actor is the named evaluator.
- **Weakness:** KA-F-011. A human acceptance step may be ceremonial if the decision basis is not presented meaningfully.
- **Retained strength:** nominal separation is explicitly rejected, and shared context, criteria, evidence, methods, tools, incentives, and authority are recognized as correlation dimensions.

### K-004 — Canonical Intent, Provenance, and Epistemic Integrity

- **Failure:** KA-F-005. Absolute raw-evidence preservation conflicts with privacy/security/deletion duties.
- **Weakness:** KA-F-012. Assumptions may remain correctly labeled but indefinitely stale.
- **Retained strength:** silent supersession, fabricated retrospective compliance, and promotion of an inference into a human decision are clearly prohibited.

### K-005 — Evidence-Grounded State and Acceptance

- **Failure:** KA-F-004. Evidence sufficiency can attach to an underscoped claim rather than the real gate.
- **Failure:** KA-F-008. The ENFORCEABLE adoption definition can be satisfied by one weak mechanism.
- **Weakness:** KA-F-011. Competent acceptance is not expressly informed acceptance.
- **Normalization:** KA-F-014. `FAILED` is not in the declared state vocabulary.
- **Retained strength:** artifact existence, structural validity alone, and absence of detected failure are expressly rejected as proof of purpose satisfaction.

### K-006 — Proportional Governance and Justified Complexity

- **Liveness failure:** KA-F-007. Higher-provisional control can become indefinite without accountable closure.
- **Burden weakness:** KA-F-010. Every small governance burden can require recursive justification.
- **Retained strength / no separate finding:** cumulative related effect, anti-fragmentation, and the ban on using proportionality to waive other essential clauses are constitutionally useful and should remain.

### K-007 — Safe Stopping, Observability, Continuity, and Recovery

- **Failure interaction:** KA-F-002. The read-only continuation language is not paired with K-002-quality effect bounds.
- **Failure interaction:** KA-F-005. Evidence preservation and active-harm/privacy deletion are unresolved.
- **Liveness failure:** KA-F-006 and KA-F-007. Emergency state and blocked state can persist without adequate disposition semantics.
- **Retained strength / no separate finding:** interrupted work, ambiguous residual state, and failed recovery are correctly denied accidental acceptance.

## 5. Cross-clause and hierarchy attack

### 5.1 Kernel versus explicit current human decisions

The hierarchy is defensible only because human decisions are limited to those “within constitutional authority.” A normal human instruction cannot formally amend the Kernel. The larger bypass is indirect: lower layers can define whether human judgment is required, what claim is being accepted, what evidence is applicable, and whether a provider is equivalent. KA-F-001, KA-F-004, and KA-F-011 close those indirect authority paths.

### 5.2 Amendment versus emergency and exception

K-001 correctly denies amendment by emergency. However, K-002’s `expiry or review condition` and K-007’s review-only emergency posture permit serial continuation that never becomes formally permanent. KA-F-006 treats cumulative continuation as the constitutional object.

### 5.3 Independence versus solo ownership

The Kernel does not require permanent separate agents, which is proportionate. The defect is not role consolidation itself; it is control of the decisive evaluation chain. A solo owner may obtain meaningful separation through criteria fixed before execution, independent evidence channels, method diversity, delayed review, external review, or non-beneficiary acceptance. Exact methods remain lower-layer work, but K-003 must prevent the beneficiary from choosing all decisive conditions.

### 5.4 Canonical authority versus distributed truth

The phrase “identifiable canonical authority” can support a file, registry, graph, or resolved set. The Kernel should not require a monolith. No new clause is needed. Lower-layer standards should make authoritative boundaries and composition explicit, while KA-F-012 ensures material assumptions do not become permanent inputs merely because they remain labeled.

### 5.5 Evidence sufficiency versus specification gaming

K-004 preserves canonical intent and K-005 requires claim-specific evidence, but the connection between them is not normative enough. KA-F-004 requires the claim used for a gate to cover the canonical objective and dependencies of that gate. This is the principal specification-gaming closure.

### 5.6 Proportionality versus constitutional floors

K-006 expressly states that it must not waive another clause’s essential protection. No finding rejects this architecture. Enforcement must still prevent criticality self-lowering and aggregate changes across branches, actors, stages, and time.

### 5.7 Stopping versus liveness

Safe stopping is constitutionally necessary. KA-F-007 does not demand automatic progress or unsafe timeouts; it requires accountable ownership and review/disposition so that `BLOCKED` is an honest managed state rather than forgotten work.

### 5.8 Privacy/security containment versus evidence preservation

K-004’s absolute raw-retention wording conflicts with K-007’s “where possible” qualifier and the open legal/privacy work. The constitution should preserve integrity and accountability under least-loss handling, not force retention of harmful or forbidden data.

### 5.9 Technology independence versus capability realism

No provider name belongs in the Kernel. KA-F-015 is deliberately an observation: the constitutional semantics can remain provider-neutral, while enforceability and substitution claims require provider capability evidence.

### 5.10 Migration and retrospective regularization

K-004 and K-005 adequately prohibit fabricated contemporaneous evidence and automatic historical compliance. Retrospective reconstruction may support a current decision only when its retrospective nature, limitations, and provenance remain explicit. Scenario KA-S-015 passes at wording level.

## 6. Minimality and omission conclusion

- No eighth clause is justified by this review.
- No existing clause must be split to close the findings.
- K-007 is broad, but stopping, continuity, observability, and recovery share a coherent violation direction and may remain combined.
- K-001/K-003 and K-004/K-005 should not be merged; their authority and violation semantics differ.
- The seven-clause architecture can remain if the operative boundaries and cross-clause links are revised.

## 7. Final finding disposition

```text
CRITICAL unresolved: 1
HIGH unresolved: 7
Status: DESIGNER_REVISION_REQUIRED
Owner decision required now: NO
Ready for Enforcement Engineering: NO
```
