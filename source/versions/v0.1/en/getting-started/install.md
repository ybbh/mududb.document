# Installation

## Install with mudup

```bash
curl --proto '=https' --tlsv1.2 -fsSL https://github.com/scuptio/mudup/releases/download/latest/mudup-init.sh | sh
mudup install
```

Verify the installed tools:

```bash
mudud --version
mcli --version
mpk --version
mgen --version
mtp --version
```

## Build from Source

Ubuntu or Debian is recommended for development builds.

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

Install workspace binaries from the source repository:

```bash
python script/build/install_binaries.py
```

## Configuration File

The default configuration path is:

```text
${HOME}/.mududb/mududb_cfg.toml
```

If the file does not exist, `mudud` creates a default file on first startup.
