# Skills

**全局约束 → 理解与判断 → 按任务交付。**

```mermaid
flowchart TB
    L0["L0 · 行为约束｜常驻"]
    L1["L1 · 理解与判断｜按需"]
    L2C["L2a · 编码简化｜编码任务"]
    L2W["L2b · 技术表达｜写作任务"]

    L0 --> IJ["Independent Judgment"]
    L0 -. "约束所有任务" .-> L1

    L1 --> CR["crux-first-reasoning"]
    L1 --> IM["interview-me"]
    L1 --> GR["grilling"]

    L1 -. "涉及编码" .-> L2C
    L1 -. "需要写作" .-> L2W

    L2C --> PT["ponytail"]
    L2W --> TW["technical-writing"]
    L2W --> TD["technical-documentation"]
    L2W --> TL["technical-language"]

    classDef layer stroke-width:2px,font-weight:bold
    class L0,L1,L2C,L2W layer
```

**真正的核心**：Independent Judgment（常驻规则）+ Crux-First Reasoning（复杂判断时触发）。其余 6 个 Skill 按需选用；流程不必逐层经过。

**精选 7 个 Skill，Matt 只保留 grilling（1/31）。** `domain-modeling`、`diagnosing-bugs`、`code-review` 已退出精选，不影响通常的建模、调试和审查工作。

[精选清单](registry/skills.yaml) · [剪枝分类](registry/curation.yaml) · [核心原则](core/README.md)

> 本机 80 个 Skill 尚未停用；上游 submodule 仍保留。
