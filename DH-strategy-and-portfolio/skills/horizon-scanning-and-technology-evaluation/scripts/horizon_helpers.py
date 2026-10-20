#!/usr/bin/env python3
"""Helpers for horizon-scanning-and-technology-evaluation (dh-strategy-and-portfolio).

Every subcommand reads saved library output or the person's own numbers. Nothing here
fetches, scores or decides. Output is Markdown for the answer.

Usage:
  python3 horizon_helpers.py signals FILE [FILE ...] [--since YYYY-MM-DD]
      Turn saved library outputs (regulatory-dh.search_devices, get_pathway_precedents,
      get_deltas or get_register_deltas, diligence-dh.get_deltas, literature.search_literature,
      regulatory-dh.search_safety_events) into a signal log: one dated, sourced record per
      row, with what the record does not show. Empty change logs print their caveat, never
      "no change".
  python3 horizon_helpers.py byyear FILE
      Decisions per year from a saved get_pathway_precedents output, with the change on
      the year before. Counts only; the reading is the person's.
  python3 horizon_helpers.py trl LEVEL
      The EU Horizon Europe wording for a TRL (SP-029 to SP-031), verbatim, with the
      NASA caveat for levels 7 to 9 (SP-035). The level assigned stays "proposed".
  python3 horizon_helpers.py swap FILE
      Recompute an analytics.mcda run (the person's 0 to 4 scores and weights), check it
      against the tool, and list the weights at which adjacent options would swap.
  python3 horizon_helpers.py rice-check FILE
      Check every analytics.rice score equals reach x impact x (confidence / 100) / effort
      and flag confidence passed as a fraction.
  python3 horizon_helpers.py tornado-check FILE
      Flag risk-tornado runs that tornado a ratio, use the default plus or minus 20 percent
      range, or skip list parameters.
  python3 horizon_helpers.py makers --code CODE FILE [FILE ...] [--since YYYY-MM-DD]
      List every maker the saved records show under a product code (search_devices rows,
      the De Novo grant in get_pathway_precedents, the predicate chain from find_predicates),
      with decisions in and before the window, and per year how many decisions are not yet
      tied to a maker. Names only what the records show; the full list is FDA's 510(k)
      database searched by product code (DL-131).
  python3 horizon_helpers.py words ANSWER.md
      Count a short answer against the 450-word cap: the whole answer except the "Calls made"
      block (which sits before the record line), leaving out the Source, Rows and Retrieved
      columns of tables.
"""
import json
import re
import sys

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
DROP_COLUMNS = {"source", "rows", "retrieved", "source url"}


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def full_date(s):
    if not s:
        return "not stored"
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(s))
    if not m:
        return str(s)
    y, mo, d = m.groups()
    return "{} {} {}".format(int(d), MONTHS[int(mo) - 1], y)


def tool_name(d):
    for k in ("tool", "call"):
        v = d.get(k)
        if isinstance(v, str):
            return v
        if isinstance(v, dict) and isinstance(v.get("tool"), str):
            return v["tool"]
    calls = d.get("calls")
    if isinstance(calls, list) and calls and isinstance(calls[0], dict) and isinstance(calls[0].get("tool"), str):
        return calls[0]["tool"]
    return ""


