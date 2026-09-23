# 19.34 Exercises

### 19.34.1 Models and boundaries

1. Threat-model a password manager, medical appointment service, build pipeline, and home sensor. For each, define assets, actors, trust boundaries, adversary capabilities, controls, and residual risks.
2. Draw an authority map for a Python web worker: files, environment, database roles, network destinations, subprocesses, and cloud permissions. Remove every capability not required for one request.
3. Classify twenty failures by confidentiality, integrity, availability, authenticity, privacy, safety, and accountability. Allow multiple classifications and explain conflicts.
4. Take one control and identify at least five assumptions required for it to work.

### 19.34.2 Secure Python boundaries

5. Build a bounded parser for a small length-prefixed record format. Test truncated input, oversized lengths, duplicate fields, invalid UTF-8, excessive records, and trailing bytes.
6. Strengthen <code>confined_path</code> for one selected operating system using descriptor-relative operations. Document remaining races and platform limits.
7. Audit ten subprocess calls. Replace shell construction, add option terminators where supported, absolute executable identity, timeouts, output limits, and restricted execution.
8. Replace a pickle-based untrusted import with a data-only schema. Demonstrate rejection of unexpected types, fields, nesting, and sizes.
9. Design an archive extraction policy including path, link, device, count, individual size, total expansion, compression ratio, permissions, and collision handling.

### 19.34.3 Cryptography and identities

10. Hash a file incrementally, alter one bit, and compare digests. Explain why an untrusted expected digest supplies no authenticity.
11. Construct an HMAC-signed, versioned message with unambiguous length framing. Add replay prevention and key rotation.
12. Use a high-level AEAD library in a disposable program. Store nonce, key identifier, associated data, and ciphertext in a versioned envelope. Demonstrate that modifying each authenticated component causes rejection.
13. Compare passwords, API keys, session tokens, public keys, private keys, certificates, and authorisation scopes. State generation, storage, rotation, and revocation for each.
14. Implement password verification using a maintained library. Test correct, incorrect, malformed, and rehash-needed verifiers without leaking distinctions to a remote caller.
15. Design a token format with at least 128 bits of generated entropy. Calculate representation length and server-side storage/expiry policy.

### 19.34.4 Assurance and response

16. Build an SBOM for a small Python application. Trace every direct dependency to transitive packages, build backend, index, hash, licence, and known advisory status. State what the inventory cannot prove.
17. Write property-based tests for an object-level authorisation invariant. Include multiple principals, resources, roles, and state transitions.
18. Fuzz a disposable parser under CPU, memory, and time limits. Classify crashes, excessive resource use, hangs, and semantic inconsistencies.
19. Create an audit-event schema. Include actor, authentication method, action, object, outcome, timestamp, correlation, and sensitivity; exclude secrets. Test display against control-character injection.
20. Write rules of engagement for an authorised assessment: scope, exclusions, methods, rate, window, test source, contacts, evidence, emergency stop, and cleanup.
21. Run a tabletop incident involving a leaked CI token and malicious release. Produce a timeline, containment plan, credential/key inventory, rebuild plan, customer-impact assessment, and corrective actions.

### 19.34.5 Initial synthesis

22. Select a Python service developed under Chapter 18 or construct a local equivalent. Produce a threat model; reduce process and database authority; validate every parser and path; eliminate command and query construction; replace unsafe serialisation; define secrets and key lifecycles; add authenticated encryption only where its objective is explicit; generate an SBOM; add security properties to automated tests; create audit events and detection rules; conduct a strictly local authorised assessment; and exercise an incident runbook. Every claimed control must include assumptions, evidence, bypass considerations, and residual risk.

### 19.34.6 Threat modelling and security architecture

