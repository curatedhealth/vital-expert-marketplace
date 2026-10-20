# Worked run: A2 risk control effectiveness, with a B1 ranking test

Run on 19 October 2026. The library data are real and saved trimmed in `live/`. The product, its risk file (`risk_file_bolus_app_illustrative.csv`), its three own complaints and the severity scale (`scale_illustrative.json`) were written for this example and are not a real product's records. The comparable mappings and their severities stand in for the person's confirmations and are marked "proposed mapping" in the events file.

## The request

"Our bolus-advice app has been on the US market for a year. Here are our risk file and our complaints since launch. Were the harms we see foreseen in the risk file, and what does the recall history of similar insulin and CGM apps tell us?"

## Calls and steps

| # | Call or step | Result |
|---|---|---|
| 1 | `regulatory-dh.list_jurisdictions` (free) | US 892 safety events; EU 0; UK 10 MHRA alerts; CH not loaded |
| 2 | `regulatory-dh.search_safety_events {"product": "insulin", "jurisdiction": "US", "limit": 10}` | 10 rows |
| 3 | `regulatory-dh.search_safety_events {"manufacturer": "Insulet", "since": "2025-01-01", "limit": 10}` | 2 rows |
| 4 | `regulatory-dh.search_safety_events {"manufacturer": "Dexcom", "limit": 10}` | 10 rows |
| 5 | `python3 scripts/risk_feedback.py --from-connector live/safety_events_insulin_US.json live/safety_events_insulet_since_2025.json live/safety_events_dexcom.json > comparable_events_prepared.csv` | 22 rows folded into 13 events (one row per app line removed) |
| 6 | Person's complaints appended with `origin = own`; seven comparable events given proposed hazard mappings; person confirms | `events_mapped_illustrative.csv` |
| 7 | `python3 scripts/risk_feedback.py --risk risk_file_bolus_app_illustrative.csv --events events_mapped_illustrative.csv --scale scale_illustrative.json` | `risk_feedback_result.md` |
| 8 | `analytics.mcda` with three findings and test scores (B1 shape check) | `live/mcda_findings_test.json`: 82.5, 67.5, 52.5 |

## The answer (short mode, as delivered)

**Answer.** Two of your three complaints match hazards already in your file (HZ-01 and HZ-03); the third, a hidden dose label with the phone set to Arabic, matches none. Of seven comparable recalls read against your file, four match your hazards and three do not. For HZ-04 (app terminates and stops alerts), a comparable recall reached a worse harm than your file estimates. Library data retrieved 13 October 2026; US recalls only.

**By hazard** (severity on your scale)

| Hazard | Own events | Comparable events | Highest observed vs file | Signal for the owner |
|---|---|---|---|---|
| HZ-01 decimal separator | 1 (CP-001, negligible) | 1 (Omnipod 5, 23 May 2025) | critical vs critical | Own event reached a user before dosing; confirm RC-01 shown the parsed value |
| HZ-02 duplicated digit | 0 | 1 (Omnipod 5, 11 September 2025) | critical vs critical | Within estimate |
| HZ-03 stale value | 1 (CP-002, serious) | 1 (Dexcom G7 apps, 14 April 2026) | serious vs serious | Own harm occurred with RC-03 in place: did the control prevent it? |
| HZ-04 app terminates | 0 | 1 (Dexcom G6 Android, 28 August 2025, Class I) | catastrophic vs serious | No control recorded; comparable harm above your estimate |

**Not foreseen candidates**
- CP-003 (own): layout broken in a right-to-left language; also seen at Tandem (3 July 2025).
- Dexcom, 24 July 2025: device failure with no failure alert.
- Tandem, 5 March 2024: crash loop draining a paired pump's battery.

**Open items.** CP-002 describes a dose on an outdated value followed by hypoglycemia; no reporting decision is recorded. That question goes to your vigilance owner (US: 30 calendar days from awareness, VG17); the awareness date is not confirmed, so no deadline is computed.

**Record.** Draft for the owner. Mapping, severity and whether each control worked are yours. Uncleared AI-assisted draft.

Want the full event table with sources?

## What the run showed

- Folding matters: 22 library rows were 13 events.
- Comparable evidence changed the picture for HZ-04 without any own event: a reason to re-examine the estimate, not proof it is wrong.
- The B1 ranking tool works on the person's scores, but treats every criterion as higher-is-better (`references/tools.md`).
- Call 3 used `since: "2025-01-01"`, which the A2 guide no longer applies unless the person gives a period. Run without it (`live/safety_events_insulet_all.json`, 19 October 2026), the Insulet call adds the 30 November 2023 Omnipod 5 Android Class I recall: the bolus calculator dropped a leading decimal point, with over-delivery "if the user does not recognize the error on the bolus calculator screen or the confirmation screen". That is a further proposed comparable for HZ-01 and bears on whether a confirmation-screen control (RC-01) is enough. The tables above are left as run.
