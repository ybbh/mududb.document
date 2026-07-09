# mcli 管理接口（HTTP）

本页介绍通过 `mcli` 的 HTTP 管理命令完成应用生命周期管理与分区路由查询。

## 前置条件

- `mudud` 服务端正在运行。
- HTTP 管理端口可访问（默认 `127.0.0.1:8300`）。

大多数管理命令通过 `--http-addr <host:port>` 指定目标服务器。

## 命令一览

### 列出已安装应用

```bash
mcli --http-addr 127.0.0.1:8300 app-list
```

### 安装应用包

```bash
mcli --http-addr 127.0.0.1:8300 app-install --mpk target/wasm32-wasip2/release/wallet.mpk
```

### 查看应用过程列表

```bash
mcli --http-addr 127.0.0.1:8300 app-detail --app wallet
```

### 查看单个过程详情

`--proc` 必须与 `--module` 一起使用。

```bash
mcli --http-addr 127.0.0.1:8300 app-detail --app wallet --module wallet --proc create_user
```

### 卸载应用

```bash
mcli --http-addr 127.0.0.1:8300 app-uninstall --app wallet
```

### 查看服务拓扑

```bash
mcli --http-addr 127.0.0.1:8300 server-topology
```

### 分区路由查询

按精确 key 路由：

```bash
mcli --http-addr 127.0.0.1:8300 partition-route --rule-name user_rule --key user-100
```

按范围路由：

```bash
mcli --http-addr 127.0.0.1:8300 partition-route --rule-name user_rule --start 100 --end 200
```

多列 key 示例：

```bash
mcli --http-addr 127.0.0.1:8300 partition-route --rule-name order_rule --key tenant-1,order-100
```

## 参数约束

- `app-detail`：`--proc` 必须与 `--module` 一起使用。
- `partition-route`：`--key` 与 `--start/--end` 二选一，不可同时使用。

## 返回结果

- 默认输出格式化 JSON。
- 添加 `--compact` 输出紧凑 JSON。
- 出错时命令返回非 0，并在 stderr 输出错误原因。
