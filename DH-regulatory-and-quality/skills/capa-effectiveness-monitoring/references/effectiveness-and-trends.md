# CAPA effectiveness and complaint trends: what the sources say

Interpretive reference for all three tasks. Rows from `quality-systems-sources.md` (QS, EU, VG) and `primary-text-additions.md` (R).

## 1. Effectiveness is required; its test is the person's

| Rule | Row |
|---|---|
| EU: the QMS includes management of corrective and preventive actions "and verification of their effectiveness" (Art. 10(9)(l)) | EU4 |
| EU: the QMS includes processes for monitoring and measurement of output, data analysis and product improvement (Art. 10(9)(m)) | EU3 |
| US: the QMSR incorporates ISO 13485 corrective action (8.5.2) and preventive action (8.5.3); FDA says no change in expectation | QS17 |
| US: CAPA depth matches the magnitude of the problem and the risk, including methods that correct or prevent recurrence | QS18 |
| US: CP 7382.850's Measurement, Analysis, and Improvement area aims at improvement activities that are "effective in identifying and reducing risks" | R8 |
| MDSAP: a nonconformity repeated within three years indicates a corrective action was not adequately taken or implemented | QS47 |
| MDSAP: when new occurrences show previously proposed actions are not effective, a nonconformity may be issued for an ineffective corrective action system | R3 |

QS47 is about repeat audit nonconformities within three years. For complaints recurring after a CAPA closed, cite R3 only.

No sourced row defines how to test effectiveness, how long the window is, or what counts as a pass `[GAP]`. Those are set in the CAPA plan by the person (sibling skill, task B1). Method rules carried from the VITAL register: a CAPA is not effective because it closed on time; a pass is the criterion met in the window, a fail is the criterion missed or no check performed; a failed check opens a new action rather than reopening the old one; a finding is not closed while a new action is open.

## 2. Recurrence and trends

- **Recurrence after closure.** A later complaint or finding with the same code or sub-clause after the CAPA closed. MDSAP's look-back for repeat findings is the two previous QMS audits that evaluated the same sub-clause, within three years (QS47, R3). For complaints, the code and the window are the person's.
- **Same product, different defect is not a recurrence by itself.** Public records show this: the same Dexcom G7 iOS app (SW12300) was recalled on 24 July 2025 for a missing "Sensor Failed" alert (versions 2.8.0 and earlier) and on 14 April 2026 for a thread-blocking defect (versions 2.9.0 to 2.11.2). The records state two different defects; nothing more can be read from them (live call, `examples/live/`).
- **Trend reporting (EU).** Statistically significant increases in the frequency or severity of non-serious incidents or expected side-effects are reported; the method and observation period sit in the PMS plan (VG9). The counts in this skill are inputs to that method, not a significance test.
- **Risk file feedback.** PMS and production information is evaluated for its effect on hazards and benefit-risk (EU15), and risk documentation is updated when new information emerges (QS22).

## 3. Reporting timeliness

The clocks are in `vigilance-clocks.md` section 3: EU and GB 15, 10 and 2 days from awareness, day 0 the awareness date (VG4 to VG6, VG12, VG28); US 30 calendar days and 5 work days (VG17, VG18, R9); US corrections and removals 10 working days from initiation (VG22). US event files keep the deliberation behind each decision (VG21). Register method rule: a reportability decision made after the due date records that the date was missed.

## 4. FDA 483 citations, fiscal year 2025 (context only, pre-QMSR)

FDA's spreadsheet for inspections ending 1 October 2024 to 30 September 2025 lists 791 system-generated 483s in the Devices area (QS52). Measured from its Devices tab (185 cite rows, 2,660 citations in total), the five most cited device areas, and selected other quality-system citations, were (QS53, QS54). "Selected" rows are not ranks 6 onward:

| Rank | Citation (QS regulation section) | Count |
|---|---|---|
| 1 | CAPA procedures, 820.100(a) | 279 |
| 2 | Complaint procedures, 820.198(a) | 211 |
| 3 | Purchasing controls, 820.50 | 115 |
| 4 | Nonconforming product, 820.90(a) | 95 |
| 5 | Process validation, 820.75(a) | 93 |
| Selected (QS54) | MDR procedures, 803.17 | 63 |
| Selected (QS54) | CAPA documentation, 820.100(b) | 63 |
| Selected (QS54) | Quality audit procedures, 820.22 | 57 |
| Selected (QS54) | Management review procedures, 820.20(c) | 49 |

How to use it, and its limits:

- **Pre-QMSR.** The data cite the retired QS regulation. FY 2025 ended before the QMSR took effect on 2 February 2026 (QS1). Later spreadsheets will cite QMSR and ISO 13485 clauses; trends across the boundary need a crosswalk (research "Changes and conflicts"; the crosswalk was not read). No FY 2026 dataset is listed yet (research "Not sourced").
- **Not complete.** The spreadsheets are system-generated 483s and are "not a comprehensive listing of all inspectional observations" (QS51).
- **Not a benchmark.** These are where FDA wrote observations across all device firms, not a rate or a target for the person's firm. Use them to say where inspectors have looked most, never to score the person.
