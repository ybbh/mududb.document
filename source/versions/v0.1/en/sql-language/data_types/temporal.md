# Temporal Types

```sql
DATE                    -- calendar date (year, month, day)
TIME(p)                 -- time of day, optional fractional-second precision
TIMESTAMP(p)            -- date + time, no time zone
TIMESTAMPTZ(p)          -- date + time, with time zone
```

The precision parameter `p` specifies the number of fractional-second digits (0–6). When omitted, no precision metadata is stored.

Temporal literals are parsed from textual input according to the type's standard format. The exact format accepted by the runtime is documented in the kernel reference.
