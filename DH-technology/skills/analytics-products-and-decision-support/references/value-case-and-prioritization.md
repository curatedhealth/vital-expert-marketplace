# Decision frame, value case and prioritization

Interpretive reference for task A1. Each sourced rule carries its row; the research files in this folder hold the URL, verbatim quote and read date. Where this file states a method step from the old framework tasks (DH-05.01.3, DH-05.02.3.1, DH-05.03.1.1, DH-05.03.1.2), it says so: those steps are the framework's own method, not an external source.

## 1. The decision frame comes before the data

Old task method (DH-05.01.3.1.1 to .3, "Do not start with a dataset"):

1. Name the decision maker and the choice they have.
2. Name what they will do differently if the analysis says yes or no.
3. Name the analysis that will not be done because it does not change the choice.
4. Write the few questions whose answers change the action; for each, the data that can answer it or `[GAP]`; order them so a gap early stops later work.
5. Confirm the frame with the decision maker: show the choice and the two actions, record what they changed, and stop if they cannot name an action.

Sourced support for writing the frame down:

| Rule | Source and rows |
|---|---|
| Document intended purposes, beneficial uses, context-specific laws and norms, and deployment settings | NIST AI RMF 1.0, January 2023, MAP 1.1 (DA-10); the framework is voluntary (DA-02) |
| Document the system's knowledge limits and how output may be used and overseen by humans | NIST AI RMF 1.0, MAP 2.2 (DA-11) |
| Weigh resources to manage risk alongside viable non-AI alternatives | NIST AI RMF 1.0, MANAGE 2.1 (DA-15) |
| Document the risks that will not or cannot be measured | NIST AI RMF 1.0, MEASURE 1.1 (DA-12) |

NIST AI RMF applies only where the analytic uses AI; for a plain report or dashboard, use the frame steps alone. The non-AI alternative (DA-15) is a line in every frame for an AI use case: "Non-AI alternative considered: [the person's words, or not given]".

## 2. Solution shape and method

Old task method (DH-05.01.3.2.1 to .3, "Do not default to a model"): name the shape the decision maker will use (table, model, dashboard, one number), its grain and refresh, and the shape considered and rejected; match a method and a source to each question and flag a question whose source is `[GAP]`; name the first output the decision maker will see; write what the solution will not decide, which outputs are descriptive rather than a recommendation, and the owner of the solution.

The method itself (regression, causal inference, forecasting, machine learning) is `data-preparation-and-analytics-methods` (this pack). This skill names the shape and routes the method.

## 3. Decision product discovery and the bet

Old task method (DH-05.02.3.1.1 to .3): name the role and the moment they decide, the tool they decide in today, and the decision kept out of the product; write the bet (what the user will do in the product that they cannot do in the current tool, the metric that will show they did it, the smallest version); record the evidence (users spoken to, the moment watched, the step they cannot do today, quoted). "Stop the bet if you did not see that step." A stakeholder interview does not replace watching the moment.

The bet metric becomes the outcome that `analytics-adoption-and-impact-monitoring` (this pack) measures later, so write it with its comparison and window now. Page views are never the bet metric (old DH-05.02.3.3.1).

## 4. The value case

Old task method (DH-05.03.1.2.1): name the decision and the user; name the cost of the current way (time, errors or money) with a source; name the change expected as a range or as `[GAP]`. "Do not write a value case with no source for the current cost."

Cost elements to ask for (each "not given" until the person supplies it with a source):

| Element | Source and rows |
|---|---|
| Implementation cost is a separate outcome from the product's effect; it varies with product complexity, strategy complexity and setting | Proctor 2011 (CS38), DOI 10.1007/s10488-010-0319-7 |
| For a technology deployed in the NHS, budget impact includes purchase, updating, maintenance, staffing and training and supporting IT infrastructure | NICE Evidence Standards Framework, last updated 9 August 2022, standard 17 (CS63) (an NHS evidence standard; context for other markets) |
| Cost (investment, supply, opportunity) and relative advantage are innovation constructs a fit check can name | CFIR 2022 (CS13), DOI 10.1186/s13012-022-01245-0 |

Rules:
- The current cost and the expected change are the person's figures with the person's sources. The model supplies no benchmark, no typical saving and no return on investment. No source in this skill gives one `[GAP]`.
- Arithmetic on the person's inputs may run through `analytics.scenario-modeler` (named `parameters`, `formula` with `**` for powers, `periods`, `aggregate`); every output is "arithmetic on your inputs, not a forecast".
- A value case that needs a health economic model (QALYs, cost-effectiveness for a payer) routes to `dh-access-and-value` economic-model-development.

## 5. The analytics portfolio and roadmap

Old task method (DH-05.03.1.1.1 to .3): list each product with the decision it serves and its owner, for a named period; name a proposal left off and why ("Do not list a product with no decision"). Mark now, next and later; name the dependency that holds a later item and the people the now items need ("Do not mark every item as now"). Record each change: the item added or removed, who decided, and which now item was delayed to make room. Adding an item without delaying or dropping another while capacity is unchanged is flagged as a fact.

"Portfolio" here means the analytics portfolio (analytics products and use cases). The company's own medical products and programs are `dh-strategy-and-portfolio` product-portfolio-prioritization.

## 6. Ranking use cases on the person's rule

Old task method (DH-05.03.1.2.2 and .3): state the rule (value, risk, dependency) before ranking; rank with that rule; show a use case the rule placed last; never change the rule after seeing the rank. Record what was funded and what was not, who decided, and the value case for each one taken ("Do not fund a use case with no value case").

Rules for the calculators:
- `analytics.rice` and `analytics.mcda` run only on the person's own scores. Proposed scores are never ranked.
- RICE is a calculator the person chooses, citing a vendor article (Intercom 2016), not a sourced rule. Confidence is a whole percent (80, not 0.8): saved output `rice_percent_confidence.json` (19 October 2026).
- `analytics.mcda` is a weighted sum on 0 to 4 (EVIDEM), reads every criterion as higher-is-better (register C17) and returns no robustness view. `scripts/metric_check.py rank` reproduces both and prints, for each adjacent pair, the score at which the lower option ties.
- The rule is written down with its date before the rank is shown. If the person changes the rule after the rank, both ranks and both dates go in the record.
- The rank is "arithmetic on your scores, not a decision". Funding is the person's.

## 7. What is not sourced

- Value benchmarks, typical savings or returns for analytics or decision support products: none `[GAP]`.
- Official guidance on analytics product governance outside quality measures (dashboard or KPI governance): none found (`data-and-ai-research.md`, "Not sourced").
- A sourced prioritization method for analytics use cases: none; the person's rule decides.
