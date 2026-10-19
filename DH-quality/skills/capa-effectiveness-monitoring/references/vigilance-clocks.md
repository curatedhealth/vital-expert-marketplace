Shared origin: written for the dh-quality pack in the audit-capa-and-complaints skill (DH-03.02.4.1), copied unchanged; row ids refer to quality-systems-sources.md and primary-text-additions.md.

# Complaints and vigilance: is it a complaint, is it reportable, by when

Interpretive reference for task A2 (and for the timeliness check in the monitoring skill). Rows cited from `quality-systems-sources.md` (QS, EU, VG) and `primary-text-additions.md` (R). The model lays out the criteria and computes dates. Whether an event is reportable is decided by the person's reporting owner.

## 1. Is it a complaint?

- MDCG 2023-3 Rev.2 adopts the EN ISO 13485:2016 definition: a written, electronic or oral communication that alleges deficiencies related to identity, quality, durability, reliability, usability, safety or performance of a device (VG16).
- US records for complaints that are investigated or reportable must hold seven items: device name, date received, UDI or UPC, complainant contact, nature and details, any correction or corrective action, any reply (QS11, 21 CFR 820.35(a)).
- A repeat investigation is not needed for a similar complaint, but the justification must be recorded (QS12).
- Devices exempt from CGMP still keep complaint files under 820.35 (QS14).

## 2. Is it reportable?

### European Union (MDR)

| Term | Meaning | Row |
|---|---|---|
| Incident | Malfunction or deterioration in characteristics or performance, use-error due to ergonomic features, inadequate information supplied, undesirable side-effect | VG1 |
| Serious incident | Directly or indirectly led, might have led or might lead to death, temporary or permanent serious deterioration of health, or a serious public health threat | VG2 |
| Indirect harm (software) | Harm from a medical decision based on incorrect information or results from the device (misdiagnosis, delayed treatment) is indirect harm and is reported when it meets serious incident criteria | VG14 |
| Software malfunction example | A software error that leads to a wrong assessment and wrong treatment | VG15 |
| FSCA | Corrective action for technical or medical reasons to prevent or reduce the risk of a serious incident with a marketed device | VG3 |

If the manufacturer is unsure whether an incident is reportable, it reports anyway within the deadline; an incomplete initial report is allowed (VG7). The PRRC ensures the Article 87 to 91 reporting obligations are fulfilled (EU10).

### Great Britain

The Medical Devices (Post-market Surveillance Requirements) (Amendment) (Great Britain) Regulations 2024 were made on 16 December 2024 and came into force on 16 June 2025 (VG26, VG27). They set the same 15, 2 and 10 day limits in new regulation 44ZH (VG28). For similar incidents with a known cause or an FSCA in place, periodic summary reports may be agreed with the Secretary of State (VG29). GB definitions, the GB awareness rule and the GB day-counting convention are not in the sourced rows `[GAP]`; MHRA guidance text beyond the statutory instrument was not read.

### United States (21 CFR 803 and 806)

| Term | Meaning | Row |
|---|---|---|
| Reportable (30-day) | Information that reasonably suggests a marketed device may have caused or contributed to a death or serious injury, or has malfunctioned and would be likely to cause or contribute to one if the malfunction recurred | VG17 |
| Serious injury | Life-threatening; permanent impairment or damage; or needs medical or surgical intervention to preclude it | R10 |
| Malfunction | Fails to meet performance specifications (including labeling claims) or to perform as intended | R11 |
| Caused or contributed | Includes failure, malfunction, design, manufacture, labeling or user error | R12 |
| Become aware | 30-day: when any employee becomes aware of a reportable event. 5-day: when a manager or supervisor over regulatory, scientific or technical staff (or someone whose duties relate to adverse event reporting) becomes aware, from any information, that remedial action is needed | VG19 |

MDR procedures must cover timely identification and evaluation, a standardized reportability review, and timely transmission (VG20). Event files document the deliberations behind each reportable and non-reportable decision and are kept 2 years from the event or the device's expected life, whichever is longer (VG21). Under the QMSR, ISO 13485 regulatory reporting is met by reporting under part 803, and advisory notices are handled under part 806 (QS8).

**Corrections and removals (806).** A correction is a repair, modification, adjustment, relabeling, destruction or inspection without physical removal (VG25); the research row reads this as including software changes pushed in place, which is the row's interpretation, not the regulation's words. Report corrections or removals made to reduce a risk to health or remedy a violation that may present a risk to health (VG22); risk to health includes temporary or medically reversible consequences (R13). Exempt: improvements that do not reduce a risk to health, market withdrawals, routine servicing, stock recovery (VG23). Unreported actions still need a record with a justification reviewed by a designated person (VG24).

## 3. The clocks

| Jurisdiction and event | Limit | Counted from | Rule |
|---|---|---|---|
| EU serious incident | Immediately, and not later than 15 days | Awareness | Art. 87(3), VG4 |
| EU death or unanticipated serious deterioration | Not later than 10 days | Awareness | Art. 87(5), VG6 |
| EU serious public health threat | Immediately, and not later than 2 days | Awareness | Art. 87(4), VG5 |
| EU FSCA | In advance of the FSCA, except in urgency | Before it is undertaken | Art. 87(8), VG8 |
| GB serious incident / death or unanticipated / public health threat | 15 / 10 / 2 days | Awareness | Reg. 44ZH, VG28 |
| US 30-day report | 30 calendar days | Day after awareness | 803.50(a), VG17 |
| US 5-day report | 5 work days (Monday to Friday, except Federal holidays) | Day after management awareness that remedial action is needed (not first receipt) | 803.53, VG18, VG19, R9 |
| US correction or removal | 10 working days | Initiation of the correction or removal | 806.10(b), VG22 |

**Counting days in the EU.** Calendar days; the awareness date is day 0, and the period starts on day 1 (VG12). The awareness date is when the first employee or representative of the manufacturer, including outsourced complaint handlers, receives the information (VG11). So an awareness date of 9 October gives a 15-day limit of 24 October.

**Counting the US 5-day report.** Ask who with management or supervisory responsibility learned of the event, and when. If that date is unknown, show the 5-day date from first receipt as the earliest possible and from the management date as given, and do not mark the 5-day date passed unless the management awareness date is known. Federal holidays are excluded by definition (R9): when one falls in the window, lead with the holiday-excluded date and say which holiday was excluded; if the holiday list was not supplied, say the date may be later. The helpers (`reporting_clock.py` in audit-capa-and-complaints, `complaint_trends.py` in capa-effectiveness-monitoring) read the OPM Federal holiday list for 2026 and 2027 (R14) and warn when a window runs outside those years. Example: management awareness on 8 October 2026 gives 16 October 2026, because Columbus Day, 12 October 2026, is excluded (R14).

**Late determination.** If new information later makes an incident reportable, the report gives both the incident awareness date and the reportability awareness date and explains the difference (VG13). Which date starts the clock is not stated in the sourced rows `[GAP]`; show both and let the reporting owner decide.

**Trend reports.** The MDR requires reporting of statistically significant increases in non-serious incidents or expected side-effects; the method and observation period belong in the PMS plan (VG9). No fixed day count is in the sourced rows.

**After an MIR.** The manufacturer investigates without delay, including a risk assessment, and does not alter the device or samples in ways that affect cause analysis before informing the authority (VG10).

`scripts/reporting_clock.py` computes every row of the table above from one anchor date.
