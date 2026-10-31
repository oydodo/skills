# Skill 生命周期：统一添加、升级与发布 SOP

**目标**：所有 Agent 按同一入口管理 Skill；允许不同来源使用不同实现，但不能每次临时改变分发流程。本文是维护规范，版本与设计交接以根目录 [CHANGELOG.md](../CHANGELOG.md) 为准。

## 1. 先判定来源类型

| 类型 | 适用条件 | 唯一维护源 | 示例 |
| --- | --- | --- | --- |
| 自研 Skill | 规则和正文由本仓库维护 | `skills/<name>/`，注册为 `source: maintained` | `crux-first-reasoning` |
| 原样引入的上游 Skill | 上游已有可用的 `SKILL.md` 及配套资源、许可清晰 | `upstream/<repo>` Git submodule 的**固定 commit**；`registry/skills.yaml` 指向选定子目录 | `wayfinder`、`visual-explainer` |
| 外部工具适配 Skill | 上游提供 CLI/MCP/软件，但没有直接可分发的同名 Skill，或需要本项目独立的工具使用说明 | `skills/<name>/`，注册为 `source: maintained`；在 references 中记录工具版本、安装和权限边界 | `codegraph` |

**不允许混用**：不能因为图省事把上游 Skill 复制进 `skills/` 再手工维护；也不能把工具适配说明假装成已安装的可执行工具。对上游 Skill 的微调优先使用 `description_override` 调整触发元数据，保持正文原样。确需改正文时，应明确转为 fork / maintained 并说明原因，而不是悄悄打补丁。

## 2. 新增 Skill：统一七步

1. **筛选**：记录用户场景、与现有 Skill 的区别、正例/反例触发、能力依赖和许可。是否精选以 `registry/curation.yaml` 为准。
2. **确定唯一来源**：自研/工具适配编辑 `skills/<name>/`；上游 Skill 使用 `git submodule add -b <branch> <url> upstream/<repo>`，选定并**固定具体提交**。仅通过 `.gitmodules` 声明分支不代表持续跟踪。
3. **登记**：在 `registry/skills.yaml` 添加一个精选条目（名称、来源、路径、分类、能力层）；必要时设置 `description_override`。更新 `registry/curation.yaml` 和 `profiles/core.yaml` 的相关条目，避免触发范围冲突。
4. **说明与许可**：更新 README、分发文档及受影响的 Plugin/Marketplace 描述和数量；上游 Skill 保留许可证、版本与 pinned commit；外部工具适配说明它**不会**自动安装二进制、MCP 服务或索引。
5. **测试**：至少验证 `SKILL.md`、元数据、资源、许可、正负触发用例与三端打包（原生 `.agents`、ChatGPT、Claude）。需要 Node、浏览器、CLI 或 MCP 的能力，应另外记录真实运行验收，不能用构建成功代替。
6. **版本记录**：先在根目录 `CHANGELOG.md` 创建**下一补丁版本**的说明（为什么引入、来源和固定版本、能力边界、未验证内容）。**不要手动修改 Plugin 版本或生成目录**。
7. **发布**：提交 PR → 通过 `Verify Plugin Build` → 合并 `main` → `Build and Publish Skill Plugins` 自动重建、递增版本、提交生成文件、发布三份 ZIP（包括通用 `.agents`）和 Release。再分别验证 ChatGPT / Claude 的 Marketplace 同步及实际触发。

## 3. 升级与移除：仍走同一条发布链

- **升级上游 Skill**：先读上游 diff、变更日志、许可证和依赖变化，再更新 submodule **gitlink**（如 `git -C upstream/<repo> fetch`、`git -C upstream/<repo> checkout <reviewed-commit>`，随后 `git add upstream/<repo>`）。若同一个 submodule 供多个 Skill 使用，要检查全部受影响条目。更新测试、`CHANGELOG.md`，走 PR/CI/发布。不要无审查地运行 `git submodule update --remote` 并直接推送生产。
- **升级自维护 Skill**：修改 `skills/<name>/`，按相同测试、Changelog、PR/CI/发布流程。
- **移除 Skill**：从 `registry/skills.yaml` 移除精选条目，更新盘点记录、描述、测试与 Changelog。仅当无人使用某个上游仓库时才删除对应 submodule；构建会移除生成包中的该 Skill。
- **仅改仓库文档**：如果未改变打包内容，可以不创建 Plugin 版本；如修改 `CHANGELOG.md` 或任何被打包来源，构建会将其视为内容变更，要求下一版本记录。

### 每周上游升级检测（已配置）

由 [`.github/dependabot.yml`](../.github/dependabot.yml) 启用 GitHub 原生 **Dependabot / `gitsubmodule`**，每周一 **09:00（Asia/Taipei）** 检查更新；不需要额外定时脚本、第三方 Bot 或长期 Token。仅监控 `registry/skills.yaml` 当前精选的七个上游 submodule；未精选的 `upstream/deepseek-harness` 不自动更新。通过 `tests/test_upstream_monitor.py` 防止两份清单漂移。

