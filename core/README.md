# 最小核心

**两个核心 Skill，各司其职：**

- [independent-judgment](../skills/independent-judgment/SKILL.md)：证据独立、认识诚实、立场可修正。广泛适用于需要判断的任务，**不是强制分析步骤**。
- [crux-first-reasoning](../skills/crux-first-reasoning/SKILL.md)：复杂判断与检查、调研汇报中，先识别主要矛盾和主次关系，再验证可能改变判断的关键不确定性，并呈现依据与取舍，帮助用户理解和行动。

**场景工具**：`interview-me`（关键需求确实缺失）、`grilling`（明确要求挑战）、`ponytail`（编码简化）、`technical-writing` / `technical-documentation` / `technical-language`（选与交付物匹配的一项）。

**本地常驻核心**：[`always-on.md`](always-on.md) 是唯一的简短核心原则正文（包含三个核心 Skill 的本地入口及 GitHub 链接）；[`hooks.json`](hooks.json) 定义可选、失败放行的 SessionStart 注入。发布流程自动将两者打包进 Plugin，无须单独维护本机 AGENTS/CLAUDE 文件。完整 Skill 仍按需加载。Web Plugin 不保证运行这些本地 Hook。

[选用配置](../profiles/core.yaml) · [Skill 索引](../registry/skills.yaml) · [剪枝状态](../registry/curation.yaml)
