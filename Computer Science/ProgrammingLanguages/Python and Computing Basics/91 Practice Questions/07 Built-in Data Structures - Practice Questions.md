# 7.17 Exercises

### 7.17.1 Lists and tuples

1. Trace list capacity conceptually across twenty appends. Mark which steps may require (O(n)) copying and explain the amortised claim without assuming an exact CPython growth formula.
2. Compare total work for removing every item with `pop(0)` and with `deque.popleft()`. Express the list shift sum.
3. Construct a shallow-copy graph with three nesting levels. Mutate each level separately and predict which observers change.
4. Design a tuple record and explain when named fields would produce a better interface.
5. Show why repeated tuple concatenation can be quadratic and replace it with a list-build/finalise design.

### 7.17.2 Dictionaries and sets

6. Implement a frequency table from an iterable without using `Counter`, then state expected and worst-case complexity including equality cost.
7. Construct a unique sentinel to distinguish missing key from a present `None` value.
8. Explain why a mutable object whose hash depends on changing state cannot safely remain a dictionary key.
9. Model directed and undirected graph edges using tuples and frozensets respectively; state the invariant each representation enforces.
10. Use set operations to compare required, granted, and forbidden permissions. Define every resulting set semantically.
11. Demonstrate that `dict.fromkeys` reuses one mutable value and repair the design.

### 7.17.3 Strings and costs

12. Build a comma-separated representation of 100,000 values using collection-and-join. Explain the cost hazard of repeated immutable concatenation.
13. Give inputs for which `split()` and `split(" ")` intentionally produce different data models.
14. Separate code-point count, grapheme count, and byte count for a Unicode example.
15. Explain why substring-search complexity cannot be stated only from the haystack length without naming the needle and algorithmic assumptions.

### 7.17.4 Structure selection

16. Choose structures for: an undo stack; a first-in-first-out work queue; unique visited nodes; an ordered ledger; lookup from account ID to balance; immutable undirected edges. Defend operations and invariants.
17. Design a least-recently-used cache using a mapping plus an ordering structure. State all cross-structure invariants before writing operations.
18. Estimate shallow and reachable memory for a structure with shared elements. Identify double-counting hazards.

### 7.17.5 Integrated exercise

19. Implement the event-window case study without using the supplied code. Add global unique-tag tracking for the retained window. Define behaviour for duplicate IDs, zero limit, empty tags, eviction, and failed validation. Provide a representation proof, per-operation cost table, mutation-failure analysis, and tests that check cross-container invariants after every transition.

### 7.17.6 Representation and cost foundations

20. For each of list, tuple, dictionary, set, frozenset, string, bytes, bytearray, range, and deque, state order, multiplicity, addressing, mutability, and hashability. Separate type-wide claims from conditional claims.
21. Give three collections with equal printed content but different alias graphs. Draw their reference graphs and predict the result of one mutation through each available alias.
22. Define an abstract data type for a bounded stack independently of Python. Then give list- and deque-backed representations and prove that each operation refines the abstract contract.
23. Construct examples showing that \(O(1)\), \(\Theta(1)\), expected \(O(1)\), and amortised \(O(1)\) are not interchangeable phrases.
24. Derive the total shift count for inserting \(n\) values repeatedly at index zero of a list. Compare it with append followed by one reversal.
25. Suppose hashing a key of length \(m\) costs \(\Theta(m)\). Rewrite the ordinary dictionary lookup complexity statement in terms of table population \(n\), key length \(m\), collision count \(c\), and equality cost \(E\).
26. Find an operation whose output size alone establishes an \(\Omega(n)\) lower bound even if every lookup is constant. Explain why an implementation trick cannot violate that bound.
27. Design a benchmark that compares list and deque FIFO draining. Specify warm-up, population sizes, setup exclusion, repetitions, summary statistic, environment metadata, and hypotheses before measurement.
28. Explain why measuring only already sorted integer lists cannot support a general claim about sorting dictionaries with expensive key extraction.

### 7.17.7 Lists, slices, and mutation contracts

