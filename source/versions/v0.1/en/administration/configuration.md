# Configuration Reference

`mudud` reads its configuration from a TOML file. The file controls listen ports, execution mode, storage paths, and io_uring behavior.

## File location

The server loads the first file that exists, in this order:

1. The path provided by `--cfg /path/to/mudud.cfg` (or `-c /path/to/mudud.cfg`), if given.
2. `./mudud.cfg` in the current working directory.
3. `~/.mududb/mudud.cfg` in the user's home directory.

If none of these files exist, `mudud` returns a `NotFound` error. Use `mudud init-cfg` to create a default `./mudud.cfg` before starting the server.

## Generate a default config

```bash
mudud init-cfg
```

## Configuration fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `mpk_path` | string | `"./mpk"` | Path to the application package directory. |
| `db_path` | string | `"./data"` | Path to the database directory. |
| `listen_ip` | string | `127.0.0.1` | IP address to listen on. |
| `http_listen_port` | u16 | `8300` | HTTP management API port. |
| `http_worker_threads` | usize | `1` | HTTP worker thread count. |
| `pg_listen_port` | u16 | `5432` | PostgreSQL wire protocol port. |
| `component_target` | string | `p2` | Wasm component ABI target. Allowed: `p2`, `p3`. |
| `enable_async` | boolean | `true` | Enable the WASI component runtime. |
| `server_mode` | string | `"IOUring"` | `"Legacy"`, `"IOUring"`, or `"Tokio"`. |
| `tcp_listen_port` | u16 | `9527` | TCP framed protocol port. |
| `tcp_multi_port` | boolean | `false` | One TCP listener per worker. |
| `worker_threads` | usize | `0` | Worker thread count. `0` means use available parallelism. |
| `io_uring_ring_entries` | u32 | `1024` | io_uring completion queue depth. |
| `io_uring_accept_multishot` | boolean | `true` | Enable io_uring accept multishot. |
| `io_uring_recv_multishot` | boolean | `true` | Enable io_uring recv multishot. |
| `io_uring_enable_fixed_buffers` | boolean | `false` | Enable io_uring fixed buffers. |
| `io_uring_enable_fixed_files` | boolean | `false` | Enable io_uring fixed files. |
| `routing_mode` | string | `"ConnectionId"` | `"ConnectionId"`, `"PlayerId"`, or `"RemoteHash"`. |
| `log_chunk_size` | u64 | `64 * 1024 * 1024` | io_uring log chunk size in bytes. |
| `page_size` | usize | `4096` | Database page size in bytes. Persistent: changing it for an existing database requires migration or re-initialization. |

## Server and routing modes

- `server_mode`: controls the backend I/O/runtime path.
  - `Legacy`: traditional blocking I/O path for maximum compatibility.
  - `IOUring`: Linux io_uring based high-performance async I/O.
  - `Tokio`: Tokio-based async runtime.

- `routing_mode`: controls how requests are routed to workers.
  - `ConnectionId` (default): route based on connection identifier.
  - `PlayerId`: route based on an application-level player/user identifier.
  - `RemoteHash`: hash-based routing using remote address or hashed key.

## Example `mudud.cfg`

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

See the [Server Configuration Contract](../reference/contracts/mudud_cfg_v1.md) for compatibility and upgrade rules.