- Dependabot 在上游固定 commit 过期时提出**独立 PR**，更新父仓库记录的 gitlink；**不自动合并**，也不直接覆盖 `skills/`。
- **先审查变更，后合并**：查看从旧 SHA 到新 SHA 的选中 Skill 子目录、许可证与依赖（同一上游仓库可能供应多个 Skill），并核对 `SKILL.md` 的触发语义。需要时可运行 `git -C upstream/<repo> diff <old-sha> <new-sha> -- <selected-skill-path>`。
- 此更新模式以 `.gitmodules` 的分支为候选来源，**追踪新提交，不等于只追踪稳定 Release tag**。例如 Visual Explainer 原来是 v0.14.0 的固定提交，检测到 main 新提交后仍需人工核对其正式发布版本、许可证和兼容性；不应仅因 SHA 更新就宣称升级到新版本号。
- 当前发布流程的 **CHANGELOG 是硬门禁**：若新 gitlink 导致 Plugin 生成内容变化，Dependabot 的原始 PR 将因缺少下一版本的 Changelog 条目而无法通过 CI。审查者应补写版本说明、更新旧版本硬编码的测试断言（例如 Visual Explainer 的固定 SHA）并在 PR 中验证通过；这是刻意保留的审查环节，不是自动检测失效。
- 通过 PR 并合并 `main` 后，现有 `publish-plugins.yml` 才执行生成、版本递增、双 ZIP 和 Release。最后仍需独立确认两个 Web Marketplace 的同步与实际触发。建议在 GitHub Rulesets 中要求 PR 审查和 `Verify Plugin Build` 检查通过，避免跳过 Changelog 门禁。
- **不监控的来源**：`skills/` 中自维护的三个判断核心及 CodeGraph 工具适配 Skill，由本仓库直接维护；CodeGraph CLI 的新版本属于另一个工具升级决策，不等于 Submodule 更新。

**首次启用**：上述 Dependabot 配置需合并到默认分支 `main` 才会运行；配置生效后由 GitHub 管理定时检查，不依赖已打开的 ChatGPT/Claude 对话。请在仓库 **Insights → Dependency graph → Dependabot** 或 **Settings → Code security and analysis** 核实更新功能与任务日志（界面名称可能调整）。

## 4. 固定版本、Submodule 与自动更新的精确定义

```text
upstream repository (可随时发布新提交)
    -> upstream/<repo> (Git submodule，父仓库固定 gitlink commit)
    -> registry/skills.yaml (决定精选哪个 Skill，并覆盖触发元数据)
    -> scripts/build_plugins.py (同时生成 .agents/skills/ 与 plugins/oydodo-skills/skills/)
    -> GitHub Actions / Release (生成原生 Agents、Claude 与 ChatGPT ZIP)
    -> 各客户端 Marketplace 同步 / 用户安装 / 真实触发（独立验收）
```

- `git submodule update --init` **只检出父仓库固定的 commit**，不会自动升级到上游最新版。
- 上游更新 **不会**自行变成 `skills/` 或 Plugin 的内容；本仓库目前**未配置自动升级上游 gitlink 的机器人**。今后如要自动跟踪，优先采用“定期发现 → 提交 PR → CI → 审查合并”，而非无审查直推。
- `main` 中精选来源变化后，GitHub Actions **自动构建与发布**；构建机器人不能替代 Marketplace 同步或客户端触发验收。
- 只有 `skills/` 的自维护内容随本仓库编辑而变化；第三方正文位于 `upstream/` 并通过编译复制进生成包。**Codex/Pi/DSH 使用仓库 `.agents/skills` 原生目录优先**，不要与同名 Plugin Skill 同时启用。

## 5. 最小本地复现

```bash
python3 -m pip install PyYAML==6.0.2
python3 scripts/build_plugins.py --list-submodules | while IFS= read -r module; do
  git submodule update --init --depth 1 -- "$module"
done
python3 scripts/build_plugins.py --write
python3 scripts/build_plugins.py --check
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/package_plugins.py --platform all
```

`--write` 要求待发布的根目录 Changelog 与预计新版本匹配；`--check` 检查已生成文件与唯一来源是否一致。

## 6. 验收状态不能混为一谈

| 层级 | 完成标准 |
| --- | --- |
| 来源 | 选定 Skill、许可证和 gitlink / 自研正文已提交 |
| 构建 | PR 校验、通用 `.agents` 与双 Plugin ZIP 内容及版本一致 |
| 发布 | GitHub Release/tag 和三份 ZIP 已存在 |
| 同步 | 目标 ChatGPT / Claude 账户确实显示新版本 |
| 行为 | 实际任务的正例触发、负例不误触发、文件/工具能力可用 |

**任一层通过不代表后续层也通过。** 尤其不要根据 Marketplace 页面残留的旧错误提示推断 GitHub 当前构建失败。
