# Authority and evidence posture (user-visible)

Owner ruling, 7 November 2026. Capability CF-01.06.01.

Anything Outcome Navigator **uses or recommends to the user** must show its warrant. Two lanes only:

| Lane | Authority | User-facing form | Insufficient if |
|---|---|---|---|
| **A** Established practice | Citable standard, official guidance, peer-reviewed method, or widely cited facilitation practice | “Per [source, year] …” / “Aligned with [standard] …” | Blog-only, undated, or unsourced “best practice” |
| **B** VITAL benchmarks / testing | Known-answer suite, back-test run, offline validator exit, harness grade | “Checked against VITAL KA [id] ([date]) …” / “Validator `script` exit 0” | Author self-sign without independent grade where required |

## Hard don'ts
- Do not advise Proceed on a point that lacks Lane A and Lane B — use Investigate first or `[GAP]`.
- Do not present teaching-example figures as live evidence.
- Do not present peer-adapted `[CHECK]` method lines as VERIFIED statute.
- Do not use model confidence as authority.

## Where to show the warrant
1. Decision record / board pack integrity posture line.
2. Exhibit footnotes (source_id + authority lane).
3. IC one-pager (fit-the-ic-reader) — short warrant under the ask.
4. Facilitation aside when recommending a method move (“we use private scoring first — per [Lane A] / checked in [Lane B]”).

## Absorption filter (for research returns already in flight)
When Perplexity/Gemini outputs arrive from a prompt fired before this posture was spelled in the prompt text, still apply this filter before editing the kit: no Lane A or B → do not land as user-facing recommendation; park as `[CHECK]` / editor note only.
