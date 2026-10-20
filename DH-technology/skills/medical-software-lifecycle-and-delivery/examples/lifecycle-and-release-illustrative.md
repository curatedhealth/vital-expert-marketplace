# Worked example: lifecycle check and release decision (illustrative product, live recall records)

Runs A1 and B1 of `medical-software-lifecycle-and-delivery`. The inventory, document register and problem log in `examples/sample-data/` are ILLUSTRATIVE: typed for this example; "GlucoStep" and "CardioTrack" are invented products, and the safety classes are typed as a person would state them. The recall records come from saved live library outputs of 19 October 2026 (`examples/live/list_jurisdictions_2026-10-19.json`, `examples/live/safety_events_QRX_2026-10-19.json`), copied from the dh-regulatory-and-quality build. The connector was disconnected on 20 October 2026, so no new library call was made.

## Requests

A1: "Read date 20 October 2026. GlucoStep 3.2.0 is our bolus advice app for the US. We set the system at IEC 62304 class C. Attached are our item inventory and document register; we plan a Basic level submission. Check our SOUP list and what we are missing, and show any public recalls of similar apps."

B1: "We want to ship 3.2.1. It fixes PR-102 and moves the cloud sync SDK to a new version with a new encryption library. Problem log attached. What does this re-open, and can we ship?"

## Calls

| Step | Call | Saved file or output | Date |
|---|---|---|---|
| A1 step 2 | `python3 scripts/lifecycle_check.py items --inventory examples/sample-data/inventory_illustrative.csv --as-of 2026-10-20` | below | 20 October 2026 |
| A1 step 3 | `regulatory-dh.list_jurisdictions {}` | `examples/live/list_jurisdictions_2026-10-19.json` | 19 October 2026 |
| A1 step 3 | `regulatory-dh.search_safety_events {jurisdiction: "US", product_code: "QRX", limit: 10}` | `examples/live/safety_events_QRX_2026-10-19.json` | 19 October 2026 |
| A1 step 4 | `python3 scripts/lifecycle_check.py docs --register examples/sample-data/doc_register_illustrative.csv --level basic --product GlucoStep` | below | 20 October 2026 |
| B1 step 1 | none: the person gave no clearance number; the answer asks for it | | |
| B1 step 3 | `python3 scripts/lifecycle_check.py problems --log examples/sample-data/problems_illustrative.csv` | below | 20 October 2026 |

The QRX rows are Dexcom and Insulet app recalls as the records state them; they say nothing about GlucoStep, which is invented. A sensor-theft row in the same output matched only on the title words "Software Version: N/A" and is left out.

## Script output

