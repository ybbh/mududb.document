# Delete

## Syntax

```sql
DELETE FROM table_name
WHERE predicate [AND predicate ...];
```

## Rules

- `WHERE` is **required**. A `DELETE` without a `WHERE` clause is rejected by the parser.
- Predicates are combined with `AND` only.

## Examples

Delete a specific row:

```sql
DELETE FROM new_order
WHERE no_w_id = 1 AND no_d_id = 2 AND no_o_id = 100;
```

Delete with placeholders:

```sql
DELETE FROM history
WHERE h_c_id = ? AND h_c_d_id = ? AND h_c_w_id = ?;
```
