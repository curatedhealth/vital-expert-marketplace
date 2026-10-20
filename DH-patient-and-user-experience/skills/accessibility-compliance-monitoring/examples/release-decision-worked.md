# Worked example: A2 issue log summary and B1 release decision

Run on 19 October 2026. The issue log (`sample-data/issue_log_illustrative.csv`) and the person's rule and scores are written for this example and are illustrative. The script outputs and the ranking calls are real (`sample-data/issue_log_summary_2.2AA.md`, `sample-data/issue_log_summary_2.1AA.md`, `live/rice_barrier_fixes.json`).

**Request:** "Here's our accessibility log for build 4.2 of the medication app. Our requirement says WCAG 2.2 AA. Our rule is the one from the register: block if a day-one task has an open break, later screens only with a named exclusion. Day-one tasks for us are sign-in, create account and log a dose. Can we ship, and what do we fix first? Our scores for the two oldest day-one items: dose button name reach 3,100, impact 3, confidence 100 percent, effort 1; sign-in puzzle reach 4,200, impact 3, confidence 80 percent, effort 3. Release decisions are made by our Head of Product, Dana."

**Calls and runs**

1. `python3 scripts/a11y_issue_log.py sample-data/issue_log_illustrative.csv --version 2.2 --level AA --as-of 2026-10-19`
2. The same with `--version 2.1`, for the comparison line.
3. `analytics.rice` with the two repairs, confidence passed as a percent (80, 100). Response: dose button name 9,300; sign-in puzzle 3,360. An earlier call with confidence as fractions (0.8, 1) returned scores 100 times smaller in the same order (register N5 evidence).

## Answer (short mode)

**Your rule says block build 4.2.** Four open in-target issues sit on day-one tasks, and your rule allows no exclusion for a day-one task. The decision is Dana's.

| Clause | Facts it reads | What it says |
|---|---|---|
| Block if a day-one task has an open break | A11Y-04 4.1.2 Name, Role, Value (A), log a dose, open 111 days; A11Y-01 3.3.8 Accessible Authentication (Minimum) (AA), sign-in, 76 days; A11Y-03 2.5.8 Target Size (Minimum) (AA), log a dose, 34 days; A11Y-11 3.3.7 Redundant Entry (A), create account, 13 days | Block |
| Later screens only with a named exclusion | Three open in-target issues on later screens: A11Y-07 (settings, 160 days), A11Y-05 and A11Y-06 (symptom diary) | Allowed only if you name an exclusion for each; none named yet |

**Your repair order (from your scores):** dose button name 9,300, then sign-in puzzle 3,360. Both are day-one items; the other two day-one items are not scored.

**What the target changes:** against 2.1 AA, three of the four day-one issues (3.3.8, 2.5.8, 3.3.7) fall outside the target, because they are new in 2.2 (UX-STD-07). Your requirement says 2.2, so they count.

**Outside your target, kept in the log:** A11Y-08 4.1.1 Parsing (removed in 2.2; test and report only if a 2.0 or 2.1 policy applies, UX-STD-08); A11Y-10 1.4.6 (AAA).

**About the log:** 5 of 12 issues came from automated tools. Automated tests check only part of what needs testing (UX-UK-24), and the 45 in-target criteria with no issue logged are not passes. Data problems: A11Y-12 is logged as AA but 1.1.1 is Level A; it is marked fixed with no closed date.

**Stops:** the release decision, any exclusion and any accessibility statement are Dana's.

**Record:** Release decision draft. Decision: ______ (by Dana). Uncleared. AI-assisted.

The full version adds the full issue table and the exclusion fields.

## What this example shows

- The model applied the person's adopted rule clause by clause and left the decision line blank.
- The target matters: the same log gives four day-one blockers at 2.2 AA and one at 2.1 AA (`issue_log_summary_2.1AA.md`).
- The ranking is the person's scores run through the connector, with the confidence-unit pitfall caught.
