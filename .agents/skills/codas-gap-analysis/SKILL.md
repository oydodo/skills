---
name: codas-gap-analysis
description: Turn a batch of problems found in a Codas-governed repository (from a trial, review or discussion) into gaps, their essence, and annotated changes on real ontology nodes laid out by their actual links, drawn as one diagram for the person to approve.
---

# Codas Gap Analysis

Work content: analyse problems and present the changes they need. It does not edit files; the approved change list goes to `codas-propose` or `codas-model`.

Start with `codas-ontology`.

1. Gaps. Write each problem as one observed gap in one sentence. A whole layer missing (no Intent, no component READMEs, no Note tree, no checks) is a gap of its own. Do not retell the conversation or say who said what. Merge duplicates.
2. Essence. For each gap ask why until the answer is no longer specific to that gap. Then check whether it holds for every use; if it does, the fix is a general rule, not a patch for the type at hand.
3. Nodes. Point each fix at the real files it changes: file path and the use it serves (Intent, guidance, reference, Note), found through directories and links (`codas-orient`). List each new decision as a Note node and the files whose text it changes. A fix that reaches no node says why (a working method, or parked).
4. Annotations. Under each node list what changes, each line tagged with the gaps it comes from.
5. Centre. The node most gaps point at is the centre of the change; review it first and say what depends on it.
6. Status. Give each gap one status: done, awaiting approval, needs research, or parked.
7. Diagram. Draw one page: gaps with their essence, and the nodes laid out by their actual links (directory nesting as nesting, links as edges), each read from the repository files at the selected snapshot. Put sources and unverified facts under the diagram.
8. Approval. The node list is the change list. Ask the person to approve the whole list; silence or approval of one point is not approval. Hand the approved list to `codas-propose` or `codas-model`.

Stop when an essence is still "this file lacks a sentence", or a fix reaches no node and no reason is given.
