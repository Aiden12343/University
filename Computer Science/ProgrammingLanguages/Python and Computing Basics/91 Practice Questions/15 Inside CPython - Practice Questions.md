# 15.22 Exercises

### 15.22.1 Compiler pipeline

1. Tokenise and parse ten constructs, including a comprehension, pattern match, closure, and exception handler. Explain load/store contexts.
2. Use `symtable` to classify locals, globals, cells, and free variables in nested code.
3. Compare `co_consts`, `co_names`, `co_varnames`, `co_freevars`, and function defaults for several definitions. Treat all ordering observations as version-scoped.
4. Demonstrate constant folding changes through disassembly without turning the observed optimisation into a language guarantee.

### 15.22.2 Bytecode and frames

5. Disassemble a loop, function call, attribute access, and `try` statement on the selected CPython version. Map instructions to semantic operations without claiming one-to-one native code.
6. Trace the evaluation stack for a nested expression and verify stack effects with supported `dis` interfaces.
7. Inspect frame locals and call relationships; then demonstrate how retaining a frame retains other objects.
8. Compare bytecode before and after warm execution where adaptive display APIs permit; document version flags.

### 15.22.3 Memory management

9. Construct acyclic and cyclic unreachable graphs. Observe collection with `weakref` and `gc` without depending on exact automatic timing.
10. Use `gc.get_referrers` only in a controlled diagnostic and explain how the inspection itself changes references.
11. Build a reachable unintended cache leak and distinguish it from allocator-retained free memory.
12. Design a finaliser-resurrection experiment, then explain why it is not a resource-management pattern.

### 15.22.4 Native boundary

13. Audit a small C API pseudocode function for borrowed/new reference errors on every success and failure path.
14. Compare full C API and stable-ABI distribution implications.
15. Design an extension interface batching work across the boundary and state GIL/free-threaded obligations.

### 15.22.5 Integrated capstone

16. Select one Python function involving closures, iteration, exceptions, attribute access, and mutation. Produce a complete dossier from source bytes through AST, symbols, code objects, bytecode, frames, object protocol dispatch, reference ownership, exception path, output boundary, and eventual reachability. Every sentence must be labelled language guarantee, documented CPython interface, private version-specific mechanism, or experiment.

### 15.22.6 Evidence, versions, and experiment design

17. Produce an implementation report for two available CPython installations. Explain which reported differences can change semantics, public introspection, private layout, performance, or only diagnostic text.
18. Take one claim from this chapter and rewrite it four times as a language guarantee, documented-interface claim, private-mechanism claim, and empirical observation. State what evidence could support each form.
19. Design a minimal experiment testing whether integer object identity is reused. Explain why neither a positive nor a negative result licenses numeric identity comparison.
20. Compare release and debug builds, if available, using one allocation-heavy workload. Record build flags and explain why timing results are not directly interchangeable.
21. Write a JSON schema for a reproducibility dossier containing executable identity, command, environment, source digest, platform, optimisation mode, imported extensions, and result. Implement a validator using only the standard library.
22. Select an internal statement found in an older Python article. Verify it against CPython 3.12 documentation/source and classify it as retained, revised, removed, or never guaranteed.
23. Construct two distinct hypotheses explaining one timing change after warm-up. Design measurements capable of rejecting at least one rather than merely repeating the timing.
24. Show how printing an object during measurement can execute arbitrary <code>__repr__</code> code. Redesign the observer to capture type and identity without invoking representation.
25. Explain why a trace-enabled run and an untraced run are different experimental treatments. Measure the overhead distribution across at least 30 repetitions and report median and a robust spread statistic.
26. Write a one-page internal-investigation protocol that another student can reproduce. Include negative knowledge and explicit stopping criteria.

### 15.22.7 Source decoding, tokens, grammar, and ASTs

