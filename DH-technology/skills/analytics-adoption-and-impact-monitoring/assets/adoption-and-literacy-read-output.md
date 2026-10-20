# Output format: adoption and literacy read

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/adoption_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 2 to 4 from `scripts/adoption_check.py funnel` and `champions` output; do not recount by hand. Budget in words: answer 70, funnel 150, stopped steps 60, champions 50, limits 40, record 45.

1. **Answer** (two sentences): penetration 1 and 2 by group with numerators, denominators and window; the stage with the largest drop; export-only users; the most common stopped step; sites with no champion. No verdict, no target.
2. **Funnel** (people in scope as the denominator, RE-AIM, re-aim.org, read 19 October 2026, CS27, CS28): Group · In scope · Trained (attended) · Practice task done · Task completed in product (penetration 1) · Penetration 2 (Proctor 2011, CS39, DOI 10.1007/s10488-010-0319-7).
3. **Where people stop:** step · count, from your roster; a fact for the design owner, not a judgment of people.
4. **Champions:** questions logged per champion in the window; "unmeasured (no record)"; sites with no champion.
5. **Limits:** flags A1 to A6 that apply, one line each (events left out, not instrumented, attendance only).
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Adoption read draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Window, read date and denominator (yours)
### Literacy objective and unit as you wrote them (metric version matched)
### Funnel by group
| Group | In scope | Invited | Trained (attended) | Practice task done | Active in window | Task completed (penetration 1) | Penetration 2 | Export only |
|---|---|---|---|---|---|---|---|---|
### Where people stop after training
| Step | Count | Group |
|---|---|---|
### Campaign result against the audience size
### Champions
| Champion seat | Agreed on | Questions in window | Source and rows |
|---|---|---|---|
### Strategies you asked about (names and definitions only, ERIC, CS41 to CS49, DOI 10.1186/s13012-015-0209-1)
### Flags and events left out
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Adoption read draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
