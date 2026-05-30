# write

Purpose

Insert, update, or delete a record in a table or key-value store.

Signature

```text
write(table: string, op: { type: 'insert' | 'update' | 'delete', row?: Row, key?: KeyExpr, patch?: Partial<Row> }) -> WriteResult
```

Parameters

- table: target table name.
- op.type: one of 'insert', 'update', or 'delete'.
- op.row: full row payload for inserts.
- op.key: primary key selector for updates/deletes.
- op.patch: partial fields to apply for updates.

Behavior

- Mutations are staged in the current transaction and become visible on commit.
- The host enforces schema, types, and constraint checks at write time.

Return

- WriteResult contains status, affected row count, and generated keys when applicable.

Errors

- ConstraintViolation: schema or uniqueness violation.
- NotFound: update/delete on a non-existing key may return NotFound depending on op mode.
- SerializationError or Conflict: transaction conflicts requiring retry.

Transaction semantics

- Writes must be performed within a transaction for atomic multi-step updates. Outside a transaction, behavior is host-defined (autocommit or reject).

Example

```sql
-- insert
write('accounts', { type: 'insert', row: { id: 5, owner: 'Carol', balance: 1000 } });

-- update
write('accounts', { type: 'update', key: 5, patch: { balance: 1200 } });
```

Best practices

- Use transactions for multi-statement updates to ensure atomicity.
- Validate inputs at the procedure boundary to avoid constraint errors.
- Prefer idempotent operations when procedures may be retried.
