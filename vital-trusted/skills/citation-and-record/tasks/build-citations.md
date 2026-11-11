# Task TR-8.4.1 Build citations

Absorbs the citation part of the earlier Prove record method, now written by hand.

## Formula

| Slot | For this task |
|---|---|
| Worker | Quality and compliance lead |
| Workflow | List the sources, write one reference line per source from its own details, name any missing detail, give the lines with no caption |
| Skill | TR-8.4.1 |
| Knowledge | `references/rules.md` (R1, R2), `references/patterns.md` (C1 to C5) |
| Tool | None. `scripts/plain_reference.py` where code can run, or the same steps by hand |
| Prompt | This guide |
| Template | `templates/reference-list.md` |
| Input | The finished text, the sources it cites with whatever details the person supplied, any source notes from `source-assessment`, the style the person named (if any) |
| Governance | TR-H1, TR-H3, TR-H4, TR-H13 |

## Steps

1. **List the sources the work actually cites.** One line each, in the order they
   appear. A source the person supplied but the text does not use is not cited; ask
   whether it belongs. A statement in the text with no source is not this task's to
   fill; it goes back to `sourced-claims` as a gap.
2. **Take each source's details as supplied.** Authors, title, journal or publisher,
   year or full date, volume, issue, pages, a label's revision or version, the online
   publication date, DOI, PMID, URL: only what the person gave or the source
   note holds. Do not look anything up from memory, and do not correct a detail you
   believe is wrong. Ask instead.
3. **Name what is missing before writing.** For each source, note any detail a reference
   needs that was not supplied (most often the year, the pages or the identifier). Do
   not ask for authors for a label, fact sheet or press release; it has a corporate
   author or none. Do not ask for a journal for a society guideline or position
   statement whose issuer is named, and do not ask for a DOI or PMID for a label, SmPC
   or leaflet. A poster's presenter is written "Presented by <name>", never as its
   author. A description the person gave ("on dosing intervals") is not a title: keep it
   out of the title slot and name the missing title in the note. Keep the source kind
   (poster, abstract, fact sheet, label, press release) in the line as the person gave
   it. These
   stay missing in the line and appear in the note after the list.
4. **Settle the style.** If the person named a style, write the lines by hand in that
   style, from the supplied details only, and say they were written by hand. If the
   person named none, write plain lines in one consistent order. Do not choose a style
   for them.
5. **Write one line per source.** Copy the supplied details as given: a full date stays
   a full date, "revision April 2026" stays in the line for a label, and "published online
   3 March 2026" stays as "Published online 3 March 2026". Never list a year as missing
   when the person gave it in any form. Add no access date
   unless the person gave one. Add no caption before the list ("Reference:" and similar
   are all captions). Do not complete or tidy a line beyond the supplied details.
6. **Mark the list once,** after the last line: "Reference lines built from the details you
   gave; not tool-checked."
7. **Write the note after the list, only if needed:** which detail is missing for which
   source, and what would close it; a style you could not apply exactly. One line each.
8. **Do not say what the references prove.** A reference list shows where statements
   came from. If the person asks whether the citations "back up" the text, say that is
   a separate check (`claim-assessment`) and offer it.

## Checks before returning

- Count of reference lines equals count of cited sources.
- No year, page, volume, author, identifier or access date appears that was not supplied.
- No caption before any line.
- The list is marked "not tool-checked".
- Nothing in the reply says or implies the claims are supported.

## Check line

See `templates/check-line.md`.

## Boundaries

- Whether a source is good enough for the use is `source-assessment`.
- Whether the source says what the text says is `claim-assessment`.
- Which statements need a reference is `sourced-claims`.
- No source score is printed under a reference. There are none.
