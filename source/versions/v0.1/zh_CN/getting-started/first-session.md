# 第一次会话

## 启动服务

```bash
ulimit -n 65535
mudud
```

如果由 `systemd` 管理服务，请在 service 文件中配置 `LimitNOFILE=65535`。

## 打开交互式 SQL shell

```bash
mcli --addr 127.0.0.1:9527 shell --app demo
```

执行一个完整的 CRUD 流程：

```sql
CREATE TABLE users_demo (
  id INT PRIMARY KEY,
  name TEXT
);

INSERT INTO users_demo (id, name) VALUES (1, 'Alice');
SELECT id, name FROM users_demo WHERE id = 1;

UPDATE users_demo SET name = 'Alice-Updated' WHERE id = 1;
DELETE FROM users_demo WHERE id = 1;
```

退出 shell：

```text
\q
```

## 下一步

继续阅读 {doc}`../tutorials/wallet`，构建、安装并调用一个过程应用。
