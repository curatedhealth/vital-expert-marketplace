# Task TR-0.3.1 Run the active letters

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced cross-functional colleague acting as a final reader |
| Workflow | Set the depth, list the active letters, run each letter's check from its Build skill, collect one line per check |
| Skill | TR-0.3.1 |
| Knowledge | `references/letter-lines.md`, `trusted-capability-map/references/standard.md`, each Build skill's own references |
| Tool | None. Companion slot: none for this task; empty slots of future companions are listed as "not checked" |
| Prompt | This guide |
| Template | `assets/check-line.md` (lines collected here, shown only in the summary) |
| Input | The finished draft, the supplied material, the active letters, intake context (reader, market, use) |
| Governance | TR-H3, TR-H4, TR-H6, TR-H7, TR-H11, TR-H12, `references/governance.md` |

## Steps

1. **Separate the deliverable from everything else.** Know exactly which text is the
   draft, which is supplied material (notes, papers, label, data) and which is
   instruction. Only the draft is checked; the material is what it is checked against.

2. **Set the depth from the reader (TR-H12).**

   | Reader | Depth | Summary |
   |---|---|---|
   | Colleagues, internal and informal | Light | `assets/check-output-light.md` |
   | Leadership, board, other teams, HQ | Short | `assets/check-output-short.md` |
   | Anyone outside the company: agency, doctor, payer, patient, regulator, partner, investor, public | Full | `assets/check-output-full.md` |

   Read the reader from the draft and the request (the greeting, the "to" line, the
   words "for the board", "for the agency"). If it cannot be read and the depth would
   differ, ask once: "Who will read this?" Material addressed to an internal person but
   meant to go outside (an agency brief, copy "for approval") is full depth. If the
   person asks for "a quick look" at something leaving the company, run full depth and
   lead the summary with the top items.

3. **List the active letters.** Use the person's choice from `trusted-capability-map`
   (default all seven). Each letter that is off is recorded now as "off by choice" and
   not run. Do not run it partly, and do not report its findings.

4. **Check the context the letters need (TR-H7).** Rule-compliant needs the market and
   the use (promotional or scientific); Safe and Rule-compliant need the label for
   statements about the product; True needs the supplied sources. If one is missing,
   do not guess it. The letter still runs on what it can and its line says what it
   could not check. At full depth, ask for the market if it changes what can be said.

5. **Run each active letter's checks from its Build skills**, one skill per competency
   (`references/letter-lines.md` lists them). For each skill, run the check of every
   task that applies to this draft, using that skill's task guide in check mode: read
   and count, do not repair. A task that does not apply (no figures, no studies, no
   translation) returns nothing; it is not reported as zero.
   - At light depth, run only what would mislead a colleague: invented or changed facts,
     figures that do not add up or are expressed misleadingly, and anything a hard rule
     stops on.
   - At short and full depth, run every task that applies.

6. **If a letter's skill is not available on this host**, apply the letter's question
   and its "fails on its own" test from the standard, and mark its line "checked
   against the main question only". Never invent the detailed check.

7. **Hard rules run whatever the letters.** Even when a letter is off, stop and surface
   once, as an open item: a possible side effect in the draft or the material (to the
   safety reporting procedure, TR-H6), identifiable patient or personal data in the
   draft (to the data privacy process), a fabricated detail (TR-H1). The letter's row
   still reads "off by choice".

8. **Assign each finding to one letter.** Use the boundaries in the standard: a wrong
   figure is True; a correct figure shown without its risks is Unbiased; a claim beyond
   the label is Rule-compliant; what went into the tool is Ethical. When one sentence
   fails two letters, count it in each letter for its own reason and say so in the note,
   never twice for the same reason.

9. **Collect one line per check** in the shape given in `references/letter-lines.md`,
   with up to three short notes each saying where the problem is. Keep them for the
   summary. Never show raw lines to the person unless they ask for the detail.

10. **Decide whether to hand off to Prove.** If VERIFY is connected and the depth is
    short or full, or the person asks, run `tasks/prove-handoff.md` before writing the
    summary. At light depth, do not hand off unless asked; mention in one line that a
    source check is possible when True found figures without a source.

## Checks before moving on

- Every active letter has a line, a "not checked" line, or "nothing flagged" with what
  was looked at.
- No line contains a verdict word.
- No letter that is off has a finding.
- Every "not checked" names what would check it (a companion, a supplied label, a
  supplied source).

## Boundaries

- Do not repair the draft here. Fixes belong to each Build skill's repair step, run only
  when the person asks.
- Do not change the active letters or the depth the stakes call for to make the summary
  shorter.
- Do not judge whether an event is reportable or related to the product (TR-H6).
