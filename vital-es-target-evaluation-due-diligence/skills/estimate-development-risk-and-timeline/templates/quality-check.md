# Quality check (before human sign)

- [ ] Every claim-bearing row has a source, rule id, or `[CHECK]`/`[GAP]`
- [ ] Offline scripts in `references/tools.md` have been run (or marked not run)
- [ ] No human-only opinion issued by the agent
- [ ] Draft guidance labeled draft
- [ ] Register status UNSIGNED until reviewer.name + reviewer.date
- [ ] No invented PoS, HC discount, or multi-stratum multiply; BIO/Wong/Schuhmacher never averaged
- [ ] US PDUFA figures (B10) and EU EMA averages (B11) stay in separate keys — never merged
- [ ] SPIRIT (B12) used only as protocol-completeness / timeline narrative — never a PoS stratum
- [ ] EU approval probability still marked `[GAP]` unless a sourced stratum with matching denominator is cited
