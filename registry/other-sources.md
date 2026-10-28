# 其他来源：本机 Skills 上游核实记录

对之前列出的 **16 个候选目录**逐项检索本机 SKILL.md、公开仓库和历史版本；本表保留一个已排除项以追溯原因。

- **13 个可追溯公开上游**：包括直接匹配、明确的衍生改写或公开历史版本。其中 `ponytail` 和 `interview-me` 已通过 Git submodule 接入；其余均仅记录来源，**不等于已安装新版本或加入主仓库**。
- **3 个未找到可验证的公开上游**：都含本机定制特征；不能据此推断“互联网上不存在源码”。
- **1 个排除项**：`code-explainer` 带 Codas authority/codegraph 专用约束，依此前“去掉 Codas Skill”的要求从主清单排除，但保留于本来源审计表。
- 不把同名但用途不同的 Skill 认定为原始来源。不在本仓库上传第三方源码或含本地机密的定制脚本。

| Skill | 领域 | 核实结论 | 对应来源 / 补充说明 |
| --- | --- | --- | --- |
| `interview-me` | 思考与需求 | **来源确认 / 已接入** | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/main/skills/interview-me)：本机正文与该 Skill 一致 |
| `product-brainstorming` | 思考与需求 | **来源确认** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management/skills/product-brainstorming)：描述、正文一致 |
| `code-annotator` | 编码 | **衍生来源确认** | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit/blob/main/plugins/code-explainer/commands/annotate.md)：本机剥离 frontmatter 后正文逐字一致；原始形式是命令文件，不是独立 Skill |
| `code-explainer` | 编码 | **本地 Codas 定制 / 已排除** | 本机 Skill 包含 `codas:design-contract`、`codas authority`、`codegraph` 专用命令；未找到对应公开上游；不再计入通用管理清单 |
| `codex-appserver-doctor` | 编码 | **本地定制 / 公开上游未证实** | 针对本机 Codex daemon 与升级故障；包含本地绝对路径及专属健康检查脚本；未发现正文对应的开源 Skill |
| `ponytail` | 编码 | **来源确认 / 已接入** | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/main/skills/ponytail)：本仓库已有 submodule；不覆盖本机旧版本 |
| `anatomy` | 可视化 | **来源确认** | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)：本机 Git remote 指向该仓库 |
| `archify` | 可视化 | **来源确认** | [tt-a1i/archify](https://github.com/tt-a1i/archify/tree/main/archify)：对应 Skill 目录 |
| `design-taste-frontend` | 可视化 | **来源确认** | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/main/skills/taste-skill)：名称、研究资料和设计方法对应；上游版本持续变化 |
| `explore-recipes` | 可视化 | **历史来源确认** | [signerlabs/shipswift-skills 历史版本](https://github.com/signerlabs/shipswift-skills/blob/fdc597554648f33e8d54a0109465da2a016c8e9b/skills/explore-recipes/SKILL.md)：去除 frontmatter 后本机正文逐字一致；当前主分支已移除该独立目录 |
| `remote-html-preview` | 可视化 | **本地定制 / 公开上游未证实** | 针对当前 Codex Remote 会话的桌面/手机 HTML 交付、Base64 与附件机制；未发现对应公开 Skill |
| `visual-explainer` | 可视化 | **来源确认** | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer/tree/main/plugins/visual-explainer)：本机旧版本与上游名称、描述一致 |
| `find-skills` | Agent 管理 | **来源确认** | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)：与本机描述一致 |
| `nopua` | Agent 管理 | **来源确认** | [wuji-labs/nopua](https://github.com/wuji-labs/nopua)：本机引用官方主页，版本较旧 |
| `write-a-skill` | Agent 管理 | **来源确认，存在同源流传版本** | [Teaonly/SKILL.mk/examples/write-a-skill](https://github.com/Teaonly/SKILL.mk/tree/main/examples/write-a-skill)：本机 SKILL.md 与该文件**完全一致**；[Matt Pocock 历史版本](https://github.com/mattpocock/skills/blob/221ffca96736afefdc08ca7cf0b3965e9ea83f41/skills/productivity/write-a-skill/SKILL.md) 也存在相近实现，但当前 Matt 主分支已无此路径 |
| `i-have-adhd` | 个人效率 | **来源确认** | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd/tree/main/skills/i-have-adhd)：名称、description 一致 |

## 接入建议

- **可直接追踪的上游**：按各原仓库独立引用，或用已经接入的上游 submodule 选择对应 Skill 子目录；先核实当前最新目录。
- **历史版本或从命令包装的 Skill**（`explore-recipes`、`code-annotator`）：不能简单把当前主分支 submodule 中的路径当作可用 Skill；需要保留历史 commit 或维护本地最小包装，避免断链。
- **没有公开对应版本的定制 Skill**（`codex-appserver-doctor`、`remote-html-preview`）：仅在明确安全边界与敏感信息审查后，考虑作为自研 Skill 维护。
- 已排除的 `code-explainer` 不上传、不加入本仓库正式登记表。
