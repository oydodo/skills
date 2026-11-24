---
name: crux-first-writing
description: "Write or revise prose that says what something is: a definition, a glossary or ontology entry, a README front page, a documentation section, a decision record body, a code comment. Start from the object's essence, state it positively, and derive the text from it. Apply on every revision too, including a one-sentence fix after review feedback. Use crux-first-reasoning first when what is true or central is still open; use technical-documentation, technical-writing or technical-language afterwards for form and wording. Skip chat replies, status reports, translations, and change records such as changelogs, release notes and migration guides."
---

# Crux-First Writing

**Goal:** A text about an object tells the reader what the object is now, so the reader can use it correctly. Every sentence follows from the object's essence, in the same way that `crux-first-reasoning` organizes an answer around the dominant tension.

## Method

1. **Find the essence before writing.** Place the object in the whole it belongs to. Ask what it connects or contains, what role it plays there, and what gives it its own nature among its neighbours. In terms of contradiction, the essence is the principal aspect of the contradiction that governs the object. For example, a link carries the relation between the objects at its two ends, plus its own sentence about these two instances. The essence is found when it fits in one positive sentence; until then, settle it with `crux-first-reasoning`, the code, or the person.
2. **Open with the essence, then unfold it.** The following sentences give its parts, behaviour, guarantees and use. A sentence that does not follow from the essence shows one of two things. Either the essence is incomplete, so return to step 1, or the sentence belongs to another object, so move it there.
3. **Test each sentence: does it state a property the object has now?** A sentence that passes stays, and takes the positive form where one exists ("merged after checks pass"). A real guarantee stays even when only a negative form fits. A sentence about a rejected alternative, an earlier version, or what other things do goes to the record that holds history, such as a decision record or changelog, or is deleted. The test reads what a sentence means, so it also catches farewells written in the present tense ("is not stored", "no document keeps a list").
4. **Revise from the essence.** Feedback on one sentence usually exposes a wrong or missing view of the whole. Restate the essence, reread the whole passage it governs, and rewrite what the old view produced. A text patched sentence by sentence becomes a diff of its past versions.

## Working with other Skills

- `crux-first-reasoning` and `independent-judgment` decide what is true and what is central. This Skill writes from their settled result.
- `technical-documentation` (document type and facts), `technical-writing` (Chinese tone), `technical-language` (English wording) and `writing-for-agents` (agent-facing instructions) shape how the text reads. They keep the essence and the order set here. When `technical-documentation` asks for contractions, apply them to the negations that remain after step 3.
- A host repository's own prose standard governs where it is stricter or more specific.

## Boundaries

- Change records narrate change by purpose; step 3 sends history to them, and their own writing follows their purpose.
- Match depth to the text. A one-line comment needs one true sentence.

For evaluation cases, see `references/evaluation.md`.
