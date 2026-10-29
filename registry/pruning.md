# 精选与剪枝

**精选 9 个 Skill**：新增 L0 `philosophical-foundation`（哲学基础）；`independent-judgment`（判断纪律）与 `crux-first-reasoning`（关键推理）仍各自独立，其余 6 项为场景能力。任何 Skill 都不假设 Always-on。

| 状态 | 数量 | 说明 |
| --- | ---: | --- |
| 精选 Skill | 9 | 哲学基础 1 / 判断 1 / 认知 3 / 编码 1 / 表达 3；其中 3 项由本仓库维护 |
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

**停用原则**：先验证 9 个精选 Skill 的调用效果，再可逆地缩减本机发现范围。此处仅修改仓库目标配置；本机原有 80 个目录未改变。

[精选清单](skills.yaml) · [80 项分类](curation.yaml) · [路由测试](../tests/core-routing.md)