23. Write rules of engagement for a laboratory assessment containing exact assets, identities, techniques, exclusions, data handling, rate, time zone, stop conditions, contacts, evidence retention, restoration, and reporting. Ask another reader to identify every ambiguous authority.
24. Construct an isolated laboratory with synthetic identities, host-only networking, snapshots, resource limits, no production credentials, and no shared writable directory. From inside each guest, attempt to disprove every claimed boundary.
25. Produce a data-flow diagram for a password reset, including browser, mail provider, identity store, support process, audit system, and attacker-controlled links. Label parsers, identities, stores, trust boundaries, and retained data.
26. State ten security invariants for an online examination system. For each, list assumptions, enforcement points, monitoring evidence, recovery behaviour, and one counterexample that a superficial endpoint check would miss.
27. Threat-model a continuous-integration pipeline from pull request through deployed artifact. Include contributor, reviewer, runner, dependency index, cache, provenance service, registry, deployment controller, and production workload identities.
28. Build an attack tree for unauthorised package publication. Distinguish alternative paths from jointly required subgoals, then identify controls shared by multiple branches and single points of control failure.
29. Write abuse cases for a hospital appointment system from patient, staff, former staff, compromised service, malicious insider, and availability adversary perspectives. Relate each to a specific asset and harm.
30. Apply STRIDE to one data-flow boundary, then document at least five important threats or harms the mnemonic failed to elicit. Explain why taxonomy coverage is not model completeness.
31. Create a risk register with qualitative scales whose meanings are operationally defined. Record evidence and uncertainty separately from likelihood and impact; prohibit arithmetic on ordinal labels.
32. Compare two treatments for a vulnerable legacy service: immediate retirement and network isolation with monitored exception. Include safety, operational dependency, attacker activity, migration, exception expiry, and residual risk.
33. Model a control that reduces confidentiality risk while increasing availability or privacy risk. Define the decision authority and the measurements that would reveal the new harm.
34. Take a current architecture diagram and mark every trusted computing-base component. For each trust, state purpose, consequence of failure, update owner, evidence, and a design that would reduce its authority.
35. Design account recovery for users who lose every authenticator. Analyse enrolment evidence, support staff, coercion, insider threat, notification, delay, dispute, and recovery from a compromised recovery channel.
36. Compare discretionary, mandatory, role-based, attribute-based, relationship-based, and capability-based access control for a research-data repository. Choose a composed policy and state which layer is authoritative.
37. Model a confused-deputy flaw in a document-fetch service. Redesign the interface so caller authority, destination, protocol, address resolution, redirects, and egress are bound and independently enforced.
38. Create a privilege matrix for web process, parser worker, job broker, database migration, support console, backup agent, and deployment controller. Remove authority until one documented operation fails, then justify the minimal restoration.
39. Define a break-glass administrator workflow with approval, time-bound access, phishing-resistant authentication, recording, user notification where lawful, automatic expiry, and independent retrospective review.
40. Review a “zero trust” architecture claim. Enumerate the trust anchors it still depends upon and test whether network location, device posture, identity, resource, and continuous policy actually affect decisions.

### 19.34.7 Operating systems, capabilities, and native boundaries

41. Inventory every authority inherited by a Python service process: identifiers, groups, capabilities, descriptors, handles, environment, working directory, network routes, volumes, service tokens, and control-plane metadata. Remove three unnecessary capabilities.
42. Launch a child process with an explicit minimal environment, closed input, fixed working directory, no unintended descriptors, and restricted identity. Verify from inside the child that omitted authority is genuinely unavailable.
43. Compare Unix mode bits, access-control lists, Windows security descriptors, and one mandatory access-control mechanism for a private application file. State which claims are portable and which are platform-specific.
44. Demonstrate safely in a temporary directory that directory permissions govern deletion of a name independently from file content permissions. Explain the result using namespace and object authority.
45. Replace a predictable temporary-name sequence with exclusive secure creation. Write a concurrent test that makes the original race fail reproducibly without touching non-test paths.
46. Design a parser sandbox with precise filesystem, network, process, syscall, CPU, memory, output, time, and credential constraints. State which control enforces each restriction and the failure behaviour when it is unavailable.
47. Compare a container, virtual machine, separate operating-system account, language sandbox, and remote disposable worker for hostile native parsing. Evaluate kernel sharing, escape impact, startup, evidence, cleanup, and cost.
48. Pass a read-only stream capability into a function that previously accepted an arbitrary path. Measure the reduction in code paths, authority, and test fixtures; identify authority still held by the stream implementation.
49. Refactor a module that reads global credentials and opens arbitrary network clients so every external effect is an explicit narrow protocol. Draw the before-and-after authority graph.
50. Design a revocable capability for reading one document. Compare central lookup, short expiry, generation number, and key rotation for latency, availability, revocation delay, and blast radius.
51. Analyse a high-entropy sharing URL as a bearer capability. Identify every channel through which it can leak and implement scope, expiry, revocation, referrer policy, and log exclusion.
52. Attempt to design an in-process restricted-Python evaluator, then enumerate escape and denial-of-service surfaces from objects, imports, exceptions, descriptors, native extensions, memory, and computation. Replace it with an external isolation design.
53. Audit all compiled distributions in a Python environment. Map each wheel to native libraries, source provenance, update owner, parser inputs, and sandbox exposure.
54. Write boundary tests for a C extension length parameter covering negative values, zero, maximum accepted size, platform conversion limits, multiplication overflow, partial allocation, and exception cleanup.
55. Compile a disposable native parser with address and undefined-behaviour sanitisers. Fuzz its real entry point with a bounded corpus and preserve one minimised failure as a regression test.
56. Trace reference ownership through every success and error edge of a short CPython extension function. Show where a missing decrement leaks and where an extra decrement creates use-after-free.
57. Demonstrate that subinterpreters share a process failure fate by designing a harmless crash simulation outside production. Explain why process isolation is required for hostile native code.
58. Evaluate stack canaries, non-executable memory, ASLR, control-flow integrity, and memory tagging against one hypothetical out-of-bounds write. State what each mitigates and what it cannot repair.
59. Build a size-product helper at a Python/native boundary and test it against platform-sized limits, application quotas, and allocator failure. Distinguish arithmetic correctness from safe operational size.
60. Create a native-boundary review checklist covering signed conversion, lengths, ownership, lifetime, thread state, GIL assumptions, callbacks, error codes, allocation, and sanitiser evidence; apply it to one dependency.

