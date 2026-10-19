# Worked example: A2 on a CGM companion app complaint

Live library calls on 19 October 2026. The product, GlucoSense app 3.2, is invented for this example; the regulatory rules, the clock computation and the comparable events are real.

**Request:** "A diabetes nurse emailed our sales rep on Friday 9 October that GlucoSense 3.2 showed a glucose value that was 40 minutes old without any stale-data warning. The patient took a correction dose and had a hypo, treated at home with glucose tablets. Quality logged it on 14 October. We sell in the EU, GB and the US. Is this reportable and by when?"

**Calls made**

1. `regulatory-dh.list_jurisdictions` (free): US holds 892 safety events, UK 10 MHRA alerts, EU 0, CH 0.
2. `regulatory-dh.search_safety_events {manufacturer: "Dexcom", jurisdiction: "all", limit: 10}`: 10 FDA recalls, 9 of them app software defects.
3. `regulatory-dh.search_safety_events {product: "insulin dosing app", jurisdiction: "US"}`: nothing (whole-phrase match). Rerun as `{product: "insulin", since: "2025-01-01", limit: 5}`: 5 software recalls (Tandem, Insulet).
4. `scripts/reporting_clock.py --date 2026-10-09 --event eu-serious-incident gb-serious-incident us-mdr-30 --reportability-date 2026-10-14 --as-of 2026-10-19`: saved as `live/clock_glucosense_2026-10-19.md`.

Trimmed outputs: `live/connector_calls_2026-10-19.json`.

## Answer (short mode)

**First date that matters.** The awareness date is 9 October, when the sales rep (an employee) received the email, not 14 October when quality logged it (VG11, VG19). If this is an EU or GB serious incident, the latest date is **24 October 2026** (15 days, day 0 = 9 October; MDR Art. 87(3), UK reg. 44ZH). If it is an FDA MDR-reportable event, the latest date is **8 November 2026** (30 calendar days, 803.50(a)). Counting from 14 October instead would give 29 October for the EU; MDCG 2023-3 asks both dates to be shown and the gap explained (VG13), and which date starts the clock is not in the sourced rules `[GAP]`. The earlier date is the safe reading.

**Criteria on the facts given.**
- EU: a malfunction (stale value, no warning) is an incident (VG1). A treatment decision on wrong device output is indirect harm (VG14). Serious incident turns on whether the hypo was, or might have been, a serious deterioration of health (VG2): **unknown**. If unsure, the MDR says report within the deadline (VG7).
- GB: same 15-day limit (VG28); GB definitions and day counting `[GAP]`.
- US: malfunction met (R11). Serious injury (R10) unknown on the facts; the malfunction route asks whether it would be likely to cause or contribute to a serious injury if it recurred (VG17): **unknown**.

**Unknowns to close.** Severity and treatment of the hypo; whether the defect is version-wide; whether a fix is planned for devices in the field (that would add an 806 or FSCA check).

**Comparables (public records).** Dexcom recalled G7 and ONE+ iOS and watchOS apps (versions 2.9.0 to 2.11.2 and 1.5.0 to 1.6.0) as Class II on 14 April 2026: a thread-blocking defect delayed glucose values, a risk of "treatment decisions based on outdated glucose information". On 24 July 2025 G7 and ONE+ apps were recalled as Class I for a missing "Sensor Failed" alert. These describe the records only; nothing about those firms' reporting or causes is inferred.

**Who decides.** Your reporting owner, not named in the request. Please name them. The decision, the MIR and any MDR report are theirs; a deliberation note for the event file can be drafted (VG21).

**Record:** Draft for the owner. Uncleared.

## What this example shows

- The awareness date is the first receipt by anyone acting for the manufacturer, and it changes the clock by five days.
- Criteria are laid out as met, not met or unknown; the model does not say "not reportable".
- The connector's phrase matching was handled by retrying with one word, and comparables were described from their records only.
- A non-software recall (stolen G7 sensor lots, "Software Version: N/A") came back in the software search and was left out after reading its summary.
