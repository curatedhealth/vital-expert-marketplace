# Integration quality monitoring rules, with rows

Interpretive reference for `integration-quality-monitoring`. Every rule carries its row id; the row (URL, verbatim quote, read date) is in the copied research files in this folder: `engineering-interop-security-research.md` (EN), `data-and-ai-research.md` (DA), `channels-partners-launch-research.md` (CP), `ux-accessibility-usability-research.md` (UX), `customer-success-implementation-research.md` (CS), `strategy-and-portfolio-research.md` (SP) and `product-lifecycle-research.md` (PL). In answers, cite the source name and date in plain words with the row id after it (`gap-rules.md`, "How to cite").

The person writes every check, pass rule, sample definition, ceiling and threshold, names every owner and sets every release and recheck date. No source in this skill sets a conformance rate, launch success rate, latency ceiling, mapping accuracy, unmatched rate, workaround count or adoption threshold: never supply one.

## 1. Conformance scoring (old DH-04.01.1.2)

- **Check definition.** The person lists must-support elements, cardinality and bound value sets for the profiles in use, with a pass rule per check and who runs them on which environment (old task DH-04.01.1.2.1). The sheet is built from the guide version the person selected; never score against another version. Element-level must-support lists are not in the sources: the person supplies the StructureDefinitions or the sheet `[GAP]` otherwise.
- **Version baseline.** If the sheet names a version, state whether it is the one ONC certification requires (FHIR R4.0.1, US Core 6.1.0: 45 CFR 170.215, eCFR read 20 October 2026, EN-133, EN-134) or a current HL7 publication (FHIR R5, US Core 9.0.0: EN-129, EN-132). Certification follows the regulation (EN research file, "Changes and conflicts").
- **Sample scoring.** A stated sample, at least one payload per profile, each check pass or fail with the payload id, failures grouped by resource type so a single broken profile is visible; never average away a profile that failed every sample (old task DH-04.01.1.2.2). `scripts/integration_check.py score` prints this, with S1 (failed in every sample), S2 (one sample only) and S3 (no sheet entry, not checked).
- **What certified EHR APIs owe the app.** Single-patient and group requests for USCDI data per US Core must support (EN-142), refresh tokens at least three months for confidential apps (EN-143), revocation at the patient's direction within one hour (EN-144), public API documentation (EN-145). These are duties of the certified EHR module. A miss against them is a fact about the EHR's behavior in the person's test, reported to the owner the person names; it is never a compliance finding by the model.

## 2. Launch reliability (old DH-04.01.2.2)

- **Matrix definition.** User roles, patient states and encounter states the product claims to support; a launch pass (the token carries the context the screen needs) and a write-back pass (the chart shows the written resource); latency ceilings for the token response and the first clinical read, all set by the person (old task DH-04.01.2.2.1). Never declare ready from a single happy-path launch (flag L7).
- **Context.** `launch/patient` and `launch/encounter` request context; a granted patient scope obliges the EHR to set patient context (HL7 SMART App Launch 2.2.0 pages, read 20 October 2026, EN-140). Scope levels and syntax: EN-138, EN-139.
- **Run.** Each cell run in the named sandbox; status code, context present, write-back visible recorded; on an EHR error the cell is stopped and recorded, not retried until it passes; a mocked token is not an EHR launch (old task DH-04.01.2.2.2; flags L1 to L6).
- **Failed cell report.** Each failed cell becomes a defect with the cell, the scope requested and the HTTP status or OperationOutcome, assigned by the person to the app or to the EHR configuration; the cell stays failed until a later run passes it; a cell is never reclassified as a known limitation without naming who accepted it (old task DH-04.01.2.2.3).

## 3. Mapping and terminology accuracy (old DH-04.01.3.2)

- **Frame.** Kahn et al. (eGEMs 2016, DOI 10.13063/2327-9214.1244) name three data quality categories, conformance, completeness and plausibility, and two assessment contexts, verification and validation (DA-94). Value conformance asks whether recorded elements agree with prespecified constraints, including allowed values and formats (DA-95, DA-96). A code map's target system and codes are a value conformance question; whether the target code is acceptable for the stated use is the clinician's validation judgment. Completeness concerns presence of attributes, not their values (DA-97). Use the framework as a vocabulary for the person's checks, not as a threshold.
- **Sample.** Size and draw method (random, or stratified by code system), the exact-match rate and unmatched rate as the person defines them, and the threshold the map must clear before production, all the person's (old task DH-04.01.3.2.1). Never sample only rows hand-checked the day before (flag R4).
- **Blinded review.** A clinician reviews a subset without seeing the mapper's label and says whether the target is acceptable for the stated use; disagreements are counted; the person who wrote the map is never the only reviewer (old task DH-04.01.3.2.2; flags R1 to R3).
- **Error classes.** Wrong target system, equivalence too strong, stale code, uncoded source, tied to the map version; the person names the class that blocks their threshold; a new map version that leaves the blocking class untouched is not published (old task DH-04.01.3.2.3).
- **Code system facts.** SNOMED CT member and non-member licensing (EN-171, EN-172); LOINC license [WF] (EN-173, EN-174); ICD-11 license (EN-175, EN-176); ICD-10-CM as the HIPAA diagnosis code set from 1 October 2015 (EN-177). Code system release versions current on a date are not in the sources `[GAP]`: the person supplies them.

