# Primary rules behind this skill

Each rule names its primary source, the date and how it was confirmed. A rule marked
`[CHECK]` has not been confirmed against the primary document and is applied as good
practice, not cited as a requirement (TR-H8). Jurisdiction is stated for each.

Last reviewed: 20 October 2026.

## The rule that governs first

| Id | Rule | Source | Status |
|---|---|---|---|
| I11 | Whether a tool may be used for a kind of material is decided by the person's company AI use policy and the owners named in it, then by the company's data, privacy, legal and compliance functions. | The person's own company policy (concept §5 and §8.3: "rule source: the user's company AI policy, then sourced public frameworks"). | Owner-stated design rule. The policy is never assumed; it is asked for. |

The public rules below explain why a question matters. They are never used to answer the
policy question on the company's behalf.

## Personal and patient data

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| I1 | Processing of special categories of personal data, including "data concerning health", genetic data and biometric data for uniquely identifying a person, is prohibited unless an exception in Article 9(2) applies (for example explicit consent). | Regulation (EU) 2016/679 (GDPR) of 27 April 2016, Article 9(1) and (2), Official Journal L 119, 4 May 2016 (original text); applies from 25 May 2018 (Article 99(2)). | EU and EEA | Confirmed 20 October 2026 from the Official Journal text (Publications Office). Later amending acts, if any, `[CHECK]`. |
| I2 | Pseudonymised data that could be attributed to a person with additional information is still information on an identifiable person. Data protection principles do not apply to anonymous information, judged by "all the means reasonably likely to be used" to identify someone. | GDPR Recital 26; Article 4(1) (personal data) and 4(5) (pseudonymisation). Same source as I1. | EU and EEA | Confirmed 20 October 2026. Used here so that removing names is never described as making data anonymous. |
| I3 | "Data concerning health" means personal data related to the physical or mental health of a person, including the provision of health care services, which reveal information about their health status. | GDPR Article 4(15). Same source as I1. | EU and EEA | Confirmed 20 October 2026. |
| I4 | Sensitive personal data includes data relating to health, genetic data and biometric data that uniquely identifies a person. | Swiss Federal Act on Data Protection (FADP) of 25 September 2020, SR 235.1, Article 5(c); consolidated version of 7 July 2025, Fedlex. | Switzerland | Confirmed 20 October 2026 from the Fedlex English text, which states that English is not an official language and the translation has no legal force. The German, French and Italian texts govern. |
| I5 | Personal data may be disclosed abroad if the Federal Council has found the destination's protection adequate or, failing that, if appropriate safeguards listed in the Act apply. | FADP Article 16(1) and (2), same source as I4. | Switzerland | Confirmed 20 October 2026. This skill does not assess where a tool processes data or whether a transfer is permitted; that is the data protection function's call. |
| I6 | Health information is de-identified only by expert determination or by removing 18 listed identifiers (names; locations smaller than a State; all date elements except year, and ages over 89; phone and fax numbers; email; Social Security, medical record, health plan, account and license numbers; vehicle and device identifiers; URLs; IP addresses; biometric identifiers; full-face photographs; any other unique identifying number, characteristic or code), with no actual knowledge that what remains could identify the person. | 45 CFR 164.514(a) and (b), eCFR, up to date as of 16 October 2026. | US; the rule is written for HIPAA covered entities. Whether it reaches the person's company (for example as a business associate) `[CHECK]` and is for the privacy function. | Confirmed 20 October 2026 from eCFR. Outside its scope, the identifier list is used only as a practical checklist of what to take out, never as a claim that data is de-identified. |

UK GDPR and the UK Data Protection Act 2018: `[CHECK]`, not yet read. Treat as good
practice in the same direction as I1 to I3 until confirmed.

## AI literacy

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| I7 | Providers and deployers of AI systems shall take measures to support the development of AI literacy of their staff and others operating AI on their behalf; the obligation does not require any specific level of AI literacy of any individual. Chapter I, which holds Article 4, applies from 2 February 2025. | Regulation (EU) 2024/1689 (AI Act), Article 4, as replaced by Regulation (EU) 2026/1744 of 8 July 2026 (Digital Omnibus on AI); Article 113(a). Consolidated text of 27 July 2026, Publications Office. | EU | Confirmed 20 October 2026. The obligation sits with the company. This skill supports a person's habits; it does not satisfy or evidence the company's obligation. |

## Price-sensitive information

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| I8 | Inside information is information of a precise nature, not made public, relating to an issuer or its financial instruments, which would be likely to have a significant effect on prices if made public. Unlawful disclosure arises where a person with inside information discloses it to another person, except in the normal exercise of employment, profession or duties. | Regulation (EU) No 596/2014 (Market Abuse Regulation), Article 7(1)(a) and Article 10(1); Regulation of 16 April 2014, Official Journal L 173, 12 June 2014 (original text). | EU, for issuers with instruments on EU trading venues | Definitions confirmed 20 October 2026 from the Official Journal text. Later amendments `[CHECK]`. Swiss and US equivalents `[CHECK]`. Whether information is inside information, and whether a tool use is a disclosure, is for legal or compliance; this skill only names the category. |

## Intellectual property

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| I9 | The copyright owner has the exclusive rights to reproduce the work and to prepare derivative works based on it (section 106), subject to limits including fair use (section 107), which is decided on four factors: purpose and character of the use, including whether commercial; nature of the work; amount and substantiality used; effect on the market for the work. | US Copyright Act, 17 U.S.C. 106 and 107, as published by the US Copyright Office (Title 17, chapter 1). | US | Confirmed 20 October 2026 from the Copyright Office page. The page shows no currency date `[CHECK]`. Fair use is a legal judgment; this skill never makes it. |
| I10 | Reproduction rights and the quotation exception in the EU; equivalents in Switzerland and the UK. | Intended: Directive 2001/29/EC, Articles 2 and 5(3)(d); Swiss Copyright Act (SR 231.1); UK Copyright, Designs and Patents Act 1988. | EU, Switzerland, UK | `[CHECK]`: not read. Applied as good practice only: summarize in new words, quote briefly with attribution, ask the licensing process before reproducing. |
| I12 | Licensed content and data are used only as the license terms allow; some publisher and data licenses address use in AI tools. | The specific license the company holds. | Any | `[CHECK]`: no license read. Good practice: ask, do not assume the terms. |

## Unpublished study data and commercial confidentiality

No single public rule decides this. Confidentiality comes from the company's own policies,
study contracts and confidentiality agreements, none of which this skill can read. The
skill names the category, asks the policy question and offers safer routes. Where the
material also holds patient data (I1 to I6) or could be price-sensitive (I8), those rules
explain why the question matters.

## How to use these rules in output

- In what the person reads, name the reason in plain words ("health details about a
  named patient are treated as especially sensitive under data protection law"). Cite
  the article only if asked.
- Never extend a rule beyond its jurisdiction. I6 is a US rule; it does not make data
  anonymous under I2.
- A `[CHECK]` rule is described as good practice, never as a requirement.
