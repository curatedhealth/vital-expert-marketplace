# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not.

This competency runs mostly on the person's own data. The library adds public signals on a partner that is a regulated digital health company or an SEC filer, a claim screen with a strong caution, a ranking calculator for remediation work the person scored, and the record. It holds no partner performance data. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## diligence-dh.get_deltas (counted)

- Arguments: `companies` (1 to 12 references), `since` (YYYY-MM-DD).
- Returns per company "no change recorded" or the changes (authorizations, studies, safety events, filings, awards), plus the log's first entry, last entry and last sweep times and its limits.
- Observed (`["Akili Interactive Labs, Inc.", "Pear Therapeutics, Inc."]`, since 1 January 2026): both "no change recorded"; log first entry 12 October 2026, last sweep 19 October 2026. The log filters on event dates, not load dates, and began on its first entry date.
- Use: "anything new in the public record about this partner since the last review". Report "no change recorded in the library's log since DATE (log started 12 October 2026)", never "nothing happened". No watch is needed; do not call `watch_*` tools.

## commercial-dh.get_deltas (counted)

- Arguments: `reference`, `since`. Merges the regulatory, Diligence and Market Access delta feeds.
- Observed (`Akili Interactive Labs, Inc.`, since 1 January 2026): no events; the Market Access feed returned `[GAP]` "market_access_dh.get_deltas is not on that server". Prefer `diligence-dh.get_deltas` for partners.

## diligence-dh.get_funding_signals (counted)

- Argument: `company`. SEC filings made by the company, NIH grants, EU TED awards, each with URL and retrieval date; private rounds `[GAP]`.
- Observed (`Pear Therapeutics, Inc.`): 46 SEC filings including 25 Form 8-K, dated 9 February 2016 to 10 April 2023.
- Pitfalls: no 8-K item number and `counterparty` null on every row, so a material definitive agreement (Item 1.01, CP-US-79) cannot be found without opening the filing; `sum_of_stated_amounts` adds different filing types; the latest filing date is not a status. Never read financial health or intent from filings.

## commercial-dh.audit_claims (counted)

- Arguments: `reference` (exact FDA number or normalized name), `claims` (up to 20), optional `intended_use`.
- Observed (`reference: "K231337"`, three claims of different strength, from a near paraphrase of a cleared use to "clinically proven to cure ADHD"): `intended_purpose_from_record` was `[GAP]`, yet all three came back "exceeds_record". With no intended purpose on file the tool cannot tell a faithful claim from an overreach. Inside the same response, the device search by "K231337" found nothing while the authorization lookup found the record.
- Use only as a screen when the person asks, and say: "the tool had no intended purpose to compare against, so its labels are not findings". The comparison that counts is against the person's approved claim list, and the decision is the regulatory or legal owner's.

## analytics.rice (counted)

- Argument: `initiatives` with `id`, `reach`, `impact`, `confidence`, `effort`.
- Pitfall: confidence is read as a percent. Sending 0.8 returned 0.008 and scores 100 times too small; send 80. Impact 1.5 was accepted although only 0.25, 0.5, 1, 2 or 3 are allowed. Observed with percent confidence: 540, 200, 150 and 133.33 for four initiatives. Details and saved calls are in the design skill (`channel-and-partner-design/examples/live/`).
- Use only when the person scores remediation initiatives in B1.

## agent-pack.download_agent

- `digital-partnerships-director` (108,025 characters). Its stop rules are the source of `references/governance.md`. Offer it only when the person wants the role on their own assistant.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`; refuses a missing, tool or model name. Call it only when an output leaves the conversation and the person names who clears it.

## Not used here

- `verify.qualify_source` on regulator or OIG pages: rated "inadmissible, no provenance" (OIG AO 26-15, 19 October 2026). The CP rows carry URL, quote and read date; cite them directly.
- `diligence-dh.retrieve_guidance`: "anti-kickback safe harbor" returned no passage.
- `watch_*` tools.