def signals_from(path, d):
    """Return (rows, caveats) for one saved file."""
    rows, caveats = [], []
    name = tool_name(d)
    gaps = d.get("gaps") or (d.get("every_call_returned") or {}).get("gaps") or []
    # Regulatory change logs with no watch: never "no change".
    if "deltas" in name and "diligence" not in name and not d.get("companies"):
        results = d.get("results")
        if results is None:
            results = (d.get("every_call_returned") or {}).get("results", [])
        if not results:
            for g in gaps or ["the change log returned no rows"]:
                caveats.append("{}: {}. This is a log that has not started, not an absence of "
                               "decisions; read dated records with search_devices or "
                               "get_pathway_precedents instead.".format(path, g))
        if d.get("observation"):
            caveats.append("{}: observation saved with the run: {}".format(path, d["observation"]))
        return rows, caveats
    # Diligence change log.
    if d.get("companies") and d.get("log"):
        log = d["log"]
        for c in d["companies"]:
            if c.get("changes") == "no change recorded":
                caveats.append(
                    "{}: {}: no change recorded in the library change log, which began {} "
                    "(last sweep {}). {}".format(
                        path, c.get("company"), full_date(log.get("first_entry_at")),
                        full_date(log.get("last_sweep_at")),
                        "; ".join(log.get("limits", []))))
            elif isinstance(c.get("changes"), list):
                for ch in c["changes"]:
                    rows.append({"type": "company record change", "date": ch.get("event_date") or ch.get("date"),
                                 "record": "{}: {}".format(c.get("company"), ch.get("type") or ch),
                                 "url": ch.get("url") or ch.get("source_url") or "[GAP]",
                                 "retrieved": d.get("retrieved"),
                                 "not_show": "a filing or decision date, not why it happened"})
        return rows, caveats
    if name.endswith("search_devices") or "search_devices" in name:
        for r in d.get("results", []):
            ident = ""
            ids = r.get("identifiers") or {}
            for k in ("FDA_SUBMISSION", "BASIC_UDI_DI"):
                if ids.get(k):
                    ident = "{} {}".format(k.replace("_", " "), ids[k][0])
                    break
            if r.get("jurisdiction") == "EU":
                not_show = ("decision date not stored; source_url is the EUDAMED search screen, "
                            "quote the Basic UDI-DI; no AI, PCCP or intended-use field")
            else:
                not_show = ("no AI, PCCP or intended-use field; product code {} is a device type; "
                            "a clearance is not evidence of clinical effect or uptake").format(r.get("product_code"))
            rows.append({"type": "authorization decision", "date": r.get("decision_date"),
                         "record": "{} ({}), {} {}, {}, status {}".format(
                             r.get("product"), r.get("manufacturer"), r.get("jurisdiction"),
                             r.get("pathway"), ident, r.get("status")),
                         "url": r.get("source_url"), "retrieved": r.get("retrieved_at"),
                         "not_show": not_show, "key": ident or r.get("product")})
        return rows, caveats
    if "pathway_precedents" in name:
        for r in d.get("results", []):
            ttd = r.get("time_to_decision") or {}
            rows.append({"type": "decisions for a device type",
                         "date": r.get("last_decision"),
                         "record": "Product code {} ({}): {} decisions {} to {}; median {} calendar days "
                                   "submission to decision (n {})".format(
                                       r.get("code"), r.get("regulation_number"), r.get("decisions"),
                                       full_date(r.get("first_decision")), full_date(r.get("last_decision")),
                                       ttd.get("median_days"), ttd.get("n")),
                         "url": "library get_pathway_precedents (FDA records)",
                         "retrieved": "19 October 2026 (saved run)",
                         "not_show": "a device-type count, not an AI count, uptake or market size; days are "
                                     "between stored dates, not MDUFA FDA days"})
        return rows, caveats
    if "search_literature" in name or (d.get("search_1") or {}).get("records"):
        searches = [v for k, v in d.items() if k.startswith("search_") and isinstance(v, dict)]
        if not searches and d.get("records"):
            searches = [d]
        for s in searches:
            for r in s.get("records", []):
                url = "https://doi.org/" + r["doi"] if r.get("doi") else (r.get("pmcid") or "[GAP]")
                flag = r.get("_observed")
                rows.append({"type": "publication record", "date": str(r.get("year") or "not stored"),
                             "record": "{} (library design label: {}, a draft)".format(
                                 (r.get("title") or "")[:110], r.get("design")),
                             "url": url, "retrieved": "19 October 2026 (saved run)",
                             "not_show": "a record, not a finding; the library's design label and empty "
                                         "trial_ids need checking against the paper (register N8)"
                                         + ("; observed: " + flag if flag else ""),
                             "key": r.get("doi") or r.get("pmcid")})
        return rows, caveats
    if "safety_events" in name:
        if d.get("observation"):
            caveats.append("{}: {}".format(path, d["observation"]))
        for r in d.get("results_first3", d.get("results", [])):
            rows.append({"type": "safety record", "date": r.get("event_date"),
                         "record": "{} ({}), {}".format((r.get("title") or "")[:90], r.get("manufacturer"),
                                                        r.get("severity")),
                         "url": r.get("source_url"), "retrieved": "19 October 2026 (saved run)",
                         "not_show": "a recall or report as filed, not a cause; check the filter matched the product"})
        return rows, caveats
    caveats.append("{}: tool not recognized ({}); read it by hand.".format(path, name or "no tool field"))
    return rows, caveats


