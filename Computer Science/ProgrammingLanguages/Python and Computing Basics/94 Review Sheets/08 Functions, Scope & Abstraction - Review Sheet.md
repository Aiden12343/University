# 8.18 Common misconceptions consolidated

1. **“Defining a function runs its body.”** Definition creates and binds a function object; calls execute the body.
2. **“A parameter is the value passed by the caller.”** A parameter is a callee-side name; the supplied object is an argument.
3. **“Python passes mutable values by reference and immutable values by value.”** One object-binding rule applies; mutation and rebinding explain the different observations.
4. **“A function can return several values.”** Comma-separated return expressions create one tuple, commonly unpacked by the caller.
5. **“Defaults are recalculated for each missing argument.”** They are evaluated when the definition executes.
6. **“Global means available in all modules.”** It names the defining module’s namespace in this resolution context.
7. **“Closures snapshot local values.”** They retain access to lexical bindings, creating late-binding behaviour unless distinct capture is arranged.
8. **“Recursion is always elegant or always inefficient.”** Suitability depends on problem structure, repeated subproblems, call depth, and implementation limits.
9. **“A decorator merely annotates a function.”** It receives the defined object and controls what is bound under the name.
10. **“Memoisation is a free speed improvement.”** It changes memory, effects, staleness, hashability, and lifetime contracts.
11. **“A function is completely described by its input and output types.”** Effects, exceptions, termination, ownership, determinism, complexity, and concurrency are also observable dimensions.
12. **“Mathematical and Python functions are the same abstraction.”** A Python call may mutate, raise, suspend, diverge, or depend on environment; a mathematical function maps every domain element to one codomain value.
13. **“Abstraction means implementation details never matter.”** A detail remains hidden only if it cannot violate the published semantic or performance contract.
14. **“Annotations validate arguments before body execution.”** Ordinary Python stores annotation metadata; it does not generally enforce it.
15. **“Keyword arguments are evaluated in parameter order.”** Argument expressions follow call-expression evaluation order; binding later associates results with parameters.
16. **“A failed argument binding means the call expression had no effects.”** Argument and expansion expressions may already have executed before the body is rejected.
17. **“Star expansion passes the iterable lazily.”** Expansion consumes it to construct call arguments before body execution. Pass the iterable as one argument for streaming.
18. **“Double-star expansion merges duplicates like dictionary union.”** Duplicate keyword names in a call are rejected as ambiguous bindings.
19. **“Optional parameter means None is valid.”** Omission through a default and acceptance of <code>None</code> are independent properties.
20. **“Positional-only parameters are private.”** They remain public parameters; only their names are unavailable as keyword call syntax.
21. **“Variadic parameters make an API future-proof.”** Unrestricted collectors can hide spelling errors, weaken tooling, and defer compatibility problems.
22. **“Rebinding a parameter rebinds the caller’s variable.”** It changes only the callee’s local name; mutation of a shared object crosses the boundary.
23. **“Passing a shallow copy prevents all callee mutation from being observed.”** Nested mutable elements remain shared.
24. **“Augmented assignment always mutates.”** It dispatches an in-place protocol when available and may instead compute a new object before rebinding.
25. **“Returning a mutable object gives the caller a copy.”** It returns an object reference; freshness, sharing, or view semantics must be stated.
26. **“None means no value exists.”** <code>None</code> is a concrete singleton object whose domain meaning is interface-specific.
27. **“Every function with a result should avoid effects.”** Combined command-query operations can be coherent when result and state transition are one abstraction, as with <code>pop</code>.
28. **“Definition-time defaults are evaluated exactly once forever.”** They run once per execution of the definition statement, which can occur repeatedly through loops, reloads, dynamic execution, or processes.
29. **“A default captures a name dynamically.”** The default expression resolves to an object at definition time; later name rebinding does not replace the retained object.
30. **“A unique sentinel should be tested with equality.”** Sentinel meaning is unique identity, so use <code>is</code>.
31. **“A frame and a scope are synonyms.”** Scope is a lexical rule region; each execution can create a distinct frame.
32. **“Each recursive frame copies mutable arguments.”** It creates new parameter bindings that may point to the same objects.
33. **“Locals always disappear immediately on return.”** Escaping values, closures, tracebacks, debuggers, and suspended execution can retain objects or frames.
34. **“Writing to locals() reliably creates a local variable.”** Optimized function locals are governed by compiled bindings; the mapping is not a portable mutation portal.
35. **“Global lookup uses the caller’s module.”** It uses the function’s defining global namespace.
36. **“global makes a value shared by every module and process.”** It targets one module namespace in one interpreter/process context.
37. **“nonlocal searches arbitrary outer blocks.”** It targets an existing binding in an applicable enclosing function scope.
38. **“Class attributes are enclosing locals for methods.”** Methods normally access them through an instance or class; the class body is not an ordinary enclosing function scope.
39. **“Comprehension loop variables leak into their surrounding function.”** Python 3 comprehensions ordinarily use an implicit separate scope for iteration targets.
40. **“An exception target remains available after except.”** It is cleared after the handler to reduce traceback/frame cycles.
41. **“A callable is necessarily a Python function.”** Classes, bound methods, built-ins, and callable instances also satisfy call syntax.
42. **“Two functions with identical source are equal.”** Separately created functions are generally distinct objects; arbitrary behavioural equivalence is not mechanically decided.
43. **“Callbacks are passive values.”** Calling one transfers control to external behaviour that may fail, mutate, retain, block, or re-enter.
44. **“Algebraic function composition permits reordering effectful calls.”** Composition order governs effects and failures; mathematical equivalence applies only under stated purity/law assumptions.
45. **“Partial application and currying are synonyms.”** Partial application fixes selected arguments; currying systematically transforms multi-argument structure into nested unary calls.
46. **“A closure stores a copy of the entire outer frame.”** It retains access to required free-variable cells; unused locals need not be captured.
47. **“nonlocal is required to mutate a captured list.”** It is required to rebind the cell, not to call mutation methods on its existing object.
48. **“Late binding is always a closure defect.”** It is necessary when sibling closures intentionally observe updated shared state.
49. **“Lambda captures loop values specially.”** Lambda follows ordinary closure/default timing. Per-iteration capture must be constructed explicitly.
50. **“One-expression lambda means simple behaviour.”** An expression can contain substantial branching, calls, and comprehensions; simplicity is semantic, not grammatical.
51. **“Tail-recursive Python code uses constant stack.”** Python does not require tail-call elimination, and ordinary CPython retains frames.
52. **“An induction proof of a recursive result proves termination.”** Partial correctness and progress/well-foundedness are separate obligations.
53. **“Recursion depth determines total runtime.”** Branching recursion can perform exponentially many calls at linear depth; balanced traversals can have logarithmic depth and linear work.
54. **“A visited set has one universal graph meaning.”** Current-path tracking detects cycles while allowing repeated DAG occurrences; global visited tracking counts/expands identities once. Choose by semantics.
55. **“Catching RecursionError converts deep valid input into a domain answer.”** It reports execution-resource exhaustion, not a semantic negative result.
56. **“Decorator expressions apply in the same top-to-bottom order they are written.”** Expressions evaluate in source order, while decorator application composes bottom-up around the function.
57. **“A wrapper that returns a coroutine preserves async semantics.”** A synchronous wrapper changes coroutine-function introspection and observes creation rather than awaited completion.
58. **“Turning a generator result into a list is transparent.”** It changes laziness, finiteness, memory, failure timing, and generator control methods.
59. **“Registration decorators have no call-time effect, so they are harmless.”** They mutate definition/import-time registries with lifetime, duplicate, ordering, and reload consequences.
60. **“Stacking authorization and caching decorators is order-independent.”** An outer cache can bypass current authorization checks; policy composition must be traced.
61. **“A retry decorator can safely retry any raised exception.”** Safety depends on failure classification, idempotency, uncertain effects, cancellation, deadlines, and backoff.
62. **“A timing decorator measures algorithmic complexity.”** It measures noisy durations for instrumented calls under one workload; complexity requires scaling and a model.
63. **“Function metadata proves origin or trust.”** Attributes are mutable and can be copied or forged.
64. **“inspect.signature proves semantic compatibility.”** It checks advertised/bindable shape, not effects, result meaning, latency, or truthful metadata.
65. **“Source is always recoverable from a running function.”** Interactive, generated, built-in, stripped, or relocated code may have no retrievable corresponding source.
66. **“Unwrapping a decorator is a neutral debugging action.”** Calling the unwrapped function can bypass validation, locking, authorization, or transactional semantics.
67. **“Hashable arguments make memoisation semantically correct.”** Keys must encode every dependency; results must also be safe to retain and share.
68. **“Cached mutable results are copied on hits.”** Standard memoisation returns the retained object reference.
69. **“A thread-safe cache computes each missing key exactly once.”** Coherent cache updates can still permit duplicate concurrent underlying calls.
70. **“A bounded entry count bounds cache memory.”** Key/result sizes and retained graphs vary; count is not bytes.
71. **“Caching instance methods cannot affect instance lifetime.”** Cache keys often include <code>self</code> and can retain it.
72. **“Every repeated code fragment should become one generic function.”** Similar syntax may encode different knowledge and change for different reasons.
73. **“Dependency injection means using a framework.”** Passing a value or callable explicitly is already dependency injection.
74. **“More defensive copies always improve safety.”** Copy depth, hooks, resource identity, cost, and snapshot meaning must match a threat/ownership model.
75. **“Function length is a direct measure of quality.”** Cohesion, contract size, hidden dependencies, and proof state are more meaningful than line count alone.
