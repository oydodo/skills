# Skills

自研核心 + 精选上游。**目标工作集：10 个 Skill（Matt 仅 4/31）**。

```mermaid
flowchart TB
    subgraph L0["L0 · 全局规则｜始终生效"]
        IJ["independent-judgment"]
    end

    subgraph L1["L1 · 核心能力｜按需调用"]
        C["核心 4"]
        C --> R["判断｜crux-first-reasoning"]
        C --> I["澄清｜interview-me"]
        C --> G["挑战｜grilling"]
        C --> P["最简实现｜ponytail"]
    end

    subgraph L2["L2 · 专项能力｜按需调用"]
        S["专项 6"]
        S --> E["工程｜domain-modeling / diagnosing-bugs / code-review"]
        S --> W["表达｜technical-writing / technical-documentation / technical-language"]
    end

    IJ -->|"约束"| C
    C -. "任务需要时扩展" .-> S
```

**层次表示约束与能力扩展，不是强制执行顺序。** 只有全局规则常驻，其他 Skill 按需触发。

[精选清单](registry/skills.yaml) · [完整剪枝分组](registry/curation.yaml) · [剪枝依据](registry/pruning.md)

> 本机仍安装原有 80 个目录。此处是目标选用清单，**尚未实际停用本机 Skill**。
