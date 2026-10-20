#!/usr/bin/env python3
"""Structure check for a mechanism map (therapeutic-mechanism-and-intervention-design).

Usage: python3 mechanism_map_check.py MAP.json [--json]

The map is JSON with: outcome, population, exclusions[], links[], components[],
assumptions[] (shape: evals/files/mechanism_map_illustrative.json), and optionally
mechanics[] (A3) and hazards[] (A4) (shape: evals/files/mechanics_safety_illustrative.json).

The script checks structure only: every component tied to an existing link, every
link with a measure or an explicit [GAP], TIDieR items 1 to 9 and 11 described,
adaptive components with a missing-data rule and stated reliability of tailoring
variables, a fixed function per component, and every assumption with a signal,
measure, milestone and stopper; for A3, every mechanic tied to a link, with an intended
use and justification or labeled "usage, not adherence", and its open flags; for A4,
every hazard with a design source, a mitigation, an indicator and the person's
threshold. It never judges whether a link holds, never
supplies a threshold, and never scores. Marks are reading aids, not findings.
Every [PAPER] row it prints carries its DOI.
"""
import json
import sys

DOI = {
    "TM8": "10.1136/bmj.n2061", "TM11": "10.1136/bmj.n2061", "TM9": "10.1136/bmj.n2061",
    "TM34": "10.1136/bmj.g1687", "TM36": "10.1136/bmj.g1687",
    "TM57": "10.1037/hea0000161",
    "TM84": "10.1007/s12160-016-9830-8", "TM88": "10.1007/s12160-016-9830-8",
    "TM89": "10.1007/s12160-016-9830-8",
    "TM97": "10.1136/bmj.h1258",
    "TM117": "10.1136/bmj.i6795",
    "TM87": "10.1007/s12160-016-9830-8",
    "SE86": "10.2196/jmir.7126", "SE89": "10.2196/jmir.7126",
    "SE90": "10.2196/jmir.8578", "SE92": "10.2196/jmir.8578",
}
WF = {"SE109", "SE110", "SE111", "SE112", "SE113", "SE117", "SE118"}
TIDIER_DESIGN_ITEMS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "11"]


def row(r):
    if r in DOI:
        return f"{r}, DOI {DOI[r]}"
    if r in WF:
        return f"{r} [WF]"
    return r


def blank(v):
    return v is None or (isinstance(v, str) and v.strip() in ("", "?"))


