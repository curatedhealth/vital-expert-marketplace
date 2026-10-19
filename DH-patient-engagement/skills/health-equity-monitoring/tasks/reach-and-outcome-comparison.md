# A2 Reach and outcome comparison

Framework task: DH-02.03.4.2, Part A, task A2. Replaces the earlier "Reach score" section (CF-12.02.03.4.2.2).

## What this task delivers

Reach and outcome rates per subgroup, computed by `scripts/equity_compare.py` from the person's aggregate counts: rates with 95 percent intervals, the difference and ratio against the reference group the person names, each subgroup's share of the eligible and of the reached, the share not recorded, and the cells hidden under the person's small-cell rule. It answers "what do our counts show by subgroup?"

Why it matters: an overall rate can rise while one group falls behind. The register's rules: count the record in the period, compare it with the users in that group or mark the denominator `[GAP]`, keep the definition used, never report a rate without a denominator.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.03.4.2 Part A, Reach and outcome comparison |
| Workflow | The steps below |
| Knowledge | `references/equity-measures.md`; A1 evidence definition; PE rows |
| Tools | `scripts/equity_compare.py` (local). Optional `literature.search_literature`, `verify.qualify_source`, `verify.check_claim` for published context. `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/reach-and-outcome-comparison-output.md` |
| Input | The request and its context; a CSV or table of counts per subgroup (`dimension, subgroup, eligible, reached`, optional `outcome_n, outcome_met`); the reference subgroup per dimension; the small-cell rule; the period |
| Governance | `references/governance.md`; no verdicts in A2; counts stay out of library calls |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. evidence-table grades a set of studies for a product's claims; this task only identifies or checks a source the person names. |

## The rule that shapes this task: compute, suppress, do not judge

Numbers come from the script on the person's counts, under the person's small-cell rule and reference. A2 reports them without "good", "bad", "significant" or "closed". Verdicts need the person's rules (B1).

## Read the request

- **Counts.** Aggregate counts per subgroup. If the person gives rates or percentages, ask for counts. If they paste a table, write it to a CSV with the columns above.
- **Evidence definition.** From A1. If none, ask for the record of use, denominator and period in one line each, and note "A1 not run".
- **Reference.** One subgroup per dimension, chosen by the person. Without one, rates only.
- **Small-cell rule.** Required. Ask; do not choose.
- **Period.** State it exactly as the person labeled it (for example 'Q3 2026, as labeled'). Do not convert a quarter label to dates; ask for start and end dates if the output needs them.
- **Earlier period.** If the person has counts for a previous period, run the script on each and compare the outputs side by side; the script itself handles one period.

## Workflow

### Step 1. Check the counts

Check, with the script's own checks: reached not above eligible; outcome measured not above reached; counts are whole numbers; eligible totals match across dimensions (the script notes a mismatch, which usually means different populations or periods).

### Step 2. Run the script

```
python scripts/equity_compare.py counts.csv --min-cell <person's rule> --reference "<dimension>=<subgroup>" [--reference ...] [--suppress-zero] [--json out.json]
```

### Step 3. Read the output

For each dimension: reach per subgroup with interval; the difference and ratio against the reference; share of eligible against share of reached (under-represented among the reached where the second is lower); the outcome among those reached; the share not recorded; suppressed cells and why (primary or complementary). Keep reach and outcome apart: a group with low reach and a high outcome rate is still mostly not reached.

### Step 4. Published context (optional)

Only if the person asks how their gaps compare with published work: `literature.search_literature` on the intervention and population, read titles, then `verify.qualify_source {doi}` and `verify.check_claim` with a passage you read that states the finding in the same direction. Label it "published context about another population, not a target". Never turn a published figure into the person's threshold.

## Build the output

Follow `assets/reach-and-outcome-comparison-output.md`. Answer first: the subgroups with the largest gaps against the reference, in numbers with intervals, and what is hidden or not recorded. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rate has its count and denominator, or is suppressed and says so.
- No count below the person's threshold appears anywhere in the output, including prose.
- The reference group and small-cell rule are stated as the person's.
- No verdict words.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Aggregate counts only; no patient-level data, no modeling of individuals.
- Not a statistical significance test or a causal analysis (dh-advanced-analytics for those).
- Accessibility conformance results come from the dh-user-experience accessibility skills.
