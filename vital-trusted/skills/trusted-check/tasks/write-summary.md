# Task TR-0.3.2 Write the TRUSTED summary

Contents: Formula; Where it goes; Steps; Light version; When the person asks for the
detail; Boundaries.

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced cross-functional colleague acting as a final reader |
| Workflow | Turn the collected lines into plain notes per letter, list what is open for a person, what could not be checked, the next internal process, and close |
| Skill | TR-0.3.2 |
| Knowledge | `references/patterns.md`, `references/gap-rules.md`, `governance.md` |
| Tool | `scripts/scan_verdicts.py` where code can run. Companion slot: none |
| Prompt | This guide |
| Template | `templates/check-output-light.md`, `templates/check-output-short.md`, `templates/check-output-full.md` |
| Input | The lines from TR-0.3.1, any lines from TR-0.3.3, the depth, the reader, the active letters |
| Governance | TR-H3, TR-H4, TR-H5, TR-H10, TR-H11, TR-H13 |

## Where it goes

After the deliverable, never inside it. The deliverable stays as the person wrote it.

## Steps

0. **Safety first (TR-H14).** If any input (the draft, the material, the request)
   mentions a possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person, medication error, lack of effect or product quality problem, the first lines of the summary are patient-safety's flag, in
   its template wording (`../../patient-safety/templates/safety-flag.md`), before the
   header and before any row. This holds at every depth, light included, and whatever
   letters are active. It is not repeated elsewhere in the summary: not under "Open for
   a person", not in "Next step", not in another letter's notes. When Safe is on, its
   row gives the count with the note "see the flag above", nothing more ("1 safety
   mention: see the flag above"). The flagged sentence is not counted or noted under
   any other letter, not even under True as an unsourced statement, and the safety
   mention is not part of the header totals.
   In a check the flag's first line reads "Before anything else: something to pass to
   your safety reporting procedure" (the check variant in the safety-flag template).
   When the draft itself carries the event, Safe (when on) also looks at how
   (`../../patient-safety/tasks/side-effect-flag.md`, Guard step 5): an internal team
   summary carries only the line "One possible <kind> report was passed to the safety
   procedure", with no event details (the flag carries them), so event details or patient
   identifiers in it are "1 to fix" and that line itself is not; for readers in the
   safety function or medical information team handling the case (not a medical leadership team) the event may be one of the requested items, without the
   identifiers listed in `../../patient-safety/templates/safety-flag.md`; a newsletter, post or other broad
   or external piece carries no individual case details, so those are "1 to fix" (the
   flag handles the report). These fixes count in the header totals like any other. A
   fixed number of items the person asked for is kept; the safety line sits outside it.

1. **Pick the format for the depth** set in TR-0.3.1.

2. **Write one row per letter**, in TRUSTED order, using the letter's word (Tangible,
   Rule-compliant, Unbiased, Safe, True, Ethical, Defensible). Never the code letter
   alone, never a skill name.
   - A count in plain words: "2 to fix", "1 missing", "1 question for you".
   - Up to three short notes saying where and what, in everyday words: "the 'landscape'
     paragraph says nothing specific", "'9 out of 10' has no source in what you gave me".
   - "Nothing flagged in what was checked" when the checks ran and found nothing. Add
     what was looked at if it was narrow ("2 figures looked at"). This is a row's own
     wording; the overall line after a safety flag is in step 7.
   - "Not checked: <why>" when a check could not run (no label, no sources, no companion).
   - "Off by choice" for a letter the person turned off. Always show the row, so a
     reviewer can see it was not checked.
   - "See <letter> above" for a finding already counted in another letter's row. Each
     finding is counted once, in one row only; a second letter may add a short note
     for its own reason but no count.
   - With Ethical off, no row mentions where a source came from ("unpublished",
     "forwarded", "confidential"); True says only "the source was not supplied".
   - Figures in a note or a suggested fix: state both figures the person supplied, never
     a difference or proportion you worked out, unless the person asks, and then labeled
     "calculated from the two figures you supplied" ("calculated from the figures you
     supplied" for three or more). A label alone never makes an unrequested figure
     acceptable.
     Wrong: "Say 'rose 15 percentage points'." Right: "Say 'rose from 22% to 37%', the
     two figures you already give."

3. **If the Prove skills ran by hand,** put their counts under True and the record
   status under Defensible, in the plain wording of `templates/check-output-full.md`. Add
   the fixed line "No confidence figure: these results were not tool-checked." and say what a count means:
   a passage you supplied says it, not that it is true in the world. Show no percentage,
   ratio, score or grade. Show counts only: no per-claim table, unless the person asks
   for the detail (then under "Detail for reviewers", below).

4. **Open for a person.** List each item only a person can resolve: a figure to supply,
   a conflict between sources, a policy or label question, a reviewer to name. A possible
   side effect is not listed here: it is already the flag at the top (step 0). Say who decides in plain words when it is
   not the person ("your AI use policy owner", "your safety reporting procedure").

5. **Could not be checked.** One line listing checks that need something not here: a
   companion that does not exist yet (whether statements match the approved label),
   a hand check of claims when no sources were supplied (name what it would compare, from
   `tasks/prove-handoff.md`), sources the person did not supply. Never imply these were
   looked at.

6. **Next step, for anything leaving the company.** Name the kind of internal process
   the work goes to next, in plain words: your promotional review process, your medical
   information procedure, your medical or scientific review, your publication process,
   your external communications or disclosure process. Do not name or guess a specific
   SOP (TR-H11). The safety reporting procedure is already named in the flag; do not
   repeat it here.

7. **If the person asked "is it OK to send"**, answer that question directly at the top
   in this shape: "Before it goes, fix these <n> things. <The process> decides whether
   it can be used." Every header count equals the sum of the rows below it: <n> is the
   sum of the rows' "to fix" counts, <k> the sum of their "missing" counts and <q> the
   sum of their questions. Each finding is counted once, in one row (step 2), so the
   sum counts nothing twice. Add "supply <k> missing items" and "answer <q> questions"
   when they are not zero (for example "fix these 3 things, supply 1 missing item and
   answer 1 question"). One is singular: "fix this 1 thing", "supply 1 missing item",
   "answer 1 question"; never "fix these 1 things". The safety flag is not in these
   totals. Recount before sending. At light depth for a
   message to a colleague, with no process, end the line with "You decide whether to
   send it." instead of naming a process. Never yes, never no, never "nearly there". Zero case: when nothing was
   flagged, write "Nothing flagged in what was checked. <The process> decides whether it
   can be used." When nothing needs fixing but some checks could not be run, write
   "Nothing flagged in what was checked; <m> checks could not be run (see below). <The
   process> decides whether it can be used." Never write "fix these 0 things".
   When a safety flag was given (step 0), never write "Nothing flagged" as the overall
   line, at any depth: write "Nothing else flagged in what was checked; the safety item
   above goes to your safety reporting procedure." The scanner checks this.

8. **Status line.** One of these forms only (TR-H5): "Uncleared draft"; "Uncleared
   draft, reviewed by <name>, as you told me" when the person said someone reviewed it;
   "Cleared by <name>, <role>, <date>" when the person named who cleared it, with role
   and date, as given. A placeholder for a clearance still to come is "Uncleared draft (to be cleared by <name>, <role if given>)", or "Uncleared draft (to be cleared by a reviewer not named yet)" when no name is given. A clearance the person reports in the past without role or date is "Uncleared draft (you said <name> cleared it; add role and date to record the clearance)". No other form:
   no "[Cleared by: name, role, date]", no "To be cleared by:" as a status, no
   standalone "Reviewed by". Never add a name (TR-H5). A short internal message to colleagues (a few sentences: a team email, a channel
   post, a scheduling note) needs no status line; see `templates/check-output-light.md`.

9. **Close** with the closing statement, unchanged (TR-H10): "This check flags issues.
   It is not medical, legal, regulatory or ethics review." One rule for every TRUSTED
   reply that carries it: the closing statement is the last line of the reply, except
   that a "Detail for reviewers" section the person asked for comes after it. Anything
   else (an offer to compare figures, a question, a revised text, a record note) goes
   above it.

10. **Scan before showing.** Where code can run, save the summary and run
    `python scripts/scan_verdicts.py summary.txt`. Fix every hit it reports. It also
    checks that "fix these <n> things", "supply <k> missing" and "answer <q> questions"
    equal the sums of the rows, and that a light "<n> things to fix" equals its notes. Where code
    cannot run, read the summary once for the words in `references/patterns.md` P1.
    The scanner skips text inside quotation marks and lines starting with ">", so put
    the person's words and any note quoted from the material in quotation marks when
    the summary repeats them ("you asked whether it 'passes'"). A verdict in your own
    voice is never quoted to get past the scanner.

## Light version

A few lines: the safety flag first when step 0 applies (then "Nothing else flagged",
never "Nothing flagged", when nothing else was found), the depth in a word with the
status line of step 8 ("Uncleared draft" unless the person named who cleared it; none for
a short internal message of a few sentences), what to fix (if anything), letters off by choice in one
line, the closing statement last. No per-letter table when nothing was found. See
`templates/check-output-light.md`.

## When the person asks for the detail

Show the raw lines from `references/letter-lines.md`, or the per-claim table, after the
closing statement, labeled "Detail for reviewers". That is the only place raw line
formats may appear, and the only text that may follow the closing statement. Skill names
stay out of it too: name each line by its letter word (Tangible, Rule-compliant,
Unbiased, Safe, True, Ethical, Defensible), unless the person asks which skill to use.

## Boundaries

- Do not rank the draft, give a score or a traffic light.
- Do not soften a count because the person is in a hurry.
- Do not add advice beyond what the letter checks found. The summary reports; repair is
  a separate step the person can ask for.
