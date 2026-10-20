# Worked run: A2 risk management file, seeded from comparable recalls (with an A1 trace check)

Run on 19 October 2026 on live library data. The product is an illustrative insulin bolus-advice app; its trace export (`trace_bolus_app_illustrative.csv`) was written for this example and is not a real product's file. The recall data are real library rows, saved trimmed in `live/`.

## The request

"We're building a bolus calculator app for people on insulin, US and EU. What hazards are we missing in our risk file? Our current hazards are HZ-01 to HZ-04 in the attached trace."

## Calls made

| # | Call | Result |
|---|---|---|
| 1 | `regulatory-dh.list_jurisdictions` (free) | US 892 safety events (last load 2026-10-19); EU 0; UK 10 MHRA alerts; CH not loaded |
| 2 | `regulatory-dh.search_safety_events {"product": "insulin", "jurisdiction": "US", "limit": 10}` | 10 rows, 8 distinct events (Tandem, Insulet), 2022 to 2025 |
| 3 | `regulatory-dh.search_safety_events {"manufacturer": "Insulet", "since": "2025-01-01", "limit": 10}` | 2 events (11 September 2025, 23 May 2025) |
| 4 | `regulatory-dh.search_safety_events {"manufacturer": "Dexcom", "limit": 10}` | 10 rows, 4 distinct events, 2025 to 2026 |
| 5 | `python3 scripts/trace_check.py examples/trace_bolus_app_illustrative.csv` | 26 items, 17 findings, including 5 G7 (design input with no design output; added after iteration 1) (`trace_check_result.md`) |

## The answer (short mode, as delivered)

**Answer.** Your four hazards cover the two Omnipod 5 entry failures and the stale-value failure, but comparable recalls show at least four more foreseeable software hazards that your file does not name. Two of your hazards also have no complete control evidence yet. Library data retrieved 13 to 19 October 2026; US recalls only (EU vigilance and Swiss field safety actions not loaded).

**Hazards from comparable products** (FDA enforcement reports via the library; counted as events, not rows)

| Event date | Firm, product line | Failure as recorded | Candidate hazard chain | In your file? |
|---|---|---|---|---|
| 3 July 2025 | Tandem, t:slim mobile app | Phone set to a right-to-left language causes pairing issues and graphical defects | Layout defect hides or misplaces a dose field; wrong therapy decision | No |
| 24 July 2025 | Dexcom, G7 and ONE+ apps | App ends the session without the expected "Sensor Failed" alert | Device failure not announced; missed hypo or hyperglycemia | No (HZ-04 covers termination, not a silent failure state) |
| 5 March 2024 | Tandem, t:connect app | Crash and relaunch loop drains pump battery over Bluetooth | App behavior shortens a connected device's operating time | No |
| 5 August 2025 | Tandem, Control-IQ+ with G7 | Unexpected automatic correction bolus with a paired sensor | Interoperability with a paired device changes dosing | No, if you pair with sensors |
| 23 May 2025 | Insulet, Omnipod 5 iOS | Comma not recognized as decimal separator; 0.1 unit read as 1 unit | Tenfold dose entry | Yes, HZ-01 |

Each chain ends in harm from a dose or decision taken on wrong or late app output: indirect harm (VG14).

Also returned. In your file: 11 September 2025 Omnipod 5 magnifier (HZ-02), 14 April 2026 Dexcom stale values (HZ-03), 28 August 2025 Dexcom G6 Android termination (HZ-04). Left out: three Tandem pump-software events (6 October 2025, 27 February 2025, 24 May 2022; not app functions), 27 May 2026 Dexcom sensors (not software), 28 February 2023 Omnipod 5 app outage (relevant only if your app controls a pump).

**Controls to look at.** HZ-04 has no risk control (G4). RC-04, "instructions tell users to check the value", is information for safety only, with no verification (G5) and no design input (G6); record why a design control was not feasible. VER-03 (maximum bolus boundary) failed; VER-04 (stale data) has no result. DI-01 and DI-03 to DI-06 have no design output recorded (G7, a working-convention check).

**Open items.** Severity and probability for the new hazards wait for your policy's scales. Confirm each recall on FDA's recall database before citing it outside the team.

**Record.** Draft for the owner. Severity, probability and acceptability are yours. Uncleared AI-assisted draft.

Want the full hazard table with the control-priority check?

## What the run showed

- The library adds failures the team had not imagined: locale, accessibility, OS lifecycle and paired-device behavior.
- One recall returned as five rows (24 July 2025); counting rows would have overstated the evidence.
- No row carries a recall number or record link; the output cites date, firm and product line and tells the person to confirm on FDA's database.
