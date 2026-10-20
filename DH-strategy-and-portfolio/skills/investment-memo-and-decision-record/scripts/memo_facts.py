#!/usr/bin/env python3
"""Memo helpers for investment-memo-and-decision-record.

Three commands. `facts` and `flags` read saved files and print Markdown;
`words` counts a short-mode answer against the 450-word cap.

  facts  Turn saved VITAL Digital Health Library output (build_company_profile,
         or the identity block of generate_report; get_funding_signals;
         get_evidence_maturity or compare_portfolio) into a memo fact table with
         source and retrieval date, Form D caveats and named gaps.

           python3 memo_facts.py facts --profile P.json [--funding F.json]
                   [--maturity M.json] [--company "Pear Therapeutics, Inc."]

  flags  Set the person's own deal facts (a JSON file they supply) beside the
         sourced transaction and data figures (DL rows). It states figures and
         rows only. It never says whether a deal is reportable, covered or clear.

           python3 memo_facts.py flags --deal deal.json

  words  Count the words of an answer the way the short-mode cap counts them:
         the "Calls made" block up to the record line is dropped, and table
         columns headed Source or Rows are left out. Prints the count and,
         if over 450, the house cut order.

           python3 memo_facts.py words ANSWER.md

Every figure printed by `flags` comes from references/transaction-and-data-rules.md
(DL rows read 20 October 2026). Nothing here is investment advice.
"""
import argparse
import json
import re
import sys
from datetime import date

# ---------- sourced figures (references/transaction-and-data-rules.md) ----------
HSR_EFFECTIVE = date(2026, 2, 17)          # DL-044
HSR_SIZE_OF_TRANSACTION = 133_900_000      # DL-045
HSR_NO_SIZE_OF_PERSON = 535_500_000        # DL-046
HSR_SIZE_OF_PERSON = (26_800_000, 267_800_000)  # DL-047
HSR_FEE_LOW = (189_600_000, 35_000)        # DL-048: USD 35,000 under USD 189.6 million
HSR_FEE_HIGH = (5_869_000_000, 2_460_000)  # DL-048: USD 2,460,000 at USD 5.869 billion or more
CFIUS_SCALE = 1_000_000                    # DL-056: more than one million individuals
CFIUS_SUBSTANTIAL_INVESTOR = 25            # DL-064
CFIUS_SUBSTANTIAL_GOVT = 49                # DL-064
DOJ_GENOMIC = 100                          # DL-066
DOJ_OMIC = 1_000                           # DL-066
DOJ_HEALTH = 10_000                        # DL-066
COUNTRIES_OF_CONCERN = ["china", "cuba", "iran", "north korea", "russia", "venezuela"]  # DL-069
EU_NEW_REGIME = date(2028, 1, 17)          # DL-075
SWISS_TURNOVER_CHF = 100_000_000           # DL-084

PATHWAY_WORDS = {
    "FDA_510K": "510(k), cleared",
    "FDA_DE_NOVO": "De Novo, granted",
    "FDA_PMA": "PMA, approved",
}


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def money(v):
    return "USD {:,.0f}".format(v)


def shown(v, missing="not stored"):
    """A field the saved record lacks stays missing: never print None, 0 or a guess."""
    return missing if v is None or v == "" else v


def full_date(s):
    if not s:
        return "not stored"
    try:
        d = date.fromisoformat(str(s)[:10])
    except ValueError:
        return str(s)
    return "{} {} {}".format(d.day, d.strftime("%B"), d.year)


def pathway_words(prod):
    pw = prod.get("pathway")
    if pw in PATHWAY_WORDS:
        words = PATHWAY_WORDS[pw]
    else:
        ref = str(prod.get("fda_submission", ""))
        if ref.startswith("DEN"):
            words = "De Novo, granted"
        elif ref.startswith("K"):
            words = "510(k), cleared"
        elif ref.startswith("P"):
            words = "PMA, approved"
        else:
            words = "pathway not stored `[GAP]`"
    if prod.get("status") == "DENG":
        words += " (FDA code DENG, register C3)"
    return words


