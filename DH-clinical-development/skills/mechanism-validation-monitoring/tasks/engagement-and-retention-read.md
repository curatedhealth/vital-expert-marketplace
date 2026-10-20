# A3 Engagement and retention read

Framework task: DH-01.01.2.2, Part A, task A3. Folds in DH-01.06.3.2 Engagement Effectiveness Assessment & Retention Quality Monitoring (register CF-12.01.06.3.2): the old sections "Engagement & Retention Monitoring" (DH-01.06.3.2.1, CF-12.01.06.3.2.1) and "engagement retention pass rule" (DH-01.06.3.2.2, CF-12.01.06.3.2.2, now steps 1 and 2 here). The old "engagement retention miss owner" (DH-01.06.3.2.3) is part of B1.

## What this task delivers

Usage and dropout for one cohort on one version, measured against the definitions the person picked before reading the data: weekly usage volume and frequency with discontinued users included, the number and share discontinuing and completing, when people dropped out, and the comparison with the person's thresholds. Where the product is a DiGA, the DiGAV § 23c definitions (SE70 to SE73) are offered as the person's choice. Engagement is reported as the "used" link of the mechanism, never as the outcome.

Why it matters: the relationship between engagement and outcomes "may not be well understood" (SE26), and usage-outcome correlations can be confounded by motivation (SE82, Perski 2017, DOI 10.1007/s13142-016-0453-1). A figure called adherence without a justified intended use is usage (SE92, Sieverink 2017, DOI 10.2196/jmir.8578).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`); the old DH-01.06.3.2 files bound `behavior-change-designer` (BUILD_NOTES) |
| Skill | DH-01.01.2.2 Part A, Engagement and retention read |
| Workflow | The steps below |
| Knowledge | `references/engagement-read-rules.md`; rows SE26 and SE69 to SE77; SE79 to SE85 (Perski 2017, DOI 10.1007/s13142-016-0453-1); SE86 to SE88 (Michie 2017, DOI 10.2196/jmir.7126); SE90 to SE93 (Sieverink 2017, DOI 10.2196/jmir.8578); SE94 to SE99 (CONSORT-EHEALTH, DOI 10.2196/jmir.1923); A1 plan rows TM57 (ORBIT, DOI 10.1037/hea0000161), CS32 (Proctor, DOI 10.1007/s10488-010-0319-7) |
| Tools | `scripts/engagement_read.py` on the person's usage file. No library call is needed; for a named product's public record, `regulatory-dh.get_authorization` (precedent identity only) |
| Prompt | This guide |
| Template | `assets/engagement-and-retention-read-output.md` |
| Input | The request and its context; the usage export; the version; the data cut; the definitions and thresholds the person set, with the date they were set |
| Governance | `references/governance.md`; definitions, thresholds and targets are the person's |
| Catalogue job | none (no saved `list_jobs` output shows an engagement or retention job; `examples/live/connector_calls_2026-10-20.json`) |

## Read the request

- **Definitions.** What counts as a session, an active week, discontinuation and completion; the window; the denominator. Were they set before the data were read, and when? If none exist, write them with the person first (step 1); nothing is compared until they exist.
- **DiGA or not.** Use the DiGAV § 23c definitions only if the person says the product is a DiGA or asks for them. Whether the DiGAV applies is `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- **Version and data cut.** As the person gave them; otherwise "not given" and ask. A read spans one version.
- **Adherence or usage.** Is there an intended use with a stated justification? If not, the word is "usage".
- **Privacy.** Usage data stay local; never send user rows to a library call.

## Workflow

### Step 1. Write the definitions before reading (old "pass rule", step 1)

List the elements that count, as the old pass rule did ("cohort, return action, and window"): the cohort, what counts as use (session or minutes, from which measurement route, SE80, Perski 2017, DOI 10.1007/s13142-016-0453-1), the window, the discontinuation rule, completion, and the denominator. Each is the person's. Offer the DiGAV § 23c items where the product is a DiGA (SE70 to SE73) and say they are a regulator-set definition, not a target (SE72). Record the date the definitions were set. A definition set after the data were read is labeled so; its result is exploratory and never compared (TM57, ORBIT, DOI 10.1037/hea0000161).

### Step 2. Thresholds, the person's (old "pass rule", steps 2 and 3)

