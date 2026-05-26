# mcli

`mcli` 是 MuduDB 的命令行客户端，覆盖交互式 SQL、HTTP 管理和过程调用。

常用命令：

```bash
mcli --addr 127.0.0.1:9527 shell --app demo
mcli --http-addr 127.0.0.1:8300 app-list
mcli --http-addr 127.0.0.1:8300 server-topology
```

交互式 shell 的查询结果在 TTY 环境中以表格形式显示。
