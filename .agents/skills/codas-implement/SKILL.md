---
name: codas-implement
description: Change code in a Codas-governed repository under the current intent that applies to the touched paths, and keep code and its documents consistent.
---

# Codas Implement

Start with `codas-ontology`, then `codas-orient` for the paths.

1. Name the part being changed, what its README promises, and the promise of the whole it belongs to.
2. Make the change on a branch; review happens in the pull request.
3. If the change needs new intent, crosses the part's boundary, changes its interface or brings a new
   design decision to hide, stop and go through `codas-model` or `codas-propose` first. Never act
   against what holds.
4. Run the ordinary checks and tests for the touched code. Never fake a result; say what was not run.
   Do not merge before checks pass; deleting history needs the person's go-ahead.
5. In the same commit keep the README, AGENTS and reference pages that describe the change true; a new code directory gets its
   README. When code and documents disagree, report it and let the person choose which changes;
   do not rewrite the design from the code.
6. In the pull request, report which Intent it serves, which part it changes, the behaviour before
   and after, the checks and what they covered, mismatches and open questions.
