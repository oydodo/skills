# Upstream CodeGraph — provenance and operational notes

- **Project:** [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)
- **Upstream license:** [MIT](https://github.com/colbymchenry/codegraph/blob/v1.6.2/LICENSE) (Copyright © 2026 Colby Mchenry).
- **Pinned documented release:** [v1.6.2](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.2), tag commit \`6560052a6f856855d3f71eee838fd66ccfa4285d\` (checked 2026-10-30).
- **Upstream manual:** [README at v1.6.2](https://github.com/colbymchenry/codegraph/blob/v1.6.2/README.md).
- This Skill is written and maintained in \`oydodo/skills\`; no upstream source files, binaries, auto-installers, or bundled server are copied. It instructs an agent how to use a **separately installed**, open-source tool.

## Deliberate, local setup only

Only after user approval, and on a compatible machine:

\`\`\`sh
# Pinned npm alternative; upstream also provides a stand-alone installer.
npm install -g @colbymchenry/codegraph@1.6.2

# Inspect intended target configuration before installation:
codegraph install --print-config codex

# Optional: writes MCP and related agent configuration (review target first).
codegraph install

# In each explicitly selected repository: creates .codegraph/ index.
codegraph init
\`\`\`

A separately installed CLI is **not** enough for MCP use: \`codegraph install\` wires supported agents, and \`codegraph init\` builds the per-project index. In an environment where config and code access are unavailable, do not claim the Plugin alone enables CodeGraph.

If the installed version differs, use \`codegraph help <command>\` and its own docs rather than assuming these flags remain valid. Do not run network shell-pipe installers, initialize repositories, or modify global agent settings without approval.

## Relevant CLI and MCP commands (v1.6.2)

| Purpose | Command |
| --- | --- |
| Version and availability | \`codegraph version\` |
| Check index | \`codegraph status [path]\` |
| Focused evidence | \`codegraph explore "<question>"\` |
| Symbol lookup | \`codegraph query "<term>"\` |
| Call relationships | \`codegraph callers <symbol>\` / \`codegraph callees <symbol>\` |
| Change radius | \`codegraph impact <symbol>\` |
| Candidate changed-file tests | \`codegraph affected <paths...>\` or \`codegraph affected --stdin\` |
| Refresh an existing index (writes) | \`codegraph sync [path]\` |

The default MCP surface exposes \`codegraph_explore\`. Other MCP tools are typically hidden unless configured; use CLI equivalents rather than assuming those extra tools exist. Indexing may be incomplete due to ignored files, unsupported language constructs, runtime dispatch, or stale content. Verify important conclusions against source and tests.

**Compatibility:** This guidance targets the local CLI/MCP project by Colby Mchenry; it is not the unrelated CodeScope/\`codegraph-ai\`, CodeGraphContext (\`cgc\`) or scholarly graph dataset projects.
