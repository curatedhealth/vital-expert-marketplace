# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not.

Behavior below was observed in live calls on 19 October 2026. Saved output: `examples/change_tracking_live_2026-10-19.json`.

## market-access-dh.list_schemes (free)

- Shows listing counts and last load per scheme. US_CMS_RPM and US_CMS_DMHT were loaded 15 October 2026; DE_DIGA 15 October 2026; FR_PECAN and FR_LATM 16 October 2026.
- The last-load date is the earliest a library-visible change can appear.

## market-access-dh.find_scheme_precedents (counted)

- `{scheme: "US_CMS_RPM"}` and `{scheme: "US_CMS_DMHT"}` return the current code rows with amounts in the evidence passage. Use them as today's value for a code; compare with the person's earlier run or contract value.
- `{scheme: "DE_DIGA", indication: <ICD code>}` returns comparators' current stored prices.
- Pitfall: `price` is empty for 99457, 99458, G0553, G0554 although the passage states the amount; the coding skill's `scripts/price_facts.py` parses it.

## market-access-dh.get_status_history (counted)

- For CMS codes: one row, the day-zero snapshot of 15 October 2026, with the gap "transition history not published". No amount history.
- For DiGA: listed products show one row dated at the listing date; deleted ones show two. No price history is stored for any scheme.

## market-access-dh.search_listings (counted)

- Product name or code. A code not in the store (for example 99445) returns nothing, with a gap line.

## commercial-dh.get_deltas (counted)

- `{reference, since}`. On 19 October 2026 for "deprexis" since 1 January 2026: no events; the Market Access feed returned "[GAP] market_access_dh.get_deltas is not on that server". It cannot report code or price changes today.

## Not used here

- `watch_scheme`: watches are not separated by customer key; do not put a confidential product name in one. Call only if the person asks to be told of changes, and say changes appear after the next library refresh.
- `verify.verify_text` and `verify.check_claim` on register facts: they rate register pages "no provenance".
- The person's claims, prices and contract terms never go into a library call.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Use only when an output leaves the conversation.
