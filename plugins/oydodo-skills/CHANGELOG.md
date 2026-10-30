# Changelog

本文件是 `oydodo/skills` 的**版本化设计交接记录**，供 Claude、Codex、ChatGPT 及后来接手的 Agent 阅读。它说明**改变了什么、为什么改变、哪些边界不能丢**；不是每次会话都必须加载的系统提示词。

- **唯一维护源**：仓库根目录 `CHANGELOG.md`；发布时复制到 Plugin 根目录，供安装后的 Claude Code、Codex 等按需查阅。
- **版本对应**：以 [GitHub Releases](https://github.com/oydodo/skills/releases) 和已合并 PR 为准；`v0.1.9` 引入版本记录分发；此后每版按本文件记录变更。
- **不要混淆**：代码合并、CI 通过、ZIP 发布、Marketplace 已同步、Agent 实际触发，是不同的验收层级。

## [0.1.11] - 2026-10-30

### Added — Agent 可视化汇报能力（Visual Explainer）

- 从 MIT 开源的 [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) 引入 **v0.14.0**，固定 Git commit `5f378868e0ea745a6284b51e710c390f0c76f72c`，作为第 **15 个独立 Skill**。通过 Git submodule 管理版本，保持 upstream `SKILL.md`、HTML 渲染 kit、模板与参考文件原样；构建时复制至 ChatGPT/Codex 和 Claude 两套 Plugin 包，保存 MIT 和随附第三方许可证。
- 适用于可视化解释、架构/流程、方案比较、审查结果、研究与项目进展回顾、数据图表及演示页面。首屏优先呈现关键结论及图示，让读者理解事实、关系、变化与下一步，而非堆砌装饰性图形。
- 在 `registry/skills.yaml` 使用受控的 **description_override**：仅在用户明确要求可视化，或任务与交付场景确实需要视觉表达时触发；避免普通答复、简短进展、简单表格无端变成 HTML。提供选择与降级说明，不修改上游 Skill 正文。
- 从精选清单的 `not_selected.other` 移出此前盘点过的 `visual-explainer`；精选数 **14 → 15**，固定版本第三方 **10 → 11**，自维护 Skill 仍为 **4**；三个核心判断 Skill 的职责和常驻 Hook 均不变。

### Compatibility and verification

- 本地 Node + 文件系统允许使用内置 `kit/render.mjs` 输出自包含 HTML；浏览器可用时进行视觉检查。**Web Plugin 的 Skill 安装不代表浏览器/Node/本地文件执行权限自动开放**；缺少产物能力时选用客户端原生图表/流程图等安全降级，不虚构 HTML 文件或已打开的浏览器。
- 发布后需分别验证真实 Agent 的触发、HTML 输出和可读性。GitHub 构建、文件存在和静态/无浏览器渲染测试仅证明分发/基本渲染，不证明所有客户端的自动触发、文件打开和渲染质量。

## [0.1.10] - 2026-10-30

### Added — 开源 CodeGraph 作为第 14 个按需 Skill

- 增加 [`codegraph`](skills/codegraph/SKILL.md)：面向跨文件调用链、函数依赖、变更影响范围、受影响测试与代码理解的**可选工具适配 Skill**。它采用独立于三个核心判断 Skill 的触发边界。
- 技术来源为 MIT 开源的 [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)，按文档固定上游 **v1.6.2**（commit `6560052a6f856855d3f71eee838fd66ccfa4285d`）；仅维护轻量 Agent 用法指导，不复制整套 CodeGraph 应用，也不自动升级第三方工具。
- 更新精选注册表、分类、Plugin 元数据、双平台发布范围与校验测试：从 **13 个 Skill 扩展为 14 个**，其中三个仍是核心判断 Skill，第 14 个是工具适配层，不改变全局常驻原则。
- 原精选记录里排除过的 Codas 项目专用 `codegraph` 与本次新增的通用开源 CodeGraph 并非同一个 Skill；在 `registry/curation.yaml` 中保留历史排除含义并明确区分。

### Boundaries

- **Skill 不是工具本体**：安装 Plugin 不会安装 CodeGraph CLI、配置 MCP 服务器、修改 Agent 全局设置或为任意仓库构建索引；本地使用前需要按授权完成工具部署和 `codegraph init`。
- 不把 CodeGraph 加进 `core/always-on.md` / SessionStart Hook；需要时再触发，简单任务正常直接执行。CLI、MCP、索引不可用或 Web 环境无法访问本机时，使用普通仓库检索方法继续工作，不因可选工具缺失中止任务。
- 发布构建和静态检查**不构成**真实 CodeGraph CLI/MCP 使用效果或跨客户端自动触发的证明；需后续以实际仓库任务分别验证。

## [0.1.9] - 2026-10-30

### Added — 正式版本交接

- 新增根目录 `CHANGELOG.md`：记录近期核心方法的演进依据，明确跨平台 handoff 的设计契约。
- 构建流程将其打包为 Plugin 根目录的 `CHANGELOG.md`，随 ChatGPT/Codex 与 Claude 两份分发包提供；`core/always-on.md` 只保留轻量常驻规则及此文档的按需入口，不注入整份历史。
- 后续涉及 Plugin 内容的版本发布，要求更新对应版本的变更记录；打包及 CI 校验版本号和记录一致性。GitHub Release 使用对应版本的 Changelog 内容，而不是泛泛的固定发行说明。

### Compatibility

- **没有修改三个核心 Skill 的方法论正文**；这次是把既有决定正式化并接入分发与发布链路。

## [0.1.8] - 2026-10-30

### Added — Plugin 内的轻量常驻核心（[PR #4](https://github.com/oydodo/skills/pull/4)）

- `core/always-on.md` 汇总独立判断、主要矛盾优先、关键不确定性从属、关键论证、系统视角与适度行动，并附三个核心 Skill 的本地路径及 GitHub 链接。
- 新增可选 `SessionStart` Hook（`startup|resume|clear|compact|fork`），在支持的**本地运行时**按需注入；不把完整 Skill 全部塞入上下文。
- **Fail-open**：规则文件缺失、不可读或为空时，静默跳过且退出成功，避免 Agent 因辅助指引失效而无法启动。构建阶段则对缺失/无效配置严格报错。
- Plugin 构建、双平台 ZIP、CI 与 Hook Shell 级验证通过；**不等于**已在真实 Codex/Claude Code 客户端验证信任、启动和压缩后的注入。

### Boundaries

- Hook 只用于**辅助判断**，不能承担安全拦截职责；fail-open 不应套用于安全控制。
- **ChatGPT Web / Claude Web 安装 Plugin 不等于全局常驻**：Web 的 Skill 依然按需调用；本地生命周期 Hook 不自动运行于网页会话。

## [0.1.7] - 2026-10-30

### Changed — 全仓定位与评测对齐（[PR #2](https://github.com/oydodo/skills/pull/2)、[PR #3](https://github.com/oydodo/skills/pull/3)）

- 将根目录 README、`core/README.md`、`profiles/core.yaml` 及 Skill 元数据对齐为：**先辨识主要矛盾和主次关系，再检查可能改变判断的关键不确定性**。
- `philosophical-foundation` 的「执本」与核心 Skill 分工不再把“高影响、证据薄弱的假设”置于主要矛盾分析之前。
- 修订 `crux-first-reasoning/references/evaluation.md` 的案例、评分准则和说明：验证是否识别主导制约、说明次要因素、呈现决定性证据并帮助读者理解；旧评分须按新准则重新评估，不能直接比较。
- 保留历史测试日志作为历史事实，不因新方法论而追改过去记录。

## [0.1.6] - 2026-10-30

### Changed — Crux-First 的根本转向（[PR #1](https://github.com/oydodo/skills/pull/1)）

- **旧路径（不再作为首要方法）**：“先找后果重大但证据薄弱的假设，优先验证它。”
- **新路径（现行）**：明确用户目标与现实差距 → 识别当前主导矛盾 / 关键制约及主次结构 → 评估能改变判断的关键未知 → 用证据与关系解释结论及可执行含义。
- 主要矛盾是相对于**目标、阶段和证据**的主导制约，不等于最不确定的假设、最显眼的症状，也不必是唯一的根因。
- 对报告、审计、调研及复杂取舍，**解释“为什么它重要、为什么其他因素暂居次要”与结论同样重要**。简单任务不强制复杂分析。

## Design contract — 给 Claude 等后续 Agent 的交接

**一条核心链路**：`目标与差距 → 主要矛盾及主次关系 → 关键不确定性与验证 → 证据链、行动和条件变化`。

### 三个自研核心，各司其职

1. [Philosophical Foundation](skills/philosophical-foundation/SKILL.md)：系统、联系、矛盾、变化、二阶效应、可逆性、反馈、简化与知止。属于项目的 **L0 方法论**，不是平台 system-role 权限。
2. [Independent Judgment](skills/independent-judgment/SKILL.md)：证据纪律、建设性质疑、诚实区分事实与未知；**不为反对而反对**，尊重用户知情后的合理选择。
3. [Crux-First Reasoning](skills/crux-first-reasoning/SKILL.md)：面对复杂诊断、审计、调研或决策，识别主导制约，解释主次与决定性证据，再决定验证什么；让用户**理解判断**，而非只收到答案。

这些是**独立 Skill**，不是一个强制的三段式执行工作流。其它精选 Skill（如 `interview-me`、`grilling`、`wayfinder`、`ponytail`）仍按真实任务触发；不要因为“核心”就让简单查询也走完整流程。

### 维护、分发与验收边界

- **维护源**：三个核心判断 Skill 和自维护适配 Skill 均改 `skills/<name>/`；常驻摘要改 `core/always-on.md`；Hook 改 `core/hooks.json`；精选和触发描述改 `registry/skills.yaml`；**变更原因和版本记录改本文件**。
- **生成文件**：`plugins/oydodo-skills/{skills,core,hooks}/` 与 Plugin 内 `CHANGELOG.md` 均由构建生成，**不要手工维护第二份**。
- **评测**：正例需观察复杂任务是否抓住主要矛盾、展示主次与依据；反例需检查简单任务能否直接完成。不能仅通过 Agent 自述、构建成功或 ZIP 存在宣称行为有效。
- **Web 同步状态**：GitHub 发布成功不保证 ChatGPT/Claude Web Marketplace 已同步。账户授权、导入器验证与 Hook 的本地行为应分别排查，不能从旧的提醒文本推断同步根因。

后续如果需要改变以上设计契约，请**先说明要推翻的决策、支持证据和影响范围**，再更新相关 Skill、评测与本 Changelog；避免在一处悄悄改回旧方法。
