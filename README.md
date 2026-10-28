# Skills

个人 AI Skills 的统一目录与自研 Skill 维护仓库。

> **原则：自研 Skill 在这里维护；第三方开源 Skill 只链接上游，不复制源码、不建立 Git submodule、不维护 fork。**

## 内容

- [`skills/crux-first-reasoning/`](skills/crux-first-reasoning/): 自研的关键问题优先分析 Skill。
- [`instructions/independent-judgment.md`](instructions/independent-judgment.md): 跨会话抗迎合、立场稳定与证据校准的建议全局指令。
- [`registry/skills.yaml`](registry/skills.yaml): 已确认来源的 Skill 清单，区分自研和第三方。
- [`registry/installed-snapshot.md`](registry/installed-snapshot.md): 本机已安装 Skill 名称快照；未核实来源的条目不会猜测或复制。
- [`skills/crux-first-reasoning/references/evaluation.md`](skills/crux-first-reasoning/references/evaluation.md): 行为验收样例。

## 使用方式

**自研 Skill**：从本仓库的 `skills/<name>/` 安装。修改原文件、提交 Git 历史，统一在这里维护。

**第三方 Skill**：在 [registry](registry/skills.yaml) 中打开原始 GitHub 仓库及对应子目录，直接从上游安装或更新。上游作者负责源码维护，本仓库只管理采用记录与自有配置。多 Skill 仓库只安装选定子目录。

**全局规则**：本仓库保存的是可复用文本。需要手动配置到 ChatGPT 自定义指令或 Agent 的全局指令文件；仅上传仓库不会自动生效。

## 维护约定

1. 新增第三方 Skill 时记录上游仓库 URL 与准确的 Skill 子路径，**不复制、改写或 fork 上游代码**。
2. 需要修改第三方 Skill 时，优先向上游提交 issue/PR；确需私有定制时，另建自研 Skill 并注明来源。
3. 自研 Skill 变更遵守 `SKILL.md` 元数据及轻量行为评估，避免越加越复杂。
4. 不提交 API 密钥、私人凭据、内部机密或未经审查的本机文件。
5. GitHub 以仓库版本为准；本机已有约 80 个 Skill 仅做名称盘点，不会自动同步或上传源码。

仓库默认设为 **Private**。若未来公开，请先审查所有自有文档与清单内容。
