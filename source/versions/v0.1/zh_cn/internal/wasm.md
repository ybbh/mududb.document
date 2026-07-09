# WebAssembly 集成

MuduDB 在 WASI 沙箱中运行用户过程 WebAssembly 组件。它在保持数据库访问受内核控制的同时，提供可移植性、隔离性与多语言支持。

## 组件模型

MuduDB 过程被编译为面向 `wasm32-wasip2` 平台的 WebAssembly 组件。该组件导入少量宿主编译的系统调用，并导出标记为 `/**mudu-proc**/` 的过程函数。

打包前，客户组件会与 MuduDB 宿主组件组合，使最终模块具备运行时加载器期望的导入/导出签名。

## WASI 沙箱

过程在 WASI 沙箱中执行，具有以下特性：

- 数据库访问只能通过显式内核系统调用进行。
- 内核中介所有网络、文件与存储访问。
- 可按每次过程调用强制执行资源限制（内存、CPU、系统调用次数）。

## 语言支持

工具链目前主要支持 Rust 作为过程语言，AssemblyScript 示例也已存在。原则上，任何能生成 WASI 组件的语言未来都可支持。

| 语言 | 目标 | 说明 |
|------|------|------|
| Rust | `wasm32-wasip2` | 主要支持语言；`mudu_wasm` crate 提供绑定。 |
| AssemblyScript | WASI 组件 | 通过 AssemblyScript 转译器与 shim 支持。 |

## 客户绑定

`mudu_wasm` crate（以 Cargo 包名 `mod_0` 发布）提供生成的客户绑定与宿主端转译辅助。它由 `mudu_binding/wit/` 中的 WIT 接口定义生成。

## 运行时限制

运行时可对每次过程调用强制执行以下限制：

- 内存使用；
- CPU 时间；
- 系统调用次数；
- 嵌套调用深度。

这些限制有助于将用户代码与内核及其他过程隔离。

## 包格式

编译后的组件与 DDL、描述符及可选初始化数据一起打包为 `.mpk` 归档。详见[应用包](../administration/packages.md)与 [MPK 清单契约](../reference/contracts/mpk_manifest_v1.md)。
