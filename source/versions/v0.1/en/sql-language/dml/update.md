# Update

## Syntax

```sql
UPDATE table_name
SET column_name = expression [, column_name = expression ...]
WHERE predicate [AND predicate ...];
```

## Rules

- `WHERE` is **required**. An `UPDATE` without a `WHERE` clause is rejected by the parser.
- The right-hand side of an assignment can be a literal, a placeholder, or an arithmetic expression involving other columns and literals.
- Predicates in the `WHERE` clause are combined with `AND` only.

## Examples

Simple update with a literal:

```sql
UPDATE stock
SET s_quantity = 100
WHERE s_w_id = 1 AND s_i_id = 10;
```

Update using an arithmetic expression:

```sql
UPDATE users
SET total = count + 1, balance = balance - amount
WHERE id = 1;
```

Update with a placeholder:

```sql
UPDATE stock
SET s_quantity = ?
WHERE s_w_id = ? AND s_i_id = ?;
```