29. Derive the normalized index for every valid negative index in a list of length six. State the first invalid negative and positive indices.
30. Predict and verify ten slices using omitted endpoints, negative endpoints, positive and negative steps, and a step whose magnitude exceeds the list length. Use <code>slice.indices</code> to expose normalization.
31. Implement a function that replaces a slice while preserving a fixed-length invariant. Reject replacements whose cardinality differs before mutating.
32. Show that extended-slice assignment with a non-unit step imposes a length equality constraint. Explain why arbitrary length change would make target positions ambiguous.
33. Compare <code>append(iterable)</code> and <code>extend(iterable)</code> on strings, generators, self-extension, and an iterable that raises after three values. Record partial effects.
34. Construct an equality method that raises on one comparison and use it with list <code>remove</code>. Determine which state changes, if any, precede the error.
35. Implement stable in-place removal of elements satisfying a predicate with read and write indices. State and prove a prefix invariant. Decide what happens if the predicate raises.
36. Implement an unstable in-place removal algorithm allowed to swap with the last element. Compare its asymptotics and ordering contract with stable compaction.
37. Give three APIs that filter a caller-supplied list: returning a new list, replacing the caller’s contents, and yielding lazily. Document aliasing, error timing, and memory for each.
38. Model a stack with a list. Add a maximum depth and define whether overflow is detected before or after constructing the pushed value.
39. Demonstrate why using <code>pop(0)</code> for breadth-first graph traversal can make total queue work quadratic. Repair it with a deque.

### 7.17.8 Tuples, records, and immutable boundaries

40. Write syntactically distinct examples of grouping parentheses, an empty tuple, a one-element tuple, a packed tuple, and tuple unpacking. Identify which commas construct tuple displays.
41. Construct a tuple that is unhashable, a tuple that is hashable but reaches a mutable object through a custom component, and a deeply immutable tuple. State the exact guarantees of each.
42. Compare a positional tuple, named tuple, frozen dataclass, and mapping for an employee record. Analyse field discoverability, runtime validation, mutability, hashability, evolution, and serialisation.
43. Demonstrate that augmented assignment to a mutable object inside a tuple can mutate the object and then raise during tuple item assignment. Trace the resulting state and explain why the apparent contradiction is not rollback.
44. Design a function returning zero, one, or many logical results without confusing tuple packing with result cardinality. Defend the interface.
45. Use a tuple as a composite dictionary key. Define normalization for every component and demonstrate a collision caused by Python numeric equality that the domain may reject.

### 7.17.9 Dictionaries, keys, and live views

46. Build a dictionary from a sequence containing three duplicate keys. Record which key object representative, value, and insertion position survive. Separate guaranteed behaviour from CPython display observations.
47. Create a user-defined key class whose equality says two objects are equal but whose hashes differ. Demonstrate lookup failure and explain which contract the class violates. Then repair it.
48. Create a key whose hash depends on mutable state, insert it, mutate it, and investigate membership. Do this only in an isolated experiment; explain why observed recovery after restoring state is not a usable design.
49. Implement frequency counting with subscription/exception, <code>get</code>, <code>setdefault</code>, and <code>defaultdict</code>. Compare absent-key semantics and factory evaluation.
50. Use a unique sentinel to distinguish absent key, present <code>None</code>, present false, and present zero. Write tests for every case.
51. Demonstrate key-view, value-view, and item-view membership. Give expected costs and explain why identical <code>in</code> syntax invokes different strategies.
52. Retain an items view after deleting the original mapping name. Use a weak reference where possible or another observation to explain lifetime. Avoid claiming an implementation-independent internal pointer layout.
53. Compare live view, shallow tuple snapshot, shallow dictionary copy, and application-specific deep immutable snapshot under nested value mutation.
54. Show that item-view set intersection works for hashable values and fails for list values while direct item membership can succeed. Explain the operation-specific hash requirement.
55. Demonstrate value-view equality behaviour. Implement ordered, set-like, and multiset-like comparisons explicitly, and state what information each ignores.
56. Filter a dictionary by snapshot mutation, planned-key deletion, and replacement comprehension. Test alias observers and injected predicate failure for each contract.
57. Implement a dictionary subclass with <code>__missing__</code>. Compare its subscription, <code>get</code>, membership, and <code>setdefault</code> behaviour.
58. Use dictionary union and update with overlapping keys. State value precedence and insertion-position results for existing and new keys.
59. Design a read-only dynamic configuration interface using <code>MappingProxyType</code>. Demonstrate both its protection and its inability to freeze the underlying mapping or nested values.

