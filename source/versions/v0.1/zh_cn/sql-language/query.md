# 查询

MuduDB 支持单表 `SELECT` 查询，并可通过 `WHERE` 子句过滤行。查询引擎计算谓词并将结果集返回给调用方。

## 3.1 概述

MuduDB 中的查询在当前事务上下文中执行。所有读取都与事务的隔离级别保持一致。结果以行集形式返回，客户端可以对其进行迭代。

当前的查询能力有意限定为单表查找和扫描。复杂分析、连接和聚合在 v0.1 中不受支持。

## 3.2 Select

### 语法

```sql
SELECT select_term [, select_term ...]
FROM table_name
[WHERE predicate [AND predicate ...]];
```

### Select 项

`select_term` 可以是以下之一：

- `*` — 按表顺序选择所有列。
- `column_name` — 选择单个列。
- 涉及列和字面量的算术表达式（例如，`amount * 2`、`count + 1`）。

### WHERE 谓词

每个谓词的形式为：

```
expression comparison_operator expression
```

**比较运算符：**

| 运算符 | 含义 |
|---|---|
| `=` | 等于 |
| `!=` | 不等于 |
| `<` | 小于 |
| `<=` | 小于或等于 |
| `>` | 大于 |
| `>=` | 大于或等于 |

谓词仅通过 `AND` 逻辑连接符组合。`OR` 和 `NOT` 在 v0.1 中不受支持。

### 表达式

表达式可以是：

- 列引用
- 数值、字符串或时间字面量
- 占位符（`?`）
- 算术表达式：`+`、`-`、`*`、`/`，具有标准优先级

### 示例

选择所有列：

```sql
SELECT * FROM users;
```

选择特定列并带过滤条件：

```sql
SELECT id, name FROM users WHERE id = 1;
```

选择多个谓词：

```sql
SELECT ol_i_id, ol_amount
FROM order_line
WHERE ol_w_id = 1 AND ol_d_id = 2 AND ol_o_id = 100;
```

选择带占位符（预备语句）：

```sql
SELECT * FROM stock WHERE s_w_id = ? AND s_i_id = ?;
```

选择带反向比较（解析器会规范化其形式）：

```sql
SELECT id FROM users WHERE 7 > id;
-- internally normalised to: id < 7
```

选择项列表中带算术表达式：

```sql
SELECT id, amount * 2 FROM ledger WHERE id = 1;
```

## 不支持的查询功能

以下功能在 v0.1 中不可用：

- `JOIN`（内连接、外连接、交叉连接）
- `GROUP BY` / `HAVING`
- `ORDER BY`
- `LIMIT` / `OFFSET`
- `DISTINCT`
- 子查询（`SELECT ... FROM (SELECT ...)`）
- 窗口函数
- 公用表表达式（`WITH`）
- 集合运算（`UNION`、`INTERSECT`、`EXCEPT`）
