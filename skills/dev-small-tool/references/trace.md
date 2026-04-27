# 子命令：trace

从服务配置中追踪它依赖的中间件连接关系，例如 Nacos、MySQL、ES、Redis。

## 建议步骤

1. 从项目配置中找到服务名和配置中心位置
2. 拉取配置
3. 解析数据库、ES、Redis、消息队列等连接信息
4. 只输出实际识别到的中间件

## 输出格式

```text
## 服务追踪：{service-name}

### Nacos
- 地址：{nacos-addr}
- 命名空间：{namespace}

### MySQL
- 地址：{host}:{port}
- 数据库：{database}

### Elasticsearch
- 地址：{es-addr}
- 索引前缀：{prefix}
```

不确定的信息标记“待确认”，不要猜。