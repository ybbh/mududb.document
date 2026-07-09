# write

在表或键值存储中插入、更新或删除记录。

## Rust API

```rust
// sync_api
pub fn mudu_put(session_id: OID, key: &[u8], value: &[u8]) -> RS<()> {
    /* ... */
}

// async_api
pub async fn mudu_put(session_id: OID, key: &[u8], value: &[u8]) -> RS<()> {
    /* ... */
}
```

## 概念签名

```text
write(table: string, op: { type: 'insert' | 'update' | 'delete', row?: Row, key?: KeyExpr, patch?: Partial<Row> }) -> WriteResult
```

## 参数

- `table` —— 目标表名称。
- `op.type` —— `insert`、`update` 或 `delete` 之一。
- `op.row` —— 插入的完整行数据。
- `op.key` —— 更新/删除的主键选择器。
- `op.patch` —— 更新时要应用的部分字段。

## 行为

- 变更操作在当前事务中暂存，并在提交时变为可见。
- 宿主在写入时强制执行模式、类型和约束检查。

## 返回值

- `WriteResult` 包含状态、受影响的行数以及适用时的生成键。

## 错误

- `ConstraintViolation`：模式或唯一性冲突。
- `NotFound`：对不存在的键进行更新/删除时，根据操作模式可能返回 `NotFound`。
- `SerializationError` 或 `Conflict`：需要重试的事务冲突。

## 事务语义

- 写入必须在事务内执行，以实现原子多步更新。
- 事务外，行为由宿主定义（自动提交或拒绝）。

## 示例

```text
-- insert
write('accounts', { type: 'insert', row: { id: 5, owner: 'Carol', balance: 1000 } });

-- update
write('accounts', { type: 'update', key: 5, patch: { balance: 1200 } });
```

## 最佳实践

- 对多语句更新使用事务以确保原子性。
- 在过程边界处验证输入，以避免约束错误。
- 当过程可能重试时，优先使用幂等操作。
