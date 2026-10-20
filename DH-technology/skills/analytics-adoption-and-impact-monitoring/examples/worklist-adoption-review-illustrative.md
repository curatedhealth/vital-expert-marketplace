# Worked example: discharge follow-up worklist, adoption and impact (ILLUSTRATIVE)

Everything about the hospital system, its sites, people, logs and rules is illustrative, typed or generated for this build (`examples/sample-data/`, see its README). The library outputs cited are real saved outputs from 19 October 2026 (`examples/live/`); the connector was not connected during this build (20 October 2026), so no new call was made. Script runs were made on 20 October 2026.

## The request

"Read date 20 October 2026, window September 2026. Attached: roster and usage log for the discharge follow-up worklist at Riverside, Northgate and Lakeview, the monthly issue log, the before-and-after call rates, ten worklist cases, the metric register and our publisher list. Our rules: penetration 1 of at least 60% per site; every issue sent on the due date with a new data timestamp; the call rate up at least 5 points on June. Owners: Priya Nair for adoption and the call rate, Tom Reyes for the monthly issue. Is it working?"

## A1: funnel and champions

`python3 scripts/adoption_check.py funnel --roster examples/sample-data/roster_illustrative.csv --events examples/sample-data/events_illustrative.csv --since 2026-09-01 --as-of 2026-09-30 --by site`

| Group | In scope | Trained (attended) | Practice task done | Task completed (penetration 1) | Penetration 2 | Export only |
|---|---|---|---|---|---|---|
| Lakeview | 15 | 6/15 (40.0%) | 3/15 (20.0%) | 5/15 (33.3%) | 3/6 (50.0%) | 1 |
| Northgate | 15 | 14/15 (93.3%) | 9/15 (60.0%) | 5/15 (33.3%) | 5/14 (35.7%) | 1 |
| Riverside | 15 | 14/15 (93.3%) | 9/15 (60.0%) | 13/15 (86.7%) | 12/14 (85.7%) | 1 |

Flags A2 to A6: 13 people attended without completing the practice task (steps stopped on: "record the call outcome" 6, "filter by unit" 4, "open the worklist from the EHR tab" 3); one event dated 3 October 2026 left out; one event for P999, not on the roster, left out.

`champions`: Riverside P001 8 questions, Northgate P017 6 questions; Lakeview has no champion on the roster.

## A2: cadence, outcome, agreement, governance

`cadence`: the July issue reused the 4 July 2026 data timestamp and went out before the refresh finished (C2, C3); the August issue was missed for "refresh failed" with no one told and no next issue date (C6, C7); the September issue went out on 7 October 2026, two days after its due date, with no data timestamp (C1, C4).

`outcome --bet-metric "Follow-up call within 2 days of discharge"`: September 297/412 (0.7209), June 243/398 (0.6106), difference +0.1103, before-after; users not given for June (O3). Arithmetic on the file, not evidence the worklist caused it.

`agreement`: agreed 5/10, varied 4/10, not recorded 1; reasons recorded for 2 of 4 variations.

`governance --as-of 2026-10-20`: M1 formula changed 15 September 2026 after certification on 3 June 2026 and still certified, dashboards not showing status (G2, G3); M3 draft on the CNO monthly without status (G3); M5 certified with no owner, certifier or date (G1, G4); m.chen moved from data analyst to nurse manager and keeps publish rights (P1); r.osei never reviewed (P2); review interval not given.

## The short answer for B1 (as handed over)

**Answer.** Against your three rules, 3 units met, 4 missed and 1 could not be measured: Riverside met the 60% penetration rule (86.7%), the call rate rose 11.0 points on June against your 5-point rule, and the June issue met the cadence rule; Lakeview and Northgate missed (33.3% each), and the July and September issues missed. Owners are named for all misses; no recheck date is given for any.

**Your rules** (20 October 2026): penetration 1 at least 60% per site; each issue on its due date with a new data timestamp; call rate up at least 5 points on June.

| Unit | Fact behind it | Owner | Recheck |
|---|---|---|---|
| Lakeview penetration | 5/15 (33.3%); 6/15 attended; no champion | Priya Nair | not given |
| Northgate penetration | 5/15 (33.3%); 14/15 attended, 9/15 practice proof | Priya Nair | not given |
| July issue | reused 4 July 2026 timestamp | Tom Reyes | not given |
| September issue | sent 7 October 2026, due 5 October 2026, no timestamp | Tom Reyes | not given |

**Limits.** The August issue was missed with no one told and no next date; your rule does not say how a missed issue counts, so it is not measurable (your call). The call-rate rise is a before-after difference with June users not given: arithmetic on your file, not evidence the worklist caused it (Proctor 2011, CS32, DOI 10.1007/s10488-010-0319-7). Metric M1 changed formula on 15 September 2026 and is still certified, so the September rate is not on the certified definition.

**For you to decide.** Recheck dates for each miss; whether M1 is decertified before the next read; whether Lakeview gets a champion; keep, change the insertion, or stop is yours.

**Calls made.** None: the connector was not connected; scripts run on your files, 20 October 2026. Full version on request.

**Record.** Impact review draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Word count: `python3 scripts/adoption_check.py words` on the text from "Answer" to the record line printed "299 words, within the short-mode cap" (20 October 2026).