### 19.34.8 Parsers, paths, injection, and serialisation

61. Specify a length-prefixed binary protocol including byte order, maximum frame, message count, zero length, end-of-stream, trailing bytes, errors, versioning, and semantic schema. Implement an incremental decoder and adversarial tests.
62. Compare two JSON parsers on duplicate keys, huge integers, invalid Unicode, deep arrays, trailing data, top-level scalars, and non-finite numbers. Resolve every differential through an explicit protocol rule.
63. Build a streaming upload reader that bounds total bytes, idle interval, absolute deadline, output, and downstream work. Show why limiting one chunk does not limit the stream.
64. Construct a harmless archive corpus containing parent paths, absolute paths, separators, links, duplicates, sparse metadata, high compression, nested archives, and platform collisions. Test a staged extraction policy in a disposable directory.
65. Use Python’s current `tarfile` extraction filter explicitly, then add application limits for entry count, expanded bytes, duplicate names, nested types, and deadline. Record what the built-in filter deliberately does not guarantee.
66. Define a Unicode identifier policy for one domain. Choose encoding, normalisation, scripts, case behaviour, confusable display, length unit, original-text retention, and migration from existing identifiers.
67. Generate alternative textual forms of IPv4 and IPv6 candidates accepted by relevant libraries. Verify an SSRF policy operates on resolved address objects and actual egress rather than textual prefixes.
68. Implement and property-test an ASCII domain identifier parser whose canonicalisation is explicitly part of the domain. Demonstrate a credential for which the same transformation would be incorrect.
69. Compare filesystem ancestry under case-sensitive and case-insensitive semantics available in your laboratory. Explain why a portable string prefix cannot establish confinement.
70. Implement descriptor-relative creation of one validated leaf on a supported operating system. Test existing files, final symlinks, concurrent replacement attempts, invalid names, permissions, and cleanup.
71. Design archive extraction as inspect–stage–validate–publish. Inject failure after each step and verify no partial content enters the application namespace.
72. Audit a subprocess wrapper for executable search, shell grammar, option injection, environment, locale, input, output, descendants, timeout, resource limits, status, and error disclosure.
73. Replace a shell pipeline with structured library or process APIs. Prove that metacharacters remain data and then test child-specific option and filename semantics separately.
74. Implement incremental child-output capture with a hard byte limit and whole-process-group termination in a disposable environment. Test a child that forks, closes pipes late, and ignores ordinary termination.
75. Map one stored string through every later interpreter context: database, JSON, HTML, JavaScript, DOM, CSV, log viewer, and shell export. Specify protection at each output boundary.
76. Replace string-built SQL, shell, LDAP, template, and regular-expression examples with parameterised or typed builders. For unavoidable structural choices, map an enum to fixed fragments.
77. Create a second-order injection test in which stored text becomes active only during an export or administrator workflow. Repair the later output boundary without corrupting the stored value.
78. Produce CSV intended for spreadsheet use and define a policy for formula-like cells, quoting, provenance, user warning, and round-trip preservation. Test multiple spreadsheet consumers if available.
79. Design a structured audit logger whose admitted schema excludes arbitrary headers and bodies. Test newline, escape, terminal-control, HTML, and query-language payloads through storage and viewing.
80. Demonstrate locally that unpickling can invoke construction behaviour, without creating persistence or external effects. Replace the boundary with a data-only schema and document the change in expressiveness.
81. Compare safe and object-constructing loaders in a serialisation library. Record exact loader configuration, version, network/entity behaviour, limits, and supported types as protocol requirements.
82. Define a versioned import envelope with strict fields, types, count, depth, numeric, and byte limits. Test missing, unknown, duplicate, null, ambiguous boolean/integer, and unsupported-version cases.
83. Authenticate a data envelope while binding purpose, producer, audience, version, event identifier, and expiry. Demonstrate that replay protection requires state beyond signature validity.
84. Migrate an old schema through current domain validation. Construct an old artifact that would bypass a newly introduced invariant if migration merely copied fields.
85. Threat-model a parser service handling documents, images, XML, archives, and media. Assign each format a sandbox, limits, patch owner, corpus, fuzz harness, telemetry, and failure policy.

