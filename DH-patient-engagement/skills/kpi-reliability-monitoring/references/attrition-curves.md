> Shared origin: built in the DH-02.03.3.1 skill build (engagement-kpi-dashboards/references/attrition-curves.md), 19 October 2026, copied unchanged below this line.

# Attrition curves and usage half-life

Interpretive reference for A2 (and, copied, for the reliability skill's recomputation). It says how to compute and read attrition from the person's own events. Every rule that defines "stopped", "used" or the window is the person's.

## Two kinds of attrition

| Kind | What it counts | Typical event | Rows |
|---|---|---|---|
| Nonusage attrition | People who stop using the product, whether or not they still answer follow-up | Last use event (session, module, reading) | PE-101, PE-102, KX4 |
| Dropout attrition | People lost to follow-up: they stop returning assessments or questionnaires | Follow-up wave not completed once due | PE-102, KX4, KX5 |

Report them separately. Dropout threatens validity because it may introduce selection bias (KX5).

## What to report

From Eysenbach (PE-103, KX1 to KX3):

1. Raw attrition proportions at points in time, shown as curves.
2. The relative risk of dropping out or stopping use, where there are groups to compare.
3. A usage half-life: the time after which 50 percent of users have stopped (t50); t10 or t25 may be more practical where attrition is slow.
4. Survival methods (Kaplan-Meier, Cox regression) to analyze and compare curves.

## How `scripts/engagement_kpis.py attrition` computes it

| Step | Rule | Whose rule |
|---|---|---|
| Start | Each person's first start event (for example "enrolled") | The person names the event |
| Use | Use events on or after the start; events before the start are counted and reported, not used | The person names the event |
| Stopped | Last use more than N days before the as-of date; N has no default | The person sets N |
| Still using | Last use within N days of the as-of date: censored at the as-of date | Follows from N |
| Never used | No use event after the start: stopped at day 0 | Follows from the data |
| Raw stopped proportion at day t | Among people enrolled at least t days before the as-of date, the share who stopped before day t | Valid denominator (everyone counted could have reached day t; CS27 by analogy) |
| Kaplan-Meier still using at day t | Product over stop times of (1 minus stopped at that time divided by people still at risk) | KX1 |
| t10, t25, t50 | First day the Kaplan-Meier share still using falls to 90, 75 and 50 percent | KX2 |
| Relative risk by group | Raw stopped proportion at the horizon in each group divided by the reference group's | KX3; descriptive only |
| Dropout per follow-up wave | Completed divided by people whose wave was due by the as-of date | Valid denominator; the person names the waves and due days |

`--interval-days` only sets the display points; it is not a threshold.

## Reading the two curves

- The raw proportion at day t uses only people enrolled at least t days ago, so late points rest on the earliest cohort. It can move up and down between points as cohorts drop out of the denominator (worked example: South 94.7 percent at day 56, 93.3 percent at day 70).
- Kaplan-Meier uses everyone, counting people still using as censored. Where many people enrolled recently, the two differ; report both, with the number behind each point, and say why they differ.
- Neither curve explains why people stop. Causes are hypotheses for the person to test.
- A difference between groups is descriptive. The script gives no test of significance; do not call a difference significant or caused by a site, a feature or a population.

## Tracking facts every computed figure carries

From the register's tracking-job method (old CF-12.02.03.3.1.3: "Do not hide a stale dashboard behind the last good numbers without a timestamp"):

- The as-of date of the data, and the date and time of the run.
- Rows excluded and why (blank or invalid dates, events after the as-of date, use events without a start).
- The person's rules used (events, N days, period).
