# 剪枝 v2 — 收紧正式选用清单

本机 80 个 Skill 目录中暂选 **9 个**，另加自研 `crux-first-reasoning`，目标工作集共 **10 个**。

| 层 | 数量 | 说明 |
| --- | ---: | --- |
| 核心 | 4 | 判断、需求澄清、方案挑战、编码最简 |
| 专项 | 6 | 领域建模、故障诊断、代码审查、三类写作 |
| Matt 未选中 | 27 | 避免全套工作流和工单/特定项目依赖 |
| DSH 项目专用 | 19 | 仅保留上游，不进入默认工作集 |
| 其他候选 | 11 | 先不选中 |
| 自研暂缓 | 2 | `codex-appserver-doctor`、`remote-html-preview` 暂不处理 |
| Codas 排除 | 12 | 包括自研 `code-explainer`，暂不处理 |

Matt **只选 4/31**：`grilling`、`domain-modeling`、`diagnosing-bugs`、`code-review`。不选 `grill-me` / `grill-with-docs` 包装入口、`ask-matt` 路由及 `to-spec → to-tickets → implement-spec` 整套工单流程。

**标准**：优先功能独特、跨项目复用且能改善任务结果的 Skill；重叠、过度流程化、只针对某个仓库/服务的 Skill 先退出精选名单。[完整分类见 curation.yaml](curation.yaml)。

**状态**：仅收紧 GitHub 的 `registry/skills.yaml`；上游 Git submodule 和本机安装不变。实际停用前先对目标客户端做触发验证，以可恢复方式迁出非选中目录。
