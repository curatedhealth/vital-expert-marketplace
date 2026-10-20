# Output format: metric definition and certification

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/metric_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 2 and 3 from `scripts/metric_check.py cards` and `recompute` output; do not recount by hand. Budget in words: answer 60, card flags 130, recomputation 70, certification 70, access 60, record 45.

1. **Answer** (two sentences): how many cards carry which flags, any duplicate pair, the recomputed figure beside the shown figure with the difference, and what the certifier must decide. No certification by the model.
2. **Card flags:** Metric · Owner · Flags with rows (CMS MMS Hub, read 20 October 2026, DA-133 to DA-137, CMS quality-measure guidance used as a checklist).
3. **Recomputation:** recomputed rate from your file and rules · figure shown · data timestamp · difference; "no tolerance is sourced; whether it matters is your rule".
4. **Certification:** your rule verbatim (or "not given"); elements met and not met; "pass or refuse is the certifier's".
5. **Access** (only if asked): roles that publish and explore as you set them; PHI facts where they apply (45 CFR 164.502 and 164.514, CS103 to CS105; Security Rule EN-101, EN-103; the January 2025 NPRM is a proposal, EN-106, EN-107).
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Metric and certification draft for the certifier. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Metric cards against the checklist
| Metric | Owner | Status | Version | Flags | Source and rows |
|---|---|---|---|---|---|
### Duplicates recomputed beside a certified metric
### Source data terms (Kahn 2016, DA-94 to DA-98, DOI 10.13063/2327-9214.1244; FAIR, DA-100, DOI 10.1038/sdata.2016.18)
### Dated standards in play (USCDI published versus required for certification, DA-108 to DA-111; OMOP version, DA-103 [SPEC])
### Recomputation from your rows
| Stratum | Denominator | Numerator | Rate | Figure shown | Difference |
|---|---|---|---|---|---|
### Changes and corrections (version or correction, who is told)
### Certification record for the certifier
| Rule element (yours) | Met, not met or not given | Evidence |
|---|---|---|
### Templates
### Publish and explore rights as you set them, with the facts beside them
| Role | Publish | Explore | No export | Source and rows |
|---|---|---|---|---|
### Center of excellence (charter, decision log, dispute) in your words
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Metric and certification draft for the certifier. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
