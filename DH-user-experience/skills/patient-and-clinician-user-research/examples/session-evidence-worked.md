# Worked example: A2 session evidence and B1 research action

Run on 19 October 2026. The product, sessions, SUS file, flags and scores are **illustrative**, written for this example (`sample-data/*_illustrative.csv`). The counts and scores come from `scripts/research_log.py` on those files; the ranking is a live `analytics.rice` call (`live/rice.json`); the rules are research rows.

**Request:** "Round 1 of our heart failure app study is done: 5 patients and 3 nurses, think-aloud on a clickable prototype. Our plan was 8 patients and 5 nurses. Our human factors lead flagged dose confirmation (T2) and threshold change (T5) as critical. We call a stop repeated at 2 or more participants. What did the sessions show, and what should we change? Rank the fixes with our RICE scores." The person gave owners: "Mobile product team" for the patient app.

**Calls and runs**

1. `python3 scripts/research_log.py stops sample-data/session_log_illustrative.csv --plan "patient=8,clinician=5" --min-participants 2`
2. `python3 scripts/research_log.py sus sample-data/sus_illustrative.csv --by user_group,round` (round R1 rows used)
3. `analytics.rice` with the person's scores, confidence as a percent (second call in `live/rice.json`; the first call, with 0.8, returned scores 100 times too small).

## Answer (short mode)

**Four stops reached your rule of 2 or more participants; two of them sit on tasks your human factors lead flagged critical and go to them as recorded.** Sessions: patients 5 of 8 planned, nurses 3 of 5.

| Stop | Participants | Task | Their words | Critical (your flag) |
|---|---|---|---|---|
| S1 dose button | 3 patients | T2 confirm dose | "I thought the green button meant I already took it" | Yes |
| S4 threshold save | 2 nurses | T5 change threshold | "It looks saved but the old number is back" | Yes |
| S2 unit toggle | 2 patients | T1 log weight | "Is this kilos or pounds?" | No |
| S3 diary scale | 2 patients | T3 diary | "What does 3 mean here?" | No |

Below your rule: S5 alert filter (1 nurse).

**SUS, round 1:** patients n 6, mean 67.9 (range 30 to 100); nurses n 3, mean 68.3 (one response excluded, item 4 missing; no imputation rule in the sources). Context, not a target: the general benchmark cited by Hyzy et al. is 68 (SD 12.5) (UX-M-08); 114 digital health apps averaged 76.64 (UX-M-09).

**Proposed actions**

| Stop | Action (proposed) | Fix type | Retest | Owner | Release |
|---|---|---|---|---|---|
| S1 | Show a confirmed state after the dose is recorded and relabel the button | Design (UX-US-33) | Yes, critical task | Mobile product team | not set |
| S4 | Show the saved threshold after save; investigate the revert | Design | Yes, critical task | owner not named | not set |
| S2 | Show the unit beside the weight field | Design | Next round | Mobile product team | not set |
| S3 | Label both ends of the diary scale | Information | Next round | Mobile product team | not set |

**Your RICE scores rank** relabel dose button 9.6, simplify diary entry 1.8, caregiver onboarding step 0.6667. The onboarding step is not traced to a stop in this study; it is ranked because you asked, and marked "not from this research". S1 and S4 go to your human factors lead whatever their score (UX-US-32).

**For the owner:** S1 and S4 are stops on critical tasks. Whether they are use errors and how severe is your human factors lead's call. A label-only fix would need new data (UX-US-42). These think-aloud sessions with one employee nurse (C02) are formative and cannot serve as validation evidence (UX-US-40, UX-US-38).

**Open:** who owns S4 (portal); which release carries each change.

**Record:** Research action draft. Decisions, owners and releases are yours. Uncleared. AI-assisted.

The full version adds outcomes per task, the insight log file and the method flags.

## What this example shows

- Counts are distinct participants by group; nurses and patients are never pooled.
- The model did not decide what is critical, repeated or acceptable: the flags, the rule and the scores are the person's.
- The RICE call needed confidence as a percent; the first call's scores were 100 times too small, with the same order, which a reader would not have noticed.
- A backlog item without a stop is labeled, so the monitoring sibling will not count it as research-driven.
