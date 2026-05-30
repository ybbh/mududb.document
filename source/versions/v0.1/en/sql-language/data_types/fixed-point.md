# Fixed-Point Types

```sql
NUMERIC(precision, scale)
DECIMAL(precision, scale)
NUMERIC        -- without parameters
DECIMAL        -- without parameters
```

`NUMERIC` stores arbitrary-precision decimal values. The optional `(precision, scale)` parameters are parsed and preserved in the column metadata but do not truncate values at insert time; they serve as documentation and validation hints for tooling.

Examples:

```sql
amount NUMERIC(18, 2)
rate   DECIMAL(9, 4)
```
