#!/usr/bin/env python3
"""ID and reference integrity across structured artifacts (06 §4, 08 §6).

Usage: check-ids.py <client-dir>

S0b scope — registries that exist at discovery:
  docs/requirements/requirements.yaml   (OBJ/FR/NFR/INT/CON/DAT, BR, ASM, ACs)
  docs/requirements/open-questions.yaml (OQ/CLAR, CTR)
  docs/handoffs/G*-*.yaml               (filename ↔ gate/sequence fields)
  project.yaml counters                 (allocation contract: used < counter)

Checks: duplicate IDs · AC scoping to parent · counter collisions ·
dangling references. References with a prefix whose registry does not exist
yet at this stage (e.g. ADR, TASK before S3) are skipped — their registries
gain checks when their schemas land (R2-02 build-at-first-consumer).

Missing artifact files are skipped silently: presence is the validator's
profile-matrix concern, not this checker's.

Exit codes: 0 clean · 1 findings (printed as 'ID-ERROR: …') · 2 operational.
"""
import os
import re
import sys


def _load(path):
    import yaml
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return data if isinstance(data, dict) else {}


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    client = argv[1]
    if not os.path.isdir(client):
        print(f"ERROR: not a directory: {client}", file=sys.stderr)
        return 2

    errors = []
    ids = {}          # id -> description of where it lives
    req_ids = set()   # requirement ids only (for depends_on/conflicts_with)

    def register(ident, where):
        if ident in ids:
            errors.append(f"duplicate ID {ident} ({ids[ident]} and {where})")
        else:
            ids[ident] = where

    req_path = os.path.join(client, "docs/requirements/requirements.yaml")
    reqs = _load(req_path) if os.path.isfile(req_path) else {}
    for obj in reqs.get("objectives") or []:
        register(obj.get("id", "?"), "objectives")
    for req in reqs.get("requirements") or []:
        rid = req.get("id", "?")
        register(rid, "requirements")
        req_ids.add(rid)
        for ac in req.get("acceptance_criteria") or []:
            acid = ac.get("id", "?")
            register(acid, f"{rid} acceptance_criteria")
            if not acid.startswith(f"{rid}-AC-"):
                errors.append(f"AC {acid} not scoped to its parent {rid} (06 §4)")
    for br in reqs.get("business_rules") or []:
        register(br.get("id", "?"), "business_rules")
    for asm in reqs.get("assumptions") or []:
        register(asm.get("id", "?"), "assumptions")

    oq_path = os.path.join(client, "docs/requirements/open-questions.yaml")
    oq = _load(oq_path) if os.path.isfile(oq_path) else {}
    for q in oq.get("questions") or []:
        register(q.get("id", "?"), "open-questions questions")
    for c in oq.get("contradictions") or []:
        register(c.get("id", "?"), "open-questions contradictions")

    # Counter allocation contract: every used number is below its counter.
    proj_path = os.path.join(client, "project.yaml")
    counters = (_load(proj_path) if os.path.isfile(proj_path) else {}).get("counters") or {}
    id_re = re.compile(r"^([A-Z]+)-([0-9]{3})(?:-(?:AC|T)-[0-9]{2})?$")
    for ident in ids:
        m = id_re.match(ident)
        if not m:
            continue
        prefix, num = m.group(1), int(m.group(2))
        if prefix in counters and num >= int(counters[prefix]):
            errors.append(
                f"counter collision: {ident} used but counter {prefix}={counters[prefix]} "
                f"has not allocated it (06 §4: counters hold the next free number)")

    # Dangling references — only into registries that exist at this stage.
    known_prefixes = {id_re.match(i).group(1) for i in ids if id_re.match(i)}

    def check_ref(owner, ref):
        m = id_re.match(str(ref))
        if not m:
            return  # anchors like interview:...#turn-nnn are evidence refs, not IDs
        if m.group(1) in known_prefixes and str(ref) not in ids:
            errors.append(f"{owner}: dangling reference to {ref}")

    for req in reqs.get("requirements") or []:
        rid = req.get("id", "?")
        for field in ("objectives", "business_rules", "assumptions",
                      "depends_on", "conflicts_with"):
            for ref in req.get(field) or []:
                check_ref(f"{rid}.{field}", ref)
    for q in oq.get("questions") or []:
        for ref in q.get("blocks") or []:
            check_ref(f"{q.get('id', '?')}.blocks", ref)

    # Handoff filenames carry the record's identity (R2-05).
    hdir = os.path.join(client, "docs/handoffs")
    fname_re = re.compile(r"^(G[0-9])-[a-z0-9-]+-([0-9]{2})\.yaml$")
    if os.path.isdir(hdir):
        for fname in sorted(os.listdir(hdir)):
            if not fname.endswith(".yaml"):
                continue
            m = fname_re.match(fname)
            if not m:
                errors.append(
                    f"handoff filename '{fname}' does not match G<n>-<slug>-<seq>.yaml (R2-05)")
                continue
            rec = _load(os.path.join(hdir, fname))
            if rec.get("gate") != m.group(1):
                errors.append(f"{fname}: gate field '{rec.get('gate')}' != filename gate {m.group(1)}")
            if rec.get("sequence") != int(m.group(2)):
                errors.append(f"{fname}: sequence field '{rec.get('sequence')}' != filename seq {int(m.group(2))}")

    for e in errors:
        print(f"ID-ERROR: {e}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
