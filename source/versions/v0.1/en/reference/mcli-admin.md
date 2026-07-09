# mcli Management Interface (HTTP)

This page describes the HTTP management commands available through `mcli` for application lifecycle management and partition routing queries.

## Prerequisites

- A running `mudud` server.
- The HTTP management endpoint reachable (default `127.0.0.1:8300`).

Most management commands take `--http-addr <host:port>` to target the server.

## Commands

### List installed applications

```bash
mcli --http-addr 127.0.0.1:8300 app-list
```

### Install an application package

```bash
mcli --http-addr 127.0.0.1:8300 app-install --mpk target/wasm32-wasip2/release/wallet.mpk
```

### Show application procedures

```bash
mcli --http-addr 127.0.0.1:8300 app-detail --app wallet
```

### Show one procedure detail

`--proc` must be used together with `--module`.

```bash
mcli --http-addr 127.0.0.1:8300 app-detail --app wallet --module wallet --proc create_user
```

### Uninstall an application

```bash
mcli --http-addr 127.0.0.1:8300 app-uninstall --app wallet
```

### Show server topology

```bash
mcli --http-addr 127.0.0.1:8300 server-topology
```

### Partition route query

Route by exact key:

```bash
mcli --http-addr 127.0.0.1:8300 partition-route --rule-name user_rule --key user-100
```

Route by range:

```bash
mcli --http-addr 127.0.0.1:8300 partition-route --rule-name user_rule --start 100 --end 200
```

Composite key example:

```bash
mcli --http-addr 127.0.0.1:8300 partition-route --rule-name order_rule --key tenant-1,order-100
```

## Argument constraints

- `app-detail`: `--proc` requires `--module`.
- `partition-route`: `--key` and `--start/--end` are mutually exclusive; provide one or the other.

## Output

- Default output is pretty-printed JSON.
- Add `--compact` for compact JSON.
- On failure the command exits non-zero and prints the error to stderr.
