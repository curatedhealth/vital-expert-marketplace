# Deployment prerequisites and sequencing rules

Interpretive reference for task A2. Rows: `CS` from `customer-success-research.md`, `CP-US`, `CP-EU`, `CP-UK` from `channels-partners-research.md`. These rows state what a law, regulator or official guide requires; they are not legal advice, and whether a given contract meets them is for the person's legal or privacy owner.

## 1. Sequencing rules this skill applies

| # | Rule | Basis |
|---|---|---|
| S1 | No personal data flows to the vendor (live interface tests, silent mode on local data, go-live) before the written agreement that market requires is signed. | US: CS96 (BAA documented in a written contract before a business associate handles PHI). EU: CS110, CP-EU-07 (Article 28 contract in writing). |
| S2 | No training before the day-one workflow is configured. | Register rule for the old Deployment sequence task (CF-12.02.02.1.1.2, "Do not schedule training before the day-one workflow is configured"). Supported by FDA's point that training knowledge decays over time (CS78). |
| S3 | User roles and access are set by job need before go-live. | CS104 (workforce classes and the PHI each needs), CS103 (minimum necessary). |
| S4 | Recurring data feeds have a standard protocol limiting data to what is reasonably necessary. | CS105. |
| S5 | Where local data can change the product's performance (for example AI), a silent-mode run on local data can precede use in care. | CS60 (NICE ESF standard 15). This is an option the site may choose, not a requirement. |
| S6 | Scale-up can be staged: pilots first, then system-wide. | CS47 (ERIC), CS5 (trialability includes reversing course). An option, not a rule. |
| S7 | The site's expected go-live date, or "unset". Never pick one. | Register method, old task CF-12.02.02.1.1.2. |

The register's own sequence method (old task) also asks for the steps (access, configure, train, go-live) with an owner and the step that cannot start until another finishes. `scripts/plan_sequence.py` checks S1, S2, unknown and circular dependencies, missing owners and dates.

## 2. United States: HIPAA business associate terms

A vendor that creates, receives, maintains or transmits PHI on behalf of a covered entity is a business associate, and so is its subcontractor doing the same (CP-US-44). Required contract content:

| Element | Row |
|---|---|
| Permitted and required uses and disclosures | CS97, CP-US-45 |
| Safeguards; Security Rule compliance for ePHI | CS98, CP-US-46 |
| Report non-permitted uses and breaches; report any security incident | CS98, CS101, CP-US-48 |
| Subcontractors agree to the same restrictions | CS99, CP-US-46 |
| Support access, amendment and accounting of disclosures | CS99 |
| Books open to HHS; return or destroy PHI at termination where feasible | CS100 |
| Covered entity may terminate for a material breach | CS100, CP-US-47 |
| Breach notice to the covered entity without unreasonable delay, at most 60 calendar days after discovery | CS102, CP-US-49 |

Minimum necessary applies to the vendor too, except disclosures to a provider for treatment (CS103).

The site's own duties (the plan should show them as the site's steps, owned by the site): train its workforce on PHI policies (CS82) and run a security awareness and training program (CS83).

Information blocking applies to a vendor only if it has at least one ONC-certified Health IT Module when it acts, or meets the network or exchange definition (CP-US-50, CP-US-51). Whether the vendor is an actor is for its legal owner `[GAP]` unless the person says.

## 3. European Union: GDPR Article 28 processor terms

| Element | Row |
|---|---|
| Controller uses only processors with sufficient guarantees | CS106, CP-EU-01 |
| No sub-processor without written authorization; under general authorization, notice of changes and a chance to object | CS107, CP-EU-02 |
| Contract sets subject matter, duration, nature and purpose, data types, data subject categories, controller rights | CS108, CP-EU-03 |
| Mandatory clauses (a) to (h): documented instructions, confidentiality, Article 32 security, sub-processor conditions, help with data subject rights and Articles 32 to 36, delete or return at the end, audits | CS109, CP-EU-04 |
| Processor tells the controller at once if an instruction infringes data protection law | CP-EU-05 |
| Contract in writing (electronic allowed) | CS110, CP-EU-07 |
| A processor that decides purposes and means itself (for example reusing hospital data to train the product) is a controller for that processing | CP-EU-07 |
| Processor notifies a breach without undue delay; no fixed hour limit for the processor | CS110, CP-EU-08 |
| The Commission's 2021 standard contractual clauses satisfy Article 28(3) and (4) | CP-EU-09 |

