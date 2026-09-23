# 20.37 Exercises

### 20.37.1 Service models, processes, and supervision

1. Choose a real or hypothetical service and identify its users, obligations, data plane, control plane, durable state, human roles, and external dependencies. Draw both authority and data-flow boundaries.
2. Distinguish development, test, staging, canary, and production by consequence rather than hostname. For each, state which real obligations and data classes it may exercise.
3. Write a process contract defining executable, arguments, directory, environment, operating-system identity, descriptors, ports, readiness, health, shutdown, exit statuses, state, and resource bounds.
4. Implement graceful shutdown for a queue worker. Simulate termination before claim, during computation, after external side effect, before acknowledgement, and after its grace deadline.
5. Model a request server as starting, ready, draining, and stopped states. Prove which transitions close admission and what happens to long-lived requests during each.
6. Run a small program directly as container PID 1 and through a reviewed init wrapper. Create child processes, terminate parents, and observe signal propagation and child reaping.
7. Write a systemd or equivalent service definition for a Python worker. Add minimal environment, fixed working directory, restart limits, resource controls, read-only paths, one writable state path, and verified readiness.
8. Make the worker deliberately fail with invalid configuration, transient dependency failure, invariant failure, clean completion, and external termination. Define stable exit classifications and verify supervisor behaviour.
9. Implement capped exponential restart delay with full jitter using injected randomness. Simulate 1,000 replicas failing together and compare restart distributions with deterministic backoff.
10. Design a watchdog whose evidence must pass through the main event loop or work queue. Demonstrate why a dedicated heartbeat thread can report health during deadlock.
11. Record a bounded crash report containing artifact, configuration, termination cause, last progress, and resource state. Ensure repeated failure cannot exhaust storage.
12. Compare foreground supervision with historical self-daemonisation. Identify duplicated responsibilities for logs, PID files, privilege dropping, restart, and descriptors.
13. Define operational toil for the service. Measure frequency, human time, growth relationship, error risk, and automation cost for five recurring tasks.
14. Select one manual task that should remain manual because it is rare, judgement-heavy, or dangerous. Design evidence and safeguards without forcing automation.
15. Integrate Chapters 2, 11, and 14 by tracing one worker from process creation through descriptors, signal, memory limit, thread shutdown, file flush, and final exit status.

### 20.37.2 Configuration and filesystem state

16. Design a typed configuration schema with defaults, file, environment, command-line, and remote sources. Specify precedence, nested-map merge, deletion, empty value, lists, and unknown keys.
17. Build a configuration provenance report that reveals source and version for non-secret values while redacting credentials, tokens, URLs containing passwords, and sensitive paths.
18. Test lexical, structural, semantic, and environmental validation separately. Make error messages actionable without revealing secrets.
19. Add a check-only startup mode and use it as a deployment precondition. Simulate an unavailable dependency and distinguish impossible configuration from transient validation failure.
20. Design dynamic configuration distribution with immutable versions, authorisation, validation, last-known-good state, telemetry, and rollback. Partition values that must remain static.
21. Create a feature-flag registry with type, owner, purpose, default, targeting, creation, expiry, audit, and removal condition. Find every flag lacking a safe failure default.
22. Demonstrate inconsistent mixed-replica configuration. Determine which properties tolerate it and which require a coordinated version transition.
23. Classify each service path as artifact, durable state, cache, temporary, runtime, log, secret, or socket. Assign owner, permissions, quota, persistence, backup, and cleanup.
24. Implement atomic file replacement on one chosen filesystem. Crash or terminate at each step and document visibility and persistence, including directory synchronisation requirements.
25. Contrast atomicity, durability, and consistency using a file plus database metadata update. Construct a state that satisfies each property separately but not the others.
26. Create temporary files safely under a shared directory and under a private runtime namespace. Test names, modes, links, quotas, cleanup, and abrupt termination.
27. Evaluate advisory file locking across two processes, descriptor duplication, process crash, and where possible a network mount. State the actual guarantee instead of “locked”.
28. Build a bounded cache whose deletion cannot affect correctness. Demonstrate recomputation and distinguish cache loss from durable-state loss in monitoring.
29. Design volume separation for uploads, temporary expansion, retained results, and logs. Show how mount flags, quotas, and backup policy differ.
30. Integrate Chapter 19 by threat-modelling every writable path for link attacks, traversal, malicious content, secret disclosure, and resource exhaustion.

