# Data Manipulation

MuduDB supports `INSERT`, `UPDATE`, and `DELETE` for modifying table data. `COPY FROM` and `COPY TO` are also available for bulk load and export.

## Overview

All DML statements execute inside the current transaction context. If no explicit transaction is active, each statement is auto-committed. MuduDB does not support `MERGE`, `UPSERT`, or `TRUNCATE TABLE` in v0.1.

Prepared-statement placeholders (`?`) can be used in place of literal values. The kernel binds parameters at execution time.

```{toctree}
:maxdepth: 1

insert
update
delete
```

## COPY

Bulk load from or export to a CSV file.

```sql
COPY table_name FROM 'file_path';
COPY table_name TO 'file_path';
```

Examples:

```sql
COPY users FROM 'users.csv';
COPY users TO 'users_export.csv';
```

`COPY` does not accept a column list in v0.1; the file must match the table column order.

## Unsupported DML

The following features are not available in v0.1:

- `MERGE` / `UPSERT`
- `TRUNCATE TABLE`
- `RETURNING` clause on `INSERT` / `UPDATE` / `DELETE`
- Multi-table `UPDATE` or `DELETE`
- `ON CONFLICT` handling
