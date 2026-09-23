# 14.23 Exercises

### 14.23.1 Threads and shared state

1. Enumerate all relevant interleavings of two unsynchronised increments modelled as read/compute/write. Identify lost updates.
2. Protect a compound account invariant with a lock and prove which operations must share it.
3. Construct a two-lock deadlock, then eliminate it with global ordering.
4. Implement a bounded thread worker queue with sentinel shutdown and explicit failure transport.
5. Run the same race tests on a conventional and, where available, free-threaded CPython build. Treat differences as observations, not correctness arguments.

### 14.23.2 Processes

6. Compare sequential, thread-pool, and process-pool execution for a CPU workload. Include startup and transfer in the measurement.
7. Vary task granularity to find when process overhead dominates.
8. Demonstrate why the main guard matters under a spawn-style start method.
9. Calculate ideal Amdahl speedup for several serial fractions and processor counts, then compare measurement.

### 14.23.3 Async I/O

10. Write a task-group program in which one child fails. Trace sibling cancellation and exception grouping.
11. Insert blocking sleep into an async task, measure loop delay, and replace it with an awaitable sleep.
12. Design cancellation-safe resource use and test cancellation at every suspension point.
13. Build a bounded producer/consumer pipeline and measure queue depth under producer overload.
14. Define retry policy for idempotent and non-idempotent operations with request identities.

### 14.23.4 Performance

15. Write a performance requirement including percentile, workload, environment, and memory limit.
16. Construct a valid `timeit` comparison and then deliberately contaminate it with setup/I/O to explain the bias.
17. Profile an application and distinguish internal from cumulative time.
18. Use `tracemalloc` to find a deliberately retained global cache; prove the reference path and bound it.
19. Replace one quadratic algorithm with a linear or \(n\log n\) design before micro-optimising syntax.
20. Measure native-boundary batching by comparing one scalar call per item with one vectorised call.

### 14.23.5 Integrated exercise

21. Implement the document-processing system with bounded async acquisition, explicit backpressure, profiled parse placement, transactional result writes, structured task ownership, cancellation, timeouts, idempotent retries, and operational metrics. Prove safety and liveness claims, state conventional/free-threaded CPython assumptions, benchmark representative workloads, profile bottlenecks, measure peak memory, and defend every worker and queue bound.

### 14.23.6 Foundations and quantitative models

22. Give separate definitions of concurrency, parallelism, and asynchrony. Construct one concrete program architecture exhibiting each of the four possible combinations: concurrent but not parallel; parallel with a synchronous caller; asynchronous but locally sequential; and concurrent plus parallel.
23. Draw the ready, running, blocked, and terminated states for a two-thread program that reads two files. Annotate every transition with the event that permits it and distinguish scheduling delay from device delay.
24. For three activities with events \(A_1<A_2\), \(B_1<B_2\), and \(A_1<C_1<B_2\), enumerate all total orders consistent with this partial order. Explain why one observed total order does not define the program’s semantics.
25. Define an invariant for a seat-reservation system with available, held, and sold counts. State which transitions preserve it and which groups of fields must be observed atomically.
26. A service receives 240 requests/s and has a measured mean residence time of 0.35 s. Use Little’s law to estimate mean in-system work. State every stability assumption and explain why the result does not determine p99 latency.
27. A pipeline stage has eight workers, each with mean service demand 20 ms. Calculate nominal capacity and utilisation at 250, 350, and 390 items/s. Explain why the calculation can overestimate real capacity.
28. Given total work \(W=960\) ms and critical-path span \(S=180\) ms, calculate lower bounds on completion time for 1, 2, 4, 8, and 16 ideal processors. Identify where span dominates.
29. A function spends 15 per cent of elapsed time in a serial stage and the rest in an ideally parallel stage. Calculate Amdahl speedup for 2, 4, 8, and infinitely many processors. Compare the result with a claimed twelvefold speedup on eight processors and list possible reasons for disagreement.
30. Construct an example in which throughput doubles but latency of each item increases. Construct another in which median latency improves while throughput remains fixed. State the queue and batching assumptions.
31. Decompose a measured request into ready wait, lock wait, remote wait, CPU execution, and transfer. Propose one instrument for each term and explain double-counting risks when terms overlap.
32. For a workload whose CPU classification changes after a cache warm-up, define two benchmark phases and predict which resource metrics would distinguish them.
33. Model a burst of 10,000 arrivals to a service completing 500/s with no further arrivals. Calculate ideal drain time and queue age for the final item; then list effects omitted by this fluid model.
34. Explain why high utilisation is desirable for an offline batch worker but potentially dangerous for a latency-sensitive dependency. Relate headroom to bursts and service-time variance.
35. Write a one-page performance contract for a command-line data converter. Include startup, warm and cold storage, input distribution, correctness, peak memory, CPU time, and output throughput.

