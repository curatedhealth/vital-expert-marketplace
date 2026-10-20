# Partner terms: what must be true before a partner starts

Interpretive reference for A2. The term families come from the register method for DH-02.01.4.1 (data access, claim use, who speaks to the buyer); the required elements come from the CP rows in `channels-partners-launch-research.md` (read 19 October 2026). Commercial terms (price, margin, territory, exclusivity, term length) are the person's; the rows set no value for them.

Each term is marked **agreed**, **in draft** or **absent**, from what the person gives. The model never marks a term agreed on its own reading of a draft; it reports what the person states.

## T-D Data terms

| Term | When it applies | Required elements | Row |
|---|---|---|---|
| D1 Business associate chain | US: the partner creates, receives, maintains or transmits PHI for you or for a covered entity buyer | The partner is a subcontractor business associate; a BAA flows down the same restrictions | CP-US-44, CP-US-46 |
| D2 BAA contents | Same | Permitted and required uses; no other use or disclosure; safeguards and Security Rule compliance for ePHI; report non-permitted uses, security incidents and breaches; subcontractor flow-down; access, amendment and accounting support; books open to HHS; return or destroy at termination where feasible; termination for material breach | CP-US-45 to CP-US-48 |
| D3 Breach notice clock | Same | No later than 60 calendar days after discovery for a business associate; set the partner's notice to you short enough for your own clock (the length is the person's) | CP-US-49 |
| D4 Processor terms | EU: the partner processes personal data for you or for a controller buyer | Sufficient guarantees; prior written authorization for sub-processors and notice of changes; Article 28(3) contents (subject matter, duration, nature, purpose, data types, data subjects) and clauses (a) to (h); flag unlawful instructions; same obligations to sub-processors with you fully liable; in writing; Commission 2021 clauses available | CP-EU-01 to CP-EU-07, CP-EU-09 |
| D5 Processor breach notice | EU | Processor notifies the controller without undue delay; no hour limit is set for the processor in the row | CP-EU-08 |
| D6 Partner reuse of data | EU and US | A processor that decides purposes and means becomes a controller for that processing; a BAA must state permitted uses | CP-EU-07, CP-US-45 |
| D7 Consumer data outside HIPAA | US direct-to-consumer | FTC Health Breach Notification Rule; unauthorized disclosure is a breach; 60-day notice | CP-US-54 to CP-US-56 |
| D8 Information blocking | US: you or the partner hold an ONC-certified Health IT Module | Actor status; knowledge standard; fees exception conditions | CP-US-50 to CP-US-53 |

## T-C Claim use

| Term | Required elements | Row |
|---|---|---|
| C1 Approved claim list | The partner uses only claims on the list you give it. Who approves the list is the person's regulatory or legal owner; this skill does not clear claims (Commercial claims audit, DH-02.01.3.2, flags them). | Register method |
| C2 No approval implied by registration | Partner materials must not imply FDA approval from registration or a registration number | CP-US-74 |
| C3 Hold rule | Register method for this competency: a partner whose claim-use term is absent is held. Offer it as the default; the person confirms or replaces it. | Register method |

## T-B Who speaks to the buyer, and the handoff

| Term | Required elements | Row |
|---|---|---|
| B1 Buyer contact | Which party presents, quotes, contracts and supports the buyer, by segment | Register method |
| B2 Handoff event | The event that moves a buyer from partner to your team, the internal owner who receives it (the person names them), and what the partner still does after. Not a shared inbox. | Register method |
| B3 Germany | No arrangement about allocating or transmitting DiGA prescriptions | CP-DE-06 |

## T-M Compensation

Any compensation that varies with referrals, volume or outcomes, any free item to patients or providers, and any donated technology is a stop: lay out the elements from `fraud-and-abuse-stops.md` (E1 to E11) for the compliance or legal owner. A fixed fee is still checked against E1 (written, signed, at least 1 year, set in advance, fair market value, not tied to referrals) (CP-US-09, CP-US-10).

## T-S Disclosure

| Term | Required elements | Row |
|---|---|---|
| S1 Form 8-K Item 1.01 | If a party is an SEC reporting company and the agreement is a material definitive agreement outside the ordinary course (or a material amendment): disclose date, parties, other material relationships and material terms | CP-US-79, CP-US-80 |
| S2 Timing | Within four business days after the event, unless otherwise specified | CP-US-81 |
| S3 Exhibit 10 | An ordinary-course contract is still filed if the business substantially depends on it; specific terms may be redacted only if customarily treated as confidential and not material | CP-US-82, CP-US-83 |

Whether an agreement is material is the reporting company's call with its counsel. The skill only names the rule and that confidentiality clauses should expect it.

## T-L Launch prerequisites the partner depends on

| Term | Required elements | Row |
|---|---|---|
| L1 FDA registration and listing | Establishments that make devices, including spec developers, register and list; initial registration within 30 days of starting; new listing when introducing a non-exempt device with a premarket number not listed; foreign establishments list before import | CP-US-71 to CP-US-73 |
| L2 UDI | Labels bear a UDI; stand-alone software shows it in plain text at start-up or in a menu, with the version in the production identifier; GUDID data by the label date | CP-US-75 to CP-US-78 |
| L3 EUDAMED | Manufacturers, authorized representatives and importers register before placing on the market; Basic UDI-DI before placing on the market; first four modules mandatory from 28 May 2026 | CP-EU-10 to CP-EU-15 |
| L4 England | DTAC for procurement; DCB0129 evidence the deploying organization needs for DCB0160 | CP-UK-01 to CP-UK-10 |

## T-P Pharma partner pilot (a drug maker as partner)

Applies when a pharmaceutical manufacturer pays for, funds, co-promotes or pilots the product. The pilot design (sites, length, success measures, exit) is method, not a sourced rule, and stays the person's. The rows below set what the owner must see.

| Term | Required elements or exclusions | Row |
|---|---|---|
| P1 Who pays whom, on what basis | State the direction and basis of every payment. Outcomes-based payments made by pharmaceutical manufacturers, PBMs, lab companies, device or medical supply manufacturers and device distributors are excluded from the outcomes-based payments safe harbor: neither the drug maker nor the device maker can be the payer of a protected outcomes-based payment. A fixed fee for services is laid out against E1 | CP-US-13; CP-US-09, CP-US-10 |
| P2 Value-based arrangements | Pharmaceutical manufacturers and device makers cannot use the substantial-downside-risk or full-risk safe harbors; device makers enter care coordination only as limited technology participants | CP-US-23, CP-US-21 |
| P3 Anything free to patients funded by the drug maker | Beneficiary inducement analysis; drug makers are not "providers, practitioners, or suppliers" for the CMP unless they own billing entities; AO 19-02 (drug maker loaning limited-function phones) binds only its requestor; for device makers the rows are silent `[GAP]` | CP-US-34, CP-US-42, CP-US-39, CP-US-43 |
| P4 Germany | A DiGA maker may make no agreement with a drug maker that could restrict patient choice or therapeutic freedom; a DiGA meant for use with a specific drug is outside the DiGA route | CP-DE-07, CP-DE-04 |
| P5 Data and claims | Data terms (T-D) and claim use (T-C) apply as for any partner; joint drug and device promotion rules are not in the rows `[GAP]` | T-D, T-C rows |

## Not sourced

Exclusivity and competition-law limits, territory rules, liability caps, indemnities and insurance norms, reseller margin norms: write `[GAP]`; they are the person's and their legal owner's.
