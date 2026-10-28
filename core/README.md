# 工作能力架构

**核心原则**：行为约束是常驻底座；按任务进入认知、行动、验证或表达，不固定调用链。

| 层 | 决策问题 | 精选 Skill |
| --- | --- | --- |
| L0 行为底座 | 凭什么相信结论？ | [Independent Judgment](../instructions/independent-judgment.md)（全局指令，非 Skill） |
| L1 理解与决策 | 目标是什么？什么最关键？方案经得起挑战吗？ | `interview-me`、`crux-first-reasoning`、`grilling` |
| L2 解决问题 | 应该怎样设计、诊断和最小化实现？ | `domain-modeling`、`diagnosing-bugs`、`ponytail` |
| L3 结果验证 | 改动满足要求和约束吗？ | `code-review` |
| L4 表达交付 | 怎样让读者准确理解成果？ | `technical-writing`、`technical-documentation`、`technical-language` |

## 触发边界

- L0 在每个任务中生效，**不靠一个每次触发的 Skill 实现**。
- L1：只有关键需求缺失才访谈；复杂分析才用 Crux；明确要求压力测试才用 Grilling。
- L2：工程任务按问题类型选 **建模、诊断或最简实现**，不默认三项全用。
- L3：需要审查现有改动时使用；不会因为未使用该 Skill 就跳过必要的自动测试。
- L4：根据交付物选择**一个主导写作 Skill**；单纯写作可直接进入此层，无须依次调用 L1–L3。

**第二个维度是选用状态，不是能力层级**：精选 / 待验证 / 项目专用 / 保留不动。详见 [剪枝清单](../registry/curation.yaml)。上游仓库不是完整的默认 Skill 集。

仓库元数据不自动改变 Codex、Claude 或 Pi 的本机发现配置。
