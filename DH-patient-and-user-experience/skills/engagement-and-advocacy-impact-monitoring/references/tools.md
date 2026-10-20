# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names are the library's; your assistant may prefix them (for example `analytics_rice`). Counted calls draw on the library key's monthly allowance. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

This is a method pack. The computation runs on the person's own logs in `scripts/engagement_monitor.py`. The library adds a ranking calculator for changes the person scored, literature and Verify for published comparators, and the record. Several calls on 19 October 2026 first returned 503 or 502 ("Nothing was counted"); a retry worked. Retry once, then say the library did not answer.

## analytics.rice (counted; B1)

- Arguments: `initiatives`, each with `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`. Every number is the person's.
- Score = reach x impact x confidence / effort.
- Pitfall seen: `confidence` is read as a percent. Passing 0.8 returned confidence 0.008 and scores one hundred times too small (3.6 instead of 360); passing 80 returned confidence 0.8 and score 360. The order was the same in this test, but mixed inputs would distort it. Always pass confidence as a percent (0 to 100) and say so to the person.
- The response note says "Public registers and published literature" and mentions price figures; it does not apply to RICE inputs.
- RICE ranks changes the person scored. It never decides to stop, change or keep an activity.

## analytics.mcda (counted; B1, alternative)

- Arguments: `alternatives` (id and 0 to 4 scores) and `criteria_weights` (summing to 1). Value = sum of weight times score / 4, times 100. Every criterion is treated as higher-is-better; no robustness view (register C17). Measured in the sibling skill (DH-02.03.2.1).

## literature.search_literature (counted; A1 or A2, optional)

- Arguments: `query`, optional `limit`, `filters` (`date_from`, `designs`).
- Observed: "patient support program digital health engagement attrition evaluation" since 2020 returned a 2026 JMIR mixed-methods systematic review of attrition in digital self-management for MASLD (doi 10.2196/89124), a 2025 npj Digital Medicine paper on engagement and attrition in digital mental health, a real-world obesity service cohort, and one off-topic record. `trial_ids` empty on every record; one record came from Crossref only with no abstract.
- Use only after reading the paper; a published attrition rate is context, never a target.

## verify.qualify_source then verify.check_claim (counted)

- `check_claim` does not judge direction (register N3): from a passage stating 27 percent of funded patient organizations disclosed funding, it returned "supported" for "about a quarter disclosed" and for "Most disclosed". Accept a claim only when you have read the passage and it states the claim in the same direction.
- Pass the object returned by `qualify_source` as `source`; `{doi, source_id}` alone returned 502 twice.
- The returned citation had DOI, authors and year empty (register C18). Build the citation from the paper.

## verify.build_record (counted)

- Refused `cleared_by.name` "Claude": "build_record refuses a record without a human cleared_by.name". Call it only when the person names who clears an output that leaves the conversation.

## agent-pack.download_agent

- The Digital Marketing Manager (`digital-marketing-manager`) download carries the three old monitoring tasks (Engagement result definition, Activity score, Programme change) and the stop rules used in `governance.md`.

## Not used

- `commercial-dh.audit_claims`: off-list claims are checked against the person's own allowed list; label checks belong to the design skill (A1) and Commercial 3.2.
- `watch_*` tools.
