# Post-market feedback into the risk file

How observed harms are read against the risk file, and which reporting facts sit beside that work. Row ids refer to `quality-systems-sources.md`.

## The obligation

- MDR: evaluate production and post-market surveillance information for its impact on hazards and their frequency, on risk estimates, on overall risk, benefit-risk and acceptability; amend controls where needed (EU15, EU14).
- FDA: review and update risk documentation when the manufacturer becomes aware of previously unforeseen risks or new information about known risks (QS22).
- ISO 14971, as FDA's public abstract states it, includes monitoring the effectiveness of risk controls (ST4).
- CAPA under the QMSR is to be proportionate to the size of the problem and the risk (QS18); the MDR requires CAPA with verification of effectiveness (EU4).

## Reading an observed event against the file: four outcomes

Working convention of this skill (not quoted from a standard). For each event the person maps to the file:

| Outcome | When | What it asks of the owner |
|---|---|---|
| Foreseen and within estimate | The event matches a hazard in the file and the observed severity is not above the file's estimate on the person's scale | Confirm the probability estimate still holds as events accumulate |
| Foreseen, worse than estimated | The event matches a hazard but the observed severity is above the file's estimate | Re-estimate; check whether the control performed |
| Foreseen, control did not prevent it | The event matches a hazard whose control should have prevented this sequence | Investigate the control's effectiveness; CAPA proportional to risk (QS18) |
| Not foreseen | No hazard in the file matches | Add the hazard; FDA's update expectation for unforeseen risks applies (QS22) |

The person maps each event to a hazard and sets severity on their own scale. The model may propose a mapping, marked "proposed", with the words in the event that support it. `scripts/risk_feedback.py` lays the mapped events beside the file; it does not decide which outcome applies.

## Own events and comparable events are different evidence

- **Own events** (the person's complaints, MDR or vigilance files) are occurrences of the person's product. They bear on probability and severity estimates.
- **Comparable events** (another product's recall or alert from the library) show that a hazard is foreseeable and how severe it got elsewhere. They are never counted as occurrences of the person's product.

## Harm in software is often indirect

MDCG 2023-3 Rev.2 (January 2025): harm arising from a medical decision based on incorrect information or results from a device is indirect harm, and must be reported when it meets serious-incident criteria (VG14). Its malfunction example is a software error causing an incorrect assessment and treatment (VG15). A complaint that says "the number was wrong" may therefore describe a harm chain even when no injury is reported.

## Reporting facts that sit beside this work

These are clocks and definitions, stated as facts. Whether a given event is reportable is the person's decision (their regulatory or vigilance owner); this skill does not decide it.

| Jurisdiction | Fact | Row |
|---|---|---|
| EU | Incident includes malfunction, use error due to ergonomic features, inadequate manufacturer information, undesirable side-effect. Serious incident: led or might have led to death, serious deterioration of health, or a serious public health threat. | VG1, VG2 |
| EU | Serious incident: no later than 15 days after awareness; serious public health threat: 2 days; death or unanticipated serious deterioration: 10 days. Calendar days; awareness day is day 0. | VG4, VG5, VG6, VG12 |
| EU | Awareness date: when the first employee or representative, including outsourced complaint handlers, receives the information. | VG11 |
| EU | Statistically significant increases in non-serious incidents or expected side-effects are trend-reported; method and observation period sit in the PMS plan. | VG9 |
| EU | Complaint definition follows EN ISO 13485:2016, as MDCG restates it. | VG16 |
| GB | Same 15, 2 and 10 day limits since 16 June 2025. | VG26 to VG28 |
| US | MDR report within 30 calendar days; 5 work days when remedial action is needed to prevent unreasonable risk of substantial harm. | VG17, VG18 |
| US | Corrections and removals to reduce a risk to health: report within 10 working days of initiation; a correction includes modification without physical removal, which covers pushed software changes. Unreported corrections still need a record with a justification. | VG22, VG24, VG25 |
| US | Investigated or reportable complaints record seven items, including device name, date, UDI, nature of complaint and any corrective action. | QS11 |

If an event in the person's data may be reportable and no reporting decision is recorded, list it as an open item for the person's vigilance owner. Do not compute a deadline from a date the person has not confirmed as the awareness date.
