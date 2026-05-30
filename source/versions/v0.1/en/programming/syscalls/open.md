# open

Purpose

Open a session or logical connection context for a procedure. Sessions group transactional and execution context for subsequent syscalls.

Behavior

- Creates or binds a session context with an optional transaction scope.
- Sessions are lightweight and scoped to the calling procedure invocation unless explicitly promoted.

Notes

- Opening a session does not implicitly start a durable transaction; transaction semantics are controlled by transaction-related syscalls or host-managed boundaries.
