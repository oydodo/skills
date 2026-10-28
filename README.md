# Skills

**原则：独立判断贯穿始终；明确问题 → 解决问题 → 验证结果 → 清晰交付。**

```mermaid
flowchart TB
    L0["L0 · 行为底座｜始终生效"]
    L1["L1 · 理解与决策｜按需"]
    L2["L2 · 解决问题｜按需"]
    L3["L3 · 结果验证｜按需"]
    L4["L4 · 表达交付｜按需"]

    L0 -.-> L1
    L1 -.-> L2
    L2 -.-> L3
    L3 -.-> L4

    L0 --> IJ["Independent Judgment"]

    L1 --> IM["interview-me"]
    L1 --> CR["crux-first-reasoning"]
    L1 --> GR["grilling"]

    L2 --> DM["domain-modeling"]
    L2 --> DB["diagnosing-bugs"]
    L2 --> PT["ponytail"]

    L3 --> RV["code-review"]

    L4 --> TW["technical-writing"]
    L4 --> TD["technical-documentation"]
    L4 --> TL["technical-language"]

    classDef layer stroke-width:2px,font-weight:bold
    class L0,L1,L2,L3,L4 layer
```

**这是一张能力关系图，不是强制流水线。** 只有 L0 常驻；其余根据任务选择，简单任务可跳过中间层。

当前 **10 个精选候选 Skill**（Matt 4/31），尚未完成实际效果验收或本机剪枝。上游 submodule 只是来源库，不代表全量启用。

[选用清单](registry/skills.yaml) · [候选与排除清单](registry/curation.yaml) · [剪枝标准](registry/pruning.md)
