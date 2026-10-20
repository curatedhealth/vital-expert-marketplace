# Security and privacy requirements by design

What the sources require when a digital health product is designed: which regimes may apply, what each asks for, and what stays the person's call. Every rule carries its row. Rows live in the copied research files: EN in `engineering-interop-security-research.md`, CP in `channels-partners-research.md`, CS in `customer-success-research.md`, DL in `diligence-research.md`, PL in `product-lifecycle-research.md`. All rows were read on 19 or 20 October 2026. [WF] rows were read through a summarizing fetch: say so when a rule rests on one. No [PAPER] rows are used in this skill.

Cite only the rows for the market in the request. Which regime applies to the person's product, which legal basis fits a data class and whether a product is a device are calls for the owners the person names; this file lays out the facts they decide on.

## 1. Which regimes may apply: the fact that decides each

| Fact about the product | Regime the rows name | What it means here | Rows |
|---|---|---|---|
| A US vendor creates, receives, maintains or transmits PHI for a covered entity | HIPAA business associate | Security Rule standards apply to the vendor; a BAA is needed before PHI flows | CP-US-44; CS96 to CS101 |
| PHI sits with a cloud provider, even encrypted and without the key | HIPAA business associate (the cloud provider) | The cloud provider is a business associate and must meet the Security Rule; offshore storage is permitted with a BAA, and location is a risk the risk analysis must address | EN-032 to EN-034 [WF] |
| A US consumer health app outside HIPAA | FTC Health Breach Notification Rule | A breach includes unauthorized disclosure, not only a hack; notice within 60 calendar days | CP-US-54 to CP-US-56 |
| Consumer health data of Washington consumers, outside HIPAA PHI | Washington My Health My Data Act (RCW 19.373) | Opt-in consent; separate sharing consent; signed authorization for sale; deletion within 45 days; geofencing ban; HIPAA PHI exempt | EN-121 to EN-128 |
| Records from a federally assisted SUD program (Part 2 program) | 42 CFR Part 2 (final rule 16 February 2024; compliance by 16 February 2026) | Single consent for treatment, payment and operations allowed; counseling notes need their own consent; HIPAA breach rules apply | EN-114 to EN-120 |
| Personal data concerning health of people in the EU | GDPR Articles 9, 25, 32, 35, 36; Article 28 for processors | Article 9(2) ground per purpose; by design and by default; security of processing; DPIA where high risk or large-scale health data | DL-099 to DL-106 (DL-101 inference in part); EN-108 to EN-113; CS106 to CS110; CP-EU-01 to CP-EU-08 |
| Device with sponsor-validated software, able to connect to the internet, with characteristics vulnerable to cyber threats (all three) | FD&C Act section 524B ("cyber device") | Postmarket vulnerability plan with coordinated disclosure, patch processes, SBOM, in 510(k), De Novo, PMA, PDP and HDE submissions; effective 90 days after 29 December 2022 (29 March 2023, computed) | EN-041 to EN-046 |
| Device with software, firmware or programmable logic, connected or not | FDA premarket cybersecurity guidance of 3 February 2026 (final) | Threat model, SBOM, known vulnerabilities, architecture views, control categories, testing; any ability to connect counts | EN-047 to EN-061 |
| Device software placed on the EU market | MDR Annex I 17.4 and 18.8; MDCG 2019-16 rev.1 (July 2020) | Minimum IT security requirements stated by the manufacturer; protection against unauthorized access; shared responsibility; operating-environment requirements | EN-069 to EN-074 |
| A product with digital elements in the EU that is not an MDR or IVDR device | Cyber Resilience Act, Regulation (EU) 2024/2847 | MDR and IVDR devices are excluded; health-monitoring wearables outside the MDR are Annex III Class I important products; reporting under Article 14 since 11 September 2026; main duties from 11 December 2027 | EN-086 to EN-092 |
| An EU medical device or IVD manufacturer, or a health entity in NIS2 Annex I | NIS2 Directive (EU) 2022/2555 | Annex II covers device and IVD manufacturers; Annex I covers health entities and makers of devices on the public health emergency critical list. Size thresholds and national transposition decide scope and were not read `[GAP]` | EN-093 to EN-096 |
| A DiGA in Germany | DiGAV | BSI data security requirements from 1 January 2025, proven by a BSI certificate; BfArM data protection test criteria from 1 August 2024 | PL87 |
| Deployment in the NHS in England | DTAC; DCB0129 (manufacturer) and DCB0160 (deploying organization) | DTAC areas include data protection and technical assurance; DTAC is labeled best practice, not a legal requirement; DCB0129 and DCB0160 are information standards the guidance labels legally required | CP-UK-01 to CP-UK-11; CS68 to CS71 [WF for CS69 to CS71] |
| A US SEC registrant | Form 8-K Item 1.05; 10-K Item 1C | A material cybersecurity incident is reported within four business days after the registrant determines materiality | DL-024, DL-027 |

