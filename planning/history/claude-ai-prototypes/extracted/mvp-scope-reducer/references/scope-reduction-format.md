# Scope Reduction Format Reference

Full detail for classifying features and structuring MVP scope reduction output. Load this before producing any output.

## Common complexity multipliers

Pay special attention to features that often look simple but increase scope, testing, support, or risk: user accounts, customer history, saved preferences, online payments, refunds, subscriptions, coupons/discounts, offers/campaigns, admin panels, editable CMS, real-time dashboards, notifications, email/SMS/WhatsApp automation, multilingual content management, roles and permissions, analytics and reporting, third-party integrations, migrations, search/filtering, scheduling/availability, inventory, audit logs, data export, legal/privacy consent workflows.

## Scope categories

Classify every requested feature into one of these:

1. **Core v1** — essential to deliver the core value; without it, the product doesn't solve the main problem.
2. **Support v1** — useful for v1 but not the core value itself; include only if low-cost or necessary for operation.
3. **Simplify for v1** — keep the business outcome, but reduce implementation complexity.
4. **Phase 2** — valuable, but can wait until after first validation.
5. **Needs client validation** — could matter, but current docs don't prove it.
6. **Risky/expensive** — may be justified, but should be explicitly acknowledged before committing.
7. **Remove or avoid** — not aligned with the MVP, or likely to distract from the core goal.

## Reduction strategies

Use these where they fit the feature being simplified:

- **Manual-first v1** — replace automation with manual handling for the first version.
- **Admin-lite** — avoid a full admin panel; use a simpler internal workflow, spreadsheet, config file, or restricted update path.
- **No-auth v1** — avoid user accounts if the flow can work with guest checkout, magic links, or simple contact details.
- **Payment-light** — use pay-on-pickup, payment link, or manual confirmation before building full payment/refund flows.
- **Notification-light** — use email-only or dashboard-only before adding real-time, SMS, WhatsApp, or push.
- **Content-light** — hardcode or seed content first before building a CMS.
- **Single-language v1** — launch in one primary language if multilingual content management would slow the build.
- **Report-light** — start with simple exports or basic summaries before full analytics dashboards.
- **Integration-light** — avoid deep integrations in v1; use manual import/export or a simple webhook where acceptable.
- **Operational fallback** — design a manual fallback path for risky flows.

## Output format

```markdown
# MVP Scope Reduction — {Project Name or Feature Set}

## 1. Core Value to Protect
The minimum valuable outcome.

## 2. Primary v1 User Journey
The smallest journey that must work end to end.

## 3. Recommended v1 Scope

### Core v1
Features that must remain.

### Support v1
Useful but secondary features to include only if feasible.

### Simplify for v1
Features whose business outcome should remain but whose implementation should be simplified.

| Feature | Keep outcome? | Simplified v1 approach | Trade-off |
|---|---|---|---|

### Phase 2
Features to defer.

### Needs Client Validation
Features or decisions that should be checked with the client.

### Risky or Expensive
Features that may significantly increase scope.

| Feature | Why it is expensive/risky | Safer v1 alternative |
|---|---|---|

### Remove or Avoid
Features that should not be part of v1.

### Feature Dependencies
Check before finalizing any cut or deferral — a retained v1 feature may depend on something being deferred.

| Feature | Depends on | Impact if dependency is cut | Recommendation |
|---|---|---|---|

## 4. Suggested Scope Cuts
Prioritized list.

| Cut | Saves | Business trade-off | Client-friendly explanation |
|---|---|---|---|

## 5. Recommended MVP Version
The proposed v1, described in plain language.

## 6. Client Validation Questions
Top 5–10 questions to confirm before finalizing scope.

## 7. Implementation Notes
Short notes for the implementer.

## 8. Next Action
Recommend one:
A) Validate cuts with client
B) Run technical/UX discovery
C) Generate artifact pack
D) Review documentation quality
E) Proceed to implementation planning
```
