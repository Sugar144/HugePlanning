# 17 — Knowledge Architecture and Authoring Standard

**Purpose:** how methodology knowledge is structured, written, sourced, cited, versioned, retrieved, activated, tested, and kept from duplicating rules/skills. Governs `freelance-methodology/knowledge/` (R2-13/14).
**Consumers:** every agent; the AI generation sessions that will author the files; `18` (research plan) executes this standard's source policy.

---

## A. Knowledge taxonomy

| Type | Nature | Volatility | Examples |
|---|---|---|---|
| `concept` | Stable conceptual knowledge | Low | requirements-taxonomy, evidence-and-uncertainty |
| `standard` | Standards & official guidance summaries | Medium (versioned) | WCAG guidance in nfr-catalog, security-baseline |
| `framework` | Decision/interpretation frameworks | Low | architecture-decision-framework, scope-and-mvp |
| `catalog` | Reference catalogues with selectable entries | Medium | nfr-catalog, question-bank, elicitation-techniques |
| `examples` | Worked examples & anti-examples | Low | embedded per file + `examples/` dirs |
| `archetype-pack` | Per-archetype concern bundles | Medium | web-project-archetypes (governed by `21`) |
| `domain-pack` | Optional client-domain bundles (restaurants, clinics…) | Medium | added post-MVP on demand |
| `legal` | Legal/regulatory summaries | **High** — review-dated, jurisdiction-tagged | gdpr-basics, cookie-consent, accessibility-law |
| `tool` | Tool/provider behaviour | **High** — version-tagged | deployment-patterns provider notes, Jira import behaviour |

## B. Common metadata (front matter — audited subset)

```yaml
---
id: kn-nfr-catalog          # stable, kebab, kn- prefix
title: NFR catalog and floors
type: catalog               # taxonomy A
status: provisional        # provisional | active | deprecated | superseded | archived
version: 0.1.0
language: en
jurisdiction: EU/ES         # legal & some standard types only
source_quality: model-generated   # model-generated | secondary-sourced | primary-sourced
reviewed_at: null
review_due: null            # mandatory for legal & tool types
consult_when: "eliciting or normalizing non-functional requirements"
do_not_use_for: "deciding legal compliance (see legal/ files)"
used_by: [client-discovery, technical-solution-architect, nfr-elicitation]
related: [kn-requirements-taxonomy]
supersedes: null
---
```

**Rejected fields** (proposal audited): `domain` (redundant with directory), `authority` (folded into `source_quality`), `created_at` (Git has it). `status: provisional` + `source_quality: model-generated` is the machine-readable marker for R2-15's "provisional until verified" rule — client-facing use of `legal` files requires `primary-sourced` + `active`.

## C. General authoring pattern (default body)

`Purpose → Scope → Consult when / Do not use for → Core concepts → Decision or interpretation framework → Examples (incl. one anti-example) → Failure modes → Limitations → References → Related`. Specialized formats (D) may replace the middle sections; front matter and the Purpose/Consult-when/References frame are universal. Target ≤ ~300 lines per file; larger bodies split into `references/` subfiles linked at section level.

## D. Specialized formats

| Format | Structure deviation |
|---|---|
| Question bank | Per interview topic: seed questions (open→specific→example→confirm forms), sufficiency check, risk keywords, common client phrasings (ES/EN), anti-patterns (leading forms to avoid) |
| Elicitation techniques | Per technique: when, script skeleton, worked mini-dialogue, failure signs |
| Taxonomies/catalogs | Entry table + per-entry: definition, detection cues, examples, floor values per profile (`21` §5 refs, not copies) |
| Architecture comparisons | Per option class: criteria table, freelance-context weighting, exit costs, "when the loser wins" |
| Security/testing baselines | Checklist items with: why, how verified, profile floor tags |
| Legal | Obligation summaries + explicit "verify with a qualified professional" header + jurisdiction + review_due; never phrased as advice |
| Tool/provider | Verified-behaviour notes with version + date + source link per claim |
| Archetype packs | Per archetype: concern list → pointers to shared knowledge sections (never restated content) |

## E. Source policy

- **Levels:** `primary-sourced` (official standard/regulator/vendor docs) > `secondary-sourced` (reputable practitioner literature) > `model-generated` (provisional).
- **Citations:** References section lists source, version/date, URL; claims that are quantitative, legal, or tool-behavioural must carry an inline `[ref-n]` marker. Conceptual/heuristic content needs no per-line citations.
- **Mandatory primary sourcing** before `active`: all `legal` files; WCAG-derived checklists; payment-security content; tool-behaviour claims (Claude Code, Jira, providers). Everything else may go `active` on scenario-validated model-generated content with `review_due` set.
- **Freshness:** `legal` review ≤ 12 months; `tool` review ≤ 6 months or on version change (lock records CLI version → triggers review). Stale = past `review_due` ⇒ `status.sh --methodology` flags it; stale legal/tool knowledge must not be consulted for client decisions (rule-enforced).
- **Conflicts:** source conflict recorded in Limitations with both positions; primary beats secondary beats model.

