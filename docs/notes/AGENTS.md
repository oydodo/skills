# AGENTS.md — Agent Notes

Agent Notes are effectively RFCs written by agents: durable proposals and decision records that preserve rationale, alternatives, consequences, and required verification. Follow the [documentation standard](../AGENTS.md) and the Agent Note rules below. The rules, the lifecycle instructions, the archive Skill and the Note checks are adopted under the MIT licence from [DeepSeek Harness `687f282e8625c6b8d11ff58211a90524be2e4317`](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/.agents/notes/README.md). Codas adapts only the paths, one Markdown file per Note, the Skill and command names, and the `## Approval` section; this file is the only source of Note policy.

**Every new Agent Note triggers a supersession check.** Search the active tree for older notes covering the same decision or mechanism, classify any full or partial supersession with `codas-note-archive`, and archive every qualifying implemented Markdown file in the same PR. Keep partial supersessions active and cross-linked.

Files under [`archived/`](archived/AGENTS.md) are frozen historical snapshots: never edit them or treat them as current authority.

One kind of design doc lives here. An **Agent Note** records a decision or proposal that affects this codebase — the *why* and *what we gave up*, the parts code and docs can't carry. This file defines where Agent Notes live, when to write one, and [the in-file format](#the-file-format).

## Layout and naming

Every Agent Note has two axes, both encoded in its **path** — `{lifecycle}/{class}/yyyy-mm-dd-topic-title.md`. A Note is one Markdown file in one language; there are no translated copies or consistency sidecars.

- **Lifecycle** (the top-level folder) is the Agent Note's status, and an Agent Note moves between folders as that status changes:
  - **`proposed/`** — proposals reviewed before implementation; not yet built (or only partly).
  - **`implemented/`** — the decision shipped. The file records what was decided and what was rejected, and is **kept current with what actually shipped**: when the code later moves a file, renames a package, or changes a key/default, the Agent Note is updated in the same change to match (facts only — paths, names, structure — not the decision itself). See [implemented/AGENTS.md](implemented/AGENTS.md).
  - **`rejected/`** — the proposal was considered and declined. Keep it only while its rationale prevents a tempting, meaningful mistake; otherwise delete the Markdown file.
