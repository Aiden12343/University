# 14.22 Common misconceptions consolidated

1. **“Concurrent means simultaneous.”** Lifetimes overlap; one core can interleave them.
2. **“The GIL prevents races.”** It serialises selected interpreter execution in conventional CPython, not compound application invariants.
3. **“Threads cannot use multiple cores.”** Native code can release the GIL; free-threaded builds differ; the claim must name workload and runtime.
4. **“Processes share nothing.”** They can communicate and share explicit memory or external resources; isolation changes the default.
5. **“Async is parallel.”** Event-loop tasks cooperate on a thread unless other executors or native work add parallel resources.
6. **“Await makes blocking code non-blocking.”** Only an awaitable operation that yields control permits other tasks to run.
7. **“A timeout stops the operation.”** It stops waiting or requests cancellation under a contract; underlying effects may continue.
8. **“More workers means faster.”** Contention, overhead, serial fractions, memory bandwidth, and downstream capacity bound useful concurrency.
9. **“Profiling and benchmarking are the same.”** Benchmarking measures outcomes; profiling attributes costs.
10. **“Python is slow.”** Performance is comparative and workload-specific; dynamic dispatch costs coexist with fast native libraries and I/O-bound systems.

### 14.22.1 Concurrency vocabulary must retain its distinctions

Concurrency describes overlapping lifetimes; parallelism describes simultaneous execution resources. Asynchrony describes a control style in which completion can be observed later rather than by blocking the current activity. These ideas often coincide but none implies the others. An asynchronous file API may delegate to a blocking worker thread; a parallel numerical kernel can be called synchronously; one-core event-loop tasks are concurrent without being parallel.

Atomicity, thread safety, and transactionality are also distinct. An atomic operation appears indivisible at a stated interface. A thread-safe object preserves its documented invariants under supported concurrent calls. A transaction groups effects under a persistence/isolation contract. Several thread-safe calls do not automatically form one atomic transaction, and a thread lock does not make an update durable.

A race condition is a semantic defect whose manifestation depends on relative timing. Nondeterminism is broader: several completion orders can be legitimate. A data race is a memory-model term and should not be used as a loose synonym in arguments requiring language-specific precision. Correctness means all admitted schedules satisfy the contract, not that one test run produced the expected output.

Deadlock, livelock, and starvation all prevent desired progress through different mechanisms. Deadlock is cyclic or otherwise permanent waiting; livelock is continued reaction without useful advance; starvation denies one participant while others progress. A timeout detects lack of timely completion but does not diagnose which occurred.

### 14.22.2 Primitive folklore is not a proof

The following claims are particularly dangerous because they appear to derive correctness from current observations:

| Folklore claim | Required replacement |
|:---|:---|
| “This dictionary operation is atomic in CPython.” | State the documented operation contract and protect the complete application invariant. |
| “The GIL is a lock around my objects.” | Use an application lock, confinement, immutability, or message ownership. |
| “The sleep makes the race reproducible.” | Use a barrier or controlled scheduler to establish the intended ordering. |
| “No test has deadlocked.” | Establish a global lock order or otherwise prove wait-cycle exclusion. |
| “One sentinel closes a worker pool.” | Supply a close protocol accounting for every independent consumer and failure. |
| “Daemon threads clean themselves up.” | Stop admission, signal, join, and close resources explicitly. |
| “A queue transfers ownership.” | Ensure the sender relinquishes mutable aliases or copy/freeze the message. |
| “A timeout killed it.” | Inspect the API’s cancellation, abandonment, and cleanup semantics. |
| “An executor cancels running work.” | Distinguish pending cancellation from a function already executing. |
| “Internal locks make iteration safe.” | Synchronise external mutation for the entire iteration protocol. |

An implementation detail can support a version-specific optimisation after being documented and tested; it cannot silently become a cross-version correctness theorem. This is especially important during CPython’s transition toward optional free-threaded operation, where accidental reliance on global serialisation is exposed.

### 14.22.3 Scale claims require a resource model

“Async scales” omits memory per task, file descriptors, connection limits, queue bounds, downstream capacity, event-loop CPU, and failure traffic. “Processes use all cores” omits serialisation, start-up, partition balance, shared bandwidth, and nested native threads. “Threads are lightweight” omits stack reservation, scheduler overhead, thread-local state, and contention.

