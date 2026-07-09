# Columns

A column definition has three parts:

```
column_name data_type [column_constraint ...]
```

- **column_name** — an identifier. Case-insensitive in parsing; stored and matched exactly as given.
- **data_type** — see {doc}`../data_types/index` for the full list.
- **column_constraint** — currently `PRIMARY KEY` (inline) and `NOT NULL`.

Column order in the `CREATE TABLE` statement determines the physical layout of the row. MuduDB does not support adding or dropping columns after creation.
