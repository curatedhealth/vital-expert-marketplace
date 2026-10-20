# Task TR-0.3.3 Hand off to Prove

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced cross-functional colleague acting as a final reader (the Prove skills bring the evidence lead) |
| Workflow | Decide whether to hand off, build the hand-off packet, send it to the Prove skills in order, collect their lines |
| Skill | TR-0.3.3 |
| Knowledge | `references/tools.md`, `references/letter-lines.md` (Prove lines) |
| Tool | VERIFY, through `source-assessment`, `claim-assessment`, `confidence-scoring` and `citation-and-record`. This skill calls no VERIFY tool itself |
| Prompt | This guide |
| Template | Prove lines in `references/letter-lines.md`; their place in `assets/check-output-full.md` |
| Input | The finished draft, the True items found in TR-0.3.1, the sources the person supplied, the reader and purpose, the reviewer's name if given |
| Governance | TR-H4, TR-H5, `references/governance.md` |

## When to hand off

| Situation | What to do |
|---|---|
| VERIFY connected, depth short or full, sources supplied | Hand off |
| VERIFY connected, light depth | Only if the person asks |
| VERIFY connected, no sources supplied | Do not hand off. Say: "VERIFY is connected, but there is nothing to check these statements against. Share the sources and I can check them." |
| VERIFY not connected | Do not hand off. Name what it would check (below) |
| True turned off, VERIFY connected | Hand off as above. Prove runs whenever VERIFY is connected; the True row still reads "off by choice" for the drafting check, and the VERIFY results are shown under it |

"Connected" means the VERIFY tools appear in this assistant's tool list. A mention of
VERIFY by the person is not a connection (`trusted-capability-map/references/tools.md`).

## Steps when VERIFY is connected

1. **Build the hand-off packet.**

   ```
   Text:       the deliverable only, not the summary or the notes
   Priority:   the True items from TR-0.3.1 (figures, study statements, claims without a source)
   Sources:    each source the person supplied, as given: DOI, PMID, PMCID, URL, PDF, or pasted passage
   Question:   what the work is for and who reads it, in one line
   Clearer:    the reviewer's name if the person gave one; otherwise none
   ```

2. **Sources first: `source-assessment`.** It qualifies each named source and checks
   currency where an identifier exists. Pass the question so relevance is scored. A PDF
   is stored only when the person confirms they may process it; ask before handing it
   over. Collect its line.

3. **Claims next: `claim-assessment`.** It splits the text into claims and decides
   support for each against a quoted passage from an admitted source. Send the priority
   items first. Collect its line.

4. **Confidence: `confidence-scoring`.** It computes the confidence line from the
   claim results and writes the VERIFY card (counts, open items, one suggestion).
   Collect its line.

5. **Record: `citation-and-record`.** It builds a citation for each source used and,
   only when a human reviewer is named, the record. Without a name it labels the work
   an uncleared draft and builds no record. Never supply a name. Collect its line.

6. **Return to TR-0.3.2** with the Prove lines. Unsupported, contradicted, partly
   supported and uncheckable claims go into "Open for a person". The citation list from
   `citation-and-record` follows the summary.

7. **If a call fails or a source cannot be read,** report it as it came back ("one
   source could not be read") and leave those claims unchecked. Never fill the gap with
   a likely status.

## Steps when VERIFY is not connected

Name, in one or two plain lines under "Could not be checked", what VERIFY would do for
this draft, using only what is in the draft:

- whether each of the <n> figures or claims matches a passage in your sources
- whether each source is what it appears to be, and whether it has been retracted,
  corrected or replaced
- a citation for each source
- a record of the check, cleared by the reviewer you name

Then one line on how to connect it, from `trusted-capability-map/references/tools.md`, or
"connection steps are not yet published" while those are marked `[CHECK]`.

Never write a status, a percentage, a citation or a record that VERIFY did not return
(TR-H4).

## Boundaries

- This task does not interpret VERIFY results. The Prove skills do, and their meaning
  is fixed: a status is support from a supplied passage, not truth in the world.
- Do not hand the summary, the person's notes or confidential material the person has
  not chosen to share to VERIFY. Only the deliverable and the sources they supplied.
- Do not choose a citation style for the person; the Prove skill uses their stated
  preference or the connector's default.
