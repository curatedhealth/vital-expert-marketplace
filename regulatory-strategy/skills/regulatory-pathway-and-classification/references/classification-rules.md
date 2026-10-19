# Classification rules by jurisdiction

Interpretive reference for task A1. Every rule names the research row it comes from: `RP-` rows are in `reg-pathways-sources.md` (written there without the prefix, for example US-20), `MR-` and `JX-` rows in `multi-region-sources.md`, `AI-` rows in `ai-ml-regulation-sources.md` (written there without the prefix). All rows were read on 19 October 2026. Where a rule is not in a research row, it is marked `[GAP]` and must not be filled from memory.

These rules support arguments. They do not decide a class. The person's regulatory owner decides.

## Start with the intended use

Every regime classifies from what the manufacturer intends the software to do, not from its code.

- FDA: substantial equivalence starts from "the same intended use as the predicate device" (RP US-06).
- EU: the technical file must state the risk class "and the justification for the classification rule(s) applied" (RP EU-14); clinical evaluation is planned around the "intended purpose" and "intended clinical benefits" (RP EU-20).
- IMDRF N12 classifies from the "SaMD definition statement"; where it covers several situations, "the highest category" applies (JX-03).

So the intended use statement in A1 must say: the medical purpose (treat, diagnose, drive or inform management, monitor), the condition and its seriousness, the intended user (patient, health care professional), the setting, and whether the output is a single directive or options the user reviews. Each of those is a classification input below.

## Is it a device at all

| Jurisdiction | Rule | Row |
|---|---|---|
| EU | Software "intended by the manufacturer to be used ... for human beings" for a medical purpose is a device; the definition names software. | RP EU-01 |
| EU | Software only for non-medical purposes ("invoicing, staff planning ... wellness or fitness apps") is not medical device software (MDSW). | RP EU-29 |
| US | FDA focuses oversight on software functions that are devices "whose functionality could pose a risk to a patient's safety"; some lower-risk device functions get enforcement discretion. Policy dated 28 September 2022. | RP US-16 to US-18 |
| US | Clinical decision support is excluded from the device definition only if it meets all four criteria of FD&C Act section 520(o)(1)(E). | RP US-20 |
| IMDRF | SaMD: software for medical purposes "without being part of a hardware medical device" (N10, as FDA restates it). | RP IM-01 |

### FDA CDS criteria, as of the guidance dated 29 January 2026

The guidance in force is dated 29 January 2026 and supersedes the 6 January 2026 version, which replaced the 2022 final (RP US-19). Anything built on the 2022 text must be rechecked.

