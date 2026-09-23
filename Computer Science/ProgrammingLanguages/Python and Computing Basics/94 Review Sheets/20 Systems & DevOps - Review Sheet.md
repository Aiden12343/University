# 20.36 Common misconceptions consolidated

1. **“DevOps means developers operate everything.”** It concerns shared delivery and operational feedback, not abandonment of role boundaries or least privilege.
2. **“A daemon should fork and manage itself.”** Modern service managers often supervise foreground processes directly.
3. **“Restarting fixes failures.”** It can recover transient process state and can amplify persistent configuration or dependency defects.
4. **“Environment variables are typed configuration.”** They are strings requiring parsing, validation, precedence, and secrecy decisions.
5. **“Atomic rename guarantees durable data.”** Atomic visibility and crash persistence are different filesystem properties.
6. **“Rebuilding the same version yields the same artifact.”** Inputs, tools, timestamps, networks, and ordering can change bytes.
7. **“A container is a lightweight virtual machine.”** It is isolated process execution ordinarily sharing the host kernel.
8. **“Containers make applications secure.”** Runtime privilege, kernel, image provenance, mounts, network, and application flaws remain.
9. **“Orchestrators guarantee exactly the desired replica count.”** Reconciliation passes through transient and failed states.
10. **“A liveness check should test every dependency.”** Dependency outages can trigger destructive restart storms.
11. **“CI is trusted because it belongs to the repository.”** Proposed code executes in CI and can attack credentials and runners.
12. **“Continuous deployment means releasing without controls.”** Automated release can have stronger preconditions, progressive exposure, and rollback than manual release.
13. **“Rollback always restores the old system.”** Schemas, messages, and external side effects may be incompatible or irreversible.
14. **“Infrastructure as code prevents manual drift.”** It makes desired state reviewable; remote and emergency changes still occur.
15. **“Cloud SDK calls are local method calls.”** They cross fallible remote APIs with ambiguous completion and rate limits.
16. **“Private network traffic is trusted.”** Routing location is not identity, authorisation, or confidentiality.
17. **“Average latency describes service speed.”** Tail distributions and user journeys determine experienced delay.
18. **“Autoscaling removes capacity planning.”** Scaling has delay, quotas, downstream bottlenecks, and cost.
19. **“Replication is a backup.”** It reproduces deletion and corruption; recovery copies need isolation and restoration tests.
20. **“A successful backup job proves recoverability.”** Only a validated restore exercises data, keys, schema, and procedure.
21. **“More telemetry always improves observability.”** Unbounded labels and events create cost, overload, and privacy risk.
22. **“An incident has one root cause.”** Complex failures arise through interacting conditions and failed safeguards.
23. **“Production means the public cloud.”** Production is any environment whose outcomes discharge real obligations; size and hosting model are irrelevant.
24. **“Control planes are outside the service.”** Their identity, availability, policy, and recovery determine whether the service can be operated safely.
25. **“SIGTERM guarantees cleanup.”** It is a notification that can be delayed, ignored, mishandled, or followed by forced termination.
26. **“PID 1 behaves like any process.”** Namespace init has child-reaping and signal-lifecycle responsibilities ordinary application processes may not satisfy.
27. **“Watchdog heartbeat proves useful progress.”** A separate heartbeat can remain alive while the guarded event loop, queue, or state transition is stuck.
28. **“Unknown configuration keys should be ignored for compatibility.”** In production they commonly represent misspellings or unsupported intent and should fail under an explicit schema policy.
29. **“A writable application directory is convenient state storage.”** It confuses artifact and state lifecycles, impedes immutable replacement, and weakens permissions and backup policy.
30. **“Reproducible bytes prove a clean build.”** They prove repeatability under declared conditions, not the honesty of source, compiler, dependency, or builder.
31. **“Image tags identify deployments.”** Mutable tags are references; record the platform-specific manifest or artifact digest selected at deployment.
32. **“A read-only root filesystem makes a container stateless.”** Writable volumes, remote databases, queues, caches, external effects, and kernel state remain.
33. **“Resource requests cap consumption.”** They commonly guide scheduling; limits and other kernel or platform controls govern caps.
34. **“A disruption budget prevents outages.”** It constrains selected voluntary disruptions and cannot prevent correlated failure or create replacement capacity.
35. **“A pipeline is a sequence of commands.”** It is a trust and dataflow graph whose caches, runners, artifacts, identities, and approval subjects affect correctness.
36. **“A flaky test is safe if it eventually passes.”** Repetition raises false-acceptance probability and removes evidence for the property the test claimed.
37. **“Feature flags make release reversible.”** State written under enabled behaviour and external effects can remain after the flag is disabled.
38. **“State marked sensitive is absent from IaC state.”** The designation often suppresses display while the value remains stored and accessible to state readers.
39. **“Idempotency means exactly once.”** It makes repeated logical requests converge under a stated scope; attempts and secondary effects can still occur many times.
40. **“An empty drift report proves ownership is complete.”** Unmanaged or orphaned resources can lie outside the tool's state and therefore outside its comparison.
41. **“Eventually consistent means data will soon be correct.”** It describes convergence assumptions under continuing conditions, not an application deadline or semantic correctness.
42. **“Explicit deny always wins everywhere.”** IAM composition rules are provider- and policy-type-specific and must be read for the exact evaluation system.
43. **“Mutual TLS authorises requests.”** It authenticates certificate-bound peers under policy; application action and resource authorisation remain separate.
44. **“Secrets in mounted files rotate automatically.”** The mount, pathname, open descriptor, process cache, session, and server acceptance lifecycle can all differ.
45. **“Service discovery returns healthy endpoints.”** It returns endpoints under delayed and scoped observations; the client still needs health, deadline, and identity policy.
46. **“A layer-7 proxy understands business semantics.”** Parsing the protocol does not reveal which retries, fallbacks, tenants, or stale results are safe.
47. **“Trace identifiers are authenticated identity.”** Incoming trace context is correlation metadata and can be attacker-controlled unless separately protected.
48. **“SLOs describe infrastructure uptime.”** Good indicators describe user-relevant service behaviour under an explicit eligible population and measurement point.
49. **“A high p99 proves only rare slowness.”** Multi-request journeys and frequent users encounter tail events far more often than one isolated operation suggests.
50. **“Game days are demonstrations of preparedness.”** They are experiments intended to expose gaps; a scripted success with hidden assistance supplies weak evidence.
