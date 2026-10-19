# Output format: submission content map

## Short mode (default for a direct question; 250 to 450 words)

Short mode: 450 words maximum, counted without tables' source column. Cut in this order: context paragraphs, secondary rules, full-mode sections. Offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** one or two sentences: the route(s) mapped, how many sections each, and the two or three items that change the content for this device (with rows).
2. **Map:** one line naming the standard sections with their row, then a table of only the rows specific to this route and level (route-only sections, software elements whose content differs by level, PCCP).
3. **Not sourced here:** one line per `[GAP]` (for example PMA content, UKCA content).
4. **Decisions for the regulatory owner:** route, class, documentation level, PCCP yes or no (whichever are open).
5. **Record:** "Uncleared draft" or the clearer's name.
6. One line: "Full version available: adds the per-route notes, draft-guidance status and the library check."

## Full mode

### Summary
Routes mapped, what drives the content for this device, what is not sourced.

### Inputs as decided
Route, class, documentation level, PCCP: each with who decided, or "not decided".

### Content map by route
| Section | When it applies (source wording) | Source row | Note |
|---|---|---|---|

### Software documentation overlay (US)
| Element | Basic | Enhanced | Row |
|---|---|---|---|

### Guidance status
Each guidance used, with its date and whether it is final or draft; superseded versions flagged (for example S-17).

### Library check
The `retrieve_guidance` query and what came back (passage with URL, or "no passage for this").

### Gaps
Each with its class from `gap-rules.md` and what to read.

### Record
Advisory draft. Cleared by NAME, or uncleared. AI-assisted.
