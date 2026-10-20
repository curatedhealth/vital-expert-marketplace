# Output format: engagement and attrition computation

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the two or three figures that answer the question, each with numerator over denominator, period and as-of date (for example usage half-life per group, share still using at a day the person names).
1a. **How to read it:** one line: "Kaplan-Meier counts people still using at the as-of date as censored, not stopped (KX1, doi:10.2196/jmir.7.1.e11); raw proportions at late days rest only on the earliest enrollees."
2. **Figures (compact):** KPI or point · Value · Numerator / denominator · Your threshold · Met / missed. With no thresholds, skip the last two columns and ask once.
3. **Data notes:** rows excluded and why, in one line.
4. **What it means for you:** two lines, conditional, no cause.
5. **Rules used:** start event, use event, days without use, dose, period (yours).
6. **Record:** "Computed on your data, as of DATE, run DATE. Clears: NAME, the owner you named (or 'owner not named'; ask). Uncleared draft: once NAME clears it, the record is built with `verify.build_record`."
7. One line offering the full version.

## Full mode

### Answer

### Run
As-of date · run date · file · rows used · rows excluded (by reason) · rules used.

### KPIs
| KPI | Numerator | Denominator | Value | Period | Your threshold (set by) | Met / missed |
|---|---|---|---|---|---|---|

### Nonusage attrition (per group)
| Day | Enrolled at least this long | Stopped before this day | Raw stopped proportion | Kaplan-Meier still using |
|---|---|---|---|---|
t10 · t25 · t50 (usage half-life), or "not reached within the data".

### Comparison between groups (descriptive)
| Group | Stopped by day H | Relative risk vs reference |
|---|---|---|
No test of significance; no cause.

### Dropout attrition (follow-up waves)
| Wave (due day) | Due | Completed | Dropout |
|---|---|---|---|

### What it means for you

### Hypotheses for you to test (labeled)
| Hypothesis | What would confirm it |
|---|---|

### Gaps

### Record
Computed on your data with your rules. Engagement figures are not clinical evidence. AI-assisted. Clears: NAME, the owner the person named, or "owner not named". Uncleared draft until NAME clears it; the record is then built with `verify.build_record`.
