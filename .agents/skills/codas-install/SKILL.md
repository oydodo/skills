---
name: codas-install
description: Adopt Codas in a repository for the first time, or update its recorded Codas copies while preserving local edits and existing host integrations.
---

# Install or update Codas

Copy a fixed Codas version into a repository, take stock of its layers, and connect its checks.
Start with `codas-ontology` in a clean checkout of the source commit. Note entrypoints follow `codas-ontology`.

## Steps

1. **Fix inputs.** Target Git root, source repository and a full commit that exists (never a branch name).
   Needs Git, Node.js 24+ and network for `npx --yes tsx@4.21.0`. Look at the target's `codas.yml`,
   root AGENTS/CLAUDE, `.claude/skills` and pre-commit hook (`git rev-parse --git-path hooks/pre-commit`,
   any hook manager). Files already present without a source record are a collision: stop.
2. **Pick the Note branch.** A host Note system exists when lifecycle folders hold files whose first
   line starts `# Agent Note:`. Then keep its tree, rules, archive Skill, checks, hooks and CI, and
   record them in `codas.yml` `roots.Note` and `notes` with the host file and line that shows each;
   if a candidate is missing or not unique, ask the person. On update keep the branch already chosen.
3. **Copy** the table below at the source commit (`git show <commit>:<path>`) as is. Do not copy Codas's Intents, READMEs, AGENTS or Notes.
4. **Take stock of the layers** (Intent, root README/AGENTS, component READMEs, local AGENTS, Notes,
   checks). Empty repository: ask the person what the product is, for whom and why, draft the root
   README's Intent sections from `docs/templates/root-readme.md` for their decision, and list components without code in one proposed Note. Existing repository:
   find where the maintainer's accepted goals, principles and success standard live (an install
   guide is not one) and map each of the four uses (ontology §2) to where the host keeps it and list what is missing as
   gaps. The mapping is the host's documentation standard: extend the host's own if it has one;
   otherwise write `docs/AGENTS.md` on the model of Codas's, keeping its structure and writing
   rules and filling its tier table with the host's actual homes. Do not rewrite host files to
   Codas's defaults.
5. **Connect.** Default Note branch: add the hook line and CI workflow below. Both branches: the
   Claude link. Write `codas.yml` with `source` (repository, commit) and any `roots` exceptions.
   Do not touch `package.json`, other workflows or unrelated settings.
6. **Check and hand off.** Run the Note checks and `git diff --check` (after `git add --intent-to-add`
   on new files); check copied links resolve. Give the person the new-session checklist; report what
   you checked apart from what only that session can verify.

## Copy table

| Source | Destination | Host Note system |
|---|---|---|
| `docs/ontology/ONTOLOGY.md` | same | copy |
| `docs/templates/**` | same | copy |
| `docs/notes/AGENTS.md`, `docs/notes/{implemented,archived}/AGENTS.md` | same | skip |
| root `AGENTS.md` managed block | root `AGENTS.md` managed block | copy |
| `src/codas/agent/skills/<dir>/**` for each dir with `SKILL.md` (not `AGENTS.md`) | `.agents/skills/codas-<dir>/**` | skip note-archive |
| `src/codas/agent/hooks/notes/{agent-note-tree.ts,archived-agent-notes.ts,verify-agent-note-format.ts,verify-agent-note-classification.ts,verify-archived-agent-notes.ts,LICENSE,pre-commit}` | `.agents/codas/hooks/` (keep exec mode) | skip |
| `src/codas/agent/hooks/codas-notes.yml` | `.github/workflows/codas-notes.yml` | skip |

**Root AGENTS.** Replace only the `<!-- CODAS:START -->`…`<!-- CODAS:END -->` block, or append it;
bytes outside stay identical. Duplicate markers or an unexpected CLAUDE symlink: stop and ask.
Every other file is copied byte for byte.

**Root CLAUDE.** Do not create a `CLAUDE.md`: without one, Claude Code reads `AGENTS.md` itself and
loads each subdirectory's `AGENTS.md` when it works there. If the host already has a root `CLAUDE.md`,
make sure it brings in `AGENTS.md` (a link to it, or add the lines `<!-- CODAS:START -->`, `@AGENTS.md`,
`<!-- CODAS:END -->`), and report that subdirectory `AGENTS.md` files will not load automatically
while that file exists.

**Default Note branch local state.** Create `docs/notes/{proposed,implemented,rejected,archived}/`
and, if there is no manifest and no archived Note, `docs/notes/archived/manifest.json` with
`{"version":1,"files":{}}`. Never replace an existing manifest.

## `codas.yml`

The repository's only Codas configuration. It holds just what an agent or program must read and
cannot work out from the repository itself:

| Field | Meaning |
|---|---|
| `roots.Note` | Only for a host Note system: lists of globs for `proposed`, `implemented`, `rejected` and `archived`. Omitted means `docs/notes/<lifecycle>/**/*.md`. |
| `notes` | Only for a host Note system: its rules file `rules`, archive Skill `archiveSkill` and check commands `checks`. |
| `exclude` | Globs never read as repository knowledge, such as generated or third-party trees. |
| `source` | `repository` URL and full Codas `commit` of the copies. Advance it only after an update is complete. Codas itself omits it. |

`roots: {}` with no `notes` selects the Codas defaults. Where each use of knowledge lives is written
in the host's documentation standard, not here.

## Hooks, CI and link

Hook line (default branch), added once to Git's actual pre-commit hook, before any terminal `exit 0`:

```sh
sh "$(git rev-parse --show-toplevel)/.agents/codas/hooks/pre-commit" || exit $?
```

With a hook manager, register it there; never change `core.hooksPath`. Confirm a bad Note really
blocks a commit. The CI template goes to `.github/workflows/codas-notes.yml` unless that file holds
something else. `.claude/skills` is a symlink to `../.agents/skills`; an existing different one is a collision.

## Update

Rebuild old and new candidates from the old `source.commit` and the new commit with the same table.
A target file equal to its old candidate is replaced; anything else (changed, deleted, old source
unreadable) is kept and shown to the person with `git diff --no-index` old↔target, old↔new,
target↔new. A source file removed upstream is the person's call. Find existing wiring by looking
for it; do not add it twice. Advance `source.commit` only when nothing is left unresolved.

## New-session checklist for the person

In a fresh Agent session in the target:

1. Every copied file exists and matches the copy table at `source.commit`.
2. The Note checks run, and a deliberately malformed Note fails a commit in a scratch branch.
3. The `codas-*` Skills are discovered and `.claude/skills` resolves.
4. `codas-orient` on a code path reaches the Intent, the nearest README and AGENTS and the implemented
   Notes that link them; missing layers come out as gaps.

Adoption is not approval of the target's intent.