The model may list which rows each fact points to. Whether the product is a cyber device, a device at all, an MDR device, a business associate, or in NIS2 scope is not the model's call: the regulatory or legal owner the person names decides, and device questions route to `dh-regulatory-and-quality` regulatory-pathway-and-classification.

## 2. Data classes and legal basis (old task DH-04.02.1.1.1)

- Separate the classes the person holds: PHI or health data, device identifiers, logs, account data (old method). Each class gets its own region and basis; one basis is not applied to every class (old "Do not").
- EU: health data is defined in GDPR Article 4(15) (DL-099); its processing is prohibited unless an Article 9(2) ground applies (DL-101, inference in part). Grounds in the rows: explicit consent for specified purposes (DL-102), care under law or a contract with a health professional (DL-103), public health including quality and safety of medical devices (DL-104). Member states may add conditions (DL-105). Any other Article 9(2) ground is not in the rows `[GAP]`.
- US: the HIPAA role (covered entity, business associate, neither) is the fact that decides which rules apply (CP-US-44). Outside HIPAA, the FTC rule (CP-US-54) and state law such as MHMDA (EN-121) may apply.
- The basis per class is the person's or their legal owner's; the model writes "basis not given `[GAP]`" where none is supplied.

## 3. Controls per data class (old task DH-04.02.1.1.2)

- Name the mechanism, not the law (old "Do not": "Do not cite HIPAA or GDPR as the control. Cite the mechanism.").
- HIPAA Security Rule as in force: standards in 164.308, 164.310, 164.312, 164.314, 164.316 (EN-097). Required: risk analysis (EN-099), risk management (EN-100), activity review (EN-101), backup, disaster recovery and emergency mode plans (EN-102), unique user identification and emergency access (EN-103), documentation kept six years (EN-105). Addressable: automatic logoff and encryption at rest (EN-103), encryption in transit (EN-104). Addressable means implement if reasonable and appropriate, or document why not and adopt an equivalent where reasonable (EN-098).
- The HIPAA Security Rule NPRM of 6 January 2025 is a proposal, not a requirement. The 2026 Unified Agenda lists it under Long-Term Actions with final action shown as 07/00/2027 (EN-106, EN-107). Its specific proposals were not read `[GAP]`; never describe them as rules.
- Minimum necessary and role-based access (CS103 to CS105).
- GDPR: by design and by default (EN-108, EN-109); security of processing including pseudonymization, encryption, restore and regular testing (EN-110).
- Mark a control that is only intended as "not in force" (old method). Each control row names the artifact that shows it in force.

## 4. Consent design (old tasks DH-04.02.4.1.1 to .3)

- Write each purpose in the product's own words, tie it to a data class, and mark a purpose with no screen or form yet (old method). Research, care and marketing are not collapsed into one purpose (old "Do not").
- Consent standards in the rows: GDPR explicit consent for specified purposes (DL-102); MHMDA consent is a clear affirmative, opt-in, specific, informed act, and sharing consent is separate from collection consent (EN-122, EN-123); sale needs a signed authorization that expires one year after signature (EN-125); Part 2 allows one consent for treatment, payment and health care operations, and counseling notes need their own consent (EN-116, EN-117).
- Capture: store who, when, which purpose and which version of the text; state how a withdrawal is stored and which processing it stops; a checkbox defaulted to on is not a captured consent (old method and "Do not").
- The GDPR right to withdraw consent at any time (Article 7) is not in the rows `[GAP]`; MHMDA deletion must flow to processors and third parties, within 45 days (EN-126).
- Data minimization: a field collected and not read by the stated purpose is removed or tied to the purpose that needs it (old method; GDPR by default, EN-109). Record the product version that carries the change.