### 14.23.7 Races, locks, and progress

36. Model <code>counter += 1</code> as read, calculate, and write. Enumerate schedules for two activities and identify every schedule that loses an update.
37. Write a deliberately racy inventory reservation and a barrier-based test that forces both threads to pass the availability check before either update. Do not use sleep for ordering.
38. Repair Exercise 37 with one lock. State the linearisation point for successful reservation, failed reservation, and snapshot.
39. Extend the inventory with cancellation of a reservation. Prove non-negativity and conservation under arbitrary interleavings of reserve and cancel.
40. Construct a check–then–act filesystem example and replace it with an operating-system interface providing exclusive creation. Analyse the remaining symbolic-link and directory-permission assumptions.
41. Design a once-only cache fill in which the expensive builder runs outside a global lock. Use a per-key future or condition and specify failure removal, waiter notification, and retry semantics.
42. Compare coarse and fine lock designs for a sharded mapping. Specify the invariant each lock protects, expected contention, and how resizing or cross-shard operations are handled.
43. Implement transfer between accounts by acquiring locks in a stable global order. Prove that the wait-for graph is acyclic even when source and destination arguments are reversed.
44. Deliberately violate the order from Exercise 43 and use barriers to construct a deadlock. Add diagnostics that identify which lock each thread awaits without relying on the program ever terminating naturally.
45. Implement a bounded buffer with one <code>Condition</code>. Explain why every wait uses a <code>while</code> predicate, which state transitions notify producers, and which notify consumers.
46. Replace <code>notify_all</code> with <code>notify</code> in a suitable condition-variable example. Measure wake-ups and explain why the choice is a performance policy only after correctness is preserved.
47. Give a schedule showing starvation without deadlock. Add a fairness policy, then discuss its throughput and implementation cost.
48. Create a two-thread livelock in which both politely yield a resource. Repair it with asymmetric priority or randomised bounded backoff, and demonstrate useful progress.
49. Define obstruction-free, lock-free, and wait-free progress in your own words after consulting an authoritative source. Do not claim that a lock-based Python example has any of these properties.
50. Review a class with three public methods that each acquire locks. Determine whether arbitrary compositions are safe, whether callbacks can re-enter, and whether a reentrant lock repairs or merely conceals the design.

### 14.23.8 Threads and synchronisation primitives

51. Create a non-daemon thread that returns a value or exception through an explicitly owned outcome object. Ensure the main thread joins and observes every outcome.
52. Demonstrate that <code>Thread.join</code> returning does not itself mean the thread completed when a timeout was supplied. Write the correct post-join liveness check.
53. Build a thread-pool mapping that preserves input order and another that processes completion order. Inject variable durations and compare latency to first result.
54. Cause one thread-pool future to fail. Specify whether remaining futures continue, how every exception is observed, and how executor shutdown behaves.
55. Construct the classic deadlock in which a task submitted to a one-worker executor waits for another future submitted to the same executor. Redesign it without increasing worker count.
56. Use an <code>Event</code> as a stop request for workers. Bound stop latency without busy waiting and distinguish graceful stop from forced process termination.
57. Use a <code>Semaphore</code> to protect a fictitious three-connection resource. Prove that resource release occurs on every exception path.
58. Replace a semaphore with <code>BoundedSemaphore</code> and deliberately over-release it. Explain which programming error becomes observable.
59. Use a <code>Barrier</code> to coordinate test phases among four threads. Break the barrier by failing one participant and handle <code>BrokenBarrierError</code> without hanging.
60. Compare thread-local storage with <code>contextvars.ContextVar</code> in an async program that offloads work through <code>asyncio.to_thread</code>. Explain request identity propagation.
61. Measure thread creation, executor reuse, and per-task submission for 1, 10, 1,000, and 100,000 trivial tasks. Interpret overhead without recommending trivial parallelism.
62. Build a reader API returning an immutable snapshot of locked mutable state. Show why returning the internal list would allow the lock protocol to be bypassed.
63. Write a stress test that repeats a shared-state operation under randomised scheduling pressure. Explain why passing it supplies evidence but not proof.
64. Run a shared-container experiment on conventional and free-threaded CPython builds if available. Separate documented guarantees from observed implementation behaviour.
65. Audit a library’s stated thread-safety contract. Identify whether instances, module globals, iterators, callbacks, and shutdown are covered; report all unspecified cases rather than guessing.

