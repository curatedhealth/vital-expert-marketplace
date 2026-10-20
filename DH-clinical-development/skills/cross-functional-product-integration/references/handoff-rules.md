# Handoff rules: what the sources say about cross-functional work, and what they leave to the person

Interpretive reference for DH-01.01.3 (Cross-Functional Integration). Every sourced rule carries its row id from the research files copied in this folder: PL (`product-lifecycle-and-integration-research.md`, read 20 October 2026), CV (`clinical-study-and-rwe-research.md`, read 19 October 2026), CS (`customer-success-implementation-research.md`, read 19 October 2026), TM (`therapeutic-mechanism-and-translation-research.md`, read 20 October 2026). Where no source sets a rule, this file says "the person's rule" and the skill asks for it.

Sources for handoffs are thin. No regulator, standard or paper read for this pack defines a "handoff", a "dependency", an "integration point" or a "joint decision" as such. What the sources do give is a set of places where work must pass between functions, who must be present when it is reviewed, and what a record of the review holds. The skill uses those places as anchors and leaves every other rule to the person.

## 1. Sourced anchors: where work must pass between functions

| # | Anchor | What the source says | Rows | Status |
|---|---|---|---|---|
| 1 | Design review | Each design and development review includes representatives of the functions concerned with the stage under review, plus other specialist personnel; the manufacturer chooses which individuals attend. | PL1 | US law: ISO 13485 7.3.5 as incorporated by the QMSR (21 CFR 820 as amended, effective 2 February 2026, PL file section 1 heading) |
| 2 | When reviews happen | Design reviews should be held at major decision points in the design phase. | PL5 | FDA preamble wording |
| 3 | What a review checks | Design inputs met for intended use and user needs; verification data against functional, safety, reliability, labeling, regulatory and manufacturing or servicing requirements. | PL4 | FDA preamble wording |
| 4 | Who may give input | For a large manufacturer: manufacturing, quality assurance, purchasing, sales and servicing; small manufacturers may tailor, but the principles still apply. | PL6 | FDA preamble wording |
| 5 | Independent review | No longer a fixed attendee rule under the QMSR; FDA still calls it an "important contribution" (PL2). IMDRF N41 recommends independent review of clinical evidence more strongly for SaMD in serious or critical situations (PL66, PL67). | PL2, PL66, PL67 | Risk-proportionate choice the person justifies (research file "Changes and conflicts") |
| 6 | Clinical evaluation inside design validation | ISO 13485 7.3.7 requires clinical or performance evaluation as part of design validation. | PL7 | As incorporated by the QMSR |
| 7 | Design transfer | The final design output, kept in the design and development file, is the starting point for the medical device file. The file contains or references all records needed to show design compliance. | PL9, PL10 | ISO 13485 7.3.8 transfer text itself not read [GAP] (PL "Not sourced") |
| 8 | Multiple function products | Impact assessments of each "other function" on the device function under review (negative, positive and no impact) are all performed and documented as design validation, and are inspectable. Two questions: is there an impact on safety or effectiveness, and could it increase risk or degrade performance. A change to an other function is assessed the same way. | PL24 to PL27, PL29 | FDA final guidance of 29 July 2020 (PL23), nonbinding, written before the QMSR: read its 820.30(g) references as ISO 13485 7.3.7 (PL12) |
| 9 | Separation decided early | Architecture decisions early in the design cycle make separation of device and other functions possible. | PL26 | Same guidance |
| 10 | Software implements the clinical model (computerized behavioral therapy, 21 CFR 882.5801) | Clinical data must describe a validated model of behavioral therapy and validate it as implemented by the device; SRS and SDS must describe the software, and software documentation must show the device implements the model; physician labeling includes a summary of clinical testing. | TM120, TM121, TM122 | Special controls for that classification only. Whether the person's product falls under it is `dh-regulatory-and-quality` regulatory-pathway-and-classification's question |
| 11 | Clinical study quality by design | Quality by design is prospective and multidisciplinary. Critical-to-quality factors are attributes whose integrity is fundamental to participant protection and reliable results, considered holistically so that dependencies among them can be identified. | CV28, CV29 | ICH E8(R1), adopted 6 October 2021 (CV27); binds only as adopted in each region |
| 12 | Decentralized element as a critical-to-quality factor | If a decentralized element is identified as critical to quality under ICH E8, a risk-proportionate approach follows. | CV96 | EU recommendation paper |
| 13 | Implementation plan | An implementation blueprint has four parts: aim, scope, timeframe and milestones, performance or progress measures. CFIR 2022 names roles (high-level leaders, implementation leads, deliverers, recipients) and a planning construct (roles, milestones and success measures defined in advance). | CS42, CS18, CS20 | [PAPER] ERIC, DOI 10.1186/s13012-015-0209-1; CFIR 2022, DOI 10.1186/s13012-022-01245-0 |
| 14 | Handoff to a deploying site | NICE ESF standard 19: the company provides a data dictionary, tolerance for incomplete data, a deployment data flow map, data format requirements and minimum infrastructure. Standard 20: communication on outputs, features, benefits and limitations, and the end-user training approach. Standard 16: a plan to report usage against an expected usage profile, and how performance changes are reported and to whom. | CS64, CS65, CS61, CS62 | NICE ESF, last updated 9 August 2022 (CS56) |
| 15 | Written partner commitments | ERIC names obtaining written commitments from partners as a strategy. | CS49 | [PAPER] ERIC, DOI 10.1186/s13012-015-0209-1 |
| 16 | DiGA application | All DiGAV §§ 3 to 6 requirements (safety, function, quality, data protection and security, interoperability) must be met at application, even for a trial listing; only the care-effect study may follow. Certificates for §§ 4 to 6 no older than 12 months on submission. | PL80, PL91 | German law and BfArM guide |
| 17 | DiGA clocks that create dependencies | Trial extension request at least three months before the trial ends (PL82); updated ePA specifications implemented within six months of publication (PL89); significant changes notified, minor ones bundled up to four times a year (PL95). | PL82, PL89, PL95 | German law |
| 18 | DTAC per version [WF] | Manufacturers keep a current DTAC form and evidence per product version. | PL98 | Read through a summarizer [WF]; re-check before relying on it |
| 19 | Pre-Sub minutes | The submitter drafts minutes for every Pre-Sub meeting within 15 days; minutes record agreements and action items and do not assign statements to individuals. | PL41 | FDA Q-Sub guidance; a rule for FDA meetings only |
| 20 | Consensus when evidence is unclear | Where the evidence required remains unclear, a group of innovators, clinicians, scientists and patients could be asked to reach a consensus-based decision. | PL120 | [PAPER] IDEAL-D stage 0, DOI 10.1097/SLA.0000000000004907 |
| 21 | Decision record structure | Evidence-to-decision frameworks close with a summary of judgments, decision options, the decision, a justification, subgroup considerations, implementation considerations, and monitoring and evaluation considerations. | TM112, TM113 | [PAPER] Moberg 2018, DOI 10.1186/s12961-018-0320-2 (full text read; the companion Alonso-Coello 2016 rows TM107 and TM108 are [WF]) |
| 22 | Core components and adaptable aspects | Define the core components to which fidelity is expected and the aspects sites may adapt. | TM117 | [PAPER] StaRI, DOI 10.1136/bmj.i6795 |