### 20.37.3 Artifacts, builds, and provenance

31. Enumerate the complete build closure for a Python wheel and container image: source, lock, backend, interpreter, compiler, libraries, locale, clock, ordering, architecture, and tools.
32. Build a wheel twice in clean environments and compare digests and archive metadata. Remove or document every source of nondeterminism found.
33. Distinguish hermeticity from reproducibility with four build experiments: isolated deterministic, isolated nondeterministic, networked deterministic, and networked mutable.
34. Construct a content-addressed release record binding source revision, artifact, SBOM, provenance, signature, tests, configuration schema, database range, and target architecture.
35. Prove that test evidence refers to the deployed digest. Attempt to substitute a different artifact under the same human version and ensure admission rejects it.
36. Design artifact retention for active, canary, rollback, unsupported, and legally retained releases. Include dependency and key availability.
37. Create a build graph and cache keys for dependency installation, wheel build, tests, and image assembly. Poison an under-specified cache and then repair the key.
38. Produce an SBOM through two independent methods and reconcile missing, generated, vendored, native, and dynamically obtained components.
39. Verify provenance subject digest, builder identity, source, invocation, and materials. Explain which malicious-source and compromised-authorised-builder cases remain.
40. Promote one exact artifact through three environments with distinct configuration. Demonstrate that no rebuild occurs and record the identity at every gate.
41. Test backward and forward compatibility across two artifact, configuration, message, and database versions. Express the supported compatibility interval.
42. Examine a Python wheel containing native code for platform and ABI constraints. Build or obtain per-platform artifacts and bind each to its own provenance.
43. Rebuild an old release after a dependency registry change. Compare preserving an old artifact with attempting to recreate it from source.
44. Design a reproducible-build verification performed by an independent builder. State which shared inputs could make both builds identically compromised.
45. Integrate Chapters 10, 12, 15, and 19 by tracing source through wheel metadata, CPython ABI, native dependencies, tests, signature, index, image, and runtime admission.

### 20.37.4 Containers and runtime isolation

46. Map a container launch into namespaces, cgroups, mounts, capabilities, seccomp, mandatory access control, user identity, and runtime process creation.
47. Run a process in a namespace without a cgroup limit and another with a limit but little namespace isolation. Compare view isolation with resource governance.
48. Inspect every layer of an image. Copy a synthetic secret, delete it later, recover it from history, then rotate and rebuild correctly.
49. Measure copy-up and ephemeral-storage behaviour when modifying a large file from a lower layer. Explain the performance and capacity result.
50. Build a multi-stage Python image from a verified wheel. Exclude compiler, package cache, source, test credentials, and unnecessary shell tools from runtime.
51. Construct an allowlisted build context and compare it with a broad context plus exclusions. Prove version-control and secret fixtures are absent.
52. Pin a base manifest digest, then design the process that detects, assesses, rebuilds, tests, and promotes updated bases without sacrificing repeatability.
53. Build multi-architecture images. Inspect the image index and platform manifests; execute architecture-specific tests and compare native dependency contents.
54. Run as a numeric non-root identity with every capability dropped. Add back one demonstrated capability and document its transitive authority.
55. Make the root filesystem read-only. Discover every implicit write and assign an explicit temporary, cache, or durable mount with quota and lifecycle.
56. Apply CPU quota and measure throttling, throughput, and tail latency. Apply memory limit and observe OOM termination, cgroup evidence, and restart semantics.
57. Bound process count, file descriptors, temporary storage, and output. Construct workloads that reach each bound without compromising the host.
58. Compare an ordinary container runtime, rootless mode, and a VM-backed sandbox for a hostile parser. Define the trusted computing base and residual escape impact.
59. Mount a synthetic host control socket into a container and map its effective authority without exploiting a real system. Remove it and design a narrow mediated API.
60. Integrate Chapter 19 by developing an isolation profile for untrusted document parsing with no general egress, one input, one output, strict resources, and disposable state.

### 20.37.5 Orchestration and workload controllers

