# command

执行单条 SQL `INSERT`、`UPDATE` 或 `DELETE` 语句。

## Rust API

```rust
// sync_api
pub fn mudu_command(
    oid: OID,
    sql: &dyn SQLStmt,
    params: &dyn SQLParams,
) -> RS<u64> {
    /* ... */
}

// async_api
pub async fn mudu_command(
    oid: OID,
    sql: &dyn SQLStmt,
    params: &dyn SQLParams,
) -> RS<u64> {
    /* ... */
}
```

## 概念签名

```text
command(sql: string, params?: [Value]) -> affected_rows: u64
```

## 参数

- `sql` —— 单条 SQL 语句，使用 `?` 作为参数占位符。
- `params` —— 绑定到占位符的值。

## 返回值

- `u64` —— 语句影响的行数。

## 错误

- `SyntaxError`：SQL 语句无效。
- `ConstraintViolation`：模式或唯一性冲突。
- `NotFound`：更新/删除不存在的键，取决于操作模式。
- `SerializationError` / `Conflict`：事务冲突，需要重试。

## 事务语义

- 该命令参与当前会话事务。
- 事务外行为由宿主定义（自动提交或拒绝）。

## 示例

```rust
let affected = mudu_command(
    oid,
    sql_stmt!("UPDATE accounts SET balance = balance - ? WHERE id = ?"),
    sql_params!(&(amount, from_id)),
)?;
assert_eq!(affected, 1);
```

## 注意

- `command` 用于 DML 语句；`SELECT` 请使用 `query`。
- 如需一次调用执行多条语句，可考虑 `batch`。
- 有结构化访问需求时，优先使用类型化系统调用原语（`read`、`write`）。
