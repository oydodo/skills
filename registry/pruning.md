# 精选与剪枝

**精选 13 个 Skill**：L0 `philosophical-foundation` 与两个判断核心保持独立。`wayfinder` 改为 Matt 原版 Submodule 来源；一并引入 `domain-modeling`、`research`、`prototype` 三项协作能力。7 个原有专项能力仍独立保留。所有第三方 Skill 的正文在构建时保持原样，不设适配补丁。

| 状态 | 数量 | 说明 |
| --- | ---: | --- |
| 精选 Skill | 13 | 哲学 1 / 判断 1 / 认知 4 / 决策导航 1 / 调研与原型 2 / 编码 1 / 表达 3；其中 3 项由本仓库维护 |
| Matt 未选中 | 26 | 已从 Matt 精选 `grilling`、`wayfinder`、`domain-modeling`、`research`、`prototype`；其余保留候选 |
| DSH 项目专用 | 19 | 不进入通用工作集 |
| 其他未选中 | 11 | 暂不加入，按真实需求再评估 |
| 自研暂停 | 2 | `codex-appserver-doctor`、`remote-html-preview` 暂不处理 |
| Codas 排除 | 12 | 包含 `code-explainer`，暂不处理 |

## 本轮退出精选

- `domain-modeling`：本轮重新入选，供 Wayfinder 与独立建模任务按需调用。
- `diagnosing-bugs`：专用故障诊断流程，基础调试无需依赖它。
- `code-review`：特定的审查流程，通用代码审查无需额外 Skill。

`diagnosing-bugs` 与 `code-review` 仍在上游和候选清单中，可根据实际效果再评估。

**停用原则**：先验证 13 个精选 Skill 的调用效果，再可逆地缩减本机发现范围。此处仅修改仓库目标配置；本机原有 80 个目录未改变。

[精选清单](skills.yaml) · [80 项分类](curation.yaml) · [路由测试](../tests/core-routing.md)
