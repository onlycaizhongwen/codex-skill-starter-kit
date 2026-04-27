---
name: req-analysis
description: Codex 的需求分析技能。需要把原始需求、原型、用户目标或问题描述拆解成可实现的需求文档、主题边界、依赖关系和状态条目时使用。它应与 `project-skill-convention` 配合，把输出落到 `docs/codex/{version}/requirements/` 并回写 `status.md`。
---

# 需求分析

把原始需求转成结构化、可交接、可继续进入设计阶段的需求文档。

## 使用方式

开始前先遵循 `$project-skill-convention` 的前置检查。

如果本次分析规模较大、会中断，或需要跨多个需求文件探索，应同时使用 `$task-control`。

## 输入来源

可接受的输入包括：

- 用户文字需求
- 原型说明
- Issue / Ticket / 任务描述
- 现有文档中的待实现条目
- 口头目标或模糊意图

## 输出位置

输出到：

- `docs/codex/{version}/requirements/{topic}-requirements.md`

并同步回写：

- `docs/codex/{version}/status.md`

## 分析步骤

1. 明确原始需求要解决的问题，而不是直接跳到实现方案。
2. 提炼需求主题名 `topic`，使用英文短横线命名。
3. 识别范围、目标、非目标、依赖关系。
4. 把需求拆成可交接给设计阶段的结构化文档。
5. 在 `status.md` 中登记该主题，并把分析状态置为完成。

## 需求文档最小结构

建议至少包含：

- 背景
- 目标
- 范围
- 关键场景
- 完成标准
- 非目标
- 依赖

## 与 status.md 的联动

完成后应在 `status.md` 中：

- 新增需求索引条目
- 填入 requirements 文档路径
- 填入依赖关系
- 将分析状态标记为已完成
- 将整体状态推进到待设计或等价状态

## 边界

本技能负责把需求讲清楚，不负责产出技术设计，也不直接进入实现。