### 19.34.9 Supply chains and secrets

86. Draw the complete dependency graph for a Python application, including interpreter, direct and transitive packages, build backends, native libraries, operating-system packages, container base, CI actions, and deployment tooling.
87. Resolve the same broad requirement set against two controlled index snapshots and compare artifacts. Explain why unchanged application source did not determine one environment.
88. Create environment-specific locks with artifact hashes for two platforms. Verify that every selected wheel or source distribution is intentional and that an unexpected artifact fails closed.
89. Model dependency confusion using harmless local indexes and invented names. Repair repository selection, namespace ownership, and fallback policy; do not publish or query deceptive public packages.
90. Build an untrusted source distribution in an isolated disposable worker with no secrets and restricted network. Record every build dependency and attempted external effect.
91. Generate an SBOM from the built artifact and compare it with source manifests and the running environment. Catalogue vendored, dynamic, operating-system, and build-time components each method misses.
92. Verify an artifact digest from approved metadata, then replace both artifact and digest in an untrusted location. Explain why trust in the metadata path, not hashing alone, determines authenticity.
93. Define an attestation policy specifying issuer, subject identity, repository, workflow, source revision, builder, predicate, transparency evidence, and freshness. Reject three correctly signed but policy-invalid attestations.
94. Attempt a reproducible build on two isolated builders. Identify timestamps, paths, archive order, locale, randomness, toolchain, and dependency inputs responsible for any difference.
95. Audit a CI workflow triggered by untrusted changes. Remove release secrets, broad tokens, mutable third-party actions, shared persistent runners, unsafe caches, and direct production authority.
96. Design a privileged release stage that consumes only reviewed source and verified test evidence, obtains short-lived publication identity, produces provenance, signs immutable output, and cannot be invoked by arbitrary branch code.
97. Compare frozen dependencies, unattended updates, and automated reviewed update proposals. Define a policy balancing known-vulnerability exposure, change risk, test confidence, and emergency response.
98. Build a secret inventory containing issuer, subject, audience, scope, owner, consumers, storage, delivery, lifetime, rotation, revocation, and audit for every credential in a small service.
99. Replace one long-lived cloud key with workload identity and short-lived credentials. Threat-model the identity issuer, metadata route, SSRF, clock, revocation, and availability dependency introduced.
100. Compare environment variables, mounted files, operating-system credential stores, and a managed secret service for one workload. Test inheritance, diagnostic exposure, update, permissions, and outage behaviour.
101. Implement a log schema that admits only approved fields. Inject secrets through URLs, nested exceptions, headers, subprocess output, object representations, and error paths; verify they never leave the process.
102. Exercise zero-downtime rotation for a signing or API credential: introduce, dual-accept, migrate, observe, revoke, and verify. Inject failure at every stage and recover without restoring the retired key for new use.
103. Design revocation for sessions, opaque API tokens, and self-contained signed access tokens. Compare maximum delay, online dependency, scale, privacy, and incident blast radius.
104. Seed a synthetic secret into a repository, history, artifact, issue, and log in a closed laboratory. Evaluate scanner coverage, then revoke the synthetic authority and remove retained copies under policy.
105. Run a tabletop exercise in which the secret-distribution pipeline, rather than one credential, is compromised. Establish a clean root of trust before issuing replacements.

