# 服务器管理

`mudud` 是 MuduDB 服务器进程。生产部署应通过进程管理器启动它，并显式配置文件路径、日志和文件描述符限制。

## 启动前检查

- `mudud --version` 可用。
- `${HOME}/.mududb/mududb_cfg.toml` 存在或可以创建。
- `nofile` 软限制足够高。`65535` 是一个实用的基线。

## 运行时检查

```bash
cat /proc/$(pgrep -x mudud)/limits | rg 'open files'
```
