# 8.19 Exercises

### 8.19.1 Calls and contracts

1. Design a signature using positional-only and keyword-only parameters for a formatting API. Defend which names are stable public vocabulary.
2. Trace argument evaluation and binding for a call containing positional, starred, keyword, and double-starred arguments.
3. Write a function that intentionally mutates a supplied list and another that returns a modified copy. State ownership contracts and aliasing consequences.
4. Repair three mutable-default defects using `None`, a private sentinel, and a default factory. Explain when each is appropriate.

### 8.19.2 Scope and closures

5. Predict and then verify an `UnboundLocalError` caused by assignment classification. Repair it once with return-value design and once with `nonlocal`; compare effects.
6. Draw frames and namespaces for three nested calls, including an exception propagation path.
7. Construct the late-binding closure defect in a loop, then repair it by default capture and by a helper scope.
8. Build a closure-based accumulator with a reset operation. State retained state, mutation authority, and thread-safety limitations.

### 8.19.3 Recursion

9. Write recursive and iterative versions of Euclid’s algorithm. Prove their shared invariant and termination.
10. Implement recursive traversal of a nested list structure. Define what counts as an atomic leaf and handle cycles or explicitly prohibit them.
11. Compare naive and memoised Fibonacci by counting calls. State the cache’s space cost and validity assumptions.
12. Rewrite a tail-recursive summation as a loop and explain why ordinary CPython does not make the recursive form constant-stack.

### 8.19.4 Decorators

13. Derive a timing decorator from the explicit assignment transformation. Keep measurement separate from printing by injecting a reporting callable.
14. Write a decorator factory that validates a numeric result range. Preserve metadata and static signature.
15. Stack two tracing decorators and predict definition order and call order.
16. Identify an operation for which `repeat(3)` changes correctness, not merely performance.

### 8.19.5 Integrated exercise

17. Build the complete measurement-report pipeline with parsing, validation, pure summarisation, formatting, and a command boundary. Require finite values, define empty input, preserve line-number causes, and permit injection of the numeric parser. Provide call contracts, LEGB analysis, frame trace, object graph for mutable arguments, recursive or iterative proof where relevant, and a decorator-based diagnostic layer that does not alter results or swallow exceptions.

### 8.19.6 Function contracts and abstraction

18. Rewrite five vague requirements—“validate a user,” “get data,” “process records,” “calculate a rate,” and “save a report”—as contracts covering domain, result, effects, failures, termination, ownership, and complexity.
19. Give a mathematical function and three Python implementations: pure/total over the admitted domain, partial via exception, and effectful. State the distinct semantic models.
20. For <code>rectangle_area</code>, decide policies for Boolean, NaN, infinity, Decimal, Fraction, mixed units, and negative zero. Implement one coherent boundary and defend exclusions.
21. Specify precondition, postcondition, and frame condition for an in-place list rotation. Prove the multiset of element identities is preserved.
22. Design a function that is pure under one observation model but impure under another. State both models without contradiction.
23. Identify three hidden environmental dependencies in an existing-style function and refactor them into explicit value or callable inputs.
24. Compare totalizing a lookup with <code>None</code>, a unique sentinel, a tagged result, and an exception. Give caller code and ambiguity analysis for each.
25. Write a function dossier for <code>sorted</code> as used on a one-shot iterable with an effectful key. Distinguish built-in contract from implementation observation.

### 8.19.7 Signatures and binding

26. Classify every parameter in six signatures containing slash, bare star, variadic collectors, defaults, and annotations. Mark which call spellings are valid.
27. Design a public API with positional-only data operands and keyword-only policy options. Explain compatibility benefits and costs.
28. Construct calls that fail for missing required, surplus positional, unknown keyword, duplicate positional/keyword, non-string double-star key, and duplicate expansion keyword. Record which expressions execute before failure.
29. Write an observation function and trace evaluation order for mixed explicit positional, star expansion, explicit keyword, and double-star expansion.
30. Demonstrate that star-expanding a generator consumes it before body entry. Add a generator that raises midway and record partial effects.
31. Demonstrate that <code>**kwargs</code> receives a fresh outer dictionary while nested values remain shared.
32. Use the same name as a positional-only parameter and a key captured by <code>**kwargs</code>. Explain why the slash makes this unambiguous.
33. Distinguish an omittable parameter from a parameter admitting <code>None</code>. Design signatures for all four combinations.
34. Use <code>inspect.Signature.bind</code> and <code>bind_partial</code> on the same signature. Explain why partial binding is not permission to call an incompletely bound function.
35. Evolve a three-version public signature while preserving old calls. Use keyword-only additions and a deprecation pathway for a renamed keyword.
36. Write a forwarding adapter that preserves positional-only and keyword-only semantics as far as its runtime/static interface permits. Explain what <code>*args, **kwargs</code> hides.

