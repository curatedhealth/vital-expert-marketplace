# Interoperability and EHR integration rules, with rows

Interpretive reference for `interoperability-and-ehr-integration`. Every rule carries its row id; the row (URL, verbatim quote, read date) is in the copied research files in this folder: `engineering-interop-security-research.md` (EN), `data-and-ai-research.md` (DA), `channels-partners-launch-research.md` (CP), `ux-accessibility-usability-research.md` (UX), `customer-success-implementation-research.md` (CS), `strategy-and-portfolio-research.md` (SP) and `product-lifecycle-research.md` (PL). Rows were read 19 or 20 October 2026, as each row states. In answers, cite the source name and date in plain words with the row id after it (`gap-rules.md`, "How to cite").

The person decides interoperability scope, the implementation guide and version they build to, which exchanges are in or out, pass rules, go-live and owners. This file lays out what the sources state.

## 1. Version facts: "required for certification" is not "current publication"

US regulation pins older versions than HL7's current publications. Certification follows the regulation, not the latest HL7 release (EN research file, "Changes and conflicts"). Always state both columns and the date read.

| Standard | Required for ONC certification (45 CFR 170.215 or 170.213, eCFR read 20 October 2026) | Current HL7 or ONC publication (read 20 October 2026) | Rows |
|---|---|---|---|
| FHIR | Release 4.0.1 is the API base standard | R5 (5.0.0, 26 March 2023, trial use) is HL7's current published release; R4 (4.0.1, 30 October 2019) is superseded by R5; R6 exists only as draft ballots and a draft "Stable" snapshot dated 17 July 2026 | EN-129, EN-130, EN-131, EN-133 |
| US Core | 6.1.0, which enables USCDI v3; US Core 3.1.1 adoption expired 1 January 2026 | 9.0.0 (STU9, trial use, 31 May 2026), which enables USCDI v6 | EN-132, EN-134, EN-135 |
| SMART App Launch | 2.0.0 with the "Patient Access for Standalone Apps" and "Clinician Access for EHR Launch" capability sets and token introspection; SMART 1.0.0 expired 1 January 2026 | 2.2.0 (STU 2.2, 30 April 2024) | EN-136, EN-137 |
| Bulk Data | v1.0.0 (STU 1) with group-export | 3.0.0 (STU 3, 11 December 2025); 4.0.0 in ballot | EN-141 |
| USCDI | 45 CFR 170.213 lists v1 (adoption expired 1 January 2026) and v3 only; v4 is not adopted in the eCFR text as read [M]; previously certified modules had to update to v3 by 31 December 2025 | v5 published 16 July 2024; v6 published 24 July 2025; v7 published 23 July 2026 (31 new data elements). Publication does not by itself make a version a certification requirement. ONC applies enforcement discretion to certain v3 data elements | EN-148, EN-149, DA-107 to DA-112 |

Rules that follow:
- A product that must connect to certified EHR APIs builds to what the EHR is certified to (R4.0.1, US Core 6.1.0, SMART 2.0.0, Bulk Data 1.0.0, USCDI v3). Supporting newer versions is the person's choice; it is not what certification requires (EN-133, EN-134, EN-137, EN-141, EN-148).
- Never say "R5 is required", "USCDI v7 is required" or "US Core 9.0.0 is required for certification". Each is a current publication, not an adopted requirement (EN-129, EN-132, DA-108, DA-111).
- The HTI-2 proposals that had proposed a new USCDI baseline were withdrawn effective 29 December 2025 (EN-150). The HTI-5 deregulatory proposal of December 2025 (90 FR 60970) was at Proposed Rule Stage on 20 October 2026, with no final rule found (EN-151). Proposals are never requirements.
- HTI-1 final rule effective 8 February 2024 (EN-147).

## 2. SMART App Launch (what an EHR-launched app asks for)

- Scope syntax in SMART v2: suffixes are an ordered subset of `c r u d s` (create, read, update, delete, search). v1 `.read` maps to `.rs`; v1 `.write` maps to `.cud` (EN-138).
- Scope levels: `patient/` covers one patient in context; `user/` covers data available to the user; `system/` is for backend services with no user (EN-139).
- Launch context: `launch/patient` and `launch/encounter` request patient or encounter context; an EHR launch passes a `launch` parameter; a granted patient scope obliges the EHR to set patient context (EN-140).
- The old task rule "do not request `system/*.read` when the app launches as a user in a patient chart" follows from EN-139: system scopes are for backend services with no user. Which scopes each screen needs is the person's design; the model checks them against EN-138 and EN-139.

## 3. What certified EHR APIs must do (45 CFR 170.315(g)(10))

