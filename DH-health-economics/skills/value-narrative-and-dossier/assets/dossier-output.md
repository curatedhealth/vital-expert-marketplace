# Output format: value dossier (draft for the owner)

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** dossier type (or ESF standards) for this audience, sections ready, sections open, and the stop. Say once that the library's `value-dossier` job is design-partner only and the dossier was built by direct calls.
2. **Skeleton:** Section · Rows · Status (ready / partly / `[GAP]`) · Filled by.
3. **Open items:** the gaps and who fills each.
4. **Record:** "Draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer

### Dossier skeleton
| # | Section | Holds | Rows (source status) | Status | Filled by |
|---|---|---|---|---|---|

### Clinical evidence
| Outcome | Study | Population, comparator, time point | Result as stated in the passage | Certainty (rating, who) | Passage locator |
|---|---|---|---|---|---|

### Economic evaluation and budget impact (type B or ESF only)
| Item | Row | Present / absent / not checkable | Note |
|---|---|---|---|
No threshold is applied by the skill. Any arithmetic on the person's numbers is labeled hypothesis.

### Required context and statements
The PC rows that bind this dossier and the wording they require, drafted for the owner.

### Not in this dossier
Unsourced sections (`[GAP]`), held claims, work for dh-market-access, DH-01.07.2 or dh-clinical-validation (literature-and-real-world-evidence-review).

### Decisions for the owner
Numbered list.

### Sources and record
Calls made. AMCP rows labeled "AMCP 6.0 draft"; [PAPER] rows with DOI. "Draft for the owner. The skill does not submit or clear dossiers. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
