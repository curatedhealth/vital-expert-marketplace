# Market Access interface (owner ruling R1)

This skill is a deal-level estimate of revenue and price for a buyer or investor. The Market Access pack (vital-pharma-market-access) covers local and regional reimbursement, coverage and access. The two are different questions and their outputs are never merged.

- **Cross-check only.** When pack outputs exist for a country, they appear in separate columns of the register (`market_access_cross_check`: pack state, peak net revenue range or null, source reference) beside the ranges of this skill.
- **Counted only when Released.** A pack that is not Released (draft 0.1.0 at the time of writing) or that carries no records contributes nothing; the register says so.
- **No back-flow.** The ranges of this skill do not change when a cross-check value is added; a difference between the two is shown, not reconciled, and is a question for the named reviewer.
- **No price or coverage invented here.** List prices come from dated public sources (references/source-register.md); net prices are the deal team's assumption ranges (FC-NET-ASSUMPTION); coverage and access are not modelled.
