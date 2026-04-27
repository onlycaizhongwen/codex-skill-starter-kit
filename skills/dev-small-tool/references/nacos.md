# 子命令：nacos

查看 Nacos 配置。适合查整个配置内容，也适合按关键词过滤某些 key。

## 推荐执行方式

```bash
curl -s "http://{nacos-addr}/nacos/v1/cs/configs?dataId={dataId}&group=DEFAULT_GROUP&tenant={namespace}"
```

## 输出规范

- 无过滤条件时：输出完整配置，但敏感字段脱敏
- 有过滤关键词时：只展示命中的配置项或命中行
- 如果涉及多个 dataId，分别标明来源
- 如遇 403 或认证失败，报告错误并提示检查认证或网络