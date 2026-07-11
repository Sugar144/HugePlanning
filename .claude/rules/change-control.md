# Rule: change-control (always loaded)

**Policy.** Nothing with status `approved` changes without a change-control
record: a `CR-nnn` change request (`12` §5) or a gate record in
`docs/handoffs/` authorizing the new baseline. Approved artifacts are
**superseded, never rewritten**: the old item gets a terminal status
(`superseded` / `deprecated`) and the replacement is a new identified item.
Gate handoff records are append-only files
(`docs/handoffs/G<n>-<slug>-<seq>.yaml`); a repeated gate pass appends the next
sequence, it never edits a previous record. No gate is ever auto-approved.

**Why.** Client approvals are commitments anchored to specific content
(`approved_in` = the baseline merge commit); silent mutation after approval
destroys the basis of every downstream estimate, review, and acceptance.

**Observable violation.** A diff that edits an `approved` artifact without an
associated CR or gate record; a modified or deleted file under
`docs/handoffs/`; a renumbered or reused ID after supersession; an approval
recorded without its written gate record.
