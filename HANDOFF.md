# Handoff — oydodo/skills（2026-10-31）

> 接手对象：本地 Codex / Pi / DSH Agent。本文件是**一次性交接**，不是新 Skill、全局指令或新的框架。以仓库实时内容和 `CHANGELOG.md` 为准；不要把本文的时间点当作持续有效的运行状态。

## 1. 用户的真实目标（主线）

构建并持续维护 **oydodo 的跨 Agent 精选 Skill 系统**。不是尽可能多装 Skill，而是用**少量、边界明确、经过实测、可持续升级**的 Skill，提升 Agent 的独立判断、关键问题识别、需求理解、编码质量与交付效率。

核心诉求：

1. **唯一事实来源**：精选清单和描述在 `registry/skills.yaml`；自维护 Skill 在 `skills/`；上游 Skill 使用可追踪、经过审查的 `upstream/` 固定提交。生成的各平台目录不得手工修改。
2. **跨端复用**：ChatGPT/Claude Web 用 Plugin；Codex **用户明确要求优先使用 `.agents/skills/`**；Pi 和 DSH 也优先复用通用 `.agents/skills/`。Pi Package 作为安装/更新手段，不应成为第二套源代码。
3. **受控持续更新**：Dependabot 发现第三方更新并提出 PR → 检查差异、测试和 CHANGELOG → 合并后自动生成/发布。固定 SHA 是已审核版本，不是永不更新，也不要无人审查地自动合并。
4. **实测优先**：GitHub 构建、Release、安装、运行时发现、实际触发是不同的验收层级；不能用构建成功代替客户端测试。
5. **保持轻量**：避免强制编排、重复 Skill、冗余配置、额外常驻上下文和过度工程化。

### 当前明确的纠偏

用户刚表示：**“我觉得偏离主线了。写个 handoff，让本地 agent 接手。”**

因此**立即停止**围绕 Hooks 做跨平台抽象、各端独立 Hook 适配层、桥接器或专门 Extension 的设计和开发。已存在的 Plugin Hook 保留即可；除非它实际阻断主线验收，**不要主动重构它**。上一轮关于“Codex Plugin 可能更方便”的判断只是条件性建议，不应推翻用户明确提出的 **Codex 优先 `.agents`**。

## 2. 已落地的仓库状态（截至本交接）

- GitHub: https://github.com/oydodo/skills
- `main` 当时 HEAD：`db645d9ad24780c9828efccebda26e21a01c7a13`（请接手时重新核对）
- 已发布 `v0.1.14`：https://github.com/oydodo/skills/releases/tag/v0.1.14
- 当前 **18 个独立精选 Skill**：**14 个第三方、4 个自维护**；具体以 `registry/skills.yaml` 为准，不要从本文件重造清单。
- `docs/skill-lifecycle.md`：统一新增、升级、测试、发布流程。
- `.github/dependabot.yml`：每周检查精选 Git Submodule，生成待审查 PR，不自动合并。
- `scripts/build_plugins.py`：从同一来源构建 `.agents/skills/` 与 `plugins/oydodo-skills/skills/`，并校验内容一致性。
- `scripts/package_plugins.py`：构建 `oydodo-skills-agents.zip`、`oydodo-skills-chatgpt.zip`、`oydodo-skills-claude.zip`。
- `package.json`：Pi Git Package，`pi.skills` 指向 `./.agents/skills`；理论安装方式为 `pi install git:github.com/oydodo/skills`，更新方式为 `pi update --extensions`，**尚缺真实 Pi 客户端验收**。
- `core/always-on.md` + `core/hooks.json`：现有轻量核心原则及 Plugin 专用 SessionStart Hook。Hook 脚本依赖 `PLUGIN_ROOT` / `CLAUDE_PLUGIN_ROOT`；不能当成可直接复制的原生独立 Hook。**本次不扩大 Hook 工作范围。**
- `retro` 与 `wayfinder` 保留显式调用限制；`diagnosing-bugs` 限复杂故障；`writing-for-agents` 限 Agent 可读指令。平台实际遵守情况需测试。

