# Codas Software Engineering Ontology

> **Version:** v0.2.2. Decision history is in Git and the Notes.
> **Scope:** The shared language for a repository's knowledge. No repository-specific objects.

## 1. Purpose

Codas helps maintainers and coding agents find what counts as good, how to work, what the system is and why it was decided, before they change software. This ontology is the small shared language that keeps those four apart, so one sentence is not read four ways. It does not replace Git, code, tests, code analysis, task trackers or agent workflow engines.

Structure emerges from a few elements acting on each other, not from more and narrower rules. An element, link, check or rule is added only when real work broke or stalled without it, and says what it replaces; a problem becomes a rule only after it recurs in review. When a rule keeps narrowing and gaining conditions, the view that produced it is wrong: find that view and rewrite what it produced, one sentence or the whole document, instead of patching the sentence that failed. Only what can be decided mechanically becomes a check, and a passing check is not approval.

## 2. Four uses of knowledge

Every sentence of repository knowledge answers one of four questions. The use of the sentence decides where it belongs; the file it happens to sit in does not.

| Use | Question | Who decides | Kept true by |
|---|---|---|---|
| **Intent** | What counts as good? | The person; an agent may draft, and a draft has no effect until the person confirms it | The person's revisions |
| **Guidance** | How do we work here? | The person, through review of the change | The change that alters the way of working |
| **Reference** | What is the system now? | Whoever changes the system | The same change as the code it describes |
| **Note** | Why was it decided then? | The person approves; the Note rules govern its lifecycle | Written once; an implemented Note's facts follow the Note rules |

Where each use lives is the repository's own choice, written in its documentation standard; this ontology names no paths.

A directory's front page (by convention its README) is the first document a reader meets there. The repository root's front page carries the repository's Intent in the sections the documentation standard names; the rest of it, and every other directory's front page, is reference for what that part is and what it promises the whole.

Code, tests and CI configuration are not a fifth use. They are the primary evidence of what the system is; a reference describes and links them and does not copy them.

**A sentence in the wrong home is misplaced, not a new kind.** A work rule in a README, a current fact in an Intent, or a quote and its date in a formal document is moved to the home of its use and linked from where it was. No type is added and no rule is written to tolerate it.

**Intent is the standard, not a description.** It says what the system should achieve, which ideas carry its design, what a good structure is and what the current stage is for; every Intent sentence should be able to judge a change as going with it or against it. A description of how the system works today is a reference.

**A Note is history.** It keeps the problem, the decision, the alternatives and the cost as they stood. Current text may state the same decision in its own words; that is not a second source, because the current text is what holds and the Note is why.

## 3. Reading links

A link's meaning comes from the uses at its two ends.

| Source → target | Meaning |
|---|---|
| Any document → Note | The rationale for the linking sentence is in that Note |
| Note → any document | The Note explains why that document says what it says |
| Reference → reference | The source is part of, or works with, the target |
| Any document → Intent | The source serves that standard |
| Note → Note | Stated beside the link in one sentence: supersedes, partly supersedes, or related |

A link is a pointer. It does not prove consistency, approval, implementation or test success. No document keeps a list of the Notes about it, and no document has to be linked to anything; which documents point at an object is found by searching.

## 4. What holds, and drift

What holds now is the current text of the selected main baseline: its Intents, guidance and references. A proposed Note is a candidate with no effect. Implemented, rejected and archived Notes are history.

**Drift** is a mismatch under the same condition: what should hold differs from what actually holds, or two current statements conflict. A Note that differs from current text is not drift by itself, and neither is an Intent not yet reached. Drift is reported to the person with both sides; an agent does not settle it alone.

## 5. Unknowns

Not found is not the same as absent. An agent states what it searched and reports the rest as unknown; it does not fill a gap by guessing.

## 6. Parts and the whole

When a change touches a part, the promise of the whole it belongs to is part of the review: the front page of the enclosing directory, or the cross-directory reference that names it. That promise is checked, not copied onto the part.
