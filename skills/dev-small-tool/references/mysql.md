# 子命令：db / mysql

用于 MySQL 的只读元数据查询。

## 典型场景

- 列出所有表
- 查看表结构
- 查看索引
- 查看建表语句
- 查看字段详情
- 查看执行计划

## 常见 SQL

| 场景 | SQL |
|------|-----|
| 列出表 | `SHOW TABLES` |
| 表结构 | `DESC {table}` |
| 索引 | `SHOW INDEX FROM {table}` |
| 建表语句 | `SHOW CREATE TABLE {table}` |
| 字段详情 | `SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, COLUMN_COMMENT FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = '{db}' AND TABLE_NAME = '{table}' ORDER BY ORDINAL_POSITION` |
| 全库索引 | `SELECT TABLE_NAME, INDEX_NAME, COLUMN_NAME, SEQ_IN_INDEX, NON_UNIQUE, INDEX_TYPE FROM information_schema.STATISTICS WHERE TABLE_SCHEMA = '{db}' ORDER BY TABLE_NAME, INDEX_NAME, SEQ_IN_INDEX` |
| 执行计划 | `EXPLAIN {sql}` |

## 输出规范

- `SHOW CREATE TABLE` 优先保留完整 DDL
- 表结构和字段详情整理成表格
- 索引输出索引名、列、是否唯一、类型
- `EXPLAIN` 时重点解释是否走索引、扫描行数、Extra

## 依赖提示

若缺少 `pymysql`，先说明依赖缺失，再在用户允许下安装。