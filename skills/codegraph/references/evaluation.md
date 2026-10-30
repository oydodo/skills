# CodeGraph Skill — behavioral acceptance examples

These are manual routing tests, not claims of measured performance. Compare comparable sessions with/without the Skill and record which tools were actually called.

| Scenario | Prompt | Expected behavior |
| --- | --- | --- |
| Positive: cross-file | "Trace how /api/users reaches the database and show the affected callers." (indexed repo, CodeGraph available) | Use available `codegraph_explore` or `codegraph explore`, then verify decisive source paths; do not dump the graph. |
| Positive: refactor | "What calls Foo::save? Which tests may break if its signature changes?" | Use callers/impact/affected test info where supported, distinguish static impact from verified test coverage. |
| Missing CLI | "Investigate this call path." (accessible repo but no CodeGraph CLI/MCP) | Fall back to built-in search; no errors, invented tool calls, installation or index creation. |
| Missing index | "Trace the call path." (CLI installed, no project index) | Report the missing index; use ordinary source tools instead of silently running `codegraph init`. |
| Negative: tiny edit | "Correct this spelling mistake in README." | Complete the edit directly; don't invoke the graph skill or initialize CodeGraph. |
| Negative: Web-only | "Show the call graph of files on my laptop." (no local environment access) | Explain access limits; don't claim local indexing or MCP access. |
| Setup explicitly requested | "Set up CodeGraph for this repo." | Show/confirm install and target scope, warn that `codegraph install` changes agent config and `init` writes index; request approval where needed, verify actual result. |

Rubric: correct routing, no unauthorized setup, actual observable tool/index access, file-path evidence, and concise decision-relevant output.
