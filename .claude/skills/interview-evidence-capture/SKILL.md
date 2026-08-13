---
name: interview-evidence-capture
description: Evidence capture and persistence for discovery interviews (plan 04 §6/§8) — transcript appends with turn anchors, state checkpoints, resume re-hydration, and the sanitization pass at close or pause (R2-03). Invoke on every interview turn, at every checkpoint event, on pause/resume, and at interview close. Not for use outside a discovery interview.
---

# interview-evidence-capture

**Purpose.** Make the interview auditable and resumable: every statement lands
in the transcript with a stable anchor, state survives any interruption, and
what gets committed is sanitized without ever distorting what the client said.

**Trigger.** Every turn (transcript append); every checkpoint event (state
write); every segment boundary (module close / pause / orchestrator-ended
segment → checkpoint, yield, fresh re-hydration); session pause, resume, and
close (sanitization pass at close and at any pause); M0 (consent record).

**Preconditions.** Client repository is the working directory;
`evidence/interviews/<session-id>/` exists; writing happens **only** inside
the client repository (the methodology directory is read-only); the project
language is known from `project.yaml`.

**Inputs.** The turn's speaker and verbatim text; the in-memory interview
state; on resume: the persisted `interview-state.json` and the last page of
`transcript.md`.

**Procedure — per-turn append.**
1. Append to `transcript.md`: turn number (`turn-nnn`, strictly sequential),
   speaker tag, timestamp, verbatim text. Operator paraphrases of a client
   answer are marked `[relayed]`.
2. Mirror the turn to `transcript.jsonl`:
   `{"turn": n, "speaker": "...", "text": "...", "ts": "...", "flags": []}`.
3. Never edit an existing turn. A correction (by client or operator) is a new
   turn that supersedes the old one by reference.
4. Any record derived from this turn (candidate requirement, fact,
   assumption, trigger) carries `source_refs` with this turn's anchor —
   a candidate without a resolving anchor cannot leave draft.

**Procedure — state checkpoint.** Write the full `interview-state.json`
(schema `interview-state.schema.json`) at: every module transition · every
register entry (CTR/ASM/OQ/scope flag) · every 10 turns · every pause. The
write is atomic (write temp, then replace) so a crash never leaves a
truncated state file. Because the **whole** file is rewritten each time,
`interview-state.json` is *working state*, not the evidence archive: keep
`coverage[].notes` and `resume_hints` **compact working annotations** (the open
gap + the pending probe + the anchor ids — a soft ceiling of a couple of lines
per node). The verbatim record already lives in the transcript, and the
consolidated per-topic narrative is written once at close in the
completion-report — duplicating either into every checkpoint amplifies write
cost with interview length without adding evidence. Compactness never drops an
anchor: every candidate still carries its `source_refs`.

**Procedure — pause.** At a module boundary when possible: set
`session.status: paused`, fill `resume_hints` (≤5 lines: where, what's
pending, the next queued question), checkpoint state, run the sanitization
pass on the transcript so far, tell the client what happens next.

**Procedure — resume.** Read `interview-state.json` + the last transcript
page only (never re-read the whole transcript); give the client a
3-sentence recap from `resume_hints` and the coverage table; continue from
the question queue. Log the new sitting in `session.sittings`.

**Procedure — segment boundary (bounded fresh context, FR-015).** The
interview is conducted in **bounded segments** (one module or small module
batch, or one sitting), not one ever-growing context. At a segment boundary —
a module close, a planned pause, or any point the orchestrator ends a segment:
1. Finish the current module's confirmed playback (never split a module across
   a boundary mid-playback).
2. Checkpoint the compact `interview-state.json` and flush the transcript page
   (`transcript.md` + `transcript.jsonl`) per the contracts above; set
   `resume_hints` (≤5 lines: where, what's pending, the next queued question);
   run the sanitization pass if the boundary is a pause or close.
3. **Return control to the orchestrator.** Do not keep conducting turns in the
   same context.
4. The next segment is a **fresh** interviewer context that re-hydrates **only**
   from: `interview-state.json`; the bounded last transcript window (the resume
   read above — never the whole transcript); the directly relevant
   current-module evidence; and the segment objective. It never inherits the
   previous segment's full internal history — the compact state is the carrier.
Turn numbering stays strictly monotonic across the seam (the next turn is
`last_turn + 1`, read from state / the last transcript line); every anchor a
later segment records still resolves to a turn already in the transcript, so
cross-segment `source_refs` never dangle. Segmentation is a context-cost
boundary only: it must not drop a register, a coverage status, an open
contradiction, or a pending risk-trigger upgrade — all of those live in the
state that each fresh segment reloads.

**Procedure — sanitization pass (close and every pause; R2-03).**
1. Sweep the working transcript for identifiers: third-party personal names
   → role aliases (`[contable]`, `[socio]`); phone numbers, emails, postal
   addresses, ID numbers → removed; the client business's own public name
   stays unless the operator directs otherwise.
2. Alias or remove only — statements are **kept verbatim** otherwise;
   rewording is not sanitization, it is evidence distortion.
3. Keep turn numbering identical to the unredacted text, so every
   `#turn-nnn` anchor resolves in both versions.
4. If anything was redacted: move the unredacted original to
   `evidence-raw/<same relative path>` (gitignored, local only) and stamp the
   committed transcript's front matter with `raw_ref: <path>` and
   `raw_sha256: <hash of the raw file>`. If nothing was redacted, no raw copy
   is created.
5. Sweep derived artifacts (state registers, trigger notes) for the same
   identifiers — evidence anchors keep them consistent.
6. Recordings and original client files always go to `evidence-raw/`;
   committed excerpts are minimized and indexed (`03` §6).

**Procedure — consent (M0).** Record the client's consent to record/
transcribe as `evidence/confirmations/consent-<session>.md` with date,
channel, and wording used.

**Outputs.** `transcript.md` + `transcript.jsonl` (sanitized when committed),
`interview-state.json`, consent record, raw counterparts in `evidence-raw/`
when redaction occurred.

**Self-checks.** Turn numbers strictly sequential with no gaps; every state
register entry's anchor resolves to an existing turn; after sanitization:
raw and committed turn counts identical, `raw_sha256` matches the raw file,
and a grep for the redacted identifiers over the committed tree comes back
empty.

**Failure modes.** Crash mid-turn → on restart, the transcript ends at the
last completed turn and state at the last checkpoint; re-ask the in-flight
question. State/schema mismatch → report to the operator and stop (repair is
not this skill's job). Redaction uncertainty (is this name third-party?) →
alias it and note the alias decision; over-aliasing identifiers is
recoverable from raw, leaked PII in Git is not.

**Must not:** paraphrase, summarize, or "clean up" client statements; edit or
renumber existing turns; write evidence-raw content into any committed path;
cite `evidence-raw/` from any generated artifact; collect credentials or
secrets into evidence; write outside the client repository.
