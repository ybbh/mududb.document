# Server Management

`mudud` is the MuduDB server process. Production deployments should start it through a process manager and explicitly configure file paths, logging, and file descriptor limits.

## Preflight Checks

- `mudud --version` is available.
- `${HOME}/.mududb/mududb_cfg.toml` exists or can be created.
- The `nofile` soft limit is high enough. `65535` is a practical baseline.

## Runtime Check

```bash
cat /proc/$(pgrep -x mudud)/limits | rg 'open files'
```
