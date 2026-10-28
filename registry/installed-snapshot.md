# 本机 Skills 分类清单

> 快照时间：2026-10-28；设备：Mac mini；目录：`~/.agents/skills/`。共 **80 个目录**，不包括 `.system`。这是盘点，不代表它们全部是已验证、互相独立或可公开的 Skill。
>
> 分类仅供发现和维护。**不修改本机目录，也不自动上传这些目录的源码。** 其中 Codas / DSH 属于项目限定的 Skill，请特别检查访问边界和内容安全。

| 领域 | 分类 ID | 数量 |
| --- | --- | ---: |
| 思考与需求澄清 | `reasoning` | 9 |
| 规划与协作 | `planning` | 4 |
| 软件架构与建模 | `architecture` | 4 |
| 编码、测试与 Git | `development` | 14 |
| 文档与技术语言 | `writing` | 3 |
| 界面设计与可视化 | `visual` | 7 |
| Agent 与 Skill 管理 | `agent` | 9 |
| 教学与个人效率 | `education` | 3 |
| Codas 项目专用 | `project-codas` | 10 |
| DSH 项目专用 | `project-dsh` | 17 |
| **合计** | | **80** |

### 1. 思考与需求澄清 (9)

- `grill-me`
- `grill-with-docs`
- `grilling`
- `interview-me`
- `product-brainstorming`
- `research`
- `to-questionnaire`
- `wait-what`
- `wayfinder`

### 2. 规划与协作 (4)

- `retro`
- `to-spec`
- `to-tickets`
- `triage`

### 3. 软件架构与建模 (4)

- `codebase-design`
- `codegraph`
- `domain-modeling`
- `improve-codebase-architecture`

### 4. 编码、测试与 Git (14)

- `code-annotator`
- `code-explainer`
- `code-review`
- `codex-appserver-doctor`
- `diagnosing-bugs`
- `git-guardrails-claude-code`
- `implement`
- `implement-spec`
- `migrate-to-shoehorn`
- `ponytail`
- `pr`
- `prototype`
- `setup-pre-commit`
- `tdd`

### 5. 文档与技术语言 (3)

- `technical-documentation`
- `technical-language`
- `technical-writing`

### 6. 界面设计与可视化 (7)

- `anatomy`
- `archify`
- `design-taste-frontend`
- `explore-recipes`
- `record-browser-gif`
- `remote-html-preview`
- `visual-explainer`

### 7. Agent 与 Skill 管理 (9)

- `agent-experience`
- `ask-matt`
- `find-skills`
- `handoff`
- `nopua`
- `setup-matt-pocock-skills`
- `wizard`
- `write-a-skill`
- `writing-for-agents`

### 8. 教学与个人效率 (3)

- `i-have-adhd`
- `scaffold-exercises`
- `teach`

### 9. Codas 项目专用 (10)

- `codas-accept`
- `codas-coordinate`
- `codas-design`
- `codas-implement`
- `codas-model`
- `codas-note-archive`
- `codas-ontology`
- `codas-prose`
- `codas-review`
- `codas-trim-cot`

### 10. DSH 项目专用 (17)

- `cordis-styling-nitpicking`
- `dsh-archive-agent-notes`
- `dsh-ci-test-reliability`
- `dsh-client-ui-ux`
- `dsh-code-review`
- `dsh-create-upgrade-guide`
- `dsh-doc`
- `dsh-error-handling`
- `dsh-find-simplifications`
- `dsh-merging-stacked-prs`
- `dsh-official-plugin-artwork`
- `dsh-pre-push-checks`
- `dsh-prose-standard`
- `dsh-responsive-ui`
- `dsh-speed-up-perf`
- `dsh-translate-docs`
- `dsh-trim-cot-leakage`

## 备注

- `grill-me`、`grill-with-docs` 等可能是调用入口，不等于独立、完整的实现。
- Codas 和 DSH 采用项目边界分组，方便与通用 Skill 区分；如需按功能再细分，可以在清单中增加标签而不移动原有路径。
- 第三方仓库来源、维护方式及实际采用范围以 [skills.yaml](skills.yaml) 为准。尚未核实来源的 Skill 不应直接生成 Git submodule。
- 主仓库的 `crux-first-reasoning` 是**已登记的自研 Skill**，并不在这次本机 80 个目录快照中。
