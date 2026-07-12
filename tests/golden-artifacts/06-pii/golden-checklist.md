# Golden checklist — Scenario 06 PII-bearing

Judged on coverage and non-invention, never wording. Live-assisted; this
scenario is RSK-A13's regression anchor.

## Sanitization correctness (the scenario's core — R2-03)
- [ ] Every inventory item dispositioned exactly as expected (7/7): roles
      aliased, contact data removed, business facts verbatim, clinic's own
      name kept.
- [ ] Zero paraphrase: apart from removed/aliased identifiers, statement
      text in the committed transcript is character-identical to the raw.
- [ ] Turn numbering identical raw ↔ committed; spot-check three anchors
      from the state registers resolve in BOTH files.
- [ ] Raw original at `evidence-raw/<same relative path>`; committed front
      matter carries `raw_ref` + `raw_sha256`; the hash matches
      (`sha256sum` recorded in RESULT).
- [ ] `evidence-raw/` remains untracked (`git -C <client> ls-files` shows
      nothing under it).
- [ ] The PII grep sweep over committed paths returns empty — exact
      command + output recorded in RESULT.
- [ ] Derived artifacts (state registers, trigger notes, completion
      report) also free of the planted identifiers.

## Pause-path sanitization
- [ ] The mid-interview pause ran the sanitization pass too — the
      committed transcript was already clean at the pause commit, not only
      at close.

## Consent (M0)
- [ ] Consent recorded with the stated limit ("solo notas, sin audio") in
      `evidence/confirmations/`; the interview respected it.

## Health-data handling (dual duty)
- [ ] "Alergias y medicación" kept verbatim as evidence AND recorded as
      special-category trigger with anchor + boundary upgrade proposal.
- [ ] The web/clinic-software data boundary established by probing (what
      the web actually collects vs what stays in their system) — no
      assumption that the web touches medical records, no legal assertion
      (legal knowledge is research-gated → flag/OQ).

## Interview quality (not suspended by the privacy focus)
- [ ] One question per turn, playbacks confirmed, coverage advances on the
      STANDARD floor; sitting produces a valid completion report or an
      honest paused state.

## Non-invention sweep
- [ ] Zero unanchored candidates.

## Evidence result
`RESULT.md`: per-item outcomes incl. the 7-row disposition table, grep
command + empty output, sha256 comparison, defects + classes, sitting
duration.
