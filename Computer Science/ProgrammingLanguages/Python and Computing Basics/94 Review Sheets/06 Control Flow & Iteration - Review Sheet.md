# 6.18 Common misconceptions consolidated

1. **“A loop repeats code all at once.”** Each iteration is a new control arrival under a new state.
2. **“`for` is a counting loop.”** It consumes an iterator; numeric counting is one iterable use.
3. **“Iterable and iterator are synonyms.”** An iterable can supply an iterator; an iterator retains one traversal state and supplies itself from `iter`.
4. **“Generator calls run their bodies immediately.”** Calling creates the generator; requests resume its body.
5. **“Lazy always means more efficient.”** Laziness changes memory, timing, reuse, side effects, failures, and overhead; suitability depends on workload.
6. **“Loop `else` runs when an `if` condition is false.”** It runs on normal loop completion without `break`.
7. **“Exceptions are merely error messages.”** They are objects initiating non-local control flow through active frames.
8. **“Catching an exception fixes the condition.”** A handler must restore an invariant, translate the failure, retry safely, or terminate at an owned boundary.
9. **“`finally` means the process can never avoid cleanup.”** It governs ordinary Python control transfers; abrupt process or machine failure can prevent it.
10. **“A `match` case name compares with an existing variable.”** Bare names usually capture in patterns; pattern grammar differs from expression grammar.

11. **“An if chain automatically partitions every possible value.”** It selects at most one suite, but coverage and residual-domain interpretation require proof over admitted inputs.
12. **“An invariant is whatever remains unchanged.”** A useful loop invariant is a precise boundary property strong enough to imply the postcondition and preserved on every back edge.
13. **“A decreasing float proves termination.”** Floating rounding, NaN, and lower bounds can defeat the argument. A variant requires a well-founded domain.
14. **“Break makes the loop condition false.”** It transfers control without changing or re-evaluating the condition.
15. **“The loop target is local to the loop.”** Ordinary loop targets bind in the surrounding scope; comprehension targets use an implicit nested scope.
16. **“Range stores all of its integers.”** It represents an arithmetic progression compactly and computes items as required.
17. **“Membership tests do not modify data.”** Searching a one-pass iterator consumes through the match or exhaustion.
18. **“Strict zip validates at construction.”** Mismatch is discovered lazily during consumption, after possible prefix effects.
19. **“A fresh iterator wrapper makes an exhausted source reusable.”** Reusability must exist in or reconstruct the underlying source.
20. **“Generator creation proves its setup succeeded.”** Body execution, resource acquisition, and most failures are deferred until resumption.
21. **“Generator close can be ignored because garbage collection handles it.”** Prompt collection is implementation-dependent; resource ownership requires controlled closure.
22. **“A list comprehension is merely shorter loop syntax.”** It has its own scope, eager construction, and destination collision semantics.
23. **“A failed lazy pipeline produced nothing.”** Earlier yielded items can already have caused irreversible downstream effects.
24. **“Except Exception is safe because it excludes system exits.”** It still catches most programming and operational failures, often beyond the handler’s ability to repair.
25. **“Raise error and bare raise are identical.”** Bare raise transparently resumes the handled exception; explicitly raising the object can alter traceback presentation.
26. **“Finally always preserves the original outcome.”** Its own return, transfer, or exception can replace a pending return or exception.
27. **“Assertions validate anything important.”** They may be disabled and are appropriate only for internal conditions not required as stable external handling.
28. **“EAFP is always more Pythonic than checking first.”** Atomicity, exception provenance, cost, and semantics decide the design.
29. **“Pattern matching validates a record.”** It establishes selected structure; domain, authority, range, and cross-field invariants remain.
30. **“No match means an error.”** Without a selected case, execution simply continues unless the program explicitly raises or supplies a fallback.
