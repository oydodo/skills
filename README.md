# Skills

个人 AI Skills 的统一清单与自研 Skill 维护仓库。

**管理原则：自研 Skill 在这里维护；第三方开源 Skill 通过 Git submodule 指向原仓库，只更新引用版本，不复制、修改或 fork 上游源码。**

## 仓库结构

```text
skills/
├── .gitmodules                         # 第三方仓库 submodule 定义
├── skills/crux-first-reasoning/        # 自研 Skill，直接维护
├── upstream/                           # 第三方源码的 Gitlinks，不是复制品
│   ├── technical-writing/
│   ├── technical-language-skill/
│   └── wondelai-skills/
├── instructions/independent-judgment.md
├── registry/skills.yaml               # 已采用 Skill 与准确路径
├── registry/installed-snapshot.md     # 本机 80 个目录按 10 类分类
└── tests/README.md
```

## 领域分类与本机清单

本机已安装的 80 个 Skill 目录按主要用途分为 10 类，完整名称见 [分类快照](registry/installed-snapshot.md)。

| 领域 | 目录数 | 管理说明 |
| --- | ---: | --- |
| 思考与需求澄清 | 9 | `reasoning` |
| 规划与协作 | 4 | `planning` |
| 软件架构与建模 | 4 | `architecture` |
| 编码、测试与 Git | 14 | `development` |
| 文档与技术语言 | 3 | `writing` |
| 界面设计与可视化 | 7 | `visual` |
| Agent 与 Skill 管理 | 9 | `agent` |
| 教学与个人效率 | 3 | `education` |
| Codas 项目专用 | 10 | `project-codas` |
| DSH 项目专用 | 17 | `project-dsh` |

分类在登记表与文档中维护，**不为分类改变本机 Skill 路径或已存在的 Git submodule 路径**，避免安装断链。Codas 与 DSH 保留项目级隔离；以后可对单个 Skill 再增加功能标签。

## 已登记 Skill

| Skill | 维护方式 | 使用路径 |
| --- | --- | --- |
| `crux-first-reasoning` | 自研 | [skills/crux-first-reasoning](skills/crux-first-reasoning/) |
| `technical-writing` | [上游 submodule](https://github.com/luoling8192/technical-writing) | `upstream/technical-writing/` |
| `technical-documentation` | [上游 submodule](https://github.com/wondelai/skills/tree/main/technical-documentation) | **仅** `upstream/wondelai-skills/technical-documentation/` |
| `technical-language` | [上游 submodule](https://github.com/jjsnack/technical-language-skill) | `upstream/technical-language-skill/` |

准确来源见 [registry/skills.yaml](registry/skills.yaml)。还有其他本机 Skill 的名称盘点，但来源尚未核实，因此未盲目引入。

## 克隆与更新

首次克隆（必须初始化 submodule，否则第三方目录为空）：

```bash
git clone --recurse-submodules https://github.com/oydodo/skills.git
cd skills
```

已有克隆：

```bash
git submodule update --init --recursive
```

只更新指定第三方仓库的引用：

```bash
git submodule update --remote upstream/technical-writing
git add upstream/technical-writing
git commit -m "chore: bump technical-writing upstream"
git push
```

Git submodule **锁定具体 commit**，上游更新不会自动改变本仓库版本。同步上游需要显式提交新 Gitlink，便于审查和回退。

### 如何安装给 Agent 使用

按照 [registry](registry/skills.yaml) 中的 `skill_path` 选择实际目录。对多 Skill 上游仓库（例如 `wondelai/skills`），虽然 submodule 检出整个仓库，**只采用登记的子目录**。不要把完整上游仓库当成一个 Skill 安装。

可把所需 Skill 目录软链接到 `~/.agents/skills/<skill-name>`，或使用客户端提供的 Skills 安装能力。已有同名目录时，先确认其来源和本地改动，不要覆盖。

## 全局行为规范

[Independent Judgment](instructions/independent-judgment.md) 属于全局指令，需要单独配置至目标客户端。它负责抗迎合与证据校准；[Crux-First Reasoning](skills/crux-first-reasoning/SKILL.md) 负责复杂问题的关键因素判断；已有写作 Skill 负责输出语言。

## 安全与维护

- 此仓库当前为 **Private**。公开前审查所有条目。
- 不提交密钥、私人文件、公司内部资料、未经审查的本机 Skill 源码。
- 第三方仅保留上游来源和 Gitlink；修改上游源码优先向作者提出 PR。
- 通过 [tests](tests/README.md) 对抗迎合、立场更新和问题本质判断做人工 A/B 验证，**不宣称已经证实有效**。