```
Read date: 20 October 2026. Fields checked: FDA OTS identity (EN-026) and SBOM support fields (EN-054). Class is shown as you wrote it.
| Id | Item | Origin | Version | Release date | Support level | End of support | Class (yours) | Hazard ref | Flags |
|---|---|---|---|---|---|---|---|---|---|
| SI-01 | Bolus advice engine | own | 3.2.0 | not given | not given | not given | C | HZ-03 | none |
| SI-02 | Glucose trend display | own | 3.2.0 | not given | not given | not given | B | not given | I2 |
| SI-03 | Mobile OS runtime (iOS) | ots | 17.5 | 13 May 2024 | maintained | not given | C | HZ-03 | I4 |
| SI-04 | Local database library | open-source | 3.39.2 | 21 July 2022 | maintained | 31 December 2027 | B | HZ-05 | I3 (patch) |
| SI-05 | Charting library | open-source | 4.1.0 | 10 February 2023 | abandoned | 30 June 2025 | not given | not given | I1, I3 (manufacturer, patch), I6 |
| SI-06 | Cloud sync SDK | ots | 2.8 | 4 November 2024 | end of life | 31 March 2026 | B | HZ-07 | I5, I6 |

Items: 6. Flag counts: I1 1, I2 1, I3 2, I4 1, I5 1, I6 2.
I6 is a date fact against your read date, not urgency. The class, and what follows from an end-of-support date, are yours; vulnerability handling routes to cybersecurity-and-privacy-by-design.

Documentation level: basic (yours; the criteria for the level are not in this skill's sources). Elements: FDA premarket software guidance (PL15).
| # | Element | Document | Version | Status | Product named | Level note | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Documentation Level Evaluation | DOC-001 Level rationale | 1.0 | present | GlucoStep |  | none |
| 2 | Software Description | DOC-002 Description | 2.1 | present | GlucoStep |  | none |
| 3 | Risk Management File | RMF-GS-01 | 4.0 | present | GlucoStep |  | none |
| 4 | Software Requirements Specification | SRS-GS | 3.2 | present | GlucoStep |  | none |
| 5 | System and Software Architecture Diagram | ARC-GS | 3.0 | draft | GlucoStep |  | D2 |
| 6 | Software Design Specification | SDS-GS | 3.1 | present | GlucoStep | Basic: kept in the design file, not submitted (PL17) | none |
| 7 | Software Development, Configuration Management, and Maintenance Practices | SDP-PLATFORM | 1.4 | present | CardioTrack | Basic: summary of the lifecycle plan and of configuration management and maintenance, or an IEC 62304 declaration (PL18) | D3 |
| 8 | Software Testing as part of Verification and Validation | VVR-GS | 3.2 | draft | GlucoStep | Basic: summary of unit, integration and system testing plus system-level protocol and report (PL19) | D2 |
| 9 | Software Version History | not given | not given | missing | not given |  | D1 |
| 10 | Unresolved Software Anomalies | ANOM-GS | 3.2 | present | GlucoStep | Each with its impact on safety and effectiveness (PL20) | none |

Flag counts: D1 1, D2 2, D3 1.
A register check reads titles and statuses only; it does not open the documents. Whether the set is ready to file is the regulatory owner's (dh-regulatory-and-quality regulatory-submission-and-dossier).

Problem resolution records (old task DH-04.03.4.1.3). Hazardous function as you marked it.
| Id | Item | Version found | Effect | Hazardous function | Change | Status | Accepted by | Flags |
|---|---|---|---|---|---|---|---|---|
| PR-101 | SI-01 | 3.1.4 | Rounding of carbohydrate ratio to one decimal changes advised dose by up to 0.1 unit | yes | CR-220 | closed | not given | none |
| PR-102 | SI-02 | 3.2.0 | Trend arrow lags new reading by up to 5 minutes after app resumes | yes | not given | open | not given | P5 |
| PR-103 | SI-05 | 3.2.0 | Axis labels overlap on small screens | no | not given | closed | not given | P4 |
| PR-104 | not given | 3.2.0 | not given | not given | not given | open | not given | P1, P2 |

Records: 4. Flag counts: P1 1, P2 1, P4 1, P5 1.
Whether an open problem blocks release, and who accepts it, are the person's.
```

## A1 short answer (382 words by `lifecycle_check.py words`)

**Answer.** You stated system class C for GlucoStep 3.2.0, driven by hazard HZ-03; that is recorded as yours, and the class definitions are not in this skill's sources. Your inventory of 6 items shows 8 flags: two third-party components are past their end-of-support dates before your read date of 20 October 2026, one carries a support level outside FDA's three values, and two items lack a class or a hazard link. At the Basic level you chose, 1 of FDA's 10 software documentation elements is missing (version history), 2 are in draft and 1 names another product. The biggest open item is the charting library: abandoned, end of support 30 June 2025, and no class or hazard given.

**Items with flags**

| Id | Item | What the check found | Source (row) |
|---|---|---|---|
| SI-05 | Charting library | Support "abandoned", end of support 30 June 2025, before your read date; manufacturer and patch not given; class and hazard not given | FDA OTS guidance, 11 August 2023 (EN-026); FDA premarket cybersecurity guidance, 3 February 2026 (EN-054) |
| SI-06 | Cloud sync SDK | Support "end of life" is not one of FDA's values (maintained, no longer maintained, abandoned); end of support 31 March 2026, before your read date | EN-054 |
| SI-03 | Mobile OS runtime | End-of-support date not given | EN-054 |
| SI-04 | Local database library | Patch not given ("as appropriate") | EN-026 |
| SI-02 | Glucose trend display | Class B stated, hazard not given | your file |

