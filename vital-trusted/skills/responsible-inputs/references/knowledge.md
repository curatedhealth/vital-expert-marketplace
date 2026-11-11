# Knowledge: responsible-inputs

This file is the single home for this skill's sourced rules, failure patterns, gap
wording and failure modes. Where the same rule or pattern appeared in more than one
earlier file, one copy is kept.

## Contents

- Part 1: Rules (sourced, with scope and confirmation status)
- Part 2: Failure patterns (before and after)
- Part 3: Gap rules (shared wording, with this skill's cases)
- Part 4: Failure modes (detection questions)

## Part 1: Rules

Each rule names its primary source, the date and how it was confirmed. A rule marked
`[CHECK]` has not been confirmed against the primary document and is applied as good
practice, not cited as a requirement (TR-H8). Jurisdiction is stated for each.

Last reviewed: 20 October 2026.

### The rule that governs first

| Id | Rule | Source | Status |
|---|---|---|---|
| I11 | Whether a tool may be used for a kind of material is decided by the person's company AI use policy and the owners named in it, then by the company's data, privacy, legal and compliance functions. | The person's own company policy (rule source: the person's company AI policy, then sourced public frameworks). | Owner-stated design rule. The policy is never assumed; it is asked for. |

The public rules below explain why a question matters. They are never used to answer the
policy question on the company's behalf.

### Personal and patient data

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| I1 | Processing of special categories of personal data, including "data concerning health", genetic data and biometric data for uniquely identifying a person, is prohibited unless an exception in Article 9(2) applies (for example explicit consent). | Regulation (EU) 2016/679 (GDPR) of 27 April 2016, Article 9(1) and (2), Official Journal L 119, 4 May 2016 (original text); applies from 25 May 2018 (Article 99(2)). | EU and EEA | Confirmed 20 October 2026 from the Official Journal text (Publications Office). Later amending acts, if any, `[CHECK]`. |
| I2 | Pseudonymized data that could be attributed to a person with additional information is still information on an identifiable person. Data protection principles do not apply to anonymous information, judged by "all the means reasonably likely to be used" to identify someone. | GDPR Recital 26; Article 4(1) (personal data) and 4(5) (pseudonymization). Same source as I1. | EU and EEA | Confirmed 20 October 2026. Used here so that removing names is never described as making data anonymous. |
| I3 | "Data concerning health" means personal data related to the physical or mental health of a person, including the provision of health care services, which reveal information about their health status. | GDPR Article 4(15). Same source as I1. | EU and EEA | Confirmed 20 October 2026. |
| I4 | Sensitive personal data includes data relating to health, genetic data and biometric data that uniquely identifies a person. | Swiss Federal Act on Data Protection (FADP) of 25 September 2020, SR 235.1, Article 5(c); consolidated version of 7 July 2025, Fedlex. | Switzerland | Confirmed 20 October 2026 from the Fedlex English text, which states that English is not an official language and the translation has no legal force. The German, French and Italian texts govern. |
| I5 | Personal data may be disclosed abroad if the Federal Council has found the destination's protection adequate or, failing that, if appropriate safeguards listed in the Act apply. | FADP Article 16(1) and (2), same source as I4. | Switzerland | Confirmed 20 October 2026. This skill does not assess where a tool processes data or whether a transfer is permitted; that is the data protection function's call. |
| I6 | Health information is de-identified only by expert determination or by removing 18 listed identifiers (names; locations smaller than a State; all date elements except year, and ages over 89; phone and fax numbers; email; Social Security, medical record, health plan, account and license numbers; vehicle and device identifiers; URLs; IP addresses; biometric identifiers; full-face photographs; any other unique identifying number, characteristic or code), with no actual knowledge that what remains could identify the person. | 45 CFR 164.514(a) and (b), eCFR, up to date as of 16 October 2026. | US; the rule is written for HIPAA covered entities. Whether it reaches the person's company (for example as a business associate) `[CHECK]` and is for the privacy function. | Confirmed 20 October 2026 from eCFR. Outside its scope, the identifier list is used only as a practical checklist of what to take out, never as a claim that data is de-identified. |

UK GDPR and the UK Data Protection Act 2018: `[CHECK]`, not yet read. Treat as good
practice in the same direction as I1 to I3 until confirmed.

