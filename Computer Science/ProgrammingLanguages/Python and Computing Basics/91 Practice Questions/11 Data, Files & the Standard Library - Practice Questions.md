# 11.19 Exercises

### 11.19.1 Files and text

1. Create one UTF-8 text fixture containing ASCII, a multi-byte code point, a combining sequence, and mixed line endings. Record code-point, byte, and line counts under explicit APIs.
2. Demonstrate decode policies `strict`, `replace`, and `ignore` on invalid bytes. State information lost by each non-strict policy.
3. Implement a streaming line analyser and bound its retained memory in terms of longest line and aggregate state.
4. Design an atomic-replacement procedure and state exactly which atomicity and durability properties remain unproved.

### 11.19.2 Serialisation

5. Define a versioned JSON schema for a dataclass model containing dates, decimals, sets, and bytes. Write explicit encode/decode functions and reject unknown or missing fields under a policy.
6. Construct CSV containing an embedded comma, quote, and newline. Show why `split(",")` fails.
7. Design protection for spreadsheet formula injection for a named spreadsheet consumer; distinguish display escaping from source data.
8. Explain why authenticating a pickle’s sender does not guarantee version compatibility or safe intent.

### 11.19.3 Standard library

9. Use `deque` to implement bounded history and specify which item is discarded on overflow.
10. Compare `Counter`, ordinary dictionary, and set for three distinct frequency/uniqueness problems.
11. Demonstrate `groupby` on unsorted and sorted data and explain shared-iterator lifetime.
12. Build a dynamic resource acquisition function with `ExitStack` and prove cleanup after failure during the third acquisition.

### 11.19.4 Integrated exercise

13. Implement the CSV-to-JSON measurement pipeline. Require controlled encodings, finite numbers, source-position diagnostics, schema versioning, deterministic fixtures, temporary-output replacement, clean resource release, and no pickle. Test invalid bytes, malformed CSV, missing columns, non-finite values, empty input, storage failure simulation, and replacement interruption. Document each boundary and the strongest durability claim actually established.

### 11.19.5 Boundary analysis

14. For a function that reads a price from an environment variable, identify representation, syntax, schema, semantic, authenticity, and authority checks. State which layers do not apply and justify each omission.
15. Refactor a function that opens JSON, computes a discount, and writes a receipt into boundary adapters and a pure core. Draw its dependency direction and write tests that use no filesystem for the core.
16. Construct three operations—set a value, increment a value, and append an event—and state the observation model under which each is or is not idempotent.
17. Model a timed-out payment request whose server may have committed. Define result states more precise than Boolean success and specify the safe retry rule for each.
18. Write a fault-injecting text writer that fails on its third call. Use it to determine the exact partial output of a five-record producer.
19. Design an idempotency-key table for a transactional store. State uniqueness, retention, content-binding, concurrency, and crash-atomicity requirements.
20. Given an importer that logs complete bad rows, identify confidentiality, log-injection, and resource-exhaustion risks. Replace it with a bounded structured diagnostic.
21. Define byte, record, field, nesting, distinct-key, elapsed-time, and output-size budgets for a public upload endpoint. Explain how each is enforced before excessive resource use.
22. Compare fail-fast and error-accumulating batch imports. Bound diagnostic storage and define whether valid rows before an error may commit.
23. Provide a compensation plan for a workflow that charges a card, writes a database row, and sends an email. Explain why compensation is not rollback.
24. Build a claim ledger for “the report was saved safely”, separating language rules, library contracts, filesystem assumptions, measurements, and judgements.
25. Take an application boundary from a prior chapter and enumerate every implicit ambient input: current directory, locale, clock, environment, installed packages, permissions, and process state. Convert at least three into explicit parameters.

### 11.19.6 Bytes, Unicode, and text