### 8.19.8 Sharing, ownership, and results

37. Draw the reference graph before, during, and after a call that mutates one nested argument, rebinds another, retains a closure, and returns an alias.
38. Compare an in-place, copy-returning, immutable-returning, and lazy transformation API over the same data. State time, memory, effects, and aliasing.
39. Build a function whose <code>+=</code> mutates a list parameter and another whose custom object <code>__iadd__</code> returns a replacement. Trace caller observations.
40. Demonstrate outer copy, recursive deep copy, immutable conversion, and read-only proxy for one nested mapping. State exactly which mutations each prevents or reflects.
41. Design a registration function that retains callbacks. Add deregistration, duplicate policy, weak/strong lifetime choice, and callback-failure semantics.
42. Return a live mapping proxy and a shallow snapshot from two functions. Mutate underlying and nested state, then tabulate observations.
43. Create a function with three normal return paths and one exceptional path. Draw the control-flow graph and prove the runtime result domain.
44. Show how a <code>return</code> in <code>finally</code> replaces a result and an exception. Refactor to preserve the original outcome.
45. Design a command-query combined operation where separation would introduce a race or invalid intermediate state. Contrast with an unjustified combined operation.
46. Define idempotency for a set mutation, a database request, and a logging function under explicit observation models.

### 8.19.9 Defaults and definition timing

47. Predict default evaluation order for a definition with three effectful defaults and two decorators. Verify definition and call traces.
48. Capture a module global in a default, read it dynamically in a body, and capture it in a closure. Rebind the global and compare all three.
49. Place a function definition with a mutable default in a loop. Prove which calls share which default objects.
50. Repair mutable list, iterator, timestamp, random token, and cache defaults. For each choose body factory, sentinel, closure, explicit owner, or standard decorator.
51. Create a valid API where explicit <code>None</code> differs from omission. Implement a unique sentinel without exposing it as an accepted public value.
52. Inspect <code>__defaults__</code> and <code>__kwdefaults__</code>, mutate a retained default, and explain the lifetime/encapsulation consequences.
53. Capture a mutable object through a default, mutate it later, and contrast early reference capture with an immutable value snapshot.
54. Compare definition-time and call-time clock sampling in a record constructor. Write deterministic tests using injected clocks.
55. Replace an intentional mutable-default cache with <code>lru_cache</code> and with an explicit cache object. Compare reset, bounds, introspection, and concurrency.

### 8.19.10 Frames and lexical scope

56. For a nested call chain, identify code objects, function objects, frames, scopes, namespaces, and shared argument objects. Do not use the terms interchangeably.
57. Construct five <code>UnboundLocalError</code> examples caused by assignment, augmented assignment, import, deletion, and a conditional binding path.
58. Classify names as local, cell, free, global, or built-in in a three-level nested factory. Verify selected metadata through introspection.
59. Use two sibling closures sharing one cell and a second factory instance with an independent cell. Draw the graph.
60. Demonstrate nearest-binding selection by <code>nonlocal</code> across three function levels. Produce a syntax error case with no eligible binding.
61. Demonstrate that <code>global</code> targets the defining module and does not affect a same-named binding in another module or process.
62. Shadow five built-ins at different scopes and recover them explicitly through <code>builtins</code>. Explain why recovery is not a justification for routine shadowing.
63. Demonstrate that a method does not see ordinary class attributes through an unqualified enclosing lookup. Repair with instance/class access.
64. Test comprehension iteration-variable scope at module, function, and class contexts. Add the leftmost-iterable timing case.
65. Show exception-target clearing and traceback retention. Preserve only a bounded derived diagnostic after the handler.
66. Analyse pattern capture bindings across successful and unsuccessful cases. Avoid relying on partial bindings after failed patterns.
67. Use an explicit namespace dictionary with <code>exec</code>. Explain why trying to inject optimized function locals is a different and unsafe model.
68. Retain a frame through an exception or generator, identify a large local object it keeps alive, and remove the retention path.

### 8.19.11 Higher-order functions and closures

