# Thesis check, read 20 October 2026

Register: `evals/files/assumption_register_illustrative.csv`. Values now come from saved library files as named. Trigger rules are the person's; 'met' means the person's rule is met on the data, not a recommendation.

| Id | Assumption | Signal | At memo | Now | Source of now | Trigger (your words) | Rule met | Owner | Reread | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | No new recall or safety event on Pear products | deltas.change_count | 0 | 0 | examples/live/diligence_deltas_Akili_Pear.json; since 1 January 2026; log began 12 October 2026; last sweep 19 October 2026 | Any change recorded in the record | not met | Maria Chen | 15 January 2027 | T5 |
| 2 | Evidence maturity stays at or above 60 | maturity.score | 67 | 67 | examples/live/evidence_maturity_K191716_somnio.json; rubric v1 (7 October 2026); retrieved 19 October 2026 | Falls below 60 | not met (not comparable: T4) | Tom Avery | not given | T2, T4 |
| 3 | No new Form D filing | funding.form_d_count | 5 | 5 | examples/live/funding_signals_pear.json | Any new Form D or Form D/A | not met | owner not named | 15 January 2027 | T1 |
| 4 | No new SEC filing of any kind | funding.latest_filing_date | 2023-04-10 | 2023-04-10 | examples/live/funding_signals_pear.json | A filing dated after the memo | not met | Priya Nair | 1 October 2026 | T6 |
| 5 | Revenue grows 30 percent a year | none | not given | not measurable | no public signal | Below 30 percent growth | not measurable from the record | Maria Chen | 15 January 2027 | T3 |

Counts: rule met 0; rule not met 3; not measurable, not comparable or no rule 2.

## Company status

Company status `[GAP]`: not read (Pear Therapeutics, Inc.). The library stores no status field and no 8-K item number; open the filings below for Items 1.03, 2.01, 3.01 and 5.01 (DL-136 to DL-141) and check for a Form 25 or Form 15 (DL-142 to DL-149). Form 25 or Form 15 is not dissolution (DL-144, DL-149). Nothing is inferred from the date filings stopped.

- 8-K of 10 April 2023: accession 0001835567-23-000022; https://www.sec.gov/Archives/edgar/data/1835567/000183556723000022/0001835567-23-000022-index.htm
- 8-K of 7 April 2023: accession 0001835567-23-000020; URL not stored
- Form 25 or Form 15 among the stored types: not in the stored types; whether the library loads them needs a live check.
- Automated EDGAR reads need a declared User-Agent contact (DL-153): ask which contact the person's organization uses; never their name or email unasked, never an invented one.

Flag key: T1 owner not named; T2 reread date not given; T3 not measurable from the public record; T4 rubric at memo not stated or different; T5 change log began after the memo date; T6 reread date earlier than the read date.
