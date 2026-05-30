# Adapters

The adapter layer connects different backend capabilities, including SQLite, PostgreSQL, MySQL, and the MuduDB kernel itself. Adapter documentation should describe supported behavior, test coverage, and known differences.

## Async session loop (async_session_loop)

- When the connection configuration enables the async session loop (`async_session_loop=true`), the adapter forwards session management and I/O commands to a dedicated background manager thread running an async runtime. This manager keeps long-lived AsyncClient connections and serializes work through a channel-based command queue.

- Behavioral differences:
  - Synchronous path (`async_session_loop=false`): each `mudu_open` creates a `SyncClient` and calls are performed blocking on the caller thread.
  - Asynchronous path (`async_session_loop=true`): adapter methods enqueue commands (Open/Close/Get/Put/Range/Query/Command/Batch) to the manager and wait for a response over a small sync channel, reducing blocking on the calling thread and improving concurrency.

- Performance notes: async loop reduces per-call blocking and thread usage, but introduces runtime and channel overhead. Choose async loop for high-concurrency scenarios or when using IOUring/Tokio backends.
