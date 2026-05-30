# 数据定义

MuduDB 支持一个精简的 DDL 子集，用于创建和删除表。模式变更通过标准的 `CREATE TABLE` 和 `DROP TABLE` 语句执行。分区规则和放置位置也可以为分布式表声明。

## 表基础

MuduDB 中的表是一个命名的行集合。每一行具有在创建时定义的相同列集合。MuduDB 在当前版本中不支持 `ALTER TABLE`；模式在 `CREATE TABLE` 成功后即固定不变。

表在当前会话的默认数据库上下文中创建。不存在 `CREATE DATABASE` 或 `USE database` 语法；会话本身决定逻辑数据库范围。

```{toctree}
:maxdepth: 1

columns
create-table
primary-key
drop-table
```

## 不支持的 DDL

以下 DDL 功能在 v0.1 中不可用：

- `ALTER TABLE`（添加 / 删除 / 重命名列）
- `CREATE INDEX`
- `CREATE VIEW`
- 外键约束（`FOREIGN KEY ... REFERENCES`）
- `ON DELETE CASCADE` / `ON UPDATE`
- `CHECK` 约束
- `UNIQUE` 约束（仅 `PRIMARY KEY` 被强制执行）
