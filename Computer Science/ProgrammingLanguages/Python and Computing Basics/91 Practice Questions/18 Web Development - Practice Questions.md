# 18.36 Exercises

### 18.36.1 Protocol foundations

1. Trace a browser navigation from a typed HTTPS URL through parsing, DNS, transport, TLS, HTTP, server routing, database query, response, and rendering. State the contract and failure modes at each layer.
2. Implement a length-prefixed message reader over a socket. Handle partial headers, partial bodies, end-of-stream, maximum size, and multiple messages in one receive buffer.
3. Parse twenty URLs into components. Include IPv6 literals, percent-encoding, non-default ports, queries, empty paths, and fragments. Identify which components the HTTP server receives.
4. Given ten methods and failure scenarios, decide whether automated retry is valid. Include an idempotency-key design for one POST operation.
5. Design caching policy for a public immutable asset, private account page, and frequently changing catalogue. Specify cache keys and validators.

### 18.36.2 Application and database

6. Implement a Flask resource with GET, POST, conditional PUT, and DELETE. Define schemas, statuses, error representation, limits, and idempotency.
7. Implement the same domain in Django. Compare what the integrated framework supplies and what remains an application obligation.
8. Design a relational schema with primary, foreign, unique, check, and not-null constraints. For ten queries, propose indexes and verify plans using the selected DBMS.
9. Reproduce an N+1 query problem, measure query count, and repair it with appropriate related-object loading.
10. Construct lost-update and write-skew schedules using two transactions. Determine which isolation or locking rule prevents each.
11. Plan an expand–migrate–contract change for splitting one required name field into structured components while old and new application versions coexist.

### 18.36.3 Security and concurrency

12. Threat-model registration, login, password reset, and session termination. Identify assets, trust boundaries, abuse cases, controls, and residual risk.
13. Demonstrate SQL injection in a disposable local test and repair it using parameters. Do not expose the test beyond an isolated environment.
14. Create XSS test cases for HTML text, attribute, URL, and JavaScript contexts. Use a template engine’s supported encoders and a sanitizer where rich text is required.
15. Build a CSRF-protected form and explain every token/cookie/origin property.
16. Design an outbound URL-fetching service resistant to SSRF. Include redirect, DNS, address-range, scheme, port, response-size, and timeout rules.
17. Implement a bounded background job with an idempotency key and transactional outbox. Simulate worker failure immediately before and after acknowledgement.
18. Compare threaded WSGI and asynchronous ASGI implementations of an I/O-bound endpoint. Measure with fixed resources and explain the saturation point.

### 18.36.4 Initial synthesis

19. Build and document a deployable service with versioned HTTP API, relational database, migrations, authenticated sessions or scoped tokens, object-level authorisation, validated schemas, parameterised queries, background work, structured errors, unit/integration/contract/security tests, proxy-aware deployment, bounded concurrency, health checks, logs, metrics, traces, rollback, and a written threat model. Demonstrate at least three injected failures and show that ambiguity, retries, and duplicate work are handled according to the documented contract.

### 18.36.5 Networks, DNS, transport, and TLS

