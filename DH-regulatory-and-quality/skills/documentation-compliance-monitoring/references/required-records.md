# Required records: the checklist behind the document check

Interpretive reference for task A1. Each line names a record or document that a sourced row requires, when it applies, and the row. QS, EU, VG, CH and ST rows are in `QUALITY_SYSTEMS.md`; QX rows in `supplementary-rows.md`. Read on 19 October 2026.

This is not the full ISO 13485 list. ISO 13485 clause text is not sourced (paywalled), so the records it requires beyond what FDA or the MDR restate are `[GAP]` here. The person's own QMS procedure list fills that part; the check compares their documents to their procedures and to the lines below.

## United States (QMSR, in force since 2 February 2026)

| Id | Record or document | Applies when | Row |
|---|---|---|---|
| US-R1 | Documented QMS complying with ISO 13485 and part 820 | Always | QS7 |
| US-R2 | Design and development file (the former DHF) | Class II and III; class I automated with software | QS9, QS24 |
| US-R3 | Complaint records with seven items (device, date, UDI or UPC, complainant contact, nature, correction, reply) | Complaints reported under part 803, required to be investigated, or investigated | QS11 |
| US-R4 | Justification for not investigating a complaint | A similar complaint was already investigated | QS12 |
| US-R5 | Servicing records with six items | Servicing is performed | QX3 |
| US-R6 | UDI recorded for each device or batch | Always for devices with a UDI | QX4 |
| US-R7 | Labeling release record and labeling inspection results | Labeling is released | QS13, QX6 |
| US-R8 | Management review, internal audit and supplier audit reports, readily available | Always; inspectable since 2 February 2026 | QS15, QX8 |
| US-R9 | CAPA records under ISO 13485 8.5.2 and 8.5.3 | Always | QS17 |
| US-R10 | Risk management documentation, reviewed when new information emerges | Always; investigators use it throughout the inspection | QS22, QS31 |
| US-R11 | Written MDR procedures | Always | VG20 |
| US-R12 | MDR event files with reportability deliberations | Each event evaluated | VG21 |
| US-R13 | Records of unreported corrections and removals, with justification reviewed by a designated person | A correction or removal was not reported | VG24 |
| US-R14 | Change records: the change and the documented basis for not submitting, available to an investigator | Each software change to a 510(k) device | QX13, QX14, QX20 |
| US-R15 | Comparative analysis showing pre-2 February 2026 records meet the QMSR | Suggested, not required | QS26 |

## European Union (MDR, consolidated text of 10 January 2025)

| Id | Record or document | Applies when | Row |
|---|---|---|---|
| EU-R1 | QMS covering the Article 10(9) elements, including a regulatory strategy with procedures for managing modifications | Always | EU1, EU3 |
| EU-R2 | Risk management system and a risk management plan per device | Always | EU5, EU14 |
| EU-R3 | Technical documentation, EU declaration of conformity and certificates, kept at least 10 years after the last device (15 for implantables) | Always | EU6 |
| EU-R4 | CAPA records with verification of effectiveness | Always | EU4 |
| EU-R5 | Vigilance reporting processes | Always | EU4 |
| EU-R6 | PMS plan stating the trend-reporting method and observation period | Always | VG9 |
| EU-R7 | PRRC responsibilities in writing where shared | More than one PRRC | EU11 |
| EU-R8 | Documentation of design and QMS change management for notified body assessment | Annex IX route | EU23 |
| EU-R9 | Documented justification that a change to a legacy device is not significant | Legacy device changed after 26 May 2021 | QX22, CH4 |
| EU-R10 | Notified body approval or supplement for certified-device changes that could affect safety and performance or conditions of use | MDR technical documentation certificate | QX30, QX31 |

## Version and citation checks (the pack's method)

From the VITAL register tasks "Document check" and "Document score" (evidence class O: owner-stated method, not a regulatory quotation):

| Check | Finding when it fails |
|---|---|
| Each controlled document has one current version, an owner and an approver | "No current version", "two versions marked current", "approver missing" |
| No obsolete version sits in the working set | "Obsolete copy in use" |
| Every submission or technical file cites the current version of each document it cites | "Wrong version cited" |
| The person's procedure names a record type that the list does not contain | "Record expected by your procedure not found" |

## Context: what inspectors cited (FY 2025, before the QMSR)

For inspections ending 1 October 2024 to 30 September 2025, 791 system-generated 483s fell in the Devices area (QS52). Among device citations: CAPA procedures 279, complaint procedures 211, MDR procedures 63, quality audit procedures 57, management review procedures 49, design change procedures 48, risk analysis 47 (QS53, QS54, measured). These cite the retired QS regulation sections; trends across 2 February 2026 need a crosswalk (QUALITY_SYSTEMS.md, changes and conflicts). They are context for where to look first, never a target or a prediction.
