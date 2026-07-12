---
id: kn-nfr-catalog
title: NFR catalog — categories, probes, measurable targets, verification
type: catalog
status: provisional
version: 0.1.0
language: en
jurisdiction: EU/ES
source_quality: model-generated
reviewed_at: null
review_due: 2027-01-12
consult_when: "eliciting quality expectations (M8), normalizing an NFR, or supplying a profile-floor default"
do_not_use_for: "deciding legal compliance (see legal/ files, S3+) or which floors are mandatory (the 21 §5 matrix owns floors)"
used_by: [client-discovery, nfr-elicitation, requirements-auditor]
related: [kn-requirements-taxonomy, kn-elicitation-techniques]
supersedes: null
---

# NFR catalog

## Purpose

Per quality category: the client-language probe, the measurable-target
pattern (the V2 NFR fields: metric / target / conditions / measurement /
verification_level), how it gets verified, and one well-formed example.
Floors — *which* categories are mandatory per profile — live once, in the
`21` §5 matrix; this catalog explains how to elicit, quantify, and verify
each category, not what is required.

## How to use a category entry

Probe in consequences, not dimensions (see consequence framing in
[[kn-elicitation-techniques]]). Quantify from the client's reaction; when the
client has no number, the pattern's default enters as `methodology_default` +
`proposed_default` — confirmed at G2, never silently imposed
([[kn-requirements-taxonomy]]).

## Categories

### Performance
- Probe: "si la página tarda en abrir y el cliente está en el móvil con poca
  cobertura, ¿le preocupa perderlo?"
- Pattern: metric LCP (or page-weight budget) · target "≤ 2.5 s" · conditions
  "4G, mid-range device, cold cache" · measurement Lighthouse mobile on
  staging · verification pre-release · tolerance p75.
- Default targets need primary sourcing (RES-02) before `active`.

Example (well-formed):

```yaml
id: NFR-002
type: nonfunctional
category: performance
statement: Las páginas públicas cargan rápido en móvil.
metric: LCP
target: "<= 2.5 s"
conditions: "4G, gama media, caché fría"
measurement: { method: "Lighthouse móvil", environment: staging }
verification_level: pre-release
tolerance: "p75"
origin: methodology_default
status: proposed_default
```

### Accessibility
- Probe: "¿entre sus clientes hay personas mayores o con dificultades de
  visión? ¿qué pasaría si no pudieran completar una reserva?"
- Pattern: metric WCAG conformance · target "2.2 AA on public pages" ·
  measurement automated scan (axe-class) per PR + keyboard walkthrough ·
  verification per-PR (automated) and G6 (manual checklist).
- WCAG-derived checklists require primary sourcing before `active` (17 §E).

### Security
- Probe: "¿qué es lo peor que podría pasar si alguien manipulara la web o el
  formulario?"
- Pattern: rarely a client number — targets arrive as floor items (HTTPS/
  HSTS, headers, form rate-limiting, dependency audit) with measurement
  "checklist item verified at G6". Deep content belongs to security-baseline
  (S3 knowledge); at discovery the duty is recording exposure signals, which
  are also risk triggers (`21` §3).

### Privacy / data protection
- Probe: "¿qué datos personales guardaría la web, y cuánto tiempo los
  necesita de verdad?"
- Pattern: metric data-minimization/retention statements · target concrete
  retention windows and consent points · measurement inspection at G6 ·
  legal_or_regulatory items enter as `proposed_default` and are flagged to
  the legal/ files (S3+; provisional legal content is never asserted to the
  client).

### SEO basics
- Probe: "¿cómo espera que le encuentren los clientes nuevos?"
- Pattern: metric indexability items (titles, sitemap, GBP link) · target
  "present and valid at launch" · measurement crawl/inspection pre-release.

### Compatibility (devices/browsers)
- Probe: "¿desde dónde le escriben sus clientes — móvil, ordenador, ambos?"
- Pattern: metric supported matrix · target e.g. "last 2 versions of major
  mobile+desktop browsers; primary flow verified on Android + iPhone" ·
  measurement smoke walkthrough per release.

### Backup / recovery
- Probe: "si mañana desapareciera el contenido de la web, ¿qué perdería y
  cuánto tardaría en poder rehacerlo?"
- Pattern: metric restore point/time expectations · target e.g. "restore
  within 1 business day; content loss ≤ 1 week" · measurement restore
  spot-check at S7-class setup.

### Maintainability / operability
- Probe: "cuando entreguemos, ¿quién tocará la web — usted, alguien de su
  equipo, nadie?"
- Pattern: metric editor-skill fit · target "monthly menu update done by the
  owner unassisted after one walkthrough" · measurement observed walkthrough
  at handover. Feeds `operational.*` facts in solution-context too.

## Failure modes

- "Fast" recorded as a requirement — quality adjectives without a target
  fail the ambiguity audit; the alternatives are a concretized target or an
  explicit recorded waiver with operator sign-off (07 §2 rule 8).
- Floor smuggling: writing a floor NFR as if the client asked for it — the
  origin field exists precisely to prevent this.
- Jargon probes ("¿qué SLA de disponibilidad quiere?") produce guesses;
  consequences produce information.

## Limitations

Model-generated; perf/a11y default numbers are industry-common but not yet
primary-sourced (RES-02). Jurisdiction notes assume EU/ES small-business web
work.

## References

- Plan `06` §7.1 (NFR fields), `07` §3 (floor semantics), `21` §5 (floors),
  `10` §5 (security/a11y baselines), `18` RES-02.

## Related

[[kn-elicitation-techniques]] (consequence framing) ·
[[kn-requirements-taxonomy]] (origin/status pairing).
