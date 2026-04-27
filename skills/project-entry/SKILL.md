---
name: project-entry
description: Codex 的项目入口技能。适用于进入一个项目后的大多数任务起点，包括代码修改、缺陷修复、代码阅读、需求分析、技术设计、执行计划、实现推进、闭环追踪、基础设施查询、业务文档沉淀和长任务恢复。它负责根据任务意图自动选择并串联 `dev-constraints`、`task-control`、`project-skill-convention`、`req-analysis`、`design-phase`、`plan-phase`、`req-trace`、`dev-small-tool`、`docs-desc-generation` 等技能，作为整套 Codex 项目工作流的统一入口。
---

# 项目入口

本技能是项目工作流的统一入口。正常情况下，项目根 `AGENTS.md` 会先把任务导到这里；如果项目还没接好入口，也可以显式使用本技能。

## 入口原则

1. 先识别任务的主要目标，再决定加载哪些技能。
2. 如果任务描述模糊，但明显属于项目工作，优先做语义分类，不要停在泛化回复。
3. 如果一句话同时包含多个阶段，优先进入当前最先缺失的阶段。
4. 长任务、可中断任务、恢复类任务自动接入 `task-control`。
5. requirements、design、plan、trace 一类结构化交付任务自动接入 `project-skill-convention`。
6. 日常开发、代码修改、代码阅读、配置调整、缺陷修复至少接入 `dev-constraints`。

## 任务分类路由表

### 1. 日常开发 / 缺陷修复 / 代码阅读

加载顺序：
- `dev-constraints`
- `task-control`，仅当任务较大、跨文件、可中断或明确要求继续推进时

识别信号：
- 修 bug、排查问题、改代码、改接口、改配置、解释代码、继续实现
- 用户虽然没说“开发”，但目标明显是修改项目内容

### 2. 需求分析

加载顺序：
- `project-skill-convention`
- `req-analysis`
- `task-control`，仅当主题较大时

识别信号：
- 分析需求、整理需求、输出 requirements、补边界条件、补异常流
- 从原始描述转成结构化需求

### 3. 技术设计

加载顺序：
- `project-skill-convention`
- `design-phase`
- `task-control`，仅当主题较大时

识别信号：
- 出技术方案、出设计文档、设计表结构、设计接口、设计时序
- 关注幂等、事务、一致性、兼容、回滚、补偿等设计问题

### 4. 执行计划

加载顺序：
- `project-skill-convention`
- `plan-phase`
- `task-control`，仅当主题较大时

识别信号：
- 拆计划、拆阶段、拆实施步骤、列验证项、列风险点
- 把设计变成可执行落地计划

### 5. 实现推进

加载顺序：
- `project-skill-convention`，仅当当前主题已有 requirements / design / plan 主线时
- `dev-constraints`
- `task-control`，默认建议接入

识别信号：
- 按计划继续实现、进入开发阶段、开始落地、恢复实现
- 用户明确说“继续做”“接着做”“开始改”

实现阶段优先读取：
- `status.md`
- 当前主题对应的 plan 文档
- 必要时读取 design 和 requirements

实现收尾补充规则：
- 如果任务语义已经进入“完成实现 / 已完成开发 / 已完成验证 / 收尾交付 / 准备提测 / 准备合并 / 需要核对是否一致”这类收尾状态，应自动补接：
  - `project-skill-convention`
  - `req-trace`
- 默认不要等用户显式说“做 trace 审查”才进入追踪阶段。
- 目标是让实现完成后的主题至少补一版 trace 文档，而不是长期停留在 requirements / design / plan / 实现记录，`trace/` 目录始终为空。

### 6. 闭环追踪 / 差异审查

加载顺序：
- `project-skill-convention`
- `req-trace`
- `task-control`，仅当审查范围较大时

识别信号：
- 检查是否闭环、审查是否一致、找缺口、输出 trace、核对实现与文档
- 也包括“这个任务做完了，帮我收尾检查一下”“验证完成后补一版审查”“交付前做一致性核对”这类说法

### 7. 基础设施只读查询

加载顺序：
- `dev-small-tool`

