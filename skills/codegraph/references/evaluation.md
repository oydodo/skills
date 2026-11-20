# CodeGraph Skill — behavioral acceptance examples

These are manual agent-behavior checks, **not** measured results. Record actual CLI/MCP calls, created/modified files, index state and whether the Agent fell back.

| Scenario | Prompt / environment | Expected behavior |
| --- | --- | --- |
| Missing local index | Cross-file trace, local CLI v1.6.3+, writable repo, no index | Confirm `status` says not initialized; `codegraph init <repo-root> --yes --local-only` once, confirm status, query. Avoid tracked Git changes. |
| Older CLI fallback | Same, CLI v1.6.2 | Use `codegraph init <repo-root> --yes` (no unsupported `--local-only`). |
| Old engine index | Existing index built by earlier engine, status advises re-index | Use `codegraph index <repo-root>` once; `sync` alone is insufficient. Do not pass `--force`. |
| Current index through MCP | Connected, current graph | Use `codegraph_explore` directly, without extra `init`/`sync`/full re-index. |
| Existing index, CLI only | Find callers, current engine, index exists | One `sync` before first query; no per-lookup sync. |
| Changed file, MCP pending | MCP flags a pending/stale file | Read real source. If mismatch persists, sync once and query once again; no stale assertions. |
| Incomplete language coverage | v1.6.3 `status --strict` reports partial indexing | Inspect language/file diagnostic, don't mislabel as absent/corrupt, and don't loop full builds. |
| Broken index | `sync` reports corruption / leaves demonstrably unusable index | Try one `codegraph index <repo-root>` if writable and safe; otherwise fall back. |
| Missing CLI/MCP | Neither exists | Use built-in search; don't install automatically. |
| Read-only worktree | No index, explicit read-only checkout | Don't initialize; fall back. |
| Wrong worktree | Multiple worktrees, one indexed | Scope precisely; no index maintenance in sibling worktree. |
| Negative: tiny edit | Correct one README typo | No graph check or index write. |
| Negative: age/HEAD alone | Index mtime old or Git HEAD changed, no source discrepancy | Don't do a full rebuild just for age/HEAD. |
| Restricted location | Path resolves into home, root or sensitive folder | Don't use `index --force` to bypass location safeguards. |
| Web-only | Local laptop repo unavailable | Explain access limits; no fake indexing. |
| Explicit tooling setup | User requests installing/upgrading CodeGraph | Seek authorization for CLI changes/config, inspect the pinned docs and verify separately. |

Rubric: index available only when relevant; missing index repaired with permission; normal changes synced without duplication; engine upgrades re-indexed; no unsafe force flag, extra infrastructure or loops; degrade gracefully.