## 5. Reviewer document set (old task DH-04.02.1.1.3)

Index what exists and list each missing document as `[GAP]`; never draft a missing policy as a summary (old "Do not"). Check that each document names the product version it describes.

| Document | Asked for by | Rows |
|---|---|---|
| Data flow, control matrix, retention schedule | Old method | old task |
| Security risk analysis (HIPAA) | Security Rule | EN-099 |
| BAA with each customer and each subcontractor | HIPAA | CS96 to CS101 |
| Processor contract with Article 28(3) clauses | GDPR | CS106 to CS110; CP-EU-03, CP-EU-04 |
| DPIA | GDPR Article 35 | EN-111, EN-112; DL-106 |
| Threat model | FDA premarket guidance | EN-050, EN-051 |
| SBOM (machine-readable) with level of support and end-of-support date per component | FDA premarket guidance; 524B(b)(3) | EN-045, EN-053, EN-054 |
| Known vulnerabilities list, including KEV entries, and how they were found | FDA premarket guidance | EN-055 |
| Architecture views: Global System, Multi-Patient Harm, Updateability/Patchability, Security Use Case | FDA premarket guidance | EN-056 |
| Security controls by the eight categories | FDA premarket guidance | EN-057 |
| Security testing and the penetration test report | FDA premarket guidance | EN-058, EN-059 |
| Postmarket vulnerability plan with coordinated disclosure | 524B(b)(1) | EN-043, EN-061 |
| OTS software documentation | FDA OTS guidance, 11 August 2023 | EN-023 to EN-027 |
| Minimum IT security requirements for users | MDR Annex I 17.4; MDCG 2019-16 | EN-069, EN-074 |
| BSI certificate (DiGA) | DiGAV | PL87 |
| DTAC submission; DCB0129 clinical safety case report | NHS England | CP-UK-01 to CP-UK-07, CP-UK-11 (blog, not the standard) |

## 6. Threat model and security architecture (old tasks DH-04.02.2.1.1 to .3)

- Boundaries: name the components (app, EHR, device, identity provider, data store), mark each hop that crosses a network, a tenant or a privilege level, and label what is inside the product boundary and what is a third party; never one box labeled cloud (old method).
- Threat sources FDA names: supply chain, manufacturing, deployment, interoperation with other devices, maintenance and update, decommissioning (EN-050). Assume an adversary controls the network and can alter, drop and replay packets; the method chosen needs a rationale (EN-051).
- Write each threat as actor, hop and asset; a threat with no asset is dropped (old method). A generic list not tied to a hop is not a threat model (old "Do not"). If the person's team uses a named threat method, keep its labels as theirs; no threat taxonomy is sourced here beyond EN-050 and EN-051.
- Controls by the eight FDA categories: authentication; authorization; cryptography; code, data and execution integrity; confidentiality; event detection and logging; resiliency and recovery; updatability and patchability (EN-057).
- Each threat ends with a control or an explicit acceptance by a named person with the condition that would reopen it; no threat is left without one, and no risk is accepted anonymously (old method).
- Risk is typically a function of adverse impact and likelihood (NIST SP 800-30 Rev. 1, September 2012, EN-079); the scale, the scores and the acceptance criteria are the person's.
- KEV vulnerabilities should be designed out of the device (EN-052).
- Frameworks to map to if the person asks: NIST CSF 2.0 functions (26 February 2024, EN-075, EN-076), NIST SSDF 1.1 practice groups (February 2022, EN-036 to EN-040). Recognized standards: AAMI TIR57 (EN-082), IEC 81001-5-1 (EN-084), AAMI TIR97 (EN-085), known here only from FDA recognition abstracts; conformance may not satisfy all 524B requirements (EN-083).
- Changes that may impact cybersecurity and bring 524B documentation: new authentication or encryption algorithms, new connectivity, a changed update mechanism (EN-060). Whether a change needs a new submission routes to `dh-regulatory-and-quality` regulatory-submission-and-dossier.

## 7. Vulnerability response and incident record (old tasks DH-04.02.3.1.1 to .3)

