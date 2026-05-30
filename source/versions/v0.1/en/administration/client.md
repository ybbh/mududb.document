# Client

`mcli` is the MuduDB command-line client for interactive SQL, HTTP administration, and procedure invocation.

Common commands:

```bash
mcli --addr 127.0.0.1:9527 shell --app demo
mcli --http-addr 127.0.0.1:8300 app-list
mcli --http-addr 127.0.0.1:8300 server-topology
```

In TTY sessions, query results are displayed as an interactive table by default.