### 7.17.10 Sets, equivalence, and algebra

60. Prove the equivalence of the two definitions of symmetric difference. Then test both expressions on Python sets and compare result types for mixed set/frozenset operands.
61. Construct two incomparable sets. Explain why subset relations are a partial rather than total order and why sorting sets by subset is not a general topological sort.
62. For three effectful set-producing functions, identify which algebraic rewrites preserve final membership but change effects. State the conditions under which the rewrites become valid.
63. Compare <code>remove</code>, <code>discard</code>, and <code>pop</code> as contracts. Write tests that avoid depending on arbitrary pop order.
64. Implement ordered first-occurrence deduplication using a set plus list, a dictionary, and a generator. Compare result representation, laziness, and retained memory.
65. Prove that exact deduplication over an unbounded stream with arbitrary historical repeats may require memory proportional to the number of distinct observed values. State any assumptions.
66. Demonstrate numeric equality collapse among integer, Boolean, float, Decimal, and Fraction values where their contracts permit. Build an explicit tagged representation when category matters.
67. Investigate identical and distinct NaN objects in sets. State only observed/version-qualified behaviour, then design a canonicalization policy.
68. Represent undirected edges with frozensets. Validate simple edges, self-loops, and hyperedges. Compare neighbour-query costs with an adjacency mapping.
69. Implement a multiset with a dictionary of positive counts. Define insertion, deletion of one occurrence, deletion of all occurrences, union under maximum counts, and addition under summed counts.
70. Use counters rather than a set to maintain exact active features under sliding-window eviction. Prove the zero-deletion invariant.
71. Given sets of licensed, trained, suspended, and supervised staff, write and simplify an eligibility expression. Translate the result into a truth-table-like set partition.

### 7.17.11 Unicode strings and byte boundaries

72. For five strings containing ASCII, a precomposed accent, a decomposed accent, an emoji modifier, and a joined family emoji, record code-point length, UTF-8 byte length, and rendered grapheme expectation. Explain why terminal width is another measure.
73. Use <code>ord</code>, <code>chr</code>, <code>repr</code>, and named Unicode escapes to trace source spelling into runtime values. Distinguish literal length from value length.
74. Demonstrate that code-point reversal can detach combining marks. Research or use a suitable grapheme segmentation library in an optional branch and compare the result, recording the Unicode version.
75. Derive the quadratic copied-volume sum for repeated concatenation of variable-length pieces. Implement join-based and streaming-output alternatives.
76. Give five examples where <code>find</code> tested by truthiness fails. Include a match at zero and absence at minus one. Repair each interface.
77. Compare <code>partition</code>, one-split <code>split</code>, and unrestricted <code>split</code> for a key/value grammar whose value may contain delimiters.
78. Enumerate differences among <code>split()</code>, <code>split(" ")</code>, <code>splitlines()</code>, and <code>split("\n")</code> over leading, trailing, repeated, CRLF, and Unicode whitespace.
79. Construct defects caused by <code>lstrip</code> and <code>rstrip</code> used as prefix/suffix removers. Explain the character-set algorithm.
80. Compare NFC, NFD, NFKC, and NFKD on representative text. Identify which distinctions compatibility forms erase and state a domain where that loss is unacceptable.
81. Design a caseless normalized lookup that preserves original spelling. Test canonical equivalence, German sharp S, empty input, internal whitespace, and a policy collision.
82. Compare <code>isdecimal</code>, <code>isdigit</code>, <code>isnumeric</code>, and <code>int</code> acceptance. Explain why pre-validation with a broader predicate can still fail parsing.
83. Validate generated Python identifiers using <code>isidentifier</code> and the keyword module. Include a Unicode identifier, a keyword, a soft-keyword context, and a visually confusable pair.
84. Encode the same text as UTF-8, UTF-16 with a specified byte order, and a legacy single-byte codec where possible. Record lengths, byte-order metadata, failures, and round-trip conditions.
85. Compare strict, replace, ignore, and backslash-replacement codec error policies. Give one appropriate and one dangerous use for lossy handling.
86. Implement the parser inverse of the escaped-field renderer in §7.9.24. Model normal and escaped states, reject incomplete/unknown escapes, and prove <code>parse(render(fields)) == fields</code> for valid fields.
87. Build a binary length-prefixed frame parser that handles partial input. Bound length before allocation, separate byte and text errors, and retain any unconsumed suffix.
88. Demonstrate that code-point lexicographic sorting differs from a chosen human collation. Document the external collation implementation and version if used.

