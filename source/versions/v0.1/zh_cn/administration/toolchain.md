# 工具链

MuduDB 工具链围绕过程应用的构建、打包、部署与调用组织。

## 工具概览

| 工具 | 用途 | 典型用法 |
|------|------|----------|
| `mudud` | MuduDB 服务端进程。 | `mudud` 或 `mudud serve --cfg ./mudud.cfg` |
| `mcli` | TCP 客户端、交互式 SQL shell、HTTP 管理 CLI。 | `mcli shell`、`mcli app-install`、`mcli server-topology` |
| `mgen` | 源码生成器。根据 SQL DDL 生成带类型的 Rust 实体。 | `mgen --ddl ddl.sql --out ./src/generated` |
| `mtp` | 转译器。将同步过程源码改写为兼容 WASM 运行时的异步形式。 | `mtp --input ./src --output ./src_async` |
| `mpm-build` | 包构建器。从 DDL、描述符与 WASM 模块生成 `.mpk` 归档。 | `mpm-build create --cfg package.cfg.json` |
| `mpm-install` | MPK 安装辅助工具（也可通过 `mcli app-install` 安装）。 | `mpm-install --mpk wallet.mpk` |
| `mudup` | 发布安装器。无需源码构建即可下载发布二进制。 | `mudup install` — **尚不稳定，建议源码构建。** |

## 典型工作流

1. **定义 schema**：编写应用的 `ddl.sql`。
2. **生成类型**：运行 `mgen` 从 DDL 生成带类型的 `Entity` 结构体。
3. **编写过程**：使用 `sys_interface::sync_api` 实现标记为 `/**mudu-proc**/` 的函数。
4. **转译**：运行 `mtp`，将阻塞式系统调用转换为组件运行时可用的异步形式。
5. **构建 WASM**：将转译后的源码编译为 `wasm32-wasip2`，并与宿主组件组合。
6. **打包**：运行 `mpm-build create` 生成 `.mpk` 文件。
7. **安装**：在目标服务器上运行 `mcli app-install --mpk <文件>.mpk`。
8. **调用**：运行 `mcli app-invoke --app <应用> --module <模块> --proc <过程> --json '{...}'`。

包格式详见[应用包](packages.md)，完整 walkthrough 参见[你的第一个 MPK 包](../tutorial/tutorials/wallet.md)。
