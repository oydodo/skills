# Changelog

本文件是 `oydodo/skills` 的**版本记录**，供 Claude、Codex、ChatGPT 及后来接手的 Agent 阅读。它说明每一版**改变了什么、为什么改变**；现行的规矩见根目录 [AGENTS.md](AGENTS.md) 和各目录的 README。它不是每次会话都必须加载的系统提示词。

- **唯一维护源**：仓库根目录 `CHANGELOG.md`；发布时复制到 Plugin 根目录，供安装后的 Claude Code、Codex 等按需查阅。
- **版本对应**：以 [GitHub Releases](https://github.com/oydodo/skills/releases) 和已合并 PR 为准；`v0.1.9` 引入版本记录分发；此后每版按本文件记录变更。
- **不要混淆**：代码合并、CI 通过、ZIP 发布、Marketplace 已同步、Agent 实际触发，是不同的验收层级。

## [0.1.17] - 2026-11-14

### Added — 自维护写作 Skill `crux-first-writing`（18 → 19）

- 新增 `skills/crux-first-writing/`：写或改“讲某样东西是什么”的文字时，先从它在整体里的位置找出本质，用一句正面的话说出，再从本质展开全文；逐句检验“这句是否在说对象现在的性质”，说被否决做法或旧版本的句子移到决策记录或 CHANGELOG；每次修改都从本质重写受影响的整段。附 `references/evaluation.md`。
- 情景：Codas 本体里 link 的定义四句话全在讲它不是什么、不做什么，没有说出本质。查下来，文档在逐条反馈中被逐句修补，每做一次减法就留下一句告别句，写成了旧版的差分。`crux-first-reasoning` 管判断，触发条件是决策和诊断，且跳过文字修改，写定义时不会加载；现有写作 Skill 只零散地管“不是X而是Y”这类句式。
- 配合顺序：`crux-first-reasoning`、`independent-judgment` 先定什么是真的、什么是主要的；本 Skill 定本质和组织；`technical-documentation`、`technical-writing`、`technical-language`、`writing-for-agents` 再管文体和措辞。
- 未验证：Agent 是否在写定义、改文档时实际触发本 Skill，以及有无对比的效果。

## [0.1.16] - 2026-11-13

### Changed — 构建只管自己生成的条目

- `scripts/build_plugins.py` 和 `scripts/package_plugins.py` 现在只检查、覆盖、打包 `.agents/skills` 与 `.agents/licenses` 里由注册表生成的条目（按本次生成和上一次生成的名单），不再把整个目录当作自己的。别的工具放进这些目录的东西，构建不报“不一致”，也不会删除，发布的 ZIP 也不含它们。
- 情景：Codex 只凭 Codas 安装说明往本仓库安装时，在“Skill 要放进 `.agents/skills/`，而该目录由构建生成并整体检查”处停下并请维护者定归属。维护者的判断：构建本来就不该碰自己范围之外的东西，所以改构建，而不是给 `codas-*` 开例外。
- 影响：`package.json` 里 Pi 的 skills 路径指向整个 `.agents/skills`，所以用 Git 包安装本仓库的 Pi 用户，装了别的工具的 Skill 后也会一并拿到。这是已知代价，未做处理。

## [0.1.15] - 2026-11-09

### Changed — 现行规矩回到仓库各处，CHANGELOG 只记版本

- 删除原来文末的 “Design contract” 一节。它写的是一直有效的规矩，放在版本记录里，Agent 要从历史条目中翻找；规矩一改，又会和旧版本的说法对不上。内容搬到：根目录 `AGENTS.md`（只改源头、“做好了”分层、新旧规矩冲突先比情景），`skills/README.md`（三个核心各自独立、怎样算改好了），`core/README.md`（常驻提醒的边界）。“想问题的顺序”本来就写在 `crux-first-reasoning` 正文里。
- 新增 `PRODUCT.md`（方向、取舍、不做什么、成功标准），`AGENTS.md` 与只引用它的 `CLAUDE.md`（新会话的 Agent 进门先读），`skills/README.md`、`scripts/README.md`（说明这两个目录是什么）。
- 情景：在本仓库试用 Codas。仓库已经写有目标、决定和流程，但新开会话的 Agent 没有一个会主动去读的入口。

### Compatibility

- 没有修改任何 Skill 正文。随插件分发的 `CHANGELOG.md` 不再包含设计契约；契约本来是写给维护本仓库的 Agent，这些规矩现在在仓库的 `AGENTS.md` 和各 README 里。

## [0.1.14] - 2026-10-31

### Added — Pi Git Package 批量安装与更新

- 新增仓库根目录 `package.json`，在 `pi.skills` 声明 `./.agents/skills`：Pi 现在可以通过 `pi install git:github.com/oydodo/skills` 将当前 18 项精选 Skill 作为**一个 Git Package** 安装，使用 `pi update --extensions` 批量更新安装的 Package。
- Pi Package 仅声明已有的生成目录，无专属 Skill 复制、Extension、`npm scripts` 或额外服务；一套 `registry/skills.yaml` 继续生成原生 `.agents` 和 ChatGPT / Claude Plugins。
- 保留 `.agents/skills` 作为 Codex / Pi / DSH 跨项目原生兼容入口；Codex Plugin 依然作为安装、统一更新及可选可信 Hook 的管理层。两者加载相同 Skill 正文，不应声称 Plugin 自动提高推理质量。
- 新增配置契约测试和 Pi 更新文档。Git 安装不附 `@tag` / `@commit` 才能跟踪主分支；`pi update` 只更新 Pi CLI，Package 统一更新使用 `pi update --extensions`。本机安装、实际路由及重复 Skill 冲突仍需在 Pi 客户端验收。

## [0.1.13] - 2026-10-31

### Added — 通用 Agent Skills 分发（Codex / Pi / DSH）

- 将 `.agents/skills/<name>/SKILL.md` 及其脚本、参考文件、`agents/openai.yaml` 设为 **Codex、Pi 和 DeepSeek Harness 的优先本地发现入口**；按标准目录命名，兼容这三个 Agent 的原生项目级 Skill 扫描，不创建重复的 `.pi/skills`、`.dsh/skills` 或 `.codex/skills`。
- `scripts/build_plugins.py` 从唯一的 `registry/skills.yaml`、自维护 `skills/` 和固定的 `upstream/` 提交构建同一棵 Skill 树，同时生成根目录 `.agents/{skills,licenses,SOURCES.md,CHANGELOG.md}` 和原有 `plugins/oydodo-skills/`。两份是**生成的分发产物**，而不是两套可人工编辑的源代码；构建检查可检测两者不一致。
- 新增 `oydodo-skills-agents.zip`，可直接解压到任意项目根目录（或用户 Home）供 Codex、Pi、DSH 识别，并保留单独的第三方许可、来源和版本变更记录。与 ChatGPT / Claude 两份 Plugin ZIP 共用一次生成、同版本测试和 GitHub Release。
- 保留 `.agents/plugins/marketplace.json` 供 ChatGPT Marketplace 使用；**通用 ZIP 不包含 Marketplace 配置、Plugin Hooks 或自动执行脚本**。现有 Plugin 安装/分发路径仍兼容，不要求网页端理解原生本地文件系统。

### 兼容与验收边界

- 推荐 Codex **优先使用 `.agents/skills`** 的原生发现；在同一个作用域内避免同时启用同名 Plugin Skill 和原生 Skill，防止重复出现。Pi 需要项目已信任，DSH 的 `.dsh/skills` 优先级高于 `.agents/skills`，如果本机已有同名 Skill 应先处理覆盖关系。
- 保留 `retro`、`wayfinder` 的 `disable-model-invocation: true` 和 Codex `allow_implicit_invocation: false`；不增加新的常驻 Hook。某些平台/版本可能不支持全部扩展字段，需单独验证实际触发和插件生命周期。
- CI 可验证目录、资源、许可、ZIP 格式与内容一致，但 **Codex/Pi/DSH 的真实运行时发现，以及 GitHub Release 至本机的更新同步，仍须在实际客户端独立验收**。本轮仅建立发行能力，不自动覆盖用户电脑上的旧 Skill。

## [0.1.12] - 2026-10-30

### Added — Matt 的 Agent 质量闭环（15 → 18）

- 从已固定的 [mattpocock/skills](https://github.com/mattpocock/skills) Submodule commit `59db609eb1e18aaf59b63284d0e52255aff0c63c` 精选三个原版 Skill（不升级整个上游，也不复制或改写正文）：`writing-for-agents`（Agent 指令质量）、`diagnosing-bugs`（复杂故障的可复现反馈闭环）、`retro`（基于证据的 Agent 会话复盘）。
- 精选数量 **15 → 18**；第三方 **11 → 14**、自维护 **4** 项不变。三个新增 Skill 均按需使用，不写入全局常驻 Hook；`retro` 必须用户主动调用，`diagnosing-bugs` 不用于常规小修，`writing-for-agents` 不用于普通文稿。
- 两类 Agent 指令相关 Skill 可以配合使用：`retro` 原版引用 `writing-for-agents`，全部参考文件、脚本和 MIT License 随 Plugin 打包；新增目录与触发边界的静态测试。

### Fixed — Claude / Codex 的隐式调用语义

- 修复生成器只保留 `name` / `description`，导致上游 `disable-model-invocation: true` 丢失的问题（已选中的 `wayfinder` 也受影响）。今后保留该用户主动调用标志，并确保对应 `agents/openai.yaml` 中 `policy.allow_implicit_invocation: false`；源 Skill 正文保持不变。
- 该字段的跨客户端支持存在差异：GitHub Actions、压缩包和静态断言验证不等于 ChatGPT Web / Claude Web 或本地真实触发验收。使用前应分别做显式调用与非匹配任务的负例验证。

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