61. Model a reconciliation loop with desired replicas, observed Pods, delayed events, and failed creation. Show why desired three does not imply exactly three at every instant.
62. Compare Deployment, StatefulSet, DaemonSet, Job, and CronJob for five workloads. Defend controller choice from identity, completion, placement, and restart semantics.
63. Design liveness, readiness, and startup probes for a slow-starting service with a temporarily unavailable database. Prevent both premature traffic and restart cascade.
64. Deliberately make readiness expensive and observe its resource effect. Replace it with bounded local evidence while retaining an independent end-to-end synthetic check.
65. Configure graceful termination: readiness withdrawal, endpoint propagation, connection draining, work completion, grace deadline, and forced termination. Measure every interval.
66. Calculate rolling-update maximum and minimum replica counts for several percentage and integer surge/unavailable settings. Test rounding and insufficient cluster capacity.
67. Spread replicas across hosts and zones. Remove one zone and prove the remaining placement and downstream services have capacity to meet the objective.
68. Create a disruption budget and demonstrate which voluntary events it constrains and which crashes, outages, and administrator actions it cannot prevent.
69. Design resource requests from measured working sets and CPU demand. Compare scheduler packing and eviction when requests are under- and over-stated.
70. Run a finite Job under worker crash and duplicate execution. Make the external effect idempotent and prove successful-completion counting matches business completion.
71. Run a CronJob across controller interruption, clock change, long execution, and missed schedule. Define concurrency, deadline, and duplicate semantics.
72. Rotate configuration and a mounted secret. Observe object update, projected path, open descriptor, application cache, session, and server-side revocation separately.
73. Write network policy for API, worker, storage gateway, policy service, and monitoring. Test representative allowed and forbidden flows from real workload identities.
74. Simulate control-plane unavailability while existing workloads continue. State which data-plane behaviour, scaling, secret renewal, and recovery operations remain possible.
75. Integrate Chapters 13 and 14 by treating scheduler placement as a constrained optimisation problem and identifying where heuristics, stale state, and concurrency defeat an ideal solution.

### 20.37.6 CI, delivery, and state evolution

76. Draw a CI trust graph including source, workflow, actions, runner, dependency sources, caches, artifacts, credentials, signing, registry, and deployment admission.
77. Execute an untrusted synthetic pull request on an isolated ephemeral runner. Prove it cannot obtain publication token, cloud metadata, internal network, or protected cache write.
78. Replace a long-lived CI credential with federated workload identity bound to repository, protected reference, workflow, audience, environment, and short session.
79. Pin every external workflow component by immutable identity. Build an update process that reviews new bytes and preserves rollback.
80. Poison an intentionally broad dependency cache from an untrusted branch, then repair writer policy, key scope, and independent artifact verification.
81. Test the built wheel and image in clean environments rather than the source tree. Introduce an omitted package-data file and verify artifact tests catch it.
82. Seed a flaky test with a known failure probability. Calculate false-acceptance probability under retries and replace randomness with controlled deterministic evidence.
83. Separate validation, build, attestation, publication, and deployment jobs. Minimise each identity and bind every handoff to an artifact digest.
84. Design rolling, blue–green, and canary strategies for one service. Include traffic, background workers, scheduled jobs, database, queues, caches, and external contracts.
85. Specify a canary experiment with randomisation, practical effect threshold, confidence, minimum sample, observation duration, guardrails, and stop condition.
86. Show a biased instance canary caused by zone, cache warmth, tenant mix, or connection affinity. Redesign assignment and interpret residual uncertainty.
87. Design an expand–migrate–contract database change across at least three releases. Test every supported old/new process and schema combination.
88. Implement a restartable rate-limited backfill with checkpoint, idempotency, progress, validation, and pause. Run it during representative foreground load.
89. Evolve a queue message envelope without poisoning old consumers. Exercise unknown version, dead letter, redelivery, and producer rollback.
90. Create a feature flag with owner, targeting, audit, expiry, and cleanup. Demonstrate that disabling it does not reverse state already written.

### 20.37.7 Rollback, infrastructure as code, and drift