| Criterion | What the row states | Row |
|---|---|---|
| 1 | Not intended to acquire, process or analyze a medical image, an IVD signal, or a pattern or signal from a signal acquisition system. | RP US-21 |
| 2 | Text not quoted in the research rows `[GAP]`. Do not paraphrase from memory; point to the guidance (https://www.fda.gov/media/109618/download). | none |
| 3 | Software that gives "a specific preventive, diagnostic or treatment output or directive" fails criterion 3. New in 2026: where "only one option is clinically appropriate" and all criteria are otherwise met, FDA intends enforcement discretion. | RP US-23 |
| 4 | The health care professional must be able to independently review the basis for the recommendation, so as not to rely primarily on it. FDA weighs the level of automation and whether the decision is time-critical. | RP US-22, RP US-24 |

All four must be met (RP US-20). A function aimed at patients rather than health care professionals cannot use criterion 4 as written, because the criterion speaks of "such health care professional" (RP US-22).

## United States: device class

| Class | Meaning | Row |
|---|---|---|
| I | General controls only. | RP US-01 |
| II | Special controls in addition. | RP US-02 |
| III | Premarket approval (PMA) required. | RP US-03 |

FDA gives each device type a three-letter product code and a class in its classification database (RP US-68). The practical classification question for software is therefore: which existing product code and regulation number describes this intended use, if any. `regulatory-dh.classify_product` returns a product code and regulation number only "from record", that is for a device already in the register; it never infers one from a description (see `tools.md`). For a new product, the code is an argument the person's regulatory owner makes, supported by A2's precedents. A 513(g) request asks FDA for classification information (fee in `pathway-facts.md`, RP US-53).

## European Union: MDR Annex VIII Rule 11

Consolidated MDR text of 19 July 2026 (RP EU-26: later amendments did not touch Rule 11). MDCG 2019-11 rev.1 (June 2025) supersedes the October 2019 version (RP EU-27, RP EU-35).

| Sub-rule | Class | Row |
|---|---|---|
| 11(a) information used for diagnostic or therapeutic decisions | IIa | RP EU-02 |
| 11(a), decisions that may cause death or irreversible deterioration | III | RP EU-03 |
| 11(a), decisions that may cause serious deterioration or a surgical intervention | IIb | RP EU-03 |
| 11(b) monitoring physiological processes | IIa | RP EU-04 |
| 11(b) monitoring vital parameters where variation could mean immediate danger | IIb | RP EU-04 |
| 11(c) all other software | I | RP EU-05 |

Implementing rules: software that drives or influences a device takes that device's class; independent software is classified in its own right (RP EU-06). Where several rules apply, the strictest applies (RP EU-07).

MDCG 2019-11 rev.1 points to note:
- Sub-rule 11(a) "is generally applicable to all MDSW" with a medical purpose; rev.1 added prevention examples and clarified 11(a) (RP EU-27, RP EU-30). Rev.1 also added treatment software examples (RP EU-27). This is why most decision software lands at IIa or higher, and why Swissmedic says Rule 11 "puts strict limits on the functionalities for Class I software" (RP CH-05).
- MDCG maps 11(a) class III to IMDRF category IV, class IIb to category III, and IMDRF categories I and II to class IIa; the table is illustrative only (RP EU-31).

AI Act link (for AI-enabled software): an MDR device that needs notified-body assessment is a high-risk AI system; MDCG 2025-6 lists class IIa, IIb and III among those, and the AI Act does not change the MDR class (AI EU-26 to EU-28). The high-risk obligations for these devices apply from 2 August 2028 under Regulation (EU) 2026/1744, which amended the original 2 August 2027 date (AI EU-19, AI EU-32). MDCG 2025-6 still shows 2027 and is superseded on dates.

## Great Britain: UK MDR 2002

GB still applies the MDD-derived rules, not Rule 11 (RP UK-14). As MHRA's software guidance states them: diagnostic devices allowing direct diagnosis or monitoring of vital processes are IIa (IIb where immediate danger); "Rule 12 - All other active devices are class I." A product can therefore be class I in GB and IIa or higher in the EU and Switzerland (RP "Changes and conflicts").

- Class I is self-declared; other UKCA devices need a UK approved body (RP UK-15).
- CE marked MDR devices are accepted in GB until 30 June 2030 (RP UK-03); indefinite recognition was consulted on (16 February to 10 April 2026) with no outcome published (RP UK-05, RP UK-06; MR-24).
- A new GB classification aligned with Rule 11 was consulted on but no made statutory instrument was found `[GAP]` (RP "Not sourced").

## Switzerland: MedDO

- Art. 15 MedDO applies EU MDR Annex VIII for classification (RP CH-01, as Swissmedic restates it; the MedDO text itself was not read, RP "Not sourced").
- Swissmedic's software information sheet, version 3.0 valid from 21 April 2026, points to MDCG 2019-11 (RP CH-04).
- Hardware plus software: where software goes beyond controlling the hardware, the whole product takes the higher software class (RP CH-06).

So the Swiss class argument follows the EU argument. The differences are in recognition and registration, not classification (see `pathway-facts.md`).

## IMDRF N12

- Four categories (I to IV) from two factors: seriousness of the healthcare situation and significance of the information to the decision; category IV is highest (JX-01; N12 read directly).
- "SaMD that provides information to treat or diagnose a disease or conditions in a critical situation or condition is a Category IV" (JX-02).
- The axes, as MDCG restates them: significance (treat or diagnose; drive clinical management; inform clinical management) by situation (critical; serious; non-serious) (RP IM-02).
- N12 is implemented by the EU, Switzerland and the USA, and partly by the UK, per IMDRF's self-reported N84 (JX-08). Implementation is at each regulator's discretion (JX-06).
- Newer: MDCG 2019-11 rev.1 cites IMDRF N81 (2025) on characterizing medical device software; whether it supersedes N12 was not checked (RP IM-04). Say so when N12 is used.
- The full N12 category table is `[GAP]` in the research rows beyond JX-01 to JX-03 and RP IM-02; do not reproduce cells from memory.

N12 is a framework, not a class in any jurisdiction. Use it to make the significance-by-situation reasoning explicit, then map through MDCG's illustrative table (RP EU-31).