# ---------- company status (DL-135 to DL-168) ----------
STATUS_FORMS = {
    "8-K": "open it for Items 1.03 (bankruptcy or receivership, DL-136, DL-137), 2.01 (deal completed, DL-138), "
           "3.01 (listing notice or withdrawal, DL-139, DL-140) and 5.01 (change in control, DL-141); no item number is stored",
    "25": "exchange delisting of a class; not dissolution and does not end 12(g) or 15(d) reporting (DL-142 to DL-144)",
    "25-NSE": "exchange delisting of a class; not dissolution and does not end 12(g) or 15(d) reporting (DL-142 to DL-144)",
    "15-12G": "end of 12(g) registration; the company stopped SEC reporting, not that it ceased to exist (DL-146, DL-147, DL-149)",
    "15-12B": "end of 12(b) registration; stopped SEC reporting, not dissolution (DL-149)",
    "15-15D": "suspension of 15(d) reporting; not dissolution, and it can lapse (DL-148, DL-149)",
}


def print_status(f):
    """Company status is never inferred: list the filings to open and mark the status [GAP] until read."""
    sec = f["sec"]
    rows = sec.get("rows") or []
    bt = sec.get("by_type") or {}
    print("## Company status")
    print()
    print("Company status `[GAP]`: not read. The library stores no status field and no 8-K item number; "
          "status comes only from the filings or the register, opened at the source, never from press, memory "
          "or the date filings stopped.")
    print()
    listed = [r for r in rows if r.get("type") in STATUS_FORMS]
    eightk = [r for r in rows if r.get("type") == "8-K"]
    listed = sorted(listed, key=lambda r: r.get("date") or "", reverse=True)
    if listed:
        print("| Filing to open | Date | Accession | URL | What it can and cannot show |")
        print("|---|---|---|---|---|")
        for r in listed[:4]:
            print("| {} | {} | {} | {} | {} |".format(r.get("type"), full_date(r.get("date")), shown(r.get("reference")),
                                                      shown(r.get("source_url"), "URL not stored"), STATUS_FORMS[r["type"]]))
        print()
    elif not eightk:
        print("- No 8-K row in the saved copy; open the company's EDGAR filing list.")
    stored = [t for t in bt if t in STATUS_FORMS and t != "8-K"]
    if bt:
        print("- Form 25 or Form 15 among the stored filing types: {}. Whether the library loads those forms "
              "needs a live check.".format(", ".join(stored) if stored else "not in the stored types"))
    print("- Also open, where the company has one: Companies House `company_status` and `company_status_detail` "
          "(DL-157 to DL-163); German insolvency notices, which are deleted after six months, so no hit is not proof "
          "(DL-165 to DL-167); PACER for US bankruptcy dockets (DL-154 to DL-156).")
    print("- Automated EDGAR reads need a declared User-Agent contact (DL-153): ask the person which contact their "
          "organization uses; never use their name or email unasked and never invent one.")
    print()


# ---------- words ----------
WORD_CAP = 450
DROP_COLUMNS = {"source", "rows", "source of now", "rows or file"}
CUT_ORDER = ("context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question; "
             "never cut a gap, a stop, the company status line or the record line")


def count_words(text, drop=DROP_COLUMNS):
    body = []
    _skip_calls = False  # the calls list sits before the record block; skip it, then count the record
    for ln in text.splitlines():
        head = ln.strip().lower().lstrip("#* ").rstrip("*: ")
        if _skip_calls:
            if re.search(r"Clears it|^\W*(#+\s*)?(\*\*)?(\d+\.\s*)?(\*\*)?Record\b", ln.strip()):
                _skip_calls = False
            else:
                continue
        if head.startswith("calls made"):
            _skip_calls = True
            continue
        body.append(ln)
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


