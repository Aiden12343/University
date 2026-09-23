# 6.19 Exercises

### 6.19.1 Selection and loops

1. Rewrite a set of overlapping independent `if` statements as an exclusive chain, then prove its intervals are complete and disjoint.
2. Implement integer exponentiation by repeated multiplication for a non-negative exponent. State invariant, variant, and postcondition.
3. Implement a sentinel-controlled input loop. Specify how EOF, empty input, and malformed values differ.
4. Construct a loop with two `continue` paths and prove that each preserves one stated invariant.
5. Use loop `else` to determine primality by trial division; state exactly what normal exhaustion establishes.

### 6.19.2 Iteration protocols

6. Demonstrate two independent iterators over one list and one iterator shared by two consumers. Trace the difference.
7. Implement an iterator class producing the first (n) powers of two. Prove termination.
8. Reimplement it as a generator and compare state representation and call timing.
9. Design an iterable whose `__iter__` returns a fresh generator on every call. Show that it is reusable while each generator remains one-shot.
10. Explain the defect risk of mutating a list while its iterator is active; do not assume a snapshot.

### 6.19.3 Laziness and comprehensions

11. Translate a nested comprehension into explicit loops with identical order.
12. Construct an eager list pipeline and a lazy generator pipeline for the same transformation. Record when side effects and failures occur.
13. Use `zip(strict=True)` to validate parallel data. Design fixtures for first-shorter, second-shorter, equal-empty, and equal-non-empty inputs.
14. Explain why calling `list` on an unbounded generator cannot complete under ordinary resources.

### 6.19.4 Exceptions

15. Write one `try`/`except` whose protected suite is too broad. Construct an unintended same-type exception it misclassifies, then narrow the suite.
16. Translate a low-level exception into domain context using explicit chaining. Inspect the causal traceback.
17. Design an interface choosing deliberately among `None`, a result object, and an exception. Defend the information preserved by your choice.
18. Construct a `finally` demonstration for normal return, handled exception, unhandled exception, and loop `break`. Do not include `return` in `finally`.

### 6.19.5 Integrated exercise

19. Implement a lazy reader of signed integers from an iterable of text lines. It must track source line numbers, ignore comments and blank lines, raise a chained domain exception for malformed data, optionally reject negatives, and expose no partial aggregate after failure. Then implement count, total, minimum, and maximum consumers. Supply invariants, termination arguments for finite input, an explicit statement for unbounded input, and tests distinguishing construction-time from consumption-time failure.

### 6.19.6 Control-flow graphs and branches

20. Draw a control-flow graph for a function containing validation guards, a three-clause selection, and two returns. Mark entry, normal exits, abrupt exits, dominators, and joins.
21. Construct an <code>if</code>/<code>elif</code> chain with an accidentally unreachable clause. Prove subsumption and repair the priority order.
22. Define a classifier over integers with five complete disjoint intervals. Derive residual domains at every clause and construct every boundary test.
23. Extend the classifier to floats admitting infinities and NaN. State why the integer partition proof no longer suffices.
24. Convert a decision table with three independent conditions into nested statements and an ordered chain. Compare the paths and test obligations.
25. Give an example where sampling a condition once is required and one where repeated sampling is required. State the temporal specification.
26. Demonstrate a mutable-attribute type refinement invalidated by a callback. Repair it with an immutable local snapshot.

### 6.19.7 Loop proofs

27. Prove repeated addition for multiplication using initialisation, preservation, exit use, and a non-negative variant.
28. Implement linear search with a while loop. State an invariant over the searched prefix and derive both found and absent postconditions.
29. Construct four off-by-one defects involving initial value, inclusive bound, exclusive bound, and update position. Use boundary algebra to repair each.
30. Implement Euclid’s algorithm and prove preservation of common divisors and strict decrease of the second component.
31. Give a loop whose state changes on every iteration but does not terminate. Explain why change alone is not a variant.
32. Supply a lexicographic or scalar variant for nested row-and-column traversal.
33. Design an intentionally non-terminating event loop. State its safety, liveness, cancellation, responsiveness, and resource-boundedness obligations.
34. Add a maximum-iteration guard to an iterative approximation. Explain what it proves and what it does not prove about convergence.
35. Replace a floating equality-controlled loop with an integer-indexed construction. Compare the represented values and error policy.

### 6.19.8 Abrupt loop paths

36. Draw every exit path for a loop containing normal completion, break, continue, return, and an exception. State which paths execute loop else.
37. Construct a defective continue path that bypasses progress and prove non-termination for one input. Centralise the progress transition.
38. Search a two-dimensional collection and exit both loops using a helper function. Compare with a flag-based solution.
39. Implement primality testing with loop else and prove why exhaustion through integer square root establishes primality.
40. Place a try/finally around a loop body with break and continue. Predict cleanup order for every route.

### 6.19.9 Iteration ownership