27. Create UTF-8, UTF-8-with-BOM, and one declared legacy-encoding source byte string. Use <code>tokenize.detect_encoding</code> and explain every returned consumed line.
28. Construct a source file whose declared codec conflicts with a byte-order mark. Record the exact failure phase and exception without treating its message as stable.
29. Tokenise a multiline expression with implicit parenthesis continuation, a backslash continuation, comments, indentation, and a triple-quoted string. Distinguish physical and logical lines.
30. Use <code>tokenize.untokenize</code> on a transformed token stream. Prove token type/string round-tripping, then list formatting properties not preserved.
31. Parse one expression under <code>exec</code>, <code>eval</code>, and <code>single</code> where valid. Compare root nodes and compiled behaviour.
32. Walk targets for simple assignment, unpacking, starred assignment, attribute assignment, subscription assignment, deletion, and assignment expression. Tabulate every <code>Load</code>, <code>Store</code>, and <code>Del</code> context.
33. Build an AST transformer that renames only load uses of one name while preserving assignment targets. Demonstrate why changing all <code>Name</code> nodes is semantically different.
34. Add source locations to a constructed AST using <code>copy_location</code>, <code>increment_lineno</code>, and <code>fix_missing_locations</code>. Test resulting traceback spans.
35. With non-ASCII identifiers preceding an expression, compare Unicode character indices, UTF-8 byte offsets, and <code>ast.get_source_segment</code>. Explain the discrepancy.
36. Compare the ASTs of operator precedence altered by parentheses, chained comparisons, Boolean short-circuiting, and conditional expressions. Draw their evaluation-order implications.
37. Parse pattern-matching cases with capture, value, sequence, mapping, class, wildcard, and guard patterns. Identify which names can become bindings.
38. Write a structural AST linter for one narrowly stated rule. Test false positives/negatives and explain why it must not execute untrusted code.
39. Attempt to design an AST allow-list sandbox, then document at least ten remaining capability or denial-of-service paths. Do not deploy or execute hostile payloads.
40. Starting from bytes, produce a report that separates decoding error, token error, parse error, compiler validation error, and runtime error with one safe example of each.

### 15.22.8 Symbol tables and lexical binding

41. Use <code>symtable</code> to inventory parameters, locals, globals, nonlocals, imports, assignments, references, free variables, and nested namespaces in one module.
42. Construct five variations of read-before-conditional-assignment. Predict <code>UnboundLocalError</code> versus <code>NameError</code> before running them.
43. Compare ordinary loop targets, comprehension targets, exception-handler targets, pattern captures, and <code>with</code> targets after their suites. Relate lifetime to scope.
44. Build sibling getter/setter closures sharing a cell. Prove identity of the cell and independence from a second factory invocation.
45. Demonstrate late binding in a loop with lambdas. Repair it once with defaults and once with another factory scope; explain why the mechanisms differ.
46. Compare <code>global</code> and <code>nonlocal</code> by compiling valid and invalid declarations. Map each error to a lexical constraint.
47. Inspect <code>co_cellvars</code>, <code>co_freevars</code>, and <code>__closure__</code> for a three-level nesting where a middle function forwards but does not otherwise use a binding.
48. Show that a method’s unqualified name does not search its class dictionary. Contrast explicit class/instance attribute access and the <code>__class__</code> cell.
49. Investigate a comprehension inside a class body that refers to a class-local name. Explain behaviour through code blocks rather than memorised exception text.
50. Compile code passed to <code>exec</code> with explicit global/local dictionaries. Explain why it cannot retroactively add a statically addressed fast local.
51. Compare name resolution in a function body, class body, annotation, comprehension, and <code>eval</code> call under CPython 3.12. Flag every version-sensitive annotation rule.
52. Integrate Chapters 8 and 15: write a closure-based state machine, prove its transitions, inspect its cells, and redesign it as a class. Compare ownership and introspection.

### 15.22.9 Code objects and compiler metadata

