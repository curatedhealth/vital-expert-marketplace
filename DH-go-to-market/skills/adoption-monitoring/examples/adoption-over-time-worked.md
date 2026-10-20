# Worked example: A2 adoption and penetration over time

Run on 19 October 2026. The roster and usage file are illustrative, written for this example (`sample-data/illustrative_roster.csv`, `sample-data/illustrative_usage.csv`): a remote monitoring alert worklist at two sites of one customer, nurses and care coordinators, task event "review and close an alert in the worklist", old step "phone log spreadsheet". The definition check is a real library call (`live/check_claim_runs.json`, `live/qualify_sources.json`).

**Request:** "Is the worklist really being used at North and South? Our rule: 70% of trained staff do the task within 30 days of training. Also check whether people still keep the phone log. Monthly, by site. I'll quote the penetration definition in the customer report, so make sure it's right."

**Calls and runs**

1. `scripts/adoption_over_time.py sample-data/illustrative_roster.csv sample-data/illustrative_usage.csv --as-of 2026-10-19 --by site --window 30 --rule-share 0.7 --maintenance-months 4` (output: `sample-data/run_by_site_window30_rule70.txt`)
2. `verify.qualify_source {doi: "10.1007/s10488-010-0319-7"}`: tier gold (counted)
3. `verify.check_claim` with the Proctor penetration passage (CS39) and `source {source_id, tier, source_type, code}`: "supported" (counted)
4. `verify.check_claim` with numerator and denominator swapped, same passage: also "supported" (counted; run to test the check, register N3)
5. `literature.get_record {doi: "10.1007/s10488-010-0319-7"}` for the citation (counted)

## Answer (short mode)

**South missed your rule; North met it.** Within 30 days of training, 5 of 11 trained South staff did the task (45 percent; your rule 70 percent). At North, 11 of 15 did (73 percent). No one's window is still open.

| Site | Adoption (adopted/trained), October | Penetration (active/eligible), October | Old-step users, October | Eligible not trained |
|---|---|---|---|---|
| North | 14/15 | 14/18 | 11 | 3 |
| South | 6/11 | 4/15 | 7 | 4 |

October runs to 19 October, so its counts cover a partial month.

**Definitions used:** adoption is Proctor's action to try or employ, with trained staff as the denominator (CS34, CS28). Penetration is Proctor's second calculation, providers who deliver divided by providers expected to deliver (CS39), with your eligible list as "expected to deliver".

**Trend:** North's adoption moved most from May to June (6 of 15 to 14 of 15). South's penetration fell from 6 of 15 in September to 4 of 15 in the partial October.

**After training (usage, not training retention):** at North, adopters still doing the task stayed at 14 of 14 in months 1 to 4. At South, 5 of 6 in month 0, 6 of 6 in month 1, 5 of 6 in month 2.

**The old step has not stopped at either site:** 11 North users and 7 South users logged the phone spreadsheet in October. At North that sits beside high adoption, so people may be doing both. That is a hypothesis for B1, not a finding.

**Your report's definition:** the penetration wording matches the Proctor passage (CS39, DOI 10.1007/s10488-010-0319-7). Verify returned "supported", but it also returned "supported" when numerator and denominator were swapped. The direction was confirmed by reading the passage, not by the check.

**Gaps:** 4 eligible South staff (3 care coordinators, 1 nurse) have no training date, so their adoption cannot be measured.

**Record:** Adoption read on illustrative data. Roles and ids only. No clinical meaning. Uncleared. AI-assisted.

The full version adds the month-by-month table per site, the window table and the data checks.

## What this example shows

- The person's rule produced the only verdicts; every rate carries its denominator.
- The partial month is labeled so a falling October figure is not misread.
- Old-step use was reported beside adoption; the possible cause was left as a B1 hypothesis.
- The Verify check was reported with its limit (register N3): "supported" does not prove direction.
