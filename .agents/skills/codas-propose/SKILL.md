---
name: codas-propose
description: Propose a change to intent in a Codas-governed repository - migrate missing intent on demand, draft or revise documents and Notes, and write the decisions as Notes for the person's decision. Not for placing a new concept that has no document yet; use codas-model.
---

# Codas Propose

Start with `codas-ontology`; a new concept goes through `codas-model` first.

1. Start from baseline M and the lookup result (`codas-orient`).
2. Before drafting any change, including one the person asked for as a correction, answer:
   - Purpose: which Intent sentence it serves, read for what that sentence means, not its wording.
     Nothing backs it: report "没有本体背书".
   - Place: which use this meaning serves and so where it lives (what counts as good in an Intent,
     how to work in AGENTS or a Skill, what it is now in a README, why in a Note). Change it there,
     not where the problem showed up.
   - Whole: after the change, does that document still read as one understandable whole, and what in
     it is now redundant? A change that only adds a qualifier, field, rule, step or file means the
     real error is not found yet; add a form only for a named piece of work that failed without it,
     otherwise report "没有出错案例".
   A correction means an earlier answer was wrong: answer the three again from the start.
3. Draft the smallest change. Mark the basis of each part: the person's words, a Note or the
   ontology; anything else is your judgment and says so. Before a new Note, check for one on the same
   decision (Note rules file). A judgment the person has not confirmed is only a proposed Note; never
   silently rewrite another Note's decision.
4. Commit on top of M and open a pull request with the diff and open questions. The person decides;
   the change takes effect only on their explicit yes.
