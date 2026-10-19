# Session evidence and the System Usability Scale

Interpretive reference for A2 (session evidence) and B1 (research action). Row ids as in the copied research files and `user-research-additions.md`.

## What a session record holds

The register task this replaces asked for three things: where each participant succeeded and where they stopped, their own words for a confusion, and a count of participants who hit the same stop. The sources add:

| Element | Rule | Rows |
|---|---|---|
| Outcome per task | Record completed, stopped or assisted in the person's own labels; never infer the outcome from a quote. | Register method |
| The participant's words | Quote verbatim; never paraphrase into a finding before the sessions are done (register "Do not"). | Register method |
| Count by user group | Distinct participants per stop, per group. A stop seen only in clinicians says nothing about patients (UX-US-36). | UX-US-36 |
| Critical-task flag | The person's (or their regulatory owner's) flag, never the model's. | UX-US-28, UX-UK-18 |
| Use error | FDA's three-part definition: an action or inaction different from what the manufacturer expected, a result the user did not expect, not caused solely by device failure, that did or could cause harm. MHRA: users may not know a use error occurred; device malfunction is not use error. The model records what happened; whether it is a use error is the owner's call. | UX-US-27, UX-UK-15 |
| Training gap | Testing immediately after training overstates retention; FDA expects a delay in validation. In formative sessions, record when training was given. | UX-US-41 |
| User interface scope | The UI includes packaging, labeling, training materials, controls, displays, alarms and logic. A stop in the instructions is a UI stop. | UX-US-31 |
| Saturation | No new relevant information emerging; FDA sets no criteria for evaluating it (PE-09). Report whether the last sessions added new stops; do not declare saturation. | PE-09 |

`scripts/research_log.py stops` produces the counts from a session log. It applies "repeated" only when the person gives a minimum.

## The System Usability Scale (SUS)

**Scoring.** As restated by Hyzy et al. 2022 (DOI 10.2196/37290): subtract 1 from odd-item ratings, subtract even-item ratings from 5, each item scores 0 to 4, sum and multiply by 2.5, giving 0 to 100 (UX-M-07). Brooke's original was not read; the scoring rests on this restatement. `scripts/research_log.py sus` applies it per respondent and summarizes by group or round.

**Missing items.** The sources give no rule for a missing or out-of-range item. The script excludes such responses and counts them; it does not impute `[GAP]`.

**Context figures, never targets.** All rows below are [PAPER] rows from Hyzy et al. 2022 (DOI 10.2196/37290); cite the row id and the DOI whenever an answer uses them.

| Figure | Basis | Rows |
|---|---|---|
| Mean 68 (SD 12.5) | General SUS benchmark, cited by Hyzy et al. from Sauro and Lewis (446 studies, 5000 responses; book not read) | UX-M-08 |
| Mean 76.64 (SD 15.12) | 117 SUS scores for 114 digital health apps, 2011 to 2021, one meta-analysis | UX-M-09 |
| Mean 68.05 (SD 14.05) | Same set excluding physical-activity apps (those averaged 83.28) | UX-M-09 |
| Authors' conclusion | The 68 (SD 12.5) benchmark is suitable for digital health apps; one meta-analysis with its own limits | UX-M-10 |

Rules:

1. The person decides whether a SUS score is acceptable. A published mean is context beside their number, labeled with its basis, never a pass mark.
2. Report n beside every mean, by user group. Small groups give unstable means; say how many responses each figure rests on.
3. A SUS score does not show that a product is safe or easy to use for its critical tasks; it is a perceived-usability questionnaire. Never write "usable", "easy to use" or "validated" from a SUS score; such wording stops for the owner (governance).
4. Adjective bands (for example "good" or "excellent") are not sourced: Bangor, Kortum and Miller (2009) was not read `[GAP]`. Do not label scores with adjectives.
5. Comparing rounds: report the difference of means and each round's n. No significance test is in the sources; do not call a change significant.
6. Literature claims about SUS go through Verify in two steps (`references/tools.md`) and are accepted only with a passage that states the claim in the same direction (register N3).

## From stops to actions (B1)

| Point | Rule | Rows |
|---|---|---|
| What counts as repeated | The person's rule. The register's starter rule is "more than one participant"; offer it as theirs to adopt, never as a default. | Register method |
| Severity before count | A stop on a critical task goes to the owner even if one participant hit it, because severity of harm matters more than probability (UX-US-32). | UX-US-32 |
| Action or refusal | Each repeated stop gets a design or content change, or a refusal with a reason. Never leave a stop only in a recording (register "Do not"). | Register method |
| Order of fixes | Design first, then protective measures, then information (UX-US-33). | UX-US-33 |
| Wording-only fixes | For critical tasks, a labeling or training fix needs new data showing it works (UX-US-42); plan a retest. | UX-US-42 |
| Release | Name the release that will show an accepted change (register method). The release and date are the person's. | Register method |
| Ranking | Only if the person supplies reach, impact, confidence and effort for each action: `analytics.rice` (`references/tools.md`). | Tool |

## Gaps

- SUS adjective bands, Brooke (1996, 2013) and Sauro and Lewis (2016) not read `[GAP]`.
- No sourced rule for SUS missing items or for comparing small samples `[GAP]`.
- No sourced severity scale for formative findings; severity is the person's `[GAP]`.