69. Pass functions as data without calling them, then accidentally pass their results. Use types and tests to expose the distinction.
70. Implement <code>map</code>, <code>filter</code>, and a left fold using explicit loops. State laziness, effects, and empty-input contracts.
71. Compare a comprehension, generator expression, <code>map</code>, and <code>filter</code> for one pipeline with a failing transformation. Record error timing.
72. Implement function composition with generics. Test normal return, inner failure, outer failure, and effect order.
73. Compare partial application, a closure factory, a lambda default capture, and a callable object for binding configuration.
74. Build an allowlisted command dispatch table. Reject duplicates/unknown commands and explain why dynamic <code>globals</code> dispatch is unsafe.
75. Design a callback host with stop-first, aggregate-all, and isolate/log failure modes. State which control exceptions propagate.
76. Make a callback mutate the collection being traversed. Repair the host with a snapshot, prohibition, and private iteration in three versions.
77. Build sibling closure operations <code>deposit</code>, <code>withdraw</code>, and <code>balance</code>. State invariants, exception safety, and concurrency limitations.
78. Demonstrate mutation versus rebinding of a captured list through <code>clear</code> and <code>nonlocal</code> replacement. Observe an external alias.
79. Repair the late-binding loop defect with defaults, helper scope, and partial. Compare introspection and mutable-object capture.
80. Use closure inspection to map free-variable names to cell contents, then explain why production callers should not depend on those names.
81. Create and break a callback/closure reference cycle or rooted registry retention. Distinguish cyclic garbage from a still-reachable logical leak.
82. Add locking to a closure counter. Analyse thread overlap, process isolation, re-entrant call risk, and lock lifetime.
83. Implement a live-settings and snapshot-settings closure factory. Test mutation, deletion, retained graph size, and temporal contracts.

### 8.19.12 Lambda and recursive reasoning

84. Rewrite six lambdas as named functions and three named key functions as lambdas. Defend where local concision or semantic naming wins.
85. Create lambdas with positional-only, defaulted, variadic, and keyword-only parameters. Document the limitation on direct annotations.
86. Show that a one-expression lambda can have several effects and failure points. Refactor it into a readable named function.
87. Prove recursive factorial by base, induction step, and variant. Then incorporate exact runtime domain validation outside the recursive core.
88. Count frames, calls, and arithmetic operations for linear recursion, naive Fibonacci, and balanced tree traversal. Distinguish depth from total work.
89. Derive the quadratic cost of slicing in recursive list sum. Repair with an index and with a loop.
90. Convert tail-recursive factorial to iteration and explain why tail position does not alter ordinary CPython stack use.
91. Implement merge sort completely, including stable linear merge. Derive its recurrence and allocation costs with slicing.
92. Implement preorder, postorder, and breadth-first traversal. State output order and auxiliary-space bounds for balanced and skewed trees.
93. Convert recursive preorder to an explicit stack and prove exact ordering equivalence by a continuation invariant.
94. Traverse a graph using current-path and global-visited sets in separate functions. Construct a DAG where their output counts differ.
95. Write mutually recursive parser functions for a small grammar. Supply a measure or grammar argument for termination and identify left-recursion danger.
96. Implement backtracking permutations with shared mutable state and <code>try/finally</code> restoration. Compare immutable-prefix copying.
97. Add pruning to subset sum under non-negative inputs. Give a counterexample showing why the pruning is invalid with negative values.
98. Refactor an adversarial-depth recursive input processor into iteration with an explicit maximum work bound.

### 8.19.13 Decorator semantics

99. Expand one and three stacked decorator syntaxes into explicit assignments. Distinguish decorator-expression evaluation order from application order.
100. Write a transparent forwarding wrapper with <code>wraps</code> and <code>ParamSpec</code>. List every semantic dimension it still might change.
101. Decorate a recursive function and determine whether recursive calls pass through the wrapper. Refactor to trace only the public call.
102. Apply a wrapper around an instance method, class method, and static method under both plausible stacking orders. Explain descriptor effects.
103. Write separate wrappers for a synchronous function, coroutine function, generator function, and async generator. Preserve their protocols and cleanup.
104. Show precisely how eager list collection breaks generator transparency: infinite input, first-result latency, exception timing, memory, and close semantics.
105. Implement a registration decorator with duplicate detection, deterministic ordering, reload policy, deregistration, and isolated test state.
106. Return a non-callable from a decorator and inspect the bound name. Explain why syntax permits it and convention discourages surprise.
107. Implement a timing decorator with injected monotonic clock and reporter. Ensure reporter failure does not silently replace a primary failure under your chosen policy.
108. Trace cache/authorization, retry/transaction, and timing/retry stacks. For each, choose an order and state the meaning.
109. Extend bounded retry with a deadline and jitter provider. State idempotency precondition and cancellation handling; implement sync or async, not an ambiguous hybrid.
110. Build a stateful call counter as closure and callable object. Preserve method binding or explicitly reject method decoration.
111. Use <code>inspect.unwrap</code> on a decorator chain. Demonstrate how calling the result bypasses semantics and restrict it to trusted diagnostics.

