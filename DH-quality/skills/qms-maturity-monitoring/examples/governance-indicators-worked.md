# Worked example: A2 governance effectiveness indicators

Run on 19 October 2026. The person's logs are illustrative files written for this example (`sample-data/`). The FDA 483 figures are real (FDA FY 2025 spreadsheet, research rows QS51 to QS54). The safety-event call is a real library call (`live/safety_events_medtronic.json`).

**Request:** "Ahead of our next management review, how is our quality governance doing? Attached: CAPA log, audit findings, our last two management reviews. Our rule: no open CAPA past its due date. We use a clinician programmer app from a partner, Medtronic; anything in the field we should know about?"

**Calls and runs**

1. `scripts/qms_indicators.py capa sample-data/capa.csv --as-of 2026-10-19`
2. `scripts/qms_indicators.py findings sample-data/findings.csv --as-of 2026-10-19`
3. `scripts/qms_indicators.py mr sample-data/management_reviews.csv --required "complaints;capa;audits;risk updates;changes"` (the person's required input list)
4. `regulatory-dh.search_safety_events` `{manufacturer: "Medtronic", since: "2025-01-01", limit: 5}`: five FDA recalls, all Class II, all "Medtronic Neuromodulation".
5. `scripts/qms_indicators.py fda483 references/data/fda_483_fy2025_devices.csv` for the context lines.

## Answer (short mode)

**Your rule is missed: 2 of 4 open CAPA are past the due date you set (CAPA-036 and CAPA-038).** Open CAPA have a median age of 181.5 days; the oldest is 244 days. One of three closed CAPA (CAPA-034) has no recorded effectiveness verification, which the MDR asks for (Article 10(9)(l), EU4).

| Indicator | Number | Your rule | Verdict |
|---|---|---|---|
| Open CAPA past your due date | 2 of 4 | none past due | Missed |
| Closed CAPA without recorded effectiveness verification | 1 of 3 | no rule set | No verdict |
| Audit findings closed | 4 of 7 (57 percent); 2 open past due | no rule set | No verdict |
| Repeat findings within three years (MDSAP definition, QS47) | 2: change control, complaint handling | no rule set | No verdict |
| Management review inputs missing against your list | December 2025: changes. June 2026: risk updates, changes | no rule set | No verdict |
| Management review actions closed | 8 of 11 | no rule set | No verdict |

**Context, FY 2025, pre-QMSR:** CAPA procedures (820.100(a), 279 citations) and complaint procedures (820.198(a), 211) were the most cited device observations on FY 2025 Form 483s (QS53). These cite the retired QS regulation and are not a benchmark for you.

**Field events for your partner's apps (as the records state):** five Class II recalls of Medtronic Neuromodulation clinician programmer or patient apps between 9 January 2025 and 8 April 2026; for example, for the A810 app, "in rare cases, the steps may be displayed out of order" (event date 8 April 2026). Source: openFDA enforcement reports; the library links the API, not the record. Process touched, per the summaries: purchasing and supplier control for your use of the partner's software (P8). No root cause is inferred.

**What it means for you:** management review and audit reports are now inspectable (QS15), so the June 2026 review without risk updates or changes is readable by an investigator. A repeat finding adds a point to an MDSAP nonconformity grade (QS45).

**Next measurements:** the effectiveness record for CAPA-034; the reasons the two open findings passed their due dates (IA-26-02, IA-26-05).

**Record:** Indicator draft on your data. Uncleared. AI-assisted.

The full version adds the per-source finding table, the CAPA age bands if you choose bins, and the 483 grouping by section.

## What this example shows

- One rule from the person produced one verdict; everything else is reported without a verdict.
- The 483 figures are labeled pre-QMSR and used only as context.
- Recalls are described by their records, with the library's provenance limit stated.
