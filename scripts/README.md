# 构建与打包脚本

本目录的脚本把源头生成为分发产物：从唯一注册表 `registry/skills.yaml`、自维护的 `skills/`、`core/` 和 `upstream/` 的固定提交，生成 `.agents/` 与 `plugins/oydodo-skills/` 两份产物，再打包成三份 ZIP。

- `build_plugins.py`：`--write` 生成产物，`--check` 核对产物和源头是否一致，`--list-submodules` 列出要初始化的上游，`--release-notes` 取出某一版的 CHANGELOG 说明。
- `package_plugins.py`：打包通用 `.agents`、ChatGPT、Claude 三份 ZIP。`package_claude_plugin.py` 是只打 Claude 包的旧入口。
- 构建只检查、覆盖、打包 `.agents/skills`、`.agents/licenses` 里由注册表生成的条目；别的工具放进这两个目录的东西不动（CHANGELOG 0.1.16）。
- `checkout-dsh-skills.sh`：只检出 DSH 上游里的 `.agents/skills`。

## 版本门禁

插件内容一变，`CHANGELOG.md` 最上面必须是下一个补丁版本，否则构建拒绝发布。情景：要求每次分发都带上“改了什么、为什么”（CHANGELOG 0.1.9）。Dependabot 的上游升级 PR 因此会先失败，这是刻意留下的审查环节，补上版本说明即可（[Skill 生命周期](../docs/skill-lifecycle.md)）。
