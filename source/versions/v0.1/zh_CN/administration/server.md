# 服务管理

`mudud` 是 MuduDB 服务进程。生产环境应由进程管理器启动，并明确配置文件、日志路径和文件描述符限制。

## 启动前检查

- `mudud --version` 可执行。
- `${HOME}/.mududb/mududb_cfg.toml` 存在或允许自动创建。
- `nofile` soft limit 足够高，建议不低于 `65535`。

## 运行时检查

```bash
cat /proc/$(pgrep -x mudud)/limits | rg 'open files'
```
