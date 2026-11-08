---
command: /val-comparables-check
args: [asset or company, buyer_mode (bd|investor), unit (asset|company), currency, valuation_date]
---
Run intake and then the skills of one mission in order: identify-comparable-transactions, then compare-deal-terms-to-benchmarks, then synthesize-market-standard-terms (mission 3). See skills/financial-modeling-and-valuation-capability-map/SKILL.md.

Inputs needed before any step: Candidate deals each with a dated source supplied by a person; the criteria; the subject's terms; the rNPV range pointer. Ask for every missing argument in one message and do not start on an assumption. A missing upstream register is a [GAP]: name its consequence and the skill to run, and do not fill it.

Steps: python3 skills/identify-comparable-transactions/scripts/comparables.py input.json --pretty; python3 skills/compare-deal-terms-to-benchmarks/scripts/benchmarks.py input.json --pretty; python3 skills/synthesize-market-standard-terms/scripts/market_standard.py input.json --pretty. Each skill ends with its register validator (scripts/validate_register.py); read the failure-mode screen and the questions with the deal lead.

Never: fetching deals from memory, or declaring a term fair or market standard; produce a single value; produce a recommendation, a fairness opinion or a solvency view. The adopted valuation is HUMAN ONLY and the recommended valuation stays empty. Every figure is a range with its sensitivity.
