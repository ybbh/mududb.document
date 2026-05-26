# MuduDB Documentation

::::{div} mududb-hero
MuduDB is a database system for procedure-oriented, data-local execution. It deploys application procedures as WebAssembly components inside the database runtime so transactions, scheduling, data access, and business logic stay inside one controlled boundary.
::::

<div class="mududb-badges">
  <span class="mududb-badge">Version v0.1</span>
  <span class="mududb-badge">English</span>
  <span class="mududb-badge">Markdown / MyST</span>
  <span class="mududb-badge">Versioned docs</span>
</div>

## Quick Links

````{grid} 1 1 2 3
:class-container: mududb-card-grid
:gutter: 3

```{grid-item-card} Install and Start
:link: getting-started/index
:link-type: doc

Install `mudud`, `mcli`, `mpk`, `mgen`, and `mtp`, then start your first local server.
```

```{grid-item-card} SQL and Sessions
:link: tutorials/sql-crud
:link-type: doc

Create tables, write data, query, update, and delete records in the interactive shell.
```

```{grid-item-card} Procedure Applications
:link: tutorials/wallet
:link-type: doc

Build `.mpk` packages, install WebAssembly procedures, and invoke them with `mcli app-invoke`.
```

```{grid-item-card} Administration
:link: administration/index
:link-type: doc

Run the server process, inspect applications, check topology, and maintain deployments.
```

```{grid-item-card} Reference
:link: reference/index
:link-type: doc

Look up commands, configuration, syscalls, and data model semantics.
```

```{grid-item-card} Architecture and Internals
:link: architecture/index
:link-type: doc

Understand the kernel, procedure runtime, toolchain, and WebAssembly integration boundaries.
```
````

## Ten-Minute Trial

::::{div} mududb-quickstart
```bash
mudup install
ulimit -n 65535
mudud
```
::::

Connect from another terminal:

```bash
mcli --addr 127.0.0.1:9527 shell --app demo
```

## Documentation Map

```{toctree}
:caption: Getting Started
:maxdepth: 2

getting-started/index
tutorials/index
```

```{toctree}
:caption: Usage and Operations
:maxdepth: 2

administration/index
reference/index
```

```{toctree}
:caption: Architecture and Project
:maxdepth: 2

architecture/index
internals/index
release-notes/index
```

## Version and Language

This page belongs to the `v0.1` English documentation set. Future database versions should keep separate English documentation under `source/versions/<version>/en`.

- 简体中文: <a href="../zh_CN/index.html">v0.1 简体中文文档</a>

## Recommended Reading Path

1. Install and start MuduDB in {doc}`getting-started/index`.
2. Run SQL and procedure examples in {doc}`tutorials/index`.
3. Look up commands, configuration, and syscall semantics in {doc}`reference/index`.
4. Study system boundaries in {doc}`architecture/index` and {doc}`internals/index`.
