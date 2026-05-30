# Configuration Reference

The default configuration file is `${HOME}/.mududb/mududb_cfg.toml`.

Recommended groups:

- network listen addresses
- storage paths
- HTTP management port
- worker and scheduling parameters
- logging level

The exact option schema should follow the configuration structures in the source code for the active version.

## Notable configuration fields

- `tcp_multi_port` (bool): When true and supported by the backend, the server may open one TCP listener per worker to improve accept/affinity and reduce contention. Default: `false`.

- `io_uring_worker_threads` (int): If > 0, the runtime will reserve this number of worker threads for the io_uring backend. If set to `0`, the server derives a sensible default from available CPU cores.

- `io_uring_ring_entries` (int): The depth of the per-worker io_uring submission/completion queue. Larger values may improve throughput at the cost of memory. Default: `1024`.

- `io_uring_accept_multishot`, `io_uring_recv_multishot` (bool): Enable multishot accept/recv for reduced syscall overhead and improved connection throughput. Defaults: `true`.

- `io_uring_enable_fixed_buffers`, `io_uring_enable_fixed_files` (bool): When enabled, the runtime uses pre-registered fixed buffers or files to avoid dynamic allocations and speed up hot I/O paths. These options require additional setup and trade flexibility for performance. Defaults: `false`.

- `io_uring_log_chunk_size` (bytes): Size used for internal io_uring-related chunking or log rotation. Default: 67108864 (64MB).

## Server and routing modes

- `server_mode` (enum): Controls backend I/O/runtime path. Possible values:
  - `Legacy` (0): Traditional blocking I/O path for maximum compatibility.
  - `IOUring` (1): Use Linux io_uring based kernel path for high-performance async I/O.
  - `Tokio` (2): Use a Tokio-based async runtime.

- `routing_mode` (enum): Controls how requests are routed to workers:
  - `ConnectionId` (0, default): Route based on connection identifier.
  - `PlayerId` (1): Route based on an application-level player/user identifier.
  - `RemoteHash` (2): Hash-based routing using remote address or hashed key.

These fields influence performance and compatibility; prefer `IOUring` or `Tokio` for high-concurrency deployments and `Legacy` for compatibility testing.
