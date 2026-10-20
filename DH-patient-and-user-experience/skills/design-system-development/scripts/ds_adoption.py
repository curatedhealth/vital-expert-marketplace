#!/usr/bin/env python3
"""Component adoption and drift from the person's own design-system inventory.

Reads one CSV (nothing is sent anywhere). One row per component version in use, with the
products (or surfaces) that use that version.

Required columns (header names are matched case-insensitively):
  component              name of the component, as the person writes it
  version                the version of the component in use (for example 3.2.0, or v10)
  products               the products or surfaces using that version, separated by ";"
                         (a column named "product" with one value per row also works)
  accessibility_status   the person's own status for that component version, as written
                         (for example "tested WCAG 2.2 AA 2026-09", "2 issues open", "not tested")

Optional columns:
  current_version        the version the person declares current for the component
  owner                  who owns the product(s) on the row, in the person's words
  clinical               yes/no: the row's products include a clinical task surface
  device_ui              yes/no: the row's products include a medical device user interface
  modification           none / override / fork (the person's record of local changes)
  lifecycle              the person's lifecycle status for the component (for example
                         trial, stable, experimental, use with caution, deprecated)

Options:
  --current FILE         CSV with columns component,current_version (overrides the column)
  --products "A;B;C"     the person's full product list, so adoption can be read against
                         every product, including ones that use no listed component
  --flag "deprecated;use with caution;retired"
                         lifecycle values to list as in use (default shown; these are the
                         USWDS status names, research rows DSX-28 and DSX-29; give your own)

What it computes, with no threshold and no verdict:
  adoption     products using each component (any version), and on the current version
  drift        per component and product: same as current, behind (major, minor or patch
               distance when both versions are dotted numbers), ahead of current (an
               inconsistency to check), or differs (distance not computable)
  by owner     uses behind current, by owner; clinical and device-UI uses shown separately
  spread       number of distinct versions of each component in use
  accessibility  status values as the person wrote them, per component version, and for
               clinical and device-UI uses
  modification   override and fork counts per component (local drift from the system)
  lifecycle    uses of components carrying a flagged lifecycle value

If no current version is given for a component, the highest version in the inventory is
used and the output says so: it is not the person's declared current version.

Usage: python3 ds_adoption.py INVENTORY.csv [--current FILE] [--products "A;B"] [--flag "x;y"]
"""
import argparse
import csv
import re
import sys
from collections import Counter, defaultdict

YES = {"yes", "y", "true", "1"}


