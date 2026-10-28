# 分层路由行为验收（待实测）

**方法**：同模型、同任务，对比“当前全量环境”和“目标核心环境”；记录是否正确触发、答案质量、是否无端访谈、是否出现过度工程、耗时/Token。下面是验收脚本，不是已通过的测试结果。

| 测试输入 | 预期触发 | 预期不触发 |
| --- | --- | --- |
| “这个 API 上线后变慢了，我们必须换数据库吗？” | crux-first-reasoning：先查关键证据 | grilling、interview-me 的长轮次访谈 |
| “帮我比较两种跨 Agent 状态管理的架构，给出选择。” | crux-first-reasoning | 三种写作 Skill 同时启用 |
| “我想做一个系统，但是不知道目标用户，帮我通过访谈定义。” | interview-me | 直接开工编码、grilling |
| “强力挑战这个计划的漏洞，逐轮问我。” | grilling | interview-me 或直接生成交付 |
| “修复这个订单接口的幂等 bug，保持改动尽量小。” | ponytail；需要诊断再按需使用对应 Skill | 不相关文档 Skill、无必要的新抽象 |
| “把这段中文技术方案改成正式的领导汇报稿。” | technical-writing | 技术英语、开发者文档 |
| “为这个 API 生成开发者 README。” | technical-documentation | technical-language（除非明确要求英语风格校正） |
| “把这段英文发布说明改成简明技术英语。” | technical-language | 中文写作 |
| “翻译 rollback plan。” | L0 行为规则；直接翻译，无需额外 Skill | 访谈/复杂推理/工程 Skill |
| “审查现有 PR 的实现是否符合规范和需求。” | L3 code-review，可直接执行 | 强制先访谈、重新设计或进行无关写作 |
| “请只润色这段技术英文。” | L4 technical-language，可直接执行 | 要求先经过 L1–L3 |
| “我们正在维护 DSH，评审这个 DSH PR。” | DSH 项目专用 Skill（有仓库证据时） | Codas 相关与不相关项目 Skill |

## 人工观察项

- **独立判断**：面对用户反复施压是否依然依据证据；新事实出现后能否合理改变观点。
- **职责边界**：是否过早启动 interview-me/grilling；是否把 write/research/implement 误串成完整“瀑布式流程”。
- **最简实现**：是否只缩减代码、却漏掉测试或安全处理。
- **文档质量**：是否只使用一个主导写作 Skill，术语、事实与结构准确。
- **剪枝回归**：移除七个候选中的任何一个后，其独有任务是否仍可完成。

手动记录每个用例的触发 Skill、结果好坏和反例。未实测前不要宣称本配置优于全量配置。
