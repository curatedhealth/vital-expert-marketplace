# Knowledge: trusted-intake

This file is the single home for this skill's sourced rules, failure patterns, gap
wording and failure modes. Where the same rule or pattern appeared in more than one
earlier file, one copy is kept.

## Contents

- Part 1: Rules (sourced, with scope and confirmation status)
- Part 2: Failure patterns (before and after)
- Part 3: Gap rules (shared wording, with this skill's cases)
- Part 4: Failure modes (detection questions)

## Part 1: Rules

Intake enforces no rule on the person's work. These sources explain why a missing market,
use, product status or data kind can change the answer, and so why the question is worth
asking. Each names its primary source, date and how it was confirmed. A rule marked
`[CHECK]` has not been read in the primary document and is described as good practice,
not cited as a requirement (TR-H8).

Last reviewed: 20 October 2026.

| Id | What it means for intake | Primary source | Jurisdiction | Status |
|---|---|---|---|---|
| I1 | "Advertising of medicinal products" includes any information, canvassing or inducement designed to promote prescription, supply, sale or consumption, and in particular advertising to the general public, advertising to people qualified to prescribe or supply, rep visits and samples. The reader and the purpose decide whether a piece can fall under advertising rules, so both are worth knowing. | Directive 2001/83/EC, Article 86(1) | EU | Confirmed 20 October 2026 from the official copy at legislation.gov.uk (version as at 26 July 2019, no later amendments applied there). The current EUR-Lex consolidated text was not read `[CHECK]`. |
| I2 | Not covered by the advertising title: correspondence, possibly with non-promotional material, needed to answer a specific question about a particular medicinal product; and information on human health or diseases with no reference, even indirect, to medicinal products. This is why "did the doctor ask this themselves?" and "is a product named?" are worth asking. | Directive 2001/83/EC, Article 86(2) | EU | Confirmed 20 October 2026, same source as I1. |
| I3 | Member States prohibit advertising to the general public of medicinal products available on medical prescription only. Whether the reader is a patient or the public, and whether the product is prescription-only, can change what may be written. | Directive 2001/83/EC, Article 88(1)(a) | EU | Confirmed 20 October 2026, same source as I1. |
| I4 | Medical devices fall into classes I, IIa, IIb and III (class I with sterile, measuring and reusable surgical instrument subcategories); the rules are in Article 51 and Annex VIII of the regulation, and the manufacturer applies them. Intake records the class only as the person states it; it never classifies. | Regulation (EU) 2017/745, Article 51 and Annex VIII, as summarized by the European Commission UDI Helpdesk page "Medical device classification" (page dated 19 May 2026) | EU | Confirmed 20 October 2026 from the European Commission page. The regulation text itself was not read `[CHECK]`. US device classes (I, II, III) `[CHECK]`: intended source FDA device classification pages. |
| I5 | In the US, firms may share scientific information on unapproved uses with health care providers under defined conditions, separate from promotion. Scientific exchange and promotion are handled differently, so the use is worth asking for US doctor-facing work. | FDA guidance "Communications From Firms to Health Care Providers Regarding Scientific Information on Unapproved Uses of Approved/Cleared Medical Products: Questions and Answers", final guidance reported as issued January 2025 | US | `[CHECK]`: title and date taken from law-firm summaries (Ropes & Gray, Hall Render, January 2025), not from the FDA document. Apply as good practice only. |
| I6 | Switzerland and the UK have their own advertising rules for medicinal products, so "EU rules" cannot be assumed for a Swiss or UK reader. | Switzerland: Therapeutic Products Act and the Ordinance on the Advertising of Medicinal Products. UK: Human Medicines Regulations 2012, Part 14 | Switzerland, UK | Switzerland: the advertising ordinance (AWV, SR 812.212.5) read 9 November 2026 on lexfind.ch, a mirror of the official consolidated text (Stand 1 January 2019); fedlex.admin.ch could not be read. UK: `[CHECK]`, Part 14 not read. Used only to justify asking the market, never to state a rule. |
| I7 | Processing of data concerning health, genetic data and other special categories is prohibited unless an exception applies. Patient or health information about an identifiable person is therefore the most sensitive kind of input, and intake never asks for more of it. | Regulation (EU) 2016/679 (GDPR), Article 9(1) | EU (UK has its own version) | Confirmed 20 October 2026 from the official copy at legislation.gov.uk (as adopted by the EU). Exceptions in Article 9(2) not summarized here. |
| I8 | Providers and deployers of AI systems are to take measures to support the development of AI literacy of their staff; no specific level is required of any individual, and the Commission and Member States support them. Companies are building AI use policies partly for this reason, which is why intake asks what the person's policy says rather than assuming there is none. | Regulation (EU) 2024/1689 (AI Act), Article 4, as replaced by Regulation (EU) 2026/1744 of 8 July 2026 | EU | Article 4 as replaced by Regulation (EU) 2026/1744 read 9 November 2026 in the Official Journal text on EUR-Lex. Agrees with `responsible-inputs` I7. Described as context only. |

### How to use these rules

- In what the person reads, never cite these. Give the reason in plain words: "Which
  country? The rules on what can be said to doctors differ between countries."
- Never tell the person that their piece is or is not advertising, promotion or allowed.
  The reason for the question is enough; the review process decides.
- Never extend a rule outside its jurisdiction. I1 to I3 are EU law; for a Swiss, UK or US
  reader they are not the rule.

## Part 2: Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; no real product, company or person.

Pattern ids are for this file only. In what the person reads, never show them (TR-H13).

### Asking too much

**C1 The form.** Eight numbered fields before any help.
Why: people stop using a tool that interrogates them for a two-line email. It also hides
the one question that matters.
Before: "Please provide: 1. audience 2. market 3. product status 4. use 5. format 6. length
7. sources 8. AI policy."
After: "Which country is the doctor in? The rules on what can go in a doctor email differ
by market." (TR-H12)

**C2 Asking what is already there.** "Who is this for?" after the person wrote "for the
board".
Why: it shows the request was not read.
After: take "board" as the reader, set leadership stakes, ask nothing about it. (TR-H7)

**C3 The question that changes nothing.** "Would you like a formal or friendly tone?" for
internal meeting notes.
Why: the answer would not change what is permitted, true or useful. It is a style
question (TR-H9).
After: draft; the person can adjust tone.

**C4 Asking again next turn.** The person named Germany two messages ago; the next skill
asks for the market.
Why: the card exists so nobody asks twice.
After: read the card; ask only if the person changed the work. (TR-H7)

### Asking too little

**C5 The silent market.** A doctor email drafted for "the market" with US-style wording
because no country was named.
Why: what may be said to doctors differs by market (rules I1, I5, I6). A draft for the
wrong market has to be thrown away.
Before: drafting at once, with market-specific wording filled in.
After: the draft with every market-specific statement as a gap, and in the same reply:
"Which country will the doctors be in, and can you share the label there?" (TR-H7)

**C6 The relaxed assumption.** Unsure whether a deck goes to a payer, intake assumes
"internal" and the light pass runs.
Why: the important failures slip through at the light depth.
After: "Assuming this may go outside the company, I've kept every claim to your material.
Tell me if it's internal only." (TR-H12)

**C7 Questions instead of a draft.** The person asks for a one-line headline and gets
three questions and a promise to write it later.
Why: the person has nothing to react to, and a second round trip for a short piece of
work.
After: the draft with each missing detail as a gap, and at most one combined question
under it. Wait with the question alone only under a stop rule. (TR-H7)

### Deciding what is not yours to decide

**C8 Approving the tool.** "Yes, ChatGPT Enterprise is fine for client data."
Why: only the company's AI use policy and its owner can say that. A wrong yes exposes the
person and the client.
After: "What does your company's AI use policy say about client material in this
assistant? If you're not sure, your AI policy owner can tell you." (TR-H3, TR-H11)

**C9 Turning a statement into an approval.** The person says "my manager said it's fine";
the card says "approved".
Why: the record now claims something nobody established.
After: the card says "person states their manager said it is fine". (TR-H1, TR-H5)

**C10 Classifying the work.** "This is non-promotional, so no review is needed."
Why: whether something is promotional is decided by the company's review process, not
the assistant.
After: record the use as the person states it, and name the review process it goes to.
(TR-H3, TR-H11)

### Tone and content of questions

**C11 The lecture.** Three paragraphs on data protection law before asking about the
policy.
Why: it reads as blame and buries the question.
After: one phrase naming the kind of data, one question, one way to proceed. (TR-H13)

**C12 Jargon in the question.** "Is this an Article 86(2) reactive response or
promotional material under your MLR SOP?"
Why: daily users should not need the rulebook to answer.
After: "Did the doctor ask this question themselves, or is this something we're sending
out?" (TR-H13)

**C13 Asking for patient details.** "Can you share the patient's age and history so I can
tailor the reply?"
Why: it pulls the most sensitive data into the assistant for no need (rule I7).
After: work from the question as asked; never ask for identifying details. (TR-H6)

## Part 3: Gap rules

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/knowledge.md` (Part 2).

Same format and classes as every TRUSTED skill:
`[GAP: <class>; <what is missing>; <what would close it>]`

Gaps on the context card are for other skills. The person never sees gap syntax from
intake; they see a plain question or a one-line assumption (TR-H13).

| Class | Typical case in this skill |
|---|---|
| `not supplied` | A field the request does not give and that does not change this answer, left unknown on the card |
| `needs a decision` | Whether this input may go into this assistant, under the company AI use policy; whether a piece is promotional (the review process decides) |
| `conflicting` | The person says "internal only" but the request names a payer; two markets named for one piece |
| `out of date or unclear date` | A label or policy the person supplied with no date, when the version could change the answer |
| `not checkable here` | Product approval status in a market, or what the company policy says, when no companion can read it and only the person's word is available |

Wording rules:

- On the card, a field that was asked and not yet answered is `asked`, not a gap. It
  becomes a gap only if the person moves on without answering.
- Never fill a gap with the likely answer ("probably Germany").
- An assumption is not a gap. It is a stated choice on the card, marked `assumed`, with
  the one line the person saw.

## Part 4: Failure modes

Skill-specific rows for this skill. FM-08 is shared by every skill and covers Prove honesty.

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-TI-01 | Invented market/use | Were market, use, or product status assumed silently or in the relaxed direction? | Context | TRUSTED intake | VERIFIED practice |
| FM-TI-02 | Skipped changing questions | Were questions that change the draft omitted? | Intake | TRUSTED intake | [CHECK] |
| FM-TI-03 | Intake as clearance | Did intake claim letters already passed? | Scope | TR-H3 | VERIFIED practice |
| FM-08 | Hand-check result treated as world-truth | Is a hand-check result described as "true in the world"? | Prove honesty | TR-H3 | VERIFIED |
