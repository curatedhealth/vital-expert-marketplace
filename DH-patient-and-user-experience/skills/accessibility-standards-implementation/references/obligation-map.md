# Obligation map: who you are and where you sell decides which rules apply

Interpretive reference for this skill. Every rule cites its row in `ux-accessibility-research.md` (UX- rows) or `wcag-criteria-additions.md` (WX rows). Rows were read on 19 October 2026. Which instruments bind a given organization is a legal question for the person's own legal or compliance owner; this file lays out what each instrument says so the person can answer it. It never declares that anyone conforms.

## The questions to ask first

The answer depends on facts only the person has. Ask these, in this order, and take the answers in their words. Do not infer a role from the product.

| # | Question | Why it matters |
|---|---|---|
| Q1 | Are you a US federal agency, or do you build ICT that a federal agency will develop, procure, maintain or use? | Section 508 standards (UX-US-01 to UX-US-06) |
| Q2 | Are you a US state or local government entity, or do you provide web content or a mobile app to one "through contractual, licensing, or other arrangements"? If an entity: total population 50,000 or more, or less, or a special district? | ADA Title II, 28 CFR 35 subpart H (UX-US-07 to UX-US-14) |
| Q3 | Do you, or the customer you build for, receive HHS federal financial assistance? If so, 15 or more employees, or fewer? | HHS Section 504, 45 CFR 84 subpart I (UX-US-15 to UX-US-20); Section 1557, 45 CFR 92.204 (UX-US-21, UX-US-22) |
| Q4 | Is your product certified health IT under the ONC program? | 45 CFR 170.315(g)(5) accessibility-centered design (UX-US-23, UX-US-24) |
| Q5 | Do you sell in the EU? As a public sector body, or to consumers? Which listed product or service, if any (for example e-commerce, consumer banking)? Are you a microenterprise providing services? | Web Accessibility Directive (UX-EU-10 to UX-EU-13); European Accessibility Act (UX-EU-02 to UX-EU-09) |
| Q6 | Do you serve the UK? As a public sector body, as a service provider to the public, or as a supplier to the NHS or a government service? | PSBAR 2018 (UX-UK-01 to UX-UK-07); Equality Act 2010 s.20 and s.29 (UX-UK-09 to UX-UK-12); GDS and NHS requirements (UX-UK-08, UX-UK-22, UX-UK-23) |
| Q7 | What is in scope: website, mobile app (native or with web views), documents, kiosks? | Web views in apps are tested under EN 301 549 clause 11 (UX-STD-32); 508 software and document exceptions (UX-US-02, UX-US-03); HHS 504 kiosks (UX-US-19) |

If an answer is unknown, the instrument stays "applies if ... `[GAP]`". Never pick the answer for them.

## What each instrument cites

| Instrument | Who it names | Technical standard it cites | Dates (as of 19 October 2026) | Rows |
|---|---|---|---|---|
| Section 508 (36 CFR 1194) | Federal agencies' ICT | WCAG 2.0 Level A and AA; non-web documents and software excused 2.4.1, 2.4.5, 3.2.3, 3.2.4; non-web software excused "complete processes" | In force (82 FR 5832, 18 January 2017); legacy safe harbor for ICT unaltered since 18 January 2018 | UX-US-01 to UX-US-06 |
| ADA Title II (28 CFR 35 subpart H) | State and local government web content and mobile apps, including through contractors | WCAG 2.1 Level A and AA, the 5 June 2018 text | Population 50,000 or more (not special districts): from 26 April 2027. Under 50,000 and special districts: from 26 April 2028. Both moved by the DOJ interim final rule effective 20 April 2026 (91 FR 20902) | UX-US-07 to UX-US-14; Changes and conflicts 1 |
| HHS Section 504 (45 CFR 84 subpart I) | Programs receiving HHS federal financial assistance, including through contractors | WCAG 2.1 Level A and AA | 15 or more employees: from 11 May 2027. Fewer than 15: from 10 May 2028. Both moved by the HHS interim final rule effective 7 May 2026 (91 FR 25496) | UX-US-15 to UX-US-20; Changes and conflicts 2 |
| Section 1557 (45 CFR 92.204) | Recipients and State Exchanges, health programs through websites and apps | Names no WCAG version itself: requires compliance with Section 504 "as interpreted consistent with title II of the ADA" | Part 92 effective 5 July 2024; 92.204 not in the later-dates schedule | UX-US-21, UX-US-22; Changes and conflicts 3 |
| ONC 170.315(g)(5) | Certified health IT developers | Identify the accessibility-centered design standard or law used; "none" is an acceptable answer | Current; HTI-5 (proposed 29 December 2025) would remove it; proposed only | UX-US-23, UX-US-24 |
| EU Web Accessibility Directive (2016/2102) | Public sector bodies' websites and mobile apps | Harmonized standard cited in the OJ: EN 301 549 V3.2.1 (WCAG 2.1 equivalence in clause 9) | Websites from 23 September 2019 or 2020; apps from 23 June 2021; accessibility statement required | UX-EU-01, UX-EU-10 to UX-EU-13, UX-STD-34 |
| European Accessibility Act (2019/882) | Listed products and consumer services, including e-commerce and consumer banking | EN 301 549 V4.1.1 (WCAG 2.2 aligned) is one voluntary means; presumption of conformity only once cited in the OJ, not checked `[GAP]` | Applies from 28 June 2025; transition to 28 June 2030 for products already in use; microenterprises providing services exempt | UX-EU-02 to UX-EU-09, UX-STD-26 to UX-STD-29 |
| UK PSBAR 2018 (SI 2018/952) | UK public sector bodies' websites and apps | "Perceivable, operable, understandable and robust" (no version number); presumption via harmonized standards | In force 23 September 2018; accessibility statement required | UX-UK-01 to UX-UK-07 |
| GDS service manual | UK government digital services | WCAG 2.2 Level AA minimum (policy guidance, not statute) | Current | UX-UK-08 |
| NHS service manual | NHS websites and apps | WCAG 2.2; the six new A and AA criteria are required | Current | UX-UK-22, UX-UK-23 |
| Equality Act 2010 s.20, s.29 | Service providers to the public | No technical standard; reasonable adjustments, accessible format, no charge to the disabled person | In force | UX-UK-09 to UX-UK-12 |

