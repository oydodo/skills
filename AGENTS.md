# 在本仓库干活的规矩

这里的规矩管在本仓库修改 Skill、构建、发布和写文档的活。仓库是什么见 [README](README.md)，方向见 README 的“预期获得什么”和“不做什么”，各目录是什么见该目录的 README。

每条规矩都写了它是为什么情景定的。新情况和某条规矩看起来冲突时，先比情景：情景不同，这条规矩管不到；情景相同，才算要推翻它，推翻要讲依据并由维护者决定。

## 动手前

- 说清这次改动服务 [README](README.md) 里的哪一条成果、没有碰“不做什么”；说不清就先问维护者。情景：本仓库曾经花大量工夫做跨平台 Hook 适配，最后被维护者叫停，认为偏离主线（[HANDOFF](HANDOFF.md) 第 1 节）。
- 读要改的目录的 README，以及 [CHANGELOG](CHANGELOG.md) 里相关版本写的“为什么”。

## 只改源头

- 源头是 `skills/`、`registry/skills.yaml`、`core/always-on.md`、`core/hooks.json`、`upstream/` 的固定提交和 `CHANGELOG.md`。`plugins/oydodo-skills/` 和 `.agents/` 下的 `skills`、`licenses`、`SOURCES.md`、`CHANGELOG.md` 里由注册表生成的条目都由 [构建脚本](scripts/README.md) 生成。情景：构建会覆盖这些条目，手改会丢失，`--check` 也会报不一致（CHANGELOG 0.1.13）。`.agents/skills/codas-*` 和 `.agents/codas/` 是 Codas 安装的，不由构建生成，构建也不会动它们。
- `upstream/` 是第三方仓库的固定版本，不在这里改它们的正文；要调整触发描述用 `registry/skills.yaml` 的 `description_override`。
- 新增、升级、移除 Skill 按 [Skill 生命周期](docs/skill-lifecycle.md) 走。

## 说“做好了”之前

- 合并、CI 通过、发布 ZIP、网页端 Marketplace 同步、Agent 实际触发，是五件不同的事。只报告实际验证到的那一层，其余写“未验证”。情景：构建和 ZIP 都成功过，但客户端是否真的加载、触发并没有测过（CHANGELOG 0.1.8、0.1.13）。

## 记录改动

- 改了会打包进插件的内容，就在 `CHANGELOG.md` 最上面写下一个补丁版本：改了什么，以及当时的情景和理由。构建会检查这一点。
- 一直有效的规矩写在这里或相关目录的 README，不写进 CHANGELOG。

<!-- CODAS:START -->
# Repository guidance

Entry for working in this repository with Codas. Codas Skills (`codas-*`) carry the steps; start with `codas-ontology`.

- **Read first:** the Intent (by default the opening sections of the root `README.md`), then `docs/ontology/` and the documentation standard (by default `docs/AGENTS.md`), which says where everything else lives. Work from the newer of local and remote default branch, compared by ancestry.
- **Before drafting or making a change to a file:** the nearest `README.md` above it says what it is now; the nearest `AGENTS.md` says how to work there. Their links lead to the Notes that say why.
- **Review happens in the pull request:** make the change on a branch, then open a pull request that says which Intent it serves, whether it changes the Intent (with the diff), which part it changes, and the behaviour before and after.
- **Missing pieces** are reported as gaps or unknown, never filled in by guessing.
- **Same commit:** a code change keeps true the README, AGENTS and reference pages that describe it; a new code directory gets its README.
- **Notes:** follow the repository's Note rules file (found through `codas-ontology`); Note checks block commits but do not prove meaning or approval.
- **Root block:** only this managed block is maintained; bytes outside it stay unchanged.
- Do not merge before checks pass.
<!-- CODAS:END -->
