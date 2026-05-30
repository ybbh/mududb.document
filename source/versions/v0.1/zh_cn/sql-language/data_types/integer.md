# 整数类型

```sql
INT      -- 32-bit signed
BIGINT   -- 64-bit signed
HUGEINT  -- 128-bit signed
```

`INT` 映射到内部 32 位有符号整数（`I32`）。`BIGINT` 映射到内部 64 位有符号整数（`I64`）。`HUGEINT` 映射到内部 128 位有符号整数（`I128`）。

SQL 中的所有整数字面量默认解析为 `I64`。解析器在解析时不强制执行范围检查；溢出行为由运行时定义。
