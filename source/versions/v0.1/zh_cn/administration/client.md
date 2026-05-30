# 客户端

`mcli` 是 MuduDB 的命令行客户端，用于交互式 SQL、HTTP 管理和过程调用。

常用命令：

```bash
mcli --addr 127.0.0.1:9527 shell --app demo
mcli --http-addr 127.0.0.1:8300 app-list
mcli --http-addr 127.0.0.1:8300 server-topology
```

在 TTY 会话中，查询结果默认以交互式表格形式显示。