53. Inventory every public <code>co_*</code> attribute on three code objects. Classify each as semantic aid, diagnostic metadata, or private-format exposure.
54. Show one code object shared by multiple function objects with different globals, defaults, names, and closure cells. State which modifications affect which calls.
55. Recursively extract nested code objects from <code>co_consts</code> without assuming tuple positions. Produce their qualified-name tree.
56. Compare <code>co_consts</code> under optimisation levels 0, 1, and 2 for assertions, docstrings, literal arithmetic, and unreachable-looking code. Separate documented effects from observations.
57. Demonstrate why a mutable list display is constructed at call time while immutable literal components can occur in <code>co_consts</code>.
58. Map <code>co_names</code> entries to their disassembled instruction contexts and show that membership alone does not distinguish globals, attributes, imports, or methods.
59. Reconstruct a semantic signature from argument-count fields, flags, local-name metadata, defaults, and keyword defaults; compare it with <code>inspect.signature</code> and list failure cases.
60. Decode named <code>co_flags</code> through <code>inspect.CO_*</code> constants for ordinary, variadic, generator, coroutine, and asynchronous-generator functions.
61. Compare <code>co_stacksize</code> for expressions of increasing nesting. Explain why source nesting and maximum evaluation depth need not be proportional.
62. Use <code>co_positions</code> and <code>dis.Instruction.positions</code> to associate instructions with a multiline expression. Account for absent and repeated ranges.
63. Use <code>code.replace</code> to change only a diagnostic name. Verify immutability and explain why changing code bytes or exception tables would demand stronger invariants.
64. Attempt positional <code>types.CodeType</code> construction only in an isolated experiment. Record the signature and show why it is version-coupled; do not ship the constructed object.
65. Compare a module, class-body, function, lambda, comprehension, and generator code object. Identify flags, names, and nesting without claiming cross-version stability.
66. Integrate Chapters 10 and 15: compile the same module source under two filenames and package contexts. Explain which metadata affects tracebacks, imports, or semantics.

### 15.22.10 Bytecode, stacks, and specialisation

67. Use structured <code>dis.Instruction</code> records to serialise disassembly without parsing formatted columns. Include positions and jump targets.
68. Display cache entries with and without <code>show_caches</code>. Explain why raw offsets cannot be interpreted as consecutive visible instructions.
69. Trace evaluation-stack states for arithmetic, a nested call, unpacking assignment, and a list construction. Mark ownership conceptually at every push/pop.
70. Use <code>dis.stack_effect</code> for all instructions in a straight-line function. Then explain why summing effects in display order fails for a branching function.
71. Construct a control-flow graph for <code>if</code>/<code>else</code>, a loop with <code>continue</code>, and a return. Propagate stack depths and verify compatible joins.
72. Disassemble <code>try</code>/<code>except</code>/<code>finally</code> and annotate exception-table edges absent from ordinary linear fall-through.
73. Compare source-line and fine-position mappings for a line containing several failing expressions. Relate the result to traceback highlighting.
74. Warm integer addition, string addition, attribute access, global lookup, and a method call. Record adaptive disassembly but assert only semantic outputs.
75. After warming one type family, supply a different valid family. Observe specialisation, miss, or deoptimisation state and state why the transition is not guaranteed.
76. Introduce a user-defined <code>__add__</code> that logs and returns <code>NotImplemented</code>; implement reflected addition on the other operand. Trace dispatch order.
77. Show that attribute-load bytecode can call a descriptor. Include success, descriptor-raised exception, and instance-dictionary cases.
78. Compare bytecode for <code>obj.method(x)</code> with separately storing <code>method = obj.method</code> before calling. Explain bound-method allocation as an observation.
79. Demonstrate that one iteration instruction can run arbitrary <code>__next__</code> code and raise. Refute bytecode-level atomicity.
80. Compare CPython 3.11 and 3.12 disassembly from recorded environments if available. Identify at least five differences and no false semantic conclusions.
81. Correlate Python disassembly with a native profiler for one arithmetic workload. State why bytecode counts do not predict machine-instruction counts.
82. Write a bytecode analyser that rejects unsupported interpreter cache tags before interpreting instruction patterns. Test the rejection path.
83. Integrate Chapters 12–15: build a regression test that checks language behaviour, stores optional diagnostic disassembly, but does not fail merely because opcodes change.

### 15.22.11 Function construction, frames, and suspension

