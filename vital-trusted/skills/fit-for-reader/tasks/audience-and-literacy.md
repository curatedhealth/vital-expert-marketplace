# Task TR-1.2.1 Audience and literacy

## Formula

| Slot | For this task |
|---|---|
| Worker | Medical writer who has written for every audience |
| Workflow | Name the reader and what they must decide or do, fill the reader card, then hold every passage to that reader's vocabulary and depth |
| Skill | TR-1.2.1 |
| Knowledge | `references/readers.md`, `references/rules.md` (R1, R2, R4, R5), `references/patterns.md` (A1–A8, L1–L9) |
| Tool | `scripts/plain_language_scan.py` for patient or lay text where code can run. Companion slot: none (no companion planned) |
| Prompt | This guide |
| Template | `assets/reader-card.md`, `assets/repair-note.md`, `assets/check-line.md` |
| Input | The request, the context card, the supplied material, any existing draft |
| Governance | TR-H1, TR-H2, TR-H3, TR-H6, TR-H7, TR-H11 |

## The reader card

Before drafting or repairing for a named reader, fill `assets/reader-card.md` from the
context card, the request and `references/readers.md`. It takes four lines: who reads
it, what they must decide or do, the words they use, and how deep to go. If the reader
is not known and it changes the draft, ask once. Do not show the card to the person
unless they ask; it steers the writing.

## Guard (while drafting)

1. **Lead with what this reader must decide or do.** A board needs the decision and the
   ask; a pharmacist needs how to dispense, store and check interactions; a payer needs
   population, comparator, outcome and cost; a patient needs what it means for them and
   what to do. Put that first.
2. **Use the words this reader uses.** Keep the technical term a doctor expects; replace
   the internal shorthand (brand codes, project names, "the asset", "LOE") a payer or
   regulator would not know. For HQ, use the global names, not affiliate slang.
3. **Set the depth to the reader.** Method detail for a medical reader; the result and
   its limits for a board; never more statistical apparatus than the reader can use.
   Depth is cut, never the limitation that changes the meaning.
4. **One finding, many readers.** When the same finding goes to two readers, keep the
   facts identical and change only the order, words and depth. If the payer version
   needs a fact the internal version did not use, it comes from the material or it is a
   gap.

### Patient and lay readers

Patient-facing material is always at full depth (TR-H12). Apply these as good practice
everywhere and, for EU package leaflets, as the guideline cited in `references/rules.md`
R1.

5. **Plain words.** Give the everyday word first and the medical term after it, in
   brackets, when the patient will meet the medical term again (on the pack, from the
   doctor): "high blood pressure (hypertension)". Otherwise use only the everyday word.
6. **Short sentences.** Split long sentences, especially those carrying new information.
   One instruction per sentence. Active voice: "Take one tablet each morning", not
   "One tablet should be taken".
7. **No unexplained terms.** Spell out an abbreviation at first use or drop it. Replace
   symbols such as < and > with words ("less than"). Explain frequency words in numbers
   a patient can picture ("very common: may affect more than 1 in 10 people") only when
   the source gives the frequency.
8. **Numbers the reader can use.** Give the number the patient needs, say what it means,
   and do not make them calculate. Where a probability is given, add words or a picture
   only if the meaning stays the same.
9. **Neither scare nor falsely reassure.** Keep each risk at the size and certainty the
   source gives it. Remove "nothing to worry about", "completely safe", "no side
   effects" unless the source says exactly that; remove alarming words the source does
   not use. Do not add comfort or warning that is not in the material.
10. **Keep the source's route to a professional.** If the source says "ask your doctor
    or pharmacist", it stays, in plain words. Whether the material needs such a route,
    and where, is `patient-safety` (Safe). Do not add or decide it here.

## Repair (existing draft)

1. **Fill the reader card** from the context card and request.
2. **Read the draft as that reader.** Mark each passage: fits; above the reader (jargon,
   method detail, unexplained term, too long); below the reader (oversimplified for a
   clinician, missing the number they need); wrong focus (answers a question this reader
   does not have).
3. **For patient or lay text**, where code can run, use
   `scripts/plain_language_scan.py <text.txt>` to list long sentences, long words,
   abbreviations, symbols, clinician terms and tone words. Read every hit; a hit is a
   prompt, not a finding. Without code, do the same reading by hand.
4. **Fix** in the reader's words. For each change, check that every fact, number,
   condition and limitation in the original is still there. Where the plain version
   would need a fact that was not supplied, leave a gap.
5. **Note the change** in the repair note, sized to the stakes.

## Check line

See `assets/check-line.md`.

## Boundaries

- Rewriting into plain words is not a user test or a readability assessment. Never say
  the text "meets" a readability standard or would pass user testing (`references/rules.md`
  R4).
- No readability score or grade level is given. The skill does not compute one, and a
  score would read as a verdict (TR-H3).
- No clinical advice is added for a patient or a prescriber (TR-H6). If the person asks
  for it ("tell them they can double the dose if they miss one"), stop and route to the
  medical function.
- Material for investors: whether a passage is inside information or needs disclosure
  is a legal determination (TR-H6). Flag for the legal or investor relations function.
- Regulator correspondence: fit the words and structure; the content and commitments
  belong to the regulatory function and its process (TR-H11).