These are duties of the certified health IT module (the EHR), useful for what an app can expect. They are not duties of a third-party app.
- Answer single-patient and group requests for all USCDI data per US Core "must support" (EN-142).
- Refresh tokens for confidential apps valid at least three months (EN-143).
- Revoke an app's access at the patient's direction within one hour (EN-144).
- API documentation at a publicly accessible hyperlink without preconditions (EN-145).
- New provider prior-authorization API criteria (g)(31) to (g)(33) use the Da Vinci CRD, DTR and PAS guides; 170.215 amended on 4 August 2025 and 4 August 2026 (EN-146).

## 4. Payer APIs (CMS-0057-F) and prior authorization

- CMS Interoperability and Prior Authorization final rule, published 8 February 2024, effective 8 April 2024 (EN-152).
- Provider Access API on FHIR R4.0.1 with claims, USCDI data and prior authorizations, compliance in 2027 (1 January 2027 for MA, Medicaid and CHIP fee-for-service; plan or rating years for others) (EN-153). Payer-to-Payer API beginning in 2027 (EN-154). Prior Authorization API with 2027 compliance dates (EN-155).
- Decision timeframes: 72 hours expedited and 7 calendar days standard, excluding drugs (EN-156); denial reasons, timeframes and public metrics from 1 January 2026 (or plan or rating year) (EN-157).
- API content is tied to 45 CFR 170.213, so it moves when ONC adopts new USCDI versions (EN-158).
- Drug prior authorization: proposed 14 April 2026 (91 FR 19890), comments closed 15 June 2026; proposed only (EN-159).
- Whether a product is reimbursed or covered is not this skill's subject: `dh-access-and-value` coverage-pathway-and-access-strategy.

## 5. TEFCA (network-to-network exchange)

- Final rule published 16 December 2024, effective 15 January 2025 (EN-160). 45 CFR part 172 ensures network-to-network exchange and a voluntary QHIN attestation process (EN-161). The RCE signs the Common Agreement with QHINs and administers it (EN-162). Each transaction needs an authorized Exchange Purpose, identified by an XP code (EN-163).
- Not sourced: the number of designated QHINs, the Common Agreement version and SOP content `[GAP]` (EN research file, "Not sourced").

## 6. Information blocking (45 CFR part 171)

- Applies to health care providers, developers of certified health IT, and HINs or HIEs, from 5 April 2021 (CP-US-50).
- A vendor is a "developer of certified health IT" only if it has at least one certified Health IT Module when it engages in the practice; a vendor without certified modules is not in that category, though it could be an HIN or HIE if it meets that definition (CP-US-51).
- Knowledge standard for developers, networks and exchanges: knows or should know the practice is likely to interfere (CP-US-52).
- Fees exception: fees, including a reasonable profit, are not information blocking when the exception's conditions are met (CP-US-53).
- Whether the person's company is an actor, and whether a practice meets an exception, is for the owner the person names for legal matters, or owner not named. The model lays out the rows.

## 7. Privacy rules that travel with the data flow

Lay these out when an exchange moves health data; the privacy design and security program belong to `dh-technology` cybersecurity-and-privacy-by-design.
- HIPAA business associates: a vendor that creates, receives, maintains or transmits PHI for a covered entity is a business associate (CP-US-44); BAA contents (CP-US-45 to CP-US-48); breach notice to the covered entity no later than 60 calendar days after discovery (CP-US-49).
- HIPAA Security Rule in force: standards in 164.308 to 164.316 (EN-097); transmission encryption is addressable (EN-104). The 2025 Security Rule NPRM (6 January 2025) is a proposal; the 2026 Unified Agenda lists it under Long-Term Actions with final action shown as 07/00/2027 (EN-106, EN-107). Never present the NPRM as a requirement.
- 42 CFR Part 2 (substance use disorder records): final rule effective 16 April 2024, compliance by 16 February 2026 (EN-114, EN-115); single consent for future treatment, payment and health care operations uses (EN-116); counseling notes need their own consent (EN-117).
- Consumer apps outside HIPAA: FTC Health Breach Notification Rule scope (CP-US-54); Washington My Health My Data Act: consent standard and separate sharing consent (EN-122, EN-123), HIPAA PHI exempt (EN-128).
- EU: GDPR Article 25 by design and by default (EN-108, EN-109), Article 32 security measures (EN-110), Article 35 DPIA (EN-111, EN-112).

## 8. European Health Data Space (Regulation (EU) 2025/327)

