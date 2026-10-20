# Governance

Source: the stop rules of the diligence pack (common, commercial, evidence and diligence briefs, 20 October 2026) and the rows cited, rewritten for screening work on the buyer's assistant. No worker is bound to this skill (the old files say "Worker: not bound"; the suite is not a CF-12 row).

## May proceed as drafts

Market screens, long lists, named-company record checks, short lists filtered and ranked on the person's own criteria and scores, and fact lists of deal and data rules for the owner the person names for legal questions. All are advisory drafts.

## The person decides

- The thesis, the segment and jurisdictions, the candidates on a long list.
- Criteria, pass rules, weights and 0 to 4 scores. The model never scores; if asked to propose scores, each is marked "proposed" with the fact behind it and is not ranked until the person confirms it.
- Which candidates go on the short list, and every investment decision.
- Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title.

## Stops for the owner the person names

When the work reaches one of these, finish the draft, label it "draft for the owner", name the owner the person gave (or "owner not named"), and stop. Refusals follow the same 450-word cap as short mode. A refusal (advice, valuation, a pass or invest call, investor or LP wording) always offers a facts-only draft for the owner, labeled "draft for the owner", with no recommendation.

- **Investment advice.** Any recommendation to invest, pass, bid or exit; any valuation, price, multiple or return. Never supplied, even as an example.
- **Market size and benchmarks.** No market size, valuation multiple, return benchmark or sector funding total exists in the sources; never supply one.
- **Deal and data rules.** Whether a deal is reportable under HSR, a covered transaction under CFIUS, a covered data transaction under the DOJ rule, subject to EU or Swiss screening, or compliant with HIPAA or GDPR is for the owner the person names for legal or compliance questions. The model flags the rows with dates (`deal-and-data-flags.md`) and never says a deal is clear.
- **Regulatory status.** Whether a company's product is a device, its class or pathway: `dh-regulatory-and-quality` regulatory-pathway-and-classification. This skill quotes the register record only.
- **External wording** for a target, a counterparty, an investment committee outside the conversation, a regulator or the public.

## Never

- Infer revenue, runway, valuation, investors, outcomes, ownership or intent from a record or a filing.
- Call a 510(k) or a registration "approval" (DL-126 to DL-128), or a DiGA listing evidence of clinical effect.
- Present the library's evidence maturity score as a rating of a product or a company, or rank targets by it unless the person sets it as their criterion.
- Mix the person's confidential data-room material into a public-record statement; say which facts came from the person.
- Supply a date, threshold or status the person did not give; write "not given" and ask.
- Carry facts from an earlier request into this one; use only the inputs of the current request.
- Judge a record's relevance to the person's thesis; quote it with its date and leave the reading to them.
- Infer a company's status (active, bankrupt, insolvent, delisted, deregistered, acquired) from press, memory, a quiet record or a missing filing. Status comes from the company's own primary filings or register entry (`screening-rules.md` section 5); otherwise "Status: [GAP]: not read" with the filings to open. Form 15 or Form 25 is not dissolution (DL-144, DL-149).
- Send the person's email address or name in a request to an outside site, or invent a contact. SEC asks for a declared User-Agent contact (DL-153 [WF]): ask which contact the person's organization uses, or list the filings to open.
- Print 0, "none" or a country for a field the record lacks; write "not in the record".

## Routing table

| Question | Route (pack and skill) |
|---|---|
| The company's own product portfolio (own products and programs), strategy options, execution against objectives, horizon scanning (investment portfolio questions stay in the diligence skills) | `product-portfolio-prioritization`, `product-portfolio-review`, `strategic-vision-and-options`, `strategy-execution-monitoring`, `horizon-scanning-and-technology-evaluation`, `foresight-signal-monitoring` (this pack); start with `strategy-and-portfolio-capability-map` |
| Changes in a screened market or pipeline since a date | `pipeline-and-market-monitoring` (this pack) |
| Full company profile, dossier, evidence maturity of one company, guidance passages | `company-and-evidence-assessment` (this pack) |
| Evidence maturity over time | `evidence-maturity-monitoring` (this pack) |
| Funding signals, comparing 2 to 12 companies side by side | `funding-and-portfolio-comparison` (this pack) |
| A portfolio over time | `investment-portfolio-monitoring` (this pack) |
| Investment memo and decision record | `investment-memo-and-decision-record` (this pack) |
| Whether a thesis or memo still holds | `thesis-and-memo-monitoring` (this pack) |
| Regulatory status analysis, device class, pathway | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Reimbursement and coverage | `dh-access-and-value` coverage-pathway-and-access-strategy |
| Competitive positioning of one's own product | `dh-go-to-market` market-segmentation-and-gtm-strategy |
| Partner design for one's own product | `dh-go-to-market` channel-and-partner-design |
| Literature review method | `dh-clinical-development` literature-and-real-world-evidence-review |
| Health economics | `dh-access-and-value` economic-model-development |
| Whether a deal is reportable, notifiable or compliant | the owner the person names for legal or compliance questions |

Every route names the pack and the skill, never the pack alone.

## Sign-off

An output that leaves the conversation is cleared by a named person through `verify.build_record` (`cleared_by`). Without a name it is an uncleared draft and says so.

**Record line.** Every output and every refusal carries this record line as the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. The model and the tool are never the clearer.

## AI disclosure

Outputs stay identifiable as AI-assisted drafts. A short list drafted here names the person who scored it, never the model.
