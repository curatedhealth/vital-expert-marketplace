# Output format: engagement and retention read (draft for the person)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** version and data cut, each as the person gave it or "not given" (never today's date); the definitions used (the person's, or DiGAV § 23c where the person chose them) and the date set; discontinued and completed shares with n; mean weekly minutes and sessions (median beside the mean); each comparison with the person's threshold, or "no threshold; no verdict". If one user carries the mean and their rows are identical every day, list it as a data check for the person (a fact from the file, not a judgment of the user).
2. **Measures:** table Measure · Definition (whose, date set) · n · Value · Person's threshold · Within / outside / not compared · Rows (each [PAPER] row with its own DOI).
3. **When people stopped:** discontinuations by week; mean days to discontinuation with the reading of which day counts, for the person to confirm.
4. **What this is:** the "used" link, not the outcome (SE26; SE82, Perski 2017, DOI 10.1007/s13142-016-0453-1); "usage", not adherence, unless the person gave a justified intended use (SE92, Sieverink 2017, DOI 10.2196/jmir.8578); no benchmark is sourced.
5. **Handed on:** use misses to B1; any level the design tied to an overuse or screen-time risk to A4, as a level only; any wording for BfArM to the owner the person names, via `dh-regulatory-and-quality` regulatory-submission-and-dossier, and whether the DiGAV applies via `dh-regulatory-and-quality` regulatory-pathway-and-classification; offer a facts-only draft.
6. **Owner question (only if the person named no owner):** write "owner not named" and ask, before the record line: "Who owns the definitions and thresholds, any wording for BfArM, and the next step on a miss, and who clears this draft? A name or role in your words."
7. **Record (last line of the answer body):** "Engagement read draft. AI-assisted. Usage only; not an outcome; no benchmark applied." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
8. **Calls made (after the record line):** list.

## Full mode

### Answer
### Version, data cut, content changes in the period (as the person gave them; "not given" otherwise)
### Definitions (the person's, with date set; set before or after the data)
| Element | Definition | Source of the definition | Rows |
|---|---|---|---|
### SE73 items
| Item | n | Value | Threshold | Result | Rows |
|---|---|---|---|---|---|
### Weekly usage volume and frequency (discontinued users included)
### Per-user spread (median, highest user; identical daily rows for one user listed as a data check)
### Not compared (definition set after the data, no threshold, no data cut)
### Handed to B1 and A4, with routes for BfArM wording and DiGAV applicability (`dh-regulatory-and-quality` regulatory-submission-and-dossier, regulatory-pathway-and-classification)
### Owner question (only if the person named no owner; before the record line)
"owner not named", then: "Who owns the definitions and thresholds, any wording for BfArM, and the next step on a miss, and who clears this draft? A name or role in your words."
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