- Applies from 26 March 2027; entry into force 25 March 2025 (SP-068, SP-069).
- Priority categories: patient summaries, ePrescriptions, eDispensations, imaging studies and reports, test results, discharge reports (EN-164). Primary-use and EHR system rules apply from 26 March 2029 for the first set (patient summaries, ePrescriptions, eDispensations) and 26 March 2031 for the second (images, lab results, discharge reports) (SP-070).
- The Commission must set the European EHR exchange format by implementing acts by 26 March 2027 (EN-165, SP-073).
- An "EHR system" is software that stores, intermediates, exports, imports, converts, edits or views priority data (EN-166); EHR systems must include a European interoperability component and a European logging component; general-purpose software is excluded (EN-167); conformity is a mandatory self-assessment with an EU declaration of conformity (EN-170).
- Medical device makers that claim interoperability with the harmonized components must prove compliance with Annex II Section 2 (EN-168). Wellness apps claiming EHR interoperability must carry a manufacturer-issued label (EN-169).
- Not sourced: Annex II text and the implementing acts' status `[GAP]`.

## 9. Germany and the UK

- DiGA: data transfer to the patient's electronic health record (ePA) with consent via the gematik interface, and updated ePA specifications implemented within six months of publication (DiGAV, read 20 October 2026, PL89).
- UK: DTAC has five core areas including interoperability; NHS England labels DTAC "best practice guidance", not a legal requirement; the refreshed form took full effect by 6 April 2026 (CP-UK-01, CP-UK-02, CP-UK-04). DCB0129 (manufacturer) and DCB0160 (deploying organization) are information standards the guidance pages label "legally required" (CP-UK-05 to CP-UK-10). The claim that a Clinical Safety Officer and a shared safety case report are required rests on a blog, not the standard (CP-UK-11): say so.

## 10. Decision support inside the EHR

- Certified decision support interventions (45 CFR 170.315(b)(11)) must occur while the user interacts with the technology (UX-US-54), capture user feedback (UX-US-55), and for predictive DSIs disclose source attributes including intended use and cautioned uses (UX-US-56 to UX-US-59). HTI-5 proposes removing parts of these; proposed only, the eCFR text still carried them on 19 October 2026 (UX-US-60).
- These are certification duties of the EHR module. Whether a CDS function is a device, and the FDA CDS guidance, route to `dh-regulatory-and-quality` regulatory-pathway-and-classification; the product's CDS design to `dh-technology` analytics-products-and-decision-support.

## 11. Terminology: code systems, licensing and the US code set

- SNOMED CT: no charge in SNOMED International member countries (register with the national release center); non-member use needs an annual Affiliate License via MLDS (EN-171, EN-172).
- LOINC: free for commercial and non-commercial use; the notice must appear on every printed copy of the LOINC Table (EN-173, EN-174, both [WF]).
- ICD-11: CC BY-ND 3.0 IGO; incorporation in software is not an adaptation if codes, URIs and attribution are kept (EN-175, EN-176).
- ICD-10-CM is the HIPAA diagnosis code set from 1 October 2015; ICD-10-PCS for inpatient procedures (EN-177). The current CDC fiscal-year version is not sourced `[GAP]`.
- RxNorm: no row in the sources `[GAP]`; the person supplies the version and terms they use.
- Equivalence labels in the old task (equal, wider, narrower, unmatched) are the old task's working labels, not an HL7 value set; the HL7 ConceptMap equivalence value set is not in the sources `[GAP]`.

## 12. Downstream data models

- USCDI defines data classes and elements for nationwide exchange (DA-107).
- OMOP CDM is an open community data standard (OHDSI documentation, [SPEC]); current version v5.5; vocabularies are central; OBSERVATION_PERIOD defines spans where absence means non-occurrence; person linkage must happen before loading (DA-102 to DA-106). Analytic data preparation routes to `dh-technology` data-preparation-and-analytics-methods.
- FAIR is a guide, not a standard (Wilkinson et al. 2016, DOI 10.1038/sdata.2016.18, DA-99 to DA-101).

## 13. EHR safety self-assessment

- ONC 2025 SAFER Guides: eight self-assessment guides in three groups; the Organizational Responsibilities guide adds AI-enabled systems (CS72, CS73). The CMS hospital measure text names "all nine" guides and ONC says the 2016 versions still apply for CMS measures (CS74). Who runs a SAFER self-assessment is the deploying organization's call.

## 14. Security of the interface

- FDA's premarket cybersecurity guidance (3 February 2026) asks that the threat model capture risks from interoperation among others (EN-050) and assume an adversary controls the network (EN-051). The interface's security design, threat model and testing route to `dh-technology` cybersecurity-and-privacy-by-design. This skill never describes attack steps.

## Not in the sources (each stays `[GAP]`)

HL7 v2 messaging and C-CDA rules; IHE profiles; US Core element-level must-support lists (the person supplies the StructureDefinitions or check sheet they build to); EHR vendor app-marketplace or app-registration terms; FDA guidance on interoperable medical devices; RxNorm licensing; HL7 ConceptMap equivalence codes; TEFCA operational facts; EHDS Annex II and implementing-act status; NHS DSPT content; any adoption, latency, conformance-rate or mapping-accuracy benchmark or threshold.
