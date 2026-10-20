# Channel rules: what each route to the buyer requires

Interpretive reference for A1. Every rule cites its row in `channels-partners-launch-research.md` (CP prefix, read 19 October 2026). Rows are primary sources; none is legal advice. Where a route has no sourced rule, it says `[GAP]`.

Keep three roles apart in every channel: the **user** (patient or clinician who uses the product), the **buyer** (who signs and pays the seller) and the **payer** (who reimburses a claim, if anyone). A channel decision changes who the buyer is, and that changes which rules apply.

## United States

### Selling to a health system or practice (buyer = covered entity)

| Rule | What it means for the channel | Row |
|---|---|---|
| A vendor that creates, receives, maintains or transmits PHI for a covered entity is a business associate; so is its subcontractor. | A reseller or implementation partner that touches PHI is a subcontractor business associate. The BAA chain runs covered entity, you, partner. | CP-US-44 |
| The BAA must carry the required clauses (permitted uses, safeguards, breach reporting, flow-down, access and amendment, books open to HHS, return or destroy). | Terms go to A2. | CP-US-45 to CP-US-48 |
| A business associate notifies the covered entity of a breach no later than 60 calendar days after discovery. | The partner agreement needs a notice duty that lets you meet your own clock. | CP-US-49 |
| Information blocking applies to providers, developers of certified health IT, and HINs or HIEs. A vendor is a "developer" only if it has at least one ONC-certified Health IT Module. | Ask whether you or the partner hold certified modules; if neither does, that actor category does not apply (HIN or HIE could, if the definition is met). | CP-US-50, CP-US-51 |
| Statutory AKS exceptions include properly disclosed discounts and GPO fees under a written contract stating the fee. | A GPO or discount channel has its own conditions; route to compliance. | CP-US-05 |
| Paying a vendor to receive referrals failed the referral-service safe harbor in AO 26-15 because fees were not uniform, cost-based and volume-neutral. | A partner that sends you buyers or patients for a fee is a fraud-and-abuse stop. | CP-US-33, CP-US-43 |

### Practitioner-billed Medicare codes (buyer = billing practitioner)

Coverage, payment amounts and codes are Market Access's subject. These rows only say what the billing rules require of the channel.

| Rule | What it means for the channel | Row |
|---|---|---|
| G0552 is not payable if the billing practitioner incurs no cost for the device or the patient gets it independently. | A manufacturer-pays or direct-to-patient model cannot use G0552; the practitioner must be the buyer of the device. | CP-US-59 |
| G0552 needs a device cleared by 510(k) or granted De Novo under 21 CFR 882.5801, extended for CY 2026 to 882.5803 (ADHD digital therapy). | Channel through behavioral health practitioners only fits devices in those classifications. | CP-US-58, CP-US-62, CP-US-63 |
| The DMHT device is furnished incident to the practitioner's services under a behavioral health plan of care. | The practitioner, not a partner, orders it. | CP-US-60, CP-US-61 |
| RPM: one practitioner bills per patient per 30 days; RPM and RTM are not billed together; the device must meet FDA's device definition. | A partner network of practitioners must not double-bill one patient; a wellness product cannot point customers to these codes. | CP-US-69, CP-US-70 |

### Direct to consumer (buyer = the person)

| Rule | What it means for the channel | Row |
|---|---|---|
| The FTC Health Breach Notification Rule covers personal health record vendors that are not HIPAA covered entities or business associates. | A consumer channel outside HIPAA falls under the FTC rule. | CP-US-54 |
| A breach includes unauthorized disclosure, not only a hack; notice within 60 calendar days; FTC notice at the same time when 500 or more people are affected. | Data sharing with a marketing partner can itself be a breach. | CP-US-55, CP-US-56 |
| Saying or implying FDA registration means approval is misbranding. | Partner materials must not say "FDA registered" as an endorsement. | CP-US-74 |

### Free items to patients (any US channel)

Offering a Medicare or state-program beneficiary anything of value likely to influence the choice of provider, practitioner or supplier is subject to civil money penalties (CP-US-34, CP-US-35). Exceptions and safe harbors exist (CP-US-25 to CP-US-28, CP-US-36 to CP-US-42). Any free device, loaner phone or patient incentive is a fraud-and-abuse stop: see `fraud-and-abuse-stops.md`.

