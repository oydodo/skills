# 本机 Skills：按领域与上游来源分类

> 快照时间：2026-10-28；实际本机仍有 **80 个** Skill 目录；以下是管理仓库的筛选清单，按要求排除了 **12 个 Codas 专用/相关目录**（10 个 `codas-*`、`codegraph` 和 `code-explainer`），剩余 **68 个**。没有删除或移动任何本机文件。
>
> 来源归类来自上游仓库对应的 `SKILL.md` 路径。名称与来源匹配不代表本地文件一定等于当前上游版本；Git submodule 的 Gitlink 记录具体版本。

## 来源汇总

| 来源 | 本机目录数 | 处理方式 |
| --- | ---: | --- |
| [Matt Pocock](https://github.com/mattpocock/skills) | 31 | 一个 submodule，逐项选取路径 |
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness/tree/master/.agents/skills) | 19 | Git submodule + Sparse Checkout，仅检出 `.agents/skills/` |
| 3 个既有来源 | 3 | 保留原 submodule |
| 其他来源 | 15 | [13 个已追溯公开来源、2 个本地定制未证实公开上游](other-sources.md)；`code-explainer` 在审计记录中但已排除 |
| **合计** | **68** | |

## 领域汇总

| 领域 | 分类 ID | 数量 |
| --- | --- | ---: |
| 思考与需求澄清 | `reasoning` | 9 |
| 规划与协作 | `planning` | 4 |
| 软件架构与建模 | `architecture` | 3 |
| 编码、测试与 Git | `development` | 13 |
| 文档与技术语言 | `writing` | 3 |
| 界面设计与可视化 | `visual` | 7 |
| Agent 与 Skill 管理 | `agent` | 9 |
| 教学与个人效率 | `education` | 3 |
| DSH 项目专用 | `project-dsh` | 17 |
| **合计** | | **68** |

## 领域明细

### 1. 思考与需求澄清 (9)

- `grill-me` — Matt
- `grill-with-docs` — Matt
- `grilling` — Matt
- `interview-me` — 已核实上游，已接入
- `product-brainstorming` — 已核实上游，待接入
- `research` — Matt
- `to-questionnaire` — Matt
- `wait-what` — Matt
- `wayfinder` — Matt

### 2. 规划与协作 (4)

- `retro` — Matt
- `to-spec` — Matt
- `to-tickets` — Matt
- `triage` — Matt

### 3. 软件架构与建模 (3)

- `codebase-design` — Matt
- `domain-modeling` — Matt
- `improve-codebase-architecture` — Matt

### 4. 编码、测试与 Git (13)

- `code-annotator` — 源自开源命令，当前为本机 Skill 包装
- `code-review` — Matt
- `codex-appserver-doctor` — 本地定制，公开上游未证实
- `diagnosing-bugs` — Matt
- `git-guardrails-claude-code` — Matt
- `implement` — Matt
- `implement-spec` — Matt
- `migrate-to-shoehorn` — Matt
- `ponytail` — 已核实上游且已接入
- `pr` — Matt
- `prototype` — Matt
- `setup-pre-commit` — Matt
- `tdd` — Matt

### 5. 文档与技术语言 (3)

- `technical-documentation` — 已接入
- `technical-language` — 已接入
- `technical-writing` — 已接入

### 6. 界面设计与可视化 (7)

- `anatomy` — 已核实上游，待接入
- `archify` — 已核实上游，待接入
- `design-taste-frontend` — 已核实上游，待接入
- `explore-recipes` — 历史上游已核实，待规划更新
- `record-browser-gif` — DSH
- `remote-html-preview` — 本地定制，公开上游未证实
- `visual-explainer` — 已核实上游，待接入

### 7. Agent 与 Skill 管理 (9)

- `agent-experience` — DSH
- `ask-matt` — Matt
- `find-skills` — 已核实上游，待接入
- `handoff` — Matt
- `nopua` — 已核实上游，待接入
- `setup-matt-pocock-skills` — Matt
- `wizard` — Matt
- `write-a-skill` — 已核实上游，当前本机文件与 Teaonly 版本一致
- `writing-for-agents` — Matt

### 8. 教学与个人效率 (3)

- `i-have-adhd` — 已核实上游，待接入
- `scaffold-exercises` — Matt
- `teach` — Matt

### 9. DSH 项目专用 (17)

- `cordis-styling-nitpicking` — DSH
- `dsh-archive-agent-notes` — DSH
- `dsh-ci-test-reliability` — DSH
- `dsh-client-ui-ux` — DSH
- `dsh-code-review` — DSH
- `dsh-create-upgrade-guide` — DSH
- `dsh-doc` — DSH
- `dsh-error-handling` — DSH
- `dsh-find-simplifications` — DSH
- `dsh-merging-stacked-prs` — DSH
- `dsh-official-plugin-artwork` — DSH
- `dsh-pre-push-checks` — DSH
- `dsh-prose-standard` — DSH
- `dsh-responsive-ui` — DSH
- `dsh-speed-up-perf` — DSH
- `dsh-translate-docs` — DSH
- `dsh-trim-cot-leakage` — DSH

## 维护边界

- 该文件是本机盘点的**筛选视图**，不是安装指令；其他来源的 15 个仍在筛选清单中，其中 ponytail 已作为 submodule 接入；没有复制其他目录源码，来源审查见 [other-sources.md](other-sources.md)。
- 本仓库对第三方 Git submodule 或稀疏克隆的固定 SHA 作版本管理；多 Skill 仓库仅采用列出的 Skill 路径。
- [正式登记的选用路径](skills.yaml) 包含 55 个来源已确认并实际接入的本机 Skill，以及 1 个本仓库自研 Skill。
