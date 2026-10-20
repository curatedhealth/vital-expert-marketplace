# B1 Scenarios, implications and the person's choice

Framework task: Part B, task B1. Replaces the old tasks DH-01.05.3.1.2 Scenario Construction, DH-01.05.3.1.3 Strategic Implication Assessment and DH-01.08.4.1.3 Disruption Assessment.

## What this task delivers

Scenarios built on the person's drivers, each assumption tied to an A1 signal id or marked as the person's; for each scenario, what would be observed if it were unfolding (the watch items); the implications for the person's current play as they state it; which signals would change that play by the person's own test of "disruptive"; and, if the person scored options (adopt, pilot, partner, license, build, watch, stop) or technologies, their scores ranked with `analytics.mcda` or `analytics.rice`, with the weights at which the order would swap, plus sensitivity runs on their numbers. Decisions are listed as the person's. It answers "if these futures unfold, what happens to our plan, and how solid is the order of our options by our own scores?"

Why it matters: scenarios that carry the model's probabilities, or a ranking that hides who scored, turn a planning aid into an unowned forecast. Tying every assumption to a record and every rank to the person's scores keeps the choice theirs and auditable.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Compliance Officer (`chief-compliance-officer-digital-health`), as bound to DH-01.05.3.1 in the old skill; Disruption Assessment came from DH-01.08.4.1 (`chief-digital-health-officer`). Better-fitting experts are proposed in the build notes, not bound |
| Skill | DH-01.05.3.1 and DH-01.08.4.1 Part B, Scenarios, implications and choice |
| Workflow | The steps below |
| Knowledge | `references/scenario-and-decision-rules.md` (SP-074 to SP-097, SP-130 to SP-147, SP-170 to SP-176; DL-099, DL-101 (inference), DL-106); A1 and A2 outputs; `references/governance.md` |
| Tools | `analytics.mcda` or `analytics.rice` (only on the person's scores); `analytics.scenario-modeler` and `analytics.risk-tornado` (only on the person's parameters and ranges); `scripts/horizon_helpers.py swap`, `rice-check`, `tornado-check` |
| Prompt | This guide |
| Template | `assets/scenarios-and-implications-output.md` |
| Input | The request and its context: drivers and their states, the current play, the options or technologies, criteria, weights, 0 to 4 scores, any parameters and ranges, owners and dates the person names, A1 signal log and A2 fact sheets |
| Governance | `references/governance.md`; people decide; benchmarks are context |
| Catalogue job | none (`partner-prioritization` runs the same calculators but is scoped to partners and indications; call them directly; `examples/live/list_jobs_2026-10-19.json`) |

## The rule that shapes this task: people decide

The person names the drivers, the current play, what counts as disruptive, the options, the criteria, weights and scores, and the choice. The model ties assumptions to records, computes on the person's numbers, and labels anything it proposes "proposed". It never picks the winner, never gives a probability or a date of arrival, never supplies a market size, and never presents a benchmark as the person's number.

## Workflow

### Step 1. Confirm the inputs

Write back, numbered and verbatim: the drivers and their states, the current play, the person's test of "disruptive", the options, criteria, weights and scores. Missing items: drivers (propose up to four from A1 signals, labeled "proposed driver" with the signal id); current play ("not given `[GAP]`", no implications written); scores (no ranking).

### Step 2. Build the scenarios

One scenario per combination of driver states the person picks (propose two to four combinations if asked, labeled). For each assumption, cite the A1 signal id (for example "AI Act Annex I obligations from 2 August 2028, EU-19") or write "your assumption". Remove any assumption with neither. For each scenario, list what would be observed if it were unfolding, as record types (a clearance under a product code, an Official Journal act, a trial registration), which become watch items for `foresight-signal-monitoring` (this pack). No likelihoods unless the person gives them.

### Step 3. Implications for the current play

For each scenario, which parts of the play it would touch (evidence plan, pathway, data access, partner, timing), with the signal ids. Use "would touch", never "will". Where an implication rests on a rule, state the rule and its status as read (draft, final, pilot), and route the regulatory reading to `dh-regulatory-and-quality` regulatory-pathway-and-classification.

### Step 4. Disruption read

List the signals or leads that, if confirmed, would change the play by the person's test. No disruption score. A lead stays a lead until its record is read (A1 Step 5).

### Step 5. Rank only what the person scored

Before ranking, ask whether the criteria capture every factor relevant to the decision (SP-076, [PAPER] Marsh 2016, DOI 10.1016/j.jval.2015.12.016, [WF]: read through a summarizer). Where an option is a license from a competitor, name dependency on the licensor as a factor the person may want to score, labeled "proposed".

