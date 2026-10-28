# 精选与剪枝

**精选 8 个 Skill**：`independent-judgment`（判断纪律）与 `crux-first-reasoning`（深度分析）为核心；其余 6 项是场景工具。两者都按 Skill 管理，不假设 Always-on。

| 状态 | 数量 | 说明 |
| --- | ---: | --- |
| 精选 Skill | 8 | 判断准则 1 / 认知 3 / 编码 1 / 表达 3；其中 2 项自研尚未在本机安装 |
| Matt 未选中 | 30 | **仅保留 `grilling`**；未选中不等于删除 |
| DSH 项目专用 | 19 | 不进入通用工作集 |
| 其他未选中 | 11 | 暂不加入，按真实需求再评估 |
| 自研暂停 | 2 | `codex-appserver-doctor`、`remote-html-preview` 暂不处理 |
| Codas 排除 | 12 | 包含 `code-explainer`，暂不处理 |

## 本轮退出精选

- `domain-modeling`：特定领域建模方法，非通用推理核心。
- `diagnosing-bugs`：专用故障诊断流程，基础调试无需依赖它。
- `code-review`：特定的审查流程，通用代码审查无需额外 Skill。

三者仍保留在上游 submodule 和候选清单，可按实际需求重新选用。

**停用原则**：先验证 8 个精选 Skill 的调用效果，再可逆地缩减本机发现范围。此处仅修改仓库目标配置；本机原有 80 个目录未改变。

[精选清单](skills.yaml) · [80 项分类](curation.yaml) · [路由测试](../tests/core-routing.md)
