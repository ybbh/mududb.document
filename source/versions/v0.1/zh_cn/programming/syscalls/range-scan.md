# range-scan

遍历某个键范围或索引范围，返回匹配的行序列。

## Rust API

```rust
// sync_api
pub fn mudu_range(
    session_id: OID,
    start_key: &[u8],
    end_key: &[u8],
) -> RS<Vec<(Vec<u8>, Vec<u8>)>> {
    /* ... */
}

// async_api
pub async fn mudu_range(
    session_id: OID,
    start_key: &[u8],
    end_key: &[u8],
) -> RS<Vec<(Vec<u8>, Vec<u8>)>> {
    /* ... */
}
```

## 概念签名

```text
range_scan(
  table: string,
  start_key: KeyExpr,
  end_key: KeyExpr,
  options?: { projection?: [string], limit?: int, for_update?: bool }
) -> [Row]
```

## 参数

- `table` —— 目标表或逻辑集合名称。
- `start_key` —— 范围下界（含）。
- `end_key` —— 范围上界（不含）。
- `options.projection` —— 可选，需要返回的列名列表。
- `options.limit` —— 可选，最多返回行数。
- `options.for_update` —— 为 true 时对返回行加锁。

## 返回值

- 匹配范围的 `(key, value)` 对列表或 `Row` 对象列表。

## 错误

- `InvalidKey`：键表达式与表模式不匹配。
- `LockConflict`：请求 `for_update` 但加锁失败。

## 事务语义

- 范围扫描遵循当前事务的快照/隔离规则。
- 事务外可见性遵循宿主默认语义。

## 示例

```rust
let rows = mudu_range(
    oid,
    b"accounts:100",
    b"accounts:200",
)?;
for (k, v) in rows {
    // 按表模式解码 k/v
}
```

## 注意

- 长时间扫描应分页或限制行数，避免占用资源。
- 扫描分区表时，内核可能将请求路由到多个工作线程。
