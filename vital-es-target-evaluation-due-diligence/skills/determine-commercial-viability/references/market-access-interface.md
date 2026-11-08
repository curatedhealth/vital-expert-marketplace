# Interface to the Market Access pack (read-only)

Status: written 7 November 2026 from a read-only look at `mcps/market_access/plugin/vital-pharma-market-access/` (README: "Status: draft 0.1.0 (6 November 2026). Not yet reviewed by market access, legal or regulatory reviewers."). The pack is not Released. Nothing in the pack was edited, and nothing from it is used as a figure here.

**Rule.** Pricing, reimbursement and access assumptions are never built in this plugin. The viability skill accepts them only from the pack, only when the pack is Released, and only as records that carry the pack's own source and support rating. Until then each is a GAP, with this consequence written on the register: *the peak-sales range is not adjusted for price, coverage or access and may be overstated; the decision cannot rely on a price or coverage assumption.*

## What this skill reads, and from which pack skill
| Input to this skill | Pack skill (name as listed in the pack) | Fields read | Used for |
|---|---|---|---|
| Assumed listing date, restrictions, share of eligible patients with access, price status, support rating | access-assumption-register | per market: assumed_listing_date, restrictions, share_of_eligible_with_access, price_status, source_or_owner, support_rating | condition C-MA; the access paragraph of the register |
| Price constraints per market (comparator cost, reference-price caps, the binding constraint) | launch-price-corridor-assembly | per market: constraint_stack, binding_constraint (it proposes no price) | the access paragraph; never a price in the range |
| Route from authorization to paid access and the interval between them | market-pathway-mapping | per market: route, interval_authorization_to_listing, decision_points | context for the expected launch date supplied by the buyer |
| Barriers between authorization and patients | access-environment-and-barrier-assessment | per market: barriers with sourced rows | questions for the decision owner |
| Named access scenarios as input sets | access-scenario-inputs | base case and alternatives with triggers | what would change the call |

## Record the skill expects (one per market)
`{market, pack_skill, record_id, fields, source, support_rating, pack_commit, pack_release_state}`

- `pack_release_state` must read "Released" for the record to count; any other value (for example "draft 0.1.0") makes the record a GAP.
- `source` is the pack's source for the field; the viability skill never replaces it.
- `access_inputs` in scripts/option_set.py carries `pack_release_state` and `records`; condition C-MA is "met" only when the state is Released and records is not empty.

## Competitor signals
The pack's `competitor-pipeline-and-launch-signals` and `competitor-access-tracking` can lead to competitor entries for the market register (skill G). They are leads: each entry still needs its own dated source in the market register.

## What this skill does not do
It does not read the pack's price figures into the range, apply a net-price haircut, model coverage, or ask the pack to produce a forecast (the pack states it builds no forecast model). Revenue forecasting and deal value are not in this plugin's release; they hand off to a valuation capability.

## Open items for the owner
1. The pack's release state and the date it is expected to be Released.
2. Whether a record format other than the one above is preferred; this interface can change without touching the scripts, which read only `pack_release_state` and `records`.

## Amendment of 7 November 2026 (owner ruling R7)
Price and revenue ranges are no longer expected from the Market Access pack. They come from the signed register of skill forecast-revenue-and-price-ranges (condition C-RV). The pack remains the source for coverage and access assumptions (condition C-MA) and its price figures are shown only as a side-by-side cross-check against the revenue register, never merged and counted only when the pack is Released. The scripts are unchanged in behavior when the input carries no `revenue_inputs` block.
