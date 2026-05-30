# Overview

MuduDB is built around data-local business procedure execution.

The database kernel owns storage, transactions, query execution, and scheduling control. User procedures are hosted as WebAssembly Component Model modules and access database capabilities through controlled syscalls.

This structure reduces cross-process and cross-network traffic on critical paths while keeping correctness boundaries concentrated in the database kernel.
