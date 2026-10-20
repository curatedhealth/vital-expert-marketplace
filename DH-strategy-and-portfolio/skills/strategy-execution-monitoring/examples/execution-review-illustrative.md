# Worked example: realization read and execution review (illustrative plan, live partner record)

Runs A2 and B1 of `strategy-execution-monitoring`. The benefits register, milestone log and experiment log in `examples/sample-data/` are ILLUSTRATIVE: typed for this example, not a real company's plan, and the people named are invented. The partner facts come from saved live library outputs of 19 October 2026 (`examples/live/diligence_get_deltas_BigHealth_Akili.json`, `examples/live/partner_profile_akili.json`). Company status comes from the research pass rows read on 20 October 2026 (SP-148 to SP-168 in `references/strategy-and-portfolio-research.md`). The connector was disconnected on 20 October 2026, so no new library call was made.

## Request

"Read date 20 October 2026. Here are our benefits register, milestone log and pilot log for the remote monitoring strategy. Our licensor for the triage algorithm is Akili Interactive Labs, Inc.; I saw a report that they were acquired. Where are we since 1 January 2025, and then review the misses."

## Calls

| Step | Call | Saved file or output | Date |
|---|---|---|---|
| A2 step 1 to 3 | `python3 scripts/execution_check.py benefits / milestones / experiments` | below | 20 October 2026 |
| A2 step 4 | `diligence-dh.get_deltas {companies: ["Big Health, Inc.", "Akili Interactive Labs, Inc."], since: "2025-01-01"}` | `examples/live/diligence_get_deltas_BigHealth_Akili.json` | 19 October 2026 |
| A2 step 4 | `diligence-dh.build_company_profile {company: "Akili Interactive Labs, Inc."}` | `examples/live/partner_profile_akili.json` | 19 October 2026 |

The triage algorithm license is part of the illustrative story; the library record does not show any agreement between Akili and anyone.

## Script output

```
Read date: 20 October 2026. Share of planned change = (actual - baseline) / (target - baseline).
| Id | Benefit | Owner | Baseline | Target | Actual (date) | Share of planned change | Your rule | Rule met | Reread | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| B1 | Clinics using the remote monitoring service | Lena Fischer | 4 | 40 | 22 (30 September 2026) | 0.50 | >=0.5 | met | 1 December 2026 | none |
| B2 | Nurse time per monitored patient per week (minutes) | Lena Fischer | 30 | 18 | 27 (30 September 2026) | 0.25 | >=0.5 | not met | 15 November 2026 | none |
| B3 | Patients enrolled in the remote monitoring service | owner not named | 300 | 5000 | 2100 (30 September 2026) | 0.38 | >=0.5 | not met | not given | E1 |
| B4 | 30-day readmissions among enrolled patients | Omar Haddad | not given | not given | not measured | n/a | not given | not measurable | 1 October 2026 | E2, E3, E4, E5, E6 |

Counts against your rules: met 1, not met 2, not measurable 1.
A share of planned change is arithmetic on your numbers; whether a benefit is on track, and what follows, is yours.

Read date: 20 October 2026. Elements checked are only those in your pass rule.
| Id | Milestone | Owner | Due | Completed | Elements failed | Recheck | Flags |
|---|---|---|---|---|---|---|---|
| M1 | Data protection impact assessment signed | Priya Nair | 31 March 2026 | 20 March 2026 | none | not given | none |
| M2 | EHR integration live in region North | Tom Avery | 30 June 2026 | 14 August 2026 | on_time | 1 November 2026 | M3 |
| M3 | Region South contract signed | owner not named | 31 July 2026 | not completed | owner, evidence, on_time | not given | M1, M2, M4, M6 |
| M4 | Nurse workflow redesign rolled out | Lena Fischer | 30 September 2026 | 28 September 2026 | evidence | 15 November 2026 | M2 |
| M5 | Outcome evaluation protocol approved | Omar Haddad | 31 October 2026 | not completed | not yet due | not given | none |

Failed elements: 5. Each goes to the owner you name, with a recheck date you set or 'stopped' if you stop the unit; the model assigns neither.
Objective served and milestones that depend on each milestone with a failed element (from your objective and depends_on columns; facts, not verdicts):
- M2 serves O1; depended on by: M4.
- M3 serves O1; depended on by: none in the log.
- M4 serves O2; depended on by: none in the log.

| Id | Option | Endpoint | Rule | Sample (planned, actual) | Result | Status | Flags |
|---|---|---|---|---|---|---|---|
| X1 | Remote monitoring in region North | median review minutes per patient | continue if met in 8 of 10 weeks | 10, 10 | median 22 minutes; met in 3 of 10 weeks | complete | none |
| X2 | Patient self-enrollment by text message | enrollment rate at 30 days | not given | 400, 160 | enrollment 31% vs 24% | complete | X2, X4 |
| X3 | AI triage of alerts | false alerts per 100 patients | stop if fewer than 15% fewer | 500, 480 | not reported | running | X3, X4, X5 |
| X4 | Pharmacy refill reminders | not given | not given | 200, not given | not reported | not given | X6, X1, X2, X5 |

Cannot be read against a rule written before the start (X1, X2, X3, X5 or X6): X2, X3, X4.
Whether a test taught something usable, and whether the option continues, is the person's call.
```

## A2 short answer (417 words by `execution_check.py words`)