def signals(paths, since=None):
    all_rows, all_cav, seen = [], [], set()
    for p in paths:
        r, c = signals_from(p, load(p))
        for row in r:
            k = row.get("key")
            if k and k in seen:
                continue
            if k:
                seen.add(k)
            all_rows.append(row)
        all_cav.extend(c)
    before = 0
    if since:
        kept = []
        for row in all_rows:
            dt = str(row.get("date") or "")
            if re.match(r"\d{4}-\d{2}-\d{2}", dt) and dt < since:
                before += 1
                continue
            kept.append(row)
        all_rows = kept
    all_rows.sort(key=lambda x: str(x.get("date") or ""), reverse=True)
    print("| Id | Signal type | Event date | Record | What it does not show | Source | Retrieved |")
    print("|---|---|---|---|---|---|---|")
    for i, row in enumerate(all_rows, 1):
        print("| S{} | {} | {} | {} | {} | {} | {} |".format(
            i, row["type"], full_date(row.get("date")), row["record"], row["not_show"],
            row.get("url") or "[GAP]", full_date(row.get("retrieved"))))
    if since:
        print("\n{} record(s) dated before {} left out of the window.".format(before, full_date(since)))
    if all_cav:
        print("\nCaveats (keep them in the answer):")
        for c in all_cav:
            print("- " + c)
    print("\nEvery row is a signal: a sourced, dated record. A trend is your interpretation of several "
          "signals; any reading the model offers is labeled 'proposed reading'.")


def byyear(path):
    d = load(path)
    for r in d.get("results", []):
        by = r.get("by_year") or {}
        print("Product code {} ({}), decisions per year as stored (retrieved in the saved run):\n".format(
            r.get("code"), r.get("regulation_number")))
        print("| Year | Decisions | Change on year before |")
        print("|---|---|---|")
        prev = None
        for y in sorted(by):
            ch = "" if prev is None else "{:+d}".format(by[y] - prev)
            print("| {} | {} | {} |".format(y, by[y], ch))
            prev = by[y]
        last = r.get("last_decision")
        print("\nThe last year is partial: last decision stored {}.".format(full_date(last)))
        print("Counts of decisions for a device type. Not an AI count, not uptake, not a market size. "
              "Whether this is a trend is your reading.")


TRL_EU = {
    1: "TRL 1 \u2014 Basic principles observed",
    2: "TRL 2 \u2014 Technology concept formulated",
    3: "TRL 3 \u2014 Experimental proof of concept",
    4: "TRL 4 \u2014 Technology validated in a lab",
    5: "TRL 5 \u2014 Technology validated in a relevant environment (industrially relevant environment in the case of key enabling technologies)",
    6: "TRL 6 \u2014 Technology demonstrated in a relevant environment (industrially relevant environment in the case of key enabling technologies)",
    7: "TRL 7 \u2014 System prototype demonstration in an operational environment",
    8: "TRL 8 \u2014 System complete and qualified",
    9: "TRL 9 \u2014 Actual system proven in an operational environment (competitive manufacturing in the case of key enabling technologies, or in space)",
}
TRL_ROW = {1: "SP-029", 2: "SP-029", 3: "SP-029", 4: "SP-029", 5: "SP-030", 6: "SP-030",
           7: "SP-031", 8: "SP-031", 9: "SP-031"}


