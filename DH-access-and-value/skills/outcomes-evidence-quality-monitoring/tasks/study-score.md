# A2 Study score

Framework task: DH-01.07.3.2, Part A, task A2. Replaces the earlier "Study score" section (CF-12.01.07.3.2.2): "Score only with the rule the buyer supplied."

## What this task delivers

A portfolio view of the person's evidence: per result, the reviewers' domain judgments, the overall level where the tool fixes it, the overall level under the person's rule where it does not, a score only under the person's points and weights, and counts across the portfolio. It answers "given our judgments and our rule, where does each result stand, and what changed since the last review?"

Why it matters: evidence portfolios are reviewed again and again, by different people. A tally that applies the same written rule each time makes results comparable and changes visible. A score without a written rule, or a score presented as validated, misleads: no validated quality score exists for CHEERS (HE-005), and GRADE is not a quantitative system (ES-94).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Clinical Trials Director |
| Skill | DH-01.07.3.2 Part A, Study score |
| Workflow | The steps below |
| Knowledge | `references/rigor-checks.md` sections 1 to 3 and 9 |
| Tool | `scripts/rigor_tally.py` (local); A1 for any result not yet checked |
| Catalogue job | none |
| Prompt | This guide |
| Template | `assets/study-score-output.md` |
| Input | The request; the reviewers' judgments per result and domain (a sheet or a list); the person's rule (overall level for ROBINS-I below critical, points, weights); the previous tally if this is a re-review |
| Governance | `references/governance.md`; judgments and rules are the person's |

## Read the request

- **Judgments in hand.** Who judged, with which tool and version. If none exist, offer A1 to lay out facts first; never judge on the reviewers' behalf.
- **The rule.** Whether the person has one. If not, Step 2 writes it with them.
- **Re-review.** If a previous tally exists, ask for it to show changes.

## Workflow

### Step 1. Collect the judgments

Write them as `study_id, result_id, tool, domain, judgment, note` (see `examples/illustrative_judgments.csv`). Levels in the tool's own words (ES-73, ES-76; RoB 1 for a JCA: Low, High, Unclear, ES-172). Check: every domain judged, levels valid for the tool, ROBINS-I version stated (2016 published; V2 is a draft, ES-80).

### Step 2. Write the person's rule

What the sources fix, applied always: ROBINS-I critical in any domain means critical overall and no synthesis (ES-77); RoB 2 overall is the least favorable domain (ES-74); RoB 1 per outcome is High if any key domain is high, Low if all are low, otherwise Unclear, with the key domains the reviewers' choice (ES-192 [PAPER] DOI 10.1136/bmj.d5928); where two or more domains are "Some concerns", say that ES-74 lets reviewers judge the result High overall, and leave that call to them. What the person sets: the ROBINS-I overall below critical (the sourced rows do not fix it `[GAP]`; "least favorable domain" is available as a proposal), and, only if they want a score, points per level and weights per domain. Write the rule back in their words with the person who owns it.

### Step 3. Run the tally

`python3 scripts/rigor_tally.py JUDGMENTS.csv RULE.json --md OUT.md`, or apply the same rules by hand. The script refuses to score a result with an unjudged domain or an unscored level, and labels every score "your rule, not a validated score".

### Step 4. Read the portfolio

Counts per overall level. Results at critical risk are excluded from any synthesis (ES-77): name them. Results with "No information" in a domain: name the domain. If a previous tally exists, list what changed and why (new judgment, new rule, new study, retraction from A1).

### Step 5. Certainty context, not a rating

For each outcome, restate that non-randomized evidence starts low in GRADE and sound non-randomized studies are generally graded low (ES-90, ES-100), and that rating down for risk of bias is one of five domains (ES-91). If the person asks what a level means, quote the GRADE definitions (ES-195 to ES-198). The certainty rating is the person's or the HTA body's; once they give it, word any finding with the Table 15.6.b verb for that rating (ES-203 to ES-207), and use no certainty verb before.

## Build the output

Follow `assets/study-score-output.md`. Short mode: the answer (counts per level, which results are excluded, the single most common weak domain), the tally table, at most three open items, the record line. Full mode adds the rule as written, per-domain judgments, changes since the last tally and the certainty context.

## Before you hand it over

- Every judgment and every rule element is attributed to the person or their reviewers.
- Every score says "your rule, not a validated score".
- Critical results are named as excluded from synthesis, with ES-77.
- The record line ends the answer: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft."

## Boundaries

- The model does not judge, set points or weights, or rank studies by a score it invented.
- Ranking with `analytics.mcda` is not used: it would turn judgments into a weighted value the sources do not support. If the person insists, it ranks only their scores with their weights, labeled as such.
- Certainty ratings and dossier inclusion stay with the person and the HTA body.
