---
prompt_id: HP-PROMPT-030
version: 0.2.0
category: CORRECTION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Implement the Project Owner-authorized bounded correction of MC-1, MC-2 and MC-3 and register the accepted future audit clarification.
target_environment: Codex
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: a4cbc500b2ca864b2eb35e9354df88c8c3d97a3e
authorization_scope:
  - inspect repository evidence
  - correct only MC-1, MC-2 and MC-3
  - update directly affected contracts, templates, validators, tests, registries, state and navigation
  - register the Owner-accepted prospective execution-insight audit clarification
  - run focused validation
forbidden_actions:
  - alter PASS-02 R1 historical artifacts
  - prepare or execute PASS-02 R2
  - execute CHECKPOINT-A or PASS-03 and later passes
  - amend the Kernel
  - adopt or activate GOV-7
  - retrospectively migrate completed reviews or findings
  - accept recommendations or risk
  - stage, commit, push, open a pull request, merge, release or ratify
exact_text_preserved: true
exact_text_sha256: 254419287a11282cfd76adfc41c5026a027ed41e709d141c53398ad2f35dc5f1
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/audits/GOV-AUD-001-gov7-enablement/07-audit-methodology-and-review-protocol.yaml
  - governance/audits/GOV-AUD-001-gov7-enablement/passes/PASS-02/contract.yaml
  - governance/audits/GOV-AUD-001-gov7-enablement/passes/PASS-07/contract.yaml
  - governance/tools/validate_audit_methodology.py
  - governance/tests/test_audit_methodology_protocol.py
  - governance/methodology/METHODOLOGY_BACKLOG.md
  - governance/audits/GOV-AUD-001-gov7-enablement/09-methodology-bounded-correction-validation.yaml
result_commit: null
supersedes: HP-PROMPT-030/0.1.0
---

# HP-PROMPT-030 — Bounded Correction of GOV-AUD-001-METHOD-001

## Exact executed text

# HugePlanning — Bounded Correction of GOV-AUD-001-METHOD-001

You are implementing a Project Owner-authorized bounded correction to the uncommitted `GOV-AUD-001-METHOD-001` audit-methodology work.

The focused independent review concluded:

```text
SUITABLE_AFTER_BOUNDED_CORRECTION
```

Correct only findings `MC-1`, `MC-2`, and `MC-3`, and durably register one accepted prospective audit clarification concerning execution-insight learning.

Do not redesign the methodology or prepare PASS-02 R2.

## Repository identity

* Repository: `Sugar144/HugePlanning`
* Required branch: `governance/kernel-designer-revision-v0.1`
* Expected committed HEAD: `a4cbc500b2ca864b2eb35e9354df88c8c3d97a3e`
* Expected worktree:

  * preserved uncommitted PASS-02 R1 candidate;
  * uncommitted `GOV-AUD-001-METHOD-001`;
  * empty staging area.

## Authorization

The Project Owner authorizes:

1. repository-wide read-only inspection where needed;
2. bounded edits required to correct MC-1, MC-2, and MC-3;
3. updates to directly affected contracts, templates, methodology validation, focused tests, registries, state, and navigation only when required;
4. durable registration of the accepted prospective audit clarification described below;
5. focused validation.

The Project Owner does not authorize:

* alteration of PASS-02 R1 historical artifacts;
* PASS-02 R2 preparation or execution;
* CHECKPOINT-A;
* PASS-03 or later pass execution;
* Kernel amendment;
* GOV-7 policy adoption or activation;
* broad methodology redesign;
* retrospective migration of completed reviews or findings;
* commit, push, PR, merge, release, ratification, or risk acceptance.

## Startup verification

Verify:

```text
repository root
branch
local and remote HEAD
staging state
presence of METHOD-001
presence and hashes of PASS-02 R1
reviewed MC-1, MC-2, and MC-3 affected artifacts
canonical identity registries
```

Do not reset, clean, stash, discard, or overwrite the worktree.

Resolve any required new identity from canonical repository sources. Do not assign IDs from this prompt or chat memory.

## MC-1 — Bindable pass-contract identity

The modified PASS-02 and PASS-07 contracts lack an explicit bindable version or supersession identity, while future prompt custody requires `CONTRACT_VERSION` or an equivalent unambiguous identity.

Implement the smallest coherent correction:

* give each affected pass contract an explicit version identity;
* define its status and supersession relationship where applicable;
* ensure instantiated prompts can bind to the exact contract version and hash;
* avoid duplicating contract authority in templates;
* preserve all prior completed-run bindings and evidence.

Do not version every unrelated contract.

## MC-2 — Review-type and result-contract coherence

Reconcile:

* methodology review types;
* allowed type-specific conclusions;
* PASS-07 permitted final results;
* insufficient-evidence outcomes;
* PASS-07 template review-type selection.

Required behavior:

1. `DETERMINISTIC_VALIDATION` and `TARGETED_CONFIRMATION` cannot independently produce a full PASS-07 substantive disposition.
2. PASS-07 must use an appropriate substantive or adversarial review type.
3. The methodology must define a clear mapping between review-type conclusions and pass-level result tokens.
4. Insufficient evidence must have an explicit valid outcome.
5. Exactly-one-result constraints must remain deterministic.
6. Do not force PASS-07 to be called adversarial unless its contract actually requires the adversarial attack method.
7. Do not silently reclassify completed historical reviews.

Prefer one canonical result vocabulary or a small explicit mapping over parallel incompatible vocabularies.

## MC-3 — Bounded instance-level semantic validation

Improve validation so that future findings and reviews governed by METHOD-001 can be checked semantically.

Validate only material invariants such as:

* finding basis is present and allowed;
* `MODEL_INFERENCE_ONLY` is not represented as verified fact;
* invalidity conclusions include causal, authority-impact, and materiality analysis;
* review type is declared;
* result is allowed for that review type and pass contract;
* adversarial reviews record actual attack attempts;
* insufficient-evidence outcomes are representable;
* exactly-one-result constraints hold.

Constraints:

* do not require exact prose equality where semantic or structured checks suffice;
* do not hardcode future finding IDs;
* do not build a universal framework for every repository artifact;
* do not retrospectively migrate completed runs;
* do not duplicate the whole methodology protocol inside validator code;
* prefer validating structured fields or explicit metadata;
* keep the correction usable for PASS-02 R2 and later governed reviews.

Existing immutable PASS-02 R1 hashes may remain protected, but separate historical-custody protection from general methodology-instance validation where practical.

## Durable registration — Execution Insight Capture and Learning Promotion Pipeline

The Project Owner accepts this as a prospective audit clarification that must not be lost.

Register it in the existing canonical methodology proposal or audit future-work mechanism, resolving a canonical identity if one is required.

Required classification:

```yaml
classification: METHODOLOGY_PROPOSAL
scope: GOV-AUD-001
status: OWNER_ACCEPTED_FOR_FUTURE_AUDIT_CLARIFICATION
implementation_status: NOT_STARTED
incorporation_point: AFTER_CHECKPOINT_A_BEFORE_PASS_03
target_passes:
  - PASS-03
  - PASS-04
  - PASS-06
  - PASS-07
```

The proposal must state that the audit will explicitly assess a minimal pipeline covering:

```text
observable execution event
→ visible execution insight
→ hypothesis
→ verification
→ confirmed or refuted conclusion
→ learning candidate
→ triage
→ durable destination
→ procedural promotion
→ selective retrieval
→ effectiveness measurement
```

It must preserve these boundaries:

* no hidden chain-of-thought collection;
* observable execution data and explicit model outputs only;
* repository evidence remains canonical;
* traces are non-authoritative;
* hypotheses remain distinct from verified conclusions;
* no silent procedural promotion;
* no automatic governance or Kernel modification;
* no automatic risk acceptance;
* material learning requires human or independent disposition;
* low-value and duplicate learning must be controlled;
* effectiveness must include recurrence reduction and retrieval usefulness.

Record the intended future allocation:

```text
PASS-03:
design capture, verification, triage, promotion, retrieval, and measurement.

PASS-04:
compare NO_NEW_TOOL, repository-native, minimal custom, external framework,
and hybrid implementation options.

PASS-06:
synthesize cost, integration, Owner burden, and proportionality.

PASS-07:
independently challenge false learning, self-certification, noise,
privacy, provider dependence, and excessive context.
```

Do not modify PASS-03 or PASS-04 contracts now. The durable proposal must explicitly require a bounded contract clarification after CHECKPOINT-A and before PASS-03 instantiation.

## Deferred observations

Preserve or route these observations to PASS-06/PASS-07 without solving them now:

* methodology propagation across many artifacts;
* duplicate-custody and maintenance cost;
* hardcoded historical hashes in validator code;
* execution time and Owner burden of small methodology changes.

Do not create another failure record solely because this correction has multiple artifacts.

## Validation

Run only validation materially relevant to this correction:

```text
focused methodology validator
focused methodology tests
audit scaffold validator
prompt/state validation if affected
learning or proposal validation if affected
PASS-02 R1 immutable-hash verification
git diff --check
git status
```

Do not run the complete repository suite unless a changed shared component makes it necessary. If you run it, state the specific reason.

## Required final report

Return:

```text
Repository
Branch
Committed HEAD
Initial and final staging state
Resolved identities
Files created
Files modified
MC-1 correction
MC-2 correction
MC-3 correction
Learning-pipeline proposal path and status
PASS-02 R1 preserved
Focused validation commands and exact results
Deferred observations preserved
PASS-02 R2 prepared: NO
CHECKPOINT-A executed: NO
PASS-03 contracts modified: NO
GOV-7 activated: NO
Kernel amended: NO
Commit authorized: NO
Push authorized: NO
Exact next action
```

Stop after validation. Do not commit or push.