def trl(level):
    n = int(level)
    if n not in TRL_EU:
        sys.exit("TRL runs from 1 to 9 (SP-032).")
    print('Proposed level: EU wording, verbatim quote (SP-028, {}): "{}"'.format(TRL_ROW[n], TRL_EU[n]))
    print("The EU definitions apply where a Horizon Europe call requires a TRL, unless otherwise specified (SP-028).")
    if n >= 7:
        print("NASA's levels 7 to 9 assume a space environment and flight (SP-035); use the EU "
              "'operational environment' wording for a health product, never NASA's flight terms.")
    print("The level is proposed for the person to confirm; it is not a regulatory status or a clinical finding.")


def value(scores, weights):
    return sum(weights[k] * scores.get(k, 0) for k in weights) * 25


def swap(path):
    d = load(path)
    call = d.get("call", {})
    args = call.get("arguments") or call.get("args") or d.get("arguments") or d
    alts, w = args["alternatives"], args["criteria_weights"]
    total = sum(w.values())
    if abs(total - 1) > 1e-6:
        print("Weights sum to {:.3f}, not 1. Ask the person to confirm before ranking.".format(total))
    for a in alts:
        bad = [k for k, v in a["scores"].items() if not (0 <= v <= 4)]
        if bad:
            print("Scores outside 0 to 4 for {}: {}. The calculator uses a 0 to 4 scale.".format(a["id"], bad))
    ranked = sorted(alts, key=lambda a: value(a["scores"], w), reverse=True)
    print("| Rank | Option | Value (recomputed, 0 to 100) |")
    print("|---|---|---|")
    for i, a in enumerate(ranked, 1):
        print("| {} | {} | {:.2f} |".format(i, a["id"], value(a["scores"], w)))
    res = (d.get("response") or {}).get("results") or d.get("results") or []
    tool = {r["id"]: r.get("value_estimate") for r in res}
    if tool:
        bad = [a["id"] for a in alts if abs((tool.get(a["id"]) or -1) - value(a["scores"], w)) > 0.01]
        print("\nCheck against analytics.mcda: " + ("all values match." if not bad else "MISMATCH for {}".format(bad)))
    print("\nWhere adjacent options would swap (one weight moved, the others kept in proportion):\n")
    print("| Pair | Criterion | Current weight | Swap at weight | Direction |")
    print("|---|---|---|---|---|")
    for hi, lo in zip(ranked, ranked[1:]):
        if abs(value(hi["scores"], w) - value(lo["scores"], w)) < 1e-9:
            print("| {} and {} | tie | | | |".format(hi["id"], lo["id"]))
            continue
        for k in w:
            a = hi["scores"].get(k, 0) - lo["scores"].get(k, 0)
            rest = sum(w[c] * (hi["scores"].get(c, 0) - lo["scores"].get(c, 0)) for c in w if c != k)
            if w[k] >= 1:
                continue
            bb = rest / (1 - w[k])
            if abs(bb - a) < 1e-12:
                continue
            t = bb / (bb - a)
            if 1e-6 < t < 1 - 1e-6 and abs(t - w[k]) > 1e-9:
                direction = "if raised above" if t > w[k] else "if lowered below"
                print("| {} over {} | {} | {:.2f} | {:.2f} | {} |".format(hi["id"], lo["id"], k, w[k], t, direction))
    print("\nThe order is your scores and weights, computed. It is not a choice and not a recommendation.")


