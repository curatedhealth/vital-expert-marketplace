# Task TR-8.4.1 Build citations

Absorbs the citation part of the earlier vital-verify record method.

## Formula

| Slot | For this task |
|---|---|
| Worker | Quality and compliance lead |
| Workflow | List the sources, build one reference per source from its own details, name any missing detail, paste the lines with no caption |
| Skill | TR-8.4.1 |
| Knowledge | `references/rules.md` (R1, R2), `references/patterns.md` (C1–C5), `references/tools.md` |
| Tool | VERIFY `build_citation`, once per source. Without VERIFY: `scripts/plain_reference.py` or the same steps by hand |
| Prompt | This guide |
| Template | `assets/reference-list.md` |
| Input | The finished text, the sources it cites with whatever details the person supplied, any source records returned by `source-assessment`, the style the person named (if any) |
| Governance | TR-H1, TR-H3, TR-H4, TR-H13 |

## Steps

1. **List the sources the work actually cites.** One line each, in the order they
   appear. A source the person supplied but the text does not use is not cited; ask
   whether it belongs. A statement in the text with no source is not this task's to
   fill; it goes back to `sourced-claims` as a gap.
2. **Take each source's details as supplied.** Use the source record from
   `source-assessment` when it ran; otherwise the details the person gave (authors,
   title, journal or publisher, year, volume, issue, pages, DOI, PMID, URL). Do not
   look anything up from memory, and do not correct a detail you believe is wrong.
   Ask instead.
3. **Name what is missing before building.** For each source, note any detail a
   reference needs that was not supplied (most often the year, the pages or the
   identifier). These stay missing in the line and appear in the note after the list.
4. **Settle the style.**
   - The person named Chicago or Harvard: pass that style.
   - The person named no style: leave the style out, so the preference set on the
     person's VERIFY key applies. Do not choose one for them.
   - The person named another style (for example Vancouver or AMA): VERIFY builds
     Chicago and Harvard only (`references/tools.md`). Say so in one line and offer
     either a VERIFY line in Chicago or Harvard, or plain lines in their style marked
     "not tool-built".
5. **With VERIFY connected: call `build_citation` once per source.** Arguments and
   pitfalls are in `references/tools.md`. Paste the returned line exactly as the
   reference. Add no caption before it ("Reference:", "As returned by VERIFY:" and
   similar are all captions). Do not edit, reorder the parts of, or complete the line.
6. **Without VERIFY:** build plain lines from the supplied details with
   `scripts/plain_reference.py` where code runs, or by hand in the same order. Leave a
   missing detail out of the line; never fill it. Mark the list once, after the last
   line: "Reference lines built from the details you gave; not tool-built."
7. **Write the note after the list, only if needed:** which detail is missing for which
   source, and what would close it; a style that could not be applied. One line each.
8. **Do not say what the references prove.** A reference list shows where statements
   came from. If the person asks whether the citations "back up" the text, say that is
   a separate check (`claim-assessment`) and offer it.

## Checks before returning

- Count of reference lines equals count of cited sources.
- No year, page, volume, author or identifier appears that was not supplied or returned.
- No caption before any line.
- Style passed only if the person named it.
- The list is marked "not tool-built" if VERIFY did not build it.
- Nothing in the reply says or implies the claims are supported.

## Check line

See `assets/check-line.md`.

## Boundaries

- Whether a source is good enough for the use is `source-assessment`.
- Whether the source says what the text says is `claim-assessment`.
- Which statements need a reference is `sourced-claims`.
- Source scores printed under each reference come from the source assessment results
  when that ran (`confidence-scoring`). This task does not compute or invent them.
  [CHECK: whether scores are printed by this skill or by confidence-scoring, to be
  settled with the owner.]