### 19.34.10 Cryptographic constructions and key lifecycles

106. For confidentiality, integrity, authenticity, password verification, public attribution, and unpredictability, select the appropriate construction and explain why each other primitive is a category error.
107. Specify a versioned cryptographic message format using length framing and domain separation. Prove that alternative field partitions cannot produce identical framed bytes.
108. Identify every observable side channel in a remote authentication path: length, lookup, parse, branch, allocation, response, retry, logging, and rate limit. State which are secret-dependent and practically measurable.
109. Compare ordinary equality with `compare_digest` for fixed-length tags. Explain precisely what the latter changes and five surrounding timing sources it does not.
110. Build a cryptographic migration inventory listing protocol, algorithm, parameter, key location, data lifetime, peer, library, owner, version signal, and fallback. Design downgrade-resistant migration.
111. Hash a multi-gigabyte synthetic file incrementally and verify memory remains bounded. Alter one bit, then explain why the result provides no publisher authenticity without trusted expected metadata.
112. Calculate generic preimage and collision work for 128-, 192-, 256-, and 512-bit digests. Relate output truncation to the property actually required.
113. Implement separated leaf and internal-node hashing for a small Merkle tree. Specify odd-leaf handling, proof order, trusted root distribution, and algorithm versioning.
114. Demonstrate a content-addressed store in a laboratory. Analyse deduplication equality leakage, malicious content, garbage collection, collision policy, provenance, and access control.
115. Construct an HMAC envelope binding protocol, version, sender role, audience, operation, identifier, timestamp, and body. Test every field for tampering and parsing ambiguity.
116. Truncate a MAC tag in a toy protocol and calculate forgery probability under its online attempt budget. Do not weaken any production protocol; derive an acceptable policy from required risk.
117. Add persistent event identifiers to the timestamped webhook example. Use one database transaction to reject replay and apply the business effect, including response loss and retry.
118. Derive distinct subkeys for two protocol contexts through an approved KDF. Show that labels and salt/context are represented unambiguously and keys never cross uses.
119. Encrypt records with a maintained AEAD library under a versioned envelope. Tamper with nonce, ciphertext, tag, key identifier, record identifier, and associated data; require indistinguishable safe failure.
120. Simulate random nonce allocation at increasing message counts and compare observed collisions with the birthday estimate. Keep this as a mathematical laboratory, not production key usage.
121. Design durable counter nonces across processes, crash rollback, restored snapshots, failover, and key rotation. Decide whether the operational proof is stronger than a suitably large random nonce policy.
122. Specify authenticated chunked encryption that detects reorder, omission, duplication, splicing, and truncation. Compare it with a reviewed streaming construction before implementing anything outside a lab.
123. Measure ciphertext metadata leakage: plaintext-length classes, access time, update frequency, key identifiers, and peer relationships. Add only padding or shaping controls justified by the threat model.
124. Perform an ephemeral authenticated key agreement using a maintained high-level protocol or library example. Identify transcript binding, KDF context, identity, forward secrecy, and private-value destruction.
125. Sign a release digest with a test Ed25519 key and verify project, version, and domain-separated bytes. Substitute a different trusted project while retaining the signature and confirm rejection.
126. Build a certificate-validation checklist covering chain, trust anchor, host or identity, time, key usage, constraints, algorithm, revocation policy, and transparency monitoring. Apply it to a local test hierarchy.
127. Benchmark Argon2id parameters on the intended authentication host under realistic concurrency and memory pressure. Select a documented policy balancing offline cost, latency, capacity, and denial-of-service risk.
128. Test password handling for long manager-generated values, Unicode, exact-byte preservation, paste, compromised-choice screening, malformed stored verifiers, rehash, generic remote errors, and recovery.
129. Generate bearer tokens from `secrets`, calculate encoded entropy, store only verifiers, apply purpose and expiry, and consume a one-time token atomically under concurrent requests.
130. Design a key hierarchy and lifecycle with pending, active, decrypt-only, revoked, compromised, and destroyed states. Exercise envelope rewrapping, backup recovery, cryptographic erasure claims, and one compromised-key response.

