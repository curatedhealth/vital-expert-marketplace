# Monitoring signals: what a public event can tell an investment portfolio watcher, and what it cannot

Interpretive reference for tasks A1 (watch rules), A2 (change read) and B1 (holding review). Rows from `diligence-research.md` (prefix DL, read 20 October 2026); library behavior from saved live outputs of 19 October 2026 (`references/tools.md`). Rows marked "(inference)" in the research file are the researcher's reading across items: label it "(inference)" every time it is cited.

No source in this skill sets a benchmark for how often a holding should file, how many events are normal, or what a healthy portfolio looks like. A count from the record is a fact judged by the person's rule.

## 1. Signals by source, with their clocks

| Signal | Clock or cadence (fact) | What it can tell | What it cannot tell | Rows or source |
|---|---|---|---|---|
| Form 8-K | Generally within four business days after the event | An event was reported; read the item: 1.01 material definitive agreement, 2.01 completed significant acquisition, 1.05 material cybersecurity incident | The item, until the filing is opened (library rows carry none); smaller acquisitions may never appear (inference) | DL-019 to DL-024; tools.md |
| Form D (new offering) | Within 15 calendar days after the first sale | A new exempt offering, its date tracking first commitment | Valuation, investors, a closing | DL-002, DL-004, DL-018 |
| Form D amendment | At least annually while the offering continues | The offering is still open | A current amount sold: no amendment is required for a change in amount sold | DL-005, DL-006 |
| 10-K | Annual report | Business, regulation effects, approval status for smaller reporting companies, cybersecurity section | Risk where risk factors are absent (smaller reporting companies need not give them) | DL-025 to DL-030 |
| FDA authorization records | Decision dates as recorded | A new clearance, grant or approval under the applicant's name | Devices cleared under a parent or predecessor name (inference); "approval" for a 510(k) | DL-128, DL-132, DL-133 |
| FDA registration and listing | Public data lags uploads, generally weekly | That an establishment registered or a device is listed | Approval: registration or listing does not denote it | DL-126, DL-127, DL-129, DL-130 |
| HHS OCR breach portal | Breaches of unsecured PHI affecting 500 or more; main list covers 24 months under investigation, the rest in an archive | Entity, state, individuals affected, submission date, breach type, whether a business associate was present | Breaches under 500 (logged and reported yearly, not posted); a vendor's breach may sit under the client's name (inference) | DL-092, DL-095 to DL-098 |
| UK confirmation statement | At least annually, within 14 days after the review period | Directors, PSC, registered office confirmed | Trading or revenue | DL-034 to DL-038 |
| UK accounts | Private companies within 9 months of the accounting reference date, public within 6 | A balance sheet | A profit and loss account, which small and micro companies may currently omit; from 1 April 2028 they must deliver it but may opt out of publishing | DL-039, DL-040, DL-042 |
| Library change log (`get_deltas`) | Log began 12 October 2026; last sweep 19 October 2026 in the saved runs | Event-dated rows in the window up to the last sweep | Anything before the log began, anything not loaded, anything after the last sweep | tools.md |

Not loaded in the library on 19 October 2026: Companies House, Zefix, any funding source, the BfArM DiGA directory feed, NICE. The HHS portal is not among the listed sources. For these the person reads the source directly.

## 2. Reading a change without judging the company

- Report what changed, with the event date, the source and the retrieval date. Never say what it means for value, runway, outcomes or intent (pack rule 3).
- A new 8-K is "an event reported"; a missing 8-K is not "no event" (DL-023 (inference)).
- A breach portal entry is a fact about a reported breach; whether the company complied with HIPAA (DL-086 to DL-094) is for the owner the person names for legal or compliance questions (or owner not named).
- A change in the library's evidence maturity score can come from the rubric (v1, 7 October 2026) or from loaded sources; it is read by `evidence-maturity-monitoring` (this pack).
- Whether a holding still fits the person's thesis is read by `thesis-and-memo-monitoring` (this pack).

## 3. Transaction and data rules that an investment portfolio event can touch

When a holding reports a new investor, a sale or a data deal, these rules may be relevant. The model lists them with rows and dates; whether they apply is for the owner the person names for legal or compliance questions (or owner not named) (pack rule 4).

| Rule | Fact | Rows |
|---|---|---|
| HSR 2026 | Size-of-transaction threshold USD 133.9 million, effective 17 February 2026; thresholds move every year; the 2024 form was vacated on 12 February 2026 and the prior form is in use | DL-044, DL-045, DL-049, DL-051 |
| CFIUS | Health data is sensitive personal data above one million individuals (genetic test results at any count); a non-controlling investment with a board or observer seat in a TID US business can be covered | DL-056 to DL-058, DL-061, DL-062 |
| DOJ bulk data rule | Personal health data over 10,000 US persons, human genomic data over 100; de-identified data still counts; six countries of concern | DL-066, DL-067, DL-069 |
| EU FDI screening | Regulation (EU) 2019/452 governs until 17 January 2028; Regulation (EU) 2026/1386 applies from that date; health and medicines are risk factors, not mandatory scope | DL-072 to DL-078 |
| Swiss IPG | Adopted, not yet in force (SECO plans 2027); applies to foreign state-controlled acquirers | DL-081 to DL-084 |

## 4. Measures the person may set (A1)

The person sets every measure and threshold. The countable facts the log and the script can give:

- holdings read in this cycle, and holdings not read (W2);
- holdings whose requested window starts before the library's log began (W1);
- holdings with no owner named (W3), no reread date (W4), or a reread date reached (W5);
- new filings by type since the person's earlier saved run, and 8-Ks whose item is not yet read;
- field changes between two comparison runs (`scripts/portfolio_watch.py diff`);
- breach portal entries the person found, by date.

A count is not a score. Holdings, founders and teams are never scored here.
