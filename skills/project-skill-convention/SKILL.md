---
name: project-skill-convention
description: Codex 的项目协作公约技能。当仓库希望让需求分析、技术设计、实现计划、实现执行、追踪审查共用一套目录、状态文件和交接规则时使用。它会定义前置检查、目录结构、状态回写规则、阶段职责和与 task-control 的联动方式。
---

# 项目技能公约

本公约用于统一需求、设计、计划、实现、追踪之间的协作规则。使用流程型技能时，应先遵循本公约，再执行目标技能。

适用阶段型技能包括：

- `req-analysis`
- `design-phase`
- `plan-phase`
- 实现阶段任务
- `req-trace`

## 一、标准目录

```text
docs/codex/{version}/
├── status.md
├── requirements/
├── designs/
├── plans/
└── trace/
```

建议使用：

- `{topic}-requirements.md`
- `{topic}-design.md`
- `{topic}-plan.md`
- `{topic}-trace.md`

## 二、前置检查

### 查询类操作

至少确认：

- `docs/codex/{version}/` 存在
- `status.md` 存在

### 变更类操作

开始前必须执行：

1. 加载 `dev-constraints`
2. 检查 `docs/codex/{version}/status.md` 是否存在，不存在则初始化
3. 读取 `status.md`
4. 检查主题依赖关系，避免跳过前置主题
5. 如果任务规模较大，则同时注册 `task-control`

## 三、公约优先规则

当具体技能默认行为与本公约冲突时，以本公约为准。

统一约束包括：

- 文档输出位置固定在 `docs/codex/{version}/...`
- 文档命名不带日期前缀
- 各阶段完成后必须回写 `status.md`
- 目录、状态和任务记录必须相互对应

## 四、status.md 结构

`status.md` 至少包含三部分：

1. 需求索引
2. 进度与状态表
3. 变更记录

建议状态值：

- 未开始
- 分析中
- 已设计
- 已计划
- 实现中
- 已完成
- 需返工

## 五、阶段职责边界

### 需求阶段

负责：

- 创建或更新 requirements 文档
- 在 `status.md` 中登记需求条目
- 更新分析状态
- 填写依赖关系

不负责：

- 代替设计或计划阶段修改其状态

### 设计阶段

负责：

- 读取 `status.md`
- 读取 requirements 文档
- 必要时读取依赖主题文档
- 输出 designs 文档
- 回写 `status.md` 中的设计文件路径与设计状态
- 如果任务较大，使用 `task-control` 记录过程

### 计划阶段

负责：

- 读取 `status.md`
- 读取 design 文档
- 输出 plans 文档
- 回写 `status.md` 中的计划文件路径与计划状态
- 与 `task-control` 联动记录过程

### 实现阶段

负责：

- 读取 `status.md`
- 读取 plan 文档
- 执行实现
- 回写实现状态
- 任务中断时同步写入 `task-control` 断点
- 当主题进入“实现完成 / 验证完成 / 收尾交付”时，主动补一轮追踪审查，输出 trace 文档或至少提示立即进入 `req-trace`

### 追踪/审查阶段

负责：

- 读取全部产物
- 输出 trace 文档或审查结论
- 在 `status.md` 备注列记录问题摘要

不负责：

- 不替其他阶段静默修改其完成状态
- 不直接代替实现阶段修代码

## 六、与 task-control 的联动

以下场景建议或必须注册到 `task-control`：

- 需求分析是分阶段进行的
- 设计需要依赖多个主题上下文
- 计划较长，存在中断风险
- 实现阶段会跨多个文件或多个步骤

推荐任务命名：

- `{version}-{topic}-需求分析`
- `{version}-{topic}-技术设计`
- `{version}-{topic}-执行计划`
- `{version}-{topic}-实现`
- `{version}-{topic}-追踪审查`

## 七、状态回写规则

每个阶段完成后都应更新 `status.md`：

- 需求阶段：补需求文档路径，分析状态完成
- 设计阶段：补设计文档路径，设计状态完成
- 计划阶段：补计划文档路径，计划状态完成
- 实现阶段：更新实现状态
- 审查阶段：记录发现，不代替其他阶段改完成态

补充要求：
- 如果一个主题已经存在 requirements / design / plan，并且实现阶段明确完成或验证完成，但仍没有 trace 文档，应视为流程未闭环。
- 此时默认动作不是结束，而是补一轮 `req-trace`。

## 八、变更处理

如果需求或设计发生变化：

1. 在 `status.md` 的变更记录中追加条目
2. 找到受影响主题
3. 把对应阶段状态改为需返工或待重做
4. 由对应阶段重新处理，而不是让其他阶段代改

## 九、参考模板

初始化新的 `status.md` 时，先读取 [status-template.md](references/status-template.md)。
