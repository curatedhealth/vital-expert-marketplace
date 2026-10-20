#!/usr/bin/env python3
"""Obligations table: turn the person's markets into dated registration,
renewal and acceptance obligations, each tied to the research row it comes from.

Every rule below restates a row in references/multi-region-sources.md (MR-,
JX-) or references/pathways-submissions-sources.md (US-, EU-, UK-, CH-).
Nothing is inferred: where no row sources a duty, the line says [GAP].
Dates are facts to check, not verdicts. A "past" date is a prompt to confirm
what was filed, never a finding that it was missed.

Input: a JSON file
{
  "as_of": "2026-10-19",                       # optional, default today
  "markets": [
    {"market": "US", "operation_start": "2026-09-01"},          # optional field
    {"market": "CA", "license_class": "II",
     "qms_certificate_issued": "2026-03-02", "qms_certificate_expires": "2029-03-01"},
    {"market": "EU", "first_placed_on_market": "2025-05-01", "still_placing": true,
     "legacy_mdd_tier": "2028"},                                # "2027", "2028", "upclassified" or omit
    {"market": "GB", "basis": "CE-MDR"},                        # CE-MDR, CE-MDD, CE-MDD-upclassified, UKCA
    {"market": "CH"},
    {"market": "BR", "anvisa_gmp_certificate_issued": "2024-02-01"},
    {"market": "AU"}, {"market": "JP"}
  ]
}
Or a plain list: --markets US,EU,GB,CA,CH

Usage: python3 obligations_table.py markets.json [--as-of YYYY-MM-DD] [--json]
       python3 obligations_table.py --markets US,EU,GB,CA,CH [--as-of YYYY-MM-DD]
"""
import argparse
import datetime as dt
import json
import sys

EUDAMED_MANDATORY = dt.date(2026, 5, 28)      # JX-36
EUDAMED_EXISTING_DEADLINE = dt.date(2026, 11, 28)  # JX-39, JX-41
GB_MDR_END = dt.date(2030, 6, 30)             # UK-03, MR-23
GB_MDD_END = dt.date(2028, 6, 30)             # UK-02, UK-04
CH_REG_DEADLINE = dt.date(2026, 12, 31)       # JX-43 (MedDO Art. 108(2))
EU_LEGACY = {"2027": dt.date(2027, 12, 31), "2028": dt.date(2028, 12, 31),
             "upclassified": dt.date(2028, 12, 31)}  # EU-21, EU-22, EU-23


def d(s):
    return dt.date.fromisoformat(s) if s else None


def fmt(x):
    return f"{x.day} {x.strftime('%B')} {x.year}" if isinstance(x, dt.date) else str(x)


def add_years(x, n):
    try:
        return x.replace(year=x.year + n)
    except ValueError:  # 29 February
        return x.replace(year=x.year + n, day=28)


def status(due, as_of):
    if not isinstance(due, dt.date):
        return "check"
    days = (due - as_of).days
    if days < 0:
        return f"date passed {-days} days ago: confirm what was filed"
    return f"{days} days from the as-of date"


def row(market, obligation, when, state, basis, legal="in force"):
    if basis == "none":
        legal = "not sourced"
    elif state == "condition":
        legal = "in force (condition)"
    return {"market": market, "obligation": obligation, "date_or_window": when,
            "status_as_of": state, "basis": basis, "legal_status": legal}


def us(m, as_of):
    out = []
    year = as_of.year
    start, end = dt.date(year, 10, 1), dt.date(year, 12, 31)
    if as_of < start:
        state = f"window opens in {(start - as_of).days} days"
    elif as_of <= end:
        state = f"window open; closes in {(end - as_of).days} days"
    else:
        start, end = dt.date(year + 1, 10, 1), dt.date(year + 1, 12, 31)
        state = f"next window opens in {(start - as_of).days} days"
    out.append(row("US", "Annual establishment registration and confirmation of every device listing, even with no changes",
                   f"{fmt(start)} to {fmt(end)}", state, "JX-29, JX-30; lapse puts the establishment in 'failed to register' or 'failed to list' status (JX-32)"))
    if start.year == 2026:
        out.append(row("US", "Annual establishment registration fee (FY 2027 rate, applies from 1 October 2026)",
                       "with the annual registration", "amount USD 13,785 per US-55", "US-55"))
    else:
        out.append(row("US", f"Annual establishment registration fee for the window starting {fmt(start)}",
                       "with the annual registration", "[GAP] rate for that fiscal year not in the research",
                       "US-55 covers FY 2027 only", legal="not sourced"))
    out.append(row("US", "Update registration information after any change", "within 30 days of the change",
                   "event-driven", "JX-31"))
    if m.get("operation_start"):
        due = d(m["operation_start"]) + dt.timedelta(days=30)
        out.append(row("US", "Initial registration and device listing for a new establishment", fmt(due),
                       status(due, as_of), "JX-28"))
    return out


