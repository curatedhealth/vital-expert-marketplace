---
command: /val-dcf-check
args: [asset or company, buyer_mode (bd|investor), unit (asset|company), currency, valuation_date]
---
Run intake and then the skills of one mission in order: build-dcf-model, then calculate-risk-adjusted-npv, then validate-valuation-assumptions (mission 1). See skills/financial-modeling-and-valuation-capability-map/SKILL.md.

Inputs needed before any step: The revenue register (R), the timeline and probability register (B) and the exclusivity register (C) of the due diligence plugin; costs, tax, capital and the discount-rate range from the deal team. Ask for every missing argument in one message and do not start on an assumption. A missing upstream register is a [GAP]: name its consequence and the skill to run, and do not fill it.

Steps: python3 skills/build-dcf-model/scripts/dcf.py input.json --pretty; python3 skills/calculate-risk-adjusted-npv/scripts/rnpv.py input.json --pretty. Each skill ends with its register validator (scripts/validate_register.py); read the failure-mode screen and the questions with the deal lead.

Never: choosing the discount rate or the probability; produce a single value; produce a recommendation, a fairness opinion or a solvency view. The adopted valuation is HUMAN ONLY and the recommended valuation stays empty. Every figure is a range with its sensitivity.
