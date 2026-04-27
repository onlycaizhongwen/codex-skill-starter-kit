---
name: dev-small-tool
description: Codex 的基础设施只读查询技能。适用于查看数据库表结构、索引、ES mapping、ES 文档、Nacos 配置，以及追踪服务依赖的中间件连接信息。当任务涉及“查配置”“查索引”“查表结构”“查数据库”“DESC”“nacos”“mapping”“文档数”等场景时优先使用，核心原则是不猜，直接查。
---

# 开发小工具

把它作为项目中的基础设施只读查询入口。核心原则：**不猜，直接查**。

## 适用场景

- 查 Nacos 配置
- 查 ES 索引 mapping
- 查 ES 文档数据
- 查 ES 文档数和索引列表
- 查数据库表结构、字段、索引、DDL、执行计划
- 从服务配置追踪中间件连接关系

## 子命令路由

根据用户意图识别子命令，不要求用户精确输入命令名：

| 意图 | 子命令 | 典型说法 |
|------|--------|----------|
| 查看或过滤 Nacos 配置 | `nacos` | “查下配置”“nacos 里 ES 地址是什么” |
| 查看 ES 索引结构 | `es index` | “看 mapping”“索引结构”“字段有哪些” |
| 查询 ES 文档 | `es search` | “查一下 ES 数据”“搜 session_id=xxx” |
| 统计 ES 文档数 | `es count` | “这个索引多少条”“文档数” |
| 列出 ES 索引 | `es list` | “有哪些索引”“索引列表” |
| 数据库表结构/索引 | `db` | “看一下表结构”“DESC xxx”“索引是什么” |
| MySQL 查询 | `mysql` | “mysql 查一下 xxx” |
| PostgreSQL 查询 | `pg` | “pg 查一下 xxx” |
| 串联追踪基础设施 | `trace` | “这个服务连了哪些中间件”“trace 一下” |

识别后按需读取对应 reference：

- `nacos` -> `references/nacos.md`
- `es index/search/count/list` -> `references/es.md`
- `mysql` -> `references/mysql.md`
- `pg` -> `references/pg.md`
- `db` -> 根据 JDBC URL 或 server type 自动判断后走 `mysql` 或 `pg`
- `trace` -> `references/trace.md`

## 连接配置文件

推荐把敏感连接信息放在：

```text
~/.codex/dev-small-tool/connections.json
```

不要把密码、IP、端口写进技能文档、项目文档或 memory。

推荐结构：

```json
{
  "default_env": "dev",
  "environments": {
    "dev": {
      "servers": {
        "mysql": { "type": "mysql", "host": "127.0.0.1", "port": 3306, "username": "root", "password": "***" },
        "es": { "type": "es", "uri": "http://127.0.0.1:9200" },
        "nacos": { "type": "nacos", "addr": "127.0.0.1:8848", "username": "", "password": "" }
      },
      "databases": [
        { "name": "app-db", "server": "mysql", "database": "app", "comment": "应用主库" }
      ],
      "es": [
        { "name": "app-es", "server": "es", "index_prefix": "app_", "comment": "搜索索引" }
      ],
      "nacos": [
        { "name": "app-nacos", "server": "nacos", "namespace": "public", "comment": "配置中心" }
      ]
    }
  }
}
```

## 连接信息获取顺序

1. 用户明确指定了已保存连接名时，直接读取 `~/.codex/dev-small-tool/connections.json`
2. 用户没有指定时，优先从当前项目配置中自动检测
3. 当前项目检测不到时，再向用户要连接信息
4. 同一会话内已确认的连接信息直接复用，不重复询问

## 输出要求

- 优先表格化输出
- 只输出和当前问题相关的字段
- 涉及密码或 token 时必须脱敏
- 查不到就明确说“未找到”或“连接失败原因”，不要猜测
- DDL、mapping、执行计划这类长输出，只保留用户需要的关键部分；必要时附上原始片段摘要

## 安全约束

- 所有操作默认只读
- 不执行写数据库、不改配置、不删索引
- ES 仅限 `_mapping`、`_search`、`_count`、`_cat/indices` 等只读查询
- Nacos 仅查询，不写入
- 连接超时应保守设置，避免长时间阻塞

## 异常处理

| 场景 | 处理 |
|------|------|
| 没有项目配置，也没有保存连接 | 询问用户提供连接信息 |
| Nacos / ES / DB 不可达 | 明确报告连接失败原因 |
| 索引或表不存在 | 提示先列出可用索引或表 |
| 数据库类型不明确 | 从 JDBC URL、server type 或端口判断；仍不明确再询问用户 |
| 驱动缺失 | 先说明缺少依赖，再在用户允许的前提下安装 |
| 用户输入过于模糊 | 展示子命令路由并引导澄清 |

## 与项目技能的关系

- 当 `dev-constraints` 遇到“查表结构、查索引、查配置、查 ES mapping”这类任务时，应优先转到本技能
- 本技能负责“查真实元数据”，不负责项目实现流程
- 若查询结果会影响实现决策，再把结论交回 `dev-constraints`、`project-entry` 或其他技能继续推进