---
name: starter-kit-import
description: Codex 中文技能工程的导入安装技能。当需要把共享仓库中的技能安装到 `~/.codex/skills` 或其他目标目录，并在安装前检查同名冲突时使用。
---

# Starter Kit 导入安装

把准备好的技能工程导入到 Codex 技能目录。

## 默认来源

如果用户没有额外指定，默认当前工作区就是 starter kit 根目录。

## 默认目标

- 推荐全局目录：`~/.codex/skills/`
- 也可以安装到用户指定的项目级技能目录

## 脚本安装方式

想直接安装时，优先使用 starter kit 根目录下的 `scripts/install_starter_kit.py`。

示例：

```bash
python scripts/install_starter_kit.py
py -3 scripts/install_starter_kit.py
python scripts/install_starter_kit.py --dry-run
python scripts/install_starter_kit.py --overwrite
python scripts/install_starter_kit.py --target ~/my-codex-skills
python scripts/install_starter_kit.py --overwrite --init-project .
```

## 导入流程

1. 确认来源目录下存在 `skills/` 子目录
2. 检查目标目录中是否有同名技能
3. 有冲突时询问覆盖还是跳过；脚本模式下可通过 `--overwrite` 指定
4. 把选中的技能目录复制到目标目录
5. 保留每个技能目录内的完整结构，包括 `agents/openai.yaml`
6. 如果目标是某个真实项目，额外初始化项目根 `AGENTS.md`、`docs/codex/v1/` 骨架和 `.codex/plans/main/TASKS.md`
7. 输出新增、跳过、覆盖结果

## 说明

- 需要安装的是技能目录本身
- 安装后即可由 Codex 自动发现或显式调用
- 想恢复接近原版的项目级自动触发，应同时在项目根放置 `AGENTS.md`
- 如果用户本机 Python 版本不确定，优先建议使用 `py -3`
- 推荐命令：`python scripts/install_starter_kit.py --overwrite --init-project <项目目录>`
