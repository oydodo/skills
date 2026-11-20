---
name: codegraph
description: "Use the open-source colbymchenry/CodeGraph CLI or MCP to investigate accessible local repositories: cross-file calls, implementation paths, callers/callees, dependency and refactor impact, and affected tests. For graph-worthy tasks, automatically initialize a missing local index or refresh a stale one when the CLI and repository writes are available. Do not force CodeGraph on small edits or install tooling without approval; fall back to ordinary repository inspection when graph access is unavailable."
---

# CodeGraph — Repository graph navigation

**Purpose:** Find the smallest code context that explains cross-file behavior or change impact. This is a maintained Skill adapter for the MIT-licensed [colbymchenry/CodeGraph](https://github.com/colbymchenry/codegraph). It does **not** bundle the executable, install MCP servers, or grant access to a user's machine.

## Workflow

1. **Scope the task.** Identify the exact local repository/worktree and the question. Use CodeGraph for cross-file paths, symbol relationships, blast radius, affected tests, and nontrivial debugging/refactoring. Skip it for a tiny edit, a known-file read, or straightforward grep. Do not index repositories outside the task.
2. **Check access and version.** Prefer an available `codegraph_explore` MCP tool. If a shell can reach the exact repository, check for the `codegraph` CLI (`command -v codegraph` on POSIX), run `codegraph version` and inspect `codegraph status <repo-root>`. On v1.6.3+, also use `codegraph status --strict <repo-root>` when useful; inspect its diagnostic, not only the exit code (it also fails on partial language coverage). Respect `CODEGRAPH_DIR` and per-OS/worktree indexes; `.codegraph/` existing does not guarantee readiness. Missing tools or inaccessible checkouts are **nonblocking**.
3. **Ensure a usable graph, only when the task needs one.**
   - **Missing index:** If `status` explicitly reports an uninitialized repository, the CLI can write there, and the target is safe to index, run `codegraph init <repo-root> --yes --local-only` on v1.6.3+ (avoid changes to tracked Git files). On v1.6.2 run `codegraph init <repo-root> --yes`. Verify with `status`. Do not classify an unknown error or a partial index as missing.
   - **Outdated engine/index metadata:** If `status` explicitly reports an index built by an older CodeGraph engine, or recommends re-indexing after a framework/config change, run `codegraph index <repo-root>` once before trusting graph queries, assuming write permission and no conflicting index writer. **Incremental `sync` does not reprocess all existing symbols after an engine upgrade.** `index` already means full rebuild: `--force` only bypasses safeguards for home/filesystem roots and must not be used for routine recovery.
   - **Existing current index, MCP:** Query via `codegraph_explore` without extra pre-query sync. v1.6.2+ MCP watches edits and reconciles files on connection. Handle its per-file staleness banner by reading current source.
   - **Existing current index, CLI only:** Run `codegraph sync <repo-root>` once before the first graph query of the task, not between individual lookups. `status` statistics alone do not prove source freshness.
   - **Persistent inconsistency or damage:** If MCP's result remains inconsistent with accessible source, try one local `sync` and query retry. If the index is demonstrably damaged or incomplete after sync (not merely a missing/unsupported symbol), try `codegraph index <repo-root>` once when safe; otherwise fall back. Do not rebuild just because time passed or Git HEAD changed.
   - **Failure:** Never loop, delete `.codegraph/`, run `uninit`, or modify global settings to recover. Report missing graph coverage and use source search.
4. **Retrieve focused evidence.** Prefer one `codegraph_explore` request (or `codegraph explore "<question>"`) about the relevant path or symbol. Supply the exact `projectPath` for MCP across repositories where supported. Use `codegraph callers <symbol>`, `callees`, `impact`, `query`, and `git diff --name-only | codegraph affected --stdin` only for focused follow-ups.
5. **Verify consequential claims.** Check decisive source contracts and tests when needed. A graph can omit dynamic behavior, generated code, or unsupported files; no result is not proof of no dependency. Explain the observed path, impact, source locations, uncertainty, and smallest useful verification. Mention auto-initialization/sync only if it actually succeeded.

## Boundaries

- **No implicit environment setup:** Do not execute `codegraph install`, download binaries, change MCP configuration, or upgrade the CLI as a side effect of graph navigation. Installation/configuration remains a separate, consented operation; see [references/upstream.md](references/upstream.md).
- **No index writes just from activation:** Do not execute `init`, `sync`, or `index --force` merely because this Skill was loaded. Automatic per-repository index maintenance begins only for a graph-worthy task, in a writable and accessible checkout. Respect explicit read-only instructions and existing project permissions.
- **No extra infrastructure:** Do not add background daemons, hooks, timestamps, lock managers, or custom staleness databases; use upstream's own index, watcher, and incremental sync. Avoid concurrent rebuilds of the same worktree.
- **No invented access:** If only an MCP tool is accessible and it reports no index, but no CLI can reach that repository, use ordinary inspection instead of claiming to have initialized it. For Web-only sessions, explain the access boundary.
- `domain-modeling` covers conceptual design, `crux-first-reasoning` complex decisions, and `ponytail` implementation simplification. CodeGraph is evidence about **existing code**, not architectural authority.

Operational details and supported versions: [references/upstream.md](references/upstream.md). Positive/negative checks: [references/evaluation.md](references/evaluation.md).