With scores on 0 to 4 and weights, call `analytics.mcda {alternatives: [{id, scores}], criteria_weights}`. Save the output and run `python3 scripts/horizon_helpers.py swap FILE`: it recomputes each value (weighted sum times 25), checks the tool, and lists the weight at which adjacent options swap (register C17: the tool gives no robustness view). Every criterion is read as higher-is-better: a "risk" or "cost" criterion must be scored so that higher is better, by the person. With RICE inputs, call `analytics.rice` with confidence as a whole percent and run `rice-check`. Present "your scores, ranked", with the swap points. Every statement of what would change the order is computed, never estimated: quote the swap weights `swap` prints, or show the arithmetic on the person's scores ("License 0.4x2 + 0.25x3 + 0.2x3 + 0.15x3 = 2.60, x 25 = 65"). If weights do not sum to 1, ask; never normalize silently. Apply the MCDA rules as questions: criteria overlap (SP-077), consistency check by re-eliciting (SP-081), decision support not decision (SP-080), citing [PAPER] Marsh 2016, DOI 10.1016/j.jval.2015.12.016 [WF].

### Step 6. Sensitivity on the person's numbers (only if asked)

With the person's formula, parameters and ranges, call `analytics.scenario-modeler` per scenario and `analytics.risk-tornado` with `parameter_ranges` for every parameter. Run `tornado-check` on the output: flag default ranges, skipped list parameters and ratio formulas. Label every number "computed on your inputs". If the person applies UK optimism bias, quote the guidance values with their date and limits (`scenario-and-decision-rules.md` section 5: Green Book 2026, SP-171; HM Treasury optimism bias guidance, 2003 document on 2002 data, SP-170, SP-172 to SP-176) as UK public-sector guidance, and compute only with the uplift and mitigation the person chooses, showing the arithmetic.

If the person asks to plug in a benchmark ("use the industry success rate"), quote what SP-082 to SP-087 measured, with method and DOI, say there is no digital health success rate in the sources, and run the model only with a probability the person states as theirs.

### Step 7. Options that involve a partner, a license or a company

Flag the facts in `scenario-and-decision-rules.md` section 7 (TTBER 2026/877 dates and thresholds, the transition to 30 April 2027, DOJ and FTC 2017 guidelines, material contract filing) for the owner the person names for legal matters, or owner not named. Put each threshold beside the person's own figure without leaning ("TTBER 2026 threshold for competitors: combined share up to 20% on any relevant market, Regulation (EU) 2026/877 (SP-136). Your figure: not given. For your legal owner."); never compute their share or say which side of the line they are on. Include every flag the rows support: data in the license (SP-142), health data used for training or validation (GDPR Articles 4(15), 9(1) and 35(3)(b): DL-099, DL-101 (inference), DL-106), a material contract filing (SP-130 to SP-133). Never "exempt", "safe" or "inside the safety zone". Partnership design routes to `dh-go-to-market` channel-and-partner-design; investing in or acquiring a company routes to `company-and-evidence-assessment` or `investment-memo-and-decision-record` (this pack). Product portfolio questions (the company's own products and programs) route to `product-portfolio-prioritization` (this pack); never call them "portfolio" without saying which.

### Step 8. What the person decides

List each decision the work surfaces (which scenario to plan against, which option, what to watch, who owns each watch item and when it is reread), with the facts behind it. Owners as named, or "owner not named"; dates as set, or "not given".

## Build the output

Follow `assets/scenarios-and-implications-output.md`. Answer first: the scenarios in one line each, the implication that bears most on the play, the order of the person's scored options with the nearest swap point, and the decisions that are theirs. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/horizon_helpers.py words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows and Retrieved columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every assumption has a signal id or is marked as the person's; no probability, date of arrival or market size from the model.
- Rankings are the person's scores, computed, with swap points; no winner picked.
- Benchmarks appear only as context with method and DOI; never as the person's number.
- Licensing facts flagged for the legal owner, never concluded.
- Proposals labeled "proposed"; owners as named.
- Swap points and sensitivity statements are computed (script output or arithmetic shown), never estimated.
- Every fact names its source in plain words with its date, then the row id ("Regulation (EU) 2026/1744, Official Journal, in force 27 July 2026 (EU-17)"); never a row id alone.
- The record line is the very last line of the answer: the calls list and the one-line offer of the full version come before the record block. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Strategic vision and option tests through prototypes and experiments: `strategic-vision-and-options` (this pack).
- Whether scenarios and calls held up later: `foresight-signal-monitoring` (this pack).
- Ranking the company's own products and programs: `product-portfolio-prioritization` (this pack).
- Investment decisions on companies: `investment-memo-and-decision-record` (this pack); never advice.
