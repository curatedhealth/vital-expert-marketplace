# A2 Price corridor evidence

Framework task: DH-02.01.3.1, Part A, task A2. Replaces the old "Price corridor" and "Read the pricing corridor" sections. Catalogue jobs on the library: `health-system-value-brief` for a health-system sale, otherwise `pricing-corridor` (see the formula table).

## What this task delivers

The evidence behind each end of a price corridor the person will set: the product's own registered price where one exists, registered comparator prices in the same indication and scheme, the payer rules that cap or shape a price in each market, and value-based or budget arithmetic on the person's own numbers. Every number carries its kind (rule, registered price, hypothesis), its source and its date. The corridor itself stays the person's.

Why it matters: a corridor with no stated reason for each end gets argued from scratch in every deal. A corridor that mixes a comparator's registered price with a model output, or quotes an unrelated product's price, collapses at the first payer question.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-02.01.3.1 Part A, Price corridor evidence |
| Workflow | The steps below |
| Knowledge | `references/price-evidence.md`; `references/payer-price-facts.md`; `references/money-flow-and-value-unit.md` (unit) |
| Tools | `commercial-dh.list_commercial_dh_sources` (free); `commercial-dh.get_pricing_corridor`; `market-access-dh.find_scheme_precedents`; `analytics.vba-price-anchor`; `analytics.budget-impact-model`; `verify.build_record`; `scripts/comparator_prices.py` (optional) |
| Prompt | This guide |
| Template | `assets/price-corridor-output.md` |
| Input | The request and its context; the A1 unit if it exists; the person's unit cost, comparator cost, QALY estimate, threshold, eligible population and uptake if they want models run |
| Governance | `references/governance.md`; the corridor and price are the person's |
| Catalogue job | `health-system-value-brief` when the corridor is for a health-system sale (corridor, literature, budget impact, price anchor on the person's numbers); otherwise `pricing-corridor`, `scheme-precedents`, `budget-impact`, `price-anchor` one call each. Live run and pitfalls: `examples/live/job_health_system_value_brief_somnio.json`, `references/tools.md` |

## Read the request

- **Product, market, indication.** The indication decides the comparators. For DE_DIGA use the ICD-10-GM code or German term.
- **Which ends?** "How high can we go" is the ceiling; "what is the floor" is the floor; "corridor" is both.
- **Models wanted?** Run `vba-price-anchor` or budget arithmetic only on numbers the person gives. Never supply a threshold, a QALY gain, a cost or an uptake share.
- **Health-system sale?** If the corridor is for a conversation with a health system, the catalogue job `health-system-value-brief` is the one-call option for steps 2 and 5 (see Step 5).
- **Unit known?** If A1 has not fixed a unit, say each comparator's unit is not stated in the record and ask which unit the corridor uses.
- **Short or full?** Direct question: short. Pricing paper or board: full.

## Workflow

### Step 1. Know what the library holds

Call `commercial-dh.list_commercial_dh_sources` (free). Keep `listing_count`, `last_load` and `posture` for each scheme in the person's markets. A missing comparator in a scheme with no listings means something different from a missing comparator in DE_DIGA with 82.

### Step 2. The product's own registered price

If the product is listed, call `commercial-dh.get_pricing_corridor` with `reference`. Keep only the price row whose `source_url` is the product's own record, with its retrieval date. Discard the other rows: they are recent listings in any indication, without names (register N4). With code execution, `scripts/comparator_prices.py corridor` separates them and says how many rows were set aside. If the product is not listed, skip this call and say so.

### Step 3. Comparator prices in the same indication

Call `market-access-dh.find_scheme_precedents` with `scheme` and `indication` (code or source-language term), `limit` up to 25. Report each comparator: product, manufacturer, status, listed on, price and currency as stored, source URL, retrieved on. For DE_DIGA add that the stored price carries no unit, no prescription period and no flag for manufacturer versus negotiated amount (`[GAP]`, DE20 names where the directory publishes them). Give the low, the high and the count; never an average presented as a target. With code execution, `scripts/comparator_prices.py precedents` builds the table.

### Step 4. Payer rules that cap or shape the price

From `references/payer-price-facts.md`, state only the rules that bind the person's market and route: for a DiGA, the year-one manufacturer price (DE7, DE9), the threshold and group maximums with their validity window and which groups exist (DE14, DE15), and the price criteria (DE12); for US codes, the payment formula (US8) or contractor pricing (US19); for France, price versus tariff (FR5); for England, the MedTech Funding Mandate test [WF] (EN1). National figures such as DE-9 are context, never targets. For anything a payer sets or negotiates, point to dh-market-access.

### Step 5. Models on the person's numbers

- Value-based ceiling: call `analytics.vba-price-anchor` with the person's `comparator_cost_per_patient`, `incremental_qalys` and `wtp_thresholds` as a plain list of numbers. Report each ceiling with its threshold and the defaults the tool applied (`non_drug_cost_offset_per_patient` 0, `units_per_patient` 1). Label it a hypothesis on the person's assumptions.
- Budget impact: try `analytics.budget-impact-model` once with the person's inputs. If it returns HTTP 422, run the arithmetic in the conversation (`references/price-evidence.md`), show every line, label it a hypothesis.
- Health-system value brief (catalogue job `health-system-value-brief`, or the same calls directly): corridor first, `literature.search_literature` only if the person asks for a published cost or outcome, then the two calculators. A corridor price or a study figure goes into a calculator only if the person adopts it, and it keeps its tool and source URL. The job also names `analytics.scenario-modeler` and `analytics.risk-tornado`; the connector does not expose them, so write "[GAP] scenario and sensitivity: tool not exposed" and never build a scenario or tornado from your own formula. In the live run (`examples/live/job_health_system_value_brief_somnio.json`) the budget impact call returned HTTP 422 again and the price anchor answered.

### Step 6. Reasons per end, for the person to choose

For each end, list the evidence that could support it (comparator low or high, unit cost, payer cap, anchor) with its kind and source. Where the person has not set an end, write the reasons and mark the end `[GAP]`; if asked for a number, give it labeled "proposed" with the evidence behind it, and say the price position stops for the owner. Where the evidence for an end is a model output only, say so.

## Build the output

Follow `assets/price-corridor-output.md`. Short mode: the answer, the comparator table, the binding payer rule, the model result if run, the gaps, the record line.

## Before you hand it over

- No number for the person's product unless the person gave it; any proposal labeled "proposed".
- Every comparator has source URL and retrieval date; no row from the unfiltered corridor list appears.
- Rules carry row ids and validity windows; model outputs carry "hypothesis" and their inputs.
- Count the words in short mode.
- Price positions stop for the person's pricing owner; if the output leaves the conversation, call `verify.build_record` with the named clearer, or label it an uncleared draft.

## Boundaries

- Never present a registered price as current or negotiated; it is the stored figure on its retrieval date.
- Never present a comparator's price, an average or an anchor as the person's price.
- Payer prices, codes and negotiation strategy belong to dh-market-access.
- Drugs, biologics and wellness apps are out of scope.