**Documents (Basic, your level).** Missing: Software Version History. Draft: architecture diagram (ARC-GS 3.0), V&V testing (VVR-GS 3.2). SDP-PLATFORM 1.4 names CardioTrack, not GlucoStep. At Basic, the SDS stays in your design file (FDA premarket software guidance, read 20 October 2026, PL15, PL17). The register check reads titles, not contents.

**Recall records, as stored.** For product code QRX the library returned Dexcom app recalls, for example "Dexcom G7 CGM iOS App, SW12300, Versions 2.9.0 through 2.11.2", 14 April 2026, Class II, a low-priority file check blocking glucose-value processing, and an Omnipod 5 iOS app recall, 11 September 2025, Class II, digits duplicated with the iPhone magnifier. Rows carry no product code. Whether either belongs in your hazard list is yours.

**Gaps.** IEC 62304 class definitions and class-by-class plans [GAP]; NTIA SBOM minimum elements not read [GAP]; criteria for Basic or Enhanced not read [GAP].

**Calls made.** `regulatory-dh.list_jurisdictions {}` and `regulatory-dh.search_safety_events {jurisdiction: "US", product_code: "QRX", limit: 10}` (saved outputs, retrieved 19 October 2026; connector unavailable 20 October 2026); `lifecycle_check.py items` and `docs`.

Full version available: plans checklist, architecture, placement and operations tables.

**Record.** Lifecycle plan draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## B1 short answer (314 words by `lifecycle_check.py words`)

**Answer.** GlucoStep 3.2.1 fixes PR-102 and moves the cloud sync SDK (SI-06) to a new version with a new encryption library. Both re-open validation, regression scope and two document elements. One problem is open on a function you marked hazardous (PR-102, the fix itself), one record lacks item and effect, and one closed record has a rationale with no named acceptor. Three regulatory questions are open for the regulatory owner; go or no-go is yours.

**Re-opened by this change**

| Item | Why | Source (row) |
|---|---|---|
| Validation status of 3.2.1 | Any change, even a small one, re-opens validation, with system-wide impact analysis | FDA General Principles of Software Validation, 11 January 2002 (EN-008) |
| Regression scope (yours to set) | Show unchanged but vulnerable portions were not adversely affected | EN-009 |
| Risk file entries for SI-02 and SI-06 (HZ-07; SI-02 hazard not given) | Risk documentation reviewed when new information emerges | QMSR final rule, 2 February 2024 (QS22) |
| SI-06 identity fields for the new version | Title, manufacturer, version, release date, patch | FDA OTS guidance, 11 August 2023 (EN-026) |
| Version history and unresolved anomalies | Both move with every tested version | FDA premarket software guidance, read 20 October 2026 (PL20) |

**Problems** (script flags). PR-102: open, hazardous function, change reference not given (P5). PR-104: item and effect not given (P1, P2). PR-103: closed with a rationale, acceptor not named (P4). PR-101: closed with CR-220.

**Regulatory questions, for the regulatory owner**

| Question | Your fact | Source (row) |
|---|---|---|
| Does the PR-102 fix only restore the most recently cleared specification? | Cleared version and its specification not given | FDA software change guidance, 25 October 2017 (CH13) |
| Does the new encryption library bring 524B documentation? | Change to encryption stated by you | FDA premarket cybersecurity guidance, 3 February 2026 (EN-060) |
| Does either change create or modify a hazard, or a risk control needed to prevent significant harm? | Not given | CH14, CH15 |

Whether a new 510(k) is needed is not answered here; route to `dh-regulatory-and-quality` document-and-change-control.

**For you to decide.** Go or no-go for 3.2.1; who accepts PR-103 and completes PR-104; the regression scope; the decision date (not given).

**Calls made.** None to the library (your clearance number not given; connector unavailable 20 October 2026); `lifecycle_check.py problems`.

Full version available: baseline, full question sheet, release decision pack.

**Record.** Release decision draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## What this example shows

- The class is recorded as the person stated it; the model neither confirms nor questions it, and says the definitions are not in the sources.
- Every flag is a fact about the person's file with its row; an end-of-support date before the read date is stated, not pressed.
- Recall records are quoted as stored, with the pitfall that rows carry no product code; relevance stays with the person.
- B1 lays out FDA's software change questions beside the person's facts and routes the answer; it never says whether a new 510(k) is needed and never calls the release go.