## F. Retrieval design

- `knowledge/INDEX.md`: one line per file — `id · consult_when · profile/archetype tags · status`. Agents read INDEX, then load only matching files, then only matching sections (files must keep self-contained sections with stable headings for section-level loading).
- **Per-agent retrieval maps** live in each agent file ("knowledge:" list = its default set); **per-skill maps** in SKILL.md preconditions. INDEX is the superset; maps are the defaults.
- Context budget rule: an agent loads ≤ 2 knowledge files beyond its defaults per task without explicit need justification (keeps sessions lean; mirrors V1's context-economy risk mitigation).
- Portability: INDEX + front matter are exactly the metadata a future RAG/MCP retrieval layer needs; no Claude-Code-specific syntax inside knowledge bodies (`01` §10 rule applies).

## G. Anti-duplication (placement decision tree)

```text
Must it always be true / never be violated?          → RULE (or CLAUDE.md if global)
Is it a procedure with steps and checks?             → SKILL
Is it who/when a role acts?                          → AGENT file
Is it concepts, references, options, examples,
  interpretation guidance consulted when relevant?   → KNOWLEDGE
Is it the shape of an output?                        → TEMPLATE + SCHEMA
```

Hard rules: knowledge never contains "must/never" policy (that's a rule) or numbered procedures (that's a skill) — it may *explain* why a rule exists. Critical policy must never exist **only** in knowledge (tested, J). Packs reference shared knowledge sections; restating shared content in a pack is a review-blocking defect.

## H. Profile & archetype activation

`INDEX.md` tags each file/section: `profiles: [lite, standard, high-risk]`, `archetypes: […]`. Activation: agent resolves project profile+archetypes from `project.yaml` → INDEX filter → default set. Examples: `security-baseline` deep sections activate on HIGH-RISK or auth/payment archetypes; question-bank deep-dive sections (payments, migration, healthcare data) activate by archetype/trigger; `nfr-catalog` floor tables are read through `21` §5 (floors live once, in the matrix — catalog explains *how to satisfy/verify*, matrix says *what's required*).

## I. Lifecycle

`provisional → active → deprecated → superseded → archived` (statuses in front matter). Ownership: you (sole maintainer); every knowledge change ships in a methodology release (MINOR for additions, PATCH for corrections, MAJOR if a floor interpretation changes behaviour); CHANGELOG lists knowledge deltas; `supersedes` links preserve history; stale alerts per E.

## J. Knowledge testing (methodology test layer, extends `02` §10)

Scenario-scored checks: (1) relevant knowledge consulted (scenario expects question-bank section X used in module Y); (2) no gratuitous loading (context inspection: unrelated packs absent); (3) knowledge never overrides client evidence (golden: client says X, catalog default says Y ⇒ output records X + proposed default, never silent Y); (4) methodology defaults surface as `proposed_default` for confirmation; (5) stale/provisional legal content triggers the flag instead of being asserted; (6) critical-policy duplication scan (grep: no "must never" phrasing in knowledge/); (7) interviewer selects correct question-bank sections per archetype fixture.

## K. Initial knowledge inventory — minimum content specifications (19 files)

Format: **Consumers · Triggers · Minimum topics · Examples required · Sources · Excludes · Maintenance · Provisional-gen OK? / Research-mandatory?** (research items → `18`).

1. **shared/requirements-taxonomy** — auditor, normalization, discovery · classification doubts · statement types (`04` §3) with detection cues; requirement types incl. DAT; origin enum semantics; promotion rules · ≥8 classified examples incl. tricky ones (solution-as-need, preference-as-fact) · concept, model-gen OK · excludes elicitation how-to · low maintenance · **Prov: yes / Research: no**
2. **shared/elicitation-techniques** — discovery skills · stuck topics, vague answers · funnel, laddering, example-anchoring, contrast questions, silence handling, "I don't know" protocols · 1 mini-dialogue per technique · secondary sources welcome (IREB-class, RES-01) · excludes question content (bank's job) · low · **Prov: yes / Research: recommended, not blocking**
3. **shared/nfr-catalog** — nfr-elicitation, auditor, technical architect · M8, normalization, design · categories (perf, a11y, security, privacy, SEO, compatibility, backup, maintainability) with: client-language probe, measurable-target patterns, verification methods, floor pointer to `21` §5 · 1 well-formed NFR per category (V2 fields) · perf/a11y targets need primary refs (RES-02) · excludes legal obligations · medium · **Prov: yes / Research: partial**
4. **shared/evidence-and-uncertainty** — all discovery/spec agents · classification & confidence doubts · evidence anchoring, confidence levels, inference vs fact, sanitization rationale · 4 examples · concept · low · **Prov: yes / Research: no**
5. **shared/glossary** — all · term disputes · project + methodology terms, ES/EN pairs for client-facing terms · — · low · **Prov: yes / Research: no**
6. **client-discovery/interview-strategies** — client-discovery · module planning, mode selection · module trajectories per profile (`21` §5 depths), rapport, pacing, fatigue signals, multi-stakeholder handling, import-mode gap analysis · 2 trajectory examples (LITE vs HIGH-RISK) · **Prov: yes / Research: no**
7. **client-discovery/question-bank** — client-discovery · every module · per topic (full `04` §5 tree): seeds, sufficiency checks, risk keywords, deep-dive sections per archetype/trigger (payments, health data, migration, CMS editors, content) · ≥3 seeds/topic; anti-example (leading form) per module · validated via scenarios, not external research · **high maintenance (grows from every real interview)** · **Prov: yes / Research: no**
8. **client-discovery/process-elicitation** — process-elicitation skill · M4/M5 · process reconstruction frame (trigger/actors/steps/exceptions/outcome), exception-hunting prompts, sufficiency criteria · 1 worked reconstruction · **Prov: yes / Research: no**
9. **client-discovery/scope-and-mvp** — client-discovery, doc-generator · M10, estimation · phase-cutting heuristics, exclusion phrasing, scope-flag disposition, budget-conversation patterns · 2 examples · **Prov: yes / Research: no**
10. **client-discovery/technical-operational-context** — client-discovery · M9 · ownership checklist (domain/hosting/email/analytics/accounts), access-status recording, maintainer-skill assessment · 1 filled example · **Prov: yes / Research: no**
11. **technical-solution/architecture-decision-framework** — architecture-option-analysis · every decision item · criteria weighting for solo-freelance context, exit-cost thinking, build-vs-buy, boring-tech default, ADR quality bar · 2 worked comparisons · **Prov: yes / Research: no**
12. **technical-solution/web-project-archetypes** — discovery, technical architect, scripts · G0/G3, activation · per-archetype concern lists per `21` §1, decision-category emphases, matrix-row seeds, adapter family — all as pointers to `21`/shared content · — · medium · **Prov: yes / Research: no**
13. **technical-solution/ux-design-framework** — ux-design-outline skill · UX deliverables per profile · IA/sitemap method, flow notation, wireframe-description format, state inventory (error/empty/loading), design tokens basics, visual-direction elicitation, responsive acceptance patterns · 1 full example set for a STANDARD site · secondary sources fine · **Prov: yes / Research: no**
14. **technical-solution/security-baseline** — risk-specialist, technical architect · security floors, trigger-area design/review · checklist per `10` §5 with why+verify per item, authN/Z patterns for common stacks, payment-integration hygiene (delegated-to-provider model), threat-model-lite method · — · **primary sources required for payment/security assertions (RES-05)** · 6-month review · **Prov: draft / Research: yes before HIGH-RISK client use**
15. **technical-solution/test-strategy** — test-planning · G3 · level selection per risk/profile, matrix authoring, E2E flow selection, migration rehearsal patterns, flake policy rationale · 1 worked matrix for booking archetype · **Prov: yes / Research: no**
16. **technical-solution/deployment-patterns** — technical architect, release-manager · deployment outline, adapter choice · adapter families (`11` §5) with per-family: envs, rollback mechanics, cost notes; provider-specific claims carry version+date+link · — · **tool type — 6-month review; provider claims research-backed (RES-09)** · **Prov: partial / Research: per provider before use**
17. **legal/gdpr-basics** — discovery (M8), auditor, technical architect · personal-data topics · lawful-basis overview, data-subject rights vs project obligations (privacy page, consent, export/delete), processor questions for providers, evidence-retention implications · ES/EU jurisdiction · **primary sources only (RES-06)** · 12-month review · **Prov: skeleton only / Research: MANDATORY before first real client**
18. **legal/cookie-consent** — technical architect, implementer · any cookies/analytics · consent requirements, categories, banner patterns that are compliant vs dark-pattern, analytics configuration implications · ES/EU · **(RES-07)** same regime as 17
19. **legal/accessibility-law** — discovery, auditor · M8, public-sector/large-client flags · which entities have legal a11y obligations (EU/ES), WCAG version/level mapping, what freelancers must flag vs decide · ES/EU · **(RES-08)** same regime as 17

All 19 begin `status: provisional`; promotion rules per E; the three legal files additionally block client-facing use until `primary-sourced`.
