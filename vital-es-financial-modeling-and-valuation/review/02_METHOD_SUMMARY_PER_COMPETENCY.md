# Method summary per competency

Written 7 November 2026 from the plugin files. One block per competency: what the skill produces, what it will not do, who decides, the sources its method rests on and how its assets are grounded.

## V1 · CF-01.02.02.1.1 · build-dcf-model

**Use when.** Use when a buyer (pharma business development or life-sciences investor) needs the UNRISKED discounted cash flow of a drug asset as a RANGE: net revenue by scenario and year taken from the signed revenue register of forecast-revenue-and-price-ranges, a cost structure, tax, capital and working-capital assumptions supplied by the deal team, a discount-rate RANGE that is labelled a human choice, and an explicit treatment of the terminal value, giving present values by scenario and rate with the share that comes from t…

**What competent output looks like (opening lines).**

- A DCF register for one asset (company mode: one per pipeline asset, then a side-by-side roll-up): net revenue by scenario and year, each with the pointer of the revenue register row it came from.
- The cost structure (cost of goods, operating expense, fixed costs, tax rate, capital expenditure, working capital) with a source or a labelled team assumption and a named owner for every line.
- The discount-rate range, labelled HUMAN CHOICE, with the method and evidence the team documents for it (VP-V-030, VP-V-031); no default rate is supplied.
- Present values by scenario and rate, unrisked, with the terminal value stated (or its absence stated) and the share of the value that comes from it. Every figure is a range or a table of a range; never a point.
- The statement that no probability of success is applied here, with the pointer to the skill that applies it.
- The adopted valuation shows HUMAN ONLY and the recommended valuation is empty. Absent evidence is a GAP with the consequence, never a number.

**Atoms called.** extract-requirements-from-source, compare-against-criteria, compose-draft.  **Tools.** scripts/dcf.py, scripts/validate_register.py.  **Requires.** forecast-revenue-and-price-ranges, assess-ip-portfolio-and-freedom-to-operate.

**Human decisions (governance gates).** the discount-rate range and the rate, if any, the team uses (decides: deal lead, with the valuation reviewer (named)); the cost structure per scenario (decides: finance lead (named) with the deal lead); the terminal assumption (decides: deal lead, with the valuation reviewer); which scenarios enter the register (decides: deal lead); the adopted valuation (decides: deal lead (BD head or investment lead)).

