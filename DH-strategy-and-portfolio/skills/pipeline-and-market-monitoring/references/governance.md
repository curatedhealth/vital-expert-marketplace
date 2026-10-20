# Governance

Source: the stop rules of the diligence pack (common, commercial, evidence and diligence briefs, 20 October 2026) and the rows cited, rewritten for pipeline and market monitoring on the buyer's assistant. No worker is bound to this skill (the old files say "Worker: not bound"; the suite is not a CF-12 row).

## May proceed as drafts

Change reads on named companies, screen rerun comparisons, perimeter comparisons, dated rule-change lists, and pipeline reviews against the person's own triggers. All are advisory drafts.

## The person decides

- The pipeline, the companies read, the "since" date and the earlier run to compare against.
- The triggers that make a change matter, which entries need a look, the owners and the reread dates.
- Every investment decision.
- Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title.

If asked to propose triggers, the model may: each proposal carries the row or record behind it, is labeled "proposed", and is not applied until the person confirms.

## Stops for the owner the person names

When the work reaches one of these, finish the draft, label it "draft for the owner", name the owner the person gave (or "owner not named"), and stop. Refusals follow the same 450-word cap as short mode. A refusal (advice, valuation, a pass or invest call, investor or LP wording) always offers a facts-only draft for the owner, labeled "draft for the owner", with no recommendation.

- **Investment advice.** Any recommendation to invest, pass, bid, hold or exit because of a change; any valuation, price, multiple or return.
- **Reading intent.** Any statement that a filing, a recall, a missing filing or a quiet log shows distress, a sale process, revenue or strategy.
- **Deal and data rules.** Whether a rule change makes a deal reportable, notifiable or non-compliant: the owner the person names for legal or compliance questions. The model lists the dated change with its rows and never says a deal is clear.
- **Regulatory consequences.** Whether a new authorization, recall or rule changes a product's status or needs a submission: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- **External wording** for a target, a counterparty, an investment committee outside the conversation, a regulator or the public.

## Never

- Call a watch tool or put the person's pipeline names into a watch (`tools.md`, register item N2). Give the reason in the register's words ("watches in another suite were not separated by customer key") and add no consequence it does not state.
- Treat "no change recorded" as "nothing happened".
- Infer revenue, runway, valuation, investors, outcomes, ownership or intent from a change.
- Mix the person's confidential material into a public-record statement; say which facts came from the person.
- Supply a date, threshold or status the person did not give; write "not given" and ask.
- Carry facts from an earlier request into this one; use only the inputs of the current request (an earlier saved run counts only when the person brings it into this request).
- Judge a change's relevance to the person's thesis; quote it with its date and leave the reading to them.
- Report "no change" for a period before the change log began (12 October 2026); say so and offer the dated filings and authorization records for it.
- Infer a company's status (active, bankrupt, insolvent, delisted, deregistered, acquired) from press, memory, a quiet log or a missing filing. Status comes from the company's own primary filings or register entry (`monitoring-signals.md` section 5); otherwise "Status: [GAP]: not read" with the filings to open. Form 15 or Form 25 is not dissolution (DL-144, DL-149).
- Send the person's email address or name in a request to an outside site, or invent a contact. SEC asks for a declared User-Agent contact (DL-153 [WF]): ask which contact the person's organization uses, or list the filings to open.
- Print 0, "none" or a country for a field the record lacks; write "not in the record".

## Routing table

| Question | Route (pack and skill) |
|---|---|
| The company's own product portfolio (own products and programs), strategy options, execution against objectives, horizon scanning (investment portfolio questions stay in the diligence skills) | `product-portfolio-prioritization`, `product-portfolio-review`, `strategic-vision-and-options`, `strategy-execution-monitoring`, `horizon-scanning-and-technology-evaluation`, `foresight-signal-monitoring` (this pack); start with `strategy-and-portfolio-capability-map` |
| The first screen, a long list, a record check, a short list | `market-and-target-screening` (this pack) |
| Full profile or dossier of a company that changed | `company-and-evidence-assessment` (this pack) |
| Evidence maturity over time | `evidence-maturity-monitoring` (this pack) |
| Funding signals, comparing 2 to 12 companies | `funding-and-portfolio-comparison` (this pack) |
| Holdings in a portfolio over time | `investment-portfolio-monitoring` (this pack) |
| Investment memo and decision record | `investment-memo-and-decision-record` (this pack) |
| Whether a thesis or memo still holds after a change | `thesis-and-memo-monitoring` (this pack) |
| Regulatory status analysis, pathway, whether a change needs a submission | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Reimbursement and coverage changes | `dh-access-and-value` coverage-pathway-and-access-strategy |
| Competitor moves against one's own product's positioning | `dh-go-to-market` market-segmentation-and-gtm-strategy |
| Partner design for one's own product | `dh-go-to-market` channel-and-partner-design |
| Literature review method | `dh-clinical-development` literature-and-real-world-evidence-review |
| Health economics | `dh-access-and-value` economic-model-development |
| Whether a deal is reportable, notifiable or compliant | the owner the person names for legal or compliance questions |

Every route names the pack and the skill, never the pack alone.

## Sign-off

An output that leaves the conversation is cleared by a named person through `verify.build_record` (`cleared_by`). Without a name it is an uncleared draft and says so.

**Record line.** Every output and every refusal carries this record line as the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. The model and the tool are never the clearer.

## AI disclosure

Outputs stay identifiable as AI-assisted drafts. A pipeline review drafted here names the person who set the triggers, never the model.
