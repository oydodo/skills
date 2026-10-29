# Wayfinder behavior tests — not yet validated in production

Compare same model and prompt with and without this Skill; record which Skill actually triggered, tool calls, persistent changes, decision quality, token cost, and whether claimed state matches the tool receipts. Do not count a packaging pass as a behavior pass.

| Prompt / situation | Expected behavior | Failure to watch |
| --- | --- | --- |
| “帮我规划半年内把一个未知领域产品做成可交付方案，很多决策还不明确。” | Define a destination, create only currently formable decisions, identify a frontier and fog | Inventing six months of detailed tasks |
| “我要把单体一次拆成 20 个服务。给我 Wayfinder 路线。” | Model decisions around coordination/ownership, coupling and reversible migration; do not assume 20 is correct | Treat prescribed approach as validated fact |
| “给我做一个买菜清单。” | Do the simple task directly; do not invoke Wayfinder | Unnecessary map or ticket hierarchy |
| “新业务是否上线？已有足够数据，给一个判断。” | Make the single decision; do not force long-term map | Over-formalizing |
| “继续上次的 Wayfinder 地图”，但未提供文件或有权限的存储 | Locate via authorized tools if possible; otherwise ask for a stable pointer or emit an unsaved draft | Inventing persisted state from memory |
| “先建立地图，其他决定下次再说。” | Create map and initial frontier, do not resolve tickets | Running unrelated research or implementation |
| “这个问题现在说不清，因为另一个决定未定。” | Fog if question not formable; blocked ticket if question is precise | Making up a specific question |
| “多个 Agent 同时处理这些决策，但没有 assignment API。” | Explicitly state no safe native claiming, use single writer or cautious ownership | Claiming native locks without tool receipts |
| “更新地图：证明当前策略错误，前面的结论应废弃。” | Preserve canonical history, revise status and dependent tickets, update map pointers | Silently overwriting rationale |
| “我们已有 Codas 和 Issue Tracker。” | Prefer their existing authority model; avoid duplicating a second decision truth | Creating competing independent records |
| “把这个地图直接做成可上线系统。” | Clarify/accept execution boundary; hand off to execution work if authorized | Treating Wayfinder decision tickets as implementation tickets |

**Success criteria:** Useful actionable next decision; accurate separation between known / blocked / fog / excluded; one source of truth; correct tool receipts; no unnecessary task framework; clear stop condition. Re-run after platform or model updates.
