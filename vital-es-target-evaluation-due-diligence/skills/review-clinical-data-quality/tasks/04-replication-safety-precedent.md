Input:    rows, literature and registry results
Atom:     classify-text-labels (replication labels: replicated / not replicated / single study / not applicable / GAP; closed set, evidence span required)
Tool:     literature_search_literature, literature_check_retraction, literature_grade_evidence; FDA surrogate table (references/regulatory-precedent.md)
Template: none
Output:   replication_status, safety_signals, regulatory_precedent.US and .EU per row; for a single-arm or externally controlled row also sat_prespecified, effect_isolation and external_control
Check:    a single-arm or externally controlled row states whether protocol, control data and analysis plan were fixed before the trial and whether the endpoint isolates the treatment effect (EMA reflection paper VP-A-111 to VP-A-114; FDA draft guidance VP-A-101, VP-A-104), and says that a result outside a randomized comparison needs much stronger evidence (ICH E10, VP-A-120 to VP-A-122) without stating a number. EU precedent says "no EU surrogate table exists" or cites a qualification opinion; US states whether the endpoint is on the table. Rule: a retracted or expression-of-concern record is flagged and removed from support; the register never says an endpoint is accepted by a regulator without the table row or review document
Human:    the clinical development reviewer checks replication labels and precedent statements