def rice_check(path):
    d = load(path)
    args = d.get("arguments") or (d.get("call") or {}).get("arguments") or {}
    given = {i["id"]: i for i in args.get("initiatives", [])}
    res = (d.get("response") or {}).get("results", [])
    print("| Item | Confidence given | Expected score | Tool score | Check |")
    print("|---|---|---|---|---|")
    for r in res:
        g = given.get(r["id"], {})
        conf = g.get("confidence", 0)
        exp = g.get("reach", 0) * g.get("impact", 0) * (conf / 100.0) / (g.get("effort") or 1)
        ok = abs(exp - (r.get("score") or 0)) <= max(1e-3, 1e-3 * abs(exp))
        note = "ok" if ok else "MISMATCH"
        if 0 < conf <= 1:
            note += "; confidence looks like a fraction: pass a whole percent (80, not 0.8)"
        print("| {} | {} | {:.4g} | {} | {} |".format(r["id"], conf, exp, r.get("score"), note))


def tornado_check(path):
    d = load(path)
    calls = d.get("calls", [d])
    for c in calls:
        if c.get("call") != "analytics.risk-tornado":
            continue
        args, res = c.get("arguments", {}), c.get("result", {})
        if not isinstance(res, dict):
            continue
        f = args.get("formula", "")
        ranges = args.get("parameter_ranges") or {}
        print("Formula: {}".format(f))
        if re.search(r"/\s*\(", f):
            print("- Flag: the formula divides by a bracketed difference. Do not tornado a ratio; "
                  "rewrite as a difference the person can read (for example net benefit).")
        default = [p for p in args.get("parameters", {}) if p not in ranges]
        if default:
            print("- Flag: default plus or minus {:.0f} percent applied to {}; these ranges are not the person's."
                  .format(100 * res.get("variation_pct", 0.2), ", ".join(default)))
        if res.get("skipped_parameters"):
            print("- Flag: list parameters skipped: {}".format(", ".join(res["skipped_parameters"])))
        for r in res.get("results", []):
            if r.get("low_output", 0) < 0 or r.get("high_output", 0) < 0:
                print("- Flag: {} gives a negative output at one end; check the sign before ranking swings."
                      .format(r["parameter"]))
        print()


def strip_calls(text):
    """Drop the "Calls made" block wherever it sits: its heading or lead-in line, the
    lines of that paragraph, and any bullet or indented lines under it. Counting resumes
    at the first ordinary line after a blank line (the full-version offer or the record)."""
    body, skipping, prev_blank = [], False, False
    for ln in text.splitlines():
        st = ln.strip()
        head = st.lower().lstrip("#*0123456789. ").rstrip("*: ")
        if head.startswith("calls made"):
            skipping, prev_blank = True, False
            continue
        if skipping:
            if not st:
                prev_blank = True
                continue
            is_list = st.startswith(("-", "*", "+")) or ln[:1] in (" ", "\t")
            if prev_blank and not is_list:
                skipping = False
            else:
                prev_blank = False
                continue
        body.append(ln)
    return body