### 7.17.12 Representation choice and ordering

89. Choose among list, deque, tuple, range, bytes, bytearray, memoryview, and generator for twelve workloads. For each, state why the nearest alternative is worse.
90. Demonstrate range equality for distinct parameter triples representing the same sequence. Derive the represented length for positive and negative steps.
91. Compare a one-million-element range and its list materialisation using shallow size, reachable-size reasoning, construction time, and iteration workload. Do not report a single number without environment metadata.
92. Use a memoryview slice to edit a bytearray and show why resizing is restricted while the view exists. Define view lifetime with a context manager.
93. Implement a bounded queue twice: automatic deque eviction and explicit eviction returning the removed value. Give a requirement that distinguishes the contracts.
94. Sort records using compound keys, stable multi-pass sorting, and a manually decorated representation. Prove result equivalence under stable pure keys.
95. Construct a missing-last optional key for integers, strings, and dates. Explain why an arbitrary placeholder is safe only behind a discriminating first component.
96. Show the difference between <code>reverse=True</code> and reversing an ascending stable result on equal-key records.
97. Define a total-order key for finite floats plus infinities, NaNs, and signed zeros. State every category and tie policy.
98. Compare full sorting, <code>min</code>/<code>max</code>, and heap-based top-k for a parameterized \(n\) and \(k\). Include key-extraction cost and output order requirements.
99. Maintain a sorted list with bisect under repeated random insertions. Separate logarithmic search comparisons from linear element movement.
100. Design a reproducible ranking when source records originate from a set. Add an immutable unique tie-breaker and explain remaining environmental dependencies.
101. Outline an external merge sort for records larger than memory. Define run format, stability token, file cleanup, resource bounds, and recovery after a failed merge.

### 7.17.13 Nested structures and graph invariants

102. For a nested structure, draw tree, DAG, and cyclic variants with equal-looking leaves. Predict a naive recursive traversal’s behaviour on each.
103. Extend the cycle-safe container counter to include tuples, sets, object attributes, and slots under an explicit policy. Document references it intentionally excludes.
104. Validate a rectangular matrix and multiply compatible matrices using triple loops. State shape, index, arithmetic, and aliasing invariants.
105. Show why an empty list-of-lists cannot distinguish every zero-row matrix shape. Design a class or tuple representation that stores shape explicitly.
106. Implement nested lookup that distinguishes unknown outer key, unknown inner key, present <code>None</code>, and present zero. Compare exceptions, tagged results, and sentinels.
107. Compare nested <code>setdefault</code>, defaultdict factories, and explicit construction when the value factory is costly or can fail.
108. Build an inverted index and its forward record store. Implement insertion, deletion, and term change while checking the bidirectional invariant.
109. Represent a directed graph with adjacency sets. Validate closed node population and no self-loops. Implement edge insertion with the strong guarantee for domain failures.
110. Represent an undirected graph and prove adjacency symmetry after insertion and deletion. Inject a failure between the two mutations and design recovery.
111. Compare normalized primary state plus derived indexes with storing only denormalized nested records. Analyse lookup, update, memory, and rebuild costs.
112. Implement immutable domain records inside mutable indexes. Demonstrate how replacement rather than in-place field mutation protects index consistency.

### 7.17.14 Memory and ownership experiments

