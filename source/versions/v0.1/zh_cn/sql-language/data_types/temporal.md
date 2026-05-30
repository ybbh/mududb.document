# 时间类型

```sql
DATE                    -- calendar date (year, month, day)
TIME(p)                 -- time of day, optional fractional-second precision
TIMESTAMP(p)            -- date + time, no time zone
TIMESTAMPTZ(p)          -- date + time, with time zone
```

精度参数 `p` 指定小数秒位数（0–6）。省略时，不存储精度元数据。

时间字面量根据类型的标准格式从文本输入中解析。运行时接受的确切格式在内核参考文档中有说明。