### 8.19.14 Introspection and memoisation

112. Inspect name, qualified name, module, docstring, annotations, defaults, closure, signature, and code metadata for five callable kinds. Identify unavailable or misleading fields.
113. Give a function a forged <code>__name__</code>, <code>__module__</code>, <code>__signature__</code>, and <code>__wrapped__</code>. Explain why metadata is not trust evidence.
114. Retrieve source for a module function and attempt it for a built-in, lambda, dynamic definition, and interactive-like code. Document contingent failures.
115. Validate a plugin signature without invoking it, then construct a malicious or defective callable that passes shape validation but violates semantics.
116. Use passive and dynamic attribute inspection on an object with a descriptor that has effects. Compare <code>getattr</code> and static inspection.
117. Memoise a pure recursive function with overlapping subproblems and one without overlap. Measure calls and retained entries to show when caching helps.
118. Construct a cached function with a hidden mutable global dependency. Demonstrate staleness and repair with versioned keys or invalidation.
119. Canonicalise positional/keyword call spellings through a public wrapper before a private cache. Test cache hit counts.
120. Return a mutable cached result and demonstrate shared corruption. Repair with immutable results and with copy-on-hit; compare costs.
121. Demonstrate that exceptions are recomputed rather than ordinarily cached. Design an explicit immutable failure-result cache with expiry/invalidation policy.
122. Launch overlapping calls for one missing cache key and observe or reason about duplicate computation. Design per-key single-flight state.
123. Cache an instance method and show how entries can retain instances. Redesign with per-instance ownership or a pure static function.
124. Implement top-down and bottom-up edit distance. Compare state count, recursion depth, table space, row compression, and path reconstruction.
125. Add unseen/active/complete states to a dependency evaluator. Detect cycles and distinguish them from cached complete results.
126. Design a cache benchmark reporting hits, misses, key costs, retained bytes, churn, cold start, and latency distribution rather than hit rate alone.

### 8.19.15 Integrated mastery

127. Design a function library for validated interval arithmetic. Use immutable values, total-order endpoints, pure operations, precise exceptions, property tests, and a compatibility plan.
128. Build a plugin command system using signature validation, a registration decorator, explicit context injection, immutable requests, callback isolation, and deterministic dispatch. Provide a threat model explaining why plugins remain trusted code.
129. Implement an expression-tree evaluator recursively and iteratively. Add variable environments, structured errors, memoisation for shared DAG nodes, cycle detection, and a maximum-work bound.
130. Build a configurable text pipeline from composable pure functions: strict decoding, Unicode normalization, validation, transformation, and encoding. Preserve original diagnostics and derive a proof of stage-domain compatibility.
131. Implement a transactional in-memory transfer service with a pure balance transition, one invariant-owning lock, idempotency keys, immutable result records, and callbacks invoked only after commit. Analyse callback failure and retry.
132. Create a recursive-descent parser for a small arithmetic grammar. Specify tokens, grammar, precedence, call graph, termination, error positions, recursion-depth limits, and AST value objects.
133. Build a bounded memoising decorator whose limits include entry count and estimated byte weight. Define key normalization, mutable results, eviction, concurrency, metrics, and explicit clearing.
134. Refactor a deliberately monolithic import/report function into parsing, validation, domain calculation, rendering, I/O, and command boundary. Justify every extraction by invariant or reason for change.
135. Create an async-aware observability decorator family that preserves sync, coroutine, generator, and async-generator protocols. Test return, exception, cancellation, early close, and metadata.
136. Write a comparative essay with executable evidence: closure, callable class, module global, explicit state parameter, and immutable state transition as five ways to model evolving state. Compare binding, lifetime, serialization, testing, concurrency, and proof.
137. Develop a complete formal dossier for the event-processing function family from Chapter 7: signatures, binding traces, ownership, frames, scope, higher-order policies, recursion where applicable, decoration, caching, exceptions, complexity, and versioning.
138. Select one real function from a standard-library module. Using primary documentation and source for a fixed Python tag, separate language/API guarantees from CPython implementation facts and reproduce a small behavioural study.