26. For the strings <code>"A"</code>, <code>"é"</code>, <code>"e\u0301"</code>, <code>"水"</code>, and one multi-code-point emoji, tabulate code points, UTF-8 bytes, Python length, NFC form, and observed display width. Label which results are specified and which are environmental.
27. Implement a hexadecimal byte viewer that accepts a binary stream and emits fixed-width offset, hex, and printable-ASCII columns without reading the complete input.
28. Demonstrate the indexing and slicing differences among <code>bytes</code>, <code>bytearray</code>, <code>memoryview</code>, and <code>str</code>. Include mutation/aliasing tests.
29. Write <code>read_exactly</code> tests for zero length, one-byte chunks, premature end, a reader that returns more than requested in violation of contract, and a reader that makes no progress.
30. Adapt <code>read_exactly</code> for an interface whose temporary unavailability raises <code>BlockingIOError</code>. State why a busy retry loop is unacceptable.
31. Implement an incremental UTF-8 decoder over arbitrarily divided chunks. Test every possible split position in a four-byte sequence and incomplete final input.
32. Compare <code>strict</code>, <code>replace</code>, <code>ignore</code>, <code>backslashreplace</code>, and <code>surrogateescape</code> on selected malformed bytes. For each, state whether exact byte recovery is possible.
33. Create an ASCII encoder boundary for a legacy protocol. Define how a non-ASCII name is rejected and ensure the diagnostic does not leak unrelated record fields.
34. Explain, with counterexamples, why decoding success cannot identify an encoding. Use one byte string decoded under UTF-8, Latin-1, and another applicable codec.
35. Build a validator that requires NFC-normalised text. Then build a normaliser. Explain the semantic difference between rejecting and transforming.
36. Investigate <code>casefold</code> examples whose length changes. Design a collision-detection step for a caseless registry and preserve the user's original spelling separately.
37. Compare <code>utf-8</code> and <code>utf-8-sig</code> on input with and without a signature. State a protocol policy for each of four combinations.
38. Write a binary UTF-16 fixture in both byte orders. Decode it with generic and explicit-endian codecs and explain the BOM's role.
39. Create a mixed-newline byte fixture. Read it with every permitted <code>newline</code> mode and record returned strings and the stream's <code>newlines</code> attribute.
40. Write the same logical lines under <code>newline=None</code>, <code>""</code>, <code>"\n"</code>, and <code>"\r\n"</code>. Compare exact bytes on two supported operating systems or explain how a controlled CI matrix would do so.
41. Wrap <code>BytesIO</code> in <code>TextIOWrapper</code>; demonstrate why <code>flush</code> is needed before inspecting bytes and why <code>detach</code> changes ownership.
42. Define a length-prefixed binary message with signature, version, unsigned length, and payload. Implement strict read/write functions and reject oversized or truncated frames.
43. Extend the binary message with an unkeyed checksum. List corruption classes it detects and explain why it does not authenticate a sender.
44. Use <code>struct.calcsize</code>, <code>pack</code>, and <code>unpack</code> to compare native and standard sizes. State why a persistent protocol should not rely on native padding.
45. Design terminal output that uses colour only when appropriate and keeps machine output on standard output separate from diagnostics. Test redirection with in-memory streams.

### 11.19.7 Streams and file objects

