Input:    intake items 6 and 7
Atom:     extract-requirements-from-source (rows: facility, role, inspection source and date, observations, status)
Tool:     none
Template: none
Output:   risk rows of category manufacturing, inspection, data_integrity, compliance
Check:    inspection classifications NAI, VAI and OAI are read with the limits of the public database (it cannot count all inspections; pre-approval inspections are not included: VP-D-060 to VP-D-063); data-integrity expectations VP-D-070, VP-D-071; manufacturing and inspection rows name the facility and the inspection source (or GAP); a contract site with no history is a gap; comparability data requested if the process changed (RL-02). Rule: inspection databases are leads; read the document before relying on it
Human:    the named regulatory reviewer (counsel for legal rows) reviews the output
