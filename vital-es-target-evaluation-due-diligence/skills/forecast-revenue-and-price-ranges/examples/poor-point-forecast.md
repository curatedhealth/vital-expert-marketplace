# Poor example (fictional asset; not a real product)

"RX-640 will make 1.4 billion euros a year across the EU at a 60 percent discount-adjusted net price, risk-adjusted by the 11 percent probability of success and discounted at 9 percent. The recommended forecast is the mid case."

What is wrong, and which check catches it:
- A point figure with no range: rule FC-ADOPTION-HUMAN; the validator rejects a point (E_POINT).
- "Across the EU" as one price: FC-COUNTRY-ONLY; E_MARKET.
- A net price with no setter and presented as fact: FC-NET-ASSUMPTION; E_NET, E_CROSSCHECK for any merged Market Access value.
- Risk-adjusted by the probability of success and discounted: FC-NO-RISK-ADJUSTMENT and FC-NO-DISCOUNTING; E_RISK_ADJUST and E_DISCOUNT in the calculator.
- A recommended forecast: the adopted forecast is human only; E_ADOPT_FIELD and E_ADOPT_TEXT.
- No sensitivity table and no failure-mode screen: E_SENSITIVITY, E_FM_UNRESOLVED.

## Fact patterns and the passages they follow
| Pattern | Documented in | Passage ids |
|---|---|---|
| a single optimistic number | forecasts of sales have run high | VP-H-001, VP-H-010 |
| net stated as a fact | net prices are confidential or differ by payer | VP-R-021, VP-R-023 |
| one price for several countries | discounts and rebates differ by country | VP-R-020, VP-R-021 |
