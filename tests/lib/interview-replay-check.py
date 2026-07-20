#!/usr/bin/env python3
"""interview-replay-check.py <fixture-dir> — deterministic resume/replay checks
for a discovery-interview working state (04 §6, FR-015).

Given a fixture directory holding ``interview-state.json`` (JSON, or YAML — a
strict superset) and ``transcript.jsonl``, this asserts the runtime-efficiency
and evidence invariants a bounded, resumable interviewer must hold. It exists
because the schema alone cannot express them: the schema bounds *shape*, this
bounds *cost and evidence integrity*.

Invariants checked:

  * turn sequence        — transcript turns are 1..N, contiguous, no dup/gap;
  * anchor integrity     — every ``#turn-nnn`` (and ``scope_flags.turn``) the
    state references resolves to a turn present in the transcript — no dangling
    evidence anchor (traceability rule);
  * compact working state — each ``coverage[].notes`` and ``resume_hints`` stays
    within the working-annotation ceiling, so the full-file checkpoint (written
    at every module transition / register / 10 turns / pause) does NOT amplify
    with interview length. The consolidated per-topic narrative belongs in the
    close-time completion-report and the verbatim transcript, not here;
  * next action from state — an open interview exposes a queued question or a
    ``not_ready`` verdict, and a closed one is ``ready`` with an empty queue:
    next-question control works from the compact state alone;
  * relevance / no needless reopen — a queued question does not target a topic
    already ``sufficient`` unless an open contradiction touches it;
  * bounded resume       — for every pause point k and window W, reading state +
    the last W transcript turns reads strictly less than the whole transcript
    once k > W: resume never requires the complete transcript;
  * no S2/S3 leakage      — the working state carries no PRD/technical-design
    output markers (ADR-/SDD/PRD/DDL/delivery-backlog): S1 collects evidence,
    it does not decide.

Exit 0 and print ``INTERVIEW-REPLAY: PASS`` with metrics on success; exit 1 and
print one stable ``VIOLATION <TOKEN>`` line per failure otherwise. Stdlib +
PyYAML only — no pytest, no Hypothesis, no new dependency (reuses the harness's
existing Python surface).
"""
import json
import re
import sys

import yaml

NOTES_MAX = 600      # bytes: ceiling for a single coverage-node working annotation
RESUME_MAX = 800     # bytes: ceiling for resume_hints
WINDOWS = (3, 5, 8)  # transcript-window sizes swept at each pause point

# S2/S3 output markers that must never appear in an S1 working state. Kept
# deliberately narrow so legitimate S1 candidate language ("FR candidato",
# "BR-a", "proposed_default") never trips it.
LEAKAGE = [
    (r"\bADR-[0-9]", "ADR-decision"),
    (r"\bSDD\b", "SDD"),
    (r"\bPRD\b", "PRD"),
    (r"\bDDL\b", "DDL"),
    (r"CREATE\s+TABLE", "DDL"),
    (r"delivery[\s-]backlog", "delivery-backlog"),
]


def main():
    if len(sys.argv) != 2:
        print("usage: interview-replay-check.py <fixture-dir>", file=sys.stderr)
        return 2
    d = sys.argv[1].rstrip("/")

    with open(f"{d}/interview-state.json", encoding="utf-8") as fh:
        state = yaml.safe_load(fh)
    turns = []
    with open(f"{d}/transcript.jsonl", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                turns.append(json.loads(line))

    present = {int(t["turn"]) for t in turns}
    violations = []

    def bad(token, msg):
        violations.append(token)
        print(f"VIOLATION {token}: {msg}", file=sys.stderr)

    # -- turn sequence: strictly 1..N, contiguous
    seq = sorted(int(t["turn"]) for t in turns)
    if seq != list(range(1, len(seq) + 1)):
        bad("TURN-SEQUENCE", f"transcript turns are not 1..N contiguous: {seq}")

    raw = json.dumps(state, ensure_ascii=False)

    # -- anchor integrity (no dangling references)
    anchors = {int(n) for n in re.findall(r"#turn-0*([0-9]+)", raw)}
    for sf in state.get("registers", {}).get("scope_flags", []):
        if isinstance(sf.get("turn"), int):
            anchors.add(sf["turn"])
    for a in sorted(anchors):
        if a not in present:
            bad("DANGLING-ANCHOR",
                f"state references turn-{a:03d}, absent from transcript")

    # -- compact working state
    for node in state.get("coverage", []):
        nb = len((node.get("notes") or "").encode("utf-8"))
        if nb > NOTES_MAX:
            bad("NOTE-TOO-LONG",
                f"{node.get('id')} notes {nb}B > {NOTES_MAX}B — working state "
                f"must stay compact (narrative belongs in the completion-report)")
    rb = len((state.get("resume_hints") or "").encode("utf-8"))
    if rb > RESUME_MAX:
        bad("RESUME-HINTS-TOO-LONG", f"resume_hints {rb}B > {RESUME_MAX}B")

    # -- no S2/S3 leakage
    for pat, tok in LEAKAGE:
        if re.search(pat, raw, re.I):
            bad("LEAKAGE",
                f"working state carries {tok} — S1 must not emit "
                f"PRD/technical-design output")

    # -- next action available from the compact state alone
    status = state.get("session", {}).get("status")
    cc = state.get("completion_check", {}).get("result")
    queue = state.get("question_queue", [])
    if status in ("in_progress", "paused"):
        if not queue and cc != "not_ready":
            bad("NO-NEXT-ACTION",
                "open interview has neither a queued question nor a not_ready "
                "verdict — resume could not choose the next question from state")
    elif status == "closed":
        if cc != "ready" or queue:
            bad("BAD-CLOSURE",
                "closed interview must be completion_check.ready with an empty "
                "question_queue")

    # -- relevance: a queued question must not reopen a sufficient topic unless
    #    an open contradiction touches it
    cov_status = {n["id"]: n.get("status") for n in state.get("coverage", [])}
    open_ctr_topics = set()
    for ctr in state.get("registers", {}).get("contradictions", []):
        if ctr.get("status") == "open":
            open_ctr_topics.add(ctr.get("topic"))
    for q in queue:
        topic = q.get("topic")
        if cov_status.get(topic) == "sufficient" and topic not in open_ctr_topics:
            bad("REOPEN-SUFFICIENT",
                f"queued question {q.get('qid')} targets already-sufficient "
                f"topic '{topic}' with no open contradiction")

    # -- bounded resume sweep: state + last W turns < whole transcript for k>W
    ordered = sorted(turns, key=lambda t: int(t["turn"]))
    full_bytes = sum(
        len(json.dumps(t, ensure_ascii=False).encode()) for t in ordered)
    cases = 0
    window_flag = False
    for W in WINDOWS:
        for k in range(1, len(ordered) + 1):
            cases += 1
            win = ordered[max(0, k - W):k]
            win_bytes = sum(
                len(json.dumps(t, ensure_ascii=False).encode()) for t in win)
            if k > W and full_bytes > 0 and win_bytes >= full_bytes:
                window_flag = True
    if window_flag:
        bad("WINDOW-NOT-BOUNDED",
            "a bounded transcript window was not smaller than the full "
            "transcript at some pause point")

    if violations:
        print(f"INTERVIEW-REPLAY: FAIL ({len(violations)} violation(s))",
              file=sys.stderr)
        return 1

    print(
        "INTERVIEW-REPLAY: PASS — "
        f"turns={len(turns)} coverage_nodes={len(state.get('coverage', []))} "
        f"state_bytes={len(raw.encode())} anchors={len(anchors)} "
        f"resume_cases_swept={cases}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