def cmd_words(a):
    n = count_words(open(a.answer, encoding="utf-8").read())
    if n <= WORD_CAP:
        print("{} words (cap {}): within the short-mode cap.".format(n, WORD_CAP))
    else:
        print("{} words (cap {}): over by {}. Cut in this order: {}.".format(n, WORD_CAP, n - WORD_CAP, CUT_ORDER))


# ---------- facts ----------
def read_profile(path):
    data = load(path)
    out = {"file": path, "retrieved": None, "company": None, "identifiers": {},
           "products": [], "studies": None, "safety": None, "form_d": [],
           "maturity": None, "gaps": []}
    if "response" in data:  # build_company_profile
        r = data["response"]
        out["company"] = data.get("call", {}).get("arguments", {}).get("company")
        out["retrieved"] = r.get("provenance", {}).get("retrieved_at")
        out["identifiers"] = r.get("identifiers", {})
        out["products"] = r.get("products", [])
        out["studies"] = r.get("clinical_evidence")
        sec = r.get("funding_and_filings", {}).get("sec_edgar", {})
        out["form_d"] = [x for x in sec.get("latest", []) if x.get("type") in ("D", "D/A")]
        em = r.get("evidence_maturity")
        if em:
            out["maturity"] = {"score": em.get("score"), "rubric": em.get("rubric_version"),
                               "points": em.get("assessable_points"),
                               "excluded": em.get("excluded_dimensions")}
        for key in ("reimbursement", "funding"):
            if r.get(key) == "[GAP]":
                out["gaps"].append("{}: [GAP] ({})".format(key, r.get(key + "_gap_reason", "no reason stored")))
        if r.get("funding") == "[GAP]" and out["form_d"]:
            out["gaps"].append("funding [GAP] while the same response lists Form D amounts (register C2): Form D amounts are what the filings state; private rounds stay [GAP]")
    elif "identity" in data:  # identity block of generate_report
        idb = data["identity"]
        out["company"] = idb.get("resolved")
        out["retrieved"] = data.get("retrieved")
        out["products"] = idb.get("products", [])
        out["studies"] = {"studies_total": idb.get("studies_total")}
        out["safety"] = idb.get("safety")
        out["maturity"] = {"score": idb.get("evidence_maturity_score")}
        if idb.get("reimbursement"):
            out["gaps"].append("reimbursement: " + idb["reimbursement"])
        out["sec_count"] = idb.get("sec_edgar_filings")
        out["latest_8k"] = idb.get("latest_8K")
    else:
        sys.exit("profile file not recognized: " + path)
    return out


def read_funding(path):
    data = load(path)
    r = data.get("response", data)
    return {"file": path, "company": data.get("call", {}).get("arguments", {}).get("company"),
            "cik": r.get("sec_cik"), "total": r.get("total_public_signals"),
            "sec": r.get("sources", {}).get("sec_edgar", {}),
            "nih": r.get("sources", {}).get("nih_reporter", {}),
            "ted": r.get("sources", {}).get("eu_ted", {}),
            "private": r.get("private_rounds")}


def read_maturity(path, company):
    data = load(path)
    calls = data.get("calls", [data])
    want = (company or "").lower()
    for c in calls:
        if "companies" in c:  # compare_portfolio
            for row in c["companies"]:
                if want and want in str(row.get("company", "")).lower():
                    em = row.get("evidence_maturity", {})
                    return {"file": path, "retrieved": c.get("retrieved_at"), "score": em.get("score"),
                            "points": em.get("assessable_points"), "components": em.get("components"),
                            "flags": row.get("risk_flags", []), "rubric": None, "limits": None}
        else:
            if not want or want in str(c.get("resolution", "")).lower():
                comps = c.get("components", [])
                if isinstance(comps, list):
                    comps = {x["component"]: "{}/{}".format(x.get("points"), x.get("max_points", "?")) for x in comps}
                return {"file": path, "retrieved": c.get("retrieved_at"), "score": c.get("score"),
                        "points": c.get("score_scale"), "components": comps,
                        "rubric": c.get("rubric_version"), "flags": c.get("risk_flags", []),
                        "not_assessable": c.get("not_assessable"), "limits": c.get("interpretation_limits")}
    return None