How the skill uses an anchor: it may say "a design review must include representatives of the functions concerned with the stage under review (PL1)". It may not say that the person's design review is compliant, that an attendee list is sufficient, or that a handoff was late "under the QMSR". The QMSR sets who reviews; it does not set handoff dates.

Analogies are labeled. Rows 19 to 21 come from FDA meetings, preclinical device evaluation and guideline panels. The skill may offer their structure as a pattern for an internal record ("modeled on the Pre-Sub minutes rule, PL41; not a requirement for internal decisions"), never as an obligation.

## 2. The person's rules (not sourced)

Each item below has no primary source in this pack. The skill asks for the person's rule, writes it back in the person's words, and labels it owner-stated (O). If the person asks for a suggestion, the skill may offer one labeled "proposed" and applies none until confirmed.

- What an integration point is for this team, and which ones are tracked. The old framework's working rule, "a shared channel is not an integration point", is kept as the default question, not as a sourced rule.
- What counts as a completed handoff. The old framework's rule "received by the named receiver, not a message sent" is the default offered; the person confirms or replaces it.
- Due dates, "late", grace periods, and how often an open dependency is looked at again.
- Categories of handoff (for example "clinical evidence" and "copy", as the old framework split them) and which handoffs carry a critical-to-quality factor for a study. ICH E8(R1) defines critical-to-quality factors (CV29); which handoffs carry one is the person's call.
- Who owes each work product, who receives it, who attends a review, who carries out a decision. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title; write "the person the user names for <topic>, or owner not named". Never supply a date, a threshold or a status the person did not give: write "not given" and ask.
- What the receiving team does if a dependency is late (the late path).
- Escalation routes, RACI charts, meeting cadences, service levels between teams.
- Any score, target or threshold for handoff performance.

## 3. Words used in this pack

| Term | Meaning here | Basis |
|---|---|---|
| Integration point | A place where one function hands a named work product to another, and a named decision cannot be made until it arrives | Old framework task DH-01.01.3.1.1; anchors in section 1 |
| Work product | A document, specification, data set, assessment or build that moves; never a meeting or a channel | Old framework |
| Open dependency | A work product asked for and not yet received by the named receiver | Old framework task DH-01.01.3.1.2 |
| Late path | What the receiving function will do if the work product is late | Old framework; the person's content |
| Joint decision | A decision that needed more than one function to agree, with the agreement or disagreement recorded and a named person who carries it out | Old framework task DH-01.01.3.1.3; record structure TM112, PL41 as labeled patterns |
| Received | The person's rule; default offered: received by the named receiver, not sent | Old framework task DH-01.01.3.2.1 |
