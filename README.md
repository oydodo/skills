# Skills

**原则：独立判断贯穿始终；明确问题 → 解决问题 → 验证结果 → 清晰交付。**

```mermaid
flowchart TB
    A["L0 · 行为底座｜Always-on<br/>Independent Judgment<br/>证据优先 · 抗迎合 · 认知诚实"]
    B["L1 · 理解与决策｜按需<br/>interview-me（澄清目标）<br/>crux-first-reasoning（识别关键问题）<br/>grilling（挑战方案）"]
    C["L2 · 解决问题｜按需<br/>domain-modeling（建模）<br/>diagnosing-bugs（故障诊断）<br/>ponytail（最小完整实现）"]
    D["L3 · 结果验证｜按需<br/>code-review（规范与需求双轴审查）"]
    E["L4 · 表达交付｜按需<br/>technical-writing（中文技术写作）<br/>technical-documentation（开发文档）<br/>technical-language（技术英语）"]

    A -->|"约束所有任务"| B
    B -. "需要工程行动" .-> C
    C -. "需要独立审查" .-> D
    D -. "需要对外表达" .-> E
    B -. "分析报告可直接交付" .-> E
```

**这是一张能力关系图，不是强制流水线。** 只有 L0 常驻；其余根据任务选择，简单任务可跳过中间层。

当前 **10 个精选候选 Skill**（Matt 4/31），尚未完成实际效果验收或本机剪枝。上游 submodule 只是来源库，不代表全量启用。

[选用清单](registry/skills.yaml) · [候选与排除清单](registry/curation.yaml) · [剪枝标准](registry/pruning.md)
