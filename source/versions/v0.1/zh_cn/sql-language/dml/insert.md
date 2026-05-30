# 插入

## 语法

```sql
INSERT INTO table_name [(column_name [, column_name ...])]
VALUES (value [, value ...]) [, (value [, value ...]) ...];
```

## 规则

- 列列表是可选的。省略时，值必须与表的列顺序完全匹配。
- 单个 `VALUES` 子句中支持多行元组。
- `NULL` 可用于可为空列的值。
- 占位符（`?`）可用于任何值位置。

## 示例

插入显式列的单行：

```sql
INSERT INTO item (i_id, i_name, i_price, i_data, i_im_id)
VALUES (1, 'Widget', 12.99, 'Standard widget', 42);
```

插入多行：

```sql
INSERT INTO users (id, name)
VALUES (1, 'alice'), (2, 'bob'), (3, 'charlie');
```

插入带占位符（预备语句）：

```sql
INSERT INTO stock (s_w_id, s_i_id, s_quantity, s_data)
VALUES (?, ?, ?, ?);
```

不带列列表插入（值必须与表顺序匹配）：

```sql
INSERT INTO item VALUES (2, 'Gadget', 9.99, 'Mini gadget', 7);
```
