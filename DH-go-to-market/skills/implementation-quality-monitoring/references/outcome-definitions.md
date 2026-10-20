# Implementation outcome definitions

Interpretive reference for task A2. Rows: `CS` in `customer-success-research.md`. Proctor et al. 2011 [PAPER], DOI 10.1007/s10488-010-0319-7; RE-AIM definitions from re-aim.org; NICE ESF ECD7. These sources define outcomes; none sets a threshold, a target or a good-or-bad level. Every target is the person's.

## Why these come first

Implementation outcomes are preconditions for clinical or service outcomes (CS32). A site where few eligible patients use the product tells you about the deployment, not about whether the product works. Usage, logins and activation are not clinical evidence (worker stop rule, `examples/live/agent_pack.json`).

## Definitions and formulas computed by `scripts/implementation_outcomes.py`

| Outcome | Formula used | Denominator rule | Row |
|---|---|---|---|
| Adoption, setting level | Sites that agreed, are live or paused / sites approached | Settings approached (valid denominator) | CS28 (RE-AIM); Proctor's adoption is the intention, decision or action to try (CS34) |
| Penetration, patients | Eligible people who used the service / all eligible people | Eligible population, not volunteers who showed interest | CS39 (first formula), CS27 |
| Penetration, providers | Providers delivering / providers trained in or expected to deliver | Providers trained or expected | CS39 (second formula) |
| Usage against the agreed profile | Observed usage / expected usage, in the unit agreed at commissioning | The profile agreed at commissioning | CS61 (NICE ESF standard 16) |
| Fidelity to plan | Milestones done on or before their baseline due date / milestones whose baseline date has passed | Baseline dates the site agreed | CS9 (fidelity to planned courses of action, timeliness), CS37 |
| Core fidelity | The same, core milestones only | Core components named in the plan | CS4, CS48 |
| Slippage | Days between baseline due and done, or the as-of date for an open item | Baseline, never the re-baselined date | Register rule of the old Site score task: note items that slipped past the agreed go-live date |
| Re-baselined count | Milestones whose current due date differs from the baseline | Shown beside slippage | Register rule: do not rescore the bar after the site is live to make it pass |

## Definitions the script does not compute (ask for the data)

| Outcome | Definition | Row |
|---|---|---|
| Reach | Number, proportion and representativeness of eligible people who take part | CS22, CS27 |
| Adoption, staff level | Percent of staff invited who take part | CS28 |
| Implementation (RE-AIM) | Staff fidelity, consistency, time and cost at setting level; patients' use at individual level; percent of "perfect" delivery, adaptations, cost | CS25, CS29 |
| Acceptability, appropriateness, feasibility | Perceptions of stakeholders; usually surveys or interviews | CS33, CS35, CS36 |
| Implementation cost | Cost impact of the effort | CS38 |
| Sustainability or maintenance | Kept in routine operations; RE-AIM setting-level check: still running 6 or more months after support ends | CS40, CS26, CS30 |
| Effectiveness | Impact on outcomes including negative effects, quality of life and economic outcomes | CS23 (not an implementation outcome; clinical or service evidence) |

## Choices to state in the output

- Terms overlap (research file, "Changes and conflicts"): penetration is similar to reach; sustainability maps to maintenance; adoption has two definitions. Name the one used.
- Pooled figures are shown beside per-site figures, never instead of them. Do not average sites into one score.
- Maintenance: the script reports months since go-live. Whether a site is "maintained" needs the person's definition; RE-AIM's 6-month check runs from the end of support, not from go-live (CS30).
- Patient-reported scores agreed as outcomes (for example PHQ-9 or GAD-7) belong to Customer Health & Value Realization (DH-02.02.3.x); where payment depends on them, Market Access outcomes-contract-monitoring.
