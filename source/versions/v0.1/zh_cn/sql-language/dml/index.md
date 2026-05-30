# 数据操作

MuduDB 支持 `INSERT`、`UPDATE` 和 `DELETE` 用于修改表数据。`COPY FROM` 和 `COPY TO` 也可用于批量加载和导出。

## 概述

所有 DML 语句在当前事务上下文中执行。如果没有显式事务处于活动状态，则每条语句自动提交。MuduDB 在 v0.1 中不支持 `MERGE`、`UPSERT` 或 `TRUNCATE TABLE`。

预备语句占位符（`?`）可用于替代字面量值。内核在执行时绑定参数。

```{toctree}
:maxdepth: 1

insert
update
delete
```

## COPY

从 CSV 文件批量加载或导出到 CSV 文件。

```sql
COPY table_name FROM 'file_path';
COPY table_name TO 'file_path';
```

示例：

```sql
COPY users FROM 'users.csv';
COPY users TO 'users_export.csv';
```

`COPY` 在 v0.1 中不接受列列表；文件必须与表的列顺序匹配。

## 不支持的 DML

以下功能在 v0.1 中不可用：

- `MERGE` / `UPSERT`
- `TRUNCATE TABLE`
- `INSERT` / `UPDATE` / `DELETE` 上的 `RETURNING` 子句
- 多表 `UPDATE` 或 `DELETE`
- `ON CONFLICT` 处理
