# 适配器

适配器层连接不同的后端能力，包括 SQLite、PostgreSQL、MySQL 和 MuduDB 内核本身。适配器文档应描述支持的行为、测试覆盖范围和已知差异。

## 异步会话循环 (async_session_loop)

- 当连接配置启用异步会话循环（`async_session_loop=true`）时，适配器将会话管理和 I/O 命令转发给运行异步运行时的专用后台管理线程。该管理线程保持长期存活的 AsyncClient 连接，并通过基于通道的命令队列序列化工作。

- 行为差异：
  - 同步路径（`async_session_loop=false`）：每次 `mudu_open` 创建一个 `SyncClient`，调用在调用线程上以阻塞方式执行。
  - 异步路径（`async_session_loop=true`）：适配器方法将命令（Open/Close/Get/Put/Range/Query/Command/Batch）加入管理线程队列，并通过小型同步通道等待响应，从而减少调用线程上的阻塞并提高并发性。

- 性能说明：异步循环减少了每次调用的阻塞和线程使用，但引入了运行时和通道开销。在高并发场景或使用 IOUring/Tokio 后端时，选择异步循环。