20. Draw the encapsulation of a 2,000-byte HTTP request through TLS, TCP, IP, and Ethernet under a stated MTU. Distinguish application length from segments, packets, and frames.
21. Measure DNS resolution, TCP connection, TLS handshake, time to first byte, and full transfer separately for a controlled service. Explain connection reuse and measurement error.
22. Use <code>getaddrinfo</code> on loopback, IPv4, IPv6, and a multi-address test domain. Implement bounded candidate fallback without assuming answer order.
23. Bind test servers to loopback, one interface, and wildcard addresses. From another namespace or host, verify which are reachable and explain the security consequence.
24. Create a table of IPv4 and IPv6 loopback, private, link-local, multicast, unspecified, documentation, and global ranges. Test Python’s <code>ipaddress</code> classification.
25. Configure a local DNS zone containing A, AAAA, CNAME, TXT, MX, NS, SOA, and CAA records. Trace recursive resolution and cache expiry.
26. Simulate a DNS migration with old and new addresses, differing TTLs, persistent connection pools, and one stale resolver. Write the coexistence runbook.
27. Implement a buffered delimiter decoder retaining trailing bytes. Feed every possible split of three concatenated messages and prove no byte is lost.
28. Implement the length-prefixed decoder from scratch with maximum body, incomplete EOF, zero-length policy, and property tests over arbitrary chunk boundaries.
29. With a socket pair, demonstrate that one <code>sendall</code> need not correspond to one <code>recv</code>. Repeat under small buffers and delayed reads.
30. Define client-visible outcomes for EOF, reset, connect timeout, read timeout, cancellation, and malformed frame. State which are safe to retry.
31. Calculate average concurrency using Little’s Law for five workloads. Then explain why burstiness and p99 latency require more than the mean.
32. Benchmark short-lived versus reused HTTP connections on a local service. Separate handshake, slow-start, pool lookup, and stale-connection failures.
33. Inspect a TLS certificate chain using a standard client. Identify subject alternative names, issuer, validity, key use, signature algorithm, and trust anchor.
34. Create a private test CA and issue server and client certificates. Configure mutual TLS locally and map certificate identity to a deny-by-default policy.
35. Trigger certificate failures for wrong host, expired certificate, unknown issuer, and invalid clock. Record the distinct diagnostic and never disable verification.
36. Place TLS termination before a test application. Configure trusted forwarding fields, then demonstrate how an untrusted direct connection could spoof them without filtering.
37. Compare HTTP/1.1, HTTP/2, and HTTP/3 framing, multiplexing, connection establishment, loss behaviour, and deployment prerequisites in a protocol matrix.
38. Model a connection pool with maximum size, idle timeout, maximum lifetime, wait deadline, and health failure. Test exhaustion and stale entries.
39. Threat-model metadata visible despite TLS: addresses, timing, sizes, terminating proxies, logs, SNI-related information, and application endpoints.
40. Write a network-failure report that identifies the first violated layer contract rather than saying merely “the API is down.”

### 18.36.6 URLs, HTTP, caching, sessions, and browsers

41. Parse URLs containing user information, IPv6 literals, Unicode domains, default and explicit ports, encoded separators, dot segments, empty queries, and fragments.
42. Implement exact-origin comparison from parsed scheme, canonical host, and effective port. Test deceptive suffixes and visually confusable names.
43. Resolve twenty relative references against one base URL by hand, then verify with <code>urllib.parse.urljoin</code>. Explain every disagreement with intuition.
44. Design an outbound callback allowlist. Specify scheme, host, port, DNS/address, redirects, TLS identity, method, credentials, size, and timeout policy.
45. Capture an HTTP/1.1 request and identify start line, each field, framing, and body bytes. Explain how conflicting length interpretations enable request smuggling.
46. Create requests exceeding each proxy and application limit: target length, field count, field bytes, body bytes, nesting, and decompressed size. Verify consistent rejection.
47. Configure a trusted reverse proxy chain and test original scheme, host, and client address. Inject forged forwarding fields from an untrusted peer.
48. Classify twenty operations by safety, idempotency, and cacheability independently. Defend ambiguous PATCH and POST cases from their documented semantics.
49. Implement an idempotency-key store scoped to principal and operation. Test same request replay, conflicting payload reuse, concurrent first requests, expiry, and response loss.
50. Implement optimistic PUT with ETag and <code>If-Match</code>. Race two clients and prove one stale update returns 412 without overwriting.
51. Design one API error media type. Include stable code, safe detail, field violations, correlation identifier, documentation, and retry guidance.
52. Map malformed framing, unsupported media type, malformed JSON, invalid field, failed authentication, forbidden object, conflict, precondition, rate limit, and outage to statuses.
53. Compare 301, 302, 303, 307, and 308 for a POST. Test a client and document method/body preservation rather than relying on reason phrases.
54. Implement media negotiation with a maintained parser supporting weights, wildcards, specificity, and parameters. Add correct <code>Vary</code> behaviour.
55. Define JSON encodings for decimal money, timestamps, binary digests, sets, large integers, and enumerations. State round-trip and cross-language constraints.
56. Stream a large result as newline-delimited JSON with bounded records and cancellation. Compare memory, time to first record, and partial-failure semantics with one array.
57. Configure cache policy for immutable assets, a public catalogue, a personalised dashboard, an authentication response, and an error response.
58. Implement strong and weak ETags and conditional GET. Test 304 fields, representation encoding variants, and byte-range suitability.
59. Reproduce a cache key omission that crosses language or user boundaries in an isolated test. Repair the key and add a regression test.
60. Simulate a cache stampede on one expensive key. Compare no protection, request coalescing, early refresh, and bounded stale serving.
61. Inspect browser cookie selection with host-only/domain, path, Secure, HttpOnly, SameSite, expiry, and duplicate names. Explain the sent header.
62. Implement session creation, rotation after login, idle and absolute expiry, logout revocation, and concurrent-session listing using opaque random identifiers.
63. Compare server-side sessions, signed client sessions, opaque access tokens, and self-contained tokens by revocation, size, disclosure, scaling, and failure mode.
64. Build an accessible form using native labels, errors, keyboard operation, focus management, and server validation. Test without CSS and without JavaScript.
65. Build a progressively enhanced interaction: ordinary link/form behaviour first, then JavaScript augmentation. Verify navigation, history, failure, and accessibility.

