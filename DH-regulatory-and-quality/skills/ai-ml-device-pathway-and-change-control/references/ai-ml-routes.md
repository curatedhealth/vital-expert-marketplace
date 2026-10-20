# AI/ML device routes: US, EU, UK

Interpretive reference. Every line cites its research row: `AI` rows are in `AI_ML_REGULATION.md`, `RP` rows are in `REG_PATHWAYS_SUBMISSIONS.md` (both read 19 October 2026). Where a row does not exist, the line says `[GAP]`. This file lays out rules; it never decides a class or a route.

## United States

**What FDA regulates.** FDA regulates medical devices, including AI-enabled ones, not AI as such [AI US-28]. So the first question is the device route, and AI adds the change control plan and documentation layer on top.

**The three routes.**

| Route | When it applies | Rule rows |
|---|---|---|
| 510(k) | A legally marketed predicate exists; same intended use and same or non-safety-raising different technology | [RP US-04 to US-08] |
| De Novo | No predicate; novel device suitable for class I or II; can follow a not-substantially-equivalent 510(k) or be filed directly | [RP US-09, US-10, US-12] |
| PMA | Class III | [RP US-03, US-14] |

A 510(k) clearance is not "approval"; saying so is misbranding [RP US-08]. Use "cleared", "granted" and "approved" by route.

**Software framing that changes the route.** Clinical decision support that meets all four statutory criteria is not a device; the current CDS guidance is dated 29 January 2026 and supersedes the 6 January 2026 version [RP US-19, US-20]. Software that analyzes a medical image or a signal fails criterion 1 [RP US-21]. Software giving a specific diagnostic or treatment output fails criterion 3, with enforcement discretion where only one option is clinically appropriate [RP US-23]. Most AI imaging and signal software therefore stays a device.

**Section 515C (statute).** Added by FDORA on 29 December 2022 [AI US-18]. For a PMA device, no supplement is needed for a change consistent with an approved PCCP [AI US-15]. For a 510(k), FDA may clear a PCCP if the device stays safe and effective without the change and would remain substantially equivalent [AI US-16]. FDA may require labeling, notification and performance requirements in the plan [AI US-17].

**PCCP guidance (final).** "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions", issued 18 August 2025, first issued 4 December 2024; cite the August 2025 version [AI US-01]. It applies to 510(k), De Novo and PMA [AI US-02]. A PCCP is established only in a submission where FDA makes an affirmative decision [AI US-09] and is authorized with the device; FDA does not authorize a PCCP in a Pre-Submission [AI US-10]. What changed between the two versions is `[GAP]` (research "Not sourced"). The guidance still cites the pre-QMSR quality system sections [AI "Changes and conflicts" 2].

**AI lifecycle guidance (draft).** "Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations", draft of 7 January 2025, docket FDA-2024-D-4488 [AI US-19]. Still draft on 19 October 2026 [AI US-21]. It is on CDRH's FY 2027 A-list as a final guidance topic CDRH intends to publish [AI US-22]; the same A-list names a device-wide PCCP final guidance [AI US-23]. A-list items are intentions, not commitments [AI US-23]. Treat its recommendations as draft: useful for content planning, not a requirement.

**Joint principles.** Ten GMLP principles (FDA, Health Canada, MHRA, 2021; IMDRF final January 2025) [AI UK-09, US-29]; five PCCP principles (October 2023) [AI US-30, US-31]; transparency principles (June 2024) [AI US-32, US-33]. Principles, not regulations.

**The FDA AI-enabled device list.** A list of AI-enabled devices authorized for US marketing [AI US-24]; FDA says it is not comprehensive [AI US-25] and is updated periodically [AI US-26]. FDA's hub says over 1,600 authorized as of September 2026 [AI US-34]. The list page is current as of 4 September 2026; its CSV export has 1,614 rows (1,553 510(k), 40 De Novo, 21 PMA), latest decision 29 June 2026 (row count measured in the research pass) [AI US-35]. Use it as context and as a check on a precedent's AI status; never as proof that a device absent from it has no AI. The library does not carry an AI-list flag (`references/tools.md`).

## European Union

**MDR route first.** Software can be a device [RP EU-01]. Rule 11 sets the class: decision software class IIa, IIb or III by impact; monitoring software IIa or IIb; all other software class I [RP EU-02 to EU-05]. MDCG 2019-11 rev.1 (June 2025) is the current software qualification guidance [RP EU-27, EU-35]. Conformity routes by class [RP EU-08 to EU-11]: class I self-declares; IIa, IIb and III need a notified body.

**AI Act high-risk test for devices.** An AI system is high-risk under Article 6(1) if it is, or is a safety component of, a product under Annex I legislation and that product needs third-party conformity assessment [AI EU-01, EU-02]. MDR and IVDR are in Annex I Section A [AI EU-03]; Regulation (EU) 2026/1744 did not amend those entries [AI EU-23].

A lower MDR class removes only the high-risk obligations. Article 4 AI literacy applies to all providers [AI EU-20], and Articles 5 and 50 apply whatever the MDR class [AI EU-37].

