#!/usr/bin/env python3
"""interview-segment-seam-check.py <fixture-dir> — deterministic seam checks for
a BOUNDED, SEGMENTED discovery interview (04 §6, FR-015, TASK-023).

Scenario 05 ran as one continuously accumulating interviewer context (peak
~112k-token final-turn footprint). The correction runs the interview as a
sequence of bounded *fresh* interviewer segments, each re-hydrated only from the
compact ``interview-state.json`` + a bounded last transcript window + the
current-module evidence — never the previous segment's full internal history.

The schema bounds the *shape* of one state; the single-state replay checker
(``interview-replay-check.py``) bounds cost/evidence for one snapshot. THIS
checker bounds the *seam* between segments: that turn numbering, anchors,
registers, and coverage remain continuous and unique across a multi-segment run,
that each fresh segment re-hydrated from a bounded window (not the whole
transcript, and not the prior segment's full history), and that a module playback
opens each non-first segment.

Fixture layout (fictitious client only)::

    <fixture-dir>/
      seg-01/  meta.json  interview-state.json  transcript.jsonl
      seg-02/  meta.json  interview-state.json  transcript.jsonl
      ...

``meta.json`` per segment::

    {"order": 1, "module": "M6",
     "rehydration": {"full_history": false, "window_turns": 0},
     "opening_playback": false}

``transcript.jsonl`` holds only THAT segment's new turns; concatenated in order
they must form 1..N. ``interview-state.json`` is the compact working state as it
stood at that segment's close.

Invariants checked:

  * segment count       — a bounded run uses >= 2 fresh segments;
  * turn sequence       — each segment's turns start at prev_max+1 and are
    contiguous; the concatenation is 1..N with no gap/dup at any seam;
  * no full history     — every non-first segment declares full_history:false
    (it re-hydrated from state, not from the prior context);
  * bounded re-hydration — every non-first segment's window_turns is <= the
    window ceiling and, once the prior transcript exceeds that ceiling, strictly
    smaller than the whole prior transcript (never re-reads everything);
  * boundary playback    — every non-first segment opens with a playback and a
    non-empty resume_hints (the fresh context recaps before continuing);
  * anchor integrity     — every #turn-nnn / scope_flags.turn a segment's state
    references resolves to a turn present up to the end of that segment;
  * register continuity  — no register id (CTR/ASM/OQ) or scope_flag turn present
    in an earlier segment is dropped by a later one (append-only across seams:
    this is how a proposed risk-trigger upgrade survives re-hydration);
  * coverage continuity  — no coverage node id is dropped across a seam;
  * compact working state — each coverage note / resume_hints stays within the
    working-annotation ceiling in every segment;
  * no S2/S3 leakage      — no PRD/technical-design output marker in any segment.

Exit 0 and print ``INTERVIEW-SEAM: PASS`` with metrics on success; exit 1 and
print one stable ``VIOLATION <TOKEN>`` line per failure otherwise. Stdlib +
PyYAML only — no pytest, no new dependency.
"""
import json
import os
import re
import sys

import yaml

NOTES_MAX = 600       # bytes: ceiling for a single coverage-node working annotation
RESUME_MAX = 800      # bytes: ceiling for resume_hints
WINDOW_MAX = 8        # turns: re-hydration window ceiling (matches replay WINDOWS max)

LEAKAGE = [
    (r"\bADR-[0-9]", "ADR-decision"),
    (r"\bSDD\b", "SDD"),
    (r"\bPRD\b", "PRD"),
    (r"\bDDL\b", "DDL"),
    (r"CREATE\s+TABLE", "DDL"),
    (r"delivery[\s-]backlog", "delivery-backlog"),
]


