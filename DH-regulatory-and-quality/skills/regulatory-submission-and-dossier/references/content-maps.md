# Content maps: what each route asks the dossier to contain

How to read this file. Each rule cites the row it comes from: `RP` = `REG_PATHWAYS_SUBMISSIONS.md`, `AI` = `AI_ML_REGULATION.md`, `S` = `submission-sources-supplement.md`. All read 19 October 2026. The machine-readable lists behind these maps are in `content-maps.json`, which `scripts/dossier_gaps.py` reads. A map says what the source names; whether a section applies to a given device is the regulatory owner's call.

## United States

### Which template

- 510(k): eSTAR is mandatory (from 1 October 2023), submitted through the CDRH Portal (RP US-36, RP US-38). The template sections are in S-13 (guidance of 2 October 2023, S-12).
- De Novo: eSTAR mandatory from 1 October 2025 (RP US-37). Sections in S-19 (guidance of 23 August 2024). A De Novo adds three things a 510(k) does not ask for in the same form: existing alternative practices (S-22), a proposed class I or II with classification summary (S-20), and a benefits, risks and mitigation section with special controls if class II (S-21, RP US-12). The classification summary must describe the searches done and list similar classification regulations, 510(k)s and product codes, with a rationale for the difference (S-79); FDA may decline a De Novo for a device type already classified (S-80).
- Current eSTAR versions: nIVD and IVD eSTAR 7.1, PreSTAR 3.1; eSTARs now carry the Human Factors content guidance effective 1 August 2026 (RP US-39). Human factors material therefore has a home in the template; place it with the regulatory owner.
- PMA: not covered by the eSTAR rows read. Content structure for a PMA is `[GAP]` in this skill; only the review clocks are sourced (RP US-14, RP US-15, RP US-48).
- eSTARs are not expected to go through refuse-to-accept; they get a technical screening instead (S-15). A failed screening puts the 510(k) on hold, and without a complete replacement within 180 days it is withdrawn (S-16).

### Software documentation overlay

The guidance "Content of Premarket Submissions for Device Software Functions" (final, 14 June 2023, RP US-25) sets ten documentation elements at two levels:

- The level is chosen for the device as a whole, by the risk of its software functions in its intended use (RP US-29). Enhanced applies where a software failure could present a hazardous situation with a probable risk of death or serious injury, judged before risk controls (RP US-26). Basic applies otherwise (RP US-27). FDA generally recommends Enhanced for class III devices and combination-product constituents; a sponsor may justify Basic (RP US-28).
- The level is stated and justified in the submission (S-01). Which level applies is the regulatory owner's decision; the model lays out the test from RP US-26 and the device facts the person gives.
- Elements at both levels: Software Description (S-02), Risk Management File (S-03), SRS (S-04), architecture diagram (S-05), development and configuration practices or an IEC 62304 Declaration of Conformity (S-07), testing (S-08), version history (S-09), unresolved anomalies (S-10).
- The difference between levels: the Software Design Specification is not recommended in a Basic submission and stays in the design history file (S-06); Enhanced adds complete configuration management and maintenance plans (S-07) and unit and integration test protocols and reports (S-08).
- Pitfall in the source: the 510(k) eSTAR guidance (2023) still names the older software guidance title in its Software/Firmware row (S-17). Use the 14 June 2023 guidance as the content source and note the stale reference if the person's team works from the eSTAR guidance text.

### AI-enabled devices

- A PCCP is a standalone, titled and versioned section, flagged in the cover letter and table of contents (AI US-11), with three parts: Description of Modifications, Modification Protocol, Impact Assessment (AI US-03). The final PCCP guidance was reissued 18 August 2025 (AI US-01).
- It can be established only in a submission where FDA makes an affirmative decision, including a Traditional or Abbreviated 510(k) and an original De Novo (AI US-09). It is not authorized in a Pre-Submission, though Q-Sub feedback on it is encouraged (AI US-10).
- The AI lifecycle guidance on marketing-submission content is still a draft (issued 7 January 2025; still draft on 19 October 2026; on the FY 2027 A-list for finalization) (AI US-19, AI US-21, AI US-22). Present its content as draft guidance, never as a requirement.
- Designing the PCCP itself belongs to the AI/ML competency (DH-03.03.1), not here.

## European Union

- Conformity route by class: class I self-declares after drawing up Annex II and III documentation (RP EU-11); class IIa, IIb and III go through a notified body under Annex IX (or Annex X with XI) with technical documentation assessed as each rule states (RP EU-08 to RP EU-10).
- Annex II sections: 1 device description and specification (RP EU-13), including the qualification rationale (S-50), the risk class with justification of the rules applied (RP EU-14) similar devices on the market (S-51) and the Basic UDI-DI (S-82); 2 information supplied by the manufacturer; 3 design and manufacturing; 4 GSPRs (S-49), including which GSPRs apply and why others do not (S-52) and the methods and standards applied (S-83); 5 benefit-risk and risk management; 6 verification and validation (RP EU-13), with software V&V (RP EU-15), a rationale where no new test was done (S-53), the CER and clinical evaluation plan, and the PMCF plan and report or a justification (S-54).
- Annex III: the post-market surveillance plan and the PSUR or PMS report (RP EU-16).
- The CER is part of the technical documentation (S-57); its content is in `clinical-evaluation-method.md`.
- Software classification under Rule 11 is the classification competency's work (DH-03.03.3). This skill only checks that the dossier states the class and the rule (RP EU-14). If the intended purpose describes monitoring (alert, monitor, watch), name the class IIb exception for vital physiological parameters (RP EU-04) as a question for the regulatory owner and route it to DH-03.03.3. Do not reclassify.
- AI Act: for medical device AI, the MDR class decides AI Act high-risk status and one set of technical documentation is kept (AI EU-28, AI EU-29). The high-risk obligations for Annex I products such as MDR devices apply from 2 August 2028, as amended by Regulation (EU) 2026/1744 (AI EU-19). Say the date with the amending act.

## United Kingdom

- Great Britain: devices conform to UK MDR 2002, with transitional acceptance of CE marking, and are registered with the MHRA (RP UK-01). CE marked devices under the EU MDR are accepted until 30 June 2030; MDD devices until the sooner of certificate expiry or 30 June 2028; up-classified software self-declared under the MDD before 26 May 2021 until 30 June 2028 (RP UK-02 to RP UK-04). Indefinite recognition was consulted on and has no published outcome (RP UK-05).
- For a CE-marked product the dossier content is the EU technical documentation plus MHRA registration. Under UKCA, class I is self-declared and other classes need a UK approved body (RP UK-15), but the content of UKCA technical documentation under UK MDR 2002 was not read: `[GAP]`.
- GB classifies software with MDD-derived rules, so a product can be class I in GB and IIa or higher in the EU (RP UK-14). Flag the difference; the regulatory owner decides.

## Switzerland (where asked)

Classification follows MDR Annex VIII (RP CH-01); Switzerland keeps its law equivalent to the EU's and enforces in line with EU interpretation documents (RP CH-03, RP CH-07). Swiss submission content beyond this is `[GAP]`.

## What the library adds

`regulatory-dh.retrieve_guidance` did not return device-submission passages for eSTAR, the software guidance, Annex II or clinical evaluation on 19 October 2026 (see `tools.md`). The maps above therefore come from the reference files. Call it once per run in case the store has been loaded since; use a passage only if it carries a source URL and is device guidance.
