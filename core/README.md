# Core v1 — 独立判断与有效执行

**定位**：本仓库最小默认工作集。不是一个新的「超级 Skill」，也不复制任何第三方 Skill 的正文；重点是明确职责、触发边界与能否被剪掉。

## 内核

| 层 | 能力 | 对应文件 / Skill | 激活 |
| --- | --- | --- | --- |
| G0 | 独立判断、证据校准、抗迎合 | [independent-judgment](../instructions/independent-judgment.md) | 需配置为**全局指令**，不是 Skill |
| R1 | 找关键问题、作可辩护的判断 | [crux-first-reasoning](../skills/crux-first-reasoning/SKILL.md) | 仅在有实质性分析、架构取舍或诊断时 |
| D1 | 澄清不可替代的缺失需求 | [interview-me](https://github.com/addyosmani/agent-skills/tree/main/skills/interview-me) | 确实无法合理继续时；按最少问题访谈 |
| D2 | 对方案做刻意压力测试 | [grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) | **用户明确要求挑战/深挖**，非每次分析默认触发 |
| C1 | 最小而完整的编码方案 | [ponytail](https://github.com/DietrichGebert/ponytail/tree/main/skills/ponytail) | 编码任务；不省略安全、检验和明确要求 |
| W1 | 中文技术方案、工作汇报 | [technical-writing](https://github.com/luoling8192/technical-writing) | 中文技术写作 |
| W2 | README、API/开发者文档 | [technical-documentation](https://github.com/wondelai/skills/tree/main/technical-documentation) | 开发者文档任务 |
| W3 | 精简技术英语与风格校正 | [technical-language](https://github.com/jjsnack/technical-language-skill) | 英文技术表达重写 |

这是 **1 条全局指令 + 7 个按任务触发的 Skill**。条件性核心 ≠ 全部每次加载；人和 Agent 不需要为了显示流程而逐个调用。

## 路由约束

1. **能直接完成，就直接完成。** 简单事实、翻译、常规改写、明确的执行请求不做强制访谈或五段式反思。
2. **复杂判断先确定结论**：R1 优先辨别关键假设，再根据任务决定是否用写作 Skill 呈现。
3. **澄清和挑战不混淆**：缺少决定性输入时 D1；用户明确要求审查漏洞、盘问时 D2。不要无条件 D1 → D2 级联。
4. **写作只选合适角色**：W1 中文技术方案，W2 开发者文档，W3 技术英语。确需跨越内容判断与表达时可 R1 + W1/W2/W3，但避免三个写作 Skill 同时套用。
5. **编码时 C1 限制复杂度**：不增加不必要的抽象/依赖；该做的验证、边界处理和测试仍需完成。
6. **项目专用不全局启用**：DSH 的 19 个 Skill 仅在相关项目按需使用；其余通用能力维持候选库。
7. **不把 GitHub 上的分类当成运行时事实**：仓库中新增索引/配置不会自动改变 Mac 的已安装 Skill 或客户端触发状态。

## 冲突优先级

用户的明确目标与约束 > 全局独立判断准则（不违背更高优先级安全规则）> 选定 Skill 的任务专用流程 > 语言/格式修饰。若上游 Skill 要求无休止地访谈，而请求本身可合理执行，应保持原始请求范围，必要时跳过访谈 Skill。

## 位置

- 可机器读取的意图配置：[profiles/core.yaml](../profiles/core.yaml)
- 候选目录的第一轮分流：[registry/curation.yaml](../registry/curation.yaml)
- 剪枝依据与恢复条件：[registry/pruning.md](../registry/pruning.md)
- 预期行为用例：[tests/core-routing.md](../tests/core-routing.md)

**实施状态**：此文定义目标工作集，不代表已切换本机技能发现配置。当前本机仍有原 80 个目录，且自研 `crux-first-reasoning` 需要单独安装到目标客户端才能被触发。
