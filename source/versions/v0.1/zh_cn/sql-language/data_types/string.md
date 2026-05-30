# 字符串类型

```sql
CHAR(n)      -- fixed-length, space-padded
VARCHAR(n)   -- variable-length up to n characters
TEXT         -- unbounded text
```

这三种类型都映射到内部 `String` 类型。MuduDB 使用 UTF-8 编码。长度参数 `n` 存储在列元数据中，但不会截断插入的值。

SQL 中的字符串字面量是单引号：`'hello'`。