46. Open one binary file through two independent file objects. Demonstrate independent offsets, then explain why this does not give coherent concurrent updates.
47. Duplicate a low-level descriptor where supported and experimentally determine offset sharing. Classify the result as platform/implementation evidence.
48. Show exactly when <code>w</code> truncates by placing a failing computation before and after opening. Rewrite the operation to preserve prior data.
49. Use <code>x</code> mode from two competing processes or controlled simulations. Explain what exclusive creation proves and why a stale file is not a complete lock.
50. Implement an append-only event writer and a recovery reader that rejects a partial final record. State unproved multi-writer atomicity assumptions.
51. Update a variable-length text value through <code>r+</code> with and without <code>truncate</code>. Construct the stale-suffix failure.
52. Demonstrate text-stream <code>tell</code> cookies with multi-byte UTF-8 and newline translation. Show why adding one to a cookie is not a supported byte-position calculation.
53. Write an API accepting any seekable binary stream. Reject a pipe-like non-seekable double with a precise capability error.
54. Implement a bounded prefix sniffer for a non-seekable chunk iterator that replays the prefix without duplicating or losing bytes.
55. Compare <code>read</code>, <code>readlines</code>, and line iteration on files of increasing size. Measure peak memory under a controlled profiler and label results empirical.
56. Construct one file containing a single 100 MiB line. Explain why line iteration alone does not meet a 10 MiB memory requirement.
57. Implement fixed-size binary block hashing using <code>hashlib</code>. Verify equality with one-shot hashing and distinguish integrity checking from authentication.
58. Demonstrate that returning a generator expression from inside <code>with</code> fails on later use. Repair it with a generator function and then design an explicit context-managed iterator.
59. Write a wrapper that owns a supplied descriptor only when <code>closefd=True</code>. Test all normal and exceptional closure paths without leaking descriptors.
60. Build a file-like text writer protocol and three implementations: in-memory, counting, and fail-after-N. Use them to test one renderer.
61. Inject a failure from <code>close</code> after successful writes. Decide which exception a boundary should expose and how it preserves both write and close evidence if both fail.
62. Compare one-character writes under unbuffered/buffered binary modes where supported. Record system-call counts with an appropriate tracing tool and avoid generalising beyond the test platform.
63. Design an ownership table for a function receiving a path, caller-owned stream, or bytes. State which layer acquires, closes, and reports each failure.

### 11.19.8 Context managers

64. Implement a class-based manager that records entry, body, and exit events. Verify normal, return, loop-break, and exception paths.
65. Write a deliberately suppressing manager for one custom exception. Ensure subclasses are either included or excluded by explicit policy.
66. Construct a manager whose <code>__enter__</code> fails. Verify that its own exit is not called while an already-entered outer manager is exited.
67. Construct an exit method that raises during propagation of a body exception. Inspect cause/context and design a combined diagnostic policy.
68. Turn a class manager into an equivalent <code>@contextmanager</code> implementation. Compare state visibility, reuse, and error handling.
69. Demonstrate accidental suppression by catching without re-raising around the yield point. Add a regression test before repairing it.
70. Implement a single-use manager state machine and tests for double entry, exit-before-entry, double exit, and reuse.
71. Determine whether a selected standard-library manager is reusable and re-entrant by reading its contract; design experiments only for facts the contract leaves open.
72. Use <code>nullcontext</code> to accept either a path or caller-owned text stream. Verify that only acquired resources close.
73. Restrict <code>suppress(FileNotFoundError)</code> to one unlink call. Demonstrate how a larger scope hides an unrelated missing-file bug.
74. Acquire zero, one, and five files dynamically through <code>ExitStack</code>. Inject failure during the third acquisition and prove reverse-order cleanup.
75. Contrast <code>ExitStack.callback</code> and <code>push</code> by showing which receives exception details and which can suppress.
76. Use <code>pop_all</code> to transfer resource ownership. Document the caller obligation and create a test that detects forgotten closure.
77. Design a transaction manager with explicit commit. Exercise normal no-commit rollback, committed exit, body exception, commit failure, and rollback failure.
78. Analyse why temporarily changing current working directory inside a context manager is unsafe under threads. Replace ambient directory use with explicit paths.

### 11.19.9 Paths and filesystem security

