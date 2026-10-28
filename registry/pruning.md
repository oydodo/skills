# 剪枝第一轮：先减少默认能力，再删除冗余

## 基线

2026-10-28 本机 80 个目录，其中此前已从通用管理范围排除的 Codas 相关项 12 个。剩余 68 个按 [curation.yaml](curation.yaml) 做**不破坏安装的初步分流**：

| 状态 | 数量 | 解释 |
| --- | ---: | --- |
| Core（已在本机） | 6 | 与 GitHub 自研的 `crux-first-reasoning` 构成 7 个条件性核心 Skill |
| On-demand | 34 | 能力不重复或适用场景有限，保留但不属于默认核心 |
| Project-only / DSH | 19 | 仅在 DSH 相关项目中发现与调用 |
| Prune review | 7 | 有明确的重叠、薄包装或专用环境证据，候选剪枝 |
| Self-maintained hold | 2 | `codex-appserver-doctor`、`remote-html-preview`，按用户要求暂不碰 |
| **合计** | **68** | 均保留本机安装，尚未执行物理移除 |

此外 `code-explainer` 属 Codas 定制，已从通用池排除，仍作为第三个自研 Skill **暂不处理**。其他 Codas 项目 Skill 不属于本轮讨论范围。

## 首批有证据的剪枝候选

| Skill | 为什么值得剪枝 | 判断条件 |
| --- | --- | --- |
| `grill-me` | 7 行转发壳，仅调用 grilling；可改为直接使用 grilling。 | 与替代方案做真实任务 A/B；无独特收益才停用 |
| `grill-with-docs` | 7 行转发壳，组合 grilling 与 domain-modeling；仅确实需要同步产出 ADR/术语表时保留。 | 与替代方案做真实任务 A/B；无独特收益才停用 |
| `ask-matt` | Matt 套件内部路由器；与本仓库的轻量核心路由职责重叠。 | 与替代方案做真实任务 A/B；无独特收益才停用 |
| `write-a-skill` | 旧版 Skill 生成入口；与 writing-for-agents、平台 skill-creator 职责重叠，需比较替代方案。 | 与替代方案做真实任务 A/B；无独特收益才停用 |
| `migrate-to-shoehorn` | 专为 @total-typescript/shoehorn 迁移设计，不宜在通用技能池中默认暴露。 | 与替代方案做真实任务 A/B；无独特收益才停用 |
| `scaffold-exercises` | 要求 ai-hero-cli 课程仓库布局及 lint，脱离该项目价值有限。 | 与替代方案做真实任务 A/B；无独特收益才停用 |
| `explore-recipes` | 依赖 ShipSwift listRecipes 服务；不使用该服务时默认发现价值低。 | 与替代方案做真实任务 A/B；无独特收益才停用 |

优先处理 `grill-me` 与 `ask-matt`：它们不是不可替代的能力，更像是对其他 Skill 的转发和路由。其次针对 `write-a-skill`、`explore-recipes` 等验证是否还存在实际使用场景。**`grill-with-docs` 有组合产物价值，不应仅凭文件只有七行就直接删掉。**

## 第二轮尚不剪的领域

- **表达**：`technical-writing`、`technical-documentation`、`technical-language` 职责相邻但输出对象不同；让路由先减少并发启用，再决定是否合并。
- **方案访谈**：`interview-me` 与 `grilling` 方向不同（发现需求 vs 挑战已有方案），暂不互相替代。
- **可视化**：`archify`、`visual-explainer`、`anatomy` 等输出方式不同，需通过真实案例比较。
- **编码安全**：`ponytail` 的“最简”不能替代测试、边界检查和风险评审；`nopua` 的触发与用户压力管理需单独观察。

## 停用门槛（应用到本机前）

1. 记录至少一个真实场景、一次触发及当前结果；没有使用数据时标记为“候选”，而不是“已证明无用”。
2. 用 [测试样例](../tests/core-routing.md) 验证核心能解决需求，再用对应专用任务检验候选是否还有独特价值。
3. 通过“停用后质量无明显下降 + 有可回退路径”两个条件，才把候选移出全局发现目录；上游 Git submodule 和来源清单仍保留。
4. 如需执行本机剪枝，先备份目录/软链接映射并选择可恢复的迁移，而非直接删除。**本轮只提交分类和决策，不做物理删除。**

GitHub 仓库保留所有上游引用，`profiles/core.yaml` 与 `registry/curation.yaml` 目前只是**目标配置**，不会自动更改 `~/.agents/skills`。