识别信号：
- 查表结构、查索引、查 Nacos、查 ES、查数据库字段、查链路或依赖

### 8. 业务域文档沉淀

加载顺序：
- `docs-desc-generation`

识别信号：
- 梳理业务域、沉淀长期说明、初始化 docs/desc、总结对象和状态流转

### 9. 项目初始化 / 项目接入

加载顺序：
- `dev-constraints`
- `task-control`

识别信号：
- 初始化当前项目
- 建立项目骨架
- 接入 Codex 项目规则
- 初始化 docs / plans / requirements / trace
- 建立 AGENTS 和任务记录入口

初始化动作要求：
- 先执行 `scripts/init_project_scaffold.py <项目根目录>`，路径相对于当前技能目录解析
- 创建或确认项目根 `AGENTS.md`
- 创建 `docs/codex/v1/requirements/.gitkeep`
- 创建 `docs/codex/v1/designs/.gitkeep`
- 创建 `docs/codex/v1/plans/.gitkeep`
- 创建 `docs/codex/v1/trace/.gitkeep`
- 创建 `docs/codex/v1/status.md`
- 创建 `.codex/plans/main/TASKS.md`
- 如果用户只是说“初始化项目”，也不要只停在生成 `AGENTS.md`
- 如果缺少 `.codex/plans/main/TASKS.md`，说明初始化未完成，应立即补齐

### 10. 安装 / 导出 / 说明类任务

按目标选择：
- 安装：`starter-kit-import`
- 导出：`starter-kit-backup`
- 解释说明：`starter-kit-guide`

## 模糊说法的自动判断

遇到下面这类说法时，按以下方式判断：

- “帮我看下这个问题”
  默认按开发问题处理，进入 `dev-constraints`；如果明显是恢复上次任务，再补 `task-control`。
- “继续上次那个需求”
  优先进入 `task-control`，再根据已有阶段材料进入 requirements、design、plan 或实现。
- “先把这个事情理清楚”
  如果偏业务目标和边界，进入 `req-analysis`；如果偏技术方案，进入 `design-phase`。
- “给个落地方案”
  如果还没有明确需求，先补 `req-analysis`；如果已有需求背景，进入 `design-phase` 或 `plan-phase`。
- “帮我查一下这个库/表/配置”
  进入 `dev-small-tool`。
- “这个任务已经做完了，帮我检查一下”
  默认进入 `req-trace`；如果实现仍需补改，再回到 `dev-constraints`。
- “初始化当前项目”
  进入项目初始化流程，补齐 `AGENTS.md`、`docs/codex/v1`、`.gitkeep`、`status.md` 和 `.codex/plans/main/TASKS.md`。

## 启动动作

当通过本技能进入任务时，应优先做这些事：

1. 判断任务属于哪一类。
2. 明确将要串联的技能。
3. 如有必要，说明为什么要接入 `task-control` 或 `project-skill-convention`。
4. 如果任务属于结构化交付流，先进入 `project-skill-convention` 再进入具体阶段技能。
5. 如果任务只是普通开发，则进入 `dev-constraints`。

## 子代理编排

当主任务需要派发给子代理时，本技能继续作为总入口来决定派发协议。

主代理至少要做：

1. 先判断子任务属于哪一类，再决定子代理必须遵守哪些技能。
2. 如果子任务是长任务、阶段任务、或者后续可能恢复，先接入 `task-control`。
3. 把项目根 `AGENTS.md` 视为持续生效的项目规则，不因拆成子代理而失效。
4. 在派发消息中写明：任务目标、边界、必读文件、必守技能、回传格式。

建议回传内容至少包含：
- 改动文件
- 已完成验证
- 未完成项或风险
- 推荐的下一步

## 目标

通过“项目根 `AGENTS.md` + 本入口技能”的组合，为 Codex 提供接近项目级自动编排的体验：
- 项目根规则负责优先导流
- 本技能负责任务识别和技能串联
- 不依赖 Hook
- 保持纯 Codex 目录分发形式
- 让用户尽量用自然语言提任务，也能高概率进入正确流程