## 4. Workflow fit and clinical adoption at the step (old DH-04.01.4.2)

- **Designed versus observed.** Observe the same step after release; mark each designed action done, skipped or replaced; quote the workaround when a person leaves the product to finish the step; never score adoption from analytics that do not see the workaround (old task DH-04.01.4.2.1).
- **Time and workarounds.** Time the step over a stated number of observations; count workarounds; separate a slow screen from a step the design got wrong; never report a mean time from a single observation (old task DH-04.01.4.2.2; flag W1).
- **The step that must change.** The person picks the one step whose workaround blocks the clinical purpose, the change, and the owner; polish items are not the blocking step (old task DH-04.01.4.2.3).
- **Context rows.** Certified decision support modules must let users give feedback on interventions and export it (45 CFR 170.315(b)(11), eCFR read 19 October 2026, UX-US-55): where the EHR is certified and the product's intervention is inside it, that export is a source of feedback data the person may use. HTI-5 proposes removing parts of (b)(11); proposed only (UX-US-60). ONC's 2025 SAFER Guides are eight self-assessment guides for EHR safety; the Organizational Responsibilities guide adds AI-enabled systems (CS72, CS73); the CMS hospital measure names "all nine" guides and ONC says the 2016 versions still apply for CMS measures (CS74). Running a SAFER self-assessment is the deploying organization's call.
- Organization-wide adoption tracking routes to `dh-go-to-market` adoption-monitoring; usability evidence to `dh-patient-and-user-experience` usability-monitoring.

## 5. Standards currency read (dated facts, rerun by the person)

The library holds no standards change log. This read compares the versions and dates the person's integration relies on with the rows as read on 19 and 20 October 2026. Anything published after the read date is `[GAP]` until a research pass reads it. Clocks are facts, never pressure.

| Fact | Date or status as read | Rows |
|---|---|---|
| US Core 3.1.1 and SMART 1.0.0 adoption for certification | Expired 1 January 2026 | EN-134, EN-137 |
| USCDI v1 adoption for certification | Expired 1 January 2026; v3 is the version in 45 CFR 170.213 | EN-148, DA-111 |
| Previously certified modules updated to USCDI v3 | By 31 December 2025 | EN-149 |
| USCDI v7 | Published 23 July 2026; not adopted by rule | DA-108, DA-111 |
| HTI-2 remaining proposals | Withdrawn effective 29 December 2025 | EN-150 |
| HTI-5 deregulatory proposal | Proposed Rule Stage on 20 October 2026; no final rule found | EN-151, UX-US-60 to UX-US-63 |
| CMS-0057-F process duties | From 1 January 2026 (or plan or rating year) | EN-157 |
| CMS-0057-F Provider Access, Payer-to-Payer and Prior Authorization APIs | Compliance in 2027 (1 January 2027 for MA, Medicaid and CHIP fee-for-service) | EN-153 to EN-155 |
| CMS drug prior authorization | Proposed 14 April 2026; comments closed 15 June 2026; proposed only | EN-159 |
| 170.215 amendments for prior authorization APIs | 4 August 2025 and 4 August 2026 | EN-146 |
| 42 CFR Part 2 compliance | 16 February 2026 | EN-115 |
| HIPAA Security Rule NPRM | Proposed 6 January 2025; Long-Term Actions, final action shown as 07/00/2027 | EN-106, EN-107 |
| EHDS exchange format implementing acts | Due by 26 March 2027 | EN-165, SP-073 |
| EHDS general application; EHR system rules | 26 March 2027; 26 March 2029 (first priority categories) and 26 March 2031 (second set) | SP-068, SP-070 |
| DiGA ePA specification updates | Implemented within six months of publication | PL89 |
| NHS DTAC refreshed form | Full transition by 6 April 2026 | CP-UK-04 |
| FHIR R6 | Draft ballots and a draft "Stable" snapshot dated 17 July 2026; not published | EN-131 |

## 6. Security and privacy signals seen while monitoring

A failed launch with an authorization error, an unexpected scope grant or a context leak is reported as the cell result only. Security analysis, threat models and vulnerability handling route to `dh-technology` security-and-privacy-operations-monitoring. Never describe attack steps; name a vulnerability only by its public identifier. HIPAA business associate breach notice runs no later than 60 calendar days after discovery (CP-US-49); whether an event is a breach is for the owner the person names for privacy or legal matters.

## Not in the sources (each stays `[GAP]`)

Any conformance, launch, latency, mapping, workaround or adoption benchmark or threshold; US Core element-level must-support lists; EHR vendor app-marketplace terms; code system release versions current on a date; HL7 ConceptMap equivalence codes; IHE or HL7 v2 test procedures; ONC certified product list (CHPL) entries; SAFER Guide item content beyond titles.