91. Classify a deployment's changes as reversible, compensatable, or irreversible across code, schema, data, messages, cache, external effects, identity, and policy.
92. Test rollback after the new version has written representative state and emitted messages. Do not accept a test performed before any new behaviour occurs.
93. Write a decision table choosing rollback, roll-forward, flag disablement, isolation, capacity increase, or traffic shedding under distinct incident conditions.
94. Construct a small IaC dependency graph with implicit and explicit edges. Remove an edge and observe unsafe concurrency; add unnecessary edges and observe serialization.
95. Force a partial IaC apply. Refresh observations, inspect state, and converge without assuming that failed apply means zero remote mutations.
96. Protect remote state with encryption, versioning, locking, restricted identity, backup, audit, and independent recovery. Demonstrate why “sensitive” display marking is insufficient.
97. Partition state by lifecycle and authority. Publish narrow outputs without granting consumers full state-read access.
98. Pin and upgrade one provider. Review schema, default, plan, import, diff, and replacement changes in an isolated environment.
99. Build policy that rejects public storage, wildcard IAM, unknown security scope, unapproved region, unencrypted state, and deletion of a protected database.
100. Bind approval to a saved machine-readable plan digest. Change remote state before apply and ensure version or plan guards prevent silent execution.
101. Import a pre-existing resource. Reach a reviewed no-change baseline, test deletion protection, and document which attributes the provider cannot observe.
102. Move a logical resource address without replacing the remote object. Verify identity before and after and recover from an intentionally wrong move.
103. Detect declared, remote, semantic, and inventory drift. Include resources absent from IaC state and provider behaviour changes producing no textual diff.
104. Perform an emergency manual containment with owner, reason, before/after evidence, expiry, and reconciliation. Prevent the ordinary controller from immediately undoing it.
105. Integrate Chapter 12 by testing an IaC module's validation, plan, apply, upgrade, import, partial failure, and destroy semantics under CI.

### 20.37.8 Cloud APIs, IAM, networks, and secrets

106. Use a cloud SDK against an authorised sandbox or emulator. Script success, transient failure, permanent failure, throttling, timeout after commit, stale read, and conflict.
107. Implement a create operation using provider idempotency token or create-if-absent precondition. Lose the response after commit and reconcile without duplication.
108. Consume a changing paginated collection. Deduplicate stable identities, bound pages, and demonstrate miss or repetition when snapshot semantics are absent.
109. Protect an update with entity tag or generation. Cause a concurrent modification and merge at policy level instead of overwriting it.
110. Audit SDK region, endpoint, credential chain, retry, timeout, proxy, and connection-pool defaults. Replace every security-critical ambient default explicitly.
111. Build an IAM authority graph for humans, CI, API, worker, backup, observability, and incident roles, including pass-role and code-deployment escalation edges.
112. Replace static application keys with federated workload identity. Validate issuer, audience, subject, expiry, refresh, clock skew, and failure behaviour.
113. Create an object-level policy for two tenants. Test direct, list, export, cache, backup, support, and administrative paths for cross-tenant denial.
114. Design and exercise break-glass access independent of the primary identity provider. Add phishing-resistant authentication, notification, short duration, audit, and review.
115. Allocate non-overlapping CIDR ranges for several environments and a future merger. Explain routing ambiguity and migration when ranges overlap.
116. Trace one request through DNS, route, firewall, NAT, load balancer, TLS, application authentication, authorisation, and response. Identify every stateful device.
117. Write and test egress policy for exact dependencies. Consider DNS aliases, shared hosting, direct IP, metadata endpoints, package downloads, and incident access.
118. Inventory a secret from generation through store, delivery, memory, log, crash dump, backup, rotation, session invalidation, revocation, and destruction.
119. Rotate a database credential with bounded overlap and verified adoption. Terminate old sessions and alert on residual old-version use.
120. Commit a synthetic credential to a test repository. Detect it, revoke first, remove history and artifacts, inspect audit, and document why masking alone failed.

### 20.37.9 Discovery, load balancing, and observability

