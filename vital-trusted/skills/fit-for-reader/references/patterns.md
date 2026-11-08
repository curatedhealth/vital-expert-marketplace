# Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it
breaks. All examples are invented for teaching; "Orzenta", "Talvoren" and every study
and figure here are fictional.

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

## Contents

- Audience A1–A8
- Patient literacy L1–L9
- Deliverable D1–D8
- Translation T1–T9

## Audience

**A1 Written for the writer.** The draft follows the team's own thinking order, not the
reader's question.
Why: the reader has to dig for what they need to decide.
Before: three paragraphs of background, the ask in the last line. After: the ask first,
background after. (R5 items 1, 2, 10)

**A2 Internal shorthand outside.** Project codes, "the asset", "LOE", "our KAMs", a
local payer acronym, in work for HQ, a payer or a regulator.
After: the plain name or term the reader uses, spelled out. (R5 item 7)

**A3 The internal debrief sent to a payer.** "Great news, the registry nailed it" for a
payer.
Why: tone and selection that suit the team read as promotion or overclaim to a payer.
After: the finding, the method and its limits, stated plainly. (TR-H9 applies: this is
about fit for the reader, not voice.)

**A4 Facts change between readers.** The payer version says "fewer admissions"; the
internal version says "admissions 12.0% vs 20.0%, observational".
Why: one finding must not become two different claims.
After: identical facts in both; only order, words and depth differ. (TR-H1)

**A5 Statistics for a board.** Hazard ratios, intervals and p-values in a board update.
After: the result in one plain line with its key limit, and the detail in an appendix
if wanted. The limit that changes the decision stays in the main text.

**A6 Oversimplified for a clinician.** "The drug works better" in a reply to a doctor.
Why: reads as promotion and gives the doctor nothing to judge.
After: the design, population, endpoint and effect size as supplied. (`grounded-statements`)

**A7 The wrong question answered.** The pharmacist asked about storage; the reply covers
efficacy.
After: the answer to the question asked, first. (R5 item 10)

**A8 Implied advice.** "You can safely stop taking it when you feel better" added while
simplifying.
Why: clinical advice no one supplied (TR-H6).
After: keep only what the source says; route the question to the medical function.

## Patient literacy

**L1 Clinician vocabulary.** "Concomitant therapy", "adverse events", "efficacy",
"indicated for".
After: "other medicines you take", "side effects", "how well it works", "is a medicine
for". (R1)

**L2 Medical term with no lay word.** "Hypertension" alone.
After: "high blood pressure (hypertension)", lay term first, medical term after. (R1)

**L3 The long sentence.** Thirty words, two conditions and an instruction in one
sentence.
After: one point per sentence. (R1)

**L4 Passive instructions.** "The tablet should be taken with water."
After: "Take the tablet with a glass of water." (R1)

**L5 Unexplained abbreviation or symbol.** "If your eGFR is <30".
After: the meaning in words, from the source: "if your kidneys are not working well
[GAP: not supplied — the plain description your label uses for this kidney test — supply
the patient leaflet wording]". (R1)

**L6 The number with no meaning.** "Incidence 4.2%", or a relative change only.
After: "about 4 in 100 people" only if that is the same figure, with what it describes
and over what time. (R5 items 15–17, 20; `grounded-statements` for the figure itself)

**L7 False reassurance.** "There is nothing to worry about", "completely safe", "no side
effects".
Why: not in the source, and it changes how a patient acts.
After: removed; the source's own wording about the risk kept. (R5 items 18, 19)

**L8 The frightening word.** "Dangerous", "toxic", "deadly" where the source says
"serious side effect" and gives its frequency.
After: the source's wording and frequency, in plain words. (R5 item 18)

**L9 Simplified into a different fact.** "This medicine lowers your blood pressure" from
"may lower blood pressure in some patients".
After: "may lower blood pressure in some people". Simplify the words, not the
qualifier. (TR-H1)

## Deliverable

**D1 The bait and switch.** A one-page summary requested; a four-page essay delivered.
After: one page; a line on what was left out and where it could go.

**D2 Over the limit.** "In 150 words" answered in 400.
After: within the limit; count it.

**D3 The essay in an email.** Background first, the ask in the fifth paragraph.
After: the point or ask in the first two lines.

**D4 The slide with no message.** A title that names a topic ("Q3 data") and eight
bullets.
After: the message in the title; points that support it.

**D5 The cut that changed the meaning.** A summary that keeps the result and drops
"post hoc" or "compared with placebo" to save space.
After: the qualifier stays, even if something else goes. (TR-H1)

**D6 The extra deliverable.** A one-pager plus an unrequested deck, slide notes and a
social post.
After: the one-pager. Offer the rest in one line if useful.

**D7 The ignored template.** The person supplied the company memo template; the draft
uses its own sections.
After: the template's sections and order.

**D8 Space over required lines.** A required statement dropped to fit the format.
After: kept, with the space problem flagged (`market-rules-and-data`).

## Translation

**T1 The improved message.** "May help reduce flares" becomes, in German, "reduziert
Schübe" (reduces flares).
Why: stronger than the original; a claim the source did not make.
After: keep "may help reduce" in the target language. (R3, TR-H1)

**T2 The dropped qualifier.** "In adults" or "compared with placebo" lost in
translation.
After: every qualifier on the fixed list survives. (R3)

**T3 The rounded number.** HR 0.66 becomes 0,7; 12.0% becomes 12%.
After: same value, same precision, local notation (0,66; 12,0 %). (`compare_numbers.py`)

**T4 Notation mistaken for value.** 1,500 (one thousand five hundred) in English left as
1,500 in German, where it reads as one and a half.
After: 1.500 in German. (`compare_numbers.py` reads each language's notation)

**T5 The changed unit.** mg becomes µg, or mL becomes L, in retyping.
After: units as in the original. (`compare_numbers.py`)

**T6 The loose medical term.** A side-effect or disease term paraphrased into everyday
words in a translation for doctors, or a regulated term replaced by a near synonym.
After: the approved local term if supplied; otherwise flagged for a qualified
translator. (R3, R6)

**T7 The invented local wording.** A local indication, frequency term or brand name
supplied from memory.
After: flagged: "[GAP: not supplied — approved German wording for the indication —
supply the German product information or ask your local regulatory team]". (TR-H1, R6)

**T8 The literal translation.** Word-for-word German that no German reader would write.
After: natural German with the same meaning; note any choice where natural wording
might shift meaning. (R3)

**T9 Adapted while translating.** A clinician key message translated and simplified for
patients in one step.
After: translate first; adapt for a new reader as a separate, visible step.
