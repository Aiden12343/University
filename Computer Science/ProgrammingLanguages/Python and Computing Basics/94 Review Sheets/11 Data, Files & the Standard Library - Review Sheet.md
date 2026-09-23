# 11.18 Common misconceptions consolidated

1. **“A text file stores characters.”** Storage contains bytes; an encoding contract maps them to text.
2. **“`read(n)` always returns exactly (n) units.”** Stream interfaces can return fewer, especially outside ordinary regular-file conditions.
3. **“Closing a file proves bytes reached permanent media.”** Buffers and durability layers require a named failure model and synchronisation contract.
4. **“Checking `exists()` guarantees the next operation.”** External state can change between check and use.
5. **“Valid JSON means valid application input.”** Parsing establishes format syntax; domain schema and semantics require separate validation.
6. **“CSV is lines split by commas.”** Quoting and embedded delimiters/newlines require a grammar-aware parser.
7. **“Pickle is just a compact data format.”** Unpickling can invoke code and must never accept untrusted content.
8. **“Context managers catch exceptions.”** They receive exit information and may release resources; suppression occurs only when explicitly indicated.
9. **“Iterator utilities are reusable collections.”** Many are one-shot lazy state machines sharing underlying inputs.
10. **“Dataclass annotations validate field values.”** They drive generated structure and static tools; domain validation remains explicit.

### 11.18.1 Further misconception boxes

> **Common misconception 11.42 — “A filename suffix proves the format.”** A suffix is naming metadata. Validate the declared format's internal grammar and schema before use.

> **Common misconception 11.43 — “If <code>write</code> returned, later <code>close</code> cannot fail.”** Buffered output can encounter its first lower-layer failure during flushing or closure.

> **Common misconception 11.44 — “An open file object keeps referring to whatever its original pathname currently names.”** An acquired handle and a repeatedly resolved pathname can diverge after rename or replacement.

> **Common misconception 11.45 — “Every readable stream can seek.”** Pipes, terminals, generators, sockets, and many transformed streams are forward-only. Seekability is a capability.

> **Common misconception 11.46 — “Binary mode means unbuffered mode.”** Binary mode selects bytes rather than text translation. Binary streams are normally still buffered unless unbuffered access is explicitly requested and supported.

> **Common misconception 11.47 — “Successful decoding identifies the encoding.”** Many codecs can decode the same byte sequence into different text. Encoding identity comes from a protocol contract or reliable metadata.

> **Common misconception 11.48 — “Unicode normalisation makes visually similar text identical.”** Normalisation addresses specified equivalences; fonts, confusables, scripts, and locale rules remain.

> **Common misconception 11.49 — “<code>casefold</code> is a complete safe username policy.”** It is one caseless-matching transformation. Normalisation, collision handling, script policy, and domain rules are separate.

> **Common misconception 11.50 — “Byte order matters only for old machines.”** Every multi-byte binary field needs an ordering contract so independent producers agree which byte is most significant.

> **Common misconception 11.51 — “A test using <code>StringIO</code> proves filesystem behaviour.”** It tests a text-stream layer, not permissions, encoding, storage exhaustion, rename, or durability.

> **Common misconception 11.52 — “Line iteration has constant memory.”** It avoids retaining all lines, but one unbounded line and aggregate state can still grow with input.

> **Common misconception 11.53 — “Rejecting <code>..</code> prevents path escape.”** Absolute paths, links, mounts, alternate separators, aliases, and races can cross an intended root.

> **Common misconception 11.54 — “Permission mode <code>0o600</code> proves secrecy.”** Access-control lists, privileges, backups, open handles, snapshots, and the surrounding directory affect confidentiality.

> **Common misconception 11.55 — “Unlinking securely erases bytes.”** It removes a namespace entry under filesystem rules; copies can remain in links, snapshots, backups, caches, journals, or storage media.

> **Common misconception 11.56 — “A temporary directory is a sandbox.”** It changes where names are created, not what resources the process can access.

> **Common misconception 11.57 — “JSON permits JavaScript comments and trailing commas.”** Standard JSON does not. A parser accepting them implements an extension that must be named.

> **Common misconception 11.58 — “JSON object member order is always meaningful because Python preserves it.”** Python exposes an order, but interoperable JSON object semantics should not depend on it without a separate application rule.

> **Common misconception 11.59 — “A JSON document must begin with an object or array.”** RFC 8259 permits any JSON value; an object/array-only rule belongs to an application schema.

> **Common misconception 11.60 — “<code>Decimal</code> serialises to JSON as an exact number automatically.”** The standard encoder rejects Decimal by default. A schema must choose and implement a representation.

> **Common misconception 11.61 — “JSON is safe, so its parser needs no limits.”** It avoids pickle-like callable reconstruction, but huge or deeply nested documents can still exhaust resources.

> **Common misconception 11.62 — “Spaces after a CSV delimiter are formatting.”** Unless the selected dialect says to skip them, spaces are field content.

> **Common misconception 11.63 — “Quoted CSV fields are strings and unquoted fields are numbers.”** Quoting protects grammar characters; type meaning comes from the column schema.

> **Common misconception 11.64 — “<code>reader.line_num</code> is the returned record number.”** It counts physical input lines consumed; one quoted record can span several.

> **Common misconception 11.65 — “CSV quoting prevents spreadsheet formula injection.”** The spreadsheet may evaluate the decoded cell after CSV parsing. Mitigation belongs to the downstream import contract.

> **Common misconception 11.66 — “Encryption makes any pickle safe.”** Confidentiality without authentication permits tampering; authenticated pickle still grants reconstruction authority to every authorised producer.

> **Common misconception 11.67 — “Overriding <code>find_class</code> creates a perfect pickle sandbox.”** Allowed objects, resource exhaustion, protocol extensions, implementation bugs, and future gadget behaviour remain.

> **Common misconception 11.68 — “The highest pickle protocol is always the best choice.”** It can exclude older readers and destabilise long-lived artefacts; select protocol by lifecycle and compatibility requirements.

> **Common misconception 11.69 — “<code>tee</code> duplicates an iterator for free.”** It buffers the lead of faster branches and shares yielded object references.

> **Common misconception 11.70 — “Lazy means no memory retention.”** <code>cycle</code>, <code>tee</code>, combinatorial pools, and downstream aggregators can retain substantial state.

> **Common misconception 11.71 — “An LRU cache can safely wrap any expensive function.”** Correctness requires stable results for keys, bounded retention, and a valid invalidation policy.

> **Common misconception 11.72 — “Frozen dataclasses are deeply immutable.”** Field rebinding is blocked through ordinary generated machinery; objects reachable through fields can still mutate.