def count_words(text, drop=DROP_COLUMNS):
    body = strip_calls(text)
    out, drop_idx = [], None
    for ln in body:
        st = ln.strip()
        if st.startswith("|"):
            cells = [c.strip() for c in st.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            if drop_idx is None:
                drop_idx = {i for i, c in enumerate(cells) if c.lower().strip("* ") in drop}
            out.append(" ".join(c for i, c in enumerate(cells) if i not in drop_idx))
        else:
            drop_idx = None
            out.append(ln)
    return len([t for t in re.findall(r"\S+", " ".join(out)) if re.search(r"[A-Za-z0-9]", t)])


def words(path):
    n = count_words(open(path, encoding="utf-8").read())
    if n <= 450:
        print("{} words (cap 450): within the short-mode cap.".format(n))
    else:
        print("{} words (cap 450): over by {}. Cut in this order: context paragraphs, repeated row ids in "
              "prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, "
              "the company status line or the record line.".format(n, n - 450))


def makers(code, paths, since=None):
    seen, rows, by_year = set(), [], {}
    for p in paths:
        d = load(p)
        name = tool_name(d)
        if "pathway_precedents" in name:
            for r in d.get("results", []):
                if r.get("code") == code:
                    by_year = r.get("by_year") or {}
                    for g in r.get("de_novo_grants") or []:
                        rows.append((g.get("applicant"), g.get("reference"), g.get("device"), g.get("decision_date"), p))
        elif "find_predicates" in name:
            for c in d.get("chain", []):
                m = re.search(r"\(([^)]+)\)\s*$", c[1] or "")
                if m:
                    rows.append((m.group(1), c[0], c[1][:m.start()].strip(), c[3], p))
        elif "search_devices" in name:
            for r in d.get("results", []):
                if r.get("product_code") == code:
                    ids = (r.get("identifiers") or {}).get("FDA_SUBMISSION") or [r.get("source_url")]
                    rows.append((r.get("manufacturer"), ids[0], r.get("product"), r.get("decision_date"), p))
    makers_, tied = {}, {}
    for mk, ref, dev, dt, p in rows:
        if ref in seen:
            continue
        seen.add(ref)
        key = re.sub(r"[ ,.]+", " ", (mk or "")).strip().lower()
        makers_.setdefault(key, {"name": mk, "items": []})["items"].append((ref, dev, dt, p))
        if dt:
            tied[dt[:4]] = tied.get(dt[:4], 0) + 1
    print("Makers the saved records show under product code {} (only makers in the records read):\n".format(code))
    print("| Maker (as stored) | Decisions under {} (identifier, date) | In window | Source file |".format(code))
    print("|---|---|---|---|")
    for m in sorted(makers_.values(), key=lambda x: max(i[2] or "" for i in x["items"]), reverse=True):
        items = sorted(m["items"], key=lambda i: i[2] or "", reverse=True)
        inw = sum(1 for i in items if since and i[2] and i[2] >= since) if since else "window not given"
        print("| {} | {} | {} | {} |".format(m["name"], "; ".join("{} ({})".format(i[0], full_date(i[2])) for i in items),
                                              inw, ", ".join(sorted({i[3].split('/')[-1] for i in items}))))
    if by_year:
        print("\n| Year | Decisions under {} | Tied to a maker above | Not yet tied |".format(code))
        print("|---|---|---|---|")
        for y in sorted(by_year):
            if since and y < since[:4]:
                continue
            print("| {} | {} | {} | {} |".format(y, by_year[y], tied.get(y, 0), by_year[y] - tied.get(y, 0)))
    print("\nThis is a name search result, not the full list. FDA's 510(k) database can be searched by "
          "product code (DL-131); ask the person for maker names to search. Never guess makers.")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd, rest = argv[1], argv[2:]
    if cmd == "signals":
        since = None
        if "--since" in rest:
            i = rest.index("--since")
            since = rest[i + 1]
            rest = rest[:i] + rest[i + 2:]
        signals(rest, since)
    elif cmd == "byyear":
        byyear(rest[0])
    elif cmd == "trl":
        trl(rest[0])
    elif cmd == "swap":
        swap(rest[0])
    elif cmd == "rice-check":
        rice_check(rest[0])
    elif cmd == "tornado-check":
        tornado_check(rest[0])
    elif cmd == "makers":
        since, code = None, None
        if "--since" in rest:
            i = rest.index("--since"); since = rest[i + 1]; rest = rest[:i] + rest[i + 2:]
        if "--code" in rest:
            i = rest.index("--code"); code = rest[i + 1]; rest = rest[:i] + rest[i + 2:]
        if not code:
            sys.exit("Give --code, for example --code QAS.")
        makers(code, rest, since)
    elif cmd == "words":
        words(rest[0])
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
