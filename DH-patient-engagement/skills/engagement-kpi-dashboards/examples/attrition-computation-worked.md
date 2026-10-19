# Worked example: A2 engagement and attrition computation

Run on 19 October 2026. The person's files are illustrative, written for this example (`sample-data/events.csv`, `eligible.csv`, `kpis.json`): 160 eligible patients at two sites, North and South, enrolling from July 2026. The figures below are the script's real output on those files (`sample-data/run_kpis.txt`, `run_attrition.txt`, `run_attrition_all.txt`). Definitions and methods cite rows from the copied research files. No library call was needed for the computation; the Verify calls behind the cited usage half-life definition are in `live/verify_eysenbach.json`.

**Request:** "Here is our app export as of today and the referral list. What is our reach for Q3, how many hit the module dose our program lead set (4 modules in 56 days, target 40 percent), and how fast do people stop using it at each site? We count someone as stopped after 14 days without a session. Follow-ups are due at week 4 and week 12."

**Runs**

1. `python3 scripts/engagement_kpis.py kpis sample-data/events.csv --defs sample-data/kpis.json --eligible sample-data/eligible.csv`
2. `python3 scripts/engagement_kpis.py attrition sample-data/events.csv --start-event enrolled --use-event session --inactive-days 14 --as-of 2026-10-19 --interval-days 14 --horizon-days 84 --group site --followup "followup_w4:28,followup_w12:84" --csv-out sample-data/attrition_curve.csv`
3. The same without `--group` for the program-wide half-life.

## Answer (short mode)

**Reach for the third quarter of 2026 is 42.5 percent: 68 of 160 eligible patients enrolled** (RE-AIM reach on the referral list as the valid denominator, CS22, CS27). **Effective engagement is 23.4 percent (11 of 47), below the 40 percent your program lead set:** missed. The denominator keeps only the 47 people enrolled at least 56 days before 19 October 2026, so no one is counted as failing before they could reach the dose; 5 more recent enrollees already reached it and are not in this figure.

**People stop quickly, faster at South.** Usage half-life (the day by which half have stopped, KX2): 24 days at North, 13 days at South; 17 days program-wide. By day 28, Kaplan-Meier estimates 39.0 percent still using at North and 25.9 percent at South.

| Figure | North | South | Rows |
|---|---|---|---|
| People enrolled (stopped / still using) | 41 (31 / 10) | 27 (22 / 5) | |
| t25 (25 percent stopped) | 11 days | 7 days | KX2 |
| t50, usage half-life | 24 days | 13 days | KX2 |
| Still using at day 28 (Kaplan-Meier) | 39.0 percent | 25.9 percent | KX1 |
| Stopped by day 84, raw (enrolled at least 84 days) | 13 of 14 | 11 of 11 | PE-103 |

**Follow-up dropout:** week 4 completed by 40 of 68 due (dropout 41.2 percent); week 12 by 9 of 25 due (dropout 64.0 percent).

**Data notes:** 1 row with a blank date and 1 event dated after 19 October 2026 excluded; 1 person had sessions but no enrollment event and is excluded. Nothing imputed.

**What it means for you:** if your core content sits after week 2, most South participants would not reach it at the current rate. Week-12 follow-up from 9 of 25 people may carry selection bias (KX5), so any week-12 outcome should be read with that limit. The site difference is descriptive (relative risk of having stopped by day 84, 1.08 for South against North, on 11 and 14 people); it says nothing about why.

**Rules used (yours):** start = enrolled; use = session; stopped = no session for more than 14 days; dose = 4 module completions within 56 days; as of 19 October 2026.

**Record:** Computed on your data, as of 19 October 2026, run 19 October 2026. Engagement figures are not clinical evidence. AI-assisted. Uncleared.

Full version available (curve table every 14 days per site, KPI card table, hypotheses to test).

## Notes on the run

- The raw stopped proportion at late points rests on the earliest cohort: at South it reads 94.7 percent at day 56 and 93.3 percent at day 70, because the day-70 denominator (15) is a different, smaller set of people than the day-56 one (19). Kaplan-Meier uses everyone and does not move this way (`references/attrition-curves.md`).
- The 5 people who reached the dose but sit outside the K2 denominator show why the card carries `min_days_observed`: without it, the dashboard version of this KPI divides by all 68 enrolled (see the reliability skill's worked example).
- Word count of the short answer, without the table's Rows column: under 450.
