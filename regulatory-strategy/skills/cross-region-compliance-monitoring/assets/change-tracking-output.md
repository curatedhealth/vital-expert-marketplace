# Output format: regulatory change tracking

## Short mode (default for a direct question)

Short mode: 450 words maximum. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose (keep them in the table), secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Do not send a short-mode answer over 450 words. Offer the full version in one line. Refusals follow the same 450-word cap.

1. **Answer:** the items that change something for this product, each with status word, instrument, date and row.
2. **Drafts and proposals to keep separate:** one line each, "not law today".
3. **Obligations:** only the lines not already given in item 1, at most five; offer the full table in one line.
4. **Sources to follow:** one per market.
5. **Record:** "Uncleared draft" or the clearer's name.

## Full mode

### Summary
Two or three sentences: what moved since the last review, what is law, what is still draft.

### Register events
What `get_deltas` returned, worded per `gap-rules.md` (register events only).

### Guidance and law
| Market | Item | Status | Date | What it changes for this product | Reopens (planning task) | Rows |
|---|---|---|---|---|---|---|

### Superseded documents
| Superseded | Replaced by | Rows |
|---|---|---|

### Where the next change will appear
| Market | Source | How to follow | Rows |
|---|---|---|---|

### Obligations table
Output of `scripts/obligations_table.py` for the person's markets.

### Record
Advisory draft. Cleared by NAME, or uncleared. AI-assisted.
