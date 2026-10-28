# 其他来源：16 个待审核的本机 Skills

本机 `~/.agents/skills/` 的 16 个条目（已扣除 Matt Pocock、DSH、三个写作 Skill 和此前排除的 Codas 相关目录）。**这一页是来源审查，不代表已经加入正式 Skill 注册表。**

- **已核实相符的上游实现：7 个（其中 1 个已接入 submodule）。** 匹配依据包括本机 Git remote、Skill 名称及正文或 description；本机版本可能滞后于上游。
- **尚未确认原始上游：9 个。** 不凭同名仓库推测，也不自动添加 submodule。
- 任何新引入前，检查维护者、实际路径、许可证、与已安装版本是否一致，以及是否包含项目专用内容。

| 本机 Skill | 所属领域 | 上游来源 / 状态 |
| --- | --- | --- |
| `interview-me` | 需求澄清 | **待核实**；不要误用同名但用途不同的开源 Skill |
| `product-brainstorming` | 需求澄清 | **待核实** |
| `code-annotator` | 编码 | **待核实** |
| `code-explainer` | 编码 | **待核实**；本机文档带 Codas 设计注释，应在接入前确认项目边界 |
| `codex-appserver-doctor` | 编码 | **待核实**，可能是环境专用 Skill |
| `ponytail` | 编码 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/main/skills/ponytail) — **已确认并接入**；上游主仓库，实际采用 `skills/ponytail/`；本机版本未被覆盖 |
| `anatomy` | 可视化 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) — **已核实**，本机 Git remote 指向该仓库 |
| `archify` | 可视化 | [tt-a1i/archify/archify](https://github.com/tt-a1i/archify/tree/main/archify) — **已核实**，匹配名称与功能 |
| `design-taste-frontend` | 可视化 | **待核实**，无法根据相似项目确定原作者 |
| `explore-recipes` | 可视化 | **待核实**，文档提到 ShipSwift Recipes |
| `remote-html-preview` | 可视化 | **待核实**，可能是本地定制 |
| `visual-explainer` | 可视化 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer/tree/main/plugins/visual-explainer) — **已核实**；本机标记 v0.12.0，上游检查时为 v0.14.0 |
| `find-skills` | Agent 管理 | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) — **已核实**，description 匹配 |
| `nopua` | Agent 管理 | [wuji-labs/nopua](https://github.com/wuji-labs/nopua) — **已核实**；本机 v2.0.0，上游检查时为 v2.0.2 |
| `write-a-skill` | Agent 管理 | **待核实** |
| `i-have-adhd` | 个人效率 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd/tree/main/skills/i-have-adhd) — **已核实**，description 匹配 |

下一步若要纳入正式仓库，按用户需求选择单独 Git submodule 或已验证的子目录检出方式。避免重复引入同一个上游仓库，也不要把未经确认的同名 Skill 当作原始来源。