### AI literacy

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| I7 | AI literacy. Article 4 of the AI Act, as replaced by Regulation (EU) 2026/1744 of 8 July 2026 (published in the Official Journal on 24 July 2026, in force 27 July 2026), paragraph 1: "Providers and deployers of AI systems shall take measures to support the development of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training and the context the AI systems are to be used in, and considering the persons or groups of persons on whom the AI systems are to be used. This obligation does not require providers or deployers to guarantee any specific level of AI literacy of any individual." Paragraph 2: the Commission and the Member States "shall support and facilitate the efforts of providers and deployers of AI systems, in particular SMEs". The duty stays with providers and deployers; it did not move to the authorities. The original 2024 wording asked providers and deployers to "take measures to ensure, to their best extent, a sufficient level of AI literacy" and applied from 2 February 2025 (Article 113) `[CHECK]`. | Regulation (EU) 2024/1689 (AI Act), Article 4, as replaced by Regulation (EU) 2026/1744 of 8 July 2026 (OJ text on EUR-Lex, ELI http://data.europa.eu/eli/reg/2026/1744/oj); Article 113 for the original application date | EU | Article 4 as replaced read 9 November 2026 in the Official Journal text on EUR-Lex; the entry-into-force date rests on the EUR-Lex metadata. `[CHECK]` applies only to the original 2024 wording and its application date, which were not re-read. The same row appears in rules.md, knowledge.md and method-standards.md, and agrees with `trusted-intake` I8. Any duty sits with the company: this skill supports a person's habits; it does not satisfy or evidence an obligation. |

### Price-sensitive information

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| I8 | Inside information is information of a precise nature, not made public, relating to an issuer or its financial instruments, which would be likely to have a significant effect on prices if made public. Unlawful disclosure arises where a person with inside information discloses it to another person, except in the normal exercise of employment, profession or duties. | Regulation (EU) No 596/2014 (Market Abuse Regulation), Article 7(1)(a) and Article 10(1); Regulation of 16 April 2014, Official Journal L 173, 12 June 2014 (original text). | EU, for issuers with instruments on EU trading venues | Definitions confirmed 20 October 2026 from the Official Journal text. Later amendments `[CHECK]`. Swiss and US equivalents `[CHECK]`. Whether information is inside information, and whether a tool use is a disclosure, is for legal or compliance; this skill only names the category. |

### Intellectual property

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| I9 | The copyright owner has the exclusive rights to reproduce the work and to prepare derivative works based on it (section 106), subject to limits including fair use (section 107), which is decided on four factors: purpose and character of the use, including whether commercial; nature of the work; amount and substantiality used; effect on the market for the work. | US Copyright Act, 17 U.S.C. 106 and 107, as published by the US Copyright Office (Title 17, chapter 1). | US | Confirmed 20 October 2026 from the Copyright Office page. The page shows no currency date `[CHECK]`. Fair use is a legal judgment; this skill never makes it. |
| I10 | Reproduction rights and the quotation exception in the EU; equivalents in Switzerland and the UK. | Intended: Directive 2001/29/EC, Articles 2 and 5(3)(d); Swiss Copyright Act (SR 231.1); UK Copyright, Designs and Patents Act 1988. | EU, Switzerland, UK | `[CHECK]`: not read. Applied as good practice only: summarize in new words, quote briefly with attribution, ask the licensing process before reproducing. |
| I12 | Licensed content and data are used only as the license terms allow; some publisher and data licenses address use in AI tools. | The specific license the company holds. | Any | `[CHECK]`: no license read. Good practice: ask, do not assume the terms. |

### Unpublished study data and commercial confidentiality

No single public rule decides this. Confidentiality comes from the company's own policies,
study contracts and confidentiality agreements, none of which this skill can read. The
skill names the category, asks the policy question and offers safer routes. Where the
material also holds patient data (I1 to I6) or could be price-sensitive (I8), those rules
explain why the question matters.

### How to use these rules in output

- In what the person reads, name the reason in plain words ("health details about a
  named patient are treated as especially sensitive under data protection law"). Cite
  the article only if asked.
- Never extend a rule beyond its jurisdiction. I6 is a US rule; it does not make data
  anonymous under I2.
- A `[CHECK]` rule is described as good practice, never as a requirement.

## Part 2: Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; no real product, study, company or person.

### Contents

- Confidentiality C1–C9
- Intellectual property P1–P7
- Tone T1–T4

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

### Confidentiality

**C1 The approval verdict.** The assistant says the tool is fine, or not allowed.
Why: only the company's policy can say; a wrong "fine" exposes the person, a wrong "not
allowed" blocks legitimate work.
Before: "ChatGPT Enterprise is approved for confidential data, go ahead."
After: "Whether this tool is allowed for unpublished study data is set by your AI use
policy. If it is, I can work with it; if you are not sure, here is a safer route." (TR-H3, TR-H11)

**C2 The data-handling claim.** The assistant states what the tool does with pasted data.
Why: terms differ by product, plan and contract, and change; the assistant cannot see
the company's agreement.
Before: "Don't worry, this tool doesn't train on your data."
After: "What happens to pasted material is in your policy or the tool's terms for your
account; I can't confirm it from here." (TR-H1)

**C3 Names removed, called anonymous.** Initials and a birth date left in; the text
called "anonymized".
Why: data that can still be linked to a person is still personal data (I2); a US
de-identification standard has its own conditions (I6).
Before: "I've anonymized the notes (Mr K., 67, admitted 3 March)."
After: "I've taken out the name, age and admission date. Other details could still point
to the person, so treat this as reduced, not anonymous." (TR-H1)

**C4 The echo.** The reply repeats the patient's details back while warning about them.
Why: it spreads what should stay contained, into the reply and any copy of it.
Before: "Note that Mrs Jane D., 54, with relapsed disease at Hospital X, is identifiable."
After: "These notes include details about an identifiable patient. I've left them out of
the summary." (TR-H1, governance stop rule)

**C5 All or nothing.** The only options offered are "paste it all" or "don't use AI".
Why: people will paste it anyway; the job usually needs far less.
After: offer the minimum extract, removed identifiers, the public version or an approved
tool.

**C6 The incident judgment.** After material is already pasted, the assistant decides
whether it is a breach or must be reported.
Why: that is a legal and privacy decision under the company's procedure.
After: "If your policy does not cover this, your privacy or data protection function
will say what, if anything, needs to happen next." (TR-H6, TR-H11)

**C7 The price-sensitive blind spot.** Undisclosed topline results of a listed company
handled like any other internal note.
Why: in the EU, undisclosed precise information likely to move a price is inside
information (I8); its handling is set by legal and compliance.
After: one line naming the category and the question for compliance; no judgment of
whether it is inside information. (TR-H11)

**C8 The silent assumption about the tool.** The assistant assumes which tool, plan or
account the person means.
After: ask which tool and whether it is the company's approved version, if it changes
the answer. (TR-H7)

**C9 The reassurance that it is "just internal".** Internal use treated as making any
input acceptable.
Why: the question is what went into the tool, not only who reads the result.
After: keep the depth light for internal results, but still ask the policy question for
sensitive inputs. (TR-H12)

### Intellectual property

**P1 The full rewrite.** A whole paid article rewritten paragraph by paragraph for an
external newsletter.
Why: close rework of a whole work engages the owner's rights (I9; EU and others
`[CHECK]` I10), whatever the wording.
After: a short summary in new words with the citation and a link; short quotations
attributed. (TR-H11)

**P2 Attribution stripped.** The source's figure or wording presented without credit.
After: cite the source next to the figure or quotation. (TR-H1)

**P3 The subscription assumption.** "We subscribe, so we can use it anywhere."
Why: subscriptions and data licenses set their own limits on audience and use, and some
address AI tools (I12 `[CHECK]`).
After: "Your licensing team can confirm whether your subscription covers this use."

**P4 The fair-use verdict.** The assistant says a use is fair use or allowed.
After: name the question; the legal or licensing function decides. (TR-H3)

**P5 Client material in another client's work.** An agency or consultancy reuses one
client's deck in work for another.
After: flag that the client agreement decides; offer to work only from public or the
current client's own material. (TR-H11)

**P6 Guideline reproduced wholesale.** A full society guideline pasted and reproduced as
an internal reference document.
After: summarize the recommendations needed, cite the guideline and link to it. (TR-H11)

**P7 Agency creative reused.** Agency concepts or images reused outside the scope they
were licensed for.
After: ask the brand or legal team which uses the agreement covers.

### Tone

**T1 The lecture.** Three paragraphs on data protection before a one-line answer.
After: one line, one question, one route. (TR-H12, TR-H13)

**T2 The flag on public material.** A note about confidentiality on a published press
release.
After: no note; do the work. (TR-H12)

**T3 Rule codes in the reply.** "Under GDPR Art. 9(1) and Recital 26…" to a brand
manager.
After: "Health details about a named patient are treated as especially sensitive." (TR-H13)

**T4 Moralizing.** "It would be irresponsible to…"
After: state the question and the route without judging the person.

## Part 3: Gap rules

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/knowledge.md` (Part 2, "Where the marker belongs").

Same format and classes as every TRUSTED skill:
`[GAP: <class>; <what is missing>; <what would close it>]`

Gaps in this skill appear mostly in check lines and notes, not inside the person's
document. In what the person reads, prefer the plain question ("Does your AI use policy
allow this tool for unpublished study data?") over raw gap syntax (TR-H13).

| Class | Typical case in this skill |
|---|---|
| `needs a decision` | Whether this tool is allowed for this kind of material; whether a license covers this use; whether information is price-sensitive; what to do after sensitive material was pasted |
| `not supplied` | Which tool or account; where the result will go; the license terms; the policy text the person refers to |
| `not checkable here` | Whether the tool's terms or location meet the company's requirements, with no AI-policy companion and no terms supplied |
| `conflicting` | The person says the material is public, but it carries a "confidential" or "draft" marking |
| `out of date or unclear date` | A policy or approved-tool list quoted with no version or date |

Wording rules:

- Name the kind of material and the decision, not the person: "permission to reproduce
  the full article", not "user may be infringing".
- Never hint at the answer inside the gap ("probably approved", "likely fair use").
- Never write a gap that repeats a personal identifier.

## Part 4: Failure modes

Skill-specific rows for this skill. FM-08 is shared by every skill and covers Prove honesty.

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-RI-01 | Public derivative of confidential | Was unpublished partner/CSR content pushed to a public pack? | Inputs | TRUSTED responsible-inputs | VERIFIED practice |
| FM-RI-02 | AI-use policy skipped | Was sensitive input pasted to a public tool without policy check? | AI policy | TRUSTED responsible-inputs | [CHECK] |
| FM-RI-03 | PHI assumed anonymized | Was identifiable data treated as fine without confirmation? | Privacy | TRUSTED responsible-inputs | PARTIAL |
| FM-08 | Hand-check result treated as world-truth | Is a hand-check result described as "true in the world"? | Prove honesty | TR-H3 | VERIFIED |
