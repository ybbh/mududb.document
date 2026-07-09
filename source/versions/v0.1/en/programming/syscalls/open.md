# open

Open a session or logical connection context for a procedure. Sessions group transactional and execution context for subsequent syscalls.

## Rust API

```rust
// sync_api
pub fn mudu_open() -> RS<OID> {
    /* ... */
}

// async_api
pub async fn mudu_open() -> RS<OID> {
    /* ... */
}
```

## Conceptual signature

```text
open() -> OID
```

## Parameters

None.

## Return value

- `OID` — a session identifier used as the first argument to subsequent syscalls such as `read`, `write`, `query`, and `command`.

## Errors

- `OutOfMemory`: the runtime cannot allocate session state.
- `NotSupported`: the runtime does not allow new sessions in the current state.

## Transaction semantics

- Opening a session does not implicitly start a durable transaction.
- Transaction boundaries are controlled by the host or by transaction-related syscalls.

## Example

```rust
let oid = mudu_open()?;
let row = read("accounts", 42, None)?;
mudu_close(oid)?;
```

## Notes

- In procedure code the session `OID` is usually passed in as the first argument, so explicit `open`/`close` are most common in interactive tests or standalone adapter code.
- Always pair `open` with `close` to release session-scoped resources.
