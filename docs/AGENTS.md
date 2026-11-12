# 文档放在哪里

本文件说明本仓库的各类知识各放在哪里，一个事实只有一个家，其他地方只放链接。四类用途的定义见 [本体](ontology/ONTOLOGY.md)。写作细则用 `codas-doc-writing` 和 `codas-prose-standard`；本文件不重复它们。

| 用途 | 家 | 不放在这里的 |
|---|---|---|
| 什么算好（Intent） | 根 [README](../README.md) 的“为什么要这样组织”“预期获得什么”（含成功标准）“不做什么”。只有维护者能改，Agent 可以起草 | 现状细节（→ 各目录 README）、规矩（→ AGENTS） |
| 怎么在这里干活（AGENTS） | 根 [AGENTS.md](../AGENTS.md)：每次会话都要在上下文里的规矩，每条写明情景；[Skill 生命周期](skill-lifecycle.md)：新增、升级、移除 Skill 的步骤 | 故事和长例子（→ Note、CHANGELOG） |
| 现在是什么（参考） | 各目录自己的 README（[`skills/`](../skills/README.md)、[`scripts/`](../scripts/README.md)、[`core/`](../core/README.md)）；[分发说明](distribution.md) | 为什么这样定（→ Note） |
| 为什么这样定、历史（Note） | [`docs/notes/`](notes/)：决策记录；[CHANGELOG](../CHANGELOG.md)：每个版本改了什么、当时的情景和理由，随插件分发 | 现行规矩（→ AGENTS） |

两点说明：

- 版本级的历史继续记在 CHANGELOG，不搬进 `docs/notes/`；只有需要单独写明理由、由维护者批准的决定才写成 Note（规则见 [本体](ontology/ONTOLOGY.md) 和 `codas-propose`）。
- `.agents/skills/codas-*`、`.agents/codas/` 由 Codas 安装，版本记在 [codas.yml](../codas.yml)；`.agents/` 里的其余条目、`plugins/`、`upstream/` 是生成物或第三方内容，Codas 不把它们当作本仓库的知识来读。