79. Use <code>PurePosixPath</code> and <code>PureWindowsPath</code> to analyse roots, drives, anchors, names, suffixes, and parents for ten edge-case strings.
80. Show that joining an absolute user component can discard a trusted root. Add lexical rejection, then list attacks lexical rejection still does not solve.
81. Create a symbolic-link fixture showing why lexical cancellation of <code>link/..</code> can differ from filesystem resolution.
82. Compare <code>absolute</code>, <code>resolve(strict=False)</code>, and <code>resolve(strict=True)</code> on existing, missing, linked, and cyclic paths under a recorded Python version.
83. Create two hard links where supported. Compare pathname strings, <code>samefile</code>, metadata identity, contents after mutation, and behaviour after replacing one name.
84. Demonstrate a TOCTOU race in a controlled test by replacing a path between <code>exists</code> and <code>open</code>. Rewrite the requirement around one acquired handle.
85. Compare <code>path.stat</code> and <code>os.fstat</code> after pathname replacement. State precisely which object each observed.
86. Create files under several requested POSIX modes and a controlled umask. Record actual results and explain access-control mechanisms not covered by mode bits.
87. Build a deterministic directory inventory and inject disappearance of an entry during traversal. Choose fail-fast or partial-results semantics.
88. Design cycle-safe recursive traversal when following directory symbolic links is required. Define filesystem-boundary, depth, and entry-count policies.
89. Compare apparent and allocated sizes for a sparse file on a supporting filesystem. Explain why the result is not portable.
90. Stage a destination in a different filesystem and attempt replacement. Identify the failure/fallback behaviour of each API tested.
91. Specify a safe recursive-delete interface that refuses roots, empty targets, project roots, and paths outside one expected parent. Include a dry-run representation and recovery policy.
92. Demonstrate why unlinking an open file has platform-dependent behaviour. Write tests conditional on documented capabilities rather than operating-system names alone.
93. Build a one-component handle-relative opener on a supporting POSIX platform. Reject separators and links, inspect the opened type, and document remaining hard-link/device risks.
94. Construct filenames that differ by case and Unicode normalisation on available filesystems. Record whether they collide and classify the result as empirical.
95. Pass a filename containing spaces and shell metacharacters to an external program through an argument vector. Contrast with unsafe string interpolation without executing destructive content.
96. Design a defensive archive extraction policy covering parent paths, absolute paths, links, devices, expansion ratio, total bytes, file count, permissions, and race resistance.

### 11.19.10 Buffering, atomicity, and durability

97. Derive the simplified batching-time equation in §11.6.1 and identify conditions under which increasing batch size stops helping.
98. Write through a buffered text wrapper to an in-memory binary buffer and observe visibility before write, after write, after flush, and after close.
99. Trace the order of <code>write</code>, <code>flush</code>, file <code>fsync</code>, replace, and directory <code>fsync</code> through injected functions.
100. Implement staged replacement with an explicit state enum rather than a nullable temporary name. Prove that cleanup never deletes a committed destination.
101. Inject failures at every stage of replacement. For each, tabulate old destination, new destination, temporary residue, returned error, and durability knowledge.
102. Explain with a state table why atomic namespace replacement, complete content, durability, and multi-writer exclusion are independent.
103. Design a two-slot crash-recovery format with generations and checksums. Enumerate every interruption point and the recovery decision.
104. Specify a minimal write-ahead log for a key/value update. Define record framing, commit, redo, checksum, checkpoint, and torn-tail recovery.
105. Redesign a two-file configuration into immutable versioned objects plus one manifest commit point. Specify garbage-collection safety.
106. Construct an API result representing not-committed, committed, and visible-but-durability-unconfirmed states. Show how callers handle retries differently.
107. Plan a buffering benchmark with cache state, repetitions, randomised trial order, correctness checks, distribution summary, and environment record.
108. Write recovery point and recovery time objectives for the pipeline. Design a restoration test proving more than replication availability.

### 11.19.11 JSON

109. Produce one example for every Python-to-JSON lossy mapping: tuple/list, non-string key, Decimal, date, bytes, set, aliasing, and custom class.
110. Parse top-level string, number, Boolean, null, array, and object documents. Layer an application rule requiring an object and test diagnostic separation.
111. Reject duplicate object names with <code>object_pairs_hook</code>, including duplicates in nested objects. Preserve source order in the diagnostic.
112. Compare default float decoding with <code>parse_float=Decimal</code> for values such as 0.1 and long decimals. State what each preserves.
113. Design a JSON numeric interoperability profile covering integer magnitude, decimal scale, exponent, non-finite values, and negative zero.
114. Reject Python's non-finite JSON extensions on both input and output. Test all three spellings and internally produced infinities.
115. Compare <code>ensure_ascii=True</code> and <code>False</code> at the Python-string and UTF-8-byte layers. Confirm semantic equality after parsing.
116. Build explicit encode/decode functions for a model containing UUID, UTC timestamp, Decimal, bytes, enum, and optional field. Define every lexical form.
117. Implement strict unknown/missing-field handling and then an additive-compatible variant. Analyse backward and forward compatibility.
118. Write version-1-to-version-2 migration code that changes units without silent rounding. Preserve the original document for audit.
119. Demonstrate that two consecutive <code>dump</code> calls do not make one document. Repair with an array, length prefix, and newline-delimited record format.
120. Use <code>iterencode</code> and measure whether the source graph is already materialised. Design a truly record-streaming alternative.
121. Compare <code>sort_keys=True</code> with the requirements of RFC 8785. List every canonicalisation dimension not supplied by sorting.
122. Threat-model a public JSON parser and implement byte, integer-digit, field-count, depth, and string limits at the earliest feasible layers.

