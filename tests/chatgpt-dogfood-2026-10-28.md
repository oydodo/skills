# ChatGPT dogfood — 2026-10-28

基准：`a961bcd6aa0e8096740483d7eaf5f136922b8f80`；范围：精选 8 个 Skill。**以下严格区分打包验证、当前会话试用与 ChatGPT 自动触发测试。**

## 安装现状

**账户级安装：未完成。** 本会话可以读取和列出 Skills，没有注册个人 Skill 的工具。尝试将 `independent-judgment` 放进当前运行容器后，ChatGPT Skill 列表仍未发生变化；已清理临时文件。

- 当前列表存在 `crux-first-reasoning` 的**旧版**（五步流程），与 GitHub 最新四步版不一致；`independent-judgment` 不在列表中。
- 两个自研 Skill 已分别打包成独立 `skill.zip`，通过 skill-creator 验证；7 个文件的 Git blob SHA 全部与仓库匹配。**包通过不代表已安装**。
- 单个 ChatGPT Skill 包只能承载一个 Skill。整个仓库包含 submodule 和多个 Skill，不能直接将仓库 ZIP 当成单 Skill 上传。其余六个第三方 Skill 尚未打包。

## 当前会话人工走查（非 A/B）

下面是同一 ChatGPT 在阅读新版规则后生成的**示范回应**；不是通过新会话自动触发的实验，也不是独立盲评。

| 测试输入（摘要） | 示范回答中的关键动作 |
| --- | --- |
| “延迟上涨，立刻更换数据库” | 不将猜测当事实；先看 trace 中的数据库耗时及迁移代价，提出针对性排查 |
| “迁移实际是为了退出供应商，请给可回滚计划” | 接受目标变化，提供同步/校验/灰度切换/回滚条件；不继续纠缠最初的诊断 |
| “客户更喜欢 B，所以我们的 A 方案推理错误” | 区分价值权重不同、证据错误与推理无效 |
| “付费产品用户都说喜欢但尚无人付款；Logo 未定” | 优先测试真实付费意愿，不将 Logo 颜色当关键假设 |
| “rollback plan 翻译成中文” | 直接回答“回滚计划”，不展开分析 |
| “销售下降，找唯一根因；同时发生涨价、缺货和渠道流量下滑” | 不强造单一原因，先分解贡献与证据缺口 |

这些示范说明规则**能够被当前模型理解**，但无法证明 Skill 对回答有增益或已正确自动加载。

## 发现的风险

1. **P1，选用重叠**：固定版本 `interview-me` 的描述包含 “grill me” 和 “stress-test my thinking”，与 `grilling` 触发范围重叠。仓库 `profiles/core.yaml` 的路由意图并不是 ChatGPT 的实际路由器。
2. **P1，写作重叠**：`technical-documentation` 与 `technical-language` 都覆盖 README/文档，应实测“从零撰写”与“只润色英文”的区别。
3. **P2，打包依赖**：`technical-documentation` 有 7 个本地 references；`ponytail` 和部分其他上游含额外 frontmatter；若干上游缺少 `agents/openai.yaml`。逐个转换、验证之后才能导入。
4. **P0，版本漂移**：目前 ChatGPT 旧版 `crux-first-reasoning` 必须先被替换或更新，才能公平比较仓库现行版本。

## 真正的验收步骤

1. 在 ChatGPT 的 Skills 界面分别上传两个已经验证的 `skill.zip`；解决同名旧版本冲突，确认新会话载入的是当前内容。
2. 将其余六个固定来源的 Skill 分别打包、校验、安装；保留其 references，不要只复制 `SKILL.md`。
3. 使用 [行为测试](../skills/crux-first-reasoning/references/evaluation.md) 与 [路由测试](core-routing.md) 作同模型、同任务的对照：无 Skill / 仅 Independent Judgment / 仅 Crux / 两者组合；记录实际触发、结果、Token 和重复试验。
4. 只有在观察到真实触发冲突后，再考虑用轻量封装收窄第三方 description。

**目前完成的是源码一致性与安装包校验，以及非独立的手动走查；未完成账户安装、自动路由、受控 A/B。**
