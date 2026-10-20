# Personalization engine rules

What the sourced rows say about specifying an adaptive intervention or personalization engine in a digital therapeutic or digital health product, and testing its tailoring rules. Rows are in `THERAPEUTIC_MECHANISM_AND_TRANSLATION.md` (TM), `DATA_AND_AI.md` (DA) and `AI_ML_REGULATION.md` (US, EU). Every [PAPER] row carries its DOI. No source here sets an engagement target, a dose or a safety bound for a tailoring rule: those are the person's.

Scope: this file covers the engine (decision points, options, tailoring variables, rules, missing-data behavior, how a rule is tested). The therapeutic mechanism, engagement mechanics and safety by design of the intervention itself are `dh-clinical-development` therapeutic-mechanism-and-intervention-design; evidence-to-feature rules are `dh-clinical-development` evidence-to-intervention-translation.

## 1. The four components (Nahum-Shani et al. 2018, DOI 10.1007/s12160-016-9830-8)

| Component | Definition | Row |
|---|---|---|
| Decision point | A time at which an intervention decision is made | TM78 |
| Intervention options | The possible treatments or actions at a decision point: types, sources, amounts and media of support | TM79 |
| Tailoring variable | Information about the individual used to decide when and which intervention to provide; from active (self-report) or passive (sensor) assessment | TM80, TM81 |
| Decision rule | Which option to offer, for whom and when; one rule per decision point; the specification a software rule engine implements | TM82 |

Proximal and distal outcomes guide the design (TM77): the distal outcome is the ultimate goal, usually a primary clinical outcome (TM83); proximal outcomes are the short-term goals of each option, often mediators (TM84). Adaptation is the use of ongoing information about the person to change type, amount and timing of support (TM85). Receptivity is the person's transient ability or willingness to receive and use support (TM86).

## 2. What a specification must hold (each from the rows)

| Element | Rule | Row |
|---|---|---|
| Allowed options per decision point | The array of possible options; anything the rule can deliver outside it is a specification gap | TM79 |
| Behavior when tailoring data are missing | Plan in advance how each rule behaves when tailoring measurements are missing | TM89 |
| Measurement validity of each tailoring variable | Unreliable tailoring variables make a rule little better than random; invalid ones may recommend counterproductive options | TM88 |
| Proximal outcome per option | Short-term goal measured shortly after the option is delivered | TM84 |
| Engagement and fatigue outcomes | Include proximal outcomes for engagement and intervention fatigue to prevent abandonment | TM87 |
| Planned tailoring described | TIDieR item 9: "If the intervention was planned to be personalised, titrated or adapted, then describe what, why, when, and how." (EQUATOR checklist, verbatim) | TM30 |
| Planned versus unplanned variation | TIDieR-PHP splits planned variation from unplanned variation after start (Campbell et al. 2018, DOI 10.1136/bmj.k1079) | TM38 |

`scripts/model_check.py rules` checks a rule table against these elements and prints flags R0 to R7. A flag is a gap in the specification, never a safety verdict.

## 3. Testing a rule

- The micro-randomized trial randomizes options at many decision points to estimate causal effects on proximal outcomes (Nahum-Shani et al. 2018, DOI 10.1007/s12160-016-9830-8, TM90). Comparisons from a log where the rule chose the option are descriptive, not causal.
- MOST (Collins, Kugler and Gwadz 2016, DOI 10.1007/s10461-015-1145-4): preparation, optimization and evaluation phases (TM66); the optimization phase uses efficient randomized experiments to measure each component's effect and interactions (TM67, TM71, TM72); the optimization criterion is set in preparation (TM69); an optimization trial tests which components work, not the package's effectiveness (TM76); the optimized package goes to an RCT when an effect estimate is needed (TM73).
- Later MOST papers call the criterion the "optimization objective" and define EASE: effectiveness balanced against affordability, scalability and efficiency (Guastaferro and Collins 2021, DOI 10.1177/26334895211054363, TM74, TM75). Same concept (TM conflicts 2). The objective is the person's.

## 4. Safety boundaries for a model that keeps learning

- EU AI Act Article 15(4): high-risk systems that continue to learn after release shall be developed to eliminate or reduce as far as possible biased outputs influencing future inputs (feedback loops) (DA-63). Article 10(2)(f): examine possible biases, especially where data outputs influence inputs for future operations (DA-48). Law; applies from 2 August 2028 for Annex I devices (DA-67).
- Changes pre-determined at the initial conformity assessment are not a substantial modification (Article 43(4), EU-05); the FDA counterpart is a PCCP (US-03 to US-13). Whether an adaptive change fits either is `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- PCCP guiding principle 1 (focused and bounded) includes mechanisms to detect and revert a failing change (US-31).
- A record example, described only as its record states: EndeavorRx (DEN200026, granted 15 June 2020) uses adaptive closed-loop algorithms that adjust difficulty per patient; its digital control matched reward and engagement but lacked the adaptive algorithms (FDA De Novo decision summary, TM141 to TM143).

## 5. Not sourced

- Bounds for dose, frequency or intensity of a digital intervention; acceptable shares of decisions with missing tailoring data; engagement or retention targets. Those are the person's `[GAP]`.
- Reinforcement learning or bandit policy design methods: no row in this skill's research.
