# Operating model options: the facts per option

Interpretive reference for B1. It lays out sourced facts that bear on each option. It does not score or rank: the person scores, the connector's `analytics.mcda` ranks what they scored, and `scripts/mcda_swap.py` shows where a weight change would flip the order.

## The decisions usually on the table

| Decision | Typical options (the person may add their own) |
|---|---|
| D1 Structure | One global QMS for all markets; one QMS with regional annexes; separate regional QMSs |
| D2 MDSAP | Join MDSAP now; join later when a dependent market is added; do not join |
| D3 EU conformity | The route and notified body are a regulatory decision; this skill only records the QMS consequences (Annex IX audits) |
| D4 Sites and outsourcing | Which activities stay in-house and which are outsourced (cloud hosting, development, complaint intake) |
| D5 Governance shape | One management review for all markets, or one per region feeding a global review |

## Facts that bear on D1 (structure)

| Fact | Rows |
|---|---|
| The QMSR incorporates ISO 13485:2016 and FDA judged it substantially similar to the old QS regulation; US additions remain (complaints, labeling, reporting). | QS3, QS7, QS8, QS11, QS13 |
| The final rule expected establishments to run internal audits and management reviews on aligned requirements instead of separately for the QS regulation and ISO 13485. | BX15 |
| The MDR QMS must cover all parts of the organization dealing with quality and is proportionate to risk class and device type. | EU1, BX1 |
| EN ISO 13485:2016 with A11:2021 is harmonised under the MDR. | EU28, EU29 |
| Where an ISO 13485 clause conflicts with US law, US law controls. | QS5 |

What this means for the person, stated as consequences only: one ISO 13485-based system can be the base for both the QMSR and the MDR, with US-specific and EU-specific requirements added where the rows show them (complaint record items, reporting parts 803 and 806, PRRC, UDI, PMS, clinical evaluation). Whether to hold those additions in one system or in regional systems is the person's decision.

## Facts that bear on D2 (MDSAP)

| Fact | Rows |
|---|---|
| Members: TGA, ANVISA, Health Canada, MHLW and PMDA, FDA. Observers: EU, Singapore HSA, UK MHRA, WHO IVD prequalification. | QS38, MR-32, MR-33 |
| Each member uses MDSAP outputs differently and keeps its own marketing authorization power. | MR-35 |
| Canada: the MDSAP site states MDSAP certification is required for Class II, III and IV licenses; the regulation itself requires a QMS certificate from a recognized registrar. | MR-03, MR-05, MR-06 |
| United States: FDA uses MDSAP audit reports as a substitute for surveillance inspections, not certificates; non-surveillance inspections still apply; PMA pre-approval and post-approval inspections are not replaced. | QS40, MR-39, MR-40, MR-43 |
| United States: FDA will not accept an ISO 13485 certificate in place of inspection. | QS25 |
| Australia: TGA considers MDSAP certificates and reports if Australian requirements were covered. | MR-36 |
| Brazil: ANVISA may use MDSAP audits for the GMP certificate for class III and IV. | MR-37 |
| Japan: MDSAP reports can exempt a site from on-site inspection or replace documents; PMDA may still inspect. | MR-38 |
| Singapore (observer) accepts MDSAP certificates as QMS evidence; Korea can replace on-site GMP audits with document review. | MR-41 |
| Audit cycle: three years, initial, two partial surveillance audits, recertification; special and unannounced audits possible. | QS42 |
| Grading: nonconformities graded 1 to 5; a 5-day notice to regulators for one grade 5 or more than two grade 4. | QS44 to QS48 |
| MDSAP documents moved to a TGA-managed site (18 December 2025); the research read fda.gov copies, which may be superseded. | QS39, MR-34 |
| The EU is an observer, not a member. No row says an MDSAP audit replaces a notified body audit under the MDR `[GAP]`; Annex IX audits still apply. | QS38, EU22, EU25 |

What this means, as consequences only: the markets the person targets decide how much MDSAP changes. Canada is the market where the rows tie MDSAP to the license itself (MR-05). For the US it changes surveillance inspections only. For the EU the rows show no substitution.

## Facts that bear on D4 (outsourcing)

| Fact | Rows |
|---|---|
| Software is a component under the QMSR. | QS6 |
| Outsourcing and purchasing is one of the six QMS areas FDA inspects; purchasing controls were the third most cited device 483 area in FY 2025 (pre-QMSR numbering). | BX3, BX11, QS53 |
| Outsourced complaint handlers count for the EU awareness date. | VG11 |
| The MDR QMS includes selection and control of suppliers and sub-contractors. | BX1 |

## Facts that bear on D5 (governance shape)

See `governance-records.md`. Each management review and audit report is inspectable by FDA (QS15). A regional review feeding a global one creates more records; the person decides whether that is worth it.

## Sequencing by dependency, not by date

Some choices block others. Lay them out as "X before Y because Z" from the rows:

- Markets and device classes (A1 scope) before D2: the MDSAP value depends on which members' markets are targeted (MR-35 to MR-39).
- D2 before the audit calendar in A2: MDSAP fixes a three-year audit cycle (QS42).
- EU route (D3, with the regulatory owner) before the PRRC and notified-body audit cadence in A2 (EU8, EU25).
- D1 before writing procedures: the structure decides whether US and EU additions are in one procedure or several.
- Any substantial QMS change under an existing EU certificate is notified to the notified body (EU24) before it takes effect.

Never attach dates or urgency to the sequence. Clocks in the rows (for example MDSAP report deadlines) are facts, not pressure.
