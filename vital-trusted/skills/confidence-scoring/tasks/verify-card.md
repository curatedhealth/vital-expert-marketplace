# Task TR-8.3.2 The Verify card

New in TRUSTED. Builds the short card from the VERIFY connector instruction: counts by
status, the open items, one recommendation.

## Formula

| Slot | For this task |
|---|---|
| Worker | Evidence lead |
| Workflow | Count by status, list the open items with the statement each concerns, choose one recommendation, size the card to the stakes, close |
| Skill | TR-8.3.2 |
| Knowledge | `references/rules.md` (C3, C4, C6), `references/patterns.md` (P3–P10) |
| Tool | `scripts/faithfulness.py` (counts and a default recommendation). Companion slot: reads `claim-assessment` findings; calls none |
| Prompt | This guide |
| Template | `assets/verify-card.md`, `assets/check-line.md` |
| Input | The counts and confidence line from TR-8.3.1, the findings with their statements and deciding passages, who will read the work |
| Governance | TR-H3, TR-H5, TR-H10, TR-H11, TR-H13 |

## Steps

1. **Counts by status.** All six, in plain words, including zeros, so a reviewer sees
   nothing was hidden. Mark which ones are not counted in the percent (out of scope).
2. **Open items.** Partly backed, not backed, contradicted, could not be checked. For
   each, name the statement (short quote) and, in one plain sentence, what is missing:
   - partly backed: the part the passage states and the part it does not;
   - not backed: the passages checked do not state it;
   - contradicted: what the passage says instead, quoted;
   - could not be checked: why (no usable source, empty passage, source could not be
     read). It is not a finding that the statement is false.
   Order: contradicted, not backed, could not be checked, partly backed. For internal
   work, a count per type is enough.
3. **One recommendation.** One sentence, in plain words, aimed at the most serious open
   item present (contradicted first, then not backed, then could not be checked, then
   partly backed). It says what to do to the text or the sources, never whether to send.
   The script's default line may be sharpened with the specific statement; keep it to
   one recommendation.
4. **No open items?** Say so and still say that a named person reviews the work through
   the usual process. Do not add "ready", "clean" or "safe to send".
5. **Status.** The card is a draft for human review. It is not a clearance; a named
   person clears through `citation-and-record` (TR-H5).
6. **Close.** When the card stands alone, end with: "This check flags issues. It is not
   medical, legal, regulatory or ethics review." When it goes into the TRUSTED summary,
   send only the check line; the summary carries the statement once.

## Not tool-checked

If VERIFY did not run, there is no Verify card. Offer a reading summary instead, titled
"Read, not tool-checked", with counts and the same open items, no percent, and the line:
"Connect VERIFY to check each statement against its passage."

## Check line

See `assets/check-line.md`.

## Boundaries

- No pass or fail, no threshold, no grade, no color scale, no "high", "medium" or "low"
  confidence label.
- No evidence table unless the person asks for it; then `citation-and-record` builds it.
- No clinical meaning of an open item (TR-H6); name it and route it.
