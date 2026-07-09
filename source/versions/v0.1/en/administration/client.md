# Client

`mcli` is the MuduDB command-line client. It supports interactive SQL, HTTP administration, and procedure invocation.

## Connection options

- `--addr <host:port>` — TCP protocol endpoint for SQL shell and procedure invocation (default `127.0.0.1:9527`).
- `--http-addr <host:port>` — HTTP management endpoint for admin commands (default `127.0.0.1:8300`).

## Interactive SQL shell

```bash
mcli --addr 127.0.0.1:9527 shell --app demo
```

Inside the shell you can run SQL statements, meta commands, and exit with `\q`.

## Common admin commands

List installed applications:

```bash
mcli --http-addr 127.0.0.1:8300 app-list
```

Show server topology:

```bash
mcli --http-addr 127.0.0.1:8300 server-topology
```

Resolve a partition route:

```bash
mcli --http-addr 127.0.0.1:8300 partition-route --rule-name user_rule --key user-100
```

## Invoke a procedure

```bash
mcli --addr 127.0.0.1:9527 --http-addr 127.0.0.1:8300 app-invoke \
  --app wallet \
  --module wallet \
  --proc transfer_funds \
  --json '{"from_user_id": 1001, "to_user_id": 1002, "amount": 1200}'
```

## Output

- Query results are displayed as a table by default in TTY sessions.
- Management commands output pretty JSON by default; add `--compact` for compact JSON.
- On error, `mcli` exits non-zero and prints the error to stderr.

See [mcli Management Interface (HTTP)](../reference/mcli-admin.md) for the full command reference.
