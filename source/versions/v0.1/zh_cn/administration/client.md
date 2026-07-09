# 客户端

`mcli` 是 MuduDB 命令行客户端，支持交互式 SQL、HTTP 管理与过程调用。

## 连接选项

- `--addr <host:port>` —— SQL shell 与过程调用使用的 TCP 协议端点（默认 `127.0.0.1:9527`）。
- `--http-addr <host:port>` —— 管理命令使用的 HTTP 管理端点（默认 `127.0.0.1:8300`）。

## 交互式 SQL shell

```bash
mcli --addr 127.0.0.1:9527 shell --app demo
```

在 shell 中可以执行 SQL 语句、元命令，使用 `\q` 退出。

## 常用管理命令

列出已安装应用：

```bash
mcli --http-addr 127.0.0.1:8300 app-list
```

查看服务拓扑：

```bash
mcli --http-addr 127.0.0.1:8300 server-topology
```

解析分区路由：

```bash
mcli --http-addr 127.0.0.1:8300 partition-route --rule-name user_rule --key user-100
```

## 调用过程

```bash
mcli --addr 127.0.0.1:9527 --http-addr 127.0.0.1:8300 app-invoke \
  --app wallet \
  --module wallet \
  --proc transfer_funds \
  --json '{"from_user_id": 1001, "to_user_id": 1002, "amount": 1200}'
```

## 输出

- 在 TTY 会话中，查询结果默认以表格形式显示。
- 管理命令默认输出格式化 JSON；添加 `--compact` 可输出紧凑 JSON。
- 出错时 `mcli` 返回非 0 退出码，并将错误输出到 stderr。

完整命令参考请参见 [mcli HTTP 管理接口](../reference/mcli-admin.md)。