- Intake: source (scanner, researcher, vendor advisory), identifier, component and version in this product, and whether the vulnerable path is reachable in the deployed configuration; a vulnerability is never filed against a component the product does not ship (old method).
- Response: patch, mitigate or accept, one of the three; a patch names the version with the fix; an acceptance names the acceptor and the expiry date; a reachable item is never left "under review" with no action (old method).
- US device law: 524B(b)(2) asks for updates and patches for known unacceptable vulnerabilities on a justified regular cycle, and out of cycle as soon as possible for critical vulnerabilities that could cause uncontrolled risks (EN-044). The 2016 postmarket guidance (EN-062) defines controlled and uncontrolled risk (EN-063, EN-064). Routine patches for controlled risk generally need no 21 CFR 806 report (EN-065). For uncontrolled risk, FDA's 806 enforcement policy asks for customer communication within 30 days and a validated, distributed fix within 60 days (EN-066, EN-067). These 30 and 60 days are an FDA enforcement policy from 2016, not statutory deadlines; 524B says "reasonable time" and "as soon as possible out of cycle" (research file, "Changes and conflicts"). Whether a risk is controlled or uncontrolled is the person's call; whether anything is reportable routes to `dh-regulatory-and-quality` audit-capa-and-complaints.
- CISA KEV: an input to prioritization; an entry needs a CVE ID, reliable evidence of active exploitation and a clear remediation (EN-080, EN-081 [WF]).
- Incident record, kept apart from the vulnerability: what was observed (time, system, indicator), which data classes were on that system, who was told and when; an incident is never described as a routine patch (old method).
- Notification clocks a legal owner weighs, each as a fact, never as pressure: HIPAA individual notice within 60 calendar days of discovery (DL-089), discovery rule (DL-090), media and HHS notices (DL-091, DL-092), presumption and four-factor assessment (DL-086, DL-087); business associate to covered entity within 60 days (CS102); BAA security incident reporting term (CS101); GDPR processor to controller without undue delay, no hour limit for the processor (CP-EU-08, CS110); FTC HBNR 60 days (CP-US-56); Part 2 programs follow HIPAA breach rules (EN-118); CRA early warning 24 hours and notification 72 hours for products in its scope (EN-089); NIS2 24 hours, 72 hours, final report one month after notification for entities in scope (EN-096); SEC 8-K Item 1.05 four business days after materiality is determined (DL-024). The GDPR controller notice to the supervisory authority (Article 33(1)) is not in the rows `[GAP]`.

## 8. Versions and status (dated facts)

| Instrument | Version or status as read | Row |
|---|---|---|
| FDA premarket cybersecurity guidance | Final, issued 3 February 2026, supersedes 27 June 2025 | EN-047 |
| FDA postmarket cybersecurity guidance | Final, 28 December 2016 (predates 524B) | EN-062 |
| FD&C Act 524B | Effective 90 days after 29 December 2022 | EN-046 |
| HIPAA Security Rule | In force with addressable specifications | EN-097, EN-098 |
| HIPAA Security Rule NPRM | Proposed 6 January 2025; not final; Long-Term Actions, final action shown 07/00/2027 | EN-106, EN-107 |
| 42 CFR Part 2 final rule | Effective 16 April 2024; compliance by 16 February 2026 | EN-114, EN-115 |
| MDCG 2019-16 | rev.1, July 2020, still the listed MDCG cybersecurity guidance | EN-071 |
| NIST CSF | 2.0, 26 February 2024 | EN-075 |
| NIST SSDF | SP 800-218 version 1.1, February 2022 | EN-036 |
| Cyber Resilience Act | Article 14 from 11 September 2026; Chapter IV from 11 June 2026; applies from 11 December 2027 | EN-087 |
| NIS2 | Applied by member states from 18 October 2024 | EN-095 |
| FDA OTS guidance | 11 August 2023 | EN-023 |

## 9. Not in the sources

IEC 62304 software safety classes and their definitions; AAMI TIR57, TIR97 and IEC 81001-5-1 content beyond the FDA recognition abstracts; NTIA SBOM minimum elements; CISA SBOM updates; the specific proposals in the HIPAA Security Rule NPRM; CVSS, EPSS or any severity scale; any threat taxonomy beyond EN-050 and EN-051; GDPR Articles 7 and 33(1); MHRA and Health Canada cybersecurity guidance; NHS DSPT content; NIS2 size thresholds and national transposition; patch windows, risk acceptance criteria and support horizons (the person's). Each is `[GAP]`: say so and ask the person, or the owner they name, for it.