113. Define shallow, reachable, retained, resident, and peak size for one shared graph. Give a case where each pair differs.
114. Measure shallow sizes of empty and growing lists, tuples, dictionaries, sets, strings, bytes, and bytearrays on a recorded CPython build. Infer capacity changes cautiously and label them implementation observations.
115. Extend the selected reachable-size walker with a pluggable edge policy. Test sharing and cycles, and explain why it still cannot infer economic ownership.
116. Construct a small dominator graph and calculate retained sizes manually. Then add a second root and recompute them.
117. Use tracemalloc snapshots to find a deliberately unbounded cache. Separate net retained allocations from cumulative temporary traffic.
118. Demonstrate a traceback or suspended generator retaining a large local object. Remove the retention path and compare snapshots.
119. Compare list-of-integers and packed-array representations. Include shallow/reachable memory, construction, summation, mutation, overflow, and interoperability.
120. Design a cache bounded by both entry count and estimated byte weight. State what the estimate omits and how sharing complicates charging.
121. Explain why deallocation need not reduce process resident memory immediately. Design measurements that distinguish live Python allocations, allocator retention, and native memory.

### 7.17.15 Concurrency and atomicity

122. Enumerate bytecode or conceptual steps in a dictionary increment, then construct a lost-update schedule. Repair it with one invariant-owning lock.
123. Give a key class whose hash or equality re-enters a container operation. Analyse why a lock choice can deadlock and redesign the callback boundary.
124. Define live, fail-fast, shallow snapshot, deep immutable snapshot, and locked-iteration semantics for one registry API. Implement two and test concurrent mutation expectations.
125. Design a per-key async request-coalescing cache. Specify the state for absent, in progress, succeeded, failed, and cancelled entries.
126. Compare a local dictionary, manager proxy, shared-memory array, and transactional database for cross-process counters. State compound-operation and failure semantics.
127. Implement a producer/consumer protocol with <code>queue.Queue</code>. Define sentinel shutdown, capacity backpressure, task completion, worker failure, and join behaviour.
128. Construct a lock-order cycle involving two indexed structures. State a global acquisition order and prove the cycle is eliminated under that discipline.
129. Design immutable snapshot publication with a version number. Explain which claims rely on a lock and which rely on deep immutability.
130. Review a claim that “dict operations are thread-safe.” Rewrite it into a versioned, operation-specific, observer-specific statement—or reject it as unsupported.

### 7.17.16 Integrated mastery projects

131. Complete the EventWindow implementation, including exact active tags, immutable snapshots, invariant checks, and the simple reference oracle. Generate thousands of random transitions and compare after every step.
132. Add arbitrary deletion to EventWindow. Analyse the deque bottleneck and compare direct removal, lazy tombstones, linked ordering, and full reconstruction.
133. Change EventWindow to a byte budget. Define a deterministic record-weight function, reject individually oversized events, and evict repeatedly. Prove termination.
134. Make EventWindow safe for concurrent reads and writes with snapshot iteration. State the lock-protected invariant, callback restrictions, and exception guarantees.
135. Persist the event window to JSON and restore it. Define order, schema version, Unicode policy, duplicate handling, counter reconstruction, atomic file replacement, and corrupt-input behaviour. Chapter 11 supplies the I/O mechanisms; use this exercise to state the structure contract now.
136. Build a word concordance from UTF-8 documents: strict decoding, versioned normalization, token policy, ordered document IDs, term frequencies, and line positions. Provide cost and memory models in terms of bytes, code points, tokens, and unique terms.
137. Build a dependency graph for a small package. Preserve node insertion order for reporting, use sets for edges, detect unknown nodes and cycles, and produce a deterministic topological order with explicit tie-breaking.
138. Design a least-recently-used cache using a dictionary plus ordering structure. Define get/put/evict transitions, representation invariant, capacity zero policy, exception safety, byte versus count bounds, and concurrent access.
139. Build an external-sort pipeline for a data file too large to memory. Include strict parsing, bounded chunks, stable global ordering, temporary-file cleanup, checksum or validation, and atomic final publication.
140. Write a chapter dossier for one original application structure. It must include the abstract data type, representation alternatives, formal invariant, proof of every mutator, expected/worst/amortised costs, alias graph, Unicode/byte boundaries, memory ownership, exception guarantee, concurrency model, tests, benchmark plan, and likely requirement changes.
