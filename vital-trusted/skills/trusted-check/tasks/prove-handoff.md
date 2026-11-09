# Task TR-0.3.3 Hand off to Prove

The Prove skills are run by hand. No tool is called, and every result carries the label
"not tool-checked".

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced cross-functional colleague acting as a final reader (the Prove skills bring the evidence lead) |
| Workflow | Decide whether to run Prove, build the packet, run the Prove skills by hand in order at the depth chosen, collect their lines |
| Skill | TR-0.3.3 |
| Knowledge | `references/tools.md`, `references/letter-lines.md` (Prove lines), `claim-assessment/references/statuses.md` |
| Tool | None. The Prove skills are written for a person or an assistant to run by hand |
| Prompt | This guide |
| Template | Prove lines in `references/letter-lines.md`; their place in `templates/check-output-full.md` |
| Input | The finished draft, the True items found in TR-0.3.1, the sources the person supplied, the reader and purpose, the reviewer's name, role and date if given |
| Governance | TR-H4, TR-H5, `governance.md` |

## When to run Prove

| Situation | What to do |
|---|---|
| Sources supplied, depth short or full | Run Prove by hand |
| Sources supplied, light depth | Only if the person asks |
| No sources supplied | Do not run Prove. Say: "There is nothing to compare these statements with. Share the sources and I can compare them by hand." Then name what could not be checked (below). The Prove skills' no-sources form does not apply inside a check: the line "No confidence figure: these results were not tool-checked." is not shown, because no results exist |
| True turned off | Do not run Prove in the check; the True row reads "off by choice" (`../../trusted-capability-map/SKILL.md`, "Letters that are off") |

## Steps when sources are supplied

1. **Build the packet.**

   ```
   Text:       the deliverable only, not the summary or the notes
   Priority:   the True items from TR-0.3.1 (figures, study statements, claims without a source)
   Sources:    each source the person supplied, as given: pasted passage, PDF text, DOI, PMID, URL
   Question:   what the work is for and who reads it, in one line
   Reviewer:   the reviewer's name, role and date if the person gave them; otherwise none
   ```

2. **Sources first: `source-assessment`.** One source card per source: kind, peer review
   (only from evidence), funders and interests, fit to the question, what it can carry
   and what it cannot, date in full, currency ("checked by you on <date>" or "not
   checked", with the check the person can do). No tier, no score. Collect its line.

3. **Claims next: `claim-assessment`.** Split the text into claims and compare each, by
   hand, with an exact quoted passage from a supplied source. The result is one of the six
   plain-word results defined in `claim-assessment/references/statuses.md`. Send the
   priority items first. Collect its line.

4. **Open items: `confidence-scoring`.** Counts by result, the open items in order of
   risk, one recommendation, and the fixed line "No confidence figure: these results were not tool-checked." No percentage. Collect its line.

5. **Reference lines and record: `citation-and-record`.** Plain reference lines from the
   supplied details, and a record note. The record names the reviewer if the person gave
   a name, role and date; otherwise its first line is "Uncleared draft". Never supply a
   name. Collect its line.

6. **Run at the depth chosen.** Short depth: priority items, the counts and the open items.
   Full depth: every step above. Label everything "not tool-checked".

7. **Return to TR-0.3.2** with the Prove lines. Partly found, not found, "your passage says
   something different" and "no passage to compare with" go into "Open for a person". The
   reference list from `citation-and-record` follows the summary.

8. **If a source cannot be read,** say so as it is ("one source could not be read") and
   leave those claims at "no passage to compare with". Never fill the gap with a likely
   result.

## When no sources are supplied

Name, in one or two plain lines under "Could not be checked", what a hand check would do
for this draft, using only what is in the draft:

- whether each of the <n> figures or claims matches a passage in your sources
- whether each source can carry what the draft says, and whether it has been retracted,
  corrected or replaced
- reference lines for each source
- a record of the check, with the reviewer you name

Never write a result, a figure, a reference or a record that nobody produced (TR-H4).

## Boundaries

- This task does not interpret the results. The Prove skills do, and their meaning is
  fixed: a result is how a supplied passage compares with the sentence, not truth in the
  world.
- No percentage, ratio, score, tier or grade appears anywhere.
- Do not hand the summary, the person's notes or confidential material the person has
  not chosen to share to anyone. Use only the deliverable and the sources they supplied.
- Do not choose a reference style for the person.