### 19.34.11 Races, abuse, observability, and vulnerability management

131. Reproduce a harmless check-then-use race on a one-time token with two concurrent workers. Replace it with one conditional database transition and verify exactly one success under repeated stress.
132. Implement optimistic versioning for an authorisation-sensitive update. On conflict, recompute identity, policy, and domain state rather than blindly replaying stale intent.
133. Model a distributed lease whose holder pauses past expiry. Add a fencing token enforced by the protected resource and prove the stale holder’s write is rejected.
134. Inventory cost amplification in an upload path from connection through parsing, storage, database, queue, third-party calls, logs, and human review. Place a measured bound at each owner.
135. Implement token-bucket rate and independent concurrency limits in a laboratory. Demonstrate workloads that satisfy one while exhausting the resource governed by the other.
136. Test an endpoint with slow input, huge headers, compressed expansion, deep structure, expensive invalid authentication, cache misses, database fan-out, and response loss. Record where admission occurs.
137. Construct a regular expression or parser with pathological worst-case behaviour in an isolated benchmark, replace it with a bounded or linear design, and compare asymptotic and observed cost.
138. Fill separate temporary, upload, log, cache, and dead-letter quotas in a disposable environment. Verify critical recovery and audit paths retain reserved capacity.
139. Propagate an absolute deadline through application, database, subprocess, and remote-call layers. Confirm cancellation releases the actual work rather than merely returning to the client.
140. Evaluate an abuse-control policy against shared networks, account creation, stolen accounts, privacy, accessibility, and appeals. Measure false positives on representative synthetic populations.
141. Define audit events for authentication, privilege change, sensitive read, export, key operation, policy denial, deployment, and incident access. Distinguish claims from trusted principal and peer data.
142. Inject control characters, forged timestamps, high-cardinality identifiers, active HTML, and query syntax into telemetry. Verify bounded ingestion, safe storage, safe viewing, and privacy-aware redaction.
143. Build a hash-chained test log with signed periodic checkpoints. Demonstrate that editing retained records is detectable and that suppressing events before emission remains outside the proof.
144. Write a detection specification with data sources, query, window, exclusions, severity, owner, runbook, tests, and quality monitors. Backtest it against synthetic benign and adversarial traces.
145. Measure precision, estimated recall, alert latency, and analyst effort for a detection. Tune it without deleting raw evidence and document uncertainty in the ground truth.
146. Build an asset record joining provider identity, owner, service, environment, data class, source repository, addresses, domains, certificates, and lifecycle. Reconcile stale observations without active scanning.
147. Derive a time-bound active target list from the authorised inventory, then run only a harmless local connectivity validation with global/per-target limits, identifiable source, response bounds, and automatic stop conditions.
148. Take one scanner banner finding and validate ownership, product, vendor build, configuration, backports, and actual prerequisite before calling it a vulnerability.
149. For ten advisories, distinguish CVE identity, CWE weakness, CVSS intrinsic severity, EPSS exploitation prediction, CISA KEV evidence, asset exposure, business harm, and remediation decision.
150. Trace a vulnerable transitive dependency from SBOM to every deployed artifact and owner. Verify actual versions and reachability, then patch, deploy progressively, and repeat the vulnerable property test.
151. Create a compensating-control exception with accountable owner, rationale, evidence, monitoring, expiry, migration plan, and automatic review. Demonstrate that expiry becomes visible and actionable.
152. Draft a coordinated vulnerability disclosure policy stating contact, encryption, scope, safe harbour, prohibited techniques, acknowledgement, communication, remediation, publication, and data deletion.

### 19.34.12 Secure lifecycle, testing, and incident response

