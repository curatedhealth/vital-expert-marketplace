# Output format: threat model and security architecture

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/secdesign_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, boundaries 60, threats 140, SBOM 80, gaps 50, record 50.

1. **Answer** (two or three sentences): hops and threats counted; covered, accepted and open by hop; the SBOM facts that most affect release (past end of support on the read date, KEV entries in your export); what is missing for the FDA views. No score, no acceptance.
2. **Boundaries:** the hops that cross a network, tenant or privilege level, and which are third party.
3. **Open and accepted threats:** Id · Hop · Actor · Asset · Control category or acceptance (acceptor, reopen condition) · Flags · Rows. Threats the model added are labeled "proposed".
4. **SBOM facts:** components past end of support, before your support horizon (if given), missing level of support or end-of-support date, in your KEV export; computed by the script on your file and read date.
5. **Gaps:** FDA views, testing evidence, design version, each with its row.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Threat model draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Components and trust boundaries (design version, read date)
### Mapping to the FDA architecture views (EN-056)
| View | Hops it covers | Have it | Rows |
|---|---|---|---|
### Threat register
| Id | Hop | Actor | Asset | Threat (at the level FDA and NIST name it) | Control (FDA category) or acceptance | Acceptor | Reopen condition | Flags | Rows |
|---|---|---|---|---|---|---|---|---|---|
### Counts by hop (script output)
### SBOM check (script output, read date, support horizon yours or not given)
| Component | Version | Level of support | End of support | Flags | Rows |
|---|---|---|---|---|---|
### Testing and reports still to evidence (EN-058, EN-059)
### Framework mapping, if asked (CSF 2.0 or SSDF; any Tier "proposed")
### Proposals (labeled "proposed")
### Gaps
### For you to decide (scores, acceptance, release)
### Calls made
### One line offering anything not shown
### Record (the very last line)
Threat model draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