### 18.36.7 WSGI, ASGI, Flask, and Django

66. Write a WSGI application that reads a bounded request body, returns byte-accurate length, streams three chunks, and closes a resource if the client stops.
67. Write WSGI middleware for correlation identifiers. Test inbound validation, existing response fields, exceptions, iterable closure, and concurrent requests.
68. Create a minimal WSGI test harness invoking the callable with a constructed environment and capturing <code>start_response</code>. State what it does not emulate.
69. Write an ASGI application that consumes all request-body events, handles disconnect, and returns chunks with correct <code>more_body</code> transitions.
70. Write ASGI middleware storing state per scope rather than on the middleware instance. Drive two interleaved requests to expose an unsafe implementation.
71. Implement lifespan startup and shutdown for a bounded connection-pool fake. Test failed startup, repeated shutdown, and process-local ownership.
72. Compare one blocking call inside an event loop with thread offload and a native asynchronous fake. Measure loop delay under fixed concurrency.
73. Implement server-sent events with identifiers, retry hints, heartbeat, reconnection, and bounded retained history. Define behaviour when history has expired.
74. Implement a local WebSocket protocol with authenticated subscription, schema version, size/rate limits, heartbeat, slow-consumer policy, and graceful server shutdown.
75. Map the Flask request lifecycle by instrumentation: context push, URL matching, hooks, view, error handler, response processing, session save, and teardown.
76. Refactor a large Flask route into transport parsing, domain service, repository, and response mapping. Demonstrate that domain tests need no Flask context.
77. Create two Flask application instances with different test configuration from one factory. Prove extensions and request state do not leak between them.
78. Organise routes into blueprints with explicit dependencies and error handlers. Test registration under two URL prefixes without hidden global state.
79. Render a Jinja template containing hostile text in HTML, attribute, URL, and script-adjacent positions. Identify which patterns are safe and prohibited.
80. Build a Django project with one bounded app, URL configuration, form, model, migration, admin registration, and object-level permission checks.
81. Instrument Django middleware order. Move session, authentication, transaction, and security middleware deliberately and explain observed failures.
82. Add database constraints matching Django model validation. Bypass model forms through a bulk operation and prove the constraints remain authoritative.
83. Reproduce Django’s N+1 query behaviour, then compare <code>select_related</code>, <code>prefetch_related</code>, and an accidental Cartesian expansion.
84. Create synchronous and asynchronous Django views over the same slow dependency. Identify any sync adaptation and measure actual concurrency.
85. Run each framework behind a production server and proxy locally. Test forwarded fields, body limits, worker restart, graceful drain, and static asset policy.

### 18.36.8 Relational data, transactions, ORMs, and migrations