## How to read the map

1. **Version differences are real.** Section 508 cites 2.0, ADA Title II and HHS 504 cite 2.1, GDS and NHS require 2.2 (Changes and conflicts 4). Content that conforms to 2.2 also conforms to 2.0 and 2.1 (UX-STD-03, UX-STD-24, WX4), but 4.1.1 Parsing may still need testing and reporting where a 2.0 or 2.1 policy applies (UX-STD-08, WX7). W3C advises 2.2 as the target (UX-STD-04); that is advice, not law.
2. **Two EN 301 549 editions are live.** V3.2.1 is the edition cited under the Web Accessibility Directive (UX-EU-01). V4.1.1 (2026-09) aligns clauses 9 to 11 to WCAG 2.2 and serves the EAA; national publication by 31 May 2027 and withdrawal of conflicting standards by 31 May 2028 (UX-STD-27, UX-STD-28). Whether V4.1.1 is cited in the OJ was not checked `[GAP]`.
3. **Moved dates carry their instrument.** Write "11 May 2027 (HHS interim final rule effective 7 May 2026, 91 FR 25496)", never the date alone. Both US extensions are interim final rules; a later final rule could change them again (Changes and conflicts 1 and 2). Any source quoting 24 April 2026 or 11 May 2026 is stale.
4. **Section 1557 wording.** Do not write "92.204 requires WCAG 2.1 AA". It requires Section 504 compliance as interpreted consistent with ADA Title II; the WCAG standard and dates come from 45 CFR 84 (UX-US-21, Changes and conflicts 3).
5. **EAA and health apps: inference, labeled.** The Directive's text has no health category (the word "health" does not occur, UX-EU-04, measured). A health app falls in scope only through a listed service, most plausibly e-commerce when it concludes consumer contracts at a distance, or consumer banking features. This is an inference from the definitions, not a stated rule. Say "inference" every time. National transposition that might extend scope was not researched `[GAP]`.
6. **Contractors are named.** ADA Title II and HHS 504 reach content provided "through contractual, licensing, or other arrangements" (UX-US-07, UX-US-16). A private vendor selling to a covered hospital or agency should ask the customer which rule the customer is bound by; the contract terms are the person's to read.
7. **Exceptions and burden.** ADA and HHS 504 list five exceptions, including individualized password-protected documents (UX-US-12, UX-US-20). A fundamental-alteration or undue-burden conclusion under ADA Title II needs the head of the entity or designee and a written statement (UX-US-14). The EAA requires the operator's own assessment against Annex VI (UX-EU-09); PSBAR requires a disproportionate-burden assessment (UX-UK-05). These are the person's determinations and stop for their owner.
8. **Apps and web views.** Under EN 301 549, clause 11 covers mobile apps, and web views inside an app are tested under clause 11, not clause 9 (UX-STD-31, UX-STD-32).
9. **A conformance claim is optional, but has required content if made**: date, guideline title, version and URI, level, and the pages covered (UX-STD-23). Conformance is for full pages and complete processes only (UX-STD-21, UX-STD-22).

## What this map does not decide

- Whether the person is a covered entity, recipient or public body. That is their legal owner's call.
- Device status and human factors submissions (MDR Annex I, FDA HF guidance, UX-EU-14 to UX-EU-20, UX-US-25 to UX-US-53): those belong to the UX 4.x usability skills and to dh-regulatory-and-quality.
- Who is reached and who is left out (equity): Patient Engagement 4.x.