84. Instrument definition-time defaults, decorator expression evaluation, decorator application, annotation evaluation, and body calls. Produce the exact event order for CPython 3.12.
85. Inspect <code>__defaults__</code> and <code>__kwdefaults__</code>, then replace them deliberately in an isolated test. Explain how omitted-argument behaviour changes.
86. Demonstrate a mutable-default defect with a failing test, then repair it with <code>None</code> and a unique sentinel. State when each sentinel is appropriate.
87. Apply two decorators that use <code>functools.wraps</code>. Follow the <code>__wrapped__</code> chain and compare object identity, signature, closure, and code.
88. Create a decorator returning a callable instance rather than a function. Explain why the defined name need not have <code>__code__</code>.
89. Construct two functions from one code object using <code>FunctionType</code>. Vary globals and show why incompatible closure length is rejected.
90. Snapshot an active frame’s locals without retaining the frame. Write a test using a weak reference to a large local holder to detect accidental retention.
91. Demonstrate that caller frames do not form lexical scope by trying, and failing, to resolve a caller-local name in a globally defined callee.
92. Inspect <code>f_back</code> through three controlled calls. Explain why external runner frames must not be asserted.
93. Compare recursive and iterative factorial implementations for Python frames, evaluation-stack requirements, error behaviour, and asymptotic space.
94. Inspect generator states before first iteration, at suspension, after <code>throw</code>, after <code>close</code>, and after exhaustion.
95. Show which generator locals remain live while suspended using weak references. Release the generator and verify eventual collection without assuming unforced timing.
96. Trace <code>yield from</code> across an outer and inner generator, including returned value and exception propagation. Map suspended frames.
97. Create an asynchronous coroutine chain and inspect coroutine states without leaving pending tasks. Compare awaiting links with ordinary caller frames.
98. Integrate Chapters 6, 8 and 15: implement an iterator, generator, and async iterator for one domain; compare code objects, frame lifetime, and cleanup.

### 15.22.12 Evaluator state and exceptions

99. Extend the miniature stack interpreter with locals, conditional jumps, comparison, and explicit errors. Define and test its stack invariants.
100. Introduce reference-owning wrapper objects into the miniature interpreter. Test that every success/error path releases them exactly once under a simulated ledger.
101. Draw runtime, interpreter, thread-state, frame-chain, and evaluation-stack relationships for a two-thread program. Mark which edges are version-specific.
102. Compare Python call depth with native call depth conceptually for ordinary interpreted calls and a recursively implemented C extension helper.
103. Install a bounded trace function with exception-safe restoration. Measure frame materialisation/retention and demonstrate a leak caused by storing frames.
104. Implement the same call counter with <code>sys.setprofile</code> and, where available, <code>sys.monitoring</code>. Compare event coverage and overhead.
105. Test signal handling latency during pure Python work and during a cooperative versus uncooperative native call available in a safe library. Explain platform limits.
106. Write C API pseudocode for a pointer-returning, unambiguous integer-sentinel, and ambiguous integer-sentinel function. State exact exception checks.
107. Translate a low-level exception into a domain exception with explicit cause. Contrast bare re-raise, <code>raise error</code>, <code>from error</code>, and <code>from None</code> tracebacks.
108. Construct nested <code>try</code>/<code>except</code>/<code>else</code>/<code>finally</code> cases with events. Predict order for success, handled error, unhandled error, return, and cleanup failure.
109. Use <code>TracebackException</code> to serialise bounded diagnostics without live-frame retention. Add redaction for a named secret local without calling arbitrary <code>repr</code> methods.
110. Demonstrate how storing an exception keeps a large local alive. Clear frames or extract diagnostics, release the exception, and verify collection.
111. Build a nested <code>ExceptionGroup</code>; handle disjoint subgroups with <code>except*</code>; verify preservation of unmatched leaves and metadata.
112. Compare ordinary <code>except</code> selection with <code>except*</code> splitting. Explain why the latter can execute several clauses for one raised group.
113. Integrate Chapters 11–15: design a context manager whose body and cleanup can fail, then specify chaining, suppression, resource state, and tests for every path.

### 15.22.13 Objects, types, and built-in representations

