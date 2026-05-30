# Per-core Worker Model

## 1. Overview

The per-core worker model assigns a dedicated worker execution context to a CPU core (or equivalent hardware slice). Each worker hosts an independent runtime, scheduling loop, and local state for the partitions it owns. The model trades coarse-grained multiprocessing and locks for per-worker isolation and cooperative, event-driven concurrency inside each worker to achieve low-latency, high-throughput operation.

## 2. Motivation

- Reduce synchronization overhead: by keeping most state and execution local to a worker, the design minimizes cross-thread locking and atomic contention.
- Predictable latency: per-core affinity reduces context-switch jitter and improves cache utilization for hot data and code paths.
- Scalable concurrency: many lightweight async tasks can run cooperatively inside a worker without spawning OS threads for each task.
- Operational isolation: faults or overloads can be contained to a worker and handled via drain/restart or partition migration.

## 3. Per-worker model

- Affinity: a worker is typically pinned to a CPU core (or logical core) and runs a single-threaded event loop or an io_uring-backed runtime.
- Runtime components inside a worker:
  - Event loop / async executor: cooperatively schedules tasks (async functions, syscalls, timers).
  - Local task queues: high-priority and background queues to separate latency-sensitive work from housekeeping.
  - Partition-local state: storage and caches for partitions assigned to this worker (physical relations keyed by (table_id, partition_id)).
  - Networking endpoint: a per-worker TCP listener (when tcp_multi_port enabled) or shared acceptor with handoff.
- Concurrency model: cooperative multitasking using async/await primitives (or transpiled equivalents). Tasks yield on I/O or when awaiting remote RPC results, allowing other tasks to make progress without OS thread switches.

Implementation notes:
- Use of io_uring or an efficient async runtime (Tokio) inside the worker to achieve high I/O concurrency with low overhead.
- Workers allocate and manage fixed resources (thread-local caches, pre-registered buffers) to reduce runtime allocation costs.

## 6. Inter-worker communication

- Message-passing: workers communicate via well-defined message channels or RPC over an internal message bus rather than shared-memory locks for coordination and remote partition access.
- Remote partition RPCs: when a worker receives a request for a partition it does not own, it forwards the request to the owning worker via the internal RPC channel. The requester awaits the response asynchronously.
- Backpressure and flow control: senders must handle backpressure (bounded queues) and apply retries or circuit-breaker logic if a target worker is overloaded.
- Ordered vs unordered messages: important operations (e.g., commit-phase messages) may require ordering guarantees; the message layer supports ordering or causal sequencing when needed.
- Batch and coalescing: small remote requests are often batched or coalesced to reduce per-message overhead and improve throughput.

Failure handling:
- Detect remote worker failure quickly (timeouts, connection errors) and trigger topology refresh and partition re-assignment.
- Drain and replay: when migrating partitions, workers drain outstanding messages and may replay or forward inflight operations during migration.

## 7. Data locality and partitioning

For a comprehensive explanation of the partition model, placement, and the partition -> worker mapping, see the Partitioning document: ./partitioning.md

- Partition placement: logical partitions are assigned to workers (partition_id -> worker_id). Workers keep local copies of the placement and expose endpoints for their owned partitions.
- Local execution: operations for partitions owned by the local worker execute without inter-worker RPCs, exploiting cache locality and minimized locking.
- Routing: the client or adapter resolves partition -> worker mapping (via topology) and opens sessions bound to the target worker to achieve direct locality.
- Hot partition mitigation: hot partitions can be monitored and moved, or split into finer-grained partitions, to distribute load across workers.

Interaction with per-core model:
- Because each worker concentrates storage and execution for its partitions, per-core affordances (CPU caches, local buffers, pinned threads) amplify locality benefits.
- Sharded TCP ports and per-worker listeners improve accept affinity and reduce kernel-networking contention, aligning network flows with partition ownership.

Summary

The per-core worker model balances high performance and operational simplicity by localizing state and using cooperative asynchronous concurrency inside each worker while relying on message-passing for cross-worker coordination. It is particularly effective for workloads with strong locality and predictable partitioning semantics.