def cmd_facts(a):
    p = read_profile(a.profile)
    company = a.company or p["company"]
    print("# Memo fact base: {}".format(company))
    print()
    print("Public record only, from saved library output. Retrieved: {} (`{}`). AI-assisted draft; "
          "not investment advice.".format(full_date(p["retrieved"]), p["file"]))
    print()
    print("## Identity")
    print()
    if p["identifiers"]:
        for k, v in p["identifiers"].items():
            print("- {}: {}".format(k, shown(v)))
    else:
        print("- Identifiers not in this file `[GAP]`")
    print()
    print("## Products and authorizations")
    print()
    print("| Product | Reference | Pathway (words) | Product code | Regulation | Decision date | Source |")
    print("|---|---|---|---|---|---|---|")
    for pr in p["products"]:
        print("| {} | {} | {} | {} | {} | {} | {} |".format(
            shown(pr.get("product")), shown(pr.get("fda_submission")), pathway_words(pr), shown(pr.get("product_code")),
            shown(pr.get("regulation_number")), full_date(pr.get("decision_date")),
            pr.get("source_url", "URL not stored `[GAP]`")))
    print()
    print("Wording: a 510(k) is cleared, a De Novo is granted; neither is \"approved\" (DL-128). "
          "Registration or listing is not an authorization (DL-126, DL-127).")
    print()
    print("## Studies")
    print()
    st = p["studies"] or {}
    print("- " + ", ".join("{}: {}".format(k, v) for k, v in st.items()) if st else "- not in this file `[GAP]`")
    print("- Counts are registered studies in the loaded registry, by link tier; not a judgment of evidence.")
    print()
    print("## Safety events")
    print()
    print("- " + (p["safety"] or "not in this file; see compare_portfolio risk flags if saved"))
    print()
    print("## Filings and funding signals")
    print()
    if a.funding:
        f = read_funding(a.funding)
        sec = f["sec"]
        dr = sec.get("date_range") or [None, None]
        print("Source: `get_funding_signals {{company: \"{}\"}}` (`{}`). SEC CIK: {}.".format(
            f["company"], f["file"], ", ".join(f["cik"]) if f["cik"] else "not stored"))
        print()
        print("| Source | Count | Dates |")
        print("|---|---|---|")
        print("| SEC EDGAR | {} | {} to {} |".format(shown(sec.get("count")), full_date(dr[0]), full_date(dr[1])))
        nd = f["nih"].get("date_range") or [None, None]
        print("| NIH RePORTER | {} | {} to {} |".format(shown(f["nih"].get("count")), full_date(nd[0]), full_date(nd[1])))
        print("| EU TED | {} | {} |".format(shown(f["ted"].get("count")), shown(f["ted"].get("status"))))
        print()
        bt = sec.get("by_type") or {}
        print("SEC filings by type: " + (", ".join("{} {}".format(k, v) for k, v in bt.items()) if bt else "not stored") + ".")
        print()
        if sec.get("sum_of_stated_amounts"):
            print("Not quoted: `sum_of_stated_amounts` adds different filing types "
                  "(tool caveat: \"{}\").".format(sec["sum_of_stated_amounts"].get("caveat")))
        print("Private rounds: {} (no funding source loaded).".format(f["private"] or "[GAP]"))
        print("The latest filing date is not a status; nothing is inferred from when filings stop.")
        print()
        print_status(f)
    if p["form_d"]:
        print("| Form D date | Amount the filing states | Note |")
        print("|---|---|---|")
        for d in p["form_d"]:
            amt = money(d["amount"]) if d.get("amount") is not None else "not stated"
            print("| {} | {} | the amount the library stores; whether it is the offering or the sold field is not stated, so open the filing (DL-015); a sold amount may be stale (DL-006) |".format(full_date(d.get("date")), amt))
        print()
    if p.get("sec_count") is not None:
        print("- SEC EDGAR filings in the identity block: {}; latest 8-K {}.".format(p["sec_count"], full_date(p.get("latest_8k"))))
        print()
    print("Form D shows no valuation, price per share or investor names (DL-016, DL-018); "
          "its date tracks first commitment, not closing (DL-002).")
    print()
    print("## Evidence maturity (library convention)")
    print()
    m = read_maturity(a.maturity, company) if a.maturity else None
    if m:
        pts = m.get("points")
        if isinstance(pts, dict):
            pts = "{} of {} assessable points".format(pts.get("earned"), pts.get("maximum"))
        print("- Score {} ({}), rubric {}; retrieved {} (`{}`).".format(
            m["score"], pts, m.get("rubric") or "v1 (7 October 2026) per formula note", full_date(m["retrieved"]), m["file"]))
        if m.get("components"):
            print("- Components: " + ", ".join("{} {}".format(k, v) for k, v in m["components"].items()) + ".")
        if m.get("not_assessable"):
            print("- Not assessable: " + "; ".join("{} ({})".format(x["component"], x["reason"]) for x in m["not_assessable"]) + ".")
        for fl in m.get("flags") or []:
            print("- Flag as stored: " + fl)
        for li in m.get("limits") or []:
            print("- Limit as stated: \"{}\"".format(li))
    elif p["maturity"] and p["maturity"].get("score") is not None:
        print("- Score {} as embedded in the profile; rubric and components in get_evidence_maturity.".format(p["maturity"]["score"]))
    else:
        print("- Not in these files `[GAP]`")
    print("- A stated convention, not an evidence verdict and not a valuation. Framework-based assessment: "
          "company-and-evidence-assessment (this pack).")
    print()
    print("## Gaps")
    print()
    for g in p["gaps"]:
        print("- " + g)
    print("- UK and Swiss company registers not loaded (Companies House, Zefix) `[GAP]`.")
    print("- HHS breach portal not in the library; a portal search is yours, with its date (DL-095, DL-096).")


