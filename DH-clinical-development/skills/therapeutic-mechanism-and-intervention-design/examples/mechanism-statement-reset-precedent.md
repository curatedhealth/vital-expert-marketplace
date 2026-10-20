# Worked example: A1 mechanism statement on live library data

Run on 20 October 2026. Request (illustrative product, real precedent and real evidence): "We are building an app that delivers community reinforcement approach lessons plus in-app rewards for negative urine screens, for adults in outpatient stimulant use treatment. Write our mechanism and tell us what reSET's record says about how its mechanism was described." No owner named.

Calls made (all saved in `live/connector_calls_2026-10-20.json`, `live/nct01104805.json`, `live/epmc_pmid*.json`):
1. `regulatory-dh.get_authorization {reference: "DEN160018"}`: reSet, Pear Therapeutics, De Novo granted 14 September 2017, 882.5801, PWE, Class 2; no intended-use field.
2. `literature.search_literature {query: "internet-delivered community reinforcement approach contingency management substance use disorder randomized trial Therapeutic Education System", limit: 6, filters: {designs: ["rct"]}}`: 18 merged, 5 shown; kept Campbell 2014 and Levesque 2017; dropped two off-topic records.
3. `literature.find_trial {nct_id: "NCT01104805"}` (the paper alone returned no registration); registry record read directly.
4. Abstracts of PMID 24700332 and 27776269 read from Europe PMC.
5. `verify.qualify_source {doi: "10.1016/j.addbeh.2016.09.012", question}`: gold; `verify.check_claim` with the abstract passage: "partial". Passage read: it says "partial mediator", the same direction as the claim below.

---

**Answer.** Proposed chain, for you to confirm: CRA lessons and abstinence-contingent rewards are expected to lead users to complete lessons and submit negative screens, which is expected to build coping skills (psychological capability, TM44) and reinforce abstinence (reflective and automatic motivation), which is expected to raise abstinence. For whom: adults in outpatient stimulant use treatment, as you state. Not for whom: `[GAP]`; you named no group. The biggest gap: no measure is named for the coping-skills link. Who chooses the mechanism: owner not named (who decides?).

**Chain**

| Link | Stated by you | Source term | Measure named | Rows |
|---|---|---|---|---|
| Component | CRA lessons; rewards for negative screens | Intervention components | n/a | TM6 (DOI 10.1136/bmj.n2061) |
| Action | Lesson completion; screens submitted | Engagement proximal outcome | [GAP] | TM84, TM87 (DOI 10.1007/s12160-016-9830-8) |
| Change | Coping skills; reinforcement of abstinence | Mediator; COM-B | [GAP] | TM84, TM44 (DOI 10.1186/1748-5908-6-42) |
| Outcome | Abstinence | Distal outcome | [GAP] | TM83 |

**What the records state (not evidence for your product).** reSET's decision summary names the CRA, a CBT variant, with contingency management as its model (TM133), and FDA's mitigation for ineffective treatment included software V&V showing the model was correctly implemented (TM139). Its trial found no abstinence benefit in self-identified primary opioid users, which became a labeled limitation (TM138). The trial registry (NCT01104805, read 20 October 2026) lists "Coping Skills" as a secondary outcome. A secondary analysis reports coping skills as "a partial mediator" of the web-delivered CRA with contingency management (Levesque 2017, DOI 10.1016/j.addbeh.2016.09.012, abstract); the main paper says the CRA and contingency management effects were not yet differentiated (Campbell 2014, DOI 10.1176/appi.ajp.2014.13081055). Your two components therefore cannot be credited separately from these records.

**Gaps.** Not-for-whom; measures for all three links; the sources of your lesson content (DiGAV § 2 asks for them if Germany is in scope, TM149). Whether 882.5801 applies to your app is a regulatory question for `dh-regulatory-and-quality` regulatory-pathway-and-classification.

**Record.** Mechanism statement draft. AI-assisted. Each link is a hypothesis until tested (TM8). Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Word count of the answer above (without the calls list and the table source column): 323, counted by script.

## What this run shows about the connector

- `get_authorization` confirms identity and dates but carries no intended use or therapy model (P5); the mechanism facts come from the decision summary rows.
- `find_trial` did not link the main paper to its registration, and the NCT lookup omitted the two papers this answer relies on (N8).
- `check_claim` returned "partial" ("the passage does not state the figure") for the correct claim and for its opposite (N3); the passage was read by the model.
- Verify rates the FDA decision summary PDF "inadmissible" (C1), so the precedent facts are quoted from the research rows with their read date.