121. Change a DNS endpoint and measure authoritative TTL, recursive cache, process resolver, connection-pool, and client cutover. Include negative caching.
122. Implement client-side discovery and compare it with proxy-side discovery under endpoint churn, control-plane outage, empty set, and stale last-known-good state.
123. Authenticate logical service identity independently of discovered address. Demonstrate failure when a valid certificate is accepted for the wrong name or audience.
124. Compare round robin, weighted, least-outstanding, power-of-two, and consistent-hash balancing under variable request cost, hot keys, and persistent multiplexed connections.
125. Drain one backend with short requests, streams, and long-lived connections. Measure detection, propagation, connection closure, reconnect storm, and completion.
126. Compose client, proxy, and SDK retries, calculate maximum amplification, and redesign with one owner, propagated deadline, and retry budget.
127. Define a structured event schema for a domain operation. Include event time, receive time, outcome, artifact/configuration identity, correlation, privacy, and version.
128. Emit a counter, gauge, and histogram for appropriate phenomena. Prove counter reset handling and select histogram buckets around SLO thresholds.
129. Calculate metric series growth from four labels. Replace raw URL, user, and error-message labels with bounded semantic dimensions.
130. Propagate W3C trace context across three services while treating incoming context as untrusted. Restrict baggage and show trace ID never authorises access.
131. Compare head and tail sampling on rare errors and high latency. Preserve sampling probability and keep audit or billing events outside probabilistic tracing.
132. Break the telemetry exporter through delay and outage. Verify bounded buffering, drop policy, application independence, and telemetry-pipeline self-observation.
133. Use profiles to identify a CPU or allocation hotspot while metrics show saturation and traces show affected paths. State what each signal cannot prove.
134. Build a dashboard starting from user journeys rather than infrastructure components. Add deployment and configuration annotations and drill-down evidence.
135. Integrate Chapter 11 by defining retention, access, redaction, export, integrity, and deletion policy for logs, metrics, traces, and profiles.

### 20.37.10 SLOs, latency, and capacity

136. Write an executable SLI specification including journey, source, measurement point, eligibility, good rule, window, late/duplicate/missing treatment, and data quality.
137. Compare server-side, client-side, and synthetic availability for the same outage. Explain which failures each source misses.
138. Compute an event-based and a time-based SLO over bursty traffic. Show why the two weight user harm differently.
139. Derive error budget and burn rate for 99%, 99.9%, and 99.99% objectives. Design short/long-window page and ticket alerts.
140. Segment the SLI by region and tenant class without unbounded labels. Find an aggregate that passes while one important population fails.
141. Measure end-to-end latency and separate pool wait, DNS, connect, TLS, queue, server, dependency, response, and client phases.
142. Demonstrate coordinated omission with closed-loop and open-loop load generation. Record timeouts as failures rather than disappearing observations.
143. Build compatible histograms across replicas and compute fleet quantiles. Demonstrate mathematically and empirically why averaging per-instance p99 fails.
144. Simulate a 20-way fan-out with independent and correlated latency. Compare observed maximum with the (F(t)^{20}) model.
145. Apply Little's Law to a stable measured queue, then overload it and explain why no finite steady-state delay follows.
146. Fit the explanatory M/M/1 mean at several arrival rates and compare with a non-exponential multi-worker simulation. Identify violated assumptions.
147. Design a load test hypothesis with representative data, arrival process, cache, dependencies, limits, ramp, steady duration, stop condition, and SLO.
148. Find successive bottlenecks by relieving CPU, then database connections, then a lock or network constraint. Record how the capacity curve changes.
149. Calculate capacity required to survive one zone loss plus deployment surge and autoscaling delay. Make the reliability headroom visible as an explicit cost.
150. Implement bounded admission and backpressure by tenant and priority. Prove overload causes early rejection rather than unbounded queue growth.

### 20.37.11 Autoscaling, resilience, and recovery