**Answer.** As of 20 October 2026, against your rules: benefits met 1, not met 2, not measurable 1; milestones with failed elements 3 (M2 and M3 serve O1, scaling to two regions, and M4 depends on M2); tests that cannot be read against a rule written before the start 3 (X2, X3, X4). Your licensor's parent, Akili, Inc., became a wholly owned subsidiary of Virtual Therapeutics Corporation on 2 July 2024, and its record lists ADHD treatment products, not a triage algorithm: please confirm the counterparty's legal name on the contract.

**Benefits**

| Id | Baseline | Target | Actual (date) | Share of planned change | Your rule | Met | Flags |
|---|---|---|---|---|---|---|---|
| B1 | 4 | 40 | 22 (30 September 2026) | 0.50 | >=0.5 | met | none |
| B2 | 30 | 18 | 27 (30 September 2026) | 0.25 | >=0.5 | not met | none |
| B3 | 300 | 5000 | 2100 (30 September 2026) | 0.38 | >=0.5 | not met | E1 |
| B4 | not given | not given | not measured | n/a | not given | not measurable | E2 to E6 |

**Milestones:** M2 completed 14 August 2026 against a due date of 30 June 2026 (on time failed); M3 not completed, due 31 July 2026, no owner and no evidence; M4 completed with no evidence of completion; M5 not yet due.

**Option tests:** X1 readable against its rule (met in 3 of 10 weeks; rule "continue if met in 8 of 10 weeks"). Cannot be read against a rule written before the start: X2 (no success criterion or decision rule), X3 (rule written 20 July 2026, after the 1 July start; result not reported), X4 (no question, endpoint or rule).

**Licensor record.** The library change log began 12 October 2026, so it cannot show your period from 1 January 2025. Dated records instead: EndeavorRx 510(k) cleared 13 December 2023 (K231337) and EndeavorOTC 510(k) cleared 14 June 2024 (K233496) (library, retrieved 19 October 2026). **Company status:** Akili 8-K, 2 July 2024, Items 2.01 and 5.01: offer completed, change in control to Virtual Therapeutics Corporation (SP-151 [WF]); Akili Form 15-12G, 12 July 2024: SEC reporting stopped, not dissolution (SP-154 [WF]; DL-149, inference). EndeavorRx is listed now by Akili Interactive Labs c/o Virtual Therapeutics (FDA registration and listing, read 20 October 2026, SP-168). The acquisition report you mention matches the parent's filings. What the change of control means for your license is for the owner you name for legal matters, or owner not named.

**Calls made:** connector unavailable on 20 October 2026; saved `diligence-dh.get_deltas` (since 2025-01-01) and `build_company_profile` for Akili Interactive Labs, Inc. of 19 October 2026; status from research rows SP-151, SP-154, SP-168; `scripts/execution_check.py` on the illustrative files. Full version on request.

Realization read draft. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## B1 short answer (337 words by `execution_check.py words`)

**Answer.** Against your rules as of 20 October 2026: 1 benefit met, 2 failed, 1 not measurable; 5 failed milestone elements across M2, M3 and M4; 3 option tests cannot be read against a prior rule. B3 and M3 have no owner and no recheck date, and that limits the review most. No verdict on the strategy.

**Your rules.** Benefits: at least 0.5 of the planned change. Milestones M1 to M4: owner, evidence and on time; M5: owner and evidence. Tests: the decision rule in the log. B4 has no rule: not marked met or failed.

**Failed elements**

| Unit | Element | Fact behind it | Owner | Recheck |
|---|---|---|---|---|
| B2 | share of planned change | 0.25 against 0.5 | Lena Fischer | reread 15 November 2026 |
| B3 | share of planned change | 0.38 against 0.5 | owner not named | not given |
| M2 | on time | completed 14 August 2026, due 30 June 2026; M4 depends on it | Tom Avery | 1 November 2026 |
| M3 | owner, evidence, on time | not completed, due 31 July 2026; serves O1 (two regions) | owner not named | not given |
| M4 | evidence | completed 28 September 2026, no evidence recorded | Lena Fischer | 15 November 2026 |

**Limits.** B4 not measurable (baseline, target, actual and rule not given; its reread date of 1 October 2026 is earlier than the read date). X2, X3 and X4 cannot be read against a rule written before the start. The licensor's change of control (Akili 8-K, 2 July 2024, SP-151 [WF]) does not fail a milestone by itself.

**For you to decide.** Who owns B3 and M3, and when each is rechecked or whether M3 is stopped. Whether X2 and X3 are rerun with a rule written first; X2's logged result was "enrollment 31% vs 24%", with no rule written before its 1 May 2026 start. Whether B4 gets a baseline and target. Whether the region South option continues, changes or stops: yours.

**Calls made:** none beyond the A2 read; `scripts/execution_check.py` on the illustrative files. Full version on request.

Execution review draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## What the example shows

- Counts come from the script against the person's own rules; there is no overall verdict.
- "No change recorded" is not reported for a period that starts before the change log began (12 October 2026); the dated records are offered instead.
- The press report about the licensor is checked against the licensor's own filings, quoted by name and date with what each form does not mean; the current FDA listing holder is stated separately.
- A mismatch between the licensor's products on record and what the person says it supplies is stated as a fact, with a question about the contract's counterparty.
- The objective each failed milestone serves and its dependents come from the person's own log, through the script.
- The record line is the very last line; the calls list and the offer of the full version come before it.
- Owners and recheck dates are only those the person set; missing ones are asked for, never filled.
