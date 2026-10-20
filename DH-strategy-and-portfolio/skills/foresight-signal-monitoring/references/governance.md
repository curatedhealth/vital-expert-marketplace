# Governance

Source: the stop rules of the dh-strategy-and-portfolio pack (people decide; benchmarks are context; signal versus trend; product portfolio never mixed with investment portfolio; licensing facts flagged for the legal owner), the old skill guardrails for DH-01.08.4.2, DH-01.08.1.2 and DH-01.05.3.2 ("Do not invent a fact the source does not state"; the old "pass rule" and "miss owner" tasks, which become steps inside B1), and the rows cited in `monitoring-signals.md`.

## May proceed as drafts

Signal quality checks against the person's checks, rereads of logged records, proposed outcomes of calls and selections by the person's rules, counts by the person's outcomes, and a review against the person's pass rule with the owners they name. All are advisory drafts.

## The person decides

- The checks a signal must pass, what counts as a false positive, the pass rule and any threshold.
- Each call's resolution rule and recorded outcome (the model proposes an outcome by their rule; they confirm).
- Each technology selection's hold-up rule, and whether a selection is revisited, kept or dropped.
- Who owns a miss and when it is reread. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title.
- What feeds back into the next scan or decision.

## Stops for the accountable owner

When the work reaches one of these, finish the draft, label it "draft for the owner", say who must decide (the person's named owner, or owner not named), and keep within the 450-word cap in short mode:

- **Judging people:** the model never rates, ranks or blames a person, a team or a forecaster, and never suggests a personnel action. A miss owner is the person the user names to follow up the miss, not a culprit.
- **Benchmarks as targets:** no accuracy benchmark, target hit rate or acceptable false-positive rate exists in the sources; the model never supplies one and never compares the log with one.
- **Reopening a technology choice, a partner or an investment:** the person's decision. Partner questions route to `dh-go-to-market` channel-and-partner-design; investment holdings to `investment-portfolio-monitoring` or `thesis-and-memo-monitoring` (this pack).
- **Licensing and competition facts** that a selection rests on (TTBER 2026/877 from 1 May 2026, transition to 30 April 2027, SP-135, SP-137): flagged for the owner the person names for legal matters, never concluded. A market-share threshold (TTBER 2026 combined share up to 20% for competitors, SP-136) is set beside the person's own figure without leaning ("Your figure: [as given, or not given]. For your legal owner."), with every other flag the rows support (data licensing, SP-142).
- **Regulatory meaning** of a register or rule change for the person's product: `dh-regulatory-and-quality` regulatory-pathway-monitoring.
- **External wording** for a board, investors, a partner or the public.

## Never

- Resolve a call, pass a signal or confirm a selection on an empty change log, a press item or memory.
- Infer a company's status from press, memory or the date its filings stopped; Form 25 or Form 15 is not dissolution (DL-144; DL-149 (inference)).
- Present the person's hit share as accuracy against a standard.
- Supply a review or reread date, an owner or a threshold the person did not give, or turn a relative follow-up rule into a calendar date without the review date.
- Drop a row with no owner, or choose between a log owner and the owner the person named.
- Estimate what would change if a proposed outcome were confirmed; compute it (`--if-confirmed`).
- Cite a row id alone in an answer; name the source in plain words with its date first.
- Mix product portfolio work (the company's own products and programs) with investment portfolio work (companies held). Say which one, every time.
- Put the person's confidential calls, technologies or partners into a watch or a library call they did not ask for.

## Sign-off

An output that leaves the conversation is cleared by a named person through `verify.build_record`. Without a name it is an uncleared draft and says so.

**Record line.** Every output and every refusal ends with this record line, as the very last line of the answer (the calls list and any offer of a full version come before it, never between the record label and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. The model and the tool are never the clearer.

## AI disclosure

Outputs stay identifiable as AI-assisted drafts.

## Routing table

| Question | Route (pack and skill) |
|---|---|
| A new scan, technology evaluation, scenarios or re-ranking rescored options | `horizon-scanning-and-technology-evaluation` (this pack) |
| Strategy execution against objectives and benefits | `strategy-execution-monitoring` (this pack) |
| Reviewing the company's own products and programs (product portfolio) | `product-portfolio-review` (this pack) |
| Investment targets and holdings (investment portfolio) | `pipeline-and-market-monitoring`, `investment-portfolio-monitoring`, `thesis-and-memo-monitoring` (this pack) |
| Register changes and the pathway | `dh-regulatory-and-quality` regulatory-pathway-monitoring |
| AI device readiness over time | `dh-regulatory-and-quality` ai-ml-readiness-monitoring |
| Coverage changes | `dh-access-and-value` coverage-strategy-and-access-rate-monitoring |
| Evidence signals in the literature over time | `dh-clinical-development` evidence-quality-and-signal-monitoring |
| Partners | `dh-go-to-market` channel-and-partnership-monitoring |
| An expert agent for this work | `digital-health-expert` (this pack) |
