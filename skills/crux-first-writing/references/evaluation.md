# Behavior evaluation (manual A/B protocol)

This is a test plan, not evidence of model-level behavior. Run the same model and prompts with and without `crux-first-writing`, and compare the texts.

## Cases

### 1. A definition written as a list of negations
Source: `docs/ontology/ONTOLOGY.md` §4 in oydodo/codas, commit `ff956a0`.

Before:
> A link is a pointer. It does not prove consistency, approval, implementation or test success. No document keeps a list of the Notes about it, and no document has to be linked to anything; which documents point at an instance is found by searching. A link between two types that have no relation in §2, or whose sentence contradicts its relation, is reported.

Prompt: "Rewrite this section so it says what a link is."
Expected: The text opens with the essence and unfolds it, as in commit `bdbc117`:
> A link joins two instances whose object types are the two ends of a relation in §2, and its meaning has two parts. The relation's nature, stated once in §2, holds for every link between those two types. The link's sentence states what is particular to these two instances: that this Note supersedes that one, or that this Component depends on that one. Review checks that each changed link fits: its two types are the ends of a relation, and its sentence is a case of that relation's nature. The instances that point at a given one are found by searching.

The sentences about what a link does not prove are gone, because they describe rejected readings rather than the link.

### 2. One flagged sentence in a passage built on a wrong view
Prompt: Give a README section with four sentences that all guard against an older design, and a review comment on only one of them: "This sentence only says what it isn't."
Expected: The agent restates the essence of the section's subject and rewrites the whole section. A fix to the flagged sentence alone fails the case.

### 3. A real guarantee stays
Prompt: "Describe the merge step: a pull request is never merged before its checks pass."
Expected: The guarantee stays, preferably in positive form ("merged after its checks pass"). Deleting it fails the case.

### 4. A change record keeps its change narration
Prompt: "Write the changelog entry for moving the design contract out of CHANGELOG.md into AGENTS.md."
Expected: The entry says what moved, from where, and why. The Skill should not strip "moved" or "removed" from a change record.

### 5. Simple task
Prompt: "Translate 'rollback plan' into Chinese."
Expected: A direct translation, with no essence analysis.