Ask for the threshold on each measure the person wants judged (for example the discontinued share), and which element, if missed, the person treats as blocking (old pass rule step 3; the person names it). No benchmark is sourced (`engagement-read-rules.md` "Never"); do not offer one. Without a threshold, values are reported without a verdict.

### Step 3. Run the read

With code execution, run `python3 scripts/engagement_read.py --definitions DEFS.json --data USAGE.csv --version "<version>"`, adding `--as-of YYYY-MM-DD` only with the data cut the person gave. Never pass today's date. Without a cut the script prints "data cut not given", marks users whose last gap cannot be judged "not determinable", and compares nothing. Check its output against the file before quoting; never impute.

### Step 4. Report the SE73 items and weekly usage

Report the number and share discontinuing, the weekly distribution, the number and share completing, the mean days to discontinuation (with the script's stated reading of which day counts, for the person to confirm), and weekly minutes and sessions with discontinued users included (SE71). Show the per-user median beside the mean when one user carries the mean. If that user's rows are identical every day, list it as a data check for the person (a fact from the file, not a judgment of the user). Read by week, not as one snapshot (SE79, Perski 2017, DOI 10.1007/s13142-016-0453-1). State the version and whether content changed in the period (SE98, CONSORT-EHEALTH, DOI 10.2196/jmir.1923).

### Step 5. Compare with the person's thresholds, and name what this is

Mark each measure within or outside the person's threshold. Say in words: this is the "used" link; it does not show the outcome (SE26; CS32, Proctor, DOI 10.1007/s10488-010-0319-7); whether a level is "effective engagement" is for A1 and A2 to test (SE86, Michie 2017, DOI 10.2196/jmir.7126). If the person asks whether a figure is "good", say no source sets a benchmark and the threshold is theirs.

### Step 6. Hand on

A use measure outside the person's threshold goes to B1 as a use-link miss. A very high usage level where the design named an overuse, screen-time or sleep risk goes to A4 as a candidate signal (SE16, SE29), described as a level only. If nonuse is high, note that a qualitative look at why is called for (SE99, CONSORT-EHEALTH, DOI 10.2196/jmir.1923); who does it is the person's choice. Any wording for BfArM goes to the owner the person names, via `dh-regulatory-and-quality` regulatory-submission-and-dossier; whether the DiGAV applies goes to `dh-regulatory-and-quality` regulatory-pathway-and-classification. Offer a facts-only draft.

## Build the output

Follow `assets/engagement-and-retention-read-output.md`. Answer first: version, data cut, definitions used and when set, discontinued and completed shares, weekly usage, and each comparison with the person's threshold. Where no owner is named, write "owner not named" in the answer and ask, before the record line: "Who owns the definitions and thresholds, any wording for BfArM, and the next step on a miss, and who clears this draft? A name or role in your words." Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every definition and threshold is the person's, with the date set; none set after the data is compared.
- No benchmark, retention target or "good" rate appears.
- Engagement is never called the outcome, "effective", or evidence the product works; no mechanic is called "safe", "effective" or "compliant".
- "Adherence" appears only with the person's justified intended use; otherwise "usage".
- Every [PAPER] row id carries its own paper's DOI: once in prose at first use, and in every table cell that holds it, even if given earlier; rows from different papers each keep their own DOI. Abstract-only and [WF] rows carry their label every time they are applied.
- No job title appears that the person did not use; owners are the person's words or "owner not named". Where no owner is named, the answer writes "owner not named" and asks, before the record line: "Who owns the definitions and thresholds, any wording for BfArM, and the next step on a miss, and who clears this draft? A name or role in your words." No date, data cut, threshold or status appears that the person did not give or a record does not state.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Designing engagement mechanics, loops and adherence features: therapeutic-mechanism-and-intervention-design (DH-01.01.2.1).
- Whether the DiGAV applies and what goes to BfArM: `dh-regulatory-and-quality` regulatory-pathway-and-classification and regulatory-submission-and-dossier; DiGA outcome measurement as reimbursement: `dh-access-and-value` coverage-pathway-and-access-strategy.
- Adoption across customer accounts: `dh-go-to-market` adoption-monitoring. Patient engagement programs: `dh-patient-and-user-experience` engagement-kpi-dashboards.
- Usability findings behind low use: `dh-patient-and-user-experience` usability-monitoring.
