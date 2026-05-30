# Drop Table

Remove a table and all its data.

```sql
DROP TABLE [IF EXISTS] table_name;
```

Examples:

```sql
DROP TABLE IF EXISTS order_line;
DROP TABLE stock;
```

`IF EXISTS` suppresses the error when the table does not exist.