114. Measure shallow sizes for fixed and variable-size objects across controlled sizes. Identify header, payload, pointer-array, and separately allocated components qualitatively.
115. Explain why <code>PyVarObject</code> does not imply Python mutability using tuples, integers, bytes, lists, and a hypothetical native type.
116. Implement a class/metaclass/descriptor trio and trace explicit versus implicit special-method lookup. Identify which namespace supplies each result.
117. Assign an operator-named method to one instance and test whether the operator changes. Explain type-slot lookup and propose a supported per-instance design.
118. Measure integer size and arithmetic time by bit length. Fit an empirical relationship cautiously and identify algorithm-threshold effects.
119. Compare negative integer storage observations with Python’s specified infinite two’s-complement bit-operation semantics.
120. Compare ASCII, Latin-1-range, BMP, and astral strings for code-point length, UTF-8 bytes, shallow CPython size, hash behaviour, and equality.
121. Demonstrate that grapheme clusters, code points, and bytes give different lengths for combining characters and emoji sequences. Keep Unicode semantics separate from CPython storage.
122. Observe list capacity growth through shallow-size transitions. Calculate amortised append cost without treating one growth factor as guaranteed.
123. Contrast list indexing, front insertion, middle deletion, append, and shallow copy through both asymptotic analysis and measured ranges.
124. Build a pathological but correct colliding-key class. Count equality calls during dictionary insertion and lookup, then restore a well-distributed hash.
125. Demonstrate equal integer/float/Boolean keys sharing dictionary entries. Explain stored-key identity and hash/equality invariants.
126. Test insertion order under update, deletion, reinsertion, union, and comprehension. Separate language-guaranteed order from compact-table mechanism.
127. Use <code>id</code> only to log simultaneous object identities, then show why deletion permits reuse. Design a persistent UUID-based alternative.
128. Integrate Chapters 7, 9, 13 and 15: implement a mapping with explicit invariants, analyse its abstract complexity, and compare its object/storage overhead with <code>dict</code>.

### 15.22.14 Ownership, reference counting, collection, and weak references

129. Annotate every pointer in a small extension pseudocode function as new, borrowed, stolen, or non-owning. Draw ownership at each control-flow node.
130. Find and repair one leak, one double decrement, one dangling borrowed reference, and one exception-state mismatch in supplied or self-written C pseudocode.
131. Refactor a manual tuple-construction sequence to a higher-level C API. Compare failure paths and ownership proof burden.
132. Show why a borrowed list item cannot survive a callback without a strong reference. Write conventional-GIL and free-threaded safety arguments.
133. Design an error-cleanup label for three owned temporaries. Test every simulated failure injection point for balanced release.
134. Demonstrate at Python level that deleting a name, clearing a container, and returning from a frame release different ownership edges to one shared object.
135. Use finaliser logging to observe cascade order, but state why the observed order is not application semantics. Replace the design with explicit close.
136. Install an exception-safe <code>sys.unraisablehook</code> in an isolated test and capture a failing finaliser without retaining the object graph.
137. Compare <code>sys.getrefcount</code> deltas under aliases, containers, function arguments, and a debugger. Explain all temporary-reference qualifications.
138. Construct live and unreachable two-node cycles. Use weak references to prove which one collection reclaims.
139. Query <code>gc.is_tracked</code> before and after collections/mutations for atomic tuples, nested tuples, dictionaries, lists, and user instances. Treat optimisation as version-specific.
140. Model trial deletion mathematically for a graph with two cycles, one external root, and one cross-edge. Identify the unreachable subgraph.
141. Instrument <code>gc.callbacks</code> with bounded timing. Restore global state and explain observer overhead.
142. Use <code>DEBUG_SAVEALL</code> in an isolated process, inspect saved cycles, then clear every diagnostic reference. Explain why the mode intentionally leaks during analysis.
143. Write <code>tp_traverse</code>, <code>tp_clear</code>, and deallocation pseudocode for a two-field native container. Audit tracking order, inheritance, and re-entrancy.
144. Demonstrate resurrection exactly once, then redesign the lifecycle so resurrection is unnecessary. State what PEP 442 guarantees and what remains implementation-sensitive.
145. Implement a weak-value cache and a weak-key metadata table. Test death, equal-key replacement, callback exceptions, and slotted-class support.
146. Integrate Chapters 9, 11, 12 and 15: design a resource-owning object with context management, explicit close, weak finalisation fallback, idempotence, and concurrent tests.

### 15.22.15 Allocation, performance, and concurrency

