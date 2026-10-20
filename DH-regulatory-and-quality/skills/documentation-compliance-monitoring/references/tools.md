# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not. Behavior observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

This competency runs on the person's own document list and change log. Those never go into a library call. The library adds public recall context and record clearance only.

## regulatory-dh.search_safety_events (counted)

- Needs at least one of `manufacturer`, `product`, `product_code`; `jurisdiction` alone returns "give manufacturer, product or product_code".
- Returns FDA recalls whose product text mentions software, algorithm, application, firmware or app (event date, class, manufacturer, summary) and MAUDE report counts by year.
- Use in A2 only when the person asks how release-control failures show up in the field. Example rows (event dates as stored): Class I recall of a CGM Android app version 1.15.0 that "can cause the app to terminate unexpectedly" (28 August 2025); Class II recall of CGM iOS and watchOS app versions 2.9.0 through 2.11.2 for a background-processing defect (14 April 2026).
- Pitfalls seen:
  - Rows carry no product code; a `product_code` filter cannot be confirmed from the row.
  - The software filter matches title text: a sensor-theft recall matched because its title says "Software Version: N/A". Flag non-software rows.
  - `product_code: "LLZ"` returned nothing while `product: "software"` returned PACS software recalls.
  - `maude_counts` can list product codes unrelated to the returned recalls; counts are reports, not confirmed events.
  - `source_url` is the openFDA API endpoint, not the recall record; cite firm, product, version and event date and ask the person to confirm in FDA's recall database.
- UK: MHRA alerts only (10 loaded); CH: nothing loaded (`list_jurisdictions`).

## regulatory-dh.retrieve_guidance (counted)

- No passage for the QMSR, FDA's 2017 software-change guidance or MDCG 2020-3. Do not use it for rules; use `references/`.

## verify.build_record (counted)

- Needs a named human in `cleared_by.name`. Observed: `{name: "Claude"}` refused ("build_record refuses a record without a human cleared_by.name").
- Use only when a check or plan leaves the conversation and the person names who clears it. Do not put confidential document titles in the record text unless the person agrees.

## agent-pack.list_experts

- `query: "quality"` returns the bound worker `quality-assurance-manager-software` and `quality-systems-director-software`. Offer a download only on request.

## Not used here

- `verify.check_claim` to judge a rationale: it can return "supported" on word overlap (register item N3). A rationale's adequacy is the owner's judgment.
- `get_deltas` and `watch_register`: not needed; the person's log is the change history.
