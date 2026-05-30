# read

用途

通过主键或查找条件读取单条记录。

签名

```text
read(table: string, key: KeyExpr, options?: { projection?: [string], for_update?: bool }) -> Row | null
```

参数

- table：目标表或逻辑集合名称。
- key：主键值或用于查找的结构化键表达式。
- options.projection：可选的列名列表，用于指定返回的列。
- options.for_update：当为 true 时，读取会获取锁，以允许在同一事务内安全地进行后续更新。

行为

- 在表或索引中执行点查找，并返回匹配的行，如果未找到则返回 null。
- 读取遵守当前事务的隔离和可见性规则（根据隔离级别可能返回已提交快照值）。

返回值

- 包含列值的单个 Row 对象，如果没有匹配行则返回 null。

错误

- NotFound：不是错误；读取在未匹配时返回 null。
- LockConflict：当请求 for_update 且锁获取失败时。

事务语义

- 在打开的事务内进行的读取受该事务的快照/隔离影响。事务外的读取遵循宿主默认语义。

示例

```rust
let row = read("accounts", 42, { projection: ["id", "balance"] });
if row != null {
  // use row.balance
}
```

备注

- 使用 projection 可以减少数据传输并提高性能。
- 对于读-改-写模式，优先使用 for_update 以避免丢失更新竞争。
