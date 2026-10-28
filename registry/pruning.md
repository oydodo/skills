# Skill 筛选与剪枝

**先按能力归位，再决定是否保留。** 层级只反映作用；Skill 的来源、是否安装、是否启用是另外的维度。

当前目标工作集：**10 个待验收 Skill**（本机已有 9 个 + 仓库自研 Crux），以及 1 条常驻的 Independent Judgment 指令。

| 能力位置 | 数量 | 评估重点 |
| --- | ---: | --- |
| L1 理解与决策 | 3 | interview-me 与 grilling 不应无端启动长访谈；Crux 要提供可辩护的判断 |
| L2 解决问题 | 3 | domain-modeling 是否超出轻量建模需求；ponytail 不可省略正确性检查 |
| L3 验证 | 1 | code-review 应有明确审查对象、标准与需求依据 |
| L4 表达交付 | 3 | 三个写作 Skill 按中文方案 / 开发文档 / 英文技术表达分工，避免同时启用 |
| L0 全局行为 | 不计入 | Independent Judgment 不是 Skill，须在客户端单独配置 |

## 先退出精选，不等于删除

- **Matt 其余 27 项**：多数是配套工单流程、包装入口或特定场景，例如 `grill-me`、`grill-with-docs`、`ask-matt`、`to-spec` / `to-tickets` / `implement-spec`。不整体引入。
- **DSH 19 项**：以项目覆盖层管理；通用技能集不自动加载。
- **其他 11 项**：保留候选，包括 `product-brainstorming`、`visual-explainer`、`archify` 等，真正有使用场景时再比较。
- **自研暂缓 2 项、Codas 排除 12 项**：保留在本机，不纳入通用剪枝；`code-explainer` 属于后者。

## 二轮筛选门槛

1. 解决了一个**独特且重复出现**的任务，而非仅包装另一个 Skill 或模型已有能力。
2. 可在目标 Agent 上实际调用，必要工具与数据源具备，未导致过度访谈或流程膨胀。
3. 与较小组合比较，能提高准确性、可靠性或完成率；没有实测结果时保持“候选”而不是宣称已验证。
4. 本机剪枝先可逆停用，再观察回归；**不删除上游 submodule 或自研文件**。

[完整 80 项状态与选用范围](curation.yaml) · [当前选用路径](skills.yaml) · [行为验收样例](../tests/core-routing.md)

**实施状态**：此次只重构能力分层与目标配置。本机 80 个 Skill 仍保持现状。
