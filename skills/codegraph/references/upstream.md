# Upstream CodeGraph — provenance and operational notes

- **Project:** [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)
- **Upstream license:** [MIT](https://github.com/colbymchenry/codegraph/blob/v1.6.2/LICENSE) (Copyright © 2026 Colby Mchenry).
- **Pinned documented release:** [v1.6.2](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.2), tag commit `6560052a6f856855d3f71eee838fd66ccfa4285d` (checked 2026-10-30).
- **Upstream manual:** [README at v1.6.2](https://github.com/colbymchenry/codegraph/blob/v1.6.2/README.md).
- This Skill is maintained in `oydodo/skills`. It does not bundle upstream software or alter a separately installed CLI/MCP server.

## Distinguish setup from per-repository maintenance

**Installation requires separate approval:**

```sh
npm install -g @colbymchenry/codegraph@1.6.2
codegraph install --print-config codex  # inspect first
codegraph install                       # modifies supported agent MCP config
```

**Per-repository graph operations for an actual graph-worthy task:**

```sh
codegraph status <repo-root>          # stats / absence; not proof of freshness
codegraph init <repo-root> --yes      # first-time local graph, when missing
codegraph sync <repo-root>            # incremental update of existing graph
codegraph index <repo-root> --force   # last resort: full rebuild, not normal refresh
```

The user may authorize the Skill to initialize/refresh a graph automatically when analyzing a writable repository. That does **not** authorize installation, modifying global MCP settings, deleting index files, or indexing unrelated repositories. Honor `CODEGRAPH_DIR`, worktree/OS-specific index locations, and explicit read-only restrictions. Do not infer "missing" from any nonzero `status` exit: inspect the diagnostic first.

## Freshness in pinned v1.6.2

- The MCP server's watcher incrementally syncs edited source files after a debounce period. It also reconciles the working tree on connection. A per-file staleness banner means current source should be inspected directly until the graph catches up.
- `codegraph status` reports statistics; it is **not** a reliable standalone freshness oracle. For CLI-only graph navigation, run an incremental `sync` once before querying, rather than inventing a Git-HEAD/mtime TTL scheme.
- When an MCP result remains inconsistent with supported local source, sync once and retry once. Reserve forced `index` for actual corruption/unusable state after sync; avoid overlapping index writers and never loop on errors.
- If the installed version differs, consult `codegraph help <command>` and its installed docs instead of assuming v1.6.2 flags or background behavior.

## Relevant CLI and MCP commands (v1.6.2)

| Purpose | Command |
| --- | --- |
| Version and availability | `codegraph version` |
| Check index | `codegraph status [path]` |
| Focused evidence | `codegraph explore "<question>"` |
| Symbol lookup | `codegraph query "<term>"` |
| Call relationships | `codegraph callers <symbol>` / `codegraph callees <symbol>` |
| Change radius | `codegraph impact <symbol>` |
| Candidate changed-file tests | `codegraph affected <paths...>` or `codegraph affected --stdin` |
| Initialize local graph (writes) | `codegraph init [path] --yes` |
| Incremental refresh (writes) | `codegraph sync [path]` |
| Forced re-index (writes) | `codegraph index [path] --force` |

The standard MCP tool is `codegraph_explore`; other MCP tools may not be exposed. Tooling may miss unsupported languages, ignored files, generated code, and runtime dispatch; verify consequential claims against source/tests. CodeGraph is not `codegraph-ai` or CodeGraphContext (`cgc`).
