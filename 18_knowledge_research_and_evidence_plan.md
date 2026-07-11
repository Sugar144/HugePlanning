# 18 — Knowledge Research and Evidence Plan

**Purpose:** the actionable research backlog separating knowledge that may start as provisional model-generated content from knowledge requiring external research before client production use (R2-15). Executable in external Research Mode without redesigning the knowledge architecture (`17`).
**Standing rule:** research items land via the integration procedure in §3; nothing here blocks S0–S3 (all provisional generation is permitted per `17` §K); items marked **pre-client** block only the first *real* client engagement in their area.

---

## 1. Provisional model-generated content (no prior research required)

File structures and skeletons for all knowledge files · question-bank seeds and sufficiency checks · requirement-quality heuristics and classification examples · elicitation dialogue examples · process-reconstruction frames · architecture comparison frames · UX method content · test-strategy heuristics · glossary. **Quality control for these is behavioural (scenario runs + golden checklists), not source research.** Each still carries `source_quality: model-generated` and a `review_due` so nothing rots unmarked.

## 2. Research backlog (RES items)

Fields per item: Question · Priority · Target file · Risk if unverified · Preferred primary sources · Acceptable secondary · Freshness / jurisdiction · Evidence standard · Completion criterion · Review date.

| | RES-01 | RES-02 | RES-03 |
|---|---|---|---|
| Question | Which formal RE practices (elicitation, specification, validation) should tighten our interview/normalization method? | Current defensible web performance & a11y target values (LCP-class budgets, WCAG 2.2 AA specifics) for NFR floors | Current Claude Code behaviour relevant to the runtime (add-dir loading, --agent, permissions, hooks) on each CLI upgrade |
| Priority | Medium | High | High (recurring) |
| Target | shared/elicitation-techniques, requirements-taxonomy | shared/nfr-catalog | `02` §5 notes + tool knowledge |
| Risk if unverified | Suboptimal method, not incorrect outputs | Wrong targets promised to clients | Broken launch mechanics after upgrade |
| Primary | ISO/IEC/IEEE 29148; IREB CPRE syllabi | web.dev/Core Web Vitals docs; W3C WCAG 2.2 + Understanding docs | code.claude.com official docs |
| Secondary | Reputable RE literature | reputable perf blogs | release notes, changelog |
| Freshness / jurisdiction | any / — | ≤12 months / — | on CLI version change / — |
| Evidence standard | cited framework mapping | every numeric target has a primary ref | quoted doc statements (as `19` §0) |
| Completion | techniques file upgraded to secondary-sourced with mapping table | catalog targets primary-sourced | smoke check re-run + notes updated |
| Review | +12 months | +12 months | each upgrade |

| | RES-04 | RES-05 | RES-06 |
|---|---|---|---|
| Question | Jira CSV/REST import behaviour: field mapping, key capture, idempotency options | Application-security baseline: OWASP-current checklist mapping to our security floors; payment-integration hygiene (SAQ-A-style delegated model) | GDPR obligations for small-business sites built by a freelance processor/developer (ES/EU): privacy info, consent, DPA-with-providers, data-subject rights implementation |
| Priority | Medium (by S5) | High (pre-HIGH-RISK client) | **Critical (pre-first real client)** |
| Target | jira-export skill notes, tool knowledge | technical-solution/security-baseline | legal/gdpr-basics |
| Risk if unverified | Import friction only | Real vulnerabilities shipped; false assurance | Legal exposure for you and the client |
| Primary | Atlassian docs | OWASP ASVS/Top10/Cheat Sheets; PCI SSC docs | GDPR text; EDPB & AEPD guidance |
| Secondary | practitioner guides | vendor security guides | reputable ES legal blogs (flagged secondary) |
| Freshness / jurisdiction | ≤6 months / cloud Jira | ≤12 months / — | ≤12 months / **EU + ES** |
| Evidence standard | tested import on a scratch project | each checklist item maps to a cited control | every obligation cited to regulation/guidance; file remains "verify with professional" |
| Completion | export-jira.sh validated round-trip | baseline primary-sourced + reviewed | file primary-sourced; checklist usable in M8 and G2 package |
| Review | +6 months | +12 months | +12 months |

| | RES-07 | RES-08 | RES-09 |
|---|---|---|---|
| Question | Cookie/consent rules (ES: LSSI + AEPD cookie guidance; EU ePrivacy): when consent needed, compliant banner patterns, analytics implications | Accessibility legal obligations (EU Accessibility Act, ES transposition, public-sector rules): who is obliged, to what level, freelancer duty to inform | Verified behaviour of the first deployment providers we adopt (deploy/rollback/health mechanics, limits, pricing) |
| Priority | **Critical (pre-first real client)** | High (pre-first affected client) | High (by S7) |
| Target | legal/cookie-consent | legal/accessibility-law | technical-solution/deployment-patterns + adapter scripts |
| Risk if unverified | Non-compliant deliverables at scale (every site has this) | Missed legal duty on obliged clients | Broken deploys, wrong rollback promises |
| Primary | AEPD guidance; LSSI; ePrivacy directive | EAA text; BOE transposition; EN 301 549 | provider official docs |
| Secondary | ES legal practitioner summaries | accessibility org summaries | community runbooks |
| Freshness / jurisdiction | ≤12 months / ES+EU | ≤12 months / ES+EU | ≤6 months / per provider |
| Evidence standard | cited; banner pattern examples classified compliant/non | cited obligation matrix | adapter contract tested against scratch deploy |
| Completion | file primary-sourced; M8 probe + G2 disclosure ready | file primary-sourced; discovery flag logic defined | one adapter fully verified per family in use |
| Review | +12 months | +12 months | +6 months |

**RES-10 (Low, S9):** current MCP/Agent-SDK options for the future API runtime — informs `01` §10 portability only; explicitly not MVP.

## 3. Integration procedure (per completed RES item)

1. Research output lands as a sourced draft in the target file (References + inline refs per `17` E).
2. Front matter updated: `source_quality`, `reviewed_at`, `review_due`; `status: provisional → active` if criteria met.
3. Affected floors/checklists reconciled with `21` §5 (matrix is the single floor authority — research updates the *how/why*, and floor changes are a conscious methodology decision, not an automatic side effect).
4. Behavioural check: one scenario touching the area re-run if the content changes agent behaviour.
5. Ships as a methodology release (MINOR), CHANGELOG lists the research delta.

## 4. Sequencing relative to the roadmap

- **Blocking nothing before S4:** all RES items.
- **Pre-first-real-client (hard):** RES-06, RES-07; RES-08 if the client is obliged; RES-05 if HIGH-RISK.
- **Stage-tied:** RES-04→S5 · RES-09→S7 · RES-03→every CLI upgrade.
- Recommended batch: run RES-06/07/08 as one Research Mode session (~half a day) during S2–S3, while pipelines are being built.