### 14.23.9 Queues, processes, and isolation

66. Implement a thread pipeline with three consumers, one sentinel per consumer, and exact <code>task_done</code> accounting. Add a test that would hang if any item is acknowledged twice or not at all, but give the test an outer deadline.
67. Change Exercise 66 so workers return tagged success/failure outcomes. Ensure the owner observes every failure and distinguish input rejection from worker defect.
68. Design shutdown for a bounded thread queue when a consumer fails while producers are blocked on <code>put</code>. Demonstrate why simply sending sentinels can deadlock.
69. Add priority to a work queue. Specify tie-breaking, starvation prevention, and whether a later urgent item may pass an earlier ordinary item.
70. Compare queue item count with byte-weighted admission for payloads varying from 1 KiB to 100 MiB. Implement a token accounting scheme and prove tokens are returned.
71. Run the same pure-Python CPU kernel sequentially, in threads, and in processes. Record conventional CPython mode, worker count, CPU time, wall time, and result equivalence.
72. Repeat Exercise 71 with a documented native operation that releases the GIL. Explain why the result cannot be generalised to arbitrary Python code.
73. Compare <code>spawn</code>, <code>fork</code>, and <code>forkserver</code> where the platform provides them. Record inherited state, startup, logging behaviour, and safety constraints.
74. Omit the main guard under a spawn-style process start in a disposable program. Explain recursive import/process creation, then repair it.
75. Submit a closure, lambda, bound method, and top-level function to a process pool. Determine which values serialise in your environment and distinguish convenience observations from portable design.
76. Vary process-pool chunk size for uniform and highly variable task durations. Plot throughput and final straggler time and explain load-balance trade-offs.
77. Measure transfer of 1 KiB, 1 MiB, and 100 MiB arguments through a process pool. Separate serialisation, copying, computation, and result transfer as far as the tools permit.
78. Use <code>multiprocessing.shared_memory</code> for a fixed-width array. Define byte order, element width, shape, ownership, and unlink protocol before writing computation.
79. Introduce two writers to Exercise 78. Protect a compound update or partition non-overlapping slices, and demonstrate what invariant makes the design safe.
80. Compare a manager proxy with a local dictionary and message batching. Count remote method calls and explain why object-like syntax hides process crossings.
81. Kill a process-pool worker during a task. Observe future and pool behaviour, then design supervisor policy for retrying only safely identified work.
82. Measure memory of fork-based workers before and after touching a large parent-created object. Explain copy-on-write and why refcount or allocator activity can change private pages.
83. Use a single database-writer process receiving commands from workers. Specify transaction boundaries, result acknowledgement, idempotency, and backpressure.
84. Design privilege separation in which an untrusted parser runs in a constrained worker process. Identify the IPC schema, resource limits, crash semantics, and validation still required in the parent.
85. Calculate effective runnable threads for \(n\) service instances, \(p\) process workers, and \(t\) native-library threads. Measure oversubscription while sweeping one dimension and propose a global budget.

### 14.23.10 Coroutines, tasks, and structured concurrency