86. Model clinics, patients, slots, reservations, and notifications. Identify candidate, primary, surrogate, foreign, and alternate keys.
87. Begin with one denormalised reservation table. Demonstrate insertion, update, and deletion anomalies, then normalise and state the dependencies removed.
88. Write constraints for status domain, positive capacity, unique active reservation, temporal order, and referential actions. Identify any invariant requiring multiple rows.
89. Create rows containing NULL and evaluate equality, inequality, <code>IN</code>, <code>NOT IN</code>, aggregation, ordering, and unique constraints under the chosen DBMS.
90. Design composite, partial, covering, and expression indexes for a declared query workload. Measure writes, storage, and plans before and after.
91. Generate skewed representative data and compare planner estimates with actual rows. Update statistics and explain any changed join strategy.
92. Write a parameterised search with optional filters. Ensure values remain parameters and sort/column choices come from fixed allowlisted fragments.
93. Demonstrate SQL injection only in an isolated disposable database, then repair it with driver parameters and a least-privileged account.
94. Create two concurrent sessions reproducing dirty read where supported, non-repeatable read, phantom, lost update, and write skew. Record isolation-specific outcomes.
95. Protect a lost update with a version column and conditional update. Protect a write-skew invariant with serialisable isolation or appropriate locking.
96. Cause a deadlock by acquiring two rows in opposite order. Capture the database error, roll back fully, retry with bounds, and impose consistent ordering.
97. Hold a transaction open during a simulated remote call and measure lock impact. Redesign so external work occurs outside the critical transaction.
98. Implement the reservation creation transaction from Section 18.34 with database uniqueness and idempotency. Race twenty clients for one slot.
99. Build a transactional outbox and relay. Terminate the relay before publish, after publish, and before mark; prove consumer deduplication.
100. Compare pessimistic row locking and optimistic version checks under low and high contention. Report latency, aborts, fairness, and throughput.
101. Use savepoints for partial recovery inside a transaction. Explain why the outer rollback still removes all enclosed effects.
102. Reproduce an ORM lazy-load after its session is closed. Define an explicit loading boundary that prevents hidden I/O in serialisation.
103. Compare object-by-object insertion, bulk insertion, and database-native loading. Identify hooks, validation, generated keys, and audit behaviour bypassed.
104. Construct one giant join over several one-to-many relations and measure row multiplication. Repair with selective joins and batched prefetch.
105. Inspect generated SQL and query plans for ten ORM expressions. Find one expression whose innocent Python appearance causes expensive SQL.
106. Implement deterministic keyset pagination with duplicate timestamps. Test insertions, deletions, filter changes, cursor tampering, and tenant mismatch.
107. Write an expand–migrate–contract plan for renaming and splitting a populated column while three application versions coexist.
108. Execute a restartable bounded backfill keyed by primary key. Interrupt it repeatedly, run workers concurrently, and verify completeness without duplication.
109. Create a large index and constraint through the DBMS’s online facilities. Record locks, I/O, replication lag, abort thresholds, and validation.
110. Restore a pre-migration backup into an isolated environment and replay migrations from zero. Verify historical migration code does not import current models.

### 18.36.9 APIs and web security

