# Syscalls

MuduDB procedures call into the kernel via a small set of controlled syscalls. These pages document each syscall's purpose, expected inputs, and transaction/consistency implications.

```{toctree}
:maxdepth: 1

syscalls/open
syscalls/close
syscalls/read
syscalls/write
syscalls/range-scan
syscalls/batch
syscalls/command
```