86. Call an async function without awaiting it. Inspect the returned coroutine object and explain why its body has not completed.
87. Write two coroutines whose outputs reveal sequential awaiting, then create tasks to overlap them. Trace creation, first execution, suspension, resumption, and result observation.
88. Demonstrate that <code>await</code> does not necessarily yield by awaiting an already-completed future. Explain why event-loop fairness cannot be inferred from the keyword alone.
89. Insert a synchronous blocking call into an async server simulation. Measure event-loop lag and repair the path with an async API or bounded offload.
90. Use <code>asyncio.sleep(0)</code> as a checkpoint in a CPU loop. Measure responsiveness and overhead across checkpoint intervals and explain why processes may be the better solution.
91. Create ten tasks with variable duration and compare <code>gather</code> result order with completion-order processing. Preserve association between input and result.
92. Cause one child passed to <code>gather</code> to fail under default behaviour. Observe siblings, then contrast the same experiment in <code>TaskGroup</code>.
93. Use a task group whose children raise two different exception types during coordinated release. Handle one type with <code>except*</code> and propagate the rest.
94. Capture task handles in a task group and read results only after successful scope exit. Specify the partial-result policy when the group fails.
95. Construct nested task groups corresponding to service/component/request ownership. Draw the exception and cancellation propagation tree.
96. Implement an async context manager for a resource that can fail on open, in the body, and on close. Test which exceptions escape in each combination.
97. Use <code>asyncio.Lock</code> to protect a task-shared invariant across awaits. Then redesign so one owner task receives messages and compare proof obligations.
98. Implement an async condition-variable wait with a predicate. Trigger spurious-like notifications that do not satisfy the predicate and verify the waiter remains correct.
99. Use an async semaphore for an external call, recording acquisition wait separately from service time. Drive the dependency into saturation and interpret both distributions.
100. Build an async iterator over paginated results. Ensure response resources close when the consumer stops after the first page.
101. Implement a fixed number of async workers consuming an async iterable without creating one task per item. Bound both queue and active calls.
102. Offload a blocking function with <code>asyncio.to_thread</code>. Cancel the awaiting task and prove whether the thread function continues.
103. Compare <code>to_thread</code> with <code>run_in_executor</code> for context propagation, executor selection, cancellation, and call signature.
104. Start a background task, deliberately lose its reference, and observe failure reporting. Replace it with a structured owner or explicit task registry.
105. Write a loop exception handler suitable for tests that turns unobserved task failures into test failure. Explain limitations.
106. Implement a stream writer that calls <code>drain</code> according to the library contract. Compare memory when producing faster than the peer reads.
107. Use <code>asyncio.wait</code> with a timeout. Explicitly cancel and await the returned pending tasks, then compare with <code>wait_for</code>.
108. Experiment with an eager task factory only if supported by the interpreter version. Show a program whose observable ordering changes and state why this is a semantic choice.
109. Model an async service with one task per connection and derive memory/file-descriptor bounds. Reject a design that relies only on low per-task overhead.
110. Build a structured async test that cancels a task at each await boundary. Verify invariant restoration and absence of leaked resources.

### 14.23.11 Cancellation, deadlines, and backpressure

111. Write a coroutine that catches <code>CancelledError</code>, records cancellation, cleans up, and re-raises. Contrast with a defective version that reports success.
112. Measure cancellation latency of a CPU loop with no await and with periodic checkpoints. Identify a checkpoint interval satisfying a stated responsiveness budget.
113. Make asynchronous cleanup block indefinitely in a controlled test. Add a cleanup deadline and specify external recovery for the unreleased resource.
114. Use <code>asyncio.shield</code> around a narrow commit step. Retain and observe the inner task; demonstrate the abandoned-work defect when its reference is lost.
115. Give three sequential operations one repeated relative timeout and measure total duration. Replace them with one propagated monotonic deadline.
116. Compare <code>asyncio.timeout</code>, <code>wait_for</code>, and <code>wait</code> with the same slow coroutine. Trace which task is cancelled and when control returns.
117. Design an idempotency-key table for an operation whose response can be lost after commit. Specify atomic insertion, duplicate response, conflicting payload, and retention.
118. Simulate 1,000 clients retrying at identical fixed intervals. Add exponential backoff with full jitter and plot attempt distribution.
119. For a producer rate of 1,200/s and sustainable consumer rate of 1,000/s, calculate backlog over five minutes. Show why every finite queue eventually fills.
120. Choose a queue bound from a 250 ms queue-wait budget and 800/s completion rate. Treat the calculation as an initial estimate and design a burst test.
121. Implement block, reject, drop-newest, and coalesce policies for telemetry. State the semantic contract and metric for every discarded update.
122. Demonstrate head-of-line blocking with one slow FIFO item. Evaluate separate queues, shortest-job-first estimates, and fairness consequences.
123. Implement both a concurrency semaphore and a token-bucket-like rate controller. Drive variable latency and show why neither substitutes for the other.
124. Design load shedding for three priority classes. Reserve capacity, prevent permanent starvation, and specify what each caller observes.
125. Test overload recovery: ramp above capacity, hold, return below capacity, and measure queue age, rejection, throughput, and time to restore the latency objective.

