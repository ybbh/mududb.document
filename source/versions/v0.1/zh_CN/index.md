# MuduDB 文档

::::{div} mududb-hero
MuduDB 是一个面向过程与数据贴近执行的数据库系统。它把应用过程以 WebAssembly 组件形式部署到数据库运行环境中，让事务、调度、数据访问和业务逻辑处在同一个受控边界内。
::::

<div class="mududb-badges">
  <span class="mududb-badge">版本 v0.1</span>
  <span class="mududb-badge">简体中文</span>
  <span class="mududb-badge">Markdown / MyST</span>
  <span class="mududb-badge">多版本文档</span>
</div>

## 快速入口

````{grid} 1 1 2 3
:class-container: mududb-card-grid
:gutter: 3

```{grid-item-card} 安装与启动
:link: getting-started/index
:link-type: doc

安装 `mudud`、`mcli`、`mpk`、`mgen` 和 `mtp`，启动第一个本地服务。
```

```{grid-item-card} SQL 与会话
:link: tutorials/sql-crud
:link-type: doc

用交互式 shell 创建表、写入数据、查询、更新和删除记录。
```

```{grid-item-card} 过程应用
:link: tutorials/wallet
:link-type: doc

构建 `.mpk` 应用包，安装 WebAssembly 过程并通过 `mcli app-invoke` 调用。
```

```{grid-item-card} 管理与运维
:link: administration/index
:link-type: doc

管理服务进程、查看应用、检查拓扑，并维护部署环境。
```

```{grid-item-card} 参考手册
:link: reference/index
:link-type: doc

查询命令、配置、系统调用和数据模型语义。
```

```{grid-item-card} 架构与内部实现
:link: architecture/index
:link-type: doc

理解内核、过程运行时、工具链和 WebAssembly 集成边界。
```
````

## 十分钟试运行

::::{div} mududb-quickstart
```bash
mudup install
ulimit -n 65535
mudud
```
::::

新终端中连接交互式 SQL shell：

```bash
mcli --addr 127.0.0.1:9527 shell --app demo
```

## 文档结构

```{toctree}
:caption: 入门
:maxdepth: 2

getting-started/index
tutorials/index
```

```{toctree}
:caption: 使用与运维
:maxdepth: 2

administration/index
reference/index
```

```{toctree}
:caption: 架构与项目
:maxdepth: 2

architecture/index
internals/index
release-notes/index
```

## 版本与语言

当前页面属于 `v0.1` 简体中文文档。后续数据库版本会在 `source/versions/<version>/zh_CN` 下维护自己的中文文档，历史版本不会被新版本覆盖。

- English: <a href="../en/index.html">v0.1 English documentation</a>

## 推荐阅读路径

1. 从 {doc}`getting-started/index` 安装并启动 MuduDB。
2. 按 {doc}`tutorials/index` 完成一次 SQL 与过程调用流程。
3. 在 {doc}`reference/index` 查询命令、配置和系统调用语义。
4. 通过 {doc}`architecture/index` 和 {doc}`internals/index` 理解系统边界。
