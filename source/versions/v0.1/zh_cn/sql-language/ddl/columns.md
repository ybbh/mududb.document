# 列

列定义包含三个部分：

```
column_name data_type [column_constraint ...]
```

- **column_name** — 标识符。在解析时不区分大小写；按给定形式精确存储和匹配。
- **data_type** — 完整列表请参见 {doc}`../data_types/index`。
- **column_constraint** — 当前为 `PRIMARY KEY`（行内）和 `NOT NULL`。

`CREATE TABLE` 语句中的列顺序决定行的物理布局。MuduDB 不支持在创建后添加或删除列。
