# open

打开一个会话或逻辑连接上下文，为后续系统调用提供事务与执行上下文。

## Rust API

```rust
// sync_api
pub fn mudu_open() -> RS<OID> {
    /* ... */
}

// async_api
pub async fn mudu_open() -> RS<OID> {
    /* ... */
}
```

## 概念签名

```text
open() -> OID
```

## 参数

无。

## 返回值

- `OID` —— 会话标识符，作为后续 `read`、`write`、`query`、`command` 等系统调用的第一个参数。

## 错误

- `OutOfMemory`：运行时无法分配会话状态。
- `NotSupported`：当前状态下运行时禁止创建新会话。

## 事务语义

- 打开会话不会隐式启动持久事务。
- 事务边界由宿主或事务相关系统调用控制。

## 示例

```rust
let oid = mudu_open()?;
let row = read("accounts", 42, None)?;
mudu_close(oid)?;
```

## 注意

- 在过程代码中，会话 `OID` 通常作为第一个参数传入，因此显式的 `open`/`close` 多见于交互式测试或独立适配器代码。
- `open` 应与 `close` 配对使用，以释放会话级资源。
