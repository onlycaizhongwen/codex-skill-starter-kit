# 子命令：es

适用于 ES mapping、索引列表、文档查询、文档计数等只读操作。

## es index

查看索引 mapping、文档数、分片信息、别名。

推荐命令：

```bash
curl -s "http://{es-addr}/{index-name}/_mapping"
curl -s "http://{es-addr}/{index-name}/_stats"
curl -s "http://{es-addr}/{index-name}/_alias"
```

输出时优先整理成字段表：字段名、类型、说明。不要凭空补字段说明。

## es search

查询文档样本数据。

推荐命令：

```bash
curl -s -X POST "http://{es-addr}/{index-name}/_search?size={size}" -H "Content-Type: application/json" -d '{"query":{...}}'
```

输出要求：

- 默认只展示少量样本
- 动态整理成表格
- 时间戳字段尽量转成人类可读时间
- 无结果时明确说未找到，不输出空表格

## es count

```bash
curl -s "http://{es-addr}/{index-name}/_count"
```

直接显示数量。多索引时分别展示。

## es list

```bash
curl -s "http://{es-addr}/_cat/indices?v"
```

输出索引名、文档数、存储大小、状态等关键列即可。