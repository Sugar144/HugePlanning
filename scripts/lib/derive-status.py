#!/usr/bin/env python3
"""Derive the client-project dashboard (DEC-11: derived live, never stored).

Usage: derive-status.py <client-dir>

Reads project.yaml, docs/handoffs/, docs/requirements/*.yaml and prints the
status report to stdout. Read-only; missing artifacts render as absent lines,
never as errors (validation is validate.sh's job, not this reporter's).

Exit codes: 0 report printed · 2 operational error (unreadable client).
"""
import os
import re
import sys


def _load(path):
    import yaml
    try:
        with open(path, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    client = argv[1]
    if not os.path.isdir(client):
        print(f"ERROR: not a directory: {client}", file=sys.stderr)
        return 2

    proj = _load(os.path.join(client, "project.yaml"))
    p = proj.get("project") or {}
    wf = proj.get("workflow") or {}
    print(f"project: {p.get('id', '?')} · profile: {p.get('profile', '?')} · "
          f"stage: {wf.get('current_stage', '?')} ({wf.get('stage_status', '?')})")

    # Gate states: latest sequence per gate from append-only records (R2-05).
    latest = {}
    hdir = os.path.join(client, "docs/handoffs")
    fname_re = re.compile(r"^(G[0-9])-[a-z0-9-]+-([0-9]{2})\.yaml$")
    if os.path.isdir(hdir):
        for fname in sorted(os.listdir(hdir)):
            m = fname_re.match(fname)
            if not m:
                continue
            gate, seq = m.group(1), int(m.group(2))
            if gate not in latest or seq > latest[gate][0]:
                latest[gate] = (seq, _load(os.path.join(hdir, fname)))
    print("gates:")
    for n in range(10):
        gate = f"G{n}"
        if gate in latest:
            seq, rec = latest[gate]
            print(f"  {gate}: {rec.get('result', '?')} "
                  f"(seq {seq}, {rec.get('date', '?')}, by {rec.get('approved_by', '?')})")
        else:
            print(f"  {gate}: no record")

    reqs = _load(os.path.join(client, "docs/requirements/requirements.yaml"))
    items = reqs.get("requirements") or []
    if items:
        hist = {}
        for r in items:
            hist[r.get("status", "?")] = hist.get(r.get("status", "?"), 0) + 1
        counts = " · ".join(f"{k}: {v}" for k, v in sorted(hist.items()))
        print(f"requirements: {counts} (total {len(items)})")
    else:
        print("requirements: none recorded")

    oq = _load(os.path.join(client, "docs/requirements/open-questions.yaml"))
    qs = oq.get("questions") or []
    open_qs = [q for q in qs if q.get("status") == "open"]
    blocking = [q for q in open_qs if q.get("blocking")]
    ctrs = oq.get("contradictions") or []
    open_ctrs = [c for c in ctrs if c.get("status") == "open"]
    print(f"open questions: {len(open_qs)} open of {len(qs)} "
          f"({len(blocking)} blocking) · contradictions: {len(open_ctrs)} open of {len(ctrs)}")

    ctx = _load(os.path.join(client, "docs/requirements/solution-context.yaml"))
    triggers = ctx.get("risk_triggers") or []
    pending = [t for t in triggers if t.get("status") == "proposed"]
    if pending:
        names = "; ".join(t.get("trigger", "?") for t in pending)
        print(f"risk triggers: {len(pending)} PENDING of {len(triggers)} — {names}")
    else:
        print(f"risk triggers: {len(triggers)} recorded, none pending")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
