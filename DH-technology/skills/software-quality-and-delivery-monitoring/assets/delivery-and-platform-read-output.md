# Output format: delivery and platform read

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/delivery_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, delivery 100, platform 80, SBOM 80, recalls 50, record 50.

1. **Answer** (two or three sentences): period; releases, rollbacks, failed health checks and releases you marked as clinical defects; skipped stages and unrecorded skips; the platform and SBOM facts that matter most. No rating, no benchmark.
2. **Delivery:** counts, then Release · What happened · Flag. Percentages are arithmetic on your log.
3. **Platform:** capacity flags (quota, no measurement, saturation elsewhere) and residency flags.
4. **SBOM:** Component · Support · End of support (days before your read date) · KEV match (your list) · Source (row).
5. **Recall records in the period:** title, date, class as stored, or "none returned; not evidence of safety".
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Delivery and platform read draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Header (period, read date, required stages yours)
### Releases in the period
| Release | Date | Build | Stages run | Skipped | Exception | Recorded on | Outcome | Clinical defect | Caught at | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
### Capacity and first failure
### Region and residency
### SBOM end of support and known vulnerabilities (CVE ids only)
### Recall records of comparable software (as stored)
### Rules behind the read (source name and date, row)
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Delivery and platform read draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