def read(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rdr = csv.DictReader(fh)
        rows = []
        for r in rdr:
            rows.append({(k or "").strip().lower(): (v or "").strip() for k, v in r.items()})
    return rows


def vparse(v):
    """Dotted-number version to a tuple, or None. Accepts a leading v."""
    m = re.fullmatch(r"[vV]?(\d+(?:\.\d+)*)", v.strip())
    if not m:
        return None
    parts = [int(x) for x in m.group(1).split(".")]
    while len(parts) < 3:
        parts.append(0)
    return tuple(parts)


def distance(used, cur):
    a, b = vparse(used), vparse(cur)
    if used.strip() == cur.strip():
        return "current"
    if a is None or b is None:
        return "differs (distance not computable)"
    if a == b:
        return "current"
    if a > b:
        return "ahead of current (check)"
    if a[0] < b[0]:
        return f"behind: major ({b[0] - a[0]})"
    if a[1] < b[1]:
        return f"behind: minor ({b[1] - a[1]})"
    return f"behind: patch ({b[2] - a[2]})"


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for r in rows:
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--current")
    ap.add_argument("--products")
    ap.add_argument("--flag", default="deprecated;use with caution;retired")
    a = ap.parse_args()

    data = read(a.file)
    if not data:
        sys.exit("The inventory has no rows.")
    need = {"component", "version", "accessibility_status"}
    cols = set(data[0].keys())
    missing = need - cols
    if "products" not in cols and "product" not in cols:
        missing.add("products")
    if missing:
        sys.exit("Missing columns: " + ", ".join(sorted(missing)) + ". See the header of this script.")

    current = {}
    for r in data:
        if r.get("current_version"):
            current[r["component"]] = r["current_version"]
    if a.current:
        for r in read(a.current):
            current[r["component"]] = r["current_version"]

    # explode to one use per component x product
    uses = []
    for r in data:
        prods = r.get("products") or r.get("product") or ""
        for p in [x.strip() for x in prods.split(";") if x.strip()]:
            uses.append(dict(r, product=p))
    if not uses:
        sys.exit("No products listed on any row.")

    comps = sorted({u["component"] for u in uses})
    derived = []
    for c in comps:
        if c not in current:
            vs = [u["version"] for u in uses if u["component"] == c]
            parsed = [(vparse(v), v) for v in vs if vparse(v)]
            if parsed:
                current[c] = max(parsed)[1]
                derived.append(c)
            else:
                current[c] = ""
    for u in uses:
        cur = current.get(u["component"], "")
        u["drift"] = distance(u["version"], cur) if cur else "no current version known"
        u["behind"] = u["drift"].startswith("behind") or u["drift"].startswith("differs")

    seen_products = sorted({u["product"] for u in uses})
    all_products = [x.strip() for x in a.products.split(";")] if a.products else seen_products
    base_label = "your product list" if a.products else "products named in the inventory"

    print(f"# Component adoption and drift\n")
    print(f"Inventory rows: {len(data)}; components: {len(comps)}; component uses (component x product): {len(uses)}; "
          f"products: {len(all_products)} ({base_label}).")
    if derived:
        print("Current version not given for: " + ", ".join(derived)
              + ". The highest version in the inventory is used for these; it is not your declared current version.")
    unused = [p for p in all_products if p not in seen_products]
    if a.products:
        print("Products in your list using no listed component: " + (", ".join(unused) if unused else "none") + ".")
    print()

    print("## Adoption by component\n")
    rows = []
    for c in comps:
        cu = [u for u in uses if u["component"] == c]
        prods = {u["product"] for u in cu}
        oncur = {u["product"] for u in cu if u["drift"] == "current"}
        versions = sorted({u["version"] for u in cu}, key=lambda v: (vparse(v) or (0,), v))
        rows.append([c, current.get(c) or "not known", f"{len(prods)} of {len(all_products)}",
                     f"{len(oncur)} of {len(prods)}", len(versions), ", ".join(versions)])
    print(table(["Component", "Current version", "Products using it", "On current version", "Versions in use", "Which versions"], rows))
    print()

    print("## Drift: uses not on the current version\n")
    beh = [u for u in uses if u["behind"] or u["drift"].startswith("ahead")]
    if beh:
        rows = [[u["component"], u["product"], u["version"], current.get(u["component"]) or "not known", u["drift"],
                 u.get("owner") or "owner not named",
                 "yes" if u.get("clinical", "").lower() in YES else ("no" if u.get("clinical") else "not stated"),
                 "yes" if u.get("device_ui", "").lower() in YES else ("no" if u.get("device_ui") else "not stated")]
                for u in sorted(beh, key=lambda u: (u["component"], u["product"]))]
        print(table(["Component", "Product", "In use", "Current", "Drift", "Owner", "Clinical surface", "Device UI"], rows))
    else:
        print("Every use is on the current version.")
    print()

    print("## Behind current, by owner\n")
    by = defaultdict(lambda: [0, 0, 0, 0])
    for u in uses:
        o = u.get("owner") or "owner not named"
        by[o][0] += 1
        if u["behind"]:
            by[o][1] += 1
            if u.get("clinical", "").lower() in YES:
                by[o][2] += 1
            if u.get("device_ui", "").lower() in YES:
                by[o][3] += 1
    print(table(["Owner", "Uses", "Behind current", "of which clinical surface", "of which device UI"],
                [[o, *v] for o, v in sorted(by.items())]))
    print()

    print("## Accessibility status, as you recorded it\n")
    rows = []
    for c in comps:
        for v in sorted({u["version"] for u in uses if u["component"] == c}):
            cu = [u for u in uses if u["component"] == c and u["version"] == v]
            st = cu[0].get("accessibility_status") or "not recorded"
            clin = sum(1 for u in cu if u.get("clinical", "").lower() in YES)
            dev = sum(1 for u in cu if u.get("device_ui", "").lower() in YES)
            rows.append([c, v, st, len(cu), clin, dev])
    print(table(["Component", "Version", "Status (your words)", "Products", "Clinical surfaces", "Device UI"], rows))
    counts = Counter((u.get("accessibility_status") or "not recorded") for u in uses)
    print("\nUses by status: " + "; ".join(f"{k}: {n}" for k, n in counts.most_common()) + ".")
    print()

    if any(u.get("modification") for u in uses):
        print("## Local modification (drift from the system)\n")
        rows = []
        for c in comps:
            cu = [u for u in uses if u["component"] == c]
            m = Counter((u.get("modification") or "not recorded").lower() for u in cu)
            rows.append([c, m.get("none", 0), m.get("override", 0), m.get("fork", 0), m.get("not recorded", 0)])
        print(table(["Component", "None", "Override", "Fork", "Not recorded"], rows))
        forks = [u for u in uses if (u.get("modification") or "").lower() == "fork"]
        if forks:
            print("\nForked uses receive no updates from the system component (research row DSX-33): "
                  + ", ".join(f"{u['component']} in {u['product']}" for u in forks) + ".")
        print()

    if any(u.get("lifecycle") for u in uses):
        flags = {x.strip().lower() for x in a.flag.split(";") if x.strip()}
        print("## Lifecycle\n")
        lc = Counter((u.get("lifecycle") or "not recorded") for u in uses)
        print("Uses by lifecycle value: " + "; ".join(f"{k}: {n}" for k, n in lc.most_common()) + ".")
        fl = [u for u in uses if (u.get("lifecycle") or "").lower() in flags]
        if fl:
            print("\nIn use with a flagged lifecycle value (" + "; ".join(sorted(flags)) + "):\n")
            print(table(["Component", "Product", "Version", "Lifecycle", "Owner", "Clinical surface"],
                        [[u["component"], u["product"], u["version"], u["lifecycle"], u.get("owner") or "owner not named",
                          u.get("clinical") or "not stated"] for u in fl]))
        print()

    print("No threshold, target or verdict is applied. Counts are on your inventory as supplied.")


if __name__ == "__main__":
    main()
