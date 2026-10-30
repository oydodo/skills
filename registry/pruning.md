# 精选与剪枝

**当前精选 18 个独立 Skill**：核心判断仍为哲学基础 + 独立判断 + 主要矛盾推理三项；其余能力按实际任务触发。原版第三方 Skill 通过固定 commit 的 Submodule 分发，不直接修改指令正文；已修复用户主动触发标志在构建中丢失的问题。

| 状态 | 数量 | 说明 |
| --- | ---: | --- |
| 精选 Skill | 18 | 哲学 1 / 判断 1 / 认知 4 / 长期导航 1 / 调研原型 2 / 编码与故障 3 / Agent 质量 2 / 可视化 1 / 技术表达 3 |
| 第三方精选 | 14 | 其中 Matt 的 8 项 Skill 来自同一个受控的 Git Submodule |
| 自维护精选 | 4 | 三个判断核心 + CodeGraph 工具适配 |
| Matt 未选中 | 23 | 如 code-review、tdd、implement-spec；避免无需求地引入完整工程编排 |
| DSH 项目专用 | 19 | 不进入通用精选 |
| 其他未选中 | 10 | 按真实任务与效果再考虑 |
| 自维护暂停 | 2 | codex-appserver-doctor、remote-html-preview |
| Codas 排除 | 12 | 不与 Codas 项目内独立工作流混合 |

## 本轮选入与保留边界

- `writing-for-agents`：专供 Agent 可读文档和 Skill 的指令质量治理；避免与普通技术写作重复。
- `diagnosing-bugs`：复杂、间歇性故障或性能回归的复现—定位—验证闭环；简单 Bug 不强制启动完整流程。
- `retro`：基于会话证据优化指令、工具和检查。**只由用户主动调用**；上游依赖的 `writing-for-agents` 已一并精选。
- `code-review`、`tdd`、`codebase-design` 等继续保留为候选；其中的方法论可借鉴，但不因此自动绑定完整 Matt 工程流程。

**停用原则**：先通过正例与负例检验十八个 Skill 的路由和实际行为，再做可逆剪枝。精选与 Plugin 分发并未改变旧版本机 80 项安装快照；不得声称客户端当前仅加载这十八项。

[精选清单](skills.yaml) · [历史盘点](curation.yaml) · [路由测试](../tests/core-routing.md) · [统一更新 SOP](../docs/skill-lifecycle.md)