Worker count is not demand. A hundred workers do not create a hundred cores, connections, or storage lanes. They create up to a hundred competing lifetimes. Useful concurrency is the amount that exposes otherwise idle capacity while meeting latency and resource limits. Beyond that region, extra work increases queueing and can reduce completed throughput.

Rate and concurrency must both be bounded where latency varies. A concurrency bound controls simultaneous operations; a rate bound controls starts per interval. Queue capacity controls waiting items. Input-size limits control memory and computation per item. These controls form a multi-dimensional admission policy.

Backpressure is end-to-end only when it reaches the source capable of slowing or rejecting arrivals. Bounding an internal queue while an unbounded task list accumulates upstream merely moves the backlog. Spilling to disk similarly moves the bound unless disk capacity, retention, and replay rate are governed.

### 14.22.4 Cancellation is not rollback

Cancellation requests that future execution stop. It does not reverse bytes sent, rows committed, files renamed, or messages published. A task group’s cancellation of sibling tasks restores lexical lifetime ownership, not business atomicity. Transactions, staging, idempotency keys, compensating operations, and reconciliation address external effects.

Cancellation-safe code maintains invariants at suspension points, uses context managers for resources, propagates cancellation after local handling, and bounds cleanup. It also anticipates abrupt termination where no Python cleanup runs. A process’s correctness cannot depend on every <code>finally</code> suite executing.

Timeout is a budget policy. A timeout can expire before cancellation is observed and can leave an external operation’s outcome unknown. Relative timeouts at every layer can exceed the end-to-end objective; a propagated deadline prevents that multiplication. Backoff changes attempt timing; only idempotency or reconciliation changes duplicate-effect safety.

### 14.22.5 Performance numbers are conditional propositions

A benchmark result should be read as: under environment \(E\), workload \(W\), implementation \(I\), and method \(M\), observations \(O\) occurred. It is not an intrinsic property of a syntax fragment. Change input distribution, runtime state, hardware, concurrency, or metric and the result can reverse.

Minimum microbenchmark time, mean service time, median response latency, p99 latency, maximum throughput, process CPU time, and RSS answer different questions. Reporting one without naming it prevents comparison. Percentiles require sufficient observations and a defined estimator. Throughput above saturation can hide unacceptable queues. Error responses can make latency appear to improve.

A profiler is similarly conditional. Deterministic profilers perturb call-heavy code; sampling profilers estimate from stack observations; line profilers alter selected functions; allocation tracers omit some native memory. A hotspot is attributed cost under the observed workload. End-to-end unprofiled measurement verifies the intervention.

### 14.22.6 Memory misconceptions are lifetime misconceptions

Deleting a name removes one binding, not necessarily the object. Finished tasks, tracebacks, closures, caches, callbacks, global collections, and native handles can retain graphs. A generator reduces eager materialisation only when its producer and consumer lifetimes also stream. A bounded number of items does not bound bytes if item sizes vary.

Python object reclamation and operating-system RSS do not move in lockstep. Allocators reuse blocks, arenas remain partially occupied, native libraries hold pools, and shared process pages have complex accounting. Diagnose at the layer named by the requirement.

Copy-on-write after process creation does not mean memory remains shared. Mutations and even some bookkeeping can dirty pages. Shared memory avoids some copying but introduces a data format and synchronisation protocol. A manager proxy gives remote object-like methods, not local-memory cost.

### 14.22.7 Optimisation must preserve the semantic surface

Changing a list to a set can alter order and duplicate handling. Changing Python integers to fixed-width native integers introduces overflow. Reordering floating-point summation changes rounding. Parallel execution can change exception order and external side effects. Caching changes freshness and retention. Batching changes latency and partial-failure granularity.

Every optimisation therefore has two proofs: it improves a measured objective, and it preserves or intentionally revises the contract. A faster implementation with subtly different semantics is a new program, not an optimisation of the old one.

The hierarchy of effort is usually:

1. eliminate unnecessary work;
2. choose a better algorithm;
3. choose a representation with appropriate locality and schema;
4. batch expensive boundaries;
5. exploit safe concurrency and parallelism;
6. move a measured kernel to specialised native code;
7. tune low-level details only while evidence supports them.

The ordering is a heuristic rather than a law, but it keeps attention on the largest causal levers. Clear code is not opposed to performance; clear contracts and separable kernels make valid measurement and replacement possible.
