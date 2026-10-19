# Equity measures: definitions, comparison and suppression

Interpretive reference for A1, A2 and B1. Rows cite `patient-engagement-equity-research.md` (PE). Read on 19 October 2026. Where a choice is a computation choice of this skill rather than a sourced rule, it says so.

## Definitions the person can adopt

| Term | Sourced definition | Row | Use here |
|---|---|---|---|
| Health disparity | A measurable difference in health between specific population groups | PE-124 | A difference in the person's counts is a measured difference; calling it a disparity is the person's framing |
| Engagement | Extent of use (amount, frequency, duration, depth) plus a subjective experience | PE-105 [PAPER], doi:10.1007/s13142-016-0453-1 | Counts measure only the behavioral part |
| Effective engagement | Enough engagement to achieve intended outcomes, defined empirically | PE-104 [PAPER], abstract only, doi:10.1016/j.amepre.2016.06.015 | Why reach alone is not the end point; pair reach with an outcome |
| Dropout attrition | Loss to follow-up | PE-102 [PAPER], doi:10.2196/jmir.7.1.e11 | Separate from nonusage in the counts |
| Nonusage attrition | Stopping use | PE-102 [PAPER] | |
| Attrition reporting | Raw attrition proportions over time as curves, relative risk of dropping out or stopping use, usage half-life | PE-103 [PAPER] | Suggests a ratio against a reference, which the script computes |
| Law of attrition | In any eHealth trial a substantial share of users drop out or stop using the application | PE-101 [PAPER] | Expect falls at each step; the question is whether they differ by group |

The register's own rules (old tasks "Equity evidence", "Reach score", "Equity follow-up"): name the change and the group, name the record (completed task, supported site, language used), set the period; do not use a policy statement as evidence; count the record in the period and compare it with the users in that group, or mark the denominator `[GAP]`; keep the definition used; do not report a rate without a denominator; do not close the question because the change shipped.

## The evidence definition (A1)

Five parts, all the person's:

1. **Change.** What shipped, in which version.
2. **Group.** The subgroup, by the person's definition and the field that records it.
3. **Record of use.** The event that counts as reached (for example enrollment completed in the Spanish flow).
4. **Denominator.** The people in that group who were eligible for the change in the period. Without it, no rate (register rule).
5. **Period.** Start and end dates, and how people who enter mid-period are counted.

Optional sixth part: an **outcome** among those reached (for example blood pressure measured at 90 days, and the share meeting the person's control definition), because reach alone is not effective engagement (PE-104).

Not evidence: a policy, a translated store listing, app availability, the release note that the change shipped (register rule; expert stop rules).

## Comparison (A2)

What the script computes, all on the person's counts:

- Reach rate = reached / eligible, per subgroup. Outcome rate = outcome met / outcome measured, among those reached.
- Wilson 95 percent interval for each rate. Computation choice of this skill, not a sourced rule; it behaves sensibly for small counts and rates near 0 or 1.
- Difference in percentage points and ratio against the reference subgroup the person names. The ratio follows PE-103's relative-risk framing; the reference is the person's choice.
- Share of eligible and share of reached per subgroup: a group whose share of the reached is lower than its share of the eligible is under-represented among those reached.
- Share of eligible with the dimension not recorded, reported, never redistributed.
- No p-values and no "significant" labels: whether a difference matters is the person's rule (B1). Overlapping intervals are not proof of no difference, and separate intervals are not a verdict.

The outcome rate is computed among people reached, so a group with low reach and a high outcome rate (as in the illustrative data, 75 and over) is still a group the change mostly did not reach. Report both.

## Small cells

- The threshold is the person's or their data provider's rule. No threshold is sourced in this skill `[GAP]`; the script refuses to run without `--min-cell`.
- Primary suppression: any count from 1 to the threshold minus 1 is hidden, and so is its complement (eligible minus reached; measured minus met), so the hidden count cannot be recovered by subtraction. Zeros are hidden only if the person's rule says so (`--suppress-zero`).
- Complementary suppression: within one dimension, if exactly one subgroup is hidden, the next smallest is hidden too, because the dimension total is shown.
- Limit: the check is per table. Several tables of the same population, or crossed dimensions, may still let a hidden count be derived; that check stays with the person.

## Area bands (SVI)

- SVI percentile ranks run 0 to 1, higher meaning more vulnerable; the 90th percentile flag (PE-122). Use the U.S. database across states, the state database within one state (PE-123). The person maps each person's area to a band before counting; the skill sees only the counts by band.
- An area band describes the area, not the person.

## Regulatory dates the review may need

- Section 1557 dates and duties: `equity-frames.md` section 1 (PE-106 to PE-117).
- DAP goals are disaggregated by age group, sex, racial and ethnic characteristics, optionally geography and socioeconomic status (PE-37); DAP status as in `equity-frames.md` section 2. Enrollment-goal attainment reported to FDA stops for the regulatory owner.
