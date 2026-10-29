# Upstream attribution and adaptation notes

This Wayfinder skill is an adapted implementation of the decision-wayfinding method described in Matt Pocock's `wayfinder` Skill:

- Source: https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md
- Upstream repository: https://github.com/mattpocock/skills
- Copyright: (c) 2026 Matt Pocock
- License: MIT

Preserved concepts: destination, canonical decision map (index rather than duplicate store), precise decision tickets, blocker dependencies, frontier of unblocked and unclaimed questions, fog of war, scoped-out work, and incremental resolution.

Adaptations for ChatGPT Web and Claude Web: no mandatory issue-tracker setup, no mandatory local file or subagent access, portable store adapters, explicit cross-session durability caveat, skill-composition optional, and same-session continuation by request. The adaptation is maintained in `oydodo/skills` rather than being a verbatim upstream copy. It must be reviewed manually when upstream behavior changes.

## MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
