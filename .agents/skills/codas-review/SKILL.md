---
name: codas-review
description: Review a change in a Codas-governed repository against the current intent and report evidence-backed findings without modifying it.
---

# Codas Review

Start with `codas-ontology`.

1. Fix what is reviewed (commit or diff) and the baseline M.
2. Look up the intent for every touched path (`codas-orient`).
3. Check the change against it: the Intent sentence it serves, what holds for the touched parts, the
   whole's promise, the parts that use them, whether README and AGENTS were kept true in the same
   commit, and whether a new responsibility should first become its own part. Reproduce claims where
   possible.
4. Report findings by impact, each with file:line, evidence and the smallest fix; separate fact,
   judgment and unknown; or say "no findings" and the scope reviewed. Passing checks are not
   meaning, and not found is not fine. Do not edit; the owner decides. A rule problem found on the
   way becomes a proposal.
