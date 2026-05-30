# 配置参考

默认配置文件为 `${HOME}/.mududb/mududb_cfg.toml`。

推荐分组：

- 网络监听地址
- 存储路径
- HTTP 管理端口
- 工作线程和调度参数
- 日志级别

具体选项模式应遵循当前版本源代码中的配置结构。

## 值得关注的配置字段

- `tcp_multi_port` (bool): 当为 true 且后端支持时，服务器可为每个工作线程打开一个 TCP 监听器，以提高 accept/亲和性并减少争用。默认值：`false`。

- `io_uring_worker_threads` (int): 如果大于 0，运行时将保留此数量的工作线程用于 io_uring 后端。如果设置为 `0`，服务器将根据可用 CPU 核心数推导一个合理的默认值。

- `io_uring_ring_entries` (int): 每个工作线程的 io_uring 提交/完成队列深度。较大的值可能提高吞吐量，但会以内存为代价。默认值：`1024`。

- `io_uring_accept_multishot`, `io_uring_recv_multishot` (bool): 启用 multishot accept/recv 以减少系统调用开销并提高连接吞吐量。默认值：`true`。

- `io_uring_enable_fixed_buffers`, `io_uring_enable_fixed_files` (bool): 启用后，运行时将使用预注册的固定缓冲区或文件，以避免动态分配并加速热 I/O 路径。这些选项需要额外的设置，以灵活性换取性能。默认值：`false`。

- `io_uring_log_chunk_size` (bytes): 用于内部 io_uring 相关分块或日志轮转的大小。默认值：67108864 (64MB)。

## 服务器和路由模式

- `server_mode` (enum): 控制后端 I/O/运行时路径。可能的值：
  - `Legacy` (0): 传统的阻塞 I/O 路径，以获得最大兼容性。
  - `IOUring` (1): 使用基于 Linux io_uring 的内核路径实现高性能异步 I/O。
  - `Tokio` (2): 使用基于 Tokio 的异步运行时。

- `routing_mode` (enum): 控制请求如何路由到工作线程：
  - `ConnectionId` (0, 默认): 基于连接标识符路由。
  - `PlayerId` (1): 基于应用层玩家/用户标识符路由。
  - `RemoteHash` (2): 使用远程地址或哈希键进行基于哈希的路由。

这些字段会影响性能和兼容性；对于高并发部署，建议优先使用 `IOUring` 或 `Tokio`，对于兼容性测试则使用 `Legacy`。
