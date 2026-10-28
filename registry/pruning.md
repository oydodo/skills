# 剪枝 v2 — 收紧正式选用清单

本机 80 个 Skill 目录中暂选 **9 个**，另加自研 `crux-first-reasoning`，目标工作集共 **10 个**。

| 分类 | 数量 | 说明 |
| --- | ---: | --- |
| 第一层 · 全局规则 | — | Independent Judgment；常驻，不计入 Skill |
| 第二层 · 思维 | 1 | Crux-First Reasoning |
| 第三层 · 表达 | 3 | Technical Writing / Documentation / Language |
| 辅助工具 | 6 | 澄清、挑战、简化编码与工程任务 |
| Matt 未选中 | 27 | 不整体引入其工作流 |
| DSH 项目专用 | 19 | 仅保留上游，不进入默认工作集 |
| 其他候选 | 11 | 暂不选用 |
| 自研暂缓 | 2 | `codex-appserver-doctor`、`remote-html-preview` |
| Codas 排除 | 12 | 包括 `code-explainer` |

Matt **只选 4/31**：`grilling`、`domain-modeling`、`diagnosing-bugs`、`code-review`。不选 `grill-me` / `grill-with-docs` 包装入口、`ask-matt` 路由及 `to-spec → to-tickets → implement-spec` 整套工单流程。

**标准**：优先功能独特、跨项目复用且能改善任务结果的 Skill；重叠、过度流程化、只针对某个仓库/服务的 Skill 先退出精选名单。[完整分类见 curation.yaml](curation.yaml)。

**状态**：仅收紧 GitHub 的 `registry/skills.yaml`；上游 Git submodule 和本机安装不变。实际停用前先对目标客户端做触发验证，以可恢复方式迁出非选中目录。
