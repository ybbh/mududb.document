# close

Purpose

Close the previously opened session, releasing session-scoped resources.

Behavior

- Flushes or discards transient session state as defined by the host.
- If a transaction is open, behavior depends on transaction lifecycle (commit/rollback semantics).

Notes

- Procedures must close sessions they open to avoid resource leaks in the runtime.
