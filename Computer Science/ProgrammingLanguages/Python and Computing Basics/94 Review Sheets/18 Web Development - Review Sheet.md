# 18.35 Common misconceptions consolidated

1. **“The Internet and the web are the same.”** The web uses Internet networking; many Internet protocols are not HTTP.
2. **“TCP preserves messages.”** It presents an ordered byte stream; the application defines message boundaries.
3. **“HTTPS means a site is safe.”** TLS protects authenticated transport, not application intent or truth.
4. **“A URL is a string.”** It is a structured identifier whose components have different parsing and encoding rules.
5. **“HTTP is stateless, so web applications cannot retain state.”** Protocol requests are stateless in the relevant sense; applications store state through sessions and databases.
6. **“GET may update state if it is convenient.”** Safe-method semantics support caching, prefetching, crawling, and user expectations; state changes violate the contract.
7. **“Idempotent means the response is identical.”** It concerns intended effect after repetitions, not necessarily response bytes or status.
8. **“A 500 means the client sent bad data.”** It reports server failure; invalid client content should map to an appropriate client-associated status.
9. **“JSON supplies a schema.”** It supplies a data syntax; field meaning and constraints remain application-defined.
10. **“An async function runs in parallel.”** It permits cooperative suspension; CPU work can still block an event loop.
11. **“Flask’s development server is a production server.”** Production requires controlled serving, limits, workers, TLS/proxy integration, and lifecycle management.
12. **“An ORM eliminates SQL.”** It generates and executes relational queries whose cardinality and plans must be understood.
13. **“Transactions prevent every race.”** Isolation level and operation design determine which anomalies remain possible.
14. **“Escaping input prevents injection.”** Structural parameterisation and context-specific output encoding are the governing boundaries.
15. **“Authentication implies authorisation.”** Knowing the principal does not decide whether it may act on a particular resource.
16. **“CORS protects the server from requests.”** It is a browser read/permission mechanism, not general request authentication or CSRF prevention.
17. **“A successful enqueue means work happened.”** Queue delivery and side effects have separate acknowledgement and retry semantics.
18. **“One process-global dictionary is application storage.”** It is neither durable nor coherently shared across workers and hosts.
19. **“More retries improve reliability.”** Unbounded retries amplify load and duplicate ambiguous operations.
20. **“Logs can safely contain everything for debugging.”** Logs are durable disclosures and must minimise secrets and personal data.
21. **“DNS is a permanent phone book from names to servers.”** It is a typed, delegated, cached database whose answers can vary and change.
22. **“A port belongs to one application forever.”** It is a transport number bound under an address, protocol, process lifetime, and operating-system policy.
23. **“Receiving fewer bytes than requested means the connection is broken.”** Stream reads may return any positive available count; protocols accumulate until their frame is complete.
24. **“TLS certificates certify that a business is trustworthy.”** They bind keys to names or identities under issuance policy, not honesty, content quality, or authorisation.
25. **“The URL path is already safe after percent-decoding.”** Decoding and normalisation order can change separators and traversal meaning; each layer needs one canonical policy.
26. **“Header names and values can be copied through a proxy unchanged.”** Hop-by-hop fields, forwarded identity, framing controls, and trust boundaries require explicit handling.
27. **“HTTP/3 is HTTP over unreliable transport.”** QUIC builds encrypted reliable streams and congestion control over UDP datagrams.
28. **“A 404 always proves that no resource exists.”** Servers can conceal unauthorised existence, and intermediaries or replicas can have different state.
29. **“Compression only reduces bandwidth.”** It consumes CPU, changes cache variants and validators, and can amplify untrusted input during decompression.
30. **“Private responses are safe in any cache.”** Cache keys, shared-cache controls, authentication scope, purge, and intermediary behaviour must all preserve isolation.
31. **“Cookie <code>Path</code> isolates applications securely.”** It controls attachment scope but same-origin scripts and cookie-setting rules can cross path boundaries.
32. **“JWT validation means decoding its JSON.”** Validation requires trusted algorithms and keys, issuer, audience, time, purpose, and application claims.
33. **“Middleware order is merely stylistic.”** Authentication, sessions, transactions, exceptions, compression, and security fields observe and transform different states by order.
34. **“Async database calls make the database handle more work.”** They free the event-loop thread while waiting; database capacity and query cost remain.
35. **“A unique application check prevents duplicates.”** Concurrent requests can both pass; an authoritative database constraint or atomic conditional write is required.
36. **“Database NULL is Python <code>None</code> with another spelling.”** SQL uses three-valued logic and query-specific null semantics that an ORM must translate.
37. **“Serializable transactions never need retries.”** Implementations can abort transactions precisely to preserve serialisability under conflict.
38. **“A migration rollback always restores the old world.”** Destructive data changes and new-version writes can be irreversible or unreadable to old code.
39. **“Cursor pagination is automatically stable.”** Its ordering, tie-breaker, filter scope, mutation policy, expiry, and authentication determine stability.
40. **“GraphQL removes API versioning.”** Schemas still evolve, clients retain assumptions, fields deprecate, and semantic changes require compatibility policy.
41. **“MFA means asking for any two secrets.”** Independent factors and phishing resistance matter; recovery must not collapse assurance.
42. **“A UUID is an access-control mechanism.”** It can reduce guessing but does not grant or deny authority.
43. **“Sanitising input prevents XSS.”** Store canonical data and encode or sanitise for the exact output context at the final boundary.
44. **“SameSite cookies eliminate CSRF.”** They mitigate common cross-site attachment paths but do not replace tokens, origin policy, and method semantics.
45. **“Private IP blocking is enough for SSRF.”** Redirects, DNS changes, IPv6, link-local services, alternate encodings, and privileged public endpoints remain.
46. **“A background task can trust the role captured when it was queued.”** Authority can be revoked; workers need minimal context and current policy where the action demands it.
47. **“WebSockets are ordinary HTTP requests that stay open.”** They establish a distinct framed bidirectional protocol with continuing authentication, limits, and delivery concerns.
48. **“Readiness and liveness should test every dependency identically.”** Readiness controls traffic; liveness controls restart. Coupling liveness to a shared outage can amplify it.
49. **“Replicas are backups.”** Replicas reproduce deletion and corruption; backups require independent retention and tested restoration.
50. **“If no alert fired, users were unaffected.”** Missing or badly defined telemetry can conceal failures; observability is itself a tested system.
