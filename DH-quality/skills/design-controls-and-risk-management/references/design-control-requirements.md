# Design control requirements for device software: what the sources say

Every rule below carries the row id of `quality-systems-sources.md` (research pass of 19 October 2026, primary sources, quotes checked against raw downloads unless marked [WF]). ISO 13485, ISO 14971 and IEC 62304 are paywalled. This file states their content only where a regulator or a public catalogue page restates it. Where nothing restates a clause, it says `[GAP]`. Do not fill a gap from memory.

## United States: the QMSR

| Rule | What it means for a software team | Row |
|---|---|---|
| The Quality Management System Regulation took effect on 2 February 2026. Before that date the old QS regulation applied; there was no phase-in. | Design records made before 2 February 2026 are still inspectable; FDA suggests a comparative analysis showing older records meet the QMSR. | QS1, QS2, QS26 |
| Part 820 incorporates ISO 13485:2016 by reference, plus Clause 3 of ISO 9000:2015. Where an ISO 13485 clause conflicts with US law, US law controls. | "Following ISO 13485" is the US obligation, read through part 820's own additions. | QS3, QS4, QS5 |
| Software and firmware are components. | Third-party and open-source software that ends up in the device is in scope of purchasing and design controls. | QS6 |
| Design and development (ISO 13485 Clause 7.3 and subclauses) applies to class II and III devices and to class I devices "automated with computer software". | A class I software device is not exempt from design controls. | QS9 |
| Investigational (IDE) devices are not exempt from design and development requirements. | Design controls start before the pivotal study, not after clearance. | QS14 |
| The former design history file maps to the ISO 13485 design and development file (Clause 7.3.10), which must contain or reference all records needed to show compliance. | The trace matrix and the risk file are records the design and development file contains or references. | QS24 |
| The QMSR drops the old explicit rule that each design review include someone without direct responsibility for the stage; ISO 13485 Clause 7.3.5 governs. | Who attends a design review is set by the person's own procedure under 7.3.5. The clause text itself is `[GAP]` here. | QS23 |
| Risk management now runs through the whole QMS, not a single design clause; FDA does not incorporate ISO 14971 but says it may help. | See `risk-management-requirements.md`. | QS20, QS21 |
| FDA may review design and development records once the device is marketed, or after an IRB submission, PDP, premarket submission or a change to a marketed device. | The file has to be inspection-ready from the first submission. | QS37 |
| Under Compliance Program 7382.850 (from 2 February 2026), inspection model 2 names minimum elements including design and development software validation and design transfer; the Change Control area includes "Software Changes" (Clauses 4.1.6, 7.5.6, 7.6). | The design review should be able to show software validation, transfer and software change records on request. | QS28, QS29, QS33, QS34 |
| Investigators review risk management documentation throughout the inspection. | The risk file is read first and used to steer the inspection. | QS31 |

`[GAP]`: the text of every ISO 13485 subclause of 7.3. The research names Clause 7.3, 7.3.5 (design review) and 7.3.10 (design and development file) only through FDA's restatement; the research lists 7.3.9 (design change) among the clauses it could not source. The ISO text can be read free, read-only, through the ANSI IBR portal or the ISO Online Browsing Platform (ST13); point the person there.

## IEC 62304: recognized in the US, not harmonized under the MDR

| Fact | Row |
|---|---|
| IEC 62304 sets lifecycle requirements for medical device software, standalone or embedded. It does not cover validation and final release of the device, even when the device is entirely software. | ST6 |
| Current text: IEC 62304:2006+AMD1:2015, edition 1.1, published 26 June 2015, stability date 2028. Edition 2.0 is in preparation, forecast 26 October 2028 (read from the page's embedded data). | ST7, ST8 |
| FDA recognizes edition 1.1 in full, recognition number 13-79, entered 14 January 2019. | ST9 |
| EU: no entry for 62304 in Implementing Decision (EU) 2021/1182 or its amendments through 11 June 2026 (measured by text search). EN 62304 therefore gives no presumption of conformity under the MDR as of that amendment. Later decisions were not checked. | EU30 |
| IEC 82304-1:2016 covers health software products on general computing platforms, across the whole lifecycle including validation; FDA recognizes it in full (13-97). Its IEC webstore status is `[GAP]`. | ST10, ST11 |

What this means in practice: in the US, a declaration of conformity to IEC 62304 edition 1.1 can support a submission because FDA recognizes it. In the EU, following IEC 62304 is a way to show the Annex I 17.2 lifecycle requirement is met, but it carries no presumption; the manufacturer argues conformity directly against Annex I. Validation of the finished software device needs its own evidence in both cases, because 62304 does not cover it (ST6). The 62304 clause structure (software safety classes, unit and integration requirements) is `[GAP]` in the research; do not state it.

## European Union: MDR requirements that bear on design

| Rule | Row |
|---|---|
| The QMS covers, among 13 minimum elements, a regulatory compliance strategy with management of modifications, risk management per Annex I Section 3, and CAPA with effectiveness checks. | EU3, EU4 |
| Design changes and changes in harmonized standards or common specifications must be taken into account in a timely manner. | EU2 |
| Software is developed and manufactured to the state of the art, considering development lifecycle, risk management including information security, verification and validation. | EU19 |
| Software ensures repeatability, reliability and performance for its intended use; single fault conditions are handled to eliminate or reduce consequent risks. | EU20 |
| Mobile software accounts for platform features; the manufacturer states minimum hardware, network and IT security requirements, including protection against unauthorized access. | EU21 |
| Under Annex IX, the QMS documentation covers regulatory strategy, identification of general safety and performance requirements, risk management, clinical evaluation, and management of design or QMS changes. | EU23 |
| EN ISO 13485:2016 with A11:2021 (and corrigendum AC:2018) and EN ISO 14971:2019 with A11:2021 are harmonized; conformity gives a presumption of conformity for the requirements they cover. | EU26, EU28, EU29 |

## Where requirements in a trace matrix come from

A design input usually has one of three origins, and the matrix should say which (see `trace-structure.md`):

1. **A user need** (intended use, user, environment).
2. **A risk control** decided in the risk file (QS20 to QS22; EU14, EU16).
3. **A regulatory or standard requirement**, for example an Annex I 17.1 to 17.4 software requirement (EU20, EU21) or a QMSR addition such as labeling examination before release (QS13).

## Counts that show where inspections find problems (context only)

FY 2025 device Form 483s (inspections ending 1 October 2024 to 30 September 2025, before the QMSR): 791 system-generated 483s. Design-related citations measured from the spreadsheet: design change procedures (old 820.30(i)) 48; risk analysis (old 820.30(g)) 47 (QS52, QS54). These cite the retired QS sections; trends across 2 February 2026 need a crosswalk that was not read. They are context, never a target or a benchmark for the person.
