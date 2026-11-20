---
name: codegraph
description: "Use the open-source colbymchenry/CodeGraph CLI or MCP to investigate accessible local repositories: cross-file calls, implementation paths, callers/callees, dependency and refactor impact, and affected tests. For graph-worthy tasks, automatically initialize a missing local index or refresh a stale one when the CLI and repository writes are available. Do not force CodeGraph on small edits or install tooling without approval; fall back to ordinary repository inspection when graph access is unavailable."
---

# CodeGraph — Repository graph navigation

**Purpose:** Find the smallest code context that explains cross-file behavior or change impact. This is a maintained Skill adapter for the MIT-licensed [colbymchenry/CodeGraph](https://github.com/colbymchenry/codegraph). It does **not** bundle the executable, install MCP servers, or grant access to a user's machine.

## Workflow

1. **Scope the task.** Identify the exact local repository/worktree and the question. Use CodeGraph for cross-file paths, symbol relationships, blast radius, affected tests, and nontrivial debugging/refactoring. Skip it for a tiny edit, a known-file read, or straightforward grep. Do not index repositories outside the task.
2. **Check access.** Prefer an available `codegraph_explore` MCP tool for graph queries. If the local shell can access the same repository, check for the `codegraph` CLI (`command -v codegraph` on POSIX) and inspect `codegraph status <repo-root>`. Respect `CODEGRAPH_DIR` and platform-specific index locations; the existence of `.codegraph/` alone is not a reliable readiness test. An unavailable CLI/tool or inaccessible repository is **nonblocking**.
3. **Ensure a usable graph, only when the task needs one.**
   - **Missing index:** If `status` clearly reports an uninitialized repository and the CLI can write to the selected worktree, run `codegraph init <repo-root> --yes` once, then confirm with `codegraph status <repo-root>`. This is automatic per-project indexing, **not** automatic CLI/MCP installation. If status fails for an unknown reason, do not mistake it for a missing index.
   - **Existing index, MCP:** Query through `codegraph_explore` without an extra pre-query sync. The pinned CodeGraph MCP server already watches edits and reconciles changes on connection.
   - **Existing index, CLI only:** Run `codegraph sync <repo-root>` once before the first graph query for this task, not before every symbol lookup. `status` reports statistics, not a definitive source-freshness check; incremental sync is the freshness check.
   - **Stale result:** If MCP reports a pending/stale file, inspect that file directly for current content. When the result remains inconsistent with accessible source, use one `codegraph sync <repo-root>` if the CLI is available, then retry the graph query once. If the index is demonstrably corrupt or still unusable after sync, `codegraph index <repo-root> --force` is a last-resort, **one-time** local rebuild, only with write permission and no competing writer. Do not force-rebuild merely because time passed, a commit changed, or a symbol was not found.
   - **Failure:** If initialization, sync, or rebuild fails, do not loop, delete `.codegraph/`, run `uninit`, or alter global settings. Fall back to source search and report the missing graph coverage.
4. **Retrieve focused evidence.** Prefer one `codegraph_explore` request (or `codegraph explore "<question>"`) about the relevant path or symbol. Supply the exact `projectPath` for MCP across repositories where supported. Use `codegraph callers <symbol>`, `callees`, `impact`, `query`, and `git diff --name-only | codegraph affected --stdin` only for focused follow-ups.
5. **Verify consequential claims.** Check decisive source contracts and tests when needed. A graph can omit dynamic behavior, generated code, or unsupported files; no result is not proof of no dependency. Explain the observed path, impact, source locations, uncertainty, and smallest useful verification. Mention auto-initialization/sync only if it actually succeeded.

## Boundaries

- **No implicit environment setup:** Do not execute `codegraph install`, download binaries, change MCP configuration, or upgrade the CLI as a side effect of graph navigation. Installation/configuration remains a separate, consented operation; see [references/upstream.md](references/upstream.md).
- **No index writes just from activation:** Do not execute `init`, `sync`, or `index --force` merely because this Skill was loaded. Automatic per-repository index maintenance begins only for a graph-worthy task, in a writable and accessible checkout. Respect explicit read-only instructions and existing project permissions.
- **No extra infrastructure:** Do not add background daemons, hooks, timestamps, lock managers, or custom staleness databases; use upstream's own index, watcher, and incremental sync. Avoid concurrent rebuilds of the same worktree.
- **No invented access:** If only an MCP tool is accessible and it reports no index, but no CLI can reach that repository, use ordinary inspection instead of claiming to have initialized it. For Web-only sessions, explain the access boundary.
- `domain-modeling` covers conceptual design, `crux-first-reasoning` complex decisions, and `ponytail` implementation simplification. CodeGraph is evidence about **existing code**, not architectural authority.

Operational details and pinned version: [references/upstream.md](references/upstream.md). Positive/negative checks: [references/evaluation.md](references/evaluation.md).
