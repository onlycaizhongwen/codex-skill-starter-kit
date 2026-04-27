---
name: session-cleanup
description: Codex 的安全版会话清理技能。适用于预览和清理 `~/.codex/sessions/` 下的旧会话文件，以及明确可删的临时残留，用来释放磁盘空间。默认只做保守清理：不删除 memories、skills、rules、auth、config、history 索引和 sqlite 状态文件。
---

# 会话清理

这是 Codex 安全版会话清理技能。目标是清理**明确可删**的旧会话和临时残留，而不是对 `~/.codex/` 做激进清理。

## 一、默认原则

1. 先预览，再确认，再执行
2. 默认只清理旧 `sessions/` 会话文件
3. 对 `tmp/`、`.tmp/` 只做非常保守的候选清理
4. 不碰全局索引、认证、配置、技能、规则和 sqlite 状态文件

## 二、允许清理的范围

### 1. 主清理目标

- `~/.codex/sessions/` 下明显过旧的 rollout 会话文件
- `~/.codex/sessions/` 下已经没有继续价值的历史 JSONL 会话记录

### 2. 可选清理目标

- `~/.codex/tmp/` 下明显过旧的临时目录
- `~/.codex/.tmp/` 下明显过旧的临时目录
- `.DS_Store` 一类无意义系统残留

> 对 `tmp/` 和 `.tmp/` 的清理必须额外谨慎，只建议在用户明确选择时执行。

## 三、禁止清理的范围

以下内容默认绝对不删：

- `~/.codex/memories/`
- `~/.codex/skills/`
- `~/.codex/rules/`
- `~/.codex/auth.json`
- `~/.codex/config.toml`
- `~/.codex/history.jsonl`
- `~/.codex/session_index.jsonl`
- `~/.codex/*.sqlite`
- `~/.codex/*.sqlite-shm`
- `~/.codex/*.sqlite-wal`
- 当前正在使用或最近刚修改的会话文件

## 四、活跃会话保护

执行删除前，必须先识别最近仍在变化的会话文件并排除。

保守规则：

- 最近 1 天内修改过的 `sessions/` 文件默认视为高风险，不进入默认清理范围
- 只有明显很旧的文件才进入候选列表
- 若用户要缩短时间阈值，必须再次明确确认

## 五、推荐流程

### 1. 扫描与预览

扫描以下内容：

- `~/.codex/sessions/` 中的旧会话文件
- `~/.codex/tmp/` 中的旧临时目录
- `~/.codex/.tmp/` 中的旧临时目录

预览时至少展示：

- 路径
- 最后修改时间
- 大小
- 所属类别（sessions / tmp / .tmp）

### 2. 推荐清理选项

只提供保守选项：

- A. 清理 30 天前的 `sessions/` 历史会话
- B. 清理 60 天前的 `sessions/` 历史会话
- C. 在 A/B 的基础上，再额外清理 30 天前的 `tmp/` 与 `.tmp/`

不默认提供“全部清空 `~/.codex/`”这类危险选项。

### 3. 执行前确认

执行前必须再次明确告诉用户：

- 会删除哪些目录或文件
- 不会删除哪些关键文件
- 删除后旧会话恢复能力会下降

### 4. 执行后验证

执行后至少验证：

- 目标会话文件确实已删
- 被禁止清理的文件仍然存在
- `history.jsonl`、`session_index.jsonl`、`memories/`、`skills/`、`rules/`、`config.toml`、`auth.json` 未被修改

## 六、推荐命令思路

### 1. 预览旧会话

```powershell
Get-ChildItem -Recurse -File "$HOME\.codex\sessions" | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } | Select-Object FullName, Length, LastWriteTime
```

### 2. 预览旧临时目录

```powershell
Get-ChildItem -Force "$HOME\.codex\tmp","$HOME\.codex\.tmp" -ErrorAction SilentlyContinue | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } | Select-Object FullName, LastWriteTime
```

### 3. 删除前保护名单检查

执行删除前，必须显式检查这些路径仍会被排除：

- `$HOME\.codex\memories`
- `$HOME\.codex\skills`
- `$HOME\.codex\rules`
- `$HOME\.codex\auth.json`
- `$HOME\.codex\config.toml`
- `$HOME\.codex\history.jsonl`
- `$HOME\.codex\session_index.jsonl`

## 七、异常处理

| 场景 | 处理 |
|------|------|
| 扫描不到 `.codex/sessions/` | 说明当前机器可能尚无可清理历史 |
| 会话目录中有最近修改文件 | 跳过，不清理 |
| `tmp/` 或 `.tmp/` 下内容无法判断用途 | 跳过，宁可不删 |
| 文件被占用 | 跳过并告知用户 |
| 用户要求激进全删 | 明确提示超出本技能安全边界，拒绝默认执行 |

## 八、定位

本技能属于本地环境维护工具，不属于项目交付主流程：

- 不参与 requirements/design/plan/trace
- 不修改项目代码
- 不修改业务文档
- 只负责安全清理本机旧会话残留