# ---------- flags ----------
def yesno(v):
    return "not given" if v is None else ("yes" if v else "no")


def cmd_flags(a):
    d = load(a.deal)
    rows = []

    def add(regime, given, rule, rows_ref, sits):
        rows.append((regime, given, rule, rows_ref, sits))

    value = d.get("value_usd")
    closing = d.get("closing_date")
    cdate = date.fromisoformat(closing) if closing else None
    # HSR
    if cdate and cdate < HSR_EFFECTIVE:
        add("HSR", "closing {}".format(full_date(closing)), "2026 figures apply from 17 February 2026; earlier-year figures not sourced",
            "DL-044", "2025 figures `[GAP]`; not compared")
    elif value is None:
        add("HSR", "value not given", "size-of-transaction USD 133.9 million", "DL-045", "not given; ask")
    else:
        sits = "above" if value > HSR_SIZE_OF_TRANSACTION else "at or below"
        add("HSR", money(value), "size-of-transaction USD 133.9 million (2026)", "DL-044, DL-045",
            "{} the figure".format(sits))
        if HSR_SIZE_OF_TRANSACTION < value <= HSR_NO_SIZE_OF_PERSON:
            sizes = d.get("party_sizes_usd")
            add("HSR", "party sizes: " + (", ".join("{} {}".format(k, money(v)) for k, v in sizes.items()) if sizes else "not given"),
                "between USD 133.9 million and USD 535.5 million the size-of-person test also applies (USD 26.8 million and USD 267.8 million)",
                "DL-046, DL-047", "compare on your figures" if sizes else "not given; ask")
        elif value > HSR_NO_SIZE_OF_PERSON:
            add("HSR", money(value), "above USD 535.5 million no size-of-person test", "DL-046", "above the figure")
        if value < HSR_FEE_LOW[0]:
            add("HSR fee", money(value), "USD 35,000 for transactions under USD 189.6 million", "DL-048", "under USD 189.6 million")
        elif value >= HSR_FEE_HIGH[0]:
            add("HSR fee", money(value), "USD 2,460,000 at USD 5.869 billion or more", "DL-048", "at or above USD 5.869 billion")
        else:
            add("HSR fee", money(value), "intermediate fee tiers not in the sources", "DL-048", "`[GAP]`")
        add("HSR form", "", "updated form vacated 12 February 2026, stay denied 19 March 2026; FTC accepts the pre-February 2025 form; appeal pending on the pages read",
            "DL-051 to DL-053", "fact for the filing owner")
    # CFIUS and DOJ
    health_n = d.get("us_individuals_health_data")
    genetic = d.get("genetic_test_results")
    if health_n is None:
        add("CFIUS", "US individuals with health data: not given", "sensitive personal data above one million individuals", "DL-056, DL-057", "not given; ask")
    else:
        sits = "above" if health_n > CFIUS_SCALE else "at or below"
        add("CFIUS", "{:,} US individuals (health data)".format(health_n), "more than one million individuals in 12 months (or targeting agencies, or a stated objective to reach it)",
            "DL-056, DL-057, DL-059", "{} one million; the other limbs are for your owner".format(sits))
    add("CFIUS", "genetic test results held: " + yesno(genetic), "identifiable genetic test results are sensitive at any count", "DL-058",
        "listed category" if genetic else ("not given; ask" if genetic is None else "none stated"))
    for inv in d.get("foreign_investors", []):
        nm = inv.get("name", "investor")
        vp = inv.get("voting_pct")
        gp = inv.get("govt_interest_pct")
        rights = []
        if inv.get("board_seat"):
            rights.append("board seat")
        if inv.get("observer"):
            rights.append("observer")
        add("CFIUS", "{} ({}): rights {}".format(nm, inv.get("country", "country not given"), ", ".join(rights) or "none stated"),
            "non-controlling investment in a TID US business is covered with a board or observer seat, MNPI access or data decisions",
            "DL-061, DL-062", "board or observer right stated" if rights else "no listed right stated")
        add("CFIUS", "{}: voting {}; foreign government interest in investor {}".format(
            nm, "{}%".format(vp) if vp is not None else "not given", "{}%".format(gp) if gp is not None else "not given"),
            "mandatory declaration: substantial interest is 25% voting by the investor and 49% by a foreign government in the investor",
            "DL-063, DL-064",
            "voting {} 25%; government {} 49%".format(
                "not given" if vp is None else ("at or above" if vp >= CFIUS_SUBSTANTIAL_INVESTOR else "below"),
                "not given" if gp is None else ("at or above" if gp >= CFIUS_SUBSTANTIAL_GOVT else "below")))
        ctry = str(inv.get("country") or inv.get("govt_country") or "").lower()
        if not ctry or ctry == "not given":
            add("DOJ bulk data", "{} country: not given".format(nm),
                "countries of concern: China, Cuba, Iran, North Korea, Russia, Venezuela; covered person 50% owned by or based in one",
                "DL-069, DL-071", "not given; ask")
        else:
            hit = ctry in COUNTRIES_OF_CONCERN
            add("DOJ bulk data", "{} country: {}".format(nm, inv.get("country") or inv.get("govt_country")),
                "countries of concern: China, Cuba, Iran, North Korea, Russia, Venezuela; covered person 50% owned by or based in one",
                "DL-069, DL-071", "listed country" if hit else "not a listed country; ownership chain is for your owner")
    for key, label, thr in (("us_individuals_health_data", "personal health data", DOJ_HEALTH),
                            ("us_persons_omic", "human 'omic data", DOJ_OMIC),
                            ("us_persons_genomic", "human genomic data", DOJ_GENOMIC)):
        n = d.get(key)
        if n is None:
            add("DOJ bulk data", "{}: not given".format(label), "bulk threshold more than {:,} US persons".format(thr), "DL-066", "not given; ask")
        else:
            add("DOJ bulk data", "{:,} US persons ({})".format(n, label), "bulk threshold more than {:,} US persons; de-identified data counts".format(thr),
                "DL-066, DL-067", "{} the threshold".format("above" if n > thr else "at or below"))
    add("DOJ bulk data", "access by a country of concern or covered person: " + yesno(d.get("country_of_concern_access")),
        "the rule bites on transactions giving such access", "DL-070, DL-071", "for your owner")
    # EU
    eu = d.get("eu_member_states")
    if eu:
        regime = "2019/452 and national mechanisms (until 17 January 2028)" if not cdate or cdate < EU_NEW_REGIME else "2026/1386 (from 17 January 2028)"
        add("EU screening", "target in " + ", ".join(eu), regime + "; health is a risk factor, not in the 2026/1386 mandatory list; national laws not sourced",
            "DL-072 to DL-078", "national law `[GAP]`; for your owner")
    # Swiss
    if d.get("swiss_target"):
        sc = d.get("acquirer_state_controlled")
        tv = d.get("swiss_turnover_chf_avg")
        add("Swiss IPG", "acquirer state-controlled: {}; average turnover {}".format(yesno(sc), "CHF {:,.0f}".format(tv) if tv is not None else "not given"),
            "IPG not in force (planned 2027); state-controlled foreign acquirers only; health companies at CHF 100 million average turnover",
            "DL-081 to DL-084", "not in force; {}".format("turnover at or above CHF 100 million" if tv is not None and tv >= SWISS_TURNOVER_CHF else ("turnover below CHF 100 million" if tv is not None else "turnover not given")))
    # HIPAA / HBNR
    role = d.get("hipaa_role")
    add("Health data", "target HIPAA role: {}".format(role or "not given"),
        "covered entity or business associate: HIPAA breach rules and BAA terms; outside HIPAA, a health app falls under the FTC rule",
        "DL-086 to DL-094, CP-US-44 to CP-US-49, CP-US-54 to CP-US-56", "ask for breach risk assessments and the portal search (DL-087, DL-095)")

    # Licensing (SP-130 to SP-147, DL-019 to DL-021): only if the person gives license facts
    lic = d.get("license")
    if lic:
        terr = [x.upper() for x in (lic.get("territory") or [])]
        comp = lic.get("parties_competitors_per_owner")
        if "EU" in terr:
            add("Licensing (EU TTBER)", "territory EU", "Regulation 316/2014 expired 30 April 2026; Regulation (EU) 2026/877 in force 1 May 2026, expires 30 April 2038",
                "SP-134, SP-135", "which regulation applies on your dates, and any exemption, is for your owner")
            shares = lic.get("shares_pct_per_owner") or {}
            if comp is None:
                add("Licensing (EU TTBER)", "competitors: not given", "competitors: combined share at most 20%; non-competitors: each party at most 30%, on any relevant market",
                    "SP-136", "not given; ask your owner whether the parties compete")
            elif not shares:
                add("Licensing (EU TTBER)", "competitors per your owner: {}; shares: not given".format(yesno(comp)),
                    "combined at most 20%" if comp else "each party at most 30%", "SP-136", "shares not given; your owner defines the markets")
            else:
                if comp:
                    tot = sum(v for v in shares.values() if v is not None)
                    add("Licensing (EU TTBER)", "combined share {}% as you state it ({})".format(tot, ", ".join("{} {}%".format(k, v) for k, v in shares.items())),
                        "competitors: combined share at most 20% on any relevant market", "SP-136",
                        "your {}% beside the 20% condition; not assessed: competitor status, the relevant markets and the shares are for your legal owner".format(tot))
                else:
                    for k, v in shares.items():
                        add("Licensing (EU TTBER)", "{} share {} as you state it".format(k, "not given" if v is None else "{}%".format(v)), "non-competitors: each party at most 30% on any relevant market",
                            "SP-136", "not given; ask" if v is None else "your {}% beside the 30% condition; not assessed: the relevant markets are for your legal owner".format(v))
            inforce = lic.get("in_force_on_2026_04_30")
            add("Licensing (EU TTBER)", "in force on 30 April 2026: {}".format(yesno(inforce)),
                "agreements in force on 30 April 2026 that met the old rules but not the new: prohibition does not apply until 30 April 2027",
                "SP-137", "transition may be relevant; for your owner" if inforce else ("not given; ask" if inforce is None else "signed after; 2026/877 applies"))
            if lic.get("r_and_d_restriction"):
                add("Licensing (EU TTBER)", "research and development restriction stated", "between competitors, hardcore unless indispensable to protect licensed know-how",
                    "SP-139", "for your owner")
            pool = lic.get("technology_pool")
            add("Licensing (EU TTBER)", "technology pool: {}".format(yesno(pool)), "agreements setting up technology pools are outside the regulation", "SP-140",
                "for your owner" if pool else ("not given; ask" if pool is None else "no pool stated"))
            if "data" in [r.lower() for r in (lic.get("rights") or [])]:
                add("Licensing (EU TTBER)", "data licensed", "TTBER can apply to data licensing where the data qualifies as an existing technology right such as production know-how",
                    "SP-142", "whether your data qualifies is for your owner")
        if "US" in terr:
            us = lic.get("us_collective_share_pct_per_owner")
            add("Licensing (DOJ/FTC 2017)", "collective share {}".format("{}% as you state it".format(us) if us is not None else "not given"),
                "safety zone: restraint not facially anticompetitive and licensor and licensees at most 20% of each relevant market significantly affected; outside the zone not presumed unlawful",
                "SP-143, SP-144, SP-146, SP-147", "not given; ask" if us is None else "your {}% beside the 20% condition; not assessed: the markets and whether the restraint is facially anticompetitive are for your legal owner".format(us))
        if "data" in [r.lower() for r in (lic.get("rights") or [])]:
            add("Health data (GDPR)", "training data licensed (as you state it)",
                "data concerning health is a special category; processing is prohibited unless an Article 9(2) ground applies; member states may add conditions",
                "DL-099, DL-101 (inference), DL-105", "whether the data is health data, and the Article 9(2) ground, are for your owner")
        if lic.get("sec_registrant_party"):
            add("Licensing (SEC disclosure)", "SEC registrant party: yes", "material contracts and licenses the business depends on are filed as exhibits (redaction allowed); 8-K Item 1.01 within four business days",
                "SP-130 to SP-133, DL-019 to DL-021", "where the counterparty's terms may appear; disclosure decisions are for your owner")
        if not terr:
            add("Licensing", "territory: not given", "EU TTBER 2026/877 and DOJ/FTC 2017 guidelines are territory-specific", "SP-135, SP-147", "not given; ask")

    print("# Transaction and data flags")
    print()
    print("Your deal facts set beside the sourced figures (`{}`). Figures and rows only. Whether the deal is reportable, "
          "covered, notifiable or compliant is for the owner you name for legal or compliance, or owner not named. "
          "Nothing here says a deal is clear.".format(a.deal))
    print()
    print("| Regime | Your fact | Sourced figure or rule | Rows | How your fact sits |")
    print("|---|---|---|---|---|")
    for r in rows:
        print("| {} | {} | {} | {} | {} |".format(*r))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("facts")
    f.add_argument("--profile", required=True)
    f.add_argument("--funding")
    f.add_argument("--maturity")
    f.add_argument("--company")
    g = sub.add_parser("flags")
    g.add_argument("--deal", required=True)
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    if a.cmd == "facts":
        cmd_facts(a)
    elif a.cmd == "words":
        cmd_words(a)
    else:
        cmd_flags(a)


if __name__ == "__main__":
    main()
