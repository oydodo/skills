---
name: codas-model
description: Model a new concept or locate an unmodeled product responsibility in a Codas-governed repository before implementation - start from its essence, then find its place and write its documents. Not for revising existing documents or drafting decisions on them; use codas-propose.
---

# Codas Model

Start with `codas-ontology`. The order is essence, place, decisions, documents, code; do not skip.

1. **Essence.** State in one sentence what problem the new thing solves, from the person's words and
   the Intents; mark your own judgment. Locate only after the person confirms it. Every later
   conclusion must follow from it; if it changes, recheck them. The sentence opens the document.
2. **Place.** Part of an existing responsibility, a new part beside or below one, or a property of
   something existing. Extend what exists when it is enough. A part earns its own directory and
   README when it hides a design decision likely to change on its own; say why the other places do
   not fit. Do not decide by names or directory similarity.
3. **Decisions** go with the whole they govern: one that concerns only a part goes with the part;
   the whole's promise and how its parts work together go with the whole.
4. **Before code exists,** list the new part in a proposed Note; its README is written in the change
   that adds its code. Tasks and milestones stay outside Codas.
5. Return: the essence and the person's confirming
   words, the place and why not elsewhere, the Notes, the files written or to write, what to build,
   and the open questions.
