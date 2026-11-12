# AGENTS.md — Archived Agent Notes

Adapted from [DeepSeek Harness `687f282e8625c6b8d11ff58211a90524be2e4317`](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/.agents/notes/archived/AGENTS.md).

## Responsibility

Maintain the frozen archive's reading and sealing entry under the [Note rules](../AGENTS.md).

## Boundary

Archived Agent Notes under the kind directories are frozen historical snapshots, not current authority. Never edit, reformat, translate, repair, delete, or move a sealed artifact; use an active Agent Note or current documentation for new decisions and facts.

## Work

The archival change may only relocate a Markdown file, insert `Archived: YYYY-MM-DD` below `Status: implemented`, and repair or delete inbound links. Do not inspect, verify, or repair links out of archived notes.

Run the `codas-note-archive` workflow and append new artifact hashes with the archive Note check in `--write` mode (commands in `codas-note-archive`). The normal verifier rejects changed or missing sealed artifacts, invalid Markdown artifacts, unknown kind folders, and invalid archive metadata.
