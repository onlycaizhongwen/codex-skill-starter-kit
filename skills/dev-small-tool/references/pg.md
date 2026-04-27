# 子命令：db / pg

用于 PostgreSQL 的只读元数据查询。

## 典型场景

- 列出表
- 查看字段结构
- 查看索引
- 查看字段注释
- 查看执行计划

## 常见 SQL

| 场景 | SQL |
|------|-----|
| 列出表 | `SELECT tablename FROM pg_tables WHERE schemaname = ''public''` |
| 字段概览 | `SELECT column_name, data_type, is_nullable, column_default FROM information_schema.columns WHERE table_schema = ''public'' AND table_name = ''{table}'' ORDER BY ordinal_position` |
| 索引 | `SELECT indexname, indexdef FROM pg_indexes WHERE schemaname = ''public'' AND tablename = ''{table}''` |
| 字段详情 | `SELECT column_name, data_type, character_maximum_length, is_nullable, column_default FROM information_schema.columns WHERE table_schema = ''public'' AND table_name = ''{table}'' ORDER BY ordinal_position` |
| 执行计划 | `EXPLAIN {sql}` |

## 输出规范

- 输出字段名、类型、可空、默认值、注释等关键列
- 索引说明中保留索引名、定义和类型
- `EXPLAIN` 时重点关注 Seq Scan / Index Scan

## 依赖提示

若缺少 `psycopg2`，先说明依赖缺失，再在用户允许下安装。