**Sources the method rests on.** 4 rows in references/method-standards.md; the first three: D1 WIPO, Intellectual Property Valuation in Biotechnology and Pharmaceuticals, chapter 3 (inc; D2 IVSC, International Valuation Standards effective 31 January 2025 (red-line edition; uncha; D3 Kossmeier et al.; Cha, Rifai, Sarraf (McKinsey): forecast optimism (registered by the comm.

**Grounding of the assets.** 3 rows trace to a registered passage, 32 are the authors' own rule (listed in 03), 2 are [CHECK] (untraced; never scored, never filled).

## V2 · CF-01.02.02.1.2 · calculate-risk-adjusted-npv

**Use when.** Use when a buyer (pharma business development or life-sciences investor) needs the RISK-ADJUSTED NPV of a development-stage drug asset as a RANGE, after the unrisked DCF inputs and the development risk and timeline ranges exist: development stages with costs and probabilities of success taken from the timeline register, the cumulative probability applied ONCE to the post-launch cash flows and the costs weighted by the probability of reaching each stage, discounted at a rate RANGE labelled a human choice, with the u…

**What competent output looks like (opening lines).**

- An rNPV register for one asset: development stages in order, each with years, cost range and probability range, every probability with the pointer of the timeline register row or benchmark stratum it came from.
- The cumulative probability of success by scenario and the reach probability of each stage; the probability applied exactly once (a series already risk-adjusted is refused).
- rNPV by scenario and discount rate as a range, with the unrisked NPV, the expected development cost and the launch value shown separately so a reader can see what the probability did.
- The statement that the rate is a human choice, with its documentation, and that the final probability of success is a person's to set.
- The adopted valuation shows HUMAN ONLY; no fairness or solvency view; absent inputs are GAPs with the consequence.

**Atoms called.** extract-requirements-from-source, compare-against-criteria, compose-draft.  **Tools.** scripts/rnpv.py, scripts/validate_register.py.  **Requires.** build-dcf-model, estimate-development-risk-and-timeline.

**Human decisions (governance gates).** the final probability of success (decides: clinical development reviewer (named) with the deal lead); the discount-rate range and the rate used (decides: deal lead, with the valuation reviewer); stage costs (decides: finance lead (named)); whether a series already includes risk (decides: valuation reviewer); the adopted valuation (decides: deal lead (BD head or investment lead)).

**Sources the method rests on.** 4 rows in references/method-standards.md; the first three: N1 WIPO, Intellectual Property Valuation in Biotechnology and Pharmaceuticals, chapter 3; N2 IVSC, IVS 103 and IVS 210; N3 BIO / Informa / QLS, Clinical Development Success Rates 2011-2020; Wong, Siah, Lo 2019 (re.

**Grounding of the assets.** 3 rows trace to a registered passage, 35 are the authors' own rule (listed in 03), 2 are [CHECK] (untraced; never scored, never filled).

## V3 · CF-01.02.02.1.3 · validate-valuation-assumptions

**Use when.** Use when a buyer (pharma business development or life-sciences investor) has a DCF and an rNPV and needs the ASSUMPTIONS behind them documented and checked: an assumption register in which every input has a source or a labelled team assumption with an owner, is traced to the due diligence register that holds it, and is checked against the success-rate benchmark, the analog range, the exclusivity end, the documentation duty for the discount rate and the risk-counted-twice question. Lists what traces, what is flagged…

**What competent output looks like (opening lines).**

- An assumption register: every input of the DCF and the rNPV with id, range, unit, source or labelled owner, and the pointer of the register row it came from.
- Nine checks stated as ok, flag or gap with the consequence: trace, order, upstream pointer, probability against the benchmark, peak revenue against the analog range, rate documentation, risk counted twice, explicit cash flows beyond the exclusivity end, terminal share.
- No claim that the valuation is validated: the statement says how many checks are ok, flagged or gaps and that a named reviewer decides.
- The adopted valuation shows HUMAN ONLY; no fairness or solvency view.

**Atoms called.** extract-requirements-from-source, compare-against-criteria, compose-draft.  **Tools.** scripts/assumptions.py, scripts/validate_register.py.  **Requires.** build-dcf-model, calculate-risk-adjusted-npv.

**Human decisions (governance gates).** whether a flagged assumption stands (decides: valuation reviewer (named) with the deal lead); the discount-rate documentation (decides: deal lead, with the valuation reviewer); an assumption with no source (decides: deal lead); the adopted valuation (decides: deal lead (BD head or investment lead)).

**Sources the method rests on.** 5 rows in references/method-standards.md; the first three: A1 BIO / Informa / QLS; Wong, Siah, Lo (reused by id); A2 Kossmeier et al.; McKinsey (reused by id); A3 IVSC IVS 103 and WIPO chapter 3.

**Grounding of the assets.** 4 rows trace to a registered passage, 28 are the authors' own rule (listed in 03), 2 are [CHECK] (untraced; never scored, never filled).

## V4 · CF-01.02.02.2.1 · design-valuation-scenarios

**Use when.** Use when a buyer (pharma business development or life-sciences investor) has a valuation model and needs the SCENARIOS designed before they are run: the drivers with low, mid and high ranges, each with a source or a labelled team assumption and an owner, the standard low / mid / high set built by one stated pairing rule (adverse ends in the low scenario, favorable ends in the high one), named scenarios the team defines on top, a coverage check of the required drivers and a weights check. Invents no scenario probabi…

**What competent output looks like (opening lines).**

- A scenario register: the drivers with unit, direction (higher or lower is better), low / mid / high, source or labelled owner.
- The standard three-scenario table by the stated pairing rule, every cell showing which end of the driver it took.
- Named scenarios defined by the team (settings per driver); drivers a named scenario leaves unset are listed.
- Coverage: required drivers without a range are gaps with the consequence. Weights, when the team gives them, all present and summing to 1; no probability is invented and no expected value is computed.
- The adopted valuation shows HUMAN ONLY.

**Atoms called.** extract-requirements-from-source, compare-against-criteria, compose-draft.  **Tools.** scripts/scenarios.py, scripts/validate_register.py.  **Requires.** calculate-risk-adjusted-npv.

**Human decisions (governance gates).** the scenario set and the named scenarios (decides: deal lead); the weights, if any (decides: deal lead, with the valuation reviewer); a driver that has no range (decides: deal lead); the adopted valuation (decides: deal lead (BD head or investment lead)).

**Sources the method rests on.** 3 rows in references/method-standards.md; the first three: S1 WIPO, Intellectual Property Valuation in Biotechnology and Pharmaceuticals, chapter 3; S2 WIPO chapter 4, real options; S3 A published rule for pairing drivers into scenarios, or for scenario weights.

**Grounding of the assets.** 1 rows trace to a registered passage, 28 are the authors' own rule (listed in 03), 0 are [CHECK] (untraced; never scored, never filled).

## V5 · CF-01.02.02.2.2 · analyze-valuation-sensitivity

**Use when.** Use when a buyer (pharma business development or life-sciences investor) has an rNPV model and needs to see what moves the result: one-at-a-time swings for revenue, probability of success, development cost, launch delay and discount rate, a tornado ranking by absolute swing, and switching values (the scale of revenue or of probability at which the base rNPV reaches a threshold the team names). The scales and the threshold are the team's. Describes the model, not the asset; chooses no rate, adopts no valuation, give…

**What competent output looks like (opening lines).**

- A sensitivity register: the base case (mid scenario, one rate) and, per driver, the value at the low and high end with the scales the team supplied.
- The tornado ranking by absolute swing with ranks, so the reader sees the drivers in order of effect.
- Switching values for revenue and probability: the scale at which the base rNPV equals the team's threshold, or the statement that it is not reached in the range.
- The statement that the ranking describes the model and depends on the chosen scales; the adopted valuation shows HUMAN ONLY.

**Atoms called.** extract-requirements-from-source, compare-against-criteria, rank-by-consequence, compose-draft.  **Tools.** scripts/sensitivity.py, scripts/validate_register.py.  **Requires.** calculate-risk-adjusted-npv, design-valuation-scenarios.

**Human decisions (governance gates).** the scales (decides: deal lead, with the valuation reviewer); the threshold for the switching value (decides: deal lead); the rate held for the swings (decides: deal lead); the adopted valuation (decides: deal lead (BD head or investment lead)).

**Sources the method rests on.** 2 rows in references/method-standards.md; the first three: T1 WIPO, chapter 3, scenarios; T2 Eschenbach 1992 (tornado diagrams); Saltelli et al. 2008.

**Grounding of the assets.** 1 rows trace to a registered passage, 32 are the authors' own rule (listed in 03), 0 are [CHECK] (untraced; never scored, never filled).

## V6 · CF-01.02.02.2.3 · communicate-valuation-scenarios

**Use when.** Use when a buyer (pharma business development or life-sciences investor) needs the valuation scenarios put in front of a decision owner: a summary that starts from the rNPV range with its register pointer, shows what would change the call (switching values and the top-ranked drivers copied from the sensitivity register), lists the decisions needed with the person who decides and the options, and the questions. Every line points to a register row; a line that recommends, states a fairness or solvency view, calls a p…

**What competent output looks like (opening lines).**

- A scenario communication register: the rNPV range with its pointer, then what would change the call (switching values and top drivers with pointers), then the decisions needed (item, owner, options), then the questions.
- Every added line carries a register pointer; lines that recommend, give a fairness or solvency view, or state one number as the value are refused.
- The comparables cross-check appears only as a pointer to the side-by-side, never merged. The human-only list is shown: the rate choice, the adopted valuation, the final probability, any fairness or solvency view, deal terms.
- Status UNSIGNED; adopted valuation HUMAN ONLY.

**Atoms called.** extract-requirements-from-source, compare-against-criteria, compose-draft.  **Tools.** scripts/scenario_summary.py, scripts/validate_register.py.  **Requires.** analyze-valuation-sensitivity.

**Human decisions (governance gates).** which sentences enter the summary (decides: valuation reviewer (named)); the decisions and their owners (decides: deal lead); release outside the buyer team (decides: BD head or investment lead); the adopted valuation (decides: deal lead (BD head or investment lead)).

**Sources the method rests on.** 2 rows in references/method-standards.md; the first three: C1 FINRA Rule 5150 Fairness Opinions; C2 17 CFR 229.1015 (Item 1015, Regulation M-A).

**Grounding of the assets.** 1 rows trace to a registered passage, 28 are the authors' own rule (listed in 03), 0 are [CHECK] (untraced; never scored, never filled).

## V7 · CF-01.02.02.3.1 · identify-comparable-transactions

**Use when.** Use when a buyer (pharma business development or life-sciences investor) has candidate licensing or acquisition deals that a person supplied, each with a dated source, and needs them screened against the team's own criteria: therapeutic area, stage, modality, date window, with match, mismatch or gap recorded per criterion, the excluded deals with the reason, the number included and a selection flag when only completed deals are present. The criteria are the team's; the script ships none and fetches no deal. Says no…

**What competent output looks like (opening lines).**

- A comparables register: the criteria the team stated, the candidate deals, and per deal a match / mismatch / gap on each criterion with the source reference and date.
- The deals included and the deals excluded with the reason, the count of each, and the minimum the team asked for.
- The selection flag: when every candidate is a completed deal, terminated and withdrawn deals are absent and the range can be biased (FV-06).
- The statement that comparability is the team's judgment and that nothing here says a deal is fair.
- A candidate with no dated source is refused; nothing is taken from memory.

**Atoms called.** extract-requirements-from-source, compare-against-criteria, classify-text-labels, compose-draft.  **Tools.** scripts/comparables.py, scripts/validate_register.py.  **Requires.** none.

**Human decisions (governance gates).** the criteria (decides: deal lead); each exclusion (decides: valuation reviewer (named)); the set of included deals (decides: deal lead); the adopted valuation (decides: deal lead (BD head or investment lead)).

**Sources the method rests on.** 3 rows in references/method-standards.md; the first three: M1 WIPO, Intellectual Property Valuation in Biotechnology and Pharmaceuticals, chapter 2 (mar; M2 IVS 210 Intangible Assets, market approach (2025 edition, redline copy); M3 IVS 103 Valuation Approaches, market approach (2025 edition, redline copy).

**Grounding of the assets.** 1 rows trace to a registered passage, 29 are the authors' own rule (listed in 03), 0 are [CHECK] (untraced; never scored, never filled).

## V8 · CF-01.02.02.3.2 · compare-deal-terms-to-benchmarks

**Use when.** Use when a buyer (pharma business development or life-sciences investor) has deal terms for a screened set of comparable deals and for the subject deal, and needs the arithmetic placement: a low / median / high range per term (upfront, milestones, royalty and others the team names) from the supplied deals, the range with each deal left out to show how much one deal moves it, and the subject's position as below, within or above the range, or 'no range' when fewer than the minimum have the term. States positions, not…

**What competent output looks like (opening lines).**

- A benchmark register: per term the deals that have it, n, low, median, high and the leave-one-out ranges.
- The subject's position per term as below, within or above the range of the supplied deals, or 'no range' with the consequence when n is below the minimum.
- Terms missing for a deal are null and counted, never filled.
- Every position carries the note that it is arithmetic and not a statement that the term is fair, market or standard.
- The adopted valuation and any fairness or solvency view show HUMAN ONLY.

**Atoms called.** extract-requirements-from-source, compare-against-criteria, rank-by-consequence, compose-draft.  **Tools.** scripts/benchmarks.py, scripts/validate_register.py.  **Requires.** identify-comparable-transactions.

**Human decisions (governance gates).** which terms are compared (decides: deal lead); a term with fewer deals than the minimum (decides: deal lead); release outside the buyer team (decides: BD head or investment lead); the adopted valuation (decides: deal lead (BD head or investment lead)).

**Sources the method rests on.** 4 rows in references/method-standards.md; the first three: B1 WIPO chapter 2 (market approach); B2 FINRA Rule 5150, Fairness Opinions; B3 17 CFR 229.1015(b)(6).

**Grounding of the assets.** 2 rows trace to a registered passage, 27 are the authors' own rule (listed in 03), 0 are [CHECK] (untraced; never scored, never filled).

## V9 · CF-01.02.02.3.3 · synthesize-market-standard-terms

**Use when.** Use when a buyer (pharma business development or life-sciences investor) has the benchmark ranges of compare-deal-terms-to-benchmarks and the rNPV range of calculate-risk-adjusted-npv and needs them put side by side, term by term: n, range, the dispersion of the range, a thin-data flag, the span without each deal, and the overlap between the valuation range and the benchmark range, shown but never merged, averaged or reconciled. Caveats carry the sample's limits. The adopted valuation and any fairness or solvency v…

**What competent output looks like (opening lines).**

- A market-terms register: per term n, low / median / high, dispersion (high over low), a thin-data flag and the leave-one-out span.
- A cross-check between the valuation range (with its register pointer) and a benchmark range, side by side with the overlap stated and an explicit 'merged: false'.
- Caveats on the sample: hand-picked, completed deals only, small n.
- The decisions that remain with people: whether the deals apply, which range informs the negotiation, any fairness or solvency view.
- Recommended valuation empty; adopted valuation HUMAN ONLY.

**Atoms called.** extract-requirements-from-source, compare-against-criteria, compose-draft.  **Tools.** scripts/market_standard.py, scripts/validate_register.py.  **Requires.** compare-deal-terms-to-benchmarks, calculate-risk-adjusted-npv.

**Human decisions (governance gates).** which benchmark field is cross-checked (decides: deal lead); how thin data is read (decides: valuation reviewer (named)); release outside the buyer team (decides: BD head or investment lead); the adopted valuation (decides: deal lead (BD head or investment lead)).

**Sources the method rests on.** 3 rows in references/method-standards.md; the first three: X1 WIPO chapter 2 (market approach); X2 IVS 103 Valuation Approaches (2025 edition, redline copy); X3 FINRA Rule 5150; 17 CFR 229.1015(b)(5) and (b)(6).

**Grounding of the assets.** 2 rows trace to a registered passage, 27 are the authors' own rule (listed in 03), 0 are [CHECK] (untraced; never scored, never filled).
