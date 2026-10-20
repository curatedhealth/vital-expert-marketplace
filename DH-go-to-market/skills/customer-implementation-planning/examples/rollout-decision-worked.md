# Worked example: B1 go-live bar and rollout decision

Run on 19 October 2026. The ranking is a real library call (`live/mcda_rollout_options.json`); the scores and weights were typed for the measurement and are presented here as the example person's. The clinic count and names are illustrative.

**Request:** "Eight clinics in the network. We're torn between two pilot clinics first then the other six, all eight at once, or region by region. Here are our scores (0 to 4) and weights. Rank them. Also, what should the go-live bar be for the pilots? Dr Park at the pilot clinic signs off."

Person's criteria and weights: site readiness covered 0.5, staff capacity spared 0.3, speed to all sites 0.2.
Person's scores: pilot-then-six 4, 3, 1; all eight 1, 1, 4; by region 3, 2, 2.

**Calls**

1. `analytics.mcda {alternatives: [{id: "staged: 2 pilot clinics then 6", scores: {...}}, {id: "all 8 clinics at once", ...}, {id: "staged by region", ...}], criteria_weights: {"site readiness covered": 0.5, "staff capacity spared": 0.3, "speed to all sites": 0.2}}` (first attempt 502, nothing counted; retry succeeded)

## Answer (short mode)

**The ranking of your scores: two pilot clinics then six (77.5), by region (62.5), all eight at once (40).** The order holds unless speed to all sites is weighted about 0.45 or more while site readiness drops to 0.25 or less (staff capacity unchanged): at 0.45 and 0.25 pilot-first and all-at-once tie at 58.75. This is the result of your scores, not a recommendation.

Facts behind the options: ERIC describes staged scale-up from small pilots to system-wide rollout (CS47); trialability includes being able to undo after a small test (CS5).

**Go-live bar for the pilot clinics (starting list for you to keep, change or drop):**

| # | Item | Evidence | Basis |
|---|---|---|---|
| G1 | Named user roles complete one real task in the day-one workflow | Task log by role | Register method |
| G2 | The data the workflow needs is present and flows as mapped | Data check against the data dictionary | CS64 |
| G3 | BAA signed before PHI flows | Signed agreement | Required, CS96 |
| G4 | Roles and access match job need | Role list vs access set | CS104 |
| G5 | Users trained on outputs and limitations, matching validated training | Training record by role | CS65, CS80 |
| G7 | Expected usage profile and reporting agreed | Agreed profile | CS61, CS62 |

**Pass rule:** not set. The register's phrasing you could adopt: "a pass only when each bar item has evidence". Which do you want?
**Site approver:** Dr Park (yours).
**Owner if an item is missed:** owner not named for each item. Who owns each, and does the clinic stay in limited launch on a miss?

**Stops:** sending this bar to the health system as the go-live plan stops for your accountable owner. The model does not call the clinic live; Dr Park agrees the bar is met.

**Record:** Go-live bar and ranking draft. Uncleared. AI-assisted.

The full version adds the contribution table by criterion and the reporting plan after go-live.

## Check of the connector's values

Weighted sums by hand: pilot 0.5 x 4 + 0.3 x 3 + 0.2 x 1 = 3.1, divided by 4 = 77.5; region 2.5 = 62.5; all eight 1.6 = 40. They match the connector. Flip point: moving weight x from site readiness to speed gives pilot 3.1 - 3x and all eight 1.6 + 3x, equal at x = 0.25.

## What this example shows

- The ranking is the person's scores, with the flip point stated; no score was filled.
- The bar is offered as a starting list, with evidence types; the approver is the person's; owners stay "owner not named" until named.
