# Output format: conformance sample

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question; 250 to 450 words)

1. **Answer:** the processes with a fail, the count of in-target criteria not tested, and the method mix ("automated tests check only part of what needs testing", UX-UK-24, where results rest on a scan).
2. **Frame:** target (version, level, criteria count), build, screens sampled, processes covered or missing.
3. **Status (compact):** Screen or process · Fails (criterion, level, issue id) · Not tested (count) · Methods used.
4. **Findings:** only facts not already in the table, each with criterion and row.
5. **Not shown by this sample:** processes not sampled, methods not used.
6. **Records that would close the gaps:** per untested screen or process, the method the requirement names, drawn from the three types of testing (testing with people, manual, automated; UX-UK-24).
7. **Open questions (at most three).**
8. **Record:** "Sample draft on your test records. Not a conformance statement. AI-assisted. To be cleared by NAME; the record is built with verify.build_record once NAME clears it." Until a named person clears it: "Uncleared draft." Who clears it: the owner the person named, in their words, or "owner not named". The record is built with `verify.build_record` once that named person clears it; until then the line reads "uncleared draft".
9. One line offering the full version.

## Full mode

### Answer

### Frame
| Item | Value |
|---|---|
| Target | |
| Build | |
| Screens sampled | |
| Processes (complete or not) | |
| Records and methods | |

### Status per criterion
| Screen | Criterion | Level | Status: pass / fail / n.a. / not tested | Record (method, date, issue id) | Row |
|---|---|---|---|---|---|

### Processes
| Process | Pages sampled | Any fail? | Consequence (UX-STD-22) |
|---|---|---|---|

### Findings

### What this sample cannot show

### Gaps

### Record
Draft. No statement that the build or a screen conforms. AI-assisted. Names who clears it (the owner the person named, or "owner not named"); the record is built with `verify.build_record` once that named person clears it. Until then: "Uncleared draft."
