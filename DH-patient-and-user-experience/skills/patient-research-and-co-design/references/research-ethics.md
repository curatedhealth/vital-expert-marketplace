# Research ethics, consent, conflicts and payments

Interpretive reference for A1. The rows lay out the questions; the answers are decisions for the person's ethics, legal or compliance owner. The model never states that a study is exempt, that consent is adequate, or that a payment is permitted.

## 1. Does the Common Rule apply? (United States)

| Question | Source says | Row |
|---|---|---|
| Who is covered | 45 CFR 46 applies to human subjects research conducted, supported or otherwise regulated by a federal department or agency that has adopted it. Privately funded product work is not covered by this text unless an institution or agency makes it so. | UX-M-11 |
| Is it research | Research means a systematic investigation designed to develop or contribute to generalizable knowledge. Product-specific co-design may or may not meet this; the source leaves it to the facts. | UX-M-12 |
| Minimal risk | Harm no greater than in daily life or routine examinations or tests. | UX-M-13 |
| Exemption (d)(2) | Research limited to surveys, interviews, tests or observation of public behavior, if one of the listed criteria is met (for example, data de-identified, disclosure would not harm subjects, or limited IRB review). | UX-M-14 |
| Exemption (d)(3) | Benign behavioral interventions with adults, verbal or written responses or recording, if the subject agrees in advance and one of the criteria is met. Benign means brief, harmless, painless, not invasive, no lasting adverse impact, not offensive or embarrassing. | UX-M-15, UX-M-16 |
| Deception | Exemption (d)(3) does not apply where subjects are deceived about the research (conditions apply). | UX-M-17 |
| Children | For research with children, (d)(2) applies only to educational tests or non-participant observation; (d)(2)(iii) never applies; (d)(3) is not listed. | UX-M-18 |
| Secondary use | Secondary research using identifiable health information regulated by HIPAA as health care operations, research or public health can be exempt under (d)(4)(iii). | UX-M-19 |
| Consent elements | 45 CFR 46.116 consent elements were not extracted `[GAP]`. | Not sourced |

How to use it: lay out which row each feature of the plan touches (who funds it, whether the output is meant to generalize, whether children take part, whether sessions are recorded), then hand the determination to the person's ethics owner or IRB. Never write "this is exempt".

## 2. Consent and participant risk in formative work (United Kingdom guidance)

- MHRA's human factors guidance (advisory, UX-UK-14) says participants should, where practicable, give informed consent, and risks and benefits to participants should be considered and documented even in early formative testing (UX-UK-19). It is written for device human factors work; use it as a stated expectation, not a rule for co-design.
- UK research ethics approval routes (HRA, NHS REC) are not in this skill's sources `[GAP]`.
- GDPR and UK GDPR rules for session recordings and notes are not in this skill's sources `[GAP]`. Ask the person's privacy owner.

## 3. Conflicts of interest and independence

| Situation | Source says | Row |
|---|---|---|
| Patients later serving in EU HTA joint work | No financial or other interests in the developer's industrial sector that could affect impartiality; interests must be declared; patients act in an individual capacity. | PE-56, PE-57 |
| Patients as individual experts at EMA | Must sign a declaration of interest and confidentiality undertaking. | PE-45 |
| Contracting a patient organization's representative | [INDUSTRY] EFPIA: written contract in advance and a documented legitimate need. ABPI: contracts with individuals representing a patient organization should be made with the organization and disclosed as payments to it. Codes, not law, and they bind member companies only. | PE-77, PE-81 |

## 4. Paying or giving things to participants

Any payment, gift card, free device, free subscription or other item of value to a patient or carer stops for the person's compliance or legal owner. Lay out these rows; never say an arrangement is permitted or protected.

| Point | Row |
|---|---|
| United States: offering anything of value to a Medicare or state-program beneficiary that the offeror knows or should know is likely to influence the choice of a particular provider, practitioner or supplier is subject to civil money penalties. | CP-US-34 |
| The statute excludes remuneration that promotes access to care and poses a low risk of harm, as designated by regulation; the regulation's tests include being unlikely to skew clinical decisions and not raising safety or quality concerns. | CP-US-36, CP-US-37 |
| Other exceptions: items on equal terms to the general public, or after a good-faith financial-need determination with further conditions. | CP-US-38 |
| A digital health tool given to patients by a device maker has its own safe harbor conditions (in-kind, no cash, recommended by the patient's licensed professional, cap $623 for calendar year 2026, not for patient recruitment). Usually not the shape of a co-design honorarium; named so the owner can rule it out. | CP-US-25 to CP-US-28 |
| NICE offers payment, support and training to its lay members. This is NICE's practice for its own committees, not a rule for companies. | PE-62 |

Whether a co-design honorarium is "remuneration" under these rows is not answered by any source here `[GAP]`; it is the compliance owner's call.

## 5. Identifiable data

The Patient Experience Designer never handles protected health information and never profiles a named individual (expert stop rules, `governance.md`). Session capture uses participant codes; the script's `check` flags emails, phone numbers, long ID numbers, date-of-birth wording and name or address columns. A file with identifiers is not processed until the person removes them.
