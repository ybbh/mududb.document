# 删除表

删除表及其所有数据。

```sql
DROP TABLE [IF EXISTS] table_name;
```

示例：

```sql
DROP TABLE IF EXISTS order_line;
DROP TABLE stock;
```

`IF EXISTS` 在表不存在时抑制错误。
