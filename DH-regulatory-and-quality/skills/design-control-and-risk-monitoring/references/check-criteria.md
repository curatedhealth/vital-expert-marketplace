# What a design control check looks at, and on what basis

Every criterion below carries the row id of `quality-systems-sources.md` (research pass of 19 October 2026). ISO 13485 and ISO 14971 clause text is paywalled and is `[GAP]` unless a row restates it. A check against these criteria produces **findings**: what the person's files show, what they do not show, and the source of the expectation. It does not produce a score or a compliance verdict.

## Criteria and their source

| # | Look for | Expectation and its source | Row |
|---|---|---|---|
| K1 | Design controls applied at all for this device | US: ISO 13485 Clause 7.3 applies to class II and III and to class I devices automated with software; IDE devices are not exempt. | QS9, QS14 |
| K2 | A design and development file that contains or references the records showing compliance | The former DHF maps to Clause 7.3.10. | QS24 |
| K3 | Trace from user need through input, output, verification, validation; hazards to controls to verification | Working structure (`trace-structure` checks G1 to G7, O1 to O3, R1, R2); expectations from EU19, ST4, ST6, EU16. | EU19, ST4, ST6, EU16 |
| K4 | Software validation and design transfer records | Named minimum elements of FDA inspection model 2. | QS33 |
| K5 | Software change records assessed for risk and impact before implementation | Change Control area purpose; "Software Changes" element (Clauses 4.1.6, 7.5.6, 7.6). | QS34 |
| K6 | Risk file current and used | US: FDA investigators read it throughout the inspection (QS31); FDA expects it updated on new or unforeseen risk information; MDR requires PMS information to feed it. | QS31, QS22, EU15 |
| K7 | Controls in priority order; residual risks disclosed | Design first, protective measures second, information for safety last; users told of residual risks. | EU16 |
| K8 | Software state of the art, single fault, IT security, minimum platform requirements | Annex I 17.1 to 17.4. | EU19, EU20, EU21 |
| K9 | EU QMS elements for design: compliance strategy with change management, risk management, CAPA with effectiveness checks | Article 10(9) (a), (e), (l); Annex IX 2.2(c). | EU3, EU4, EU23 |
| K10 | Changes in harmonized standards reflected in time | Article 10(9). | EU2 |
| K11 | For a US software change: the 510(k) decision recorded against the risk file | FDA's 2017 guidance asks first whether the change creates or modifies a hazard, hazardous situation or cause in the risk management file; it predates the QMSR and says so. | CH11, CH14, CH15, CH10 |
| K12 | For an EU legacy device: no significant change in design or intended purpose | MDCG 2020-3 Rev.1, chart C for software; bug fixes and security updates are examples of non-significant changes only if benefit-risk is not negatively affected. | CH2, CH5 to CH8 |

## Sampling

Check every hazard in the risk file against its controls and verifications. If the file is too large and the person asks for a sample, say how the sample was drawn and include hazards that do not trace as well as those that do. The earlier task wording carried the rule: "Do not sample only the hazards that trace."

## Grading: only if the person chooses a scheme

The model does not grade findings. If the person wants a grade, offer the MDSAP scheme as one public option they may apply themselves (MDSAP AU P0037.001, effective 8 September 2021, fda.gov copy; the authoritative copy has moved to the TGA-managed site, QS39):

- grade = QMS impact (direct 3, indirect 1) plus 1 each for a repeat nonconformity, a missing procedure combined with failure to implement, and release of nonconforming devices (QS45);
- ISO 13485 clauses 4.1 to 6.3 are indirect except 4.2.3; 6.4 to 8.5 are direct except 8.2.4 (QS46), so design and development (7.3) findings are direct-impact under this scheme;
- a repeat nonconformity is one found in audits in the previous three years (QS47).

The person scores each element. The model then adds up what they scored and states the result as theirs.

## Context, never a target

FY 2025 device Form 483s (inspections ending 1 October 2024 to 30 September 2025, under the old QS regulation): 791 system-generated 483s; design change procedures cited 48 times and risk analysis 47 times; CAPA procedures 279 and complaint procedures 211 were the most cited (QS52 to QS54). These show where investigators found problems. They are not a benchmark for the person, and they cite retired section numbers; a crosswalk to the QMSR was not read.