def load_segments(d):
    segs = []
    for name in sorted(os.listdir(d)):
        p = os.path.join(d, name)
        if not (os.path.isdir(p) and name.startswith("seg-")):
            continue
        with open(f"{p}/meta.json", encoding="utf-8") as fh:
            meta = json.load(fh)
        with open(f"{p}/interview-state.json", encoding="utf-8") as fh:
            state = yaml.safe_load(fh)
        turns = []
        with open(f"{p}/transcript.jsonl", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    turns.append(json.loads(line))
        segs.append({"name": name, "meta": meta, "state": state, "turns": turns})
    segs.sort(key=lambda s: s["meta"].get("order", 0))
    return segs


def reg_ids(state):
    r = state.get("registers", {}) or {}
    ids = set()
    for key in ("contradictions", "assumptions", "open_questions"):
        for item in r.get(key, []) or []:
            if item.get("id"):
                ids.add(f"{key}:{item['id']}")
    for sf in r.get("scope_flags", []) or []:
        if isinstance(sf.get("turn"), int):
            ids.add(f"scope_flag:turn-{sf['turn']}")
    return ids


def cov_ids(state):
    return {n["id"] for n in state.get("coverage", []) or [] if n.get("id")}


def main():
    if len(sys.argv) != 2:
        print("usage: interview-segment-seam-check.py <fixture-dir>", file=sys.stderr)
        return 2
    d = sys.argv[1].rstrip("/")
    segs = load_segments(d)

    violations = []

    def bad(token, msg):
        violations.append(token)
        print(f"VIOLATION {token}: {msg}", file=sys.stderr)

    if len(segs) < 2:
        bad("SEGMENT-COUNT",
            f"a bounded segmented run needs >= 2 fresh segments, found {len(segs)}")

    running = 0                 # highest turn number seen so far
    cumulative = []             # all turns seen so far, in order
    prev_regs = set()
    prev_covs = set()
    max_window = 0

    for i, seg in enumerate(segs):
        first = (i == 0)
        state, turns, meta = seg["state"], seg["turns"], seg["meta"]
        nums = [int(t["turn"]) for t in turns]

        # -- turn sequence across the seam
        if nums:
            if nums != list(range(nums[0], nums[0] + len(nums))):
                bad("TURN-SEQUENCE",
                    f"{seg['name']} turns not internally contiguous: {nums}")
            if nums[0] != running + 1:
                bad("TURN-SEQUENCE",
                    f"{seg['name']} starts at turn-{nums[0]:03d}, expected "
                    f"turn-{running + 1:03d} (gap/overlap at seam)")
            running = max(running, nums[-1])
        cumulative.extend(turns)
        present = {int(t["turn"]) for t in cumulative}

        rehy = meta.get("rehydration", {}) or {}

        # -- no full history + bounded re-hydration (non-first segments)
        if not first:
            if rehy.get("full_history") is not False:
                bad("FULL-HISTORY-CARRIED",
                    f"{seg['name']} must re-hydrate from state, not the prior "
                    f"segment's full history (rehydration.full_history != false)")
            w = rehy.get("window_turns")
            if not isinstance(w, int) or w < 1:
                bad("NO-REHYDRATION-WINDOW",
                    f"{seg['name']} declares no bounded transcript window")
            else:
                max_window = max(max_window, w)
                prior = running - len(nums)   # turns that existed before this segment
                if w > WINDOW_MAX:
                    bad("UNBOUNDED-REHYDRATION",
                        f"{seg['name']} window {w} > ceiling {WINDOW_MAX}")
                elif prior > WINDOW_MAX and w >= prior:
                    bad("UNBOUNDED-REHYDRATION",
                        f"{seg['name']} window {w} not smaller than the whole "
                        f"prior transcript ({prior} turns) — re-reads everything")
            # -- boundary playback
            if meta.get("opening_playback") is not True:
                bad("MISSING-PLAYBACK",
                    f"{seg['name']} does not open with a boundary playback")
            if not (state.get("resume_hints") or "").strip():
                bad("MISSING-PLAYBACK",
                    f"{seg['name']} has empty resume_hints — fresh context cannot recap")

        raw = json.dumps(state, ensure_ascii=False)

        # -- anchor integrity across the seam
        anchors = {int(n) for n in re.findall(r"#turn-0*([0-9]+)", raw)}
        for sf in state.get("registers", {}).get("scope_flags", []) or []:
            if isinstance(sf.get("turn"), int):
                anchors.add(sf["turn"])
        for a in sorted(anchors):
            if a not in present:
                bad("DANGLING-ANCHOR",
                    f"{seg['name']} state references turn-{a:03d}, absent from the "
                    f"transcript through this segment")

        # -- register / coverage continuity (append-only across seams)
        regs, covs = reg_ids(state), cov_ids(state)
        dropped_r = prev_regs - regs
        if dropped_r:
            bad("REGISTER-DROPPED",
                f"{seg['name']} dropped register(s) {sorted(dropped_r)} carried by "
                f"the previous segment — a re-hydrated segment must retain them "
                f"(this is how a proposed trigger upgrade survives)")
        dropped_c = prev_covs - covs
        if dropped_c:
            bad("COVERAGE-DROPPED",
                f"{seg['name']} dropped coverage node(s) {sorted(dropped_c)} across "
                f"the seam")
        prev_regs, prev_covs = prev_regs | regs, prev_covs | covs

        # -- compact working state
        for node in state.get("coverage", []) or []:
            nb = len((node.get("notes") or "").encode("utf-8"))
            if nb > NOTES_MAX:
                bad("NOTE-TOO-LONG",
                    f"{seg['name']} {node.get('id')} notes {nb}B > {NOTES_MAX}B")
        rb = len((state.get("resume_hints") or "").encode("utf-8"))
        if rb > RESUME_MAX:
            bad("RESUME-HINTS-TOO-LONG", f"{seg['name']} resume_hints {rb}B > {RESUME_MAX}B")

        # -- no S2/S3 leakage
        for pat, tok in LEAKAGE:
            if re.search(pat, raw, re.I):
                bad("LEAKAGE", f"{seg['name']} working state carries {tok}")

    # -- final concatenation is 1..N contiguous
    seq = sorted(int(t["turn"]) for t in cumulative)
    if seq != list(range(1, len(seq) + 1)):
        bad("TURN-SEQUENCE", f"concatenated turns are not 1..N contiguous: {seq}")

    if violations:
        print(f"INTERVIEW-SEAM: FAIL ({len(violations)} violation(s))", file=sys.stderr)
        return 1

    print(
        "INTERVIEW-SEAM: PASS — "
        f"segments={len(segs)} total_turns={len(cumulative)} "
        f"max_window={max_window} registers={len(prev_regs)} "
        f"coverage_nodes={len(prev_covs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
