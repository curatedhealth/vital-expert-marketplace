# Worked example: A2 insight actionability indicators

Run on 19 October 2026. The insight log, change log and SUS file are **illustrative**, written for this example (`sample-data/*_illustrative.csv`). The numbers come from `scripts/research_log.py` on those files; no library call was needed.

**Request:** "Here is our research insight log and our release change log. As of today, did we act on the March study, and does anything in the release notes claim research it can't show? Our HF lead flagged the threshold-save stop (S4) as critical." The person set no rules.

**Runs**

1. `python3 scripts/research_log.py trace sample-data/insight_log_illustrative.csv --as-of 2026-10-19 --changes sample-data/changes_illustrative.csv`
2. `python3 scripts/research_log.py sus sample-data/sus_illustrative.csv --by round`

## Answer (short mode)

**As of 19 October 2026, 3 of 6 insights have a decision (2 actions, 1 refusal) and 3 are open; one shipped change cites no insight and one cites an insight that is not in the log.**

| Status | Count |
|---|---|
| Action | 2 of 6 |
| Refusal | 1 of 6 (I-04, no reason recorded) |
| Open | 3 of 6 |

**Open insights, oldest first**

| Insight | Stop | Age (days) | Owner | Participants hit |
|---|---|---|---|---|
| I-03 | S3 diary scale | 129 | owner not named | 2 |
| I-05 | S5 alert filter | 129 | Clinical portal team | 1 |
| I-06 | S6 login timeout | 60 | owner not named | 4 |

**Critical-task stop:** S4 threshold save (I-04) was refused with no reason recorded. Because your HF lead flagged it critical, that refusal goes to them as recorded; whether it is acceptable is theirs to decide (UX-US-32).

**Trace to shipped changes:** CH-301 traces to I-01 (shipped 4 August 2026). CH-307 "New onboarding carousel" cites no insight: not traced to this research. CH-309 cites I-09, which is not in the log. I-02's change (CH-305) has no ship date yet.

**Time to decision:** median 20 days, longest 33 (n 3).

**SUS:** round 1 mean 68.1 (n 9), round 2 mean 80.7 (n 7), a difference of 12.7 points with different respondents in each round; no significance test is in the sources. Context only: 68 (SD 12.5) as cited by Hyzy et al. (UX-M-08).

**Against your rules:** none set, so no verdict. To review, tell me, for example, how long an insight may stay open and whether every refusal needs a reason; B1 then checks them and records owners for I-03 and I-06.

**Record:** Indicator draft from your logs as of 19 October 2026. Uncleared. AI-assisted.

The full version adds the change table and the column mapping.

## What this example shows

- The release note's onboarding carousel is not credited to research: no insight id stands behind it.
- The refusal on a critical-task stop is surfaced for the owner although only one of six insights is affected.
- Ages are facts to a stated date; "overdue" would need the person's rule.
