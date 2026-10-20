# Task TR-0.3.2 Write the TRUSTED summary

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced cross-functional colleague acting as a final reader |
| Workflow | Turn the collected lines into plain notes per letter, list what is open for a person, what could not be checked, the next internal process, and close |
| Skill | TR-0.3.2 |
| Knowledge | `references/patterns.md`, `references/gap-rules.md`, `references/governance.md` |
| Tool | `scripts/scan_verdicts.py` where code can run. Companion slot: none |
| Prompt | This guide |
| Template | `assets/check-output-light.md`, `assets/check-output-short.md`, `assets/check-output-full.md` |
| Input | The lines from TR-0.3.1, any lines from TR-0.3.3, the depth, the reader, the active letters |
| Governance | TR-H3, TR-H4, TR-H5, TR-H10, TR-H11, TR-H13 |

## Where it goes

After the deliverable, never inside it. The deliverable stays as the person wrote it.

## Steps

1. **Pick the format for the depth** set in TR-0.3.1.

2. **Write one row per letter**, in TRUSTED order, using the letter's word (Tangible,
   Rule-compliant, Unbiased, Safe, True, Ethical, Defensible). Never the code letter
   alone, never a skill name.
   - A count in plain words: "2 to fix", "1 missing", "1 question for you".
   - Up to three short notes saying where and what, in everyday words: "the 'landscape'
     paragraph says nothing specific", "'9 out of 10' has no source in what you gave me".
   - "Nothing flagged in what was checked" when the checks ran and found nothing. Add
     what was looked at if it was narrow ("2 figures looked at").
   - "Not checked: <why>" when a check could not run (no label, no sources, no companion).
   - "Off by choice" for a letter the person turned off. Always show the row, so a
     reviewer can see it was not checked.

3. **If VERIFY ran,** put its counts and the confidence line under True, and the record
   status under Defensible, in the plain wording of `assets/check-output-full.md`. Say what
   the percentage means in the same sentence: support from the sources supplied, not
   truth in the world. Never show a VERIFY figure that the Prove skills did not return.

4. **Open for a person.** List each item only a person can resolve: a figure to supply,
   a conflict between sources, a policy or label question, a possible side effect for
   the safety function, a reviewer to name. Say who decides in plain words when it is
   not the person ("your AI use policy owner", "your safety reporting procedure").

5. **Could not be checked.** One line listing checks that need something not here: a
   companion that does not exist yet (whether statements match the approved label),
   VERIFY when it is not connected (name what it would check, from
   `tasks/prove-handoff.md`), sources the person did not supply. Never imply these were
   looked at.

6. **Next step, for anything leaving the company.** Name the kind of internal process
   the work goes to next, in plain words: your promotional review process, your medical
   information procedure, your medical or scientific review, your publication process,
   your external communications or disclosure process. Do not name or guess a specific
   SOP (TR-H11).

7. **If the person asked "is it OK to send"**, answer that question directly at the top
   in this shape: "Before it goes, fix these <n> things. <The process> decides whether
   it can be used." Never yes, never no, never "nearly there".

8. **Status line.** "Draft, not yet reviewed" unless the person named who cleared it, in
   which case "Cleared by <name as given>". Never add a name (TR-H5).

9. **Close** with the closing statement, unchanged, as the last line (TR-H10):
   "This check flags issues. It is not medical, legal, regulatory or ethics review."

10. **Scan before showing.** Where code can run, save the summary and run
    `python scripts/scan_verdicts.py summary.txt`. Fix every hit it reports. Where code
    cannot run, read the summary once for the words in `references/patterns.md` P1.

## Light version

A few lines: the depth in a word, what to fix (if anything), letters off by choice in one
line, the closing statement. No per-letter table when nothing was found. See
`assets/check-output-light.md`.

## When the person asks for the detail

Show the raw lines from `references/letter-lines.md` after the summary, labeled "Detail
for reviewers". That is the only place skill names and line formats may appear.

## Boundaries

- Do not rank the draft, give a score or a traffic light.
- Do not soften a count because the person is in a hurry.
- Do not add advice beyond what the letter checks found. The summary reports; repair is
  a separate step the person can ask for.