- **Class** (the nested folder) is the *kind* of decision — see [Classification](#classification) below.

The date in the filename is when the topic was **first proposed** (per git history). Cross-references between Agent Notes use relative markdown links (`[topic](../../implemented/architecture/2026-…-….md)`) — never bare prose or numbers — so they are mechanically checkable and survive moves between folders.

The active lifecycle tree is the working inventory: browse its lifecycle/class folders or search the repository. Do not add a centralized `INDEX.md`: it duplicates path metadata and makes unrelated note changes contend on one generated file. Implemented records with historical decision value but little future guidance move to the separate frozen [`archived/`](archived/AGENTS.md) tree described below.

## Classification

Each Agent Note belongs to one path-encoded class from the table below. The Note checks read the table's first column, with each class name in backticks, and reject other folders. Adding a class requires updating this table.

| Class | What it covers |
|---|---|
| `feature` | A new user- or model-facing capability. |
| `bug-fix` | Corrects a defect or closes a gap a postmortem surfaced. |
| `simplification` | Removes code, behavior, or surface area without adding a capability. |
| `architecture` | A structural decision about the **shipped source** — how packages relate, what the runtime vocabulary is. |
| `process` | Tooling, policy, or workflow **around** the code — gates, the package manager, vendoring — not runtime behavior. |
| `testing` | Test infrastructure and strategy. |

The `architecture` / `process` line: **architecture** is about the source we ship; **process** is the surrounding tooling and workflow. (`refactor` is deliberately absent — it overlaps `simplification`, whose discriminator, "does observable behavior change?", already covers it.)

## Archiving and deletion

Delete an implemented Agent Note that only describes small UI adjustments or purely mechanical changes; delete its Markdown file and repair or remove inbound links. A local bug fix, performance change, new capability, or substantive behavior decision does not qualify merely because its implementation is small. Archive other implemented notes only when the shipped decision is complete, its rationale is unlikely to guide future work, and the record still has historical decision value. Keep it active when its alternatives, ownership boundary, negative guarantee, durable or wire semantics, security rule, or reintroduction condition remains useful. Never archive a proposed note: reject an obsolete proposal. Keep a rejected note only while it prevents a plausible mistake; otherwise delete its Markdown file. Use the calibrated `codas-note-archive` workflow rather than word count, age, or a target quota.

The archive is path-encoded as `archived/{class}/yyyy-mm-dd-topic-title.md`; `implemented` is deliberately absent because only implemented notes can enter it. An archival change moves the Markdown file, retains `Status: implemented`, inserts `Archived: YYYY-MM-DD` immediately below that status, and repairs or deletes inbound links. These are the only permitted content changes during archival. Existing title punctuation and blank-line layout do not block archival; preserve them with the body.

Once sealed, every archived Markdown file is permanently frozen. Do not edit, translate, reformat, update, move, or delete it, and do not treat it as authority for current behavior. Documentation gates skip archived sources, including their outbound links; active prose may still link into an archived note when it intentionally cites history. The archive Note check enforces the closed class tree, single Markdown artifacts, archive metadata, and the append-only frozen-content manifest, except for the exact seal transitions documented in [archive instructions](archived/AGENTS.md). The [archive-policy Agent Note](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/.agents/notes/implemented/process/2026-07-26-frozen-agent-note-archive.md) owns the rationale.

## When to write one

Add or update an Agent Note in the same PR only for lasting decision rationale that code, tests, and existing documentation do not explain. A proposal for substantial future work starts in `proposed/`; a decision already made starts in `implemented/`. Pick the class folder that matches the decision (see [Classification](#classification)).

Updating the Agent Note that already owns the decision satisfies the rule; do not create a duplicate. Mechanical or local edits, including local UI presentation and interaction changes, are exempt. An Agent Note is never edited into a *different decision*: supersede it with a new one, and keep both notes cross-linked unless the old note is later fully consolidated under the rule below. Editing an `implemented/` Agent Note to track where its existing decision lives is required, not forbidden; see [implemented/AGENTS.md](implemented/AGENTS.md).

An implemented Agent Note that is fully superseded may be consolidated into the current owning note and deleted. Before deletion, the owner must preserve every unique rationale, alternative, consequence, required verification, and named coverage gap; and repair every inbound link. Partial supersession does not qualify: keep both notes cross-linked and update every fact that remains current. Consolidation must not rewrite the old file into its opposite or rely on git history as the only copy of rationale.

A feature-addition note may be consolidated into the later removal note only when the feature is absent from production code, configuration, schemas, durable or wire formats, migration, and compatibility behavior; no current documentation presents it as available; and no test exercises it as supported behavior. Removal rationale and tests that verify absence may remain. The removal owner preserves the original motivation, why it no longer justified the feature, alternatives to full removal, the capability given up, conditions for reintroduction, and verification of complete absence. Obsolete implementation inventories and tests that only verified the deleted behavior are not current verification evidence. Removing one transport, default, implementation, or presentation is partial supersession, as is any surviving durable data or compatibility handling.

## The file format

Every active Agent Note follows one in-file format, enforced by the format Note check; the rationale for the format — and the alternatives it rejected — is [archived the uniform-format Agent Note](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/.agents/notes/archived/process/2026-07-05-uniform-agent-note-format.md). Archived notes retain the format they had when sealed plus the archive-date line above.

### The header block

The first three lines of every Agent Note are exactly:

```markdown
# Agent Note: <title>

Status: <status>
```

followed by a blank line. The `Status:` value is one of three forms, and must agree with the lifecycle folder the file sits in — the gate cross-checks them:

- `Status: proposed`
- `Status: implemented`
- `Status: rejected — <why, in one line>`

The status carries no dates and no parentheticals: the filename holds the first-proposed date, git holds everything else, and an "accepted in amended form" note is body content (state the amendment where the decision is stated). The rejection reason is the one status with content, because a rejected Agent Note's verdict is the fact readers come for.

### The body skeleton

Every Agent Note opens its body with `## Problem` — the motivation, written to stand without the solution. What follows depends on the lifecycle; recurring sections use these canonical names and nothing else, while genuinely bespoke technical sections (package topology, wire contracts, schemas) remain free-form between the required ones.

#### `proposed/`

```markdown
## Problem
## Proposal
## Approval          (only once the person has approved)
…bespoke sections…
## Alternatives considered
## Acceptance criteria
## Risks
```

`## Proposal` is the intended change and may legitimately speak in the future tense — plans, migration steps, and open questions belong here while the work is unbuilt. `## Acceptance criteria` says what observable state means done. `## Risks` covers both what could go wrong and what the change knowingly gives up.

`## Approval` records the person's decision on the proposal, so its state is read in the Note rather than in a pull request: one line with the date, who approved, and their words or the option they chose, plus what was amended if they approved a changed version. Only the person's decision moves a proposed Note to `implemented/`; an agent never infers it from silence, passing checks, or a merged change.

#### `implemented/`

```markdown
## Problem
## Decision
…bespoke sections…
## Alternatives considered
## Consequences
```

`## Decision` describes shipped reality in the present tense, and the whole file is kept current with it per [implemented/AGENTS.md](implemented/AGENTS.md). `## Consequences` records what the trade-off cost **and** bought. Proposal-era headings are spec-speak here and the gate rejects them: `## Proposal`, `## Plan`, `## Migration plan`, and `## Acceptance criteria` may not appear in an implemented Agent Note (the [slop checklist](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/docs/AGENTS.md) names why). A `## Testing`, `## Deferred`, or `## Related` section is fine where it states present-tense fact.

#### `rejected/`

A rejected Agent Note is the proposal, frozen: it keeps whatever proposal-time sections it had (including `## Acceptance criteria` or `## Plan`), and the verdict lives on the `Status:` line. Only the header block, the `## Problem` opener, a `## Proposal` section, and the Alternatives-considered mandate below apply.

### Alternatives considered — mandatory

Every Agent Note carries an `## Alternatives considered` section: each genuine alternative and why it lost, one bold-led paragraph per alternative or a `### Why not <X>?` subsection per contested one. A decision recorded without what it beat invites re-litigation — the failure Agent Notes exist to prevent.

Alternatives are recorded, never invented. An Agent Note dated before 2026-07-05 whose alternatives are not reconstructible from the record carries this exact comment in place of the section, which the gate accepts for pre-format files only:

```markdown
<!-- agent-note-format: alternatives-not-recorded (pre-format Agent Note) -->
```

### Moving between lifecycles

Moving a file between lifecycle folders means updating the `Status:` line and re-satisfying that folder's skeleton in the same change — the gate fails the move otherwise. Concretely, `proposed/` → `implemented/` rewrites `## Proposal` into a present-tense `## Decision`, folds `## Approval` into the Decision's source sentence, folds `## Acceptance criteria` and `## Risks` into `## Consequences` (or a present-tense `## Testing`/`## Verification` section for what now pins the behavior), and drops plans in favor of what shipped — the rewrite [implemented/AGENTS.md](implemented/AGENTS.md) requires, made mechanical. `proposed/` → `rejected/` only adds the reason to the `Status:` line and freezes the file.
