# 配置参考

`mudud` 从 TOML 配置文件读取配置。该文件控制监听端口、执行模式、存储路径与 io_uring 行为。

## 文件位置

服务端按以下顺序加载第一个存在的文件：

1. `--cfg /path/to/mudud.cfg`（或 `-c /path/to/mudud.cfg`）指定的路径（若提供）。
2. 当前工作目录下的 `./mudud.cfg`。
3. 用户主目录下的 `~/.mududb/mudud.cfg`。

若都不存在，`mudud` 返回 `NotFound` 错误。启动前可使用 `mudud init-cfg` 生成默认的 `./mudud.cfg`。

## 生成默认配置

```bash
mudud init-cfg
```

## 配置字段

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `mpk_path` | string | `"./mpk"` | 应用包目录路径。 |
| `db_path` | string | `"./data"` | 数据库文件目录路径。 |
| `listen_ip` | string | `127.0.0.1` | 监听 IP 地址。 |
| `http_listen_port` | u16 | `8300` | HTTP 管理 API 端口。 |
| `http_worker_threads` | usize | `1` | HTTP worker 线程数。 |
| `pg_listen_port` | u16 | `5432` | PostgreSQL wire protocol 端口。 |
| `component_target` | string | `p2` | Wasm 组件 ABI 目标。允许值：`p2`、`p3`。 |
| `enable_async` | boolean | `true` | 是否启用 WASI 组件运行时。 |
| `server_mode` | string | `"IOUring"` | `"Legacy"`、`"IOUring"` 或 `"Tokio"`。 |
| `tcp_listen_port` | u16 | `9527` | TCP 定帧协议端口。 |
| `tcp_multi_port` | boolean | `false` | 每个 worker 一个 TCP 监听器。 |
| `worker_threads` | usize | `0` | Worker 线程数。`0` 表示使用可用并行度。 |
| `io_uring_ring_entries` | u32 | `1024` | io_uring 完成队列深度。 |
| `io_uring_accept_multishot` | boolean | `true` | 启用 io_uring accept multishot。 |
| `io_uring_recv_multishot` | boolean | `true` | 启用 io_uring recv multishot。 |
| `io_uring_enable_fixed_buffers` | boolean | `false` | 启用 io_uring fixed buffers。 |
| `io_uring_enable_fixed_files` | boolean | `false` | 启用 io_uring fixed files。 |
| `routing_mode` | string | `"ConnectionId"` | `"ConnectionId"`、`"PlayerId"` 或 `"RemoteHash"`。 |
| `log_chunk_size` | u64 | `64 * 1024 * 1024` | io_uring 日志 chunk 大小，单位字节。 |
| `page_size` | usize | `4096` | 数据库页大小，单位字节。持久化配置；已有数据库变更该值需要迁移或重新初始化。 |

## 服务端与路由模式

- `server_mode`：控制后端 I/O/运行时路径。
  - `Legacy`：传统阻塞 I/O 路径，兼容性最好。
  - `IOUring`：基于 Linux io_uring 的高性能异步 I/O。
  - `Tokio`：基于 Tokio 的异步运行时。

- `routing_mode`：控制请求如何路由到工作线程。
  - `ConnectionId`（默认）：基于连接标识符路由。
  - `PlayerId`：基于应用层玩家/用户标识符路由。
  - `RemoteHash`：基于远程地址或哈希键路由。

## 示例 `mudud.cfg`

```toml
mpk_path = "./mpk"
db_path = "./data"
listen_ip = "127.0.0.1"
http_listen_port = 8300
http_worker_threads = 1
pg_listen_port = 5432
tcp_listen_port = 9527
server_mode = "Tokio"
worker_threads = 0
io_uring_ring_entries = 1024
io_uring_accept_multishot = true
io_uring_recv_multishot = true
io_uring_enable_fixed_buffers = false
io_uring_enable_fixed_files = false
routing_mode = "ConnectionId"
enable_async = true
tcp_multi_port = false
log_chunk_size = 67108864
page_size = 4096
```

兼容性与升级规则请参见[服务端配置契约](../reference/contracts/mudud_cfg_v1.md)。
