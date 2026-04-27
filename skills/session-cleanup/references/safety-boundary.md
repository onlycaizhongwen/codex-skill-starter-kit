# 安全边界

## 默认保留

- memories
- skills
- rules
- auth.json
- config.toml
- history.jsonl
- session_index.jsonl
- sqlite 状态文件

## 默认可删

- 30 天前的 `sessions/` 历史会话文件
- 30 天前且用户明确同意的 `tmp/`、`.tmp/` 旧临时目录

## 不建议做的事

- 不要一上来清空整个 `~/.codex/`
- 不要删除最近 1 天内修改的会话
- 不要删除 sqlite 文件
- 不要删除 history / session 索引