# range-scan

Iterate over a key range or index range, producing a stream of rows.

## Rust API

```rust
// sync_api
pub fn mudu_range(
    session_id: OID,
    start_key: &[u8],
    end_key: &[u8],
) -> RS<Vec<(Vec<u8>, Vec<u8>)>> {
    /* ... */
}

// async_api
pub async fn mudu_range(
    session_id: OID,
    start_key: &[u8],
    end_key: &[u8],
) -> RS<Vec<(Vec<u8>, Vec<u8>)>> {
    /* ... */
}
```

## Conceptual signature

```text
range_scan(
  table: string,
  start_key: KeyExpr,
  end_key: KeyExpr,
  options?: { projection?: [string], limit?: int, for_update?: bool }
) -> [Row]
```

## Parameters

- `table` — target table or logical collection name.
- `start_key` — inclusive lower bound of the scan.
- `end_key` — exclusive upper bound of the scan.
- `options.projection` — optional list of column names to return.
- `options.limit` — optional maximum number of rows to return.
- `options.for_update` — when true, acquires locks on returned rows.

## Return value

- A list of `(key, value)` pairs or `Row` objects matching the range.

## Errors

- `InvalidKey`: the key expression does not match the table schema.
- `LockConflict`: `for_update` is requested and lock acquisition fails.

## Transaction semantics

- Range scans honor the current transaction's snapshot/isolation rules.
- Outside a transaction, visibility follows host default semantics.

## Example

```rust
let rows = mudu_range(
    oid,
    b"accounts:100",
    b"accounts:200",
)?;
for (k, v) in rows {
    // decode k/v according to the table schema
}
```

## Notes

- Long-running scans should be paginated or limited to avoid holding resources.
- When scanning a partitioned table, the kernel may route the request across workers.