147. Classify ten C allocations into raw, memory, or object domains. For each, specify matching resize/free and thread-state requirements.
148. Audit an allocation-size calculation for signed conversion, addition, multiplication, and alignment overflow before calling an allocator.
149. Compare default, debug, and system allocator modes in separate processes for one small-object workload. Record traced, resident, and elapsed measurements.
150. Use <code>tracemalloc</code> snapshots to locate intended cache growth and an unintended reachable leak. Explain why both are live allocations.
151. Measure current versus peak traced memory and explain why the peak can remain after all temporary objects die.
152. Compare shallow recursive-size estimation with tracemalloc and resident memory for a shared object graph. Prevent double-counting by identity.
153. Run repeated create/use/release cycles and test whether memory plateaus. Distinguish warm-up, free lists, allocator retention, and unbounded reachability.
154. Write a conventional-GIL thread benchmark combining CPU work and blocking I/O. Explain throughput using serialised bytecode and released-lock intervals.
155. Vary the switch interval only as a stress treatment. Show why no value repairs a deliberately unsynchronised invariant.
156. Audit a hypothetical <code>ALLOW_THREADS</code> block for raw Python pointers, buffer exports, callbacks, native errors, cancellation, and reattachment.
157. Design per-module state for a native extension and describe traverse, clear, free, multiple-interpreter, and GIL-support declarations.
158. Implement a bank-account or bounded-queue invariant protected across its entire compound transition. Test on conventional and free-threaded builds if available.
159. Identify five ways built-in container internal locking falls short of application transaction semantics. Provide a lock or message-passing solution for each.
160. Compare one, two, four, and eight threads on a free-threaded-capable CPU workload. Report speedup, efficiency, confidence intervals, and single-thread overhead.
161. Repeat the workload with an extension that does and does not release/support free threading. Record runtime GIL state and explain changed scaling.
162. Draw cache-line contention for one shared counter versus sharded counters. Connect the model to biased/deferred reference counting without claiming internal measurements you did not make.
163. Integrate Chapters 12, 14 and 15: build a benchmark harness recording environment, warm-up, distributions, correctness oracle, allocation metrics, and profiler evidence.

### 15.22.16 Calls, imports, extensions, and source research

164. Trace argument evaluation, starred expansion, duplicate keywords, positional-only rejection, default application, and body entry. Separate caller and callee obligations.
165. Sketch a vectorcall argument array for several positional and keyword combinations. Mark borrowed entries, positional count, <code>kwnames</code>, and optional scratch slot.
166. Compare immediate method calls, stored bound methods, built-ins, callable instances, classes, and <code>partial</code> objects using semantic signatures and measured allocations.
167. Design an Argument Clinic signature for a small native function, then compare generated parsing obligations with manual parsing conceptually.
168. Write a logging meta-path finder that delegates without changing semantics. Install and remove it in <code>try</code>/<code>finally</code>; avoid persistent global interference.
169. Create two temporary modules demonstrating a circular import and a partially initialised attribute. Refactor shared declarations into an acyclic dependency.
170. Build a loader that intentionally fails after importing a helper module. Inspect <code>sys.modules</code> and side effects, then clean the isolated environment.
171. Compile timestamp, checked-hash, and unchecked-hash bytecode caches in a temporary tree. Compare headers through documented constants without treating them as authenticated.
172. Demonstrate <code>reload</code> retaining an obsolete name and an external old-function reference. Design an explicit process-restart or versioned-plugin strategy instead.
173. Starting from one opcode, navigate a checked-out CPython 3.12 tree through generated definition, fallback helpers, slots, ownership, and tests. Preserve exact commit references.
174. Use version history to explain one changed internal mechanism. Distinguish rationale, accepted design, current documentation, current tests, and empirical effect.

### 15.22.17 Integrated mastery assessment

175. Build a capstone dossier for a non-trivial, ethically benign Python subsystem of your own: begin with encoded source; map tokens, AST, symbol tables, code objects, positions, exception regions, and adaptive disassembly; trace successful and failing calls through frames, type slots, ownership and allocation; analyse cyclic and weak-reference lifetime; test conventional and free-threaded concurrency contracts; inspect import/cache behaviour; corroborate with a pinned CPython source revision and tests; and finish with a table marking every conclusion L, P, I, or E plus its evidence, limits, and a falsifying observation. The dossier must be reproducible from a clean environment and must not depend on a private mechanism for application correctness.
