# Insert

## Syntax

```sql
INSERT INTO table_name [(column_name [, column_name ...])]
VALUES (value [, value ...]) [, (value [, value ...]) ...];
```

## Rules

- The column list is optional. When omitted, values must match the table column order exactly.
- Multiple row tuples are supported in a single `VALUES` clause.
- `NULL` can be used as a value for nullable columns.
- Placeholders (`?`) are accepted for any value position.

## Examples

Insert a single row with explicit columns:

```sql
INSERT INTO item (i_id, i_name, i_price, i_data, i_im_id)
VALUES (1, 'Widget', 12.99, 'Standard widget', 42);
```

Insert multiple rows:

```sql
INSERT INTO users (id, name)
VALUES (1, 'alice'), (2, 'bob'), (3, 'charlie');
```

Insert with placeholders (prepared statement):

```sql
INSERT INTO stock (s_w_id, s_i_id, s_quantity, s_data)
VALUES (?, ?, ?, ?);
```

Insert without a column list (values must match table order):

```sql
INSERT INTO item VALUES (2, 'Gadget', 9.99, 'Mini gadget', 7);
```
