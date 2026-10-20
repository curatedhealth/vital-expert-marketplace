# Output format: intervention components (draft for the person)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** components tied to a link (count), components not tied (names), the biggest open item (often: fixed versus variable not agreed, TM11, DOI 10.1136/bmj.n2061), and who decides what ships (named, or "owner not named").
2. **Components:** table Component · Link served · Function (BCW) · Dose as the person states it (TIDieR 8) · Fixed function / may vary · Open items · Rows (each [PAPER] row with its own DOI; abstract-only and [WF] rows labeled).
3. **Adaptive components:** one line each: decision point, options, tailoring variable, rule, missing-data rule (TM82, TM89, JITAI, DOI 10.1007/s12160-016-9830-8), or [GAP].
4. **Left out of this version:** each with the person's reason, or "proposed for removal: not tied to a link".
5. **Precedent (only if asked):** record facts, including any recall summary naming a component.
6. **Record (last line of the answer body):** "Component specification draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
7. **Calls made (after the record line):** list.

## Full mode

### Answer
### Components by TIDieR item
| Component | 1 Name | 2 Why (link) | 3 Materials | 4 Procedures | 5 Who | 6 How | 7 Where | 8 When and how much | 9 Tailoring | 11 Fidelity planned | Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
Items 10 and 12 are not completed for a design (TM34). "?" marks an item not described (TM36). TIDieR rows: DOI 10.1136/bmj.g1687.
### Functions and techniques (BCT Taxonomy v1 read from the abstract only, TM51, DOI 10.1007/s12160-013-9486-6; labels are the person's)
### Adaptive decision rules
| Decision point | Options | Tailoring variable (active or passive) | Rule | Missing-data rule | Proximal outcome | Reliability or validity stated | Rows |
|---|---|---|---|---|---|---|---|
### Fixed and variable (the person's words)
### Left out of this version
### Ranking (only the person's scores, inputs shown)
### Gaps
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
