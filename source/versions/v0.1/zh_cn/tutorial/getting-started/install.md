# 安装

## 使用 mudup 安装

```bash
curl --proto '=https' --tlsv1.2 -fsSL https://github.com/scuptio/mudup/releases/download/latest/mudup-init.sh | sh
mudup install
```

验证已安装的工具：

```bash
mudud --version
mcli --version
mpk --version
mgen --version
mtp --version
```

## 从源码构建

开发构建建议使用 Ubuntu 或 Debian。

```bash
sudo apt-get update -y
sudo apt-get install -y python3 python3-pip python-is-python3 build-essential curl liburing-dev clang libclang-dev llvm-dev pkgconf
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup toolchain install nightly
rustup default nightly
rustup target add wasm32-wasip2
python -m pip install toml tomli-w
cargo install cargo-make
```

从源码仓库安装工作区二进制文件：

```bash
python script/build/install_binaries.py
```

## 配置文件

默认配置文件路径为：

```text
${HOME}/.mududb/mududb_cfg.toml
```

如果文件不存在，`mudud` 会在首次启动时创建默认文件。