### 11.19.12 CSV

123. Define and register a custom CSV dialect, then argue whether global registration or a local dialect class is safer for a library.
124. Construct a record containing delimiter, quote, CRLF, LF, leading/trailing spaces, and empty fields. Round-trip it under one explicit dialect.
125. Track data-record number, starting physical line, and ending physical line for multi-line records. Test a malformed quoted field.
126. Demonstrate duplicate-header overwrite in <code>DictReader</code>. Implement exact-order and order-independent unique-header policies.
127. Exercise <code>restkey</code> and <code>restval</code> on wide and narrow rows. Decide why a strict importer should reject or retain each.
128. Define column parsers for identifier, optional decimal, Boolean, date, and enum. Do not infer types from quoting.
129. Show the irreversible collision between <code>None</code> and empty string under ordinary <code>csv.writer</code>. Design a reversible schema.
130. Compare <code>QUOTE_MINIMAL</code>, <code>QUOTE_ALL</code>, and other options available in Python 3.12. Test interoperability with one named consumer.
131. Give <code>Sniffer</code> several ambiguous samples and measure inferred dialect/header. Design an interactive confirmation flow rather than trusting the guess.
132. Bound field size, row width, record count, and distinct aggregation keys. Explain the global-state hazard of <code>field_size_limit</code>.
133. Create spreadsheet-targeted malicious-looking cell values in a harmless test. Evaluate consumer-specific import-as-text and transformation policies without executing formulae.
134. Implement a streaming aggregate whose memory is proportional to distinct keys. Add a threshold and an external-sort alternative.
135. Design a CSV export/import conformance suite shared between two independently implemented producers and consumers.

### 11.19.13 Pickle

136. Pickle a graph with shared references and a cycle. Prove equality, identity preservation, and mutation aliasing after restoration.
137. Produce protocol 4 and 5 artefacts and test them under the project's minimum Python. Explain why highest-protocol selection is a deployment policy.
138. Rename a module/class in a controlled package and observe old-pickle failure. Implement and then retire a compatibility migration path.
139. Write versioned <code>__getstate__</code>/<code>__setstate__</code> for trusted historical state. Test missing, extra, invalid, and future versions.
140. Disassemble a benign pickle with <code>pickletools</code> and identify memo, global reference, construction, and state opcodes. Do not load unknown data.
141. Complete the authenticated-pickle envelope with key ID, purpose binding, timestamp, expiry, size bound, and replay identifier. Explain why the producer still needs full trust.
142. Evaluate a restricted unpickler against allowed classes with effectful state methods and oversized primitive graphs. State why process isolation remains valuable.
143. Design an out-of-band protocol-5 envelope binding main stream and ordered buffers with lengths and authentication. Specify ownership/release.

### 11.19.14 Standard-library composition