def check(m):
    out = {"structure": [], "links": [], "components": [], "assumptions": [], "mechanics": [], "hazards": []}
    links = {l["id"]: l for l in m.get("links", [])}

    if blank(m.get("outcome")):
        out["structure"].append(f"Distal outcome not stated [GAP] ({row('TM84')})")
    if blank(m.get("population")):
        out["structure"].append(f"For whom not stated [GAP] ({row('TM9')})")
    if not m.get("exclusions"):
        out["structure"].append(f"Not-for-whom not stated [GAP]; carry to B1 as an assumption ({row('TM9')})")

    for l in m.get("links", []):
        meas = l.get("measure")
        if blank(meas):
            out["links"].append(f"{l['id']} ({l.get('type')}): no measure named [GAP] ({row('TM97')})")
        elif str(meas).strip() == "[GAP]":
            out["links"].append(f"{l['id']} ({l.get('type')}): measure marked [GAP] by the person")

    for c in m.get("components", []):
        cid = f"{c['id']} {c.get('name', '')}".strip()
        lk = c.get("link")
        if blank(lk):
            out["components"].append(f"{cid}: not tied to a link; list as left out or proposed for removal ({row('TM8')})")
        elif lk not in links:
            out["components"].append(f"{cid}: names link {lk}, which is not in the map")
        t = c.get("tidier", {}) or {}
        open_items = [i for i in TIDIER_DESIGN_ITEMS if blank(t.get(i))]
        if open_items:
            out["components"].append(f"{cid}: TIDieR items not described ('?'): {', '.join(open_items)} ({row('TM36')}); items 10 and 12 not completed for a design ({row('TM34')})")
        if blank(c.get("fixed_function")):
            out["components"].append(f"{cid}: fixed function and permitted variation not agreed ({row('TM11')}, {row('TM117')})")
        a = c.get("adaptive")
        if a:
            if blank(a.get("missing_data_rule")):
                out["components"].append(f"{cid}: adaptive rule has no missing-data rule ({row('TM89')})")
            for tv in a.get("tailoring_variables", []):
                if blank(tv.get("reliability_or_validity")):
                    out["components"].append(f"{cid}: tailoring variable '{tv.get('name')}' has no stated reliability or validity; an assumption for B1 ({row('TM88')})")

    assumed_links = set()
    for a in m.get("assumptions", []):
        assumed_links.add(a.get("link"))
        missing = [f for f in ("signal", "measure", "milestone", "stopper") if blank(a.get(f))]
        if missing:
            note = []
            if "milestone" in missing:
                note.append(f"milestone is the person's, set in advance ({row('TM57')})")
            if "stopper" in missing:
                note.append("stopper: owner not named; ask")
            out["assumptions"].append(f"{a['id']} (link {a.get('link')}): missing {', '.join(missing)}" + (f"; {'; '.join(note)}" if note else ""))
    if m.get("assumptions"):
        for lid in links:
            if lid not in assumed_links:
                out["assumptions"].append(f"Link {lid} carries no assumption in the register")

    comp_ids = {c["id"] for c in m.get("components", [])}
    mech_ids = set()
    for k in m.get("mechanics", []) or []:
        mech_ids.add(k["id"])
        kid = f"{k['id']} {k.get('name', '')}".strip()
        lk = k.get("link")
        if blank(lk):
            out["mechanics"].append(f"{kid}: not tied to a link; list as not tied for the person to decide ({row('TM8')})")
        elif lk not in links:
            out["mechanics"].append(f"{kid}: names link {lk}, which is not in the map")
        if not blank(k.get("component")) and k.get("component") not in comp_ids:
            out["mechanics"].append(f"{kid}: names component {k.get('component')}, which is not in the map")
        if blank(k.get("usage_measure")):
            out["mechanics"].append(f"{kid}: no usage measure named [GAP]")
        if not blank(lk) and (blank(k.get("intended_use")) or blank(k.get("justification"))):
            out["mechanics"].append(f"{kid}: intended use or its justification not given; report as usage, not adherence ({row('SE90')}; {row('SE92')}); effective engagement is the person's to define ({row('SE86')})")
        for fl in k.get("flags", []) or []:
            if str(fl.get("status", "open")).lower() != "settled":
                out["mechanics"].append(f"{kid}: flag open: {fl.get('pattern')} ({row(fl.get('row', '?'))}); for the owner the person names, or owner not named")
        if not blank(k.get("health_risk")):
            out["mechanics"].append(f"{kid}: possible risk to health noted ({k.get('health_risk')}); carry to A4 as a hazard source, unrated")
    if m.get("mechanics") and m.get("links"):
        engagement_links = [l for l in links.values() if l.get("type") == "outcome" and any(w in str(l.get("text", "")).lower() for w in ("engagement", "usage", "retention", "sessions"))]
        for l in engagement_links:
            out["mechanics"].append(f"Link {l['id']} reads engagement as the outcome; engagement is a proximal outcome ({row('TM87')})")

    known_sources = set(links) | comp_ids | mech_ids
    for h in m.get("hazards", []) or []:
        hid = f"{h['id']}"
        src = h.get("source")
        if blank(src):
            out["hazards"].append(f"{hid}: no source in the design (link, component or mechanic) named")
        elif src not in known_sources:
            out["hazards"].append(f"{hid}: names source {src}, which is not in the map")
        if blank(h.get("mitigation")):
            out["hazards"].append(f"{hid}: mitigation not given; ask")
        if blank(h.get("indicator")):
            out["hazards"].append(f"{hid}: no indicator for after launch named")
        if blank(h.get("threshold")):
            out["hazards"].append(f"{hid}: threshold not given; the person sets it before launch (SE63, MDCG 2025-10, not legally binding)")
    tied_sources = {h.get("source") for h in m.get("hazards", []) or []}
    for k in m.get("mechanics", []) or []:
        if not blank(k.get("health_risk")) and m.get("hazards") is not None and k["id"] not in tied_sources:
            out["hazards"].append(f"Mechanic {k['id']} notes a possible risk to health but no hazard names it")

    counts = {
        "links": len(links),
        "links_with_measure": sum(1 for l in links.values() if not blank(l.get("measure")) and str(l.get("measure")).strip() != "[GAP]"),
        "components": len(m.get("components", [])),
        "components_tied": sum(1 for c in m.get("components", []) if not blank(c.get("link")) and c.get("link") in links),
        "assumptions": len(m.get("assumptions", [])),
        "assumptions_complete": sum(1 for a in m.get("assumptions", []) if all(not blank(a.get(f)) for f in ("signal", "measure", "milestone", "stopper"))),
        "mechanics": len(m.get("mechanics", []) or []),
        "mechanics_tied": sum(1 for k in m.get("mechanics", []) or [] if not blank(k.get("link")) and k.get("link") in links),
        "hazards": len(m.get("hazards", []) or []),
        "hazards_complete": sum(1 for h in m.get("hazards", []) or [] if all(not blank(h.get(f)) for f in ("source", "mitigation", "indicator", "threshold"))),
    }
    return counts, out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    m = json.load(open(sys.argv[1]))
    counts, out = check(m)
    if "--json" in sys.argv:
        print(json.dumps({"counts": counts, "findings": out}, indent=1))
        return
    label = m.get("label", "")
    print(f"# Mechanism map structure check: {m.get('product', 'unnamed')}" + (f" ({label})" if label else ""))
    print()
    print("Structure marks only. Not a finding about whether any link holds, and not a score.")
    print()
    c = counts
    print(f"- Links: {c['links']} ({c['links_with_measure']} with a measure named)")
    print(f"- Components: {c['components']} ({c['components_tied']} tied to a link)")
    print(f"- Assumptions: {c['assumptions']} ({c['assumptions_complete']} with signal, measure, milestone and stopper)")
    sections = [("structure", "Chain"), ("links", "Links"), ("components", "Components"), ("assumptions", "Assumptions")]
    if "mechanics" in m:
        print(f"- Mechanics: {c['mechanics']} ({c['mechanics_tied']} tied to a link)")
        sections.append(("mechanics", "Mechanics (A3)"))
    if "hazards" in m:
        print(f"- Hazards: {c['hazards']} ({c['hazards_complete']} with source, mitigation, indicator and threshold)")
        sections.append(("hazards", "Hazards (A4)"))
    for sec, title in sections:
        print()
        print(f"## {title}")
        if out[sec]:
            for f in out[sec]:
                print(f"- {f}")
        else:
            print("- No structural gap found.")


if __name__ == "__main__":
    main()
