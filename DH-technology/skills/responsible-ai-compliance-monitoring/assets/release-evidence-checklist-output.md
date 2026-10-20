# Output format: release evidence checklist

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/evidence_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 60, release 30, core items 60, items by market 200, record 45.

1. **Answer** (two sentences): how many items apply now and how many from a later date (with the dates and the instrument that set them); the three core items.
2. **Release (yours):** system, model version, markets, role, device status as you stated it. Missing: "not given".
3. **Core items:** subgroup test on the release model (test), intended use (document), the human who can override (control, named in your words).
4. **Items for your markets:** Item · Type · Standing · Applies from · Source and rows (source name and date in plain words, row id after; DOI for [PAPER]). Drafts and proposals labeled; "applies if you are ...: for your legal owner".
5. **Not enough on its own:** policy in place of a test; evidence on another model version; unseen groups.
6. **Calls made**, then one line offering the full version and the index as CSV.
7. **Record (the very last line, nothing after it):** "Release evidence checklist draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Release (yours)
### Core items
| Item | Type | Why it is here | Source and rows |
|---|---|---|---|
### Items by market and role
| Item | Type | Standing | Applies from | Applies to you (for your legal owner) | Source and rows |
|---|---|---|---|---|---|
### Draft and proposed items (not requirements)
### Evidence that is not enough on its own
### Your items (added as given)
### The index (CSV columns for scripts/evidence_check.py)
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Release evidence checklist draft. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
