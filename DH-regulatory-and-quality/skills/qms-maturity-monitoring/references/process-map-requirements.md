> Shared origin: built in the DH-03.02.3.1 skill build (qms-design-and-governance/references/process-map-requirements.md), 19 October 2026, copied unchanged below this line. It is the A1 process map the maturity check runs against.

# Process map requirements: which source asks for which process

Interpretive reference for A1. Every cell cites row ids in `quality-systems-research.md` (QS, EU, ST, VG, CH), `qms-requirements-additions.md` (BX) or `multi-region-research.md` (MR). Clause numbers are ISO 13485:2016 clause numbers as FDA prints them in Compliance Program 7382.850 (BX6). Clause text is never quoted: it is paywalled (free read-only access: ST13). Where no row supports a cell, the cell says `[GAP]`.

## 1. Which requirement set applies, by market

| Market | What the QMS must meet | Rows | What the person must tell you |
|---|---|---|---|
| United States | Part 820 (QMSR) since 2 February 2026: a documented QMS complying with ISO 13485:2016 as incorporated, plus US additions (complaint records, labeling, reporting under parts 803 and 806). US law controls where a clause conflicts. | QS1, QS3 to QS8, QS11, QS13 | Device class; whether design controls apply (class II, III, and class I automated with software: QS9); any CGMP exemption (complaint files still required: QS14) |
| European Union | MDR Article 10(9): a QMS proportionate to risk class and device type, covering all quality-relevant parts of the organization, with at least elements (a) to (m). A risk management system (Article 10(2)). A person responsible for regulatory compliance (Article 15). Under Annex IX, notified body audits at least every 12 months and unannounced audits at least once every five years. | EU1 to EU5, BX1, BX2, EU8 to EU11, EU22 to EU25 | Device class and conformity route. Which classes go through an Annex IX QMS audit is not in the research rows `[GAP]`: take it from the person's regulatory owner or the Regulatory pack |
| Canada | A QMS certificate to CAN/CSA-ISO 13485 for Class II license applications in the regulation; the MDSAP site states MDSAP certification is required for Class II, III and IV licenses. | MR-03, MR-05 | Device class in Canada |
| Australia | TGA may use MDSAP reports and certificates if Australian requirements were covered in the audit. | MR-36, MR-07, MR-42 | Whether Australia is a target market (it changes the MDSAP audit scope) |
| Brazil | ANVISA may use MDSAP audits instead of its own inspection for the GMP certificate for class III and IV. | MR-37 | Device class in Brazil |
| Japan | MHLW and PMDA may use an MDSAP report to exempt a site from on-site inspection or replace much of the documentation; PMDA may still inspect. | MR-38 | Whether Japan is a target market |
| Switzerland | Only devices with a declaration of conformity under Swiss or EU law are recognized today; EU notified body certificates can be deemed equivalent. | MR-19, MR-20 | Whether the EU QMS and certificates will carry Switzerland |
| United Kingdom | The research rows hold GB post-market surveillance and vigilance rules (VG26 to VG29) and the MHRA's MDSAP observer status (QS38), not the GB QMS requirement itself `[GAP]`. Reliance proposals are not yet law (MR-24 to MR-26). | VG26 to VG29, QS38, MR-24 to MR-26 | Take the GB QMS route from the regulatory owner |

## 2. Process map skeleton

Use this as the starting list. Keep the person's own process names where they have them; the "US basis" and "EU basis" columns say which requirement each process answers. A process the person runs that no row supports is kept, marked "the person's process, no regulatory row".

