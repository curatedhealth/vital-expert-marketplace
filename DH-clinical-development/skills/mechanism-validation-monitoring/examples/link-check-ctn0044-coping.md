# Worked example: A2 link-by-link check and B1 miss review on live library and registry data

Run on 20 October 2026. Request (illustrative requester, real records): "Our app uses the same community reinforcement approach plus contingency management as reSET. Before we lean on the CTN-0044 trial, check its mechanism link by link. Our rule: a link counts as met if the trial registered a measure for it before results and a published passage reports a statistically significant effect in the predicted direction. Our chain: TES delivered as built, lessons completed, coping skills improve, abstinence rises." No owner named.

Calls made (saved in `live/connector_calls_2026-10-20.json`, `live/nct01104805.json`, `live/epmc_pmid*.json`):
1. `literature.search_literature {query: "internet-delivered community reinforcement approach contingency management substance use disorder randomized trial Therapeutic Education System", limit: 6, filters: {designs: ["rct"]}}`: kept Campbell 2014 and Levesque 2017.
2. `literature.find_trial {record: Campbell 2014}`: "no linked registration found"; `literature.find_trial {nct_id: "NCT01104805"}`: CTN-0044, five papers, not including the two kept (N8).
3. ClinicalTrials.gov API read for NCT01104805 (registered outcomes, first submitted 14 April 2010).
4. Europe PMC abstracts of PMID 24700332 and 27776269.
5. `verify.qualify_source {doi: "10.1016/j.addbeh.2016.09.012"}`: gold; `verify.check_claim` with the mediation passage: "partial" for the claim and also for its opposite (N3); passage read by the model.
6. `regulatory-dh.get_authorization {reference: "DEN160018"}` and `regulatory-dh.search_safety_events {product_code: "PWE"}` for the device built on this trial.

---

**Answer.** CTN-0044 (NCT01104805, 507 enrolled, unmasked, read 20 October 2026): 2 of 2 measurable links met by your rule; two links not measurable from the records read; one population signal reported as context. Not a quality score, and a met link here is not evidence for your app.

| Link | Registered before results? | Passage | Result | Source |
|---|---|---|---|---|
| Delivered as built | No fidelity measure registered | none read | not scored [GAP] | registry |
| Lessons completed | No | engagement paper (DOI 10.1016/j.jsat.2021.108585) listed by the library, not read | not scored [GAP] | find_trial |
| Coping skills improve | Yes, "Coping Skills" secondary | "TES intervention was significantly associated with higher coping strategies scores when accounting for baseline scores (F1,1342=8.3, p=0.004)" | met | Levesque 2017, DOI 10.1016/j.addbeh.2016.09.012, abstract |
| Abstinence rises | Yes, primary "Reduced Substance Use and Improved Treatment Retention" | "greater abstinence rate (odds ratio=1.62, 95% CI=1.12, 2.35)" | met | Campbell 2014, DOI 10.1176/appi.ajp.2014.13081055, abstract |

Reading note: the delivery and use links are unread, so these results cannot separate the mechanism from delivery (CS32, DOI 10.1007/s10488-010-0319-7). The same abstract reports coping as "a partial mediator"; whether it mediates is a question for whoever you name for the analysis (owner not named). The main paper says the CRA and contingency management effects were not differentiated, so neither component can be credited alone.

**Population (context, not scored: no subgroup was registered).** reSET's decision summary reports no abstinence benefit in self-identified primary opioid users (5.7 percent vs 15.9 percent), which became a labeled limitation (TM138). Its odds ratios (2.22, 3.17, TM137) come from a different analysis than the paper's 1.62; both are quoted as stated.

**Recall records on product code PWE (reSET, reSET-O).** Two Class II recalls of 7 June 2021 state that rewards were granted "regardless of the UDS results". Quoted as the records state; no judgment on your app.

**For B1 (your decisions).** If your population includes primary opioid use, decide whether to measure that subgroup or narrow your claim, and who owns it (owner not named). Claim wording stops for `dh-regulatory-and-quality` regulatory-submission-and-dossier.

**Record.** Link check draft. AI-assisted. One cohort, one version; a met link is not proof the product works. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Word count of the answer above (without the calls list and the table source column): 342, counted by script. The F statistic's subscript (F1,1342) is flattened from the abstract's markup.

## What this run shows about the connector

- The library linked neither the main results paper nor the mediation paper to NCT01104805, and its NCT lookup listed five other papers (N8). The registry had to be read directly to see that "Coping Skills" was registered.
- `classify_study` called the mediation paper `rct` 0.95 and `grade_evidence` gave it CEBM level 2, from the publication type alone (N8).
- `check_claim` returned "partial", "the passage does not state the figure", for the correct mediation claim and for its opposite (N3).
- Verify rates the FDA decision summary "inadmissible" (C1); TM rows carry the read date instead.
