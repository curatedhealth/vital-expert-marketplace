# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted".

**How this file was built.** The connector was disconnected during this build (20 October 2026: a tool search for the regulatory suite returned no tools), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied into `examples/live/` (file named on each entry, read 20 October 2026), and from those builds' `tools.md` files. Where a tool has no saved output for the use this skill makes of it, the step is marked **needs a live check**. Most of this skill runs on the person's own control matrix, vulnerability log, consent text, processing list and test logs through `scripts/secops_check.py`; the library supplies safety events in the product's category and authorization records, and Verify supplies the record.

## regulatory-dh.get_authorization (counted; A2 step 1, only when the person names an authorized product)

- Arguments: `reference` (a K, DEN or P number).
- Saved output: none in this skill (the sibling design skill holds `get_authorization_K191716.json`, retrieved 19 October 2026: Somryst, FDA 510(k), decision 23 March 2020). Use only to state the pathway and decision date of a product the person names.
- Pitfalls: De Novo records may show the raw FDA code `status: "DENG"` (register C3); write "De Novo granted". Search by product name is exact matching (register C7); prefer the K, DEN or P number. No cybersecurity field is stored.

## regulatory-dh.search_devices (counted; A2 step 1, to find the authorization number when the person gives only a name)

- Arguments seen in saved outputs of other builds: `manufacturer`, `product`, `product_code`, `jurisdiction`, `limit`.
- Pitfalls from those builds: names must match the stored legal name (register C7: "Viz.Al, Inc." stored with a letter l, register N1). **Needs a live check** for this skill's use; when it misses, ask the person for the authorization number.

## regulatory-dh.search_safety_events (counted; A2 step 5, optional, to read recalls in the person's product category)

- Arguments (all optional): `manufacturer`, `product`, `product_code`, `jurisdiction` (US, EU, UK, CH, all), `since` (YYYY-MM-DD), `limit` 1 to 25 (from the regulatory builds' tools files).
- Saved: `safety_events_insulin_us.json` (`{product: "insulin", jurisdiction: "US", since: "2025-01-01", limit: 10}`, retrieved 19 October 2026, trimmed by the build that saved it: "6 results returned; all fields kept for the 3 interface-related rows, others summarized"). The three full rows: Insulet Corporation, Omnipod 5 iOS App, Class II, 23 May 2025 (summary: a software design issue in which a comma is not recognized as a decimal separator); Tandem Diabetes Care, Inc., t:slim X2 with mobile app, Class II, 3 July 2025 (summary: an app defect with right-to-left phone languages causing pairing issues and graphical defects); Tandem Diabetes Care, Inc., Tandem Mobi, Class I, 6 October 2025 (summary: false vibration motor failure). MAUDE block: product code QRX, 1 report in 2022, "counts are reports, not confirmed events". None of the three summaries names a security cause.
- No saved output in any build returns a recall whose summary names a cybersecurity cause; a keyword search of every saved `safety_events*` file for "cyber", "security", "vulnerab", "unauthori" and "hack" on 20 October 2026 found none. Whether the tool can find cybersecurity recalls (for example with `product: "cybersecurity"` or by manufacturer) **needs a live check**.
- Pitfalls from the regulatory builds: `product` matches the whole phrase (register C9); `product_code` filters MAUDE counts, not recalls; recall `source_url` is the openFDA endpoint, not the recall page (register C1); MHRA `manufacturer` can name a firm the alert text does not (register N1). Describe each event only by what its record states; never judge its relevance to the person's product.

## regulatory-dh.retrieve_guidance (not used)

The regulatory builds found passages without source URL or read date and off-topic hits (register C6). Cybersecurity queries were not run in any saved output: **needs a live check**. Requirements in this skill come from `references/` only.

## verify.build_record (counted; every task, when a record leaves the conversation)

- Saved: `verify_build_record_refusal.json` (19 October 2026): with `cleared_by: {name: "Claude"}, role: "model"`, the tool returned "build_record refuses a record without a human cleared_by.name".
- Use: only after a named person clears the output; pass their name in `cleared_by`.

## verify.qualify_source and verify.check_claim (not needed for regulator texts)

The regulatory builds saw regulator and eCFR pages rated "inadmissible, no provenance" (register C1). Requirements here carry their URL, quote and read date in the research rows. Accept any Verify "supported" only with a passage read in the same direction (register N3).

## Catalogue

- Saved: `list_jobs_2026-10-19.json` (19 October 2026): no catalogue job covers security or privacy. Catalogue job for every task: none.

## Not called

`watch_*` tools (never called by this skill), `generate_report`, `compare_authorizations`.
