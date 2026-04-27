---
name: starter-kit-backup
description: Codex 中文技能工程的导出打包技能。当需要把 `~/.codex/skills` 中的现有技能整理成可分享的 starter kit，并排除个人缓存、会话历史、无关文件和敏感信息时使用。
---

# Starter Kit 导出打包

把现有 Codex 技能环境打包成可分享的中文 starter kit。

## 应包含的内容

- `~/.codex/skills/` 下的技能目录
- 每个技能的 `SKILL.md`
- `agents/openai.yaml`
- 可选的 `scripts/`、`references/`、`assets/`

## 不应包含的内容

- 个人临时笔记
- 会话历史
- 机器本地缓存
- 引用资料或脚本中的敏感信息

## 打包流程

1. 确定输出目录，默认可放到工作区下的 `codex-skill-starter-kit/`
2. 复制选中的技能目录
3. 清理明显无用文件，例如 `.DS_Store`
4. 检查是否误带敏感信息或私人内容
5. 输出最终目录树和统计结果

## 说明

- 打包对象是 Codex 技能目录本身
- 可分享单元通常是一个或多个技能目录，加上必要的项目说明
- 导出结果应当保持简洁、可安装、可复用