# Output format: economic evidence requirements

Two modes, same order. Short mode is the default for a direct question.

## Short mode (default; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** per body, one sentence: the economic case it asks for (evaluation type, perspective, budget impact), as read 19 October 2026.
2. **Requirements table:** Element · Body A (row) · Body B (row) · ... Elements: governing text, evaluation type, perspective, utilities and value set, discount rate, budget impact, threshold or none. A missing element is `[GAP]`.
3. **Placement (proposed):** ESF tier, NICE guidance type, ICER-PHTI tier, JCA scope, each from the person's facts or `[GAP]`; "the owner decides".
4. **Conflicts:** one line each, only those that touch the request (always both NICE threshold ranges if a threshold is mentioned).
5. **Calls and record:** calls made (often none). "Rules read 19 October 2026 from primary sources." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

End with one offer: the full profile, or the next task (A2 economic case gap check).

## Full mode

### Answer
Two or three sentences per body.

### Product facts used
Intended purpose, device class, guidance type, topic date, each with its source or `[GAP]`.

### Governing texts
| Body | Text and version | Applies because | Row |
|---|---|---|---|

### Economic elements by body
| Element | Body | Rule | Row |
|---|---|---|---|

### Placement (proposed)
| Category | Proposed placement | Fact it rests on | Row | Owner decides |
|---|---|---|---|---|

### Conflicts and moved dates
| Topic | Text A (date) | Text B (date) | Row | What to do |
|---|---|---|---|---|

### What it means
Which deliverables each body expects, where one model can serve several bodies and where it cannot. Facts only; the person decides.

### Sources and record
Row ids with URLs from `references/health-economics-methods-research.md` and `references/evidence-synthesis-research.md`; [PAPER] rows with DOI. AI-assisted draft. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
