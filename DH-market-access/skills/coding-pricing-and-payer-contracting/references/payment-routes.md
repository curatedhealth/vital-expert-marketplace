# Payment routes by market: which code or route could pay

Interpretive reference for task A1. Every rule cites a row id in `coding-pricing-sources.md` (US, DE, FR, EN, MO rows), `outcomes-contracting-sources.md` (cited by topic), or `france-pecan-lppr-latm.md` (cited by topic). Read on 19 October 2026; not owner-reviewed. Library coverage per scheme comes from `list_schemes` at run time, never from this file.

## How to read a route

A route is one of three things, and the map must say which:

| Kind | What is paid | Who bills | Example |
|---|---|---|---|
| Service code | A clinician's service that uses a device | The practitioner | US RPM, RTM, DMHT codes |
| Product listing | The product itself, per prescription or period | The manufacturer | German DiGA (PZN), French PECAN and LATM technical fee |
| Procurement | A contract with a buyer; no national code | Supplier to a trust or framework | England frameworks, MedTech Funding Mandate |

A code that exists is not a code the product can use. Each route has entry conditions; the map states them and marks unmet or unknown ones `[GAP]`.

## United States (Medicare Physician Fee Schedule and CMMI)

| Route | Codes | Entry conditions (row) | Library |
|---|---|---|---|
| Remote physiologic monitoring (RPM) | 99453 set-up; 99454 device supply 16 to 30 days; 99445 device supply 2 to 15 days (new 2026); 99457 first 20 minutes management; 99458 each further 20 minutes; 99470 first 10 minutes (new 2026) | Billed by practitioners eligible for E/M services (US15); device meets the FDA medical device definition (US15); one practitioner per patient per 30 days (US11, US15); established patient (US13); 2 to 15 and 16 to 30 day codes are alternatives, not additive (US4); not with RTM in the same period (US12) | US_CMS_RPM holds 99453, 99454, 99457, 99458 only (live call 19 October 2026); 99445 and 99470 are not stored |
| Remote therapeutic monitoring (RTM) | 98975 set-up; 98976, 98977, 98978 device supply 16 to 30 days; 98984, 98985, 98986 device supply 2 to 15 days (new 2026); 98980, 98981 management; 98979 first 10 minutes (new 2026) | Same biller and one-per-30-days rules (US11, US15); RTM does not require an established patient today; proposed for 2027 (US23, Changes and conflicts 2) | Not a library scheme; facts from the research file only |
| Digital mental health treatment (DMHT) | G0552 device supply and onboarding per course; G0553 first 20 minutes monthly management; G0554 each further 20 minutes (effective 1 January 2025, US16) | Device FDA 510(k) cleared or De Novo, classified at 21 CFR 882.5801, or from 1 January 2026 at 882.5803 for ADHD (US17, US18); the billing practitioner must incur the device cost (US17); supply incident to the practitioner's services under a behavioral health plan of care (US17); patient has a mental health diagnosis (US18) | US_CMS_DMHT holds G0552 to G0554 |
| CMMI ACCESS model | G0669 to G0675, monthly outcome-aligned payments (US35) | Voluntary, 10 years, began 5 July 2026 (US29); tracks eCKM, CKM, MSK, BH; heart failure, COPD, substance use disorder and tobacco cessation from 1 April 2027 (US30); payee is a Part B enrolled organization, not the device maker (outcomes file, "ACCESS: who is paid"); no other FFS billing for aligned beneficiaries (US36) | Not a library scheme |
| No FDA authorization | None | CMS did not finalize coding for digital tools without FDA authorization (US21) | |

Channel conflict to state whenever both apply: DMHT G0552/G0553 and RTM 98975 billed by another provider count as substitute spend against an ACCESS behavioral health participant (US34).

DMHT uptake: CMS states G0552 to G0554 claims volume has stayed low and that the cost-bearing condition may not fit direct-to-consumer models (US20). This is CMS's statement, not a forecast.

### Pending CY 2027 proposals: a dated risk, not law

The CY 2027 PFS proposed rule was published 16 July 2026 with comments due 14 September 2026; the final rule was not published at the research date (US22). If finalized, from 1 January 2027:

| Proposal | Row | Effect on a coding map |
|---|---|---|
| RTM only for established patients | US23 | New entry condition for RTM |
| RPM/RTM initiated in a face-to-face visit (in person or telehealth) | US24 | New entry condition |
| Time counts only by clinical staff employed by the practice; no third-party monitoring companies | US25 | Vendor-staffed models lose billable time |
| Device codes judged overvalued; crosswalk revaluation; practice-expense inputs removed from management codes | US26 | Lower amounts to be expected: device and set-up codes crosswalked to 99473/99474 inputs (RTM device codes to 93270 inputs), practice-expense inputs removed from 99470, 99457, 99458; no figure is stated |
| Comment solicitation: 17 RPM/RTM codes into 4 monthly G-codes, one naming "digital therapeutic intervention" | US27 | Code mapping could change entirely |
| "SaaS" renamed "Software as a Medical Service" | US28 | Terminology only, as proposed |

Write each as "proposed on 16 July 2026; final rule not published as of the read date". Never as current rule.

## Germany (DiGA)

| Route | Identifier | Entry conditions (row) | Library |
|---|---|---|---|
| DiGA listing, paid by statutory insurance | DiGA-ID and PZN per product (library `decision_reference`) | Listing in the BfArM directory; detail in the coverage pathway skill. The directory publishes prescription periods and the amount per period (DE20) | DE_DIGA, 82 listings, loaded 15 October 2026 |
| Physician fee for trial-phase DiGA | EBM 86700 (EUR 8.15) | For follow-up and evaluation of provisionally listed DiGA where BfArM defined physician tasks; once per DiGA per treatment case, at most twice per illness case; outside budget; not by video (DE18) | Not stored |
| Physician fee for permanent DiGA | Product-specific EBM codes (64 points each), for example 01471/30780 somnio, 01483/30782 Axia | EBM must be adapted within three months of listing where physician services are needed (DE17); first prescription is in base fees (DE19) | Not stored |

## France

| Route | What is paid | Entry conditions (source) | Library |
|---|---|---|---|
| PECAN, therapeutic DMN | Flat-fee compensation to the operator; maximum 780 EUR incl. tax per patient per year; G_NIUS schedule: 435 EUR initial quarter, then 38.3 EUR per month from month 4; no fee for health professionals | France file rows "PECAN payment: therapeutic DMN cap" and "schedule" (G_NIUS updated 12 December 2024; may be superseded, France file Not sourced 4) | FR_PECAN, 2 listings |
| PECAN, telemonitoring | Monthly per-patient technical amount "from 50 € TTC", degressive with active patients | France file row "PECAN payment: telemonitoring"; library row ODYSIGHT states "forfait exploitant 50 € TTC par patient par mois" | FR_PECAN |
| LATM (telemonitoring) | Operator fee to the health professional and technical fee to the DMN operator, billed by the operator | France file rows "LATM basics: two fees" and "billing"; amounts set by the arrêté of 16 May 2023, not read (France file Not sourced 5) | FR_LATM, 2 listings; CUREETY TECHCARE row states monthly fees from 48.43 to 73.33 EUR incl. tax by LPP code |
| LPP brand-name listing | Price and tariff set by CEPS after HAS evaluation | Up to 5 years renewable; a 180-day clock covers evaluation and price negotiation; interoperability and security certificate (FR4, FR6); price may exceed tariff (FR5) | FR_LPPR, none loaded |

## England

No national product code exists for digital therapies in the pages read (Not sourced 7). The routes are procurement and funding policy:

| Route | Condition (row) |
|---|---|
| Endorsed digital procurement frameworks | Trusts should buy all digital through endorsed frameworks; clinical software and apps is one pillar; non-use must be justified (EN4) |
| DTAC | Used to assess suppliers at procurement; any developer seeking NHS market access needs a DTAC evaluation (EN5) |
| MedTech Funding Mandate | NICE finds the technology cost saving within 3 years; budget impact not above GBP 20 million in any of the first 3 years; scope includes digital products (EN1); compliance through the NHS Standard Contract, paid from existing allocations (EN2); MTFM products sit on an exclusion list in the 2026/27 payment scheme (EN6) |
| Proposed rules-based pathway | 2024 engagement only; current status not established (EN3, Not sourced 8) |
| Payment currency precedent | Digital eye screening has its own NHSPS currency (EN7); no digital-therapy currency found (EN6) |

All England rows were read through a summarizer [WF]; re-check the quote before external use (Changes and conflicts 10).
