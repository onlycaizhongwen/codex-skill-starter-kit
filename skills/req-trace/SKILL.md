---
name: req-trace
description: Codex 的需求追踪技能。需要对照 requirements、designs、plans 和实现结果做一致性审查，找出缺口、偏差、遗漏和未闭环项时使用。它应与 `project-skill-convention` 配合，把结果输出到 `docs/codex/{version}/trace/`，并在 `status.md` 中记录审查摘要。
---

# 需求追踪

对一个主题从需求到实现的全链路产物做一致性检查。

## 使用方式

开始前先遵循 `$project-skill-convention` 的前置检查。

本技能默认是只读审查型技能：

- 负责指出缺口和不一致
- 不直接替代实现阶段修代码
- 不静默替其他阶段改完成状态

## 输入范围

按主题读取以下产物中的已存在项：

- `requirements/{topic}-requirements.md`
- `designs/{topic}-design.md`
- `plans/{topic}-plan.md`
- 当前实现或已交付结果
- 必要时读取 `status.md`

## 输出位置

输出到：

- `docs/codex/{version}/trace/{topic}-trace.md`

## 审查步骤

1. 读取需求文档，明确承诺范围与完成标准。
2. 读取设计与计划文档，确认是否覆盖需求。
3. 对照实现结果，识别未落地、偏离、缺失和额外实现。
4. 形成结构化追踪报告。
5. 在 `status.md` 备注列或变更记录中写入审查摘要。

## 追踪报告最小结构

建议至少包含：

- 审查范围
- 已对齐项
- 未对齐项
- 风险与影响
- 建议后续动作
- 总结结论

写报告时优先复用 [report-template.md](references/report-template.md)。

## 与 status.md 的联动

完成后可以：

- 在备注中记录“发现 N 处差异，详见 trace 文档”
- 在变更记录中追加审查结果

但不要直接把别的阶段标成完成，除非用户明确要求按审查结果回写状态。

## 边界

本技能做的是审查与追踪，不负责自动修复。
