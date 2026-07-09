# 服务端管理

`mudud` 是 MuduDB 服务端进程。它托管数据库内核、运行已安装的 MPK 包，并暴露三类监听：TCP 协议端点、HTTP 管理端点、PostgreSQL 兼容 wire protocol 端口。

## 前置条件

- `mudud` 与 `mcli` 已安装并位于 `PATH`。
- 配置文件存在于 `./mudud.cfg`、`~/.mududb/mudud.cfg`，或通过 `--cfg` 指定的路径。
- 在 Linux 上使用 `io_uring` 模式需要运行时存在 `liburing-dev`。
- 建议以较高的文件描述符限制启动（`ulimit -n 65535` 是一个实用基线）。

## 启动服务端

### 默认启动

```bash
ulimit -n 65535
mudud
```

若当前目录不存在 `./mudud.cfg`，`mudud` 会检查 `~/.mududb/mudud.cfg`。可用以下命令生成默认配置：

```bash
mudud init-cfg
```

### 使用自定义配置启动

```bash
ulimit -n 65535
mudud serve --cfg ./config/mudud.cfg
```

### 启动后

启动后 `mudud` 会记录生效配置并打开三个监听：

- TCP 协议：`listen_ip:tcp_listen_port`（默认 `127.0.0.1:9527`）
- HTTP 管理：`listen_ip:http_listen_port`（默认 `127.0.0.1:8300`）
- PostgreSQL wire protocol：`listen_ip:pg_listen_port`（默认 `127.0.0.1:5432`）

## 停止服务端

向进程发送 `SIGINT`（`Ctrl+C`）或 `SIGTERM`。`mudud` 会执行优雅关闭，等待在途工作完成后再退出。

## 验证服务端

使用 `mcli` 检查 HTTP 管理端点：

```bash
mcli --http-addr 127.0.0.1:8300 app-list
mcli --http-addr 127.0.0.1:8300 server-topology
```

若命令返回 JSON 输出，说明服务端正在运行且可访问。

## 服务端模式

| 模式 | 适用场景 |
|------|----------|
| `Legacy` | 最大兼容性；单 TCP/PG 服务模型。 |
| `IOUring` | Linux 上基于 io_uring 的高性能异步 I/O（Linux 推荐使用）。 |
| `Tokio` | 当 `io_uring` 不可用时使用的可移植异步运行时。 |

## 常见问题

- **地址已被占用**：其他进程占用了某个配置端口。在 `mudud.cfg` 中修改冲突端口。
- **权限被拒绝**：可能没有权限绑定到配置的 `listen_ip` 或端口。本地开发建议使用 `127.0.0.1` 与 1024 以上端口。
- **打开文件过多**：启动前使用 `ulimit -n 65535` 提高文件描述符限制。
- **io_uring 不可用**：若不在 Linux 或缺少 `liburing-dev`，将 `server_mode` 切换为 `Tokio`。

所有可用选项请参见[配置参考](configuration.md)。