153. Convert ten vague requirements such as “protect data” into testable security invariants with threat, scope, control, evidence, monitoring, recovery, and owner.
154. Audit installation defaults for listening, debug, credentials, cookies, telemetry, permissions, encryption, administrative routes, and failure. Make the protected state usable without hidden hardening steps.
155. Review a security-sensitive change by tracing identity, object-level authorisation, parser, canonicalisation, transaction, key context, retry, cancellation, logs, old clients, and rolling deployment.
156. Protect a release branch while accounting for administrators, automation identities, workflow changes, mutable actions, force pushes, compromised reviewers, and evidence outside the repository.
157. Build and deploy an immutable test artifact with source revision, SBOM, provenance, signature, registry digest, approval, and running-instance identity. Prove a locally rebuilt unapproved artifact is rejected.
158. Design end-of-life controls for an unsupported service: inventory, owner notification, deployment prevention, exposure removal, data migration, evidence retention, credential revocation, and verified destruction.
159. Map a small project to NIST SSDF outcomes. For every claimed practice, attach concrete repository, pipeline, test, deployment, or response evidence rather than a policy statement alone.
160. Build a security assurance matrix mapping invariants to unit, property, integration, configuration, fuzz, dependency, system, penetration, and incident-exercise evidence. Identify untested assumptions.
161. Calibrate static analysis, dependency scanning, secret scanning, and configuration checks against deliberately seeded safe test cases. Measure false positives, false negatives, runtime, and suppression expiry.
162. Write a deterministic fuzz harness for one real parser boundary. Add CPU, memory, and output limits; preserve minimised cases; and treat hangs, resource growth, differential results, and invariant violations as findings.
163. Construct negative authorisation tests over multiple principals, tenants, objects, roles, delegations, states, exports, search, caches, and support paths. Verify both denial and absence of information leakage.
164. Perform differential testing between two parser implementations or versions. For every disagreement, consult the protocol specification and add one conformance test rather than choosing the convenient result.
165. Define metamorphic properties for canonicalisation, signatures, AEAD associated data, archive ordering, and log serialisation. Generate transformations that should preserve or invalidate results predictably.
166. Plan a production-safe validation requiring explicit approval. Specify minimal request, synthetic identity, monitored window, rollback, stop signal, cleanup, evidence, and why a lower-risk environment is insufficient.
167. Write a finding report that separates direct observation, interpretation, consequence, likelihood factors, uncertainty, and remediation. Have another reviewer reproduce it without receiving unnecessary exploit automation.
168. Run an incident tabletop beginning with a suspicious release attestation. Establish command, independent communications, timeline, evidence, containment, clean trust root, rebuild, impact, notification, and recovery gates.
169. Acquire a synthetic evidence file through a documented laboratory process. Record source, tool, time, handler, size, digest, storage, copies, and every limitation of what the hash proves.
170. Simulate compromised identity-provider administration. Inventory sessions, recovery routes, service accounts, federation, signing keys, downstream trust, and independent re-enrolment paths.
171. Restore a backup captured during a simulated compromise into isolation. Search for persistence and vulnerable configuration, patch through a clean pipeline, validate invariants, and measure recovery time and data loss.
172. Write an incident decision log while evidence changes from low-confidence alert to confirmed cross-tenant disclosure. Preserve why each containment action was taken and what would reverse it.
173. Conduct a post-incident review using multiple contributing conditions rather than one “root cause”. Produce owned actions across architecture, identity, detection, testing, process, training, and recovery.
174. Verify every corrective action from Exercise 173 through a test, control observation, or completed exercise. Reject “be careful”, “monitor closely”, and unowned documentation as closure evidence.

### 19.34.13 Final integrated branch capstone

175. Design, implement, harden, assess, and operate a substantial Python system containing authentication, object-level authorisation, untrusted structured input, file or network I/O, durable state, background work, dependencies, and deployment automation. Begin with written authorisation for the laboratory, assets, actors, data-flow and authority maps, abuse cases, security invariants, assumptions, privacy and safety consequences, and a risk register. Reduce operating-system, database, network, build, and cloud capabilities; isolate native parsers; bound bytes, depth, expansion, time, memory, output, queues, and third-party cost; enforce canonicalisation and domain validation before structured interpreter boundaries; eliminate path, shell, query, template, log, archive, and deserialisation ambiguity; use current high-level cryptography only for stated objectives with versioned envelopes, nonce and key lifecycles, recovery, and compromise handling; implement phishing-resistant authentication where feasible, safe recovery, scoped sessions, and resource-specific policy; lock and authenticate dependencies, produce an SBOM and provenance, and admit only approved artifacts; add negative, property, differential, integration, fuzz, configuration, load, and penetration evidence; design privacy-aware audit events and tested detections; triage current advisories using exploit and deployment context; deploy progressively with rollback that preserves security state; and exercise a compound incident involving credential theft plus a parser vulnerability. For every security claim, provide scope, threat, assumption, enforcement point, measurement, bypass analysis, failure mode, owner, residual risk, and reproducible evidence. Defend whether the system should be released and which claims remain unproved.
