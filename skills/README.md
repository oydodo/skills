# 自维护 Skill

本目录是本仓库自己维护的 4 个 Skill 的源码：三个判断核心 `philosophical-foundation`、`independent-judgment`、`crux-first-reasoning`，以及 CodeGraph 工具适配 `codegraph`。

不在这里的：第三方 Skill 在 `upstream/` 以固定提交引入；`.agents/skills/` 里注册表对应的条目和 `plugins/oydodo-skills/skills/` 里是构建生成的副本，不在那里改。

## 三个核心各管各的

- `philosophical-foundation`：从联系、矛盾和变化看问题，兼顾二阶效应、简化、可逆和知止。它是本仓库的方法论底层，不是平台的系统指令。
- `independent-judgment`：凭证据判断，必要时建设性地指出问题；不为反对而反对，尊重用户知情后的选择。
- `crux-first-reasoning`：先看目标和现状差在哪，再找起主导作用的矛盾，然后才验证可能改变判断的不确定处，并讲清为什么其他因素是次要的。

它们是三个独立的 Skill，按任务单独触发，不是必须依次走完的三步；简单任务直接完成。情景：如果把“核心”当成每次都要走的流程，简单查询也会被拖进完整分析。

`crux-first-reasoning` 以前是先找“影响大、证据弱的假设”，2026-10-30 改为先找主要矛盾，理由见 [CHANGELOG](../CHANGELOG.md) 0.1.6。

## 怎样算改好了

正例看复杂任务是否抓住主要矛盾、讲清主次和依据；反例看简单任务能否直接完成。不能只凭 Agent 自述、构建成功或 ZIP 存在，就说行为有效。各 Skill 的测试案例在它自己的 `references/evaluation.md`。