111. Derive a resource-oriented API from a command-oriented domain. Identify where subordinate resources clarify actions and where a documented POST is better.
112. Specify filtering, ordering, field selection, expansion, page limits, count policy, cursor lifetime, and mutation semantics for one collection.
113. Produce an OpenAPI document for five endpoints, then write conformance tests that find one implementation/schema disagreement.
114. Design an API deprecation process using consumer inventory, telemetry, documentation, warnings, compatibility tests, and an enforced retirement date.
115. Build a GraphQL schema with nullable and non-null fields. Trigger a resolver failure and trace null propagation and partial errors.
116. Reproduce GraphQL N+1 queries and implement a request-scoped batch loader preserving key order and missing values.
117. Define GraphQL cost accounting for aliases, fragments, nested lists, pagination bounds, and expensive fields. Test rejection before execution.
118. Apply object- and field-level authorisation to GraphQL. Prove schema visibility does not grant record or sensitive-field access.
119. Implement webhook signing over timestamp and raw body. Test replay window, rotated secrets, body transformation, duplicate delivery, and conflicting identity.
120. Build webhook ingestion that durably records before acknowledging, processes asynchronously, and supports safe manual redelivery with one event identity.
121. Configure password hashing with a maintained library. Inspect encoded parameters, verify salts differ, and upgrade an old verifier on successful login.
122. Threat-model registration, login, MFA enrolment, password reset, recovery, credential change, logout, and session review as one authentication lifecycle.
123. Implement WebAuthn or a faithful local demonstrator. Explain origin binding, challenge, credential key, signature counter limitations, and recovery.
124. Trace an OAuth authorisation-code flow with PKCE. Validate state, redirect URI, issuer, audience, nonce where applicable, token purpose, and scope.
125. Construct tokens with wrong issuer, audience, algorithm, key, expiry, not-before, and purpose. Verify every one is rejected.
126. Express one policy through RBAC, ABAC, and relationship rules. Compare revocation, explanation, caching, and object-query integration.
127. Build an authorisation matrix across anonymous user, owner, tenant member, staff, administrator, and suspended principal for every operation.
128. Create stored, reflected, and DOM XSS cases in an isolated test application. Repair them with context encoding, safe DOM APIs, and sanitisation.
129. Deploy a nonce-based Content Security Policy in report-only mode, remove unsafe inline dependencies, then enforce and inspect violation noise.
130. Implement CSRF tokens and origin checks for cookie-authenticated forms. Test cross-site form submission, login CSRF, SameSite variants, and token rotation.
131. Configure credentialed CORS for an exact origin allowlist. Test preflight, simple requests, <code>null</code> origin, caching, and malicious origin reflection.
132. Build an SSRF-resistant fetch service using a fixed scheme, exact hosts, bound resolution, redirect revalidation, egress filtering, and byte/deadline limits.
133. Test SSRF controls against IPv4, IPv6, mapped addresses, link-local metadata, DNS change, redirects, user information, encoded hosts, and alternate ports.
134. Build file upload handling with generated names, streaming limits, archive-path rejection, format parser, image dimensions, isolated processing, and authorised download.
135. Audit an input model for mass assignment. Add a new privileged persistence field and prove external clients cannot set it automatically.

### 18.36.10 Background work, concurrency, and testing

136. Implement a queue worker with visibility lease, renewal, idempotency, bounded retry, jitter, dead-letter state, and graceful shutdown.
137. Define payload schema evolution for queued jobs. Run old and new workers concurrently and replay an event created by each supported version.
138. Schedule a local-time daily task across both daylight-saving transitions in Europe/London. State gap, repetition, misfire, and deduplication policy.
139. Model a multi-step saga with compensation and one irrecoverable side effect. Expose states and manual-resolution paths rather than hiding failure.
140. Benchmark process, threaded, and asynchronous server models on CPU-bound, blocking-I/O, and non-blocking-I/O endpoints under equal resources.
141. Calculate total possible deepest calls when nested services retry. Introduce one deadline and retry budget that prevents multiplicative amplification.
142. Implement per-operation concurrency bulkheads. Saturate an expensive report endpoint and verify health and critical writes retain capacity.
143. Implement token-bucket rate limiting and a separate concurrency limit. Demonstrate why one does not substitute for the other.
144. Generate overload with an open-loop load tool. Compare unbounded queueing, bounded rejection, and adaptive shedding through tail latency and useful throughput.
145. Write unit, request, database integration, contract, browser, load, fault, and security tests for one operation. State the unique evidence each contributes.
146. Replace a mock that encoded a wrong provider assumption with a fake plus real sandbox integration test. Document the defect the mock concealed.
147. Use property-based tests for URL canonicalisation, cursor authentication, money conservation, and idempotent replay. Minimise one discovered counterexample.
148. Inject DNS failure, connection refusal, header timeout, truncated body, database deadlock, and response loss after commit. Verify classification and recovery.
149. Fuzz one parser boundary with size and depth limits. Preserve crashing inputs as regression tests and distinguish resource exhaustion from semantic rejection.
150. Measure line/branch coverage, mutation score, and requirement coverage for one module. Explain contradictions among the three.
151. Run database tests once on SQLite and once on the production DBMS. Catalogue every type, constraint, query, transaction, or concurrency difference.
152. Design a test-data strategy that preserves privacy, foreign-key shape, distribution, rare cases, and reproducibility without copying production secrets.

