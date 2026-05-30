# Data Definition

MuduDB supports a concise DDL subset for creating and dropping tables. Schema changes are executed through the standard `CREATE TABLE` and `DROP TABLE` statements. Partition rules and placements can also be declared for distributed tables.

## Table Basics

A table in MuduDB is a named collection of rows. Each row has the same set of columns defined at creation time. MuduDB does not support `ALTER TABLE` in the current release; the schema is fixed after `CREATE TABLE` succeeds.

Tables are created within the default database context of the current session. There is no `CREATE DATABASE` or `USE database` syntax; the session itself determines the logical database scope.

```{toctree}
:maxdepth: 1

columns
create-table
primary-key
drop-table
```

## Unsupported DDL

The following DDL features are not available in v0.1:

- `ALTER TABLE` (add / drop / rename columns)
- `CREATE INDEX`
- `CREATE VIEW`
- Foreign-key constraints (`FOREIGN KEY ... REFERENCES`)
- `ON DELETE CASCADE` / `ON UPDATE`
- `CHECK` constraints
- `UNIQUE` constraints (only `PRIMARY KEY` is enforced)