### 14.23.12 Benchmarking and profiling

126. Inspect every clock returned by <code>time.get_clock_info</code> on your platform. Explain monotonicity, adjustability, resolution, and appropriate uses.
127. Measure timer-call overhead and effective tick granularity without claiming that subtracting mean overhead repairs every short benchmark.
128. Write two <code>timeit</code> experiments that answer different questions about set versus list membership: preconstructed lookup and construction-plus-lookup.
129. Enable cyclic garbage collection inside a <code>timeit</code> setup and compare allocation-heavy results with the default. Explain applicability.
130. Build an interleaved A/B benchmark with randomised treatment order and raw observation storage. Inject artificial machine drift and show the bias of blocked ordering.
131. Compare cold-start, warmed, and long-running performance of an import-heavy command. Define exactly where timing begins and ends.
132. Measure a function across geometrically increasing input sizes. Plot \(T(n)\), \(T(n)/n\), \(T(n)/(n\log n)\), and \(T(n)/n^2\); identify the most plausible regime without claiming proof.
133. Construct a latency dataset with a low median and severe tail. Report mean, median, p95, p99, maximum, and sample count under a named quantile convention.
134. Simulate coordinated omission in a closed-loop load generator, then schedule open-loop arrivals and compare recorded latency distributions.
135. Measure a fan-out request waiting for all children. Relate parent tail latency to child count and correlated slowdowns.
136. Generate a throughput-versus-offered-load curve, marking the SLO-compliant knee, saturation, rejection, and recovery. Do not select worker count from maximum throughput alone.
137. Use bootstrap resampling or another justified method to estimate uncertainty in a median ratio. Explain assumptions and why it cannot correct workload bias.
138. Profile the same workload with <code>cProfile</code> and an available sampling profiler. Compare perturbation, native visibility, call counts, and ranking.
139. Read <code>pstats</code> output by cumulative and internal time. Choose one function whose interpretation changes and explain its caller graph.
140. Add stage timers for semaphore wait and service. Increase concurrency until service time grows, then identify the bottleneck with supporting metrics.
141. Measure event-loop lag while a CPU task runs. Offload the task to a thread and a process, comparing responsiveness, throughput, and cancellation.
142. Profile each process-pool worker into a unique file. Identify load imbalance and show why one aggregate profile can conceal a straggler.
143. Create a small flame graph or stack-aggregation visual from samples. Explain why horizontal position is not chronological order.
144. Form a causal optimisation hypothesis from a profile, predict the end-to-end effect with Amdahl’s law, implement it, and explain any prediction error.
145. Write a reproducibility record containing source revision, command, input digest, interpreter/build, dependencies, operating system, CPU quota, raw samples, and analysis method.

### 14.23.13 Memory, representation, and native boundaries

