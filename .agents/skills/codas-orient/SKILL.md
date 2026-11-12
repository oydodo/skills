---
name: codas-orient
description: Find the current intent, reasons and unknowns relevant to a path or question in a Codas-governed repository before deciding what to do.
---

# Codas Orient

Before a change, find four things: which Intent sentence it serves, what holds now, why, and what is
unknown or missing. Start with `codas-ontology`.

1. Name what this work serves and the Intent sentence it traces to, and whether a simpler way exists.
   If nothing backs it, report "没有本体背书" and hand it to the person.
2. From each path, read the nearest `README.md` (what it is now) and `AGENTS.md` (how to work there),
   then the README of the whole it belongs to: its promise is part of the change. Follow their links to
   Notes for why. List proposed Notes that concern it apart from what holds; a proposal does not bind
   existing code.
3. Look at dependencies: what it uses and what uses it. Run `codegraph status`; with an index,
   `codegraph node -f "<file>" --symbols-only` and `codegraph callees "<symbol>" -f "<file>"`. Without
   one, report "代码关系未知" and go on; do not build an index.
4. Only when links run out, `git grep` at M; report what only the search finds as a missing link.
   Do not infer ownership from names, directories or similar text; not found is not absent.
5. Read the code or facts needed; keep them apart from stated text. Do not write findings back as rules.
6. Return, with sources: M and whether it is verified; the Intent sentence served; what holds and why;
   the whole's promise; dependencies; proposals; missing homes, missing links and unknowns; the next
   decision for the person.
