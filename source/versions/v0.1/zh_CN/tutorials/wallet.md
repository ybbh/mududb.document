# Wallet 示例

`example/wallet` 展示了如何把业务过程打包成 `.mpk`，安装到 MuduDB，并通过 `mcli app-invoke` 调用。

## 构建包

```bash
cd example/wallet
cargo make
```

生成产物：

```text
target/wasm32-wasip2/release/wallet.mpk
```

## 安装应用

```bash
mcli --http-addr 127.0.0.1:8300 app-install --mpk target/wasm32-wasip2/release/wallet.mpk
mcli --http-addr 127.0.0.1:8300 app-list
```

## 调用过程

```bash
mcli --addr 127.0.0.1:9527 --http-addr 127.0.0.1:8300 app-invoke --app wallet --module wallet --proc create_user --json '{
  "user_id": 1001,
  "name": "Alice",
  "email": "alice@example.com"
}'
```

过程调用通过 TCP 发送，`--http-addr` 用于读取过程元数据。
