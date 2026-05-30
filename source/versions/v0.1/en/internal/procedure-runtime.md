# Procedure Runtime

The procedure runtime is a passive component: it does not introduce its own scheduler or define an independent execution policy.

Procedure execution is triggered and controlled by the kernel. Database access inside procedures crosses the syscall boundary and is governed by transaction, scheduling, and consistency rules.

This model suits applications that need strong consistency, low-latency business logic, and data locality.
