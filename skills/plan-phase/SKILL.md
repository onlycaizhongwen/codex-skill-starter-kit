---
name: plan-phase
description: Codex 的计划阶段技能。需要根据 design 文档拆解实施步骤、确定执行顺序、验证依赖、形成可执行计划，并把结果写入 `docs/codex/{version}/plans/` 时使用。它应与 `project-skill-convention` 配合，并在完成后回写 `status.md`。
---

# 计划阶段

根据技术设计文档产出可执行的实施计划文档。

## 使用方式

开始前先遵循 `$project-skill-convention` 的前置检查。

如果计划较长、涉及多阶段交付或可能中断，应同时使用 `$task-control`。

## 输入来源

计划阶段的最小输入是：

- `docs/codex/{version}/status.md`
- `docs/codex/{version}/designs/{topic}-design.md`

必要时还应读取：

- 依赖主题的 plan 或 design 文档
- 与当前实施直接相关的代码入口和目录结构

## 输出位置

输出到：

- `docs/codex/{version}/plans/{topic}-plan.md`

并同步回写：

- `docs/codex/{version}/status.md`

## 计划步骤

1. 读取 `status.md`，确认当前主题和依赖关系。
2. 读取 design 文档，明确方案边界和关键风险。
3. 把实现工作拆成可执行步骤，确定顺序和前置条件。
4. 标出需要用户确认、需要验证、可能中断的检查点。
5. 产出结构化 plan 文档。
6. 在 `status.md` 中回写 plan 文档路径和计划状态。

## 计划文档最小结构

建议至少包含：

- 目标
- 前置条件
- 实施步骤
- 验证方式
- 风险与回滚考虑
- 检查点/确认点

## 与 status.md 的联动

完成后应在 `status.md` 中：

- 填入 plan 文档路径
- 将计划状态标记为已完成
- 将整体状态推进到待实现或等价状态

## 边界

本技能负责把设计变成执行计划，不直接代替实现阶段改代码。
