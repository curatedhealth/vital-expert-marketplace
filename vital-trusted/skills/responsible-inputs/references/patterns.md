# Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; no real product, study, company or person.

## Contents

- Confidentiality C1–C9
- Intellectual property P1–P7
- Tone T1–T4

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

## Confidentiality

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
tool. (concept §5, Ethical stays concrete)

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

## Intellectual property

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

## Tone

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
