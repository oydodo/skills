# CodeGraph Skill — behavioral acceptance examples

Manual agent-behavior tests, **not** performance measurements. For each case, record actual CLI/MCP calls, index changes, source checks, and whether the agent fell back appropriately.

| Scenario | Prompt / environment | Expected behavior |
| --- | --- | --- |
| Missing local index | "Trace how /api/users reaches storage." CLI installed, writable local repo, no index | Detect absent index via `status`; run `codegraph init <repo-root> --yes` once; confirm status; query graph and cite source. |
| Current index through MCP | "Trace this cross-file call chain." MCP connected, current graph | Use `codegraph_explore`; do **not** run unnecessary `init`, `sync`, or a forced rebuild. |
| Existing index, CLI only | "Find callers of Foo::save." CLI installed, index exists, no MCP | Run one `codegraph sync <repo-root>` before first task query; use focused `callers` / `impact`; don't sync between every lookup. |
| Changed file, MCP pending | "What calls Foo?" MCP response marks a pending/stale source file | Read that file from source; if mismatch persists and CLI is accessible, sync once and retry once. Do not present the pending graph as fresh. |
| Broken index | "Analyze this flow." `sync` reports corruption or leaves a demonstrably unusable index | Try one `codegraph index <repo-root> --force` only if writable and safe; otherwise fall back; never delete the index or loop. |
| Missing tool | "Investigate this call path." Neither local CLI nor usable MCP | Use built-in search; no installation, invented queries, or graph writes. |
| Read-only worktree | "Trace this path." CLI available but checkout explicitly read-only and index absent | Do not initialize; use other tools and state the limitation. |
| Wrong worktree | Same project has multiple worktrees, only one indexed | Use the task's exact root; do not silently initialize or sync a sibling checkout. |
| Negative: tiny edit | "Correct a typo in README." | Edit directly; no graph check, indexing, or sync. |
| Negative: time/commit change alone | An index is present, but its mtime is old or Git HEAD changed | Don't force a full rebuild based solely on age/HEAD; use upstream freshness mechanisms. |
| Web-only | "Show the call graph of files on my laptop." No local filesystem/tool access | Explain limitations; no claim of local indexing or MCP connectivity. |
| Explicit tooling setup | "Install CodeGraph for this machine." | Obtain approval for changing the executable/MCP configuration, follow pinned docs, and independently verify installation. |

Rubric: graph used only when relevant; missing index repaired automatically with valid permission; stale graph refreshed without extra infrastructure; no destructive retries; actual source and task-scope evidence; graceful degradation.
