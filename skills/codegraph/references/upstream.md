# Upstream CodeGraph — provenance and operational notes

- **Project:** [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph).
- **Upstream license:** [MIT at v1.6.3](https://github.com/colbymchenry/codegraph/blob/v1.6.3/LICENSE) (Copyright © 2026 Colby Mchenry).
- **Current documented release:** [v1.6.3](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.3), tag commit `ef4bd058d97020a2b2a74a89f1bf21b84e9f5b30` (released 2026-11-17; checked 2026-11-20).
- **Previous local verified CLI:** v1.6.2, tag `6560052a6f856855d3f71eee838fd66ccfa4285d` (tested 2026-11-20).
- **Upstream manual:** [README at v1.6.3](https://github.com/colbymchenry/codegraph/blob/v1.6.3/README.md).
- This is a Skill maintained in `oydodo/skills`, not a bundled binary or an installed MCP server.

## Installation vs local index maintenance

Installation/upgrade is separate and requires user approval. The Skill does not run these implicitly:

```sh
npm install -g @colbymchenry/codegraph@1.6.3
codegraph install --print-config codex  # inspect global config target
codegraph install                       # changes MCP / agent configuration
codegraph upgrade --check              # read-only update check
```

For a graph-worthy task in an accessible, writable local worktree:

```sh
codegraph version
codegraph status <repo-root>
codegraph status --strict <repo-root>  # v1.6.3+: stronger, but inspect diagnostic
codegraph init <repo-root> --yes --local-only  # v1.6.3+ first-time, keep Git clean
codegraph init <repo-root> --yes       # v1.6.2 fallback (no --local-only)
codegraph sync <repo-root>             # incremental refresh, same engine
codegraph index <repo-root>            # full rebuild; needed when old engine indexed it
```

`codegraph index` **always performs a full rebuild**. The optional `--force` flag permits otherwise restricted root/home locations; **do not use it as a routine force-reindex switch**. Avoid special/sensitive paths, unrelated repos and concurrent writers. Honor `CODEGRAPH_DIR` and worktree/OS-specific index locations. No arbitrary deletion of `.codegraph/` or global changes.

## Index freshness and diagnostics

- **MCP mode:** The CodeGraph server already watches files, debounces edits and reconciles on connection. A pending-file staleness banner means inspect that file directly; do not sync before every MCP request.
- **CLI-only mode:** Run one `sync` before the first graph query per task. A normal `status` can show statistics without establishing source freshness; no custom Git SHA / age / mtime ledger is needed.
- **Old engine index:** From v1.6.3, `status` explicitly warns if the graph was built by an earlier engine, and the agent may surface a one-time warning. `sync` cannot replace the full re-index of unchanged files after an upgrade; run `codegraph index <repo-root>` once when permitted.
- **Framework/config changes:** Follow an explicit `status` recommendation for full re-index if the effective framework/config changed, rather than treating a routine source edit the same way.
- **Partial language coverage:** v1.6.3 adds `status --strict`, which exits nonzero for missing/incomplete/outdated indexes and partial parser coverage. A nonzero exit **does not by itself prove index corruption or mean retry until green**. Inspect the diagnostic and source compatibility.
- **Errors:** At most one incremental recovery/retry, and one full re-index if the index is demonstrably unusable or engine-old. No loops; gracefully fall back to source search if recovery cannot complete.

## Relevant CLI and MCP commands

| Purpose | Command |
| --- | --- |
| Version and availability | `codegraph version` |
| Check graph | `codegraph status [path]`; v1.6.3+ `status --strict [path]` |
| Focused evidence | `codegraph explore "<question>"` or MCP `codegraph_explore` |
| Symbol lookup | `codegraph query "<term>"` |
| Call relationships | `codegraph callers <symbol>` / `codegraph callees <symbol>` |
| Change radius | `codegraph impact <symbol>` |
| Candidate changed-file tests | `codegraph affected <paths...>` or `codegraph affected --stdin` |
| Initialize local-only (v1.6.3+) | `codegraph init [path] --yes --local-only` |
| Incremental refresh | `codegraph sync [path]` |
| Full re-index | `codegraph index [path]` |
| New v1.6.3 navigation | `codegraph implementations <name>`; `codegraph cycles` |

The standard MCP surface exposes `codegraph_explore`; other tools may not be exposed. Real code may use unsupported constructs, dynamic dispatch or ignored/generated files; verify consequential conclusions against actual source/tests. If local CLI version differs, check `codegraph help <command>` before using version-specific flags.

**Compatibility:** Not the unrelated CodeScope/`codegraph-ai` or CodeGraphContext (`cgc`).
