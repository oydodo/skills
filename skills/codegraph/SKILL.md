---
name: codegraph
description: "Use the open-source colbymchenry/CodeGraph CLI or MCP to investigate an accessible local repository's structural code graph: cross-file calls, implementation paths, callers/callees, dependency and refactor impact, and affected tests. Apply for nontrivial codebase navigation, bug localization or change-risk analysis when a CodeGraph index/tool is available, or when the user explicitly wants to set up CodeGraph. Do not force graph queries for small edits; if the binary, MCP tool, or local index is unavailable, fall back to ordinary repository inspection without blocking."
---

# CodeGraph — Repository graph navigation

**Purpose:** Find the smallest code context that explains a cross-file behavior or change impact. This is a **maintained Skill adapter** for the MIT-licensed external project [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph); it does **not** bundle the CodeGraph executable, install MCP servers, or assume Web sessions can access local files.

## Workflow

1. **Establish scope.** Identify the actual repository/worktree and the question to answer. Use graph analysis for cross-file symbol relationships, call chains, route-to-handler paths, blast radius, test selection, and refactor/bug investigations. Simple edits, known-file reads, or straightforward grep do not need CodeGraph.
2. **Check availability without modifying the environment.** If an installed `codegraph_explore` MCP tool is exposed, use it. Otherwise check whether `codegraph` CLI is accessible (`command -v codegraph` in a POSIX shell, or the platform's equivalent); run `codegraph status .` in the target repository before querying. Respect configured alternate index directories. A missing CLI, unusable tool, absent index, or failing command is **nonblocking**: continue with built-in repository search and label the missing coverage.
3. **Retrieve focused graph evidence.** Prefer one `codegraph_explore` request (or `codegraph explore "<question>"`) asking specifically for the relevant call path, symbol or flow. Include `projectPath` when using MCP across repositories and the tool accepts it. For targeted follow-up use the CLI, if installed:
   - `codegraph callers <symbol>` / `codegraph callees <symbol>` — callers and callees.
   - `codegraph impact <symbol>` — potential change radius.
   - `codegraph query "<symbol-or-query>"` — symbol discovery.
   - `git diff --name-only | codegraph affected --stdin` — candidate affected tests (only when meaningful for the diff).
4. **Verify, don't reify the index.** Confirm decisive file paths, line ranges, contracts, dynamic behavior and test coverage in real source and/or executable checks. A static graph can miss runtime dispatch, generated code or unsupported files, and an index can be stale; report such limits. Avoid treating graph edges as authoritative architecture or a proven root cause.
5. **Deliver actionable context.** Explain the observed route/call chain, the likely binding point or impact surface, supporting source locations, what is still uncertain, and the smallest sensible verification. Prefer concise evidence over a full repository dump.

## Setup is a separate, consented operation

CodeGraph is **not installed by this Skill**. If the user asks to install or configure it, first check their environment and refer to [the version-pinned upstream guide](references/upstream.md). `codegraph install` modifies agent MCP/instruction settings; `codegraph init` writes a local project index; `codegraph sync` changes that index. Do not execute these commands merely because this Skill was loaded. Respect the user's requested scope and permissions.

## Integration boundaries

- The CodeGraph MCP tool and its usage guidance come from the **separately installed** CodeGraph server. The Plugin's Skill metadata is not an MCP server and does not grant remote or local code access on its own.
- Never invent a graph, project index, tool output or completed installation. If tooling is missing or a client is Web-only, provide a normal code-analysis response with the available tools, or state which local step requires user action.
- `domain-modeling` concerns conceptual/domain design; this Skill inspects **existing code relationships**. `crux-first-reasoning` handles complex decisions and dominant constraints. `ponytail` handles implementation simplification. Combine only when the actual task requires them; do not make CodeGraph a global prerequisite.
- Upstream source, pinned CLI version, license and command reference: [references/upstream.md](references/upstream.md).
- Positive/negative routing checks: [references/evaluation.md](references/evaluation.md).
