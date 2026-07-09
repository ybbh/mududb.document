# Server Management

`mudud` is the MuduDB server process. It hosts the database kernel, runs installed MPK packages, and exposes three listeners: a TCP protocol endpoint, an HTTP management endpoint, and a PostgreSQL-compatible wire protocol port.

## Prerequisites

- `mudud` and `mcli` are installed and in `PATH`.
- A configuration file exists at `./mudud.cfg`, `~/.mududb/mudud.cfg`, or a path passed with `--cfg`.
- On Linux, `io_uring` mode requires `liburing-dev` at runtime.
- The process should be started with a high file-descriptor limit (`ulimit -n 65535` is a practical baseline).

## Starting the server

### Default start

```bash
ulimit -n 65535
mudud
```

If `./mudud.cfg` does not exist, `mudud` checks `~/.mududb/mudud.cfg`. Create a default config with:

```bash
mudud init-cfg
```

### Start with a custom config

```bash
ulimit -n 65535
mudud serve --cfg ./config/mudud.cfg
```

### What to expect

After starting, `mudud` logs the effective configuration and opens three listeners:

- TCP protocol: `listen_ip:tcp_listen_port` (default `127.0.0.1:9527`)
- HTTP management: `listen_ip:http_listen_port` (default `127.0.0.1:8300`)
- PostgreSQL wire protocol: `listen_ip:pg_listen_port` (default `127.0.0.1:5432`)

## Stopping the server

Send `SIGINT` (`Ctrl+C`) or `SIGTERM`. `mudud` performs a graceful shutdown, waiting for in-flight work to finish before exiting.

## Verifying the server

Use `mcli` to check the HTTP management endpoint:

```bash
mcli --http-addr 127.0.0.1:8300 app-list
mcli --http-addr 127.0.0.1:8300 server-topology
```

If the commands return JSON output, the server is running and reachable.

## Server modes

| Mode | When to use |
|------|-------------|
| `Legacy` | Maximum compatibility; single TCP/PG serving model. |
| `IOUring` | High-performance async I/O on Linux (recommended on Linux). |
| `Tokio` | Portable async runtime when `io_uring` is unavailable. |

## Common issues

- **Address already in use**: another process is using one of the configured ports. Change the conflicting port in `mudud.cfg`.
- **Permission denied**: you may not have permission to bind to the configured `listen_ip` or port. Use `127.0.0.1` and ports above `1024` for local development.
- **Too many open files**: raise the file descriptor limit with `ulimit -n 65535` before starting.
- **io_uring not available**: if you are not on Linux or `liburing-dev` is missing, switch `server_mode` to `Tokio`.

See the [Configuration Reference](configuration.md) for all available options.
