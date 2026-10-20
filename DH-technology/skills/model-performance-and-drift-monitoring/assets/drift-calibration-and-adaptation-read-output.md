# Output format: drift, calibration and adaptation read

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/drift_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 2 to 5 from `scripts/drift_check.py drift` and `adaptation` output; do not recompute by hand. Budget in words: answer 70, scope 40, performance 100, inputs 60, engine 80, safety records 40, record 45.

1. **Answer** (two sentences): what moved between the reference and the latest period, which of your thresholds were crossed (or "thresholds not given"), pending outcomes, and for an engine the decisions outside its rules.
2. **Scope:** model and version · reference period · periods · read date · thresholds file and date written (or "not given").
3. **Performance and calibration by period:** Period · Outcomes known · Event rate · O/E · AUROC · Calibration slope · Flags (your thresholds); the Davis pattern quoted (DA-92); "stable" is your reading.
4. **Inputs:** Input · Period · Missing share · SMD · Flags (your limits).
5. **Engine (if any):** decisions outside allowed options (dates); missing-data rule not followed (count); per-option rates labeled descriptive (TM90).
6. **Public safety records (named product only):** title · date · severity · manufacturer as stored; MAUDE counts unattributed; empty is not evidence of safety.
7. **Calls made**, then one line offering the full version.
8. **Record (the very last line, nothing after it):** "Monitoring read draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Scope and your thresholds (with date written)
### Performance and calibration by period (script output)
| Period | Predictions | Outcomes known | Event rate | Mean predicted | O/E | AUROC | Calibration slope | Sensitivity at your threshold | Flags (your thresholds) |
|---|---|---|---|---|---|---|---|---|---|
### What moved (facts, no verdict)
### Inputs against the reference period
| Input | Period | Mean | SD | Missing share | SMD | Flags (your limits) |
|---|---|---|---|---|---|---|
### Groups, latest period
### Personalization engine against its rules
| Decision point | Decisions | Outside allowed options | Missing data, rule not followed | Per-option rates (descriptive) |
|---|---|---|---|---|
### Engagement by week
### Public safety records (as stored)
| Record | Date | Severity | Manufacturer as stored | Source |
|---|---|---|---|---|
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Monitoring read draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