144. Implement FIFO, LIFO, round-robin, and bounded-history structures with <code>deque</code>. State eviction and empty-operation behaviour.
145. Compare list left-pop and deque left-pop through asymptotic analysis and controlled measurement over increasing sizes.
146. Use <code>Counter</code> for inventory deltas containing negative counts. Define validation before committing a physical-stock view.
147. Demonstrate zero-count storage, unary plus, subtraction, intersection, union, and tie ordering in <code>Counter</code>.
148. Compare <code>defaultdict</code> subscription, <code>get</code>, <code>setdefault</code>, and explicit branching for missing keys and side effects.
149. Build layered settings with <code>ChainMap</code>. Trace lookup, write, deletion, <code>new_child</code>, live parent mutation, and flattening.
150. Compare <code>namedtuple</code>, <code>NamedTuple</code>, frozen dataclass, and ordinary class for one coordinate model.
151. Build an LRU-like cache with <code>OrderedDict</code>, then enumerate correctness/concurrency features supplied by <code>lru_cache</code> that your version lacks.
152. Use <code>chain.from_iterable</code> to flatten batches one level. Test strings, empty batches, and infinite outer input.
153. Demonstrate consumption semantics of <code>islice</code>, <code>takewhile</code>, and <code>dropwhile</code> by inspecting the remaining source.
154. Quantify <code>tee</code> buffering when one branch lags. Repeat with mutable yielded objects and explain shared identity.
155. Use <code>groupby</code> for already-sorted streaming aggregation and compare it with dictionary aggregation of unsorted data.
156. Calculate product, permutation, and combination counts before generation. Enforce a maximum output budget and reject an explosive request.
157. Implement a rolling balance with <code>accumulate</code>, including an initial value. Compare intermediate-output and final-only requirements.
158. Use strict <code>zip</code> to enforce parallel-column length and <code>zip_longest</code> with a unique sentinel to report missing entries.
159. Create a partial callable retaining a mutable argument, expose the aliasing bug, and replace it with an explicit factory or named wrapper.
160. Write a typed decorator using <code>ParamSpec</code>, <code>TypeVar</code>, and <code>wraps</code>. Confirm signature and <code>__wrapped__</code> introspection.
161. Cache a function dependent on a mutable file. Demonstrate staleness, then redesign the key/invalidation policy or remove caching.
162. Show duplicate concurrent computation for a cached miss under a controlled barrier. Explain why internal cache coherence is not once-only execution.
163. Use <code>singledispatch</code> for three nominal types and one abstract base class. Inspect dispatch selection and ambiguous design axes.
164. Define dataclasses exercising keyword-only fields, <code>InitVar</code>, <code>ClassVar</code>, derived <code>init=False</code> state, slots, and frozen validation.
165. Compare <code>asdict</code> with an explicit schema encoder on nested mutable data. Measure allocation and identify type/alias information lost.

### 11.19.15 Integrative and research exercises

166. Implement the full schema-version-2 measurement pipeline from §11.17 as a package with pure core, adapters, CLI, type checking, tests, and documentation.
167. Add an error-accumulation mode that reports at most 100 bad records while continuing syntax-safe parsing. Define whether any output commits when errors exist.
168. Replace in-memory sensor aggregation with SQLite from the standard library. Define transaction, uniqueness, numeric range, cleanup, and crash-recovery semantics.
169. Add a content-addressed immutable output object plus one manifest pointer. Verify hashes during reads and design safe garbage collection.
170. Make the pipeline reproducible across Python 3.12 and the project's newest supported release. Record every version-dependent API and output difference.
171. Port path and durability integration tests to Linux, macOS, and Windows. Produce a matrix of documented guarantees, observations, and unsupported claims.
172. Threat-model the pipeline under a malicious local user who can modify the input directory but not the process. Redesign authority and race resistance.
173. Write a mini-RFC for the CSV input and JSON output: grammar, encoding, schema, limits, versions, errors, security, canonical examples, and compatibility.
174. Conduct a structured code review using the Chapter 11 claim ledger. Require evidence for every claim containing “atomic”, “safe”, “exact”, “thread-safe”, or “durable”.
175. Integrate Chapters 1–11 by tracing one input byte from storage hardware, kernel and buffers, through UTF-8/CSV parsing, object allocation and function calls, into aggregation, JSON encoding, buffered output, replacement, and persistence. At every transition name the representation, owning component, possible failure, and evidence source.