### 18.36.11 Deployment, observability, and reliability

153. Package a service into a minimal non-root container with pinned dependencies, multi-stage build, read-only runtime filesystem, health endpoints, and no embedded secrets.
154. Produce a software bill of materials and provenance record. Rebuild the same source and compare artifact digests, explaining any nondeterminism.
155. Configure a reverse proxy with TLS, host allowlist, forwarding trust, request limits, timeouts, buffering policy, and graceful upstream draining.
156. Separate startup, readiness, and liveness checks. Simulate database outage, exhausted pool, broken configuration, and application deadlock.
157. Deploy an immutable static asset under a content-hashed URL through a CDN. Verify cache key, compression variants, origin authentication, and old-page compatibility.
158. Execute rolling, blue–green, and canary deployments in a test environment. Compare resource cost, rollback, long connections, sessions, and schema compatibility.
159. Create an incompatible schema change, observe rolling failure, then redesign it using expand–migrate–contract and feature activation.
160. Implement graceful shutdown for HTTP, WebSocket, and background workers. Verify readiness withdrawal, connection drain, lease release, and hard deadline.
161. Define structured log schemas for request, authentication, database conflict, job, and deployment events. Apply redaction and retention tests.
162. Instrument counters, gauges, and histograms without unbounded labels. Deliberately create a cardinality explosion, measure it, and repair the dimensions.
163. Propagate trace context through HTTP and a queue while refusing to trust baggage for authorisation. Link a metric exemplar to one failed trace.
164. Define availability, correctness, latency, and freshness SLIs from eligible events. Identify cases that naive status-code counting misclassifies.
165. Set one SLO and calculate its error budget over 30 days. Construct short- and long-window burn-rate alerts and test notification routing.
166. Aggregate histograms across three instances and compare the correct percentile estimate with the invalid average of per-instance percentiles.
167. Build a circuit breaker with closed, open, and half-open states. Test classification, probe concurrency, recovery flapping, and shared-scope hazards.
168. Demonstrate nested retry amplification, then centralise retries with backoff, jitter, deadline, and a system-wide retry budget.
169. Design graceful degradation for a catalogue dependency. State which stale or absent data remain safe and which operations must fail closed.
170. Create encrypted backups with independent retention. Restore into isolation, run integrity/domain checks, and measure actual RPO and RTO.
171. Simulate failover to a lagging replica. Identify acknowledged writes at risk and define promotion, fencing, client routing, and failback.
172. Run a bounded chaos experiment terminating application instances during traffic. Define steady state, blast radius, abort condition, and evidence.
173. Write an incident runbook for certificate expiry, database saturation, credential leak, and bad deployment. Assign command, communications, mitigation, and evidence roles.
174. Conduct a post-incident review that moves from triggering action to systemic contributing factors and produces owned, testable corrective actions.

### 18.36.12 Final integrated branch capstone

175. Design, implement, attack-test, deploy, and operate a substantial Python web system. Begin with domain invariants, principals, trust boundaries, data classification, protocol semantics, and failure assumptions. Provide accessible browser interaction plus a versioned HTTP or GraphQL interface; WSGI or ASGI serving justified by workload; relational constraints and measured indexes; non-leaking transactions under concurrency; idempotency and an outbox for external work; phishing-resistant authentication where feasible; object-level authorisation; XSS, CSRF, SSRF, injection, upload, and resource-exhaustion controls; compatible migrations; unit, property, integration, contract, browser, security, load, and fault evidence; immutable deployment with proxy trust, health, draining, and rollback; privacy-aware logs, metrics, traces, SLIs, SLOs, and runbooks; tested backup restoration and one chaos exercise. Document every unproven assumption, inject at least ten boundary failures, and defend whether the resulting service should be released.
