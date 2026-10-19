# Worked run: A2 account health read and B1 value note (illustrative data)

Illustrative. The account file, targets, meta and notes in `examples/sample-data/` were written for this example; they describe no real customer. Northfield's PHQ-9 rows (20 starters with baseline 10 or more, 15 with a follow-up score, 11 with a drop of 5 points or more) are derived from the illustrative 20-patient cohort used in the outcomes-contract build. Run on 19 October 2026.

## Request

"Here is our account file for Q3 and the targets we set in July (v2). How are our four accounts doing, and what can we send Northfield?"

## Calls and runs

- `python3 scripts/account_health.py attain examples/sample-data/accounts_illustrative.csv --targets examples/sample-data/targets_illustrative_v2.json` (output: `examples/runs/attain.md`)
- `python3 scripts/account_health.py health ... --meta examples/sample-data/meta_illustrative.csv --as-of 2026-10-19` (output: `examples/runs/health.md`)
- Library calls made while building this skill (not with account data): `verify.extract_claims` on a draft note, `verify.qualify_source` and `verify.check_claim` on the PHQ-9 bands, `analytics.rice` on three scored actions (`examples/live/`).

## Answer (short mode, as the skill would hand it over)

**Answer.** Under your rule (activation, active use, PHQ-9 follow-up and sponsor review all met), Northfield meets it for the period ending 30 September 2026. Lakeside misses on active use (0.416 against 0.5). Harbor misses on activation (0.15 against 0.4) and active use (0.375 against 0.5), and has no PHQ-9 data this period. Riverbend misses on sponsor reviews (0 against 1); its activation (0.8) is not comparable, because it is computed on enrolled members and your target needs eligible members (CS27).

**Frame.** Targets v2, set 15 July 2026 by your customer success lead; Lakeside has its own activation target of 0.35. Register rule adopted: an open day-one item blocks a healthy status (Lakeside has one; it misses anyway).

| Account | Met | Missed | Not measured or not comparable | Under your rule |
|---|---|---|---|---|
| Northfield | 4 | 0 | 0 | meets |
| Lakeside | 3 | 1 (active use) | 0 | misses |
| Riverbend | 2 | 1 (sponsor reviews) | 1 (activation basis) | misses |
| Harbor | 1 | 2 (activation, active use) | 1 (PHQ-9 follow-up) | misses |

Uptake, use and customer-reported outcomes are not clinical evidence; with no comparator, the PHQ-9 figures are not evidence of effect (CS32).

**Northfield value note (draft for the owner).** "Between go-live on 2 March 2026 and 30 September 2026, 455 of 1,000 eligible members activated (45.5 percent), and 250 of them were active in the last 90 days. Of the 20 members who started with a PHQ-9 of 10 or more, 15 have a follow-up score, and 11 had a drop of 5 points or more. These figures describe use and scores in your population; they do not show what caused the change." Every number points to a row in the account file. The figure in the earlier sent note VN-01 (62 percent) does not match the file (45.5 percent); that is a finding for the monitoring sibling.

**Open questions.** Riverbend: can the eligible population be supplied? Harbor: where is the PHQ-9 report for Q3? Who owns the Lakeside active-use action: owner not named.

**Record.** Health read and draft note on data you supplied. Nothing sent. Uncleared.
