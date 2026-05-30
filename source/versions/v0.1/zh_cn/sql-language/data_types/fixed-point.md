# 定点类型

```sql
NUMERIC(precision, scale)
DECIMAL(precision, scale)
NUMERIC        -- without parameters
DECIMAL        -- without parameters
```

`NUMERIC` 存储任意精度的小数值。可选的 `(precision, scale)` 参数在列元数据中被解析和保留，但在插入时不会截断值；它们作为文档和工具验证的提示。

示例：

```sql
amount NUMERIC(18, 2)
rate   DECIMAL(9, 4)
```
