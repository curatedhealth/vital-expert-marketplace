# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the key's monthly allowance; free calls do not. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

Most of this skill runs on the person's own records and `scripts/launch_measures.py`. The library supplies the public side: dated authorizations and listings for the product and its peers, and change events where the library has them.

## commercial-dh.list_commercial_dh_sources (free)

- No arguments. Use it first in A1 to say what the library can see and how fresh it is (DE_DIGA loaded 15 October 2026, "not the history feed"; no UK device registrations; no Swiss records; EU decision dates empty).

## commercial-dh.get_deltas (counted)

- Required `reference`. Optional `since` (YYYY-MM-DD).
- Copies `what`, `event_date`, `observed_at`, `source_url` from three upstream delta tools and names each.
- Observed: `{reference: "deprexis", since: "2026-01-01"}` and `{reference: "Big Health", since: "2020-01-01"}` both returned no events. The regulatory and census feeds returned empty lists with `gap: null`; the Market Access feed returned `[GAP]` "market_access_dh.get_deltas is not on that server". For Big Health the library holds a Sleepio NICE listing dated 20 May 2022, inside the window, which no feed returned.
- Reading: an empty result does not mean nothing changed. Earlier builds found that delta feeds return rows only after a watch is registered (register C11), and watches are not separated per customer key (register N2). Write "no change events available from the library `[GAP]`" and use step 2 of A1 instead: compare two dated runs of the sequence.

## commercial-dh.get_launch_sequence (counted)

- Required `reference`. Optional `peers` (up to 10 exact names), `limit`, `route_hypothesis`.
- The reliable way to monitor today: run it for the product and its peers, save the output with its date, and compare with the earlier saved run. A new `changed_on`, a new peer listing or a removed row is a change; say which run it came from.
- Observed pitfalls (details in the sibling skill's tools file and `examples/live/launch_sequence_runs.json`): unmatched peers dropped silently; a brand name does not reach the FDA record (use the K number); "HelloBetter" merged six DiGA-IDs; second `changed_on` events (Selfapy 11 April 2022, Novego 9 October 2023, HelloBetter 17 July 2023) carry no status value.

## market-access-dh.find_scheme_precedents (counted)

- Required `scheme`. Optional `indication`, `limit`.
- Use it for the cohort around the product: `{scheme: "DE_DIGA", indication: "F32", limit: 10}` returned seven depression DiGA with status, listing date, price as stated and source. A provisional row (elona explore, listed 18 February 2025) carries no end date: the trial end is `[GAP]`.
- Prices in these rows are the register amounts as stored, not negotiated or current prices; they are context, never the buyer's price.

## analytics.rice (counted), B1 only on the person's scores

- Observed (illustrative numbers, `examples/live/rice_runs.json`): `confidence` is read as a percent and divided by 100 without warning (0.8 became 0.008). Pass it as a percent and check one score by hand.

## analytics.mcda (counted), B1 only on the person's scores

- Not called in this build. Register C17 records its behavior: 0 to 4 scores, weights summing to 1, every criterion higher-is-better, no robustness view.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Use it only when an output leaves the conversation.

## Not called here

- `commercial-dh.watch_product`: not called. It registers watches that are not separated per customer key (register N2); do not put a confidential product name into a watch.
- The person's field records never go into a library call.
- `get_launch_readiness` and `generate_commercial_brief`: planning tools of the sibling skill; their outputs are large (102,610 and 72,154 characters observed) and add nothing to monitoring.
