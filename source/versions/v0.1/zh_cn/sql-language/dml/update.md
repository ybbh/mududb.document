# 更新

## 语法

```sql
UPDATE table_name
SET column_name = expression [, column_name = expression ...]
WHERE predicate [AND predicate ...];
```

## 规则

- `WHERE` 是**必需的**。不带 `WHERE` 子句的 `UPDATE` 将被解析器拒绝。
- 赋值的右侧可以是字面量、占位符，或涉及其他列和字面量的算术表达式。
- `WHERE` 子句中的谓词仅通过 `AND` 组合。

## 示例

使用字面量的简单更新：

```sql
UPDATE stock
SET s_quantity = 100
WHERE s_w_id = 1 AND s_i_id = 10;
```

使用算术表达式更新：

```sql
UPDATE users
SET total = count + 1, balance = balance - amount
WHERE id = 1;
```

使用占位符更新：

```sql
UPDATE stock
SET s_quantity = ?
WHERE s_w_id = ? AND s_i_id = ?;
```
