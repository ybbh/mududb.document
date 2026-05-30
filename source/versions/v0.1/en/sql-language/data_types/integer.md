# Integer Types

```sql
INT      -- 32-bit signed
BIGINT   -- 64-bit signed
HUGEINT  -- 128-bit signed
```

`INT` maps to the internal 32-bit signed integer (`I32`). `BIGINT` maps to the 64-bit signed integer (`I64`). `HUGEINT` maps to the internal 128-bit signed integer (`I128`).

All integer literals in SQL are parsed as `I64` by default. The parser does not enforce range checking at parse time; overflow behaviour is defined by the runtime.
