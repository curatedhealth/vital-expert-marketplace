# Segments and payer routes by market

Interpretive reference for tasks A1 and B1. Every rule cites a row in `channels-partners-launch-sources.md` (CP rows) or `promotion-and-claims-sources.md` (PC rows), read 19 October 2026, not owner-reviewed. Which schemes the library holds, and how fresh each copy is, comes from `list_commercial_dh_sources` or `market-access-dh.list_schemes` at run time, never from this file. Payer prices, codes, coverage and negotiation are the Market Access pack's subject: this file says only whether a route exists and who sits in which role.

## How a segment is written

A segment is one row with five cells, all in the person's words where they gave them:

| Cell | What it holds | Why |
|---|---|---|
| Buyer | Who signs the purchase or the prescription (practice, health system, sickness fund route, employer, consumer) | The motion targets the buyer |
| User | Who uses the product (patient group, clinician) | The positioning line speaks to the user's change |
| Payer | Who pays, and through which route | A segment with no payer route is self-pay or [GAP], and the plan must say so |
| Setting and job | Where it is used and the job the product is hired for | The register's method: a segment defined only by specialty is not a segment |
| Market | Country or region | Routes and rules differ per market |

User, buyer and payer are three roles; the connector keeps them apart and so does this skill. Where two roles are the same entity, say so; do not merge the cells.

## Which payer route exists, per market

### United States

| Route | Who is in which role | Entry conditions that shape the segment (rows) |
|---|---|---|
| Medicare digital mental health treatment codes (G0552 device supply; G0553, G0554 management) | Payer: Medicare. Buyer: the billing practitioner, who must bear the device cost. User: patient under a behavioral health plan of care | Effective 1 January 2025 (CP-US-57, CP-US-61). Device cleared by 510(k) or De Novo and classified at 21 CFR 882.5801, or from CY 2026 at 882.5803 for ADHD (CP-US-58, CP-US-62). Not payable if the practitioner bears no cost or the patient gets the device independently (CP-US-59). Furnished incident to the practitioner's services under a plan of care (CP-US-60). Use must match the FDA classification (CP-US-64). CMS declined further classifications for CY 2026 (CP-US-63). |
| Medicare remote physiologic and therapeutic monitoring codes | Payer: Medicare. Buyer and biller: practitioners eligible for E/M services. User: monitored patient | New 2 to 15 day and 10-minute codes for CY 2026 (CP-US-65); device codes not additive (CP-US-66); device must meet FDA's medical device definition, data uploaded automatically (CP-US-70); RPM needs an established patient, one practitioner per patient per 30 days, RPM and RTM not billed together (CP-US-69); pharmacists, dietitians and athletic trainers cannot bill (CP-US-68). A wellness product cannot point customers to these codes (CP-US-70). |
| Health system or practice purchase (no national code) | Buyer: the covered entity. Payer: the buyer's own budget | The vendor is a business associate when it handles PHI for the covered entity, and a BAA is needed (CP-US-44 to CP-US-49). Information blocking rules reach the vendor only if it has certified health IT modules (CP-US-50, CP-US-51). |
| Direct to consumer | Buyer, user and payer: the consumer | A consumer health app outside HIPAA falls under the FTC Health Breach Notification Rule (CP-US-54 to CP-US-56). Wellness marketing limits apply (PC-US-59 to PC-US-66). |
| Employer | Not sourced | The research found no ERISA or HHS provision stating what a digital health seller must do in the employer channel (CP file, "Not sourced"). Write the employer route as `[GAP]` for rules; the person's own facts can fill the cells. |
| App store | Not sourced | Platform policies are private terms and were not read (CP file, "Not sourced"). |

### Germany

| Route | Who is in which role | Entry conditions (rows) |
|---|---|---|
| DiGA listing | Payer: statutory sickness funds. Buyer: the treating physician or psychotherapist who prescribes, or the fund on approval. User: insured patient | Two routes to the patient: prescription, or fund approval with proof of the indication (CP-DE-01, CP-DE-02). The patient pays the difference for extra functions or a price above the amount (CP-DE-03). Not covered: products that control active therapeutic devices, DiGA for use with a specific aid or drug, everyday items (CP-DE-04). BfArM decides within three months of complete documents, extendable by up to three (CP-DE-12); a trial listing runs up to twelve months (CP-DE-13). Price is agreed with the GKV-Spitzenverband after the first year (CP-DE-08, CP-DE-09; Market Access subject). |

The library's DE_DIGA copy names listed peers per indication (search by ICD code, for example "F51"); it is a mirror of the directory, not BfArM's feed (see `tools.md`).

### England

| Route | Who is in which role | Entry conditions (rows) |
|---|---|---|
| NHS procurement | Buyer and payer: the NHS organization. User: clinicians and patients | Adopters review the supplier's DTAC during procurement; NHS England labels DTAC best practice, not legally required (CP-UK-01, CP-UK-02). Refreshed DTAC form, full transition by 6 April 2026 (CP-UK-04). DCB0129 and DCB0160 are information standards under the Health and Social Care Act 2012 section 250 (CP-UK-05); adopters should not adopt non-compliant technology (CP-UK-10). Frameworks usually last up to four years and are closed to new suppliers except a Dynamic Purchasing System (CP-UK-12). NHS England groups digital services into 6 pillars covering 32 framework agreements (CP-UK-14). |

Named framework lots and entry criteria were not read (CP file, "Not sourced"): `[GAP]`.

### European Union, any member state

Before placing a device on the market, manufacturers, authorized representatives and importers register in EUDAMED, and the manufacturer assigns a Basic UDI-DI (CP-EU-10, CP-EU-12). The Commission states the first four modules have been mandatory since 28 May 2026 (CP-EU-15). A hospital buyer acting as controller needs an Article 28 processor contract from the vendor (CP-EU-01 to CP-EU-07). These are launch conditions for any EU segment, not routes to payment.

### Other markets

For France (PECAN, LATM, LPPR), Belgium, Switzerland, Ireland, the Nordics, Spain and Australia, take what the library holds from `list_commercial_dh_sources` (scheme, kind, clock rule, listing count, posture) and point to the Market Access pack for what a route requires. A scheme with listing count 0 is `[GAP]`, never "no route".

## Reading a peer

| What the record shows | How to write it | Never |
|---|---|---|
| An authorization (510(k), De Novo, EUDAMED) | Product, pathway, the status as the record states it (for example "Substantially Equivalent"), decision date, source URL | "Approved" for an establishment registration (CP-US-74) or any status the record does not state; "market leader" |
| A listing (DiGA, PECAN, NICE) | Status, listed date, source URL, as of the retrieval date | "Proven", "reimbursed everywhere" |
| Studies, filings, recalls | Count and the dated rows | Outcomes, revenue or intent not stated in the row |
| No row | "Not in the library's copy" with the coverage line | "Not authorized", "not reimbursed" |