| # | Process | US basis (QMSR, CP 7382.850 area and element) | EU basis (MDR) | MDSAP audit chapter (QS43) |
|---|---|---|---|---|
| P1 | QMS planning, quality manual, medical device file, document and record control | 820.10(a) (QS7); Management Oversight: QMS 4.1.1 to 4.1.4, quality manual 4.2.2, medical device file 4.2.3, documents and records 820.35, 820.45, 4.2.1, 4.2.4, 4.2.5 (BX7) | Art. 10(9) scope (BX1); retention at least 10 years, 15 for implantables (EU6) | Management |
| P2 | Management responsibility and management review | Management Oversight: commitment 5.1, policy and objectives 5.3, 5.4.1, 5.4.2, responsibility and authority 5.5.1 to 5.5.3, management review 5.6.1 to 5.6.3 (BX7); "top management" per ISO 9000 (BX13); records inspectable (QS15) | Art. 10(9)(c) responsibility of the management (BX1) | Management |
| P3 | Regulatory compliance strategy, marketing authorization, registration | Inspection general items: registration and listing, marketing authorizations (BX5) | Art. 10(9)(a) strategy for regulatory compliance including conformity assessment and modifications (EU3); Art. 15 PRRC (EU8 to EU11) | Device marketing authorization and facility registration |
| P4 | Resources, competence and infrastructure | Provision of resources 6.1, human resources 6.2 (BX7); infrastructure 6.3 (BX12) | Art. 10(9)(d) resource management (BX1) | `[GAP]` chapter mapping not read |
| P5 | Risk management | Risk management throughout the QMS (QS20); risk-based approach 4.1.2 b) (BX7); ISO 14971 not incorporated (QS21) but FDA-recognized (ST5); the risk file steers the inspection (QS31); update risk files on new information (QS22) | Art. 10(9)(e) and Art. 10(2), Annex I Section 3 (EU4, EU5, EU14, EU15); EN ISO 14971:2019/A11:2021 harmonized (EU29) | `[GAP]` chapter mapping not read |
| P6 | Design and development, including the software lifecycle | Design controls scope (QS9); Design and Development area 7.3.1 to 7.3.10 including software validation 7.3.7 (BX10); design and development file replaces the DHF (QS24); IEC 62304 FDA-recognized (ST9) | Art. 10(9)(g) product realization (BX2); Annex I 17.1 to 17.4 software (EU19 to EU21); EN 62304 not harmonized (EU30) | Design and development |
| P7 | Clinical evaluation and PMCF | `[GAP]` no QMSR row in the research | Art. 10(9)(f) (BX2) | `[GAP]` |
| P8 | Purchasing and outsourcing (including software and cloud suppliers) | Outsourcing 4.1.5, purchasing 7.4.1 to 7.4.3 (BX11) | Art. 10(9)(d) selection and control of suppliers and sub-contractors (BX1) | Purchasing |
| P9 | Production and service provision: release, deployment, servicing, identification, traceability, labeling, UDI | Production and Service Provision area (BX12); labeling 820.45 (QS13); UDI as an OAFR (BX4) | Art. 10(9)(g) and (h) UDI verification (BX2) | Production and service controls |
| P10 | Change control (QMS, software, product and process, purchasing) | Change Control area: QMS changes, software changes 4.1.6, 7.5.6, 7.6, product and process changes, purchasing changes (BX9, QS34); software changes are design changes (CH9) | Art. 10(9)(a) management of modifications (EU3); changes taken into account in a timely manner (EU2); substantial QMS changes to the notified body (EU24) | `[GAP]` |
| P11 | Feedback and complaint handling | Complaint handling 820.10(b)(3)(4), 820.35, 8.2.2, 8.2.3 (BX8); seven complaint record items (QS11); justification when not investigating (QS12) | Art. 10(9)(j) communication with customers (BX2); complaint definition per EN ISO 13485 (VG16) | Measurement, analysis and improvement |
| P12 | Vigilance and regulatory reporting; corrections and removals | OAFR Medical Device Reporting, part 803 (BX4; VG17 to VG21); Reports of Corrections and Removals, part 806 (BX4; VG22 to VG25) | Art. 10(9)(k) (EU4); Art. 87 clocks of 15, 10 and 2 days (VG4 to VG8); MDCG 2023-3 awareness date (VG11, VG12) | Adverse events and advisory notices reporting |
| P13 | Post-market surveillance and trend reporting | Feedback 8.2.1 (BX8) | Art. 10(9)(i) PMS system (BX2); PSUR for class IIa and above, class IIa at least every two years (BX16); production and PMS information fed into risk (EU15); trend reporting method in the PMS plan (VG9) | `[GAP]` |
| P14 | Internal audit | Internal audits 8.2.4 (BX8); audit reports now inspectable (QS15) | Not named in the Article 10(9) list; notified body audits under Annex IX (EU25) | `[GAP]` chapter mapping not read |
| P15 | Nonconforming product, data analysis, CAPA | Nonconforming product 8.3.1 to 8.3.4, analysis of data 8.4, corrective action 8.5.2, preventive action 8.5.3 (BX8); CAPA proportional to risk (QS17, QS18) | Art. 10(9)(l) CAPA and verification of effectiveness, (m) monitoring, data analysis and improvement (EU4, EU3) | Measurement, analysis and improvement |
| P16 | Communication with authorities and notified bodies | `[GAP]` no QMSR row | Art. 10(9)(j) (BX2) | `[GAP]` |

Notes on reading the map:

- The MDSAP column names a chapter only where QS43 names a chapter with that title. The research holds the chapter titles, not which clauses each chapter audits; other cells stay `[GAP]`.
- "US basis" cites the CP area as the place an investigator looks. The legal duty is Part 820 and ISO 13485 as incorporated (QS7).
- For a software-only product, P9 still applies: release, deployment and servicing are production and service provision activities. Whether a cell such as sterile product validation applies is the person's call; say "not applicable, per the person" rather than deleting it.

## 3. Scope statement: what it has to say

From the rows above, a scope statement for a multi-market QMS names:

1. The products and versions covered, by name. Never claim the QMS for a product it does not name.
2. The sites and outsourced parties (P8).
3. The markets and, per market, the device class the person states, and the requirement set from section 1.
4. Exclusions or non-applicable requirements with the reason. Under the QMSR, design and development (7.3) cannot be excluded for class II, III or software-automated class I devices (QS9); IDE devices are not exempt from design requirements (QS14).
5. The PRRC arrangement for the EU (EU8, EU9) and, where responsibilities are shared, that they are set out in writing (EU11).
