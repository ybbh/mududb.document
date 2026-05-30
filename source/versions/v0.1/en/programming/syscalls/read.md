# read

Purpose

Read a single record by primary key or lookup criteria.

Signature

```text
read(table: string, key: KeyExpr, options?: { projection?: [string], for_update?: bool }) -> Row | null
```

Parameters

- table: target table or logical collection name.
- key: primary key value or a structured key expression for lookup.
- options.projection: optional list of column names to return.
- options.for_update: when true, the read acquires locks to allow safe subsequent updates within the same transaction.

Behavior

- Performs a point lookup in the table or index and returns the matching row, or null if not found.
- Reads respect the current transaction isolation and visibility rules (may return committed snapshot values depending on isolation).

Return

- A single Row object with column values, or null when no row matches.

Errors

- NotFound: not an error; read returns null when no match.
- LockConflict: when for_update is requested and lock acquisition fails.

Transaction semantics

- Reads inside an open transaction are subject to that transaction's snapshot/isolation. Reads outside a transaction follow host default semantics.

Example

```rust
let row = read("accounts", 42, { projection: ["id", "balance"] });
if row != null {
  // use row.balance
}
```

Notes

- Use projection to reduce data transferred and improve performance.
- For read-modify-write patterns, prefer for_update to avoid lost-update races.