def ca(m, as_of):
    out = []
    due = dt.date(as_of.year, 11, 1)
    if as_of >= due:
        due = dt.date(as_of.year + 1, 11, 1)
    out.append(row("CA", "Annual signed statement confirming or updating each medical device license",
                   f"before {fmt(due)}", status(due, as_of),
                   "JX-33; if not filed the Minister may cancel the license (JX-34)"))
    issued = d(m.get("qms_certificate_issued"))
    if issued:
        sub = issued + dt.timedelta(days=30)
        out.append(row("CA", "Send a copy of a new or modified QMS certificate to Health Canada",
                       fmt(sub), status(sub, as_of), "JX-35"))
    exp = d(m.get("qms_certificate_expires"))
    if exp:
        out.append(row("CA", "QMS certificate expiry (as stated on the certificate)", fmt(exp),
                       status(exp, as_of), "MR-04 (validity at most three years); MR-05 (MDSAP certificate for Class II to IV, per the MDSAP site)"))
    elif issued:
        cap = add_years(issued, 3)
        out.append(row("CA", "QMS certificate expiry: the date on the certificate, at most three years after issue",
                       f"no later than {fmt(cap)}", status(cap, as_of) + "; read the certificate", "MR-04"))
    else:
        out.append(row("CA", "QMS certificate expiry", "[GAP] issue or expiry date not given",
                       "check", "MR-04, MR-05"))
    return out


def eu(m, as_of):
    out = []
    first = d(m.get("first_placed_on_market"))
    if first and first < EUDAMED_MANDATORY and m.get("still_placing", True):
        out.append(row("EU", "Register the device in the EUDAMED UDI/device module (device first placed before 28 May 2026, units still being placed)",
                       fmt(EUDAMED_EXISTING_DEADLINE), status(EUDAMED_EXISTING_DEADLINE, as_of),
                       "JX-39 (Commission timeline), JX-41 (Regulation (EU) 2024/1860, 12 months from the notice of 27 November 2025, JX-37)"))
    else:
        out.append(row("EU", "Register the device in the EUDAMED UDI/device module before the first unit is placed on the EU market",
                       "before first placing", "event-driven", "JX-40 (EUDAMED Q&A, not formally endorsed by the Commission)"))
    out.append(row("EU", "Use EUDAMED actor, UDI/device, certificate and market surveillance modules",
                   f"mandatory since {fmt(EUDAMED_MANDATORY)}", "in force", "JX-36"))
    out.append(row("EU", "EUDAMED vigilance/PMS and clinical investigation modules",
                   "[GAP] no date published; mandatory on release with no voluntary period", "check",
                   "JX-38"))
    tier = m.get("legacy_mdd_tier")
    if tier in EU_LEGACY:
        end = EU_LEGACY[tier]
        out.append(row("EU", f"End of MDD legacy transition ({tier} tier) if its conditions were met (QMS, application by 26 May 2024, written agreement by 26 September 2024, no significant change)",
                       fmt(end), status(end, as_of), "EU-21, EU-22, EU-23, EU-24"))
    return out


def gb(m, as_of):
    out = []
    basis = (m.get("basis") or "").upper()
    if basis == "CE-MDR":
        out.append(row("GB", "Placing CE-marked (EU MDR) devices on the GB market accepted until", fmt(GB_MDR_END),
                       status(GB_MDR_END, as_of), "UK-03, MR-23"))
    elif basis == "CE-MDD":
        out.append(row("GB", "Placing CE-marked (MDD) devices on the GB market accepted until the sooner of certificate expiry or",
                       fmt(GB_MDD_END), status(GB_MDD_END, as_of) + "; certificate expiry may come first", "UK-02"))
    elif basis == "CE-MDD-UPCLASSIFIED":
        out.append(row("GB", "Self-declared MDD devices that need a notified body under the EU MDR (up-classified) accepted until",
                       fmt(GB_MDD_END), status(GB_MDD_END, as_of), "UK-04"))
    elif basis == "UKCA":
        out.append(row("GB", "UKCA marking: class I self-declared; other classes need a UK approved body",
                       "no end date sourced", "check", "UK-15, UK-07"))
    else:
        out.append(row("GB", "Basis for the GB market (CE-MDR, CE-MDD, up-classified MDD or UKCA)",
                       "[GAP] basis not given", "check", "UK-02, UK-03, UK-04"))
    out.append(row("GB", "Register the device with the MHRA", "[GAP] no date or renewal cycle in the research",
                   "check", "UK-01"))
    out.append(row("GB", "Indefinite recognition of EU MDR/IVDR CE marking", "consultation 16 February to 10 April 2026; outcome not published",
                   "proposal only; the end dates above remain law", "UK-05, UK-06, MR-24", legal="proposal"))
    return out