151. Simulate a proportional autoscaler with metric delay, startup delay, cooldown, and bursty demand. Find oscillation and tune stabilisation without hiding overload.
152. Compare CPU, concurrency, queue depth, queue age, and predictive signals for CPU-bound, I/O-bound, and long-running work.
153. Coordinate horizontal, vertical, and cluster scaling. Construct a case where one controller's change makes another oscillate.
154. Scale queue workers down during jobs. Implement lease, checkpoint, drain, and termination semantics that avoid loss and uncontrolled duplication.
155. Propagate one end-to-end deadline through three dependencies. Allocate phase budgets and cancel work after the result is no longer useful.
156. Implement retry with full jitter, total deadline, semantic classification, idempotency key, and shared retry budget. Simulate overload and ambiguous success.
157. Test a circuit breaker under transient errors, persistent errors, slow calls, tiny samples, recovery, and half-open probe concurrency.
158. Partition bulkheads by dependency and tenant, allow bounded reserve borrowing, and measure preserved critical capacity during one slow workload.
159. Design safe graceful degradation for a catalogue, payment system, and medical-result service. State which correctness and security properties may never relax.
160. Hedge selected idempotent reads after a delay. Measure tail benefit, duplicate load, cancellation, and behaviour under a shared bottleneck.
161. Define RPO and RTO for database, object store, queue, identity, configuration, and audit evidence. Identify dependency cycles in recovery.
162. Perform a clean-room restoration from base backup plus logs. Recover keys, infrastructure, artifacts, identity, schema, and domain invariants; measure actual RPO/RTO.
163. Corrupt data before the latest immutable backup and show why immutability alone does not supply a clean recovery point.
164. Fail over to a recovery site, accept new writes, and design failback without split brain, duplicate effects, or loss of recovery-site changes.
165. Integrate Chapters 14 and 19 by testing resilience against concurrency races, resource exhaustion, credential compromise, parser failure, and partial network partition.

### 20.37.12 Cost, change, incidents, and operational assurance

166. Build a cost model per successful user outcome including fixed, variable, stepwise, network, telemetry, licences, failure waste, and operator labour.
167. Allocate shared costs through two different rules and analyse the incentives each creates. Reconcile the allocation total to the provider bill.
168. Design budget and anomaly response for experimental and critical environments. Ensure cost control cannot silently delete durable state or disable security evidence.
169. Measure the five current DORA delivery metrics for one service under explicit definitions. Identify gaming paths and pair them with user and quality outcomes.
170. Risk-assess ten changes by blast radius, reversibility, observability, novelty, state, dependency, and consequence rather than line count.
171. Run a timed incident exercise with commander, operations, communications, scribe, decision log, hypotheses, mitigations, handover, and user-relevant recovery gates.
172. Write a post-incident review with timeline, impact, contributing conditions, successful controls, detection/recovery analysis, and verified systemic actions.
173. Convert a recurring manual runbook into safe automation with immutable plan, exact targets, preconditions, bounded concurrency, audit, pause, and recovery.
174. Conduct a chaos experiment and a wider game day for the same failure. Compare technical evidence with organisational, access, communication, and handover findings.

### 20.37.13 Final integrated branch capstone

175. Take a packaged Python service from the trunk and operate it as a defensible production system in an authorised isolated environment. Define its socio-technical boundary, users, data and control planes, service/process/configuration contracts, SLI/SLO/error budget, failure model, RPO/RTO, cost unit, and ownership. Produce one immutable signed artifact with lock, SBOM, provenance, reproducibility assessment, compatibility interval, and retained rollback digest; construct least-privilege multi-platform containers with explicit namespace, cgroup, filesystem, capability, system-call, identity, network, lifecycle, and resource policy; deploy through modular tested IaC whose encrypted locked state, plan approval, imports, unknowns, partial failure, deletion protection, and drift process are evidenced; use short-lived federated identities, bounded IAM, managed secret lifecycle, authenticated discovery, segmented ingress/egress, and exact artifact admission; build an isolated CI trust graph and progressive delivery state machine with canary inference, expand–migrate–contract state evolution, idempotent messages, and tested rollback/roll-forward criteria; instrument bounded logs, metrics, traces, profiles, deployment annotations, burn alerts, latency histograms, capacity curves, backpressure, autoscaling, retry budgets, circuit breakers, bulkheads, and safe degradation; restore a representative encrypted backup with keys and infrastructure into a clean environment and execute failover/failback; calculate cost per successful outcome and enforce graduated budgets; then conduct a compound incident involving a bad release, dependency slowdown, credential revocation, queue growth, and one failed zone. Deliver an evidence graph mapping every source revision, artifact digest, configuration and policy version, infrastructure plan, identity, deployment event, data migration, observation, decision, recovery result, cost, residual risk, and unresolved assumption. Defend whether the service should remain released.
