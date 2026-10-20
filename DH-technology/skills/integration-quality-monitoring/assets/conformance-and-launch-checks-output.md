# Output format: conformance and launch checks

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/integration_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, profiles 130, cells 130, limits 50, record 50.

1. **Answer** (two sentences): profiles checked and those with misses, naming any that failed in every sample; cells run and cells flagged; the flag that most limits the read; read date (yours, or "not given"). No overall score or verdict.
2. **By profile:** Profile · Samples · Samples with a miss · Failing ids and elements · Flags (S1 to S3).
3. **Launch cells with a flag:** Cell · Role / patient / encounter · HTTP · Context missing · Write-back · Flags (L1 to L7).
4. **Limits:** checks or ceilings not given, unchecked resource types, mocked or not-run cells, version of the sheet against certification and current publication.
5. **Calls made**, then one line offering the full version.
6. **Record (the very last line, nothing after it):** "Integration check draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your check sheet (guide, version, checks and pass rules, who runs them, environment)
### Sample (count per profile, how drawn, dates, as you gave it)
### Score by profile
| Profile | Samples | Samples with a miss | Failing payload / resource: element | Flags |
|---|---|---|---|---|
### Launch matrix (roles, patient states, encounter states, pass rules and ceilings, yours)
### Launch run
| Cell | Role / patient / encounter | HTTP | Context missing | Write-back | Token ms | First read ms | Flags |
|---|---|---|---|---|---|---|---|
### Certified EHR duties touched by a failed cell (duty and observed fact side by side, for the owner)
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Integration check draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
