# A1 Reimbursement status check

Framework task: DH-03.01.4.1, Part A, task A1. Catalogue job on the library: `reimbursement-matrix`.

## What this task delivers

A sourced, dated answer to "where is this product (or category) paid today, and what does that status actually mean", with every gap explained honestly and, where useful, the comparable products that are paid. It is the evidence base that coverage pathway mapping, access strategy, and any payer conversation build on.

Why it matters: a status word on its own misleads. "Listed" in Germany means the product is on the DiGA directory. "Recommended" by NICE means guidance, not funding. A CMS code pays for a service, not for a named product. A buyer who reads these as equivalent will make a wrong market call. Your value is the interpretation, not the lookup.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.4.1 Part A, Reimbursement status check |
| Workflow | The steps below |
| Knowledge | Library scheme records; `references/scheme-kinds.md`; `references/gap-rules.md` |
| Tools | `list_schemes`, `search_listings`, `find_scheme_precedents`, `get_market_matrix`, `get_reimbursement_status`, `get_status_history`, `retrieve_guidance`, `generate_report`; `verify.build_record` when a named person clears the output |
| Prompt | This guide |
| Template | `generate_report` (`memo`, `status`, `history`, `matrix`, `identity`) for the data; `assets/status-check-output.md` for the answer |
| Input | The request and its context: a product or category, optionally countries or schemes, optionally audience, depth and format |
| Governance | `references/governance.md` |

Tool names below use the library's names (`market-access-dh.search_listings`). Your assistant may show them with a prefix; they are the same tools. Arguments, return fields and known quirks are in `references/tools.md`.

## Before you start: read the request

Decide four things from the request and its context. Ask at most one clarifying question, and only if the product cannot be identified; otherwise state your assumption in the answer and proceed.

- **Product or category?** A named product ("somnio", "DiGA-ID 00508") runs the product path. A category ("insomnia apps", "remote patient monitoring") runs the category path.
- **Which countries or schemes?** Keep to the ones named. If none are named, check all schemes but show only the ones that answer the question.
- **Short or full?** "Quick", "overview", "in a line", "yes or no", or a one-line question gets the **short** output. "Memo", "for the board", "full picture", "detail", or a document to be shared gets the **full** output. When unsure, give the short output and offer the full one. Length is part of quality: a quick question answered with a page is a worse answer.
- **Is the real question about precedent?** "Can we cite this", "is there a precedent", "who else is paid for this" means the person needs comparable products, not just the one named. Run step 4.

## Workflow

### Step 1. Know what the library holds

Call `market-access-dh.list_schemes` (free). Keep, for each scheme: `pathway_kind`, `clock_rule`, `listing_count`, `last_load`, `posture` and `posture_reason`. Every later gap is judged against this: a missing product means something different in a scheme with 82 listings than in one with none.

### Step 2. Find the product, or the category's rows

**Product path.** Call `search_listings` with `query` set to the product name or identifier, plus `country` or `scheme` if named. Confirm identity from `manufacturer` and `decision_reference`. If two different products match, ask which, or show both. If nothing matches, try the manufacturer name and any identifier before concluding it is absent.

**Category path.** Search by what the rows actually hold, not by scheme code:
- To list one scheme's rows, call `find_scheme_precedents` with `scheme` (and `indication` to narrow). Searching `search_listings` with a scheme code as `query` returns nothing.
- To search across schemes, call `search_listings` with indication or product words ("insomnia", "remote", "asthma").
- Country codes: the United Kingdom is `UK`, not `GB`.
Group results by scheme. A category answer lists what was found; it never claims the list is complete.

### Step 3. Read status, and history where it matters

For one product, call `get_market_matrix` with `name` for every scheme at once, then `get_reimbursement_status` (`reference`, `scheme`) for each scheme where it appears. Call `get_status_history` when the status is provisional, conditional, delisted or withdrawn, or when the person asks how it got there. History often starts at the library's first snapshot: earlier transitions are a `[GAP]`, not "no change".

### Step 4. Find comparable paid products, when it helps

Run this when the product was not found in a scheme the person cares about, or when the question is about precedent. Call `find_scheme_precedents` on the relevant schemes with the product's indication (from its own record, or from the request). Report up to three comparable listed products per scheme with status, date and price as stated. Label them as comparables: they show a route exists for this kind of product, not that this product would qualify.

### Step 5. Interpret each status by kind of scheme

Open `references/scheme-kinds.md`. For each scheme in the answer, write one plain line on what the status means in that kind of scheme, and the clock or next event if the record states one. Code-based schemes need special care: the code is covered, not the product, so say who bills it and for what. Do not import rules from memory: if the reference does not state a rule, say the rule is not in the reference.

### Step 6. Classify every gap

Use `references/gap-rules.md`: not covered by the library; covered but the product is not in its copy; a field missing on a found record. In the short output, give one line per class, not one per scheme. If code execution is available, `scripts/classify_gaps.py` does this from the step 1 and step 3 outputs.

### Step 7. Guidance only if the records are silent

If the question is about a rule the records do not answer ("what evidence does PECAN need"), call `retrieve_guidance` once with a short query. Use a passage only if it carries a `source_url`. If nothing usable comes back, mark the rule `[GAP]` and name the authority to check; do not search repeatedly.

## Build the output

Follow `assets/status-check-output.md`, short or full as decided above. For a memo or document, call `generate_report` with `reference` and the matching `template`, then wrap it: the plain answer and the interpretation layer on top, and your classified gaps in place of its flat "checked, none loaded [GAP]" lines.

## Before you hand it over

- **Sources.** Every fact in the answer comes from a library record and carries its `source_url` and retrieval date. Say that the facts rest on the library's copy of the register and should be confirmed on the authority's page before external use. Do not send register facts to `verify.verify_text` or `verify.check_claim`: the Verify tools currently rate register pages as inadmissible, so they return "unverifiable" for every register fact and spend counted calls without adding assurance.
- **Sign-off.** If the output will leave the conversation, ask who will clear it and call `verify.build_record` with that person in `cleared_by`. If nobody is named, label the output an uncleared draft. The model never clears its own record.

## Boundaries

- Never say a product "is not reimbursed" because the library has no row. Say what the library holds and where to check.
- Never present a listing, a code, or a recommendation as evidence that the product works clinically.
- Never state a price as current or negotiated. Report the price the record states, with its retrieval date.
- Drugs, biologics and wellness apps are out of scope. Say so in two or three lines, name where the answer would come from, and stop without calling the library.
- European coverage in the library is partial. Say so whenever a European scheme is in the answer.

## When you are unsure

If a status word is ambiguous, quote `status_raw` in the source language beside your reading. If identity is uncertain, stop and ask rather than merge. If confidence in the overall answer is low, say what evidence is missing instead of filling it.
