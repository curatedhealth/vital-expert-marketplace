# Primary rules behind this skill

Each rule names its primary source, the date and how it was confirmed. A rule marked
`[CHECK]` has not been confirmed against the primary document and is applied as good
practice, not cited as a requirement (TR-H8).

Most of these rules govern regulated records (GxP data, signed electronic records,
journal submissions). Everyday work such as a board update or a payer deck is usually
outside their legal scope. This skill borrows their practice, not their obligation, and
never tells a person that a rule applies to their document unless its scope plainly
covers it.

Last reviewed: 20 October 2026.

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| R1 | Data should be attributable to the person generating it; records should identify both the person performing a task and the person completing the record; processing should include attribution to who performed the activity. | MHRA, "GXP Data Integrity Guidance and Definitions", Revision 1, March 2018, sections 3.10 (ALCOA), 5.2 (scribes), 6.1 (data), 6.9 (data processing). Official copy on assets.publishing.service.gov.uk. | UK, GxP data and records | Confirmed from the MHRA PDF on 20 October 2026. Applied here as practice for attributing every record entry. |
| R2 | An audit trail allows reconstruction of the "who, what, when and why" of an action; changes are associated with the persons making them and dated. | Same MHRA document, section 6.13 (audit trail). | UK, GxP computerized systems | Confirmed 20 October 2026. Applied here as practice: the record says who did what, in which order, and when where dates were given. |
| R3 | Signed electronic records show the printed name of the signer, the date and time of signing, and the meaning of the signature (such as review, approval, responsibility or authorship), in any human-readable form of the record. | US Code of Federal Regulations, 21 CFR 11.50 (a) and (b), signature manifestations. eCFR, up to date as of 15 October 2026. | US, electronic records and signatures under FDA predicate rules | Confirmed from eCFR on 20 October 2026. Applied here as practice: a status above "draft" carries a name, a date and its meaning. |
| R4 | Authors who use AI-assisted technologies should disclose it and describe how they used it, in the cover letter and the submitted work; AI tools are not listed as authors because they cannot be responsible for the accuracy, integrity and originality of the work; humans are responsible for submitted material that used AI. | International Committee of Medical Journal Editors (ICMJE), Recommendations, section "Artificial Intelligence: A. Use of AI by Authors", icmje.org. | Manuscripts submitted to journals that follow ICMJE | Confirmed from icmje.org on 20 October 2026. The page shows no revision date `[CHECK: revision date of the AI section]`. Used here for "what the AI did" and for "a human stands behind it". Whether a disclosure is required in a given deliverable is responsible-use. |
| R5 | Deployers of an AI system that generates or manipulates text published to inform the public on matters of public interest disclose that the text was artificially generated or manipulated, unless it has undergone human review or editorial control and a person holds editorial responsibility. | Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 50(4); application date per Article 113. | EU | Confirmed 20 October 2026 from the Commission's official copy of the text consolidated at 27 July 2026, read during the responsible-use build (see that skill's rule U6); applies from 2 August 2026. Not applied by this skill. Listed so the record captures the facts (AI involvement, named human review) that responsible-use needs to decide. |

## How to use these rules in output

- When the person asks why the record or status matters, explain the practice in plain
  words: "A reader should be able to tell who did what and who stands behind it."
- Cite a rule by name only when its scope covers the work (for example R4 for a journal
  manuscript, R3 for a signed electronic record in a GxP system) and the person asks.
- Never extend a rule beyond its scope. R1 to R3 do not make a board update a GxP
  record. R5 is not applied by this skill; responsible-use owns the disclosure question.
