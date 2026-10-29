# Decision Map — canonical format and storage adapters

Use existing conventions first. The following schemas are *fallbacks*, not mandatory project structure. If a tracker or ontology already models these facts, map its existing fields rather than duplicating its authority.

## Map (an index, not a second source of decisions)

```markdown
# <Destination name>

## Destination
<What route we must make clear; what sufficient clarity looks like.>

## Notes
<Standing constraints, owner, pointers to current project authority.>

## Decisions so far
- [<Decision title>](<canonical location>): <one-line outcome>

## Fog of war
- <In-scope area whose precise question is not yet formable; what may reveal it>

## Out of scope
- <Excluded work and why; reference a closed ticket if one existed>
```

**Open decisions are not copied into the map.** Discover them by querying child issues or reading the separate decision index. If file-only storage cannot query, an index of linked *titles and statuses* is acceptable, but the decision's full contents stay in the decision file.

## Decision ticket (one canonical source)

```markdown
# <Decision title>

Question: <One question that can be stated precisely now>
Status: open | claimed | blocked | resolved | out-of-scope
Mode: research | conversation | prototype | prerequisite
Blocked by: <links to decisions or facts, or none>
Owner: <only when supported or manually assigned>

## Evidence and options
<Observations, provenance, alternative answers and uncertainties>

## Resolution
<Answer and decisive reasons; only after actually resolved>
<Reversal condition / what new evidence would change this>
```

Statuses are illustrations; prefer tracker-native state and labels. In a tracker, record resolution in the canonical ticket/comment; the map points to it rather than copying the answer. In Markdown, record one canonical resolved answer inside the ticket file and link it from the map.

## Storage selection

1. **Existing system (preferred)**: use the project's current Issue Tracker, Codas ontology or another authorized decision system. Match its states and ownership rules. Do not create a separate project truth system.
2. **GitHub Issues or another tracker**: use one parent map issue and child issues for decisions. Native dependencies and assignees only if the connected API supports them; otherwise record blocker links in the issue. Read before writing; use a claim only after a real successful assignment. Decisions are closed with their resolution in the issue. Do not silently write to a shared repo without permission.
3. **Writable Markdown workspace**: suggested fallback `wayfinder/<slug>/MAP.md` and `wayfinder/<slug>/decisions/<name>.md`, or adapt to the user's structure. This is durable only if the actual file write succeeds in a persistent place. Treat concurrent file edits cautiously; avoid phantom locking. Use one canonical decision document per question.
4. **Chat-only/no writable workspace**: produce a clearly labelled *unsaved* map and decision drafts in the answer or a user-downloadable artifact. Provide instructions for importing/saving them; do not pretend a later conversation can rediscover them.

## Frontier and fog

- **Frontier** = open AND no unresolved blockers AND not claimed by another worker. Sort by unblock impact and available evidence, not simply creation date.
- **Blocked ticket** = precise question already known, but prerequisites are unresolved. Keep it as a ticket.
- **Fog** = an in-scope region whose question **cannot yet be stated** without inventing details.
- **Out of scope** = intentionally excluded by the current destination, not unknown.

## Small example

Destination: *decide whether an internal app should be split into services, and on what boundaries.*

- Decision **What is the actual coordination failure?**: frontier, research + team interview.
- Decision **Which boundaries need independent deployment?**: blocked by the preceding decision.
- Fog: *data-ownership migration constraints*, not yet a precise question until boundaries emerge.
- Out of scope: *implementing the full migration*, because this Wayfinder is for deciding the design.

After resolving the first decision, add a short map pointer to its answer, unblock or reshape the second, and refine the fog if an actionable question is now sharp. Do **not** create a twenty-service delivery plan upfront.