146. Compare Python allocation snapshots, process RSS, and peak RSS for a create–release cycle. Explain why the three measurements need not move together.
147. Deliberately retain payloads through completed task exceptions. Find the ownership path, repair it, and confirm bounded repeated-cycle behaviour.
148. Implement an unbounded memoisation cache under adversarial unique keys. Replace it with a capacity/expiry policy and report hit value, eviction, and memory.
149. Use weak references for ancillary metadata. Demonstrate that collection timing is not a deterministic capacity policy.
150. Compare materialised and streamed transformations while varying consumer speed. Measure true end-to-end peak memory rather than one function in isolation.
151. Admit variable-size payloads first by item count and then by byte tokens. Inject one extreme item and compare memory safety.
152. Measure copy-on-write erosion in worker processes that read and then mutate parent-created data. Record proportional/private memory where available.
153. Compare a list of Python integers with a packed fixed-width representation. Account for schema restrictions, memory, conversion, and repeated-kernel time.
154. Transform a quadratic nested join into an indexed join. Test duplicate keys and absent references, measure scaling, and justify expected dictionary assumptions.
155. Benchmark scalar boundary calls against batches over a range of sizes. Locate the empirical break-even point and measure first-item latency.
156. Rewrite a multi-pass materialising calculation as a one-pass aggregate. Verify numerical semantics, iterator consumption, and peak memory.
157. Identify a vectorised expression that creates large temporaries. Use fusion, in-place operation, or chunking and analyse aliasing and rounding changes.
158. Bind to a small existing C ABI in a disposable project. Specify exact widths, ownership, error conversion, callback lifetime, and platform assumptions; test invalid inputs safely.
159. Build a tiny Cython kernel and compare it with a Python reference. Test overflow, non-contiguous buffers, tiny-input overhead, large-input throughput, and GIL behaviour.
160. Design a binary-wheel test matrix across supported Python versions, platforms, architectures, conventional/free-threaded modes, and ABI strategies. State which cells are intentionally unsupported.

### 14.23.14 Integrative design and research

161. Design a web crawler with per-origin concurrency, global rate, robots/policy compliance, deduplication, bounded frontier, cancellation, durable checkpointing, and process-isolated parsing. Provide safety and liveness arguments.
162. Design a parallel build executor for a dependency DAG. Schedule only ready nodes, preserve failure causality, cap CPU/memory, and prove no node runs before dependencies succeed.
163. Design a real-time telemetry aggregator that may coalesce updates but must never lose alarms. Separate channels and overload semantics by message class.
164. Design a bank-transfer processor under at-least-once delivery. Use idempotency, transactional commit, reconciliation, and backpressure; explain why task cancellation is not rollback.
165. Design an image service combining async upload, native decode, process isolation, internal library threads, byte-weighted admission, and storage transactions. Derive a global concurrency budget.
166. Design graceful shutdown for a hybrid async/thread/process service. Give a total order over admission stop, drain, cancellation, executor close, resource close, and telemetry flush; test repeated signals.
167. Compare actor ownership, lock-protected shared state, immutable snapshots, and transactional database state for one collaborative document model. Identify ordering and failure trade-offs.
168. Specify and implement a deterministic simulator for selected concurrent interleavings of a small state machine. Use it to find a race that stress testing rarely exposes.
169. Apply a model checker or systematic concurrency-testing tool, where available, to a bounded protocol. Translate its counterexample back into a Python test.
170. Read the current official documentation and relevant PEPs for free-threaded CPython. Audit one extension dependency and distinguish build capability, runtime GIL state, documented support, and observed behaviour.
171. Reproduce a published concurrency or performance result using its artefacts. Report deviations in hardware, software, workload, statistics, and outcome without selectively omitting negative results.
172. Write a technical decision record choosing among threads, processes, and asyncio for a concrete system. Include rejected alternatives, evidence, portability, observability, and reversal cost.
173. Conduct a full performance investigation in which the original suspected hotspot is not causal. Preserve the evidence trail from requirement through profile, falsified hypothesis, revised model, and verified change.
174. Audit a production-like service for unbounded dimensions: tasks, queues, payload bytes, retries, caches, logs, connections, temporary files, process workers, and shutdown time. Add explicit policies and tests for each.
175. Capstone: implement, verify, and document a recoverable document-processing service derived from Section 14.21. Supply a sequential oracle, concurrent implementation, fault-injection suite, invariant argument, load curve, latency distributions without coordinated omission, CPU and memory profiles, conventional/free-threaded analysis, deployment budgets, native-boundary decision, reproducibility package, and a written account of every limitation.
