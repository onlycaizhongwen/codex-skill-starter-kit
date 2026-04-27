---
name: design-phase
description: Codex 的设计阶段技能。需要根据 requirements 文档产出技术设计、明确实现方案、拆分关键模块、梳理依赖和风险，并把结果写入 `docs/codex/{version}/designs/` 时使用。它应与 `project-skill-convention` 配合，并在完成后回写 `status.md`。
---

# 设计阶段

根据需求文档产出可交接给计划和实现阶段的技术设计文档。

## 使用方式

开始前先遵循 `$project-skill-convention` 的前置检查。

如果任务较大、存在中断风险或需要跨多个设计点探索，应同时使用 `$task-control`。

## 输入来源

设计阶段的最小输入是：

- `docs/codex/{version}/status.md`
- `docs/codex/{version}/requirements/{topic}-requirements.md`

必要时还应读取：

- 依赖主题的设计或需求文档
- 与当前主题相关的代码、配置、现有架构说明

## 输出位置

输出到：

- `docs/codex/{version}/designs/{topic}-design.md`

并同步回写：

- `docs/codex/{version}/status.md`

## 设计步骤

1. 读取 `status.md`，确认当前主题和依赖关系。
2. 读取 requirements 文档，明确范围、完成标准和非目标。
3. 识别实现该需求涉及的关键模块、数据流、入口点和边界。
4. 明确方案取舍、风险、兼容性影响和待确认项。
5. 产出结构化 design 文档。
6. 在 `status.md` 中回写设计文档路径和设计状态。

## 设计文档最小结构

建议至少包含：

- 背景与目标
- 范围与边界
- 方案概述
- 模块/流程设计
- 数据结构或关键对象
- 风险与取舍
- 待确认项

## 与 status.md 的联动

完成后应在 `status.md` 中：

- 填入 design 文档路径
- 将设计状态标记为已完成
- 将整体状态推进到待计划或等价状态

## 边界

本技能负责技术设计，不直接拆实施步骤，也不直接进入编码实现。
