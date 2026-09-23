# 19.33 Common misconceptions consolidated

1. **“Security means preventing hackers.”** It manages risks to defined assets from accidental and adversarial causes.
2. **“A system is secure.”** Security claims are relative to objectives, adversaries, assumptions, and time.
3. **“The internal network is trusted.”** Location is not identity or least privilege; internal systems can be compromised.
4. **“Python is memory-safe, so Python applications are secure.”** Memory safety prevents one defect family at one level; native extensions and logic flaws remain.
5. **“Input validation means removing special characters.”** Validity is a domain grammar, and structural separation is required at interpreter boundaries.
6. **“A resolved path prefix proves confinement.”** Links, races, case rules, and component semantics can invalidate string-based checks.
7. **“Using an argument list makes subprocesses safe.”** It removes shell parsing; the child program and its arguments remain an attack surface.
8. **“JSON is safe to deserialize.”** It avoids arbitrary Python object reconstruction but can still exhaust resources or violate schemas.
9. **“A hash encrypts data.”** A hash is one-way digest computation and supplies no confidentiality.
10. **“Encryption provides integrity automatically.”** Unauthenticated modes can permit modification; use an approved AEAD construction.
11. **“A nonce is a secret.”** It is commonly public but must satisfy uniqueness or other scheme-specific rules.
12. **“A salt is the password-encryption key.”** It is unique non-secret input to password hashing.
13. **“SHA-256 is sufficient for password storage.”** It is designed to be fast; passwords need deliberately expensive password hashing.
14. **“One seed source serves simulation and security.”** Scientific pseudorandom generators are not designed for adversarial unpredictability.
15. **“Dependency scanning proves the build is clean.”** It detects known matches under an inventory and database; provenance and unknown flaws remain.
16. **“Secrets are safe in environment variables.”** They can be a delivery mechanism but remain visible to authorised processes and diagnostics.
17. **“Rate limits stop denial of service.”** They are one capacity control and introduce identity and fairness trade-offs.
18. **“More logs always improve security.”** Excessive logging leaks data and overwhelms detection.
19. **“Reconnaissance is harmless because it only gathers information.”** Active requests can disrupt systems and require explicit authorisation.
20. **“Patching completes vulnerability management.”** Configuration, exposure, verification, compensating controls, and recurrence matter.
21. **“Public exposure implies permission to test.”** Technical reachability never substitutes for an owner’s explicit scope and rules of engagement.
22. **“Threat modelling predicts every future attack.”** It makes present assumptions and attack paths explicit so they can be challenged, tested, and revised.
23. **“Security and usability are opposites.”** Poor usability often causes control bypass, unsafe recovery, credential sharing, and operational error; both are design properties.
24. **“Privacy means encrypting personal data.”** Collection, purpose, inference, access, retention, correction, and deletion remain even when storage is encrypted.
25. **“A role check is complete authorisation.”** Policy must also bind the action to the particular resource, tenant, state, delegation, and context.
26. **“Containers are smaller virtual machines.”** They commonly share the host kernel and rely on namespaces, capabilities, policy, and runtime configuration.
27. **“Untrusted Python can be sandboxed with a restricted globals dictionary.”** Introspection, object graphs, imports, native code, and resource abuse defeat simplistic in-process restrictions.
28. **“Memory-safe languages remove native vulnerabilities.”** Interpreters, extensions, drivers, foreign libraries, kernels, and unsafe interfaces remain in the trusted computing base.
29. **“A parser either accepts or rejects, so two parsers cannot create a security issue.”** Different normalisation, duplicate, overflow, and recovery semantics can make one byte string acquire two meanings.
30. **“Allowlisting input removes the need for output encoding.”** Valid domain data can still contain syntax in a later HTML, SQL, shell, spreadsheet, or logging context.
31. **“An archive is safe once member paths are checked.”** Links, devices, expansion, collisions, metadata, nested formats, and partial extraction remain.
32. **“A source distribution is safer because it is human-readable.”** Installing it executes a build backend and dependencies; reviewability does not constrain runtime authority.
33. **“A digital signature makes software trustworthy.”** It authenticates a statement by a key; policy must trust the identity, source, build, review, and key custody.
34. **“Secret redaction can be added centrally at the log collector.”** Secrets may already traverse networks, queues, crash storage, and third-party processors; minimise before emission.
35. **“Cryptography fails only when algorithms are weak.”** Key lifecycle, nonce reuse, encoding, downgrade, side channels, endpoint compromise, and protocol composition dominate many failures.
36. **“Longer keys compensate for protocol mistakes.”** Key size cannot repair replay, unauthenticated context, nonce reuse, confused identities, or plaintext leakage.
37. **“Hash collisions mean hashes are useless.”** Security depends on the required property and algorithm; broken collision resistance does not make every non-adversarial checksum use equivalent.
38. **“HMAC encrypts authenticated messages.”** A MAC supplies integrity and symmetric source authentication; message bytes remain visible.
39. **“Authenticated encryption prevents replay.”** A copied valid ciphertext remains valid unless the protocol tracks sequence, freshness, or one-time use.
40. **“Anyone with a public key can know whose key it is.”** Public keys require an authenticated binding to names, roles, devices, or organisations.
41. **“Passwords with more character classes are always harder to guess.”** Human selection biases and predictable transformations can dominate nominal alphabet size.
42. **“Cryptographic randomness can be verified by looking random.”** Statistical appearance does not prove unpredictability or hidden state quality.
43. **“Destroying ciphertext deletes confidential data.”** Plaintext, keys, derived indexes, caches, exports, logs, and backups may survive.
44. **“A Python lock protects a database invariant.”** Only actors sharing that lock participate; the database or state owner must enforce cross-process concurrency.
45. **“Autoscaling defeats denial of service.”** It can amplify cost, hit downstream bottlenecks, and scale slower than hostile demand; admission and budgets remain necessary.
46. **“Tamper-evident logs are complete logs.”** Cryptographic chaining can expose alteration of received records but not events suppressed before emission.
47. **“An open port identifies the owning product and version.”** Addresses, proxies, shared infrastructure, deceptive banners, and backports make attribution an evidence problem.
48. **“No scanner findings means no vulnerabilities.”** Coverage, signatures, configuration, dynamic paths, unknown weaknesses, and scanner failure delimit the claim.
49. **“Security tests should reproduce the maximum possible impact.”** The least intrusive evidence sufficient to establish the property is safer, more ethical, and usually more useful.
50. **“Restoring from backup ends an incident.”** Backups can contain vulnerable configuration or persistence; identity, trust roots, monitoring, and affected parties also require recovery.