41. Implement a reusable iterable with a separate iterator class. Create two simultaneous iterators and prove their positions are independent.
42. Wrap a one-shot iterator in an iterable whose <code>__iter__</code> creates fresh generator objects. Demonstrate why the wrapper remains one-shot.
43. Search for a present and absent value in an iterator, then list the remainder. Explain partial and complete consumption.
44. Use a unique sentinel with two-argument <code>next</code> for an iterator that legitimately yields <code>None</code>.
45. Construct a temporarily empty external-source abstraction and explain why <code>StopIteration</code> would incorrectly declare permanent exhaustion.
46. Compare materialisation, recomputation, and <code>itertools.tee</code> for two consumers. Derive the memory risk when one tee consumer stops.
47. Design an iterator whose diagnostic representation does not consume its remaining values.
48. Create a custom iterator that raises a recoverable non-exhaustion exception on one request. State whether and how later requests proceed.

### 6.19.10 Generators and lazy control

49. For one generator, record created, running, suspended, and closed states. Identify which transitions can be directly observed without re-entry.
50. Write a generator receiving values with <code>send</code>. Trace the two temporal halves of every yield expression.
51. Return a summary from a subgenerator and capture it with <code>yield from</code>. Distinguish yielded items from the return value.
52. Inject a handled and an unhandled exception with <code>throw</code>. Record the resulting generator states.
53. Build a resource-owning generator and demonstrate explicit close after early consumer exit. Then redesign so a surrounding context owns the resource.
54. Show that an accidental <code>StopIteration</code> escaping from a generator becomes <code>RuntimeError</code>. Replace it with proper return.
55. Construct a suspended generator that retains a large local graph. Identify which references preserve it and redesign its state if retention is unnecessary.
56. Explain why generator non-reentrancy does not establish thread safety.

### 6.19.11 Comprehensions and alignment

57. Translate a four-clause comprehension into nested loops without changing evaluation order or output order.
58. Compare list, set, dictionary, and generator comprehensions over duplicate inputs. State destination invariants and collision behaviour.
59. Demonstrate that the leftmost iterable expression of a generator expression is evaluated immediately while element transformations are deferred.
60. Construct a dictionary comprehension with duplicate derived keys. Replace it with explicit uniqueness validation.
61. Compare eager and lazy parsing of a source whose fifth item is malformed. Record binding, partial results, and external effects.
62. Build independent matrix rows with a nested comprehension and contrast them with repeated inner-list aliasing.
63. Demonstrate original-source numbering versus post-filter numbering with <code>enumerate</code>.
64. Use default, strict, and longest zip policies on mismatched inputs. State which data is discarded, rejected, or padded.
65. Demonstrate that strict zip can consume an unmatched item from an earlier source while discovering a later source’s exhaustion.
66. Transpose a finite rectangular sequence with zip and define behaviour for empty, ragged, huge, and unbounded inputs.

### 6.19.12 Exception architecture

67. Draw the relevant built-in exception hierarchy for <code>BaseException</code>, <code>Exception</code>, lookup errors, arithmetic errors, and control exceptions.
68. Write handlers in a deliberately wrong superclass-before-subclass order. Prove which clause is unreachable and repair it.
69. Translate a low-level exception twice, once with implicit context and once with explicit cause. Compare traceback meaning.
70. Add a bounded non-sensitive note while re-raising an exception. Explain why notes differ from replacement.
71. Construct an exception group containing three types and handle two with <code>except*</code>. Trace the remaining subgroup.
72. Write an assertion that incorrectly performs an essential effect. Run the reasoning under disabled assertions and replace it with stable logic.
73. Compare EAFP and LBYL for dictionary access and for a filesystem existence check. Analyse time-of-check/time-of-use races.
74. Give an operation with no exception-safety guarantee, then redesign it for the basic and strong guarantees.
75. Define a three-class domain exception hierarchy with structured fields. Show broad domain handling and narrow subtype handling.
76. Demonstrate how retaining an exception can retain a large local object through its traceback. Design a bounded diagnostic record.
77. Trace nested try/except/finally execution when work fails and cleanup also fails. Identify primary, context, and propagating exceptions.

### 6.19.13 Results, retries, and integrated mastery

78. Design optional-result, tagged-result, and exception-based versions of one lookup. State caller obligations and ambiguity risks.
79. Build a batch validator that accumulates independent data defects but stops immediately when an invariant required for safe continuation fails.
80. Analyse a retry loop for a non-idempotent payment. Specify the idempotency mechanism and outcome-query protocol needed for safety.
81. Write a complete control-flow dossier for the line parser in §6.17. Include graph, invariants, source ownership, failure timing, cleanup, and oracles.
82. Implement lazy and eager versions of one finite data pipeline. Prove ordinary-result equivalence and document every difference in memory, latency, effects, and error timing.
83. Construct a pattern-matching command interpreter using literal, sequence, mapping, class, OR, AS, and guarded patterns. Identify every capture and residual case.
84. Find a class pattern that admits Boolean values through an integer class relationship. Add an exact domain guard and tests.
85. Combine a resource context, lazy parser, strict zip, pattern-based record classification, and transactional sink. State which layer owns each exception and which claims depend on external transaction semantics.