最近完成的 PR：[#8](https://github.com/oydodo/skills/pull/8) 更新监测规范、[#9](https://github.com/oydodo/skills/pull/9) Matt 三个 Skill、[#10](https://github.com/oydodo/skills/pull/10) 通用 `.agents`、[#11](https://github.com/oydodo/skills/pull/11) Pi Git Package。交接时查询未发现未合并 PR。

**CI 提醒说明**：PR #10 中两次旧 `Verify Plugin Build` 失败，分别是 Python import 路径与测试误要求自维护 Skill 有第三方 LICENSE；均已修复。最终 PR 验证与 v0.1.14 发布流水线成功。不要把历史失败邮件当作当前发布故障。

## 3. 尚未验证的现实问题（优先级由高到低）

**P0：本地真实使用路径是否成立。** 在可控的测试项目里验证 Codex、Pi（若已安装）、DSH（若已安装）的真实 Skill 发现：是否读取期望的 `.agents/skills`，能否看到 18 个、正确找到附属资源、是否存在旧目录/Plugin 的同名覆盖。至少分别跑 1 个正例和 1 个负例；对于用户显式调用的 Skill，验证未被普通任务误触发。**不可仅从目录存在推断 Agent 已成功加载。**

**P1：Pi Git Package 的安装/升级实测。** 先查看本机 Pi 版本和 `pi --help`/子命令帮助，确认当前发行版对 `package.json` 和 `pi update --extensions` 的支持；在隔离环境或测试项目进行 `pi install git:github.com/oydodo/skills`、`pi list`、升级检查，记录真实结果。不要直接覆盖用户全局已有 Skill 或制造同名双加载。

**P2：Codex 路径选型实证。** 以用户已决定的 `.agents` 优先为默认；如果原生发现、冲突处理、跨项目管理存在可复现的明显问题，再与 Plugin 做同任务比较（发现、版本、冲突、是否需要 Hook），以证据建议是否调整，而不是预设 Plugin 更好。

**P3：维护链端到端验收。** 验证 Dependabot 创建的真实升级 PR 能否被现有 CI 接纳；特别检查上游提交变化、固定 SHA 测试及 CHANGELOG 的版本门禁是否造成升级 PR 长期卡住。目标是“自动发现 + 可审查升级 + 自动发布”，不新增第二个更新系统。

**后置**：ChatGPT/Claude Web Marketplace 的安装版本、自动触发及同步测试，若本地 Agent 无账户/UI 授权则记录缺口，不虚构成功。

## 4. 建议的接手动作（先观察，再最小修改）

1. 在本地仓库执行 `git status --short`、`git log -1 --oneline`、`git remote -v`；**工作区有未提交修改时先保护，不要盲目拉取/覆盖**。在工作区干净、远端一致后更新 `main`。
2. 阅读 `README.md`、`registry/skills.yaml`、`docs/skill-lifecycle.md`、`docs/distribution.md`、`CHANGELOG.md` 最近两版和相应测试。不要为了读代码而重新复制第三方上游。
3. 若需要本地构建检查，先执行 `python3 scripts/build_plugins.py --list-submodules`，初始化其中列出的固定 Submodule，再运行 `python3 scripts/build_plugins.py --check`、`python3 -m unittest discover -s tests -p 'test_*.py' -v`。**不要先执行 `--write` 或修改生成物来掩盖差异**。
4. 先完成 **P0 或 P1 中当前机器实际具备条件的一项**；记录观察证据、准确的失败环节、成本最小的修复和正负回归测试。
5. 若确需改仓库：遵循 `docs/skill-lifecycle.md`，在分支/PR 中修改唯一来源及必要测试，更新 `CHANGELOG.md`（改变分发内容时），CI 通过后再合并发布。**不要无需求地增加新 Skill、Hook、管理器或配置层**。

## 5. 交付与回报要求

向用户用简短结构汇报：

- **已验证的事实**：测试的 Agent、实际版本、具体发现路径、成功/失败场景与证据。
- **主导问题**：是否真正阻断“精选 Skill 可安装、可更新、能正确触发”，不要泛化成整个 Agent 生态研究。
- **最小行动**：已完成的修复/PR（如有）、回归结果及目前还差哪一项真实验收。
- **停止条件**：核心路径已经可用且无关键冲突就收敛；不要继续扩展到 Hooks、Orchestrator、跨平台框架或无关插件设计。

**现在请从检查本地工作区和原生 Skill 发现开始，不要直接实现新的 Hook 方案。**
