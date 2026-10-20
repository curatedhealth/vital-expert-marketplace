# Worked example: A1 and A2 on one dashboard

Run on 19 October 2026. The person's files are illustrative, written for this example (`sample-data/kpis.json` the cards, `dashboard.json` the definitions the dashboard uses, `dashboard_values.csv` the numbers it shows, `events.csv` and `eligible.csv` the source). The figures are the scripts' real output on those files (`sample-data/run_*.txt`). Rules cite rows from the copied research files and the register method.

**Request:** "Our dashboard says effective engagement is 23.5 percent, refreshed 18 October 2026. Can we trust it, and are the other KPIs on the dashboard still what we agreed?"

**Runs**

1. `python3 scripts/kpi_definition_check.py cards sample-data/kpis.json`
2. `python3 scripts/kpi_definition_check.py drift sample-data/kpis.json sample-data/dashboard.json`
3. `python3 scripts/kpi_definition_check.py missing sample-data/events.csv --as-of 2026-10-19 --start-event enrolled`
4. `python3 scripts/engagement_kpis.py kpis sample-data/events.csv --defs sample-data/kpis.json --eligible sample-data/eligible.csv` (the cards)
5. `python3 scripts/engagement_kpis.py kpis sample-data/events.csv --defs sample-data/dashboard.json --eligible sample-data/eligible.csv` (the dashboard's own definitions)

No library call was needed.

## Answer (short mode)

**The 23.5 percent is computed correctly, but not on the agreed card: the dashboard's denominator drifted.** The card (K2) divides by people enrolled at least 56 days before the as-of date, so everyone counted had the full window to reach 4 modules; the dashboard divides by everyone enrolled.

| Source | Value | Numerator | Denominator |
|---|---|---|---|
| Dashboard, refreshed 18 October 2026 | 23.5 percent | 16 | 68 |
| Recomputed with the card | 23.4 percent | 11 | 47 |
| Recomputed with the dashboard's definition | 23.5 percent | 16 | 68 |

The dashboard's own definition reproduces its number, so the pipeline works; the gap is drift in one field (denominator: `min_days_observed` 56 on the card, absent on the dashboard). The two values nearly match by chance: they count different people. The dashboard includes 21 people who enrolled too recently to reach the dose and 5 of them already did, so its figure will move as they age in.

**Other KPIs on the dashboard:**

| KPI | Finding | Basis |
|---|---|---|
| K1 Program reach | Match; recomputes to 68 of 160 (42.5 percent) | CS27 |
| K3 Active in September | Shown as "Monthly active patients" (MAP), same formula: renamed; confirm with the card owner before treating them as one. Card has no missing-data rule (fail) | Register method; PE-21 |
| K9 Average sessions per active user | On the dashboard with no card; its denominator "active users" is not defined, so it cannot be recomputed | Register method |

**Data notes:** 834 rows; 1 blank date and 1 event after 19 October 2026 excluded; 1 person with sessions and no enrollment event; no month without events (July to October 2026). Nothing imputed.

**Questions for you:** Which K2 denominator is the agreed one (the card owner decides)? What difference between dashboard and recomputation do you accept? Who owns a card for K9, or should it be retired?

**Record:** Recomputed on your data, as of 19 October 2026. No number adjusted. AI-assisted. Uncleared.

Full version available (all card checks, events per month, the drift table field by field).

## Notes on the run

- The card check also raised "Definition source named" on K3 as a check, not a fail; the answer leaves it out for length (secondary rule).
- The B1 repair plan for this result is the one ranked in `live/rice.json`, with illustrative scores typed for the measurement and presented there as the example person's.
- `sample-data/kpis_flawed.json` holds four illustrative cards with typical defects (reach on app downloads, retention with no period, a PAM change score with no measurement evidence or threshold owner, a windowed numerator on a full denominator); `run_cards_flawed.txt` shows the checks they raise.