def ch(m, as_of):
    return [
        row("CH", "Register products with Swissmedic: devices placed on the market on or after 1 July 2026 (MedDO Art. 108(2))",
            fmt(CH_REG_DEADLINE), status(CH_REG_DEADLINE, as_of), "JX-42, JX-43"),
        row("CH", "Register products with Swissmedic: devices placed from 26 May 2021 (from 26 November 2017 under former MedDO Art. 22a) and before 1 July 2026 (MedDO Art. 108(3))",
            "without delay once a serious incident, FSCA or trend must be reported; no other date in the text [GAP]",
            "condition", "JX-43"),
        row("CH", "Recognition basis: a declaration of conformity under Swiss or EU law", "current law",
            "in force", "MR-19, MR-20"),
        row("CH", "Recognition of FDA-authorized devices", "ordinance changes being drafted; no in-force date",
            "not available today", "MR-21, MR-22", legal="draft policy"),
    ]


def br(m, as_of):
    out = []
    issued = d(m.get("anvisa_gmp_certificate_issued"))
    if issued:
        ren = add_years(issued, 4)
        out.append(row("BR", "ANVISA GMP certificate renewal (class III and IV; MDSAP audits may be used)", fmt(ren),
                       status(ren, as_of), "MR-37"))
    else:
        out.append(row("BR", "ANVISA GMP certificate renewal every four years (class III and IV)",
                       "[GAP] issue date not given", "check", "MR-37"))
    out.append(row("BR", "Registration renewal and software classification", "[GAP] not in the research", "check", "none"))
    return out


def au(m, as_of):
    return [row("AU", "ARTG registration and annual duties", "[GAP] not in the research", "check", "none"),
            row("AU", "MDSAP reports count only if Australian requirements were audited", "with each audit",
                "condition", "MR-36")]


def jp(m, as_of):
    return [row("JP", "Registration and renewal duties", "[GAP] not in the research", "check", "none"),
            row("JP", "MDSAP report may exempt a site from on-site inspection; PMDA may still inspect", "with each inspection",
                "condition", "MR-38")]


RULES = {"US": us, "CA": ca, "EU": eu, "GB": gb, "UK": gb, "CH": ch, "BR": br, "AU": au, "JP": jp}


def build(markets, as_of):
    out = []
    for m in markets:
        code = str(m.get("market", "")).upper()
        fn = RULES.get(code)
        if fn is None:
            out.append(row(code, "Registration and renewal duties", "[GAP] not in the research", "check", "none"))
        else:
            out.extend(fn(m, as_of))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--markets")
    ap.add_argument("--as-of")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    data = {}
    if a.file:
        with open(a.file, encoding="utf-8") as fh:
            data = json.load(fh)
    markets = data.get("markets") or [{"market": x.strip()} for x in (a.markets or "").split(",") if x.strip()]
    if not markets:
        sys.exit("give a markets file or --markets")
    as_of = d(a.as_of or data.get("as_of")) or dt.date.today()
    rows_ = build(markets, as_of)
    if a.json:
        json.dump({"as_of": as_of.isoformat(), "obligations": rows_}, sys.stdout, indent=2, ensure_ascii=False)
        print()
        return
    print(f"Obligations as of {fmt(as_of)}. Dates restate sourced rules; each is a prompt to check, not a finding.")
    print()
    print("| Market | Obligation | Date or window | Status as of | Legal status | Basis (row) |")
    print("|---|---|---|---|---|---|")
    for r in rows_:
        print(f"| {r['market']} | {r['obligation']} | {r['date_or_window']} | {r['status_as_of']} | {r['legal_status']} | {r['basis']} |")


if __name__ == "__main__":
    main()
