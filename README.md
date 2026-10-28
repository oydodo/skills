# Skills

**判断可靠 → 深入分析 → 按需交付。** 所有核心能力均以 Skill 管理。

```mermaid
flowchart TB
    L0["L0 · 判断准则"]
    L1["L1 · 理解与分析"]
    L2C["L2a · 编码简化"]
    L2W["L2b · 技术表达"]

    L0 --> IJ["independent-judgment"]
    L0 -. "问题需要深入分析" .-> L1
    L1 --> CR["crux-first-reasoning"]
    L1 --> IM["interview-me"]
    L1 --> GR["grilling"]

    L1 -. "编码任务" .-> L2C
    L1 -. "写作任务" .-> L2W

    L2C --> PT["ponytail"]
    L2W --> TW["technical-writing"]
    L2W --> TD["technical-documentation"]
    L2W --> TL["technical-language"]

    classDef layer stroke-width:2px,font-weight:bold
    class L0,L1,L2C,L2W layer
```

**核心 2 个**：`independent-judgment`（判断纪律）、`crux-first-reasoning`（深度分析）。其他 6 个按任务调用，不强制逐层执行。

**精选 8 个 Skill**，其中 Matt 仅 `grilling`（1/31）。Skill 的存储形式不保证每次自动调用；本机 80 个目录尚未调整。

[选用清单](registry/skills.yaml) · [剪枝分组](registry/curation.yaml) · [调用边界](core/README.md)
