# Skills

个人 AI Skills 的统一管理仓库。自研 Skill 在此维护；**所有第三方来源统一采用 Git submodule** 固定上游版本，按需结合 Sparse Checkout 和 Partial Clone。使用 [registry/skills.yaml](registry/skills.yaml) 精确声明已采用的子目录。

## 我们的 Core v1 · 精简、分工、可验证

**1 条始终生效的独立判断准则 + 7 个按任务触发的 Skill**，其中 `crux-first-reasoning` 自研，其余直接使用上游。核心不是新的超级 Skill，不强迫每次运行整个流程。

- [核心职责和触发路由](core/README.md)
- [声明式核心 Profile](profiles/core.yaml)（**尚未自动应用到本机**）
- [第一轮剪枝分析](registry/pruning.md) · [68 个目录分流](registry/curation.yaml)
- [行为验收样例](tests/core-routing.md)

**初步分流**：6 个本机核心 / 34 个按需 / 19 个 DSH 项目专用 / 7 个剪枝候选 / 2 个自研暂停；自研 `crux-first-reasoning` 在 GitHub 中单列。**候选未删除，本机环境未改变**。

## 领域分类

| 领域 | 本机选用目录数 |
| --- | ---: |
| 思考与需求澄清 | 9 |
| 规划与协作 | 4 |
| 软件架构与建模 | 3 |
| 编码、测试与 Git | 13 |
| 文档与技术语言 | 3 |
| 界面设计与可视化 | 7 |
| Agent 与 Skill 管理 | 9 |
| 教学与个人效率 | 3 |
| DSH 项目专用 | 17 |
| **合计** | **68** |

[查看全部本机分类清单](registry/installed-snapshot.md)（原有 80 个目录中，Codas 项目相关的 12 个已从本仓库管理范围排除；不会改动本机安装）。

## 按上游仓库管理

| 来源 | 本机对应数量 | 位置 | 维护 |
| --- | ---: | --- | --- |
| [Matt Pocock](https://github.com/mattpocock/skills) | 31 | `upstream/mattpocock-skills` | submodule，main |
| [DeepSeek Harness Skills](https://github.com/deepseek-ai/deepseek-harness/tree/master/.agents/skills) | 19 | `upstream/deepseek-harness/.agents/skills` | Git submodule + Sparse Checkout，Gitlink 固定版本 |
| [Technical Writing](https://github.com/luoling8192/technical-writing) | 1 | `upstream/technical-writing` | submodule |
| [Technical Documentation](https://github.com/wondelai/skills/tree/main/technical-documentation) | 1 | `upstream/wondelai-skills/technical-documentation` | submodule（**只使用此子目录**） |
| [Technical Language](https://github.com/jjsnack/technical-language-skill) | 1 | `upstream/technical-language-skill` | submodule |
| [Ponytail](https://github.com/DietrichGebert/ponytail/tree/main/skills/ponytail) | 1 | `upstream/ponytail/skills/ponytail` | submodule，仅采用此子目录 |
| [Interview Me](https://github.com/addyosmani/agent-skills/tree/main/skills/interview-me) | 1 | `upstream/addyosmani-agent-skills/skills/interview-me` | submodule，仅采用此子目录 |
| 其他来源（含 Ponytail） | 15 | [逐项来源审查（保留 1 项已排除记录）](registry/other-sources.md) | 13 个已核实（2 个已接入）；2 个本地定制未找到公开上游 |

**注意：上游同名 Skill 只代表来源路径得到确认，不证明本机版本与所固定的 Git commit 相同。** 仓库保留 `upstream` 子模块，实际使用哪一项由 `registry/skills.yaml` 中的 `skill_path` 指定。

> 其他来源的 16 个本机 Skill 已独立列于 [来源审查表](registry/other-sources.md)；`ponytail` 和 `interview-me` 已确认并接入，其余已核实来源尚待单独评估。

## 自研内容

- [Crux-First Reasoning](skills/crux-first-reasoning/SKILL.md)：识别关键问题、独立评估证据、形成决策相关结论。
- [Independent Judgment](instructions/independent-judgment.md)：建议常驻的抗迎合规则，必须按客户端设置独立配置。
- [行为评估样例](skills/crux-first-reasoning/references/evaluation.md)：人工 A/B 验收流程。

## 克隆与更新

```bash
# 先克隆主仓库，submodule 按需要单独初始化
git clone https://github.com/oydodo/skills.git
cd skills

# 根据需要选择具体上游
git submodule update --init upstream/mattpocock-skills
git submodule update --init upstream/technical-writing
# DSH 使用 submodule；初始化时只检出 .agents/skills/
bash scripts/checkout-dsh-skills.sh
```

更新固定版本（需要明确提交新的 Gitlink）：

```bash
git submodule update --remote upstream/mattpocock-skills
git add upstream/mattpocock-skills
git commit -m "chore: update Matt Pocock skills"
git push
```

### DSH：Submodule + Sparse Checkout

DSH 与其他第三方仓库一样，主仓库通过 **Gitlink** 固定整个上游仓库的 commit；`skill_path` 声明**采用的子目录**，而 Sparse Checkout 才负责限制**工作树实际检出的文件**。Git submodule 本身无法直接引用一个子目录。

首次克隆主仓库时不要使用 `--recurse-submodules`，否则可能先检出 Harness 的全部文件。运行：

```bash
bash scripts/checkout-dsh-skills.sh
```

脚本先执行 `git clone --no-checkout --filter=blob:none --depth 1`，再配置 `sparse-checkout`，最后检出父仓库 Gitlink 固定的版本并执行 `git submodule absorbgitdirs`。因此只在工作树中保留 `.agents/skills/`，不包含 Harness 的其他应用源码文件；Git 元数据仍包含上游仓库的树结构。

主动更新到上游最新版本：

```bash
bash scripts/checkout-dsh-skills.sh --latest
git add upstream/deepseek-harness
git commit -m "chore: update DSH skills"
git push
```

首次初始化后，常规 `git submodule status` 可查看版本；不再使用额外的 SHA pin 文件。旧方案遗留的 `upstream/dsh-skills/` 不会自动删除，如需清理请先确认无本地修改。

其他 submodule（如 WondelAI）同样可**按需**启用稀疏检出，但仅登记 `skill_path` 不等于自动应用 Sparse Checkout。

单个 Skill 的实际安装目录请在 [登记表](registry/skills.yaml) 查 `skill_path`，不要把大型多 Skill 仓库直接作为单个 Skill 安装；可根据客户端支持的方式选择子目录或创建软链接。

## 维护原则

- 第三方由上游维护，统一通过 Git submodule 记录来源和版本；稀疏检出只管理工作树，不复制或修改上游源码。
- 未核实的本机 Skill 不上传源文件；也不自动把所有已安装目录变成自研项目。
- 仅更新 GitHub 元数据与 submodule **不会改变本机现有 Skill 安装**。
- 保持私有仓库，尤其不要上传项目内部资料、密钥或未经审核的第三方内容。
