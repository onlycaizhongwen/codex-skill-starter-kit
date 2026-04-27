# 最小示例项目

这是一个用于演示 `codex-skill-starter-kit` 接入后的最小项目模板。它的重点不是业务代码，而是演示项目入口、自动分流、阶段文档和长任务记录如何配合。

## 目录说明

- `AGENTS.md`：项目级规则入口
- `docs/codex/v1/status.md`：阶段状态文档
- `docs/codex/v1/requirements/`：需求文档目录
- `docs/codex/v1/designs/`：设计文档目录
- `docs/codex/v1/plans/`：计划文档目录
- `docs/codex/v1/trace/`：闭环审查目录
- `.codex/plans/main/TASKS.md`：长任务入口文件

## 怎么使用这个示例

1. 先确保已经把 starter kit 安装到 `~/.codex/skills/`。
2. 进入这个示例项目目录。
3. 直接对 Codex 用自然语言描述任务，不必手动点名全部技能。
4. 由项目根 `AGENTS.md` 和 `project-entry` 自动做第一轮识别与分流。

## 第一条建议口令

进入项目后，可以先说：

```text
请按项目入口规则初始化当前项目工作流，并补齐 AGENTS.md、docs/codex/v1 骨架和 .codex/plans/main/TASKS.md。
```

## 可直接复制的任务示例

### 1. 普通开发任务

```text
请按项目规则排查这个项目里的示例缺陷，并说明准备如何修改。
```

预期流转：

```text
AGENTS.md -> project-entry -> dev-constraints
```

### 2. 需求分析任务

```text
请按项目规则分析“新增用户注册审核流”这个需求，并输出 requirements 文档。
```

预期流转：

```text
AGENTS.md -> project-entry -> project-skill-convention -> req-analysis
```

### 3. 技术设计任务

```text
请基于已有 requirements，为“新增用户注册审核流”输出技术设计，补充接口、状态流转和回滚策略。
```

预期流转：

```text
AGENTS.md -> project-entry -> project-skill-convention -> design-phase
```

### 4. 执行计划任务

```text
请按项目规则把这个设计拆成执行计划，明确改动范围、验证方式和风险点。
```

预期流转：

```text
AGENTS.md -> project-entry -> project-skill-convention -> plan-phase
```

### 5. 长任务恢复

```text
请按项目规则恢复上次中断的任务，先读取已有记录，再继续推进未完成部分。
```

预期流转：

```text
AGENTS.md -> project-entry -> dev-constraints -> task-control
```

### 6. 基础设施查询

```text
请按项目规则查一下这个项目假设场景中的 user_profile 表结构、索引和配置项。
```

预期流转：

```text
AGENTS.md -> project-entry -> dev-small-tool
```

### 7. 闭环审查

```text
请按项目规则审查“新增用户注册审核流”是否已经形成 requirements、design、plan、实现和验证的闭环。
```

预期流转：

```text
AGENTS.md -> project-entry -> project-skill-convention -> req-trace
```

## 演示主链路

```text
AGENTS.md
-> project-entry
-> req-analysis
-> design-phase
-> plan-phase
-> 实现
-> req-trace
```

## 这个示例的用途

- 帮团队理解“自然语言任务 -> 自动识别 -> 技能流转”这套机制
- 帮新项目快速照着搭建目录和入口
- 帮演示 starter kit 在真实研发流程中的用法
