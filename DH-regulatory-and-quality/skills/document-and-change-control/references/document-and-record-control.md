# Document and record control: what the sources require

Interpretive reference for task A1. Every statement cites its row: QS, EU, VG, ST rows are in `QUALITY_SYSTEMS.md`; QX rows are in `supplementary-rows.md`. All rows were read on 19 October 2026 from primary sources. ISO 13485 clause text is not sourced (paywalled); what appears here is what FDA, the MDR or a regulator says. Where a point is not sourced it is marked `[GAP]`.

## 1. The US frame since 2 February 2026

| Point | What the source says | Row |
|---|---|---|
| Which rule | The QMSR took effect on 2 February 2026. No phase-in. | QS1, QS2 |
| What it is | Part 820 incorporates ISO 13485:2016 by reference, plus Clause 3 of ISO 9000:2015. | QS3, QS4 |
| Conflicts | Where an ISO 13485 clause conflicts with the FD&C Act or FDA regulations, US law controls. | QS5 |
| Core duty | Document a QMS that complies with ISO 13485 and the rest of part 820. | QS7 |
| Software | Software and firmware are components under the QMSR definition. | QS6 |
| Certificate | An ISO 13485 certificate does not replace an FDA inspection. | QS25 |
| Reading the standard | ISO 13485:2016 and ISO 9000:2015 Clause 3 can be read free, read-only, through the ANSI IBR portal and the ISO Online Browsing Platform. | ST13 |

## 2. Documents versus records

FDA restates the split in ISO 13485: documents required by the QMS are controlled under Clause 4.2.4; records are a special type of document, controlled under Clause 4.2.5 (QX1). What Clauses 4.2.4 and 4.2.5 require in detail is `[GAP]` in these sources; the person's team should read them through the free portal (ST13).

The QMSR adds US content on top of Clause 4.2.5 (QX2):

| Record | Required content | Row |
|---|---|---|
| Complaints that are reported under part 803, must be investigated, or were investigated | Seven items: device name, date received, UDI or UPC, complainant contact, nature and details, correction or corrective action, reply | QS11 |
| Complaints not investigated because a similar one was | The justification for not investigating | QS12 |
| Servicing | Six items: device, UDI or UPC, date, who serviced, service performed, test and inspection data | QX3 |
| Every device or batch | The UDI | QX4 |
| Labeling | Release of labeling documented; results of labeling inspection documented | QS13, QX6 |
| Confidential records | May be marked to help FDA decide on disclosure | QX5 |

**Old record names.** The QMSR drops the separate DMR, DHF and DHR record types; FDA says their elements are largely required by ISO 13485 Clause 4.2 and Clause 7 (QX7). The former design history file maps to the design and development file, Clause 7.3.10 (QS24). Design and development requirements apply to class II and III devices and to class I devices automated with software (QS9).

## 3. The inspectability change

Under the old QS regulation, 820.180(c) kept management review, internal audit and supplier audit reports out of FDA inspection. The QMSR does not keep that exception: FDA may now inspect them (QS15). FDA expects these records to be "readily available upon inspection" (QX8) and calls robust management review and audit programs fundamental to the culture of quality it expects (QS16). Investigators may also review QMS records created before 2 February 2026; FDA suggests a comparative analysis showing older records meet the QMSR (QS26).

What this means for setup: write management review and audit reports knowing an investigator may read them. That is a consequence of QS15 and QX8, not a rule about tone or content, which the sources do not set.

## 4. Retention periods

| Record | Period | Row |
|---|---|---|
| EU: technical documentation, EU declaration of conformity, certificates | At least 10 years after the last device covered by the declaration is placed on the market; at least 15 years for implantables | EU6 |
| US: MDR event files (including the deliberations on whether an event was reportable) | 2 years from the event or the device's expected life, whichever is greater | VG21 |
| US: records of corrections and removals not reported to FDA | 2 years beyond the device's expected life; the record includes a justification for not reporting, reviewed by a designated person | VG24 |
| US: general QMS records under ISO 13485 Clause 4.2.5 | `[GAP]`: the clause text is not sourced, and the QMSR text read (820.35) adds content, not a period | QX2 |

Never state a general US retention period from memory. Say `[GAP]` and point to Clause 4.2.5 through the free portal.

## 5. EU frame

- Article 10(9) lists 13 minimum QMS elements, starting with a regulatory compliance strategy that includes procedures for managing modifications to devices (EU3), and including risk management, vigilance and CAPA with effectiveness checks (EU4).
- Design changes and changes in harmonized standards must be taken into account in a timely manner (EU2).
- Under Annex IX, the QMS documentation for assessment covers management of design or QMS changes (EU23).
- EN ISO 13485:2016 with A11:2021 is a harmonized standard under the MDR (EU28, EU29); conforming to it gives a presumption of conformity for what it covers (EU26). EN 62304 is not harmonized under the MDR as of the 11 June 2026 amendment (EU30, measured).
- The PRRC must ensure technical documentation and the declaration are kept up to date (EU10); where responsibility is shared, areas are set out in writing (EU11).

## 6. How inspectors and auditors look at it

- FDA's Compliance Program 7382.850, in use since 2 February 2026, organizes inspections into 6 QMS areas and 4 other FDA requirements (QS28 to QS30). Its Change Control area exists "to ensure changes are adequately evaluated for risk and impact on products and processes prior to implementation", with software changes as an element (QS34).
- MDSAP grades nonconformities 1 to 5 (QS44). ISO 13485 clauses 4.1 to 6.3 count as indirect QMS impact, except 4.2.3 (medical device file), which is direct (QS46). Document and record control (4.2.4, 4.2.5) therefore sits in the indirect range by that rule; a missing procedure combined with failure to implement adds a point (QS45). Grades are the auditor's decision, not the model's.

## 7. The controlled document lifecycle used in this pack

The lifecycle below is the pack's working method (evidence class O: owner-stated method of the VITAL register task "Controlled document" and "Obsolete copy"), not a quotation of ISO 13485. It is built to produce the records the rows above ask for.

| Stage | What is recorded | Why (row) |
|---|---|---|
| 1. Identify | Document id, title, owner, the QMS process it serves | QS7 (documented QMS) |
| 2. Draft and review | Version, reviewer, what changed against the predecessor | QX1 (documents controlled) |
| 3. Approve | Approver named by the person, date | QX1; approver rules in Clause 4.2.4 are `[GAP]` |
| 4. Release | Effective date, where the current version lives | QX9 (be ready to provide records) |
| 5. Change | Change record that links to the change assessment (task A2) | QS34, QX13, QX22 |
| 6. Withdraw | Obsolete version removed from points of use, kept as a record if needed | QX1; Clause 4.2.4 detail `[GAP]` |
| 7. Retain | Retention period per record type (section 4) | EU6, VG21, VG24 |

Gaps the person fills: who may approve, how electronic signatures are handled (not sourced in these files), and retention periods for records with no sourced period.
