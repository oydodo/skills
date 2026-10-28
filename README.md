# Skills

个人 AI Skills 的统一管理仓库。自研 Skill 在此维护；第三方开源 Skill 优先以 **Git submodule** 追踪，DSH 例外采用固定版本的 **稀疏部分克隆**（只取 Skill 目录）。使用 [registry/skills.yaml](registry/skills.yaml) 精确声明已采用的子目录。

## 领域分类

| 领域 | 本机选用目录数 |
| --- | ---: |
| 思考与需求澄清 | 9 |
| 规划与协作 | 4 |
| 软件架构与建模 | 3 |
| 编码、测试与 Git | 14 |
| 文档与技术语言 | 3 |
| 界面设计与可视化 | 7 |
| Agent 与 Skill 管理 | 9 |
| 教学与个人效率 | 3 |
| DSH 项目专用 | 17 |
| **合计** | **69** |

[查看全部本机分类清单](registry/installed-snapshot.md)（原有 80 个目录中，Codas 项目相关的 11 个已从本仓库管理范围排除；不会改动本机安装）。

## 按上游仓库管理

| 来源 | 本机对应数量 | 位置 | 维护 |
| --- | ---: | --- | --- |
| [Matt Pocock](https://github.com/mattpocock/skills) | 31 | `upstream/mattpocock-skills` | submodule，main |
| [DeepSeek Harness Skills](https://github.com/deepseek-ai/deepseek-harness/tree/master/.agents/skills) | 19 | `upstream/dsh-skills/.agents/skills` | 固定 SHA、稀疏部分克隆，仅获取 Skills |
| [Technical Writing](https://github.com/luoling8192/technical-writing) | 1 | `upstream/technical-writing` | submodule |
| [Technical Documentation](https://github.com/wondelai/skills/tree/main/technical-documentation) | 1 | `upstream/wondelai-skills/technical-documentation` | submodule（**只使用此子目录**） |
| [Technical Language](https://github.com/jjsnack/technical-language-skill) | 1 | `upstream/technical-language-skill` | submodule |
| 待核实来源 | 16 | [仅本机清单](registry/installed-snapshot.md) | 不复制、不添加 submodule |

**注意：上游同名 Skill 只代表来源路径得到确认，不证明本机版本与所固定的 Git commit 相同。** 仓库保留 `upstream` 子模块，实际使用哪一项由 `registry/skills.yaml` 中的 `skill_path` 指定。

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
# DSH 不使用 submodule；只检出上游 .agents/skills/ 目录
bash scripts/checkout-dsh-skills.sh
```

更新固定版本（需要明确提交新的 Gitlink）：

```bash
git submodule update --remote upstream/mattpocock-skills
git add upstream/mattpocock-skills
git commit -m "chore: update Matt Pocock skills"
git push
```

### DSH：为什么不使用 submodule

Git submodule 不能指向上游仓库的单个子目录。为避免整个 Harness 源码进入本仓库和本地工作树，DSH 改为 `scripts/checkout-dsh-skills.sh`：

- `--filter=blob:none`：部分克隆，避免下载不需要的源码 blob。
- `--no-checkout` + `sparse-checkout --no-cone '/.agents/skills/'`：仅检出 `.agents/skills/` 下的文件。
- `registry/dsh-upstream.sha`：固定可复现的上游版本；本仓库不会提交 DSH 的源码副本。
- 如需跟进最新上游，可以运行 `bash scripts/checkout-dsh-skills.sh --latest`，然后审查并提交更新后的 SHA 文件。

若此前已完整检出旧 DSH submodule，本次 GitHub 变更不会自动清理旧文件；请确认无本地修改后再手动清理。

单个 Skill 的实际安装目录请在 [登记表](registry/skills.yaml) 查 `skill_path`，不要把大型多 Skill 仓库直接作为单个 Skill 安装；可根据客户端支持的方式选择子目录或创建软链接。

## 维护原则

- 第三方由上游维护。Git submodule 与 DSH 稀疏部分克隆只记录来源、版本及实际采用路径，不改写上游代码。
- 未核实的本机 Skill 不上传源文件；也不自动把所有已安装目录变成自研项目。
- 仅更新 GitHub 元数据与 submodule **不会改变本机现有 Skill 安装**。
- 保持私有仓库，尤其不要上传项目内部资料、密钥或未经审核的第三方内容。
