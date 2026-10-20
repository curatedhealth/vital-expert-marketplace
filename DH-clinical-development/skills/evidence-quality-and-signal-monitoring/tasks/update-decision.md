# B1 Update decision

Framework task: DH-01.02.4.2, Part B, task B1. Replaces the old *digital evidence pass rule* and *digital evidence miss owner* sections, which are now Steps 3 and 5.

## What this task delivers

A decision frame for the person: rely on the review as it is, update it, rerun it under the target body's rules, or move it to a living review. It sets the three Cochrane questions (still relevant, done well enough, anything new) against the facts from A1 and A2, applies the person's pass rule in their words, names the owner of each open item as the person names them, and lists what an update would need. It answers "what do we do about this evidence, and who owns it?"

Why it matters: Cochrane puts relevance and quality before new studies when deciding to update (ES-103); an EU JCA dossier cannot lean on an old search date (ES-168); and an update has its own reporting and retraction duties (ES-21, ES-119, ES-120).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI/ML Governance Director (`ai-ml-governance-director`) |
| Skill | DH-01.02.4.2 Part B, Update decision |
| Workflow | The steps below |
| Knowledge | `references/currency-rules.md` sections 1, 3 and 4; `references/review-and-data-quality.md` section 1; ES-21, ES-101 to ES-104, ES-107, ES-119, ES-120, ES-133, ES-152, ES-156, ES-168 to ES-170 |
| Tool | A1 and A2 outputs; `verify.qualify_source` then `verify.check_claim` for any finding the decision rests on; `verify.build_record` on release |
| Prompt | This guide |
| Template | `assets/update-decision-output.md` |
| Input | A1 and A2 results, the decision the evidence serves and its date, the person's pass rule, owners, and resources only as the person states them |
| Governance | `references/governance.md`; the decision is the person's |
| Catalogue job | none (an update search runs through the sibling skill; its B1 names `evidence-table`) |

## Read the request

- **Purpose and body.** Publication, JCA, NICE, IQWiG, internal. It decides which options are open (a JCA needs its own retrieval cut at most 3 months before submission; NICE HealthTech allows existing reviews to be used or updated, ES-133).
- **Pass rule.** What evidence the person needs for their decision, in their words. If none is given: "pass rule not given `[GAP]`"; never write one.
- **Owners.** As the person names them. "Owner not named" otherwise.
- **If A1 or A2 has not been run,** run what is needed first or say which facts are missing.

## Workflow

### Step 1. The three questions (ES-103)

| Question | Facts from A1 and A2 | Person's answer |
|---|---|---|
| Is the question still relevant to the decision? | The decision and PICO as the person states them | |
| Was the review done well enough to keep? | A2: critical domains with passages; the appraisers' overall confidence (ES-107) | |
| Is there anything new? | A1: candidate new studies after the last search, retractions or corrections, superseded methods | |

A review rated "critically low" by the appraisers "should not be relied on" (ES-107); say so as the rule, attributed.

### Step 2. Options with what each needs

| Option | When it fits (rows) | What it needs |
|---|---|---|
| Rely as is | Relevant, adequate quality, no material new evidence, and the body's date rule is met | A note of the checks done and their dates |
| Update | Relevant and adequate, with new studies or methods (ES-103); NICE HealthTech allows use or update of existing reviews (ES-133) | Rerun searches for all sources; screen; re-check retractions of included studies (ES-119, ES-120); report the previous version's study count (ES-21) |
| Rerun under the body's rules | The body's rules differ from the review's (for example JCA databases, cut-off, RoB 1 with its seven domains, AI disclosure; ES-151 to ES-168, ES-171; RoB 2 remains Cochrane's current tool, ES-69) | A new protocol and search through the sibling skill's A1 |
| Living review | High-importance question with frequent new evidence (ES-104) | A standing search and screening process with owners |

Label any recommendation "proposed". The choice is the person's.

### Step 3. The person's pass rule

Write it in their words. Set the facts against it: "meets the person's rule", "does not", or "cannot tell: GAP", one line per element of the rule.

### Step 4. Check any finding the decision rests on

If the decision cites a review finding (for example an effect size), get the results passage with its locator, run `verify.qualify_source(doi=...)` then `verify.check_claim(claim, passage{text, locator}, source)`, and accept it only if the passage states it in the same direction (register N3). Record the tool status beside your reading.

### Step 5. Owners for every open item

One line per open item (date rule not met, critical domain without evidence, candidate studies to screen, retraction to examine, AI-use disclosure) with the owner the person named, in their words, or "owner not named". Never suggest a job title.

### Step 6. AI-use and record

If the evidence feeds an EU JCA, add the AI-use table for any AI-assisted step of the check or the update, with the named human responsible (ES-169, ES-170). If the output leaves the conversation, call `verify.build_record(clearances=[{"cleared_by": {"name": "<person named>"}}], ...)`; otherwise label it an uncleared draft.

## Build the output

Follow `assets/update-decision-output.md`. Answer first: the three questions with their facts, the options open for this purpose, the person's rule applied, and the one decision they must make. No timing pressure: the date rules are facts about the review.

## Before you hand it over

- The decision is framed, not made; any recommendation is labeled "proposed".
- The pass rule and owners are the person's words or marked missing.
- Every finding the decision rests on has a passage read in the same direction.
- Record line present in every answer, refusals included: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft."

## Boundaries

- Running the update or rerun is the sibling skill's (`literature-and-real-world-evidence-review`).
- Notifying a body about a retraction or withdrawing evidence from a filed dossier stops for the owner the person names (in their words; if none, "owner not named" and ask).
- Economic consequences belong to dh-access-and-value; payer routes, submissions and prices to dh-access-and-value; marketing claims to dh-go-to-market; device status to dh-regulatory-and-quality.
