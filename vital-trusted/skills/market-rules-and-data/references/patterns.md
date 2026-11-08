# Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; "Lumivra", "Zelorastat" and every person named
are fictional.

## Contents

- Jurisdiction J1 to J8
- Required statements S1 to S8
- Personal data in the output D1 to D9

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

## Jurisdiction

**J1 The wrong regulator's approval.** A deck for German doctors says "FDA-approved".
Why: the reader's market has its own authorization; another country's approval tells
them nothing about use in theirs and can suggest a status the product does not have
there.
Before: "Zelorastat, FDA-approved for moderate to severe disease."
After: "Zelorastat [GAP: not supplied — approval status and indication in Germany — the
German or EU summary of product characteristics]." (TR-H1, TR-H7; M1, M5)

**J2 US label headings in an EU or Swiss piece.** "Indications and Usage", "Important
Safety Information", "Boxed Warning", "see full Prescribing Information" in material for
Europe.
Why: these name US label sections; the reader looks for the SmPC or the Swiss product
information. In the UK, "prescribing information" means something narrower (M6).
After: use the name of the label document the person or the label supplies; otherwise a
placeholder. (TR-H7; M6, M10)

**J3 One approval read as everywhere.** "Approved for adults with condition Y" in a
global deck, when the supplied label is from one country.
After: "Approved in [market] for adults with condition Y, per the label you supplied."
Other markets: ask. (TR-H1)

**J4 Professional material that reaches the public.** A post about a prescription
medicine "for HCPs" on an open social account or web page.
Why: in the EU, the UK and Switzerland, advertising prescription medicines to the
public is prohibited or restricted (M2, M8, M12). An audience line does not stop the
public reading it.
After: "This post is about a prescription medicine and the account is public. Where it
can be posted is a question for your promotional review process." (TR-H11)

**J5 Another market's reporting route.** A Swiss email ends with the UK Yellow Card line.
Why: the reader is sent to the wrong system; the line is a UK code requirement (M7).
After: `[Side-effect reporting statement for Switzerland, if your review process
expects one]`. (M13, M19)

**J6 The silent market.** The assistant drafts a doctor email with no market and writes
to US conventions by default.
After: ask "Which country?" before the first product sentence. (TR-H7)

**J7 The remembered rule.** "In Switzerland you must include the full SmPC." stated from
memory.
After: use only the rules read in `references/rules.md`; otherwise "your review process
will confirm what this market expects". (TR-H8)

**J8 US consumer conventions as a rule abroad.** "Regulations require absolute figures
next to relative ones" applied to an EU doctor deck.
Why: the FDA guidance is US and consumer-directed (M16). It may still be good practice,
which is `honest-framing`.
After: no rule cited; the framing point is handed to `honest-framing`. (TR-H8)

## Required statements

**S1 No prescribing information or no pointer to it.** A UK email to doctors promoting a
product with no PI and no link.
After: `[Prescribing information: direct link to the current UK PI — from your PI
owner]` and, if not obvious, a line saying where it is. (M6)

**S2 The invented job code.** "Job code: LUM-UK-0423 | Date of preparation: October
2026" written by the assistant.
Why: the code and date come from the company's approval system at approval; an
invented one makes unreviewed material look approved.
After: `[Job code — from your approval system] [Date of preparation — set at
approval]`. (TR-H1, TR-H5; M17)

**S3 PI written from memory.** The assistant composes a "prescribing information" block
from what it knows about the product.
After: take it word for word from the supplied label for the market, or leave a
placeholder. (TR-H1; M6, M11)

**S4 The wrong market's element.** ABPI adverse event wording in an EU deck; the Swiss
public notice in a German leaflet.
After: placeholder for the right market's element, or ask. (TR-H8)

**S5 The missing audience line on professional material.** A doctor email with no line
saying who it is for.
After: `[Audience statement, if your review process expects one]`, with the reason in
plain words. Usual practice, not a confirmed rule. (M18)

**S6 The reminder assumption.** "It's only a reminder, so it needs nothing." on a piece
that names an indication.
After: note that some markets exempt pieces that carry only the name; this one carries
more, and the review process decides. (M1, M5)

**S7 The complete list claim.** "This email now has everything it needs."
After: "Here is what is usually expected in the UK for this kind of material; your
promotional review process holds the full list." (TR-H3)

**S8 Elements on the wrong piece.** PI attached only to the cover email, not to each
item that promotes the product.
After: flag that each promotional item usually carries its own (M6 supplementary
information, UK); ask the review process for other markets.

## Personal data in the output

**D1 The named patient.** A payer follow-up repeats the payer's case with the patient's
name.
After: "the patient case you raised", with no name, age, place or dates. (P1, P3)

**D2 Name removed, still identifiable.** "A 67-year-old woman from a small village near
the lake, admitted in September."
Why: age, a small place and a date can single out one person (P2).
After: "a patient on treatment who was admitted to hospital". (P2)

**D3 The small cell.** "2 patients in canton X stopped treatment."
After: aggregate to a level the privacy function accepts, or `[GAP: needs a decision —
minimum count to show — your data privacy function]`. (P2, P6)

**D4 The case study with color.** "A 34-year-old teacher in Lausanne went back to work
in two weeks."
After: keep the point, drop the identifying color, and ask whether the case is
permissioned for this use. (P1, P4)

**D5 Called anonymous.** "I've anonymized the notes."
After: "I took out the name, age, village and admission month. Other details could still
point to the person, so I haven't called it anonymous; your privacy function decides
that." (TR-H6; P2)

**D6 The named professional.** "Dr Weber at the university hospital told us she prefers
Lumivra."
After: "a hospital dermatologist" unless the person confirms the doctor agreed to be
named for this use. (P1)

**D7 The echo.** The reply warns about the patient by repeating the details.
After: "These notes include details about an identifiable patient. I've left them out."
(governance stop rule)

**D8 The gap that leaks.** `[GAP: confirm consent from Mrs A. Brunner]`.
After: `[GAP: needs a decision — whether the case can be used at all — your data
privacy function]`. (gap-rules)

**D9 Over-removal.** Every detail cut, so the email no longer says what the payer asked.
After: keep the question ("whether hospital costs during treatment count in the budget
model"), drop the person.