A shorter breach limit in a contract is the person's term, not the law's (research file, "Changes and conflicts").

## 4. England (NHS): DTAC and the clinical risk standards

- DTAC is used by commissioners and providers as part of assurance before buying and deploying (CS69 [WF]); buyers review the supplier's completed DTAC during procurement (CP-UK-01). Five areas: clinical safety, data protection, technical assurance, interoperability, usability and accessibility (CP-UK-02). NHS England's page calls DTAC best practice guidance, "not legally required" (CP-UK-02). The refreshed form applies, with full transition by 6 April 2026 (CP-UK-04).
- DTAC asks for proof of UKCA marking (or recognized equivalent) and the risk management system (CP-UK-03). Device status is the regulatory owner's fact.
- DCB0129 (manufacturer) and DCB0160 (deploying organization) are information standards under section 250 of the Health and Social Care Act 2012 (CP-UK-05; CS70 [WF]); NHS Digital states compliance is mandatory (CS71 [WF]).
- The deploying organization considers how the product will be deployed and used, makes sure the developer complies with DCB0129, and does its own clinical risk assessment (CP-UK-09); it should not adopt a product that does not meet the standards (CP-UK-10).
- The manufacturer presents its clinical risk findings to the adopter (CP-UK-06). An official service blog says the DCB0129 Clinical Safety Case Report is shared with the deploying organization and that a Clinical Safety Officer is required (CP-UK-11); this is a blog, not the standard.
- Not sourced: the DCB0160 clause content (hazard log, safety case structure, officer qualifications) `[GAP]`; both standards are under review with no date given (research file, "Changes and conflicts").

## 5. US hospitals: SAFER Guides context

ONC's 2025 SAFER Guides are eight self-assessment guides; the Organizational Responsibilities guide adds AI-enabled systems (CS72, CS73). Hospitals and CAHs in Medicare Promoting Interoperability have an annual SAFER Guides self-assessment measure; the regulation text still names "all nine" guides and ONC says the 2016 versions apply for the CMS measure (CS74). This is the hospital's duty; a deployment plan may show it as a site step where the person says it applies.

## 6. Training placement

| Fact | Row |
|---|---|
| Design changes beat labeling or training; training depends on memory | CS77 |
| Training knowledge decays over time | CS78 |
| "Additional training" alone is not accepted as a risk control in a premarket submission without data | CS79 |
| Training in a validation test should match real-world training; testing right after training is not valid. A customer training plan should match the training that was validated | CS80 |
| NICE: the company should describe its end-user training approach | CS65 |

Training content and delivery belong to the sibling competency Adoption & Change Enablement (DH-02.02.4.x); this skill only places training in the sequence.

## 7. Free items and payments around a deployment

Anything given free or below cost to a site or patients (devices, EHR software, cybersecurity technology, loaner phones) and any payment tied to referrals, volume or outcomes stops for the person's compliance or legal owner. Lay out the elements from the rows without saying an arrangement is protected:

- Safe harbor protection applies only when every condition is met (CP-US-07); the "one purpose" test (CP-US-08).
- Anything of value offered to a Medicare or state-program beneficiary that is likely to influence their choice of provider or supplier is subject to civil money penalties (beneficiary inducements CMP, CP-US-34).
- Devices loaned or given to patients: OIG treated even a restricted loaner phone as remuneration (CP-US-40); its favorable opinion relied on need-based eligibility, no advertising, return of the device and limited functions, and said a general-purpose device would likely change the outcome (AO 19-02, CP-US-39, CP-US-41). A tablet with general functions is closer to the unfavorable side of that line; the call is the compliance owner's.
- Donated EHR items: interoperable when provided, 15 percent recipient contribution, signed agreement (CP-US-30, CP-US-31).
- Donated cybersecurity technology: written signed description, not tied to referrals (CP-US-29).
- Patient engagement tools from a device maker: digital health technology only, in-kind, recommended by the patient's professional, annual cap $623 for 2026 (CP-US-25 to CP-US-28).
- Outcome-based payments to an agent: written measures, monitoring schedule, at least one year (CP-US-11 to CP-US-14). Outcome-linked customer payments belong to Market Access (outcomes-contract-monitoring).
