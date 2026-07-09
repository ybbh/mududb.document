# WebAssembly Integration

MuduDB runs user procedures as [WebAssembly components](https://component-model.bytecodealliance.org/) inside a WASI sandbox. This provides portability, isolation, and multi-language support while keeping database access under kernel control.

## Component model

A MuduDB procedure is compiled to a WebAssembly component that targets the `wasm32-wasip2` platform. The component imports a small set of host-provided syscalls and exports the procedure functions marked with `/**mudu-proc**/`.

Before packaging, the guest component is composed with the MuduDB host component so that the final module has the expected import/export signature for the runtime loader.

## WASI sandbox

Procedures execute inside a WASI sandbox with the following properties:

- Database access is available only through explicit kernel syscalls.
- The kernel mediates all network, file, and storage access.
- Resource limits (memory, CPU, syscalls) can be enforced per procedure invocation.

## Language support

The toolchain currently supports Rust as the primary procedure language. AssemblyScript examples also exist. In principle, any language that can emit WASI components can be supported in the future.

| Language | Target | Notes |
|----------|--------|-------|
| Rust | `wasm32-wasip2` | Primary supported language; `mudu_wasm` crate provides bindings. |
| AssemblyScript | WASI component | Supported via the AssemblyScript transpiler and shim. |

## Guest bindings

The `mudu_wasm` crate (published as the Cargo package `mod_0`) provides generated guest bindings and host-side transpilation helpers. It is generated from the WIT interface definitions in `mudu_binding/wit/`.

## Runtime limits

The runtime can enforce per-procedure limits for:

- memory usage,
- CPU time,
- number of syscalls,
- nested call depth.

These limits help isolate user code from the kernel and from other procedures.

## Package format

Compiled components are packaged into `.mpk` archives together with DDL, descriptors, and optional initialization data. See [Application Packages](../administration/packages.md) and the [MPK Manifest Contract](../reference/contracts/mpk_manifest_v1.md).