**Which MDR classes are high-risk (MDCG 2025-6).** Joint AIB 2025-1 / MDCG 2025-6 FAQ, June 2025, not legally binding [AI EU-25]. Its Table 1 (non-exhaustive): MDR class I (non-sterile, non-measuring, non-reusable-surgical), IVDR class A non-sterile and in-house devices are not high-risk; MDR Is, Im, Ir, IIa, IIb, III, Annex XVI, and IVDR class A sterile, B, C and D are [AI EU-27]. The AI Act does not change the MDR class; the MDR class decides AI Act status [AI EU-28]. Whether the software is an "AI system" at all is the person's determination; Commission guidelines on that definition were not read `[GAP]`.

**One conformity assessment, one file.** Annex I Section A products follow the MDR procedure, with AI Act requirements checked inside it [AI EU-04]; one set of technical documentation [AI EU-29]. Requirements for high-risk AI: risk management [AI EU-06], data governance [AI EU-07], technical documentation [AI EU-08], logging [AI EU-09], transparency [AI EU-10], human oversight [AI EU-11], accuracy, robustness and cybersecurity [AI EU-12], QMS with modification procedures [AI EU-13], post-market monitoring [AI EU-33, EU-34].

**Dates, as amended by Regulation (EU) 2026/1744.** The Digital Omnibus on AI, Regulation (EU) 2026/1744 of 8 July 2026, published 24 July 2026 [AI EU-17], in force 27 July 2026 (computed in the research pass) [AI EU-18].

| Obligation | Date in force | Set by | Row |
|---|---|---|---|
| High-risk requirements (Chapter III Sections 1 to 3) for Article 6(1) and Annex I systems, which include MDR and IVDR devices | 2 August 2028 | Regulation (EU) 2026/1744 (was 2 August 2027 in the 2024 text) | [AI EU-19, EU-14] |
| High-risk requirements for Annex III systems | 2 December 2027 | Regulation (EU) 2026/1744 (was 2 August 2026) | [AI EU-19] |
| AI literacy (Article 4), now "take measures to support", no guaranteed level | Since 2 February 2025; wording amended by Regulation (EU) 2026/1744 | Regulation (EU) 2024/1689 as amended | [AI EU-15, EU-20] |
| Prohibited practices (Article 5) | Since 2 February 2025; new points (ba), (bb), (1a), (1b) from 2 December 2026 | Regulation (EU) 2024/1689; new points by Regulation (EU) 2026/1744 | [AI EU-16, EU-21] |
| Commission guidance with a post-market monitoring plan template (Article 72(3)) | Due by 2 September 2027 (was an implementing act by 2 February 2026) | Regulation (EU) 2026/1744 | [AI EU-35] |

MDCG 2025-6 still states 2 August 2027 for Annex I systems; on dates it is superseded by the omnibus, while its classification and pre-determined-change content stands [AI EU-32; "Changes and conflicts" 6]. Whether the omnibus also defers Article 72 for Annex I systems needs a legal read `[GAP]` (research "Not sourced").

**Devices already on the market.** High-risk systems placed on the market before the Chapter III date are caught only if they then undergo significant changes in design [AI EU-22]. What counts as a significant change under the AI Act (Commission guidelines, Article 96) was not read `[GAP]`.

**Pre-determined changes.** Changes pre-determined at the initial conformity assessment and documented under Annex IV point 2(f) are not a substantial modification [AI EU-05], and MDCG 2025-6 says they are not a change to the certified device under MDR Annex IX 4.10 [AI EU-30]. EU PCCP guidance is expected to build on IMDRF work; none is published [AI EU-31]. The IMDRF N93 lifecycle framework addressing PCCPs is a draft of 7 April 2026 [AI IM-04, read through a summarizing fetch].

## United Kingdom

**Device route.** Devices in Great Britain must conform to the UK MDR 2002 and be registered with the MHRA; CE marking is accepted transitionally [RP UK-01]. EU MDR devices are accepted until 30 June 2030 [RP UK-03]; MDD devices until the sooner of certificate expiry or 30 June 2028 [RP UK-02]; up-classified software self-declared under the MDD until 30 June 2028 [RP UK-04]. Indefinite recognition was consulted on and has no published outcome [RP UK-05]. GB still classifies software under MDD-derived rules, so a product can be class I in GB and IIa or higher in the EU [RP UK-14; "Changes and conflicts"].

**PCCPs in the UK.** The 2022 roadmap planned PCCPs in secondary legislation [AI UK-02, UK-03]; that page was last updated 14 June 2023 and may be stale [AI "Changes and conflicts" 10]. In its government response published 6 October 2026, the MHRA accepted the recommendation and stated it will issue PCCP draft guidance for public comment, with an intent to issue it by December 2026, describing boundary-based allowable change while keeping intended use [AI UK-04, UK-05]. No published MHRA PCCP guidance was found [AI UK-04]. So in GB a planned-change mechanism is announced, not in force.

**Other UK facts.** The government accepted all 44 recommendations of the National Commission on 6 October 2026 [RP UK-18]. The AI Airlock sandbox started in spring 2024; phase 3 was announced 6 October 2026 [AI UK-06, UK-07]; innovator case studies are not MHRA guidance [AI UK-08]. GB serious incident clocks: 15, 10 and 2 days [RP UK-10, UK-11].

## Not in the references `[GAP]`

Health Canada's own GMLP and PCCP pages; any MHRA PCCP text; Commission AI Act guidelines on classification and substantial modification; any MDCG 2025-6 revision after the omnibus; the consolidated AI Act text after the omnibus; the corrigendum to Regulation (EU) 2026/1744 (dated 29 September 2026, content not read); Switzerland's position on AI; Japan, China, Australia AI rules. Name the authority to check.