## Germany: DiGA as a channel

| Rule | What it means for the channel | Row |
|---|---|---|
| Insured patients get a listed DiGA on prescription by the treating physician or psychotherapist, or with sickness fund approval; fund approval needs proof of the indication. | Two routes to the patient; a channel plan names which it serves. | CP-DE-01, CP-DE-02 |
| Contract physicians and psychotherapists may not make deals with DiGA manufacturers about allocating or transmitting prescriptions. | No partner arrangement may steer or route prescriptions. | CP-DE-06 |
| DiGA manufacturers may not make agreements with drug or aid manufacturers that could restrict patient choice or physicians' therapeutic freedom. | A pharma co-promotion needs legal review before it is designed. | CP-DE-07 |
| DiGA meant for use with a specific aid or drug are not covered. | A drug-companion app tied to one drug falls outside the DiGA route. | CP-DE-04 |
| Delivery is electronic or on data carriers; public app stores only where that is not possible; needed hardware is usually lent. | The delivery partner and any hardware loan follow these terms. | CP-DE-05 |
| The patient pays the difference for extra functions or a price above the reimbursement amount. | A "premium" partner offer shifts cost to the patient. | CP-DE-03 |
| The GKV-Spitzenverband agrees the amount with each manufacturer, binding on all funds; self-pay and other European prices are negotiation inputs. | Prices a partner sets in other channels become inputs to the German negotiation (Market Access subject). | CP-DE-08, CP-DE-10 |

## England: NHS

| Rule | What it means for the channel | Row |
|---|---|---|
| NHS England guidance: technology used in the NHS needs to meet DTAC; adopters review the completed DTAC during procurement. DTAC is labeled best practice, not a legal requirement. | Any NHS partner or reseller will ask for your DTAC. | CP-UK-01, CP-UK-02 |
| DTAC asks for UKCA (or recognized equivalent) and the risk management system; the form was refreshed with full transition by 6 April 2026. | Use the refreshed form. | CP-UK-03, CP-UK-04 |
| DCB0129 binds the manufacturer and DCB0160 the deploying organization; information standards must be complied with unless waived. Adopters should not adopt non-compliant technology. | The deploying NHS organization does its own clinical risk work; the partner who implements must support it. | CP-UK-05 to CP-UK-10 |
| Sharing the DCB0129 Clinical Safety Case Report with the deployer and appointing a Clinical Safety Officer rest on an official service blog, not the standard. | Say so when you apply it. | CP-UK-11 |
| Frameworks usually last up to four years; new suppliers cannot join except a Dynamic Purchasing System. NHS England groups digital services into 6 pillars covering 32 framework agreements. | A reseller already on a framework can be the faster route; which framework fits is `[GAP]` (lot structure not sourced). | CP-UK-12 to CP-UK-14 |

## European Union

| Rule | What it means for the channel | Row |
|---|---|---|
| A controller (for example a hospital) may use only processors with sufficient guarantees; sub-processors need prior written authorization; the contract carries the Article 28(3) clauses. | A partner that processes patient data for you is your sub-processor; the hospital must authorize it. | CP-EU-01 to CP-EU-04 |
| A processor that decides purposes and means itself is treated as a controller for that processing. | A partner reusing hospital data for its own product becomes a controller. | CP-EU-07 |
| The Commission's 2021 clauses satisfy Article 28(3) and (4). | A ready template exists. | CP-EU-09 |
| Before placing a device on the market, manufacturers, authorized representatives and importers register in EUDAMED; the first four modules are mandatory from 28 May 2026. | An importer partner must itself be registered. Distributors are not named in the rows `[GAP]`. | CP-EU-10, CP-EU-13 to CP-EU-15 |

## Not sourced (write `[GAP]`)

Employer channel rules, app-store rules, Stark Law (downloaded, not used), inflation-adjusted CMP amounts, DiGA framework agreement thresholds, named NHS framework lots, EU or UK anti-bribery and competition rules on exclusivity, and any national anti-kickback law outside the United States. If the person's question turns on one of these, say it is not sourced and route to their legal owner.
