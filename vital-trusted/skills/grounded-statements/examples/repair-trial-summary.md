# Worked example: repairing a trial summary

Invented case for teaching. "ZELORA-2" and "zelorastat" are fictional; no real product,
trial or person.

## Supplied material (abstract)

> ZELORA-2 was a randomized, double-blind, placebo-controlled phase 3 trial in adults with
> chronic condition X. 600 patients were randomized 1:1. The primary endpoint was the
> proportion of patients with a major event by week 52: 6.0% with zelorastat versus
> 9.0% with placebo (hazard ratio 0.66, 95% CI 0.45 to 0.97). In a post hoc analysis of
> patients aged 65 and over, the hazard ratio was 0.52. Serious adverse events occurred in
> 11% of the zelorastat group and 10% of the placebo group.

## Draft to repair

> ZELORA-2, the largest trial ever conducted in condition X, showed that zelorastat cut
> major events by 34%. In older patients the benefit was even greater, nearly halving
> the risk. Zelorastat reduces events because it restores pathway Y. Serious adverse
> events occurred in 11% of patients.

## Repaired text

> ZELORA-2 was a randomized, double-blind, placebo-controlled phase 3 trial of 600 adults
> with condition X. By week 52, a major event occurred in 6.0% of patients on zelorastat
> and 9.0% on placebo: an absolute difference of 3.0 percentage points (hazard ratio
> 0.66, 95% CI 0.45 to 0.97). In a post hoc analysis of patients aged 65 and over, the
> hazard ratio was 0.52 [GAP: not supplied — number of patients and confidence interval
> for this subgroup — supply the subgroup table]. Serious adverse events occurred in 11%
> of patients on zelorastat and 10% on placebo.

## Repair note (as the person sees it)

What I changed and why (draft, not yet reviewed)

Based on: ZELORA-2 abstract (supplied)

Changed
1. "the largest trial ever conducted in condition X" → "a randomized, double-blind,
   placebo-controlled phase 3 trial of 600 adults". The abstract does not say it is the
   largest; size and design are what it does say.
2. "cut major events by 34%" → the event rates in both groups, the difference between
   them and the hazard ratio. 34% is a relative figure; on its own it hides that the
   difference is 3 percentage points (9.0% vs 6.0%).
3. "In older patients the benefit was even greater, nearly halving the risk" → stated as
   an unplanned (post hoc) analysis in patients aged 65 and over, with its hazard ratio.
   "Even greater" is gone: nothing supplied compares the two groups formally.
4. "because it restores pathway Y" → removed. The abstract gives no mechanism.
5. "Serious adverse events occurred in 11% of patients" → both groups given (11% vs 10%),
   so the reader does not assume placebo had none.

Left as gaps for you to fill
1. Number of patients and confidence interval for the age 65+ analysis — from the
   subgroup table.

Questions for you
1. Should the hazard ratio or the event rates lead? Both are now given.

Next step: if this goes to doctors or other external readers, it goes through your
medical or promotional review process before it is used.

I compared the draft with what you gave me; I did not check it against the original
sources with a tool.

## Behind the note (reference only, not shown to the person)

Patterns: F2, N1, M2, F5, M8 in `references/patterns.md`. Rule R1 (CONSORT 2025,
absolute and relative effects) supports change 2; R3 supports change 3.

## Script used

```
python scripts/risk_metrics.py --treat-rate 0.06 --ctrl-rate 0.09
```

Derived: risk difference −3.0 percentage points; relative risk 0.667 (crude, from
rates). The abstract's hazard ratio of 0.66 is a time-to-event estimate and is reported
as given, not replaced by the crude figure.
