#!/usr/bin/env python3
"""Turn a content map plus the person's inventory into a dossier status table.

Usage:
  python3 dossier_gaps.py --route fda-de-novo [--software basic|enhanced] [--pccp]
                          [--inventory inventory.csv] [--format md|json]

inventory.csv columns (header row required): section_id,status,owner,file,note
  status is the person's word: ready, draft, missing, not applicable (anything else is kept as written).
  owner is the name the person gave; an empty owner prints "owner not named".

The script never decides that a section applies or is ready. It lists every section the
source names for the route, shows what the person said about it, and marks a section the
person did not mention as [GAP] (not in the inventory). Sections the source marks
"if applicable" keep that wording so the regulatory owner can rule on them.
"""
import argparse, csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAPS = os.path.join(HERE, "..", "references", "content-maps.json")


def load_sections(route, software, pccp):
    data = json.load(open(MAPS, encoding="utf-8"))
    if route not in data["routes"]:
        sys.exit("unknown route %r; choose from %s" % (route, ", ".join(data["routes"])))
    r = data["routes"][route]
    rows = [dict(s, group=r["label"]) for s in r["sections"]]
    if software:
        if not route.startswith("fda-"):
            sys.exit("--software is the FDA documentation-level overlay; for the EU use the eu-mdr route (Annex II 6.1(b))")
        ov = data["overlays"]["fda-software"]
        for s in ov["sections"]:
            if s["level"] == "enhanced" and software == "basic":
                rows.append(dict(s, group=ov["label"], applies="not recommended in a Basic submission; kept in the design history file (S-06)"))
            else:
                rows.append(dict(s, group=ov["label"], applies="always at this level"))
    if pccp:
        if not route.startswith("fda-"):
            sys.exit("--pccp is the FDA PCCP section; EU pre-determined changes are described in the technical documentation (AI EU-30)")
        ov = data["overlays"]["fda-pccp"]
        rows += [dict(s, group=ov["label"], applies=s["level"]) for s in ov["sections"]]
    return r["label"], rows


def load_inventory(path):
    if not path:
        return {}
    inv = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sid = (row.get("section_id") or "").strip()
            if sid:
                inv[sid] = {k: (v or "").strip() for k, v in row.items()}
    return inv


def build(route, software, pccp, inventory):
    label, sections = load_sections(route, software, pccp)
    inv = load_inventory(inventory)
    known = {s["id"] for s in sections}
    out = []
    for s in sections:
        i = inv.get(s["id"])
        if i is None:
            status, owner, file_, note = "[GAP] not in the inventory", "owner not named", "", ""
        else:
            status = i.get("status") or "[GAP] status not given"
            owner = i.get("owner") or "owner not named"
            file_, note = i.get("file", ""), i.get("note", "")
        out.append({"section_id": s["id"], "section": s["name"], "applies": s.get("applies", ""),
                    "source_row": s["row"], "status": status, "owner": owner, "file": file_, "note": note})
    extra = sorted(set(inv) - known)
    counts = {}
    for o in out:
        key = o["status"].split()[0].lower() if not o["status"].startswith("[GAP]") else "[GAP]"
        counts[key] = counts.get(key, 0) + 1
    return {"route": label, "sections": out, "counts": counts,
            "inventory_items_not_in_map": extra,
            "owners_not_named": sum(1 for o in out if o["owner"] == "owner not named")}


def to_md(res):
    lines = ["Route: " + res["route"], "",
             "| Section | When the source says it applies | Status (person's word) | Owner | File | Source row |",
             "|---|---|---|---|---|---|"]
    for o in res["sections"]:
        lines.append("| %s | %s | %s | %s | %s | %s |" % (o["section"], o["applies"], o["status"], o["owner"], o["file"], o["source_row"]))
    lines += ["", "Counts by status: " + ", ".join("%s %d" % kv for kv in sorted(res["counts"].items())),
              "Sections with no owner named: %d" % res["owners_not_named"]]
    if res["inventory_items_not_in_map"]:
        lines.append("Inventory items the source map does not name (ask the regulatory owner where they belong): " + ", ".join(res["inventory_items_not_in_map"]))
    return "\n".join(lines)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--route", required=True)
    ap.add_argument("--software", choices=["basic", "enhanced"])
    ap.add_argument("--pccp", action="store_true")
    ap.add_argument("--inventory")
    ap.add_argument("--format", choices=["md", "json"], default="md")
    a = ap.parse_args()
    res = build(a.route, a.software, a.pccp, a.inventory)
    print(to_md(res) if a.format == "md" else json.dumps(res, indent=2, ensure_ascii=False))
