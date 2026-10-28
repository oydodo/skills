# Skills

个人 AI Skills 工作集：**自研核心、复用上游、按需剪枝**。第三方仓库用 Git submodule 固定版本，不复制源码。

## 核心

| 作用 | 组件 |
| --- | --- |
| 全局独立判断 | [independent-judgment](instructions/independent-judgment.md) |
| 找关键问题 | [crux-first-reasoning](skills/crux-first-reasoning/SKILL.md) |
| 澄清需求 / 挑战方案 | `interview-me` / `grilling` |
| 最小而完整的编码 | `ponytail` |
| 中文技术写作 / 开发文档 / 技术英语 | `technical-writing` / `technical-documentation` / `technical-language` |

[触发与职责](core/README.md) · [核心配置](profiles/core.yaml)

**核心配置尚未应用到本机**：全局指令需单独配置，Skill 按任务触发。

## 获取

```bash
git clone https://github.com/oydodo/skills.git
cd skills

# 按需初始化指定上游（示例）
git submodule update --init upstream/mattpocock-skills

# DSH：submodule + sparse checkout，仅检出 .agents/skills/
bash scripts/checkout-dsh-skills.sh
```

## 清单

[Skill 与上游路径](registry/skills.yaml) · [分类与剪枝状态](registry/curation.yaml) · [剪枝依据](registry/pruning.md) · [本机盘点](registry/installed-snapshot.md)
