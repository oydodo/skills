---
name: wayfinder
description: "Use for long, uncertain, multi-session goals where the next decisions depend on discoveries not yet made: build or continue a decision map, find the current unblocked frontier, distinguish precise questions from fog of war, and preserve decisions across sessions. Trigger for 'wayfinder', '决策地图', '长期复杂目标', '跨会话推进', '未知路径' or similar intent. Skip routine plans, linear task lists, or one-off decisions that fit a single session."
---

# Wayfinder — navigate decisions through uncertainty

**Purpose:** chart the *route to a destination*, not execute the destination. Treat the unknown as real: create decisions only when their questions can already be stated. Work from the reachable frontier, then let each answer reveal the next part of the route. This is a lightweight, portable adaptation of Matt Pocock's Wayfinder (attribution: `references/attribution.md`).

## 1. Define the destination and the canonical store

- Confirm the desired **destination** in one or two sentences and the condition under which the *route is sufficiently clear* to hand off. Distinguish *deciding how* from *doing the work*; execution remains out of scope unless expressly requested.
- Resume the user's existing map if supplied. Use **one durable system of record**: an existing issue tracker with parent/child and dependencies when possible, or Markdown documents in a writable shared workspace. Do not make a second truth source when the project already has one (including Codas or another project ontology).
- A chat message, model memory, or an unshared temporary path is **not** durable cross-session storage. If no writable store is available, provide copyable map/decision artifacts and clearly mark them **not saved**; ask for a destination only when persisting is necessary. Never claim to have written or assigned an issue without a tool result.
- Keep a **map as an index**, not an encyclopedia: destination, short context pointers, links to resolved decisions, fog, and out-of-scope. Each decision's evidence and answer live in **one** canonical ticket/document. See `references/map-format.md`.

## 2. Chart the known frontier

1. Name the destination and its boundary. If the route is already obvious and fits one session, say a Wayfinder map is unnecessary and proceed with the simpler task.
2. Capture **precise decision questions** as tickets, even if their answers remain unknown or blocked. Record dependencies on other decisions or prerequisite facts. Prefer decisions over implementation to-dos.
3. Put only **not-yet-formulable** in-scope areas in **Fog of war**. Do not turn guessed future questions into dozens of premature tickets.
4. Put excluded work in **Out of scope**, not fog. Mark it with a reason.
5. The **frontier** consists of open, unblocked, unclaimed decisions. Report the best next decision by *name* (plus its link/path), with the reason it is ready. Stop at the map unless the user also asked you to resolve a decision.

## 3. Advance the map, one decision at a time

1. Load the saved map, its canonical links, and the latest ticket states. Check the current destination, known decisions, blocking relations, and frontier; do not substitute conversation memory for saved state.
2. Pick the requested decision, or select an open, unblocked, unclaimed frontier decision. **Claim before work** only where the store supports a real ownership/locking mechanism. Otherwise stay single-writer or warn about concurrent edits; never invent a lock.
3. Resolve by the smallest suitable method: **research** for missing evidence, **conversation** for a human-owned choice, **prototype** when a tangible example distinguishes options, or **prerequisite action** if the decision cannot be made until something concrete is done. Do not answer human-owned preferences on their behalf. Use `grilling`, `interview-me`, `crux-first-reasoning`, or other Skills only when each genuinely helps; none is a mandatory prerequisite.
4. Record the evidence, trade-off, decision, assumptions, and reversal condition **in that ticket**. Close only when its stated question is answered; if the evidence is insufficient, leave it open/blocked and identify the missing discriminator.
5. Update the map with a **one-line pointer** to the resolved decision; sharpen the fog into new tickets only as information permits. Re-evaluate blockers, invalidated earlier decisions, and changed scope. Respect the project's ownership/approval rules for remote writes.
6. Report what changed, what remains unknown, the current frontier, and **one** suggested next decision. Default to one decision per advancement; continue within the same session when explicitly requested, instead of imposing a fixed session limit.

## 4. Closure and guardrails

- **Done means the route is clear**, not that the destination has been implemented. Exit when the destination is defined, there are no unresolved in-scope decision tickets or relevant fog, and the next execution/decision owner can act from durable pointers. If the destination cannot yet be reached, state the blockers.
- Use a *name* and stable link/path for every ticket; keep findings where they belong rather than copying full notes into the map.
- Avoid auto-creating elaborate issue hierarchies for a small effort. Never require a particular issue tracker, GitHub write access, subagents, background execution, or a local shell on ChatGPT Web / Claude Web. Use available tools honestly, and avoid claiming background research or automatic future progress.
- The map reflects the **current state of knowledge**; it is not a fixed master plan. Update it when reality changes, but preserve traceability to the original decisions.

Templates, storage adaptations, and a compact example: `references/map-format.md`. Behavior tests and failure modes: `references/evaluation.md`.
