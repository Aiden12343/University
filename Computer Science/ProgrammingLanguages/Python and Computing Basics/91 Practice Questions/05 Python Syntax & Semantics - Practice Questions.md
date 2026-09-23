# 5.21 Exercises

### 5.21.1 Syntax, expressions, and evaluation

1. Classify ten original constructs as expression, simple statement, or compound statement. For each statement containing expressions, mark their evaluation order.
2. Construct one syntactically invalid addition and one syntactically valid addition that fails at runtime. Explain the phase distinction.
3. Write a three-call expression whose printed trace distinguishes precedence from operand evaluation order. Predict before executing.
4. Explain why rewriting an expression with side effects using algebra alone can change behaviour.

### 5.21.2 Bindings and object graphs

5. Draw names and objects after every line:

   ```python
   a = [1, 2]
   b = a
   c = a[:]
   b[0] = 9
   a = c
   c.append(3)
   ```

6. Give one pair that is equal but not identical and one pair that is identical. Do not rely on immutable literal caching.
7. Construct a tuple whose hash operation fails and explain why tuple immutability is insufficient.
8. Explain `del name` using reachability. Include a surviving alias and a newly unreachable object.
9. Design an ownership contract that makes shared mutation of a list intentional rather than accidental.

### 5.21.3 Numeric and textual boundaries

10. Explain the output of `-17 // 5` and `-17 % 5` using the reconstruction equation.
11. Find a decimal fraction exactly representable in binary and one that is not. Show the positional reasoning.
12. Compare constructing `Decimal` from text and from float. State which prior representation each receives.
13. Choose representations for currency, scientific measurement, exact fractions, and very large counts. State domain requirements and costs.
14. Produce a string whose `len` differs from both its UTF-8 byte length and its user-perceived character count. Explain all three measures.
15. Demonstrate indexing and slicing of `bytes`, and explain the result-type difference.

### 5.21.4 Truth and absence

16. For each of `0`, `0.0`, `""`, `"0"`, `[]`, `[False]`, `{}`, `None`, and `float("nan")`, predict `bool(value)` and justify it from the type contract.
17. Write an interface where zero is a valid result and `None` means absence. Show the defect introduced by `result or default`.
18. Use short-circuiting to guard a subscription that is valid only for a non-empty sequence. Then explain which operand must come first.

### 5.21.5 Integrated exercise

19. Analyse a small inventory state containing nested dictionaries, lists, strings, integers, and `None`. Produce:
    - a complete object-and-binding graph;
    - every mutable identity;
    - a shallow-copy trace;
    - one equality comparison and one justified identity comparison;
    - a text-to-bytes boundary;
    - a numeric representation choice;
    - a classification of each asserted fact as language, CPython, environment, or experiment.

### 5.21.6 Lexical and grammatical analysis

20. Tokenise five source lines by hand. Identify names, literals, operators, delimiters, indentation changes, logical newlines, and discarded comments.
21. Give four different literal spellings for integer 45. Demonstrate that radix is a source representation rather than an integer property.
22. Construct a list whose missing comma silently concatenates two adjacent string literals. Write an oracle that detects the defect.
23. Compare <code>(value)</code>, <code>(value,)</code>, and <code>()</code>. Explain the role of comma and parentheses in each.
24. Classify one failure at each of source decoding, parsing, name lookup, operation dispatch, and domain validation. State why a later-stage case necessarily passed some earlier boundaries.
25. Use <code>ast.parse</code> to compare the trees for <code>a + b * c</code> and <code>(a + b) * c</code>. Identify what surface punctuation the abstract tree omits.

### 5.21.7 Assignment and partial effects

26. Trace a chained assignment to a mutable object and demonstrate shared identity. Repair it for independent state.
27. Create an unpacking assignment whose source yields one too many elements. Record every source effect and determine whether target names were changed.
28. Create a multiple-target assignment in which an early attribute target succeeds and a later target rejects assignment. Show that no rollback occurs.
29. Explain the tuple-containing-list augmented-assignment paradox: mutation succeeds, storage fails, and an exception is raised. Draw the object graph before and after.
30. Compare <code>target += value</code> for integer, string, list, and a user-defined type. Record identity and alias observations without generalising implementation reuse.
31. Design an all-or-nothing state update that validates every proposed value before replacing one immutable aggregate.

### 5.21.8 Lifetime and ownership

32. Draw the object graph for a list and dictionary sharing one nested record. Identify every path through which its state can be mutated.
33. Construct an unreachable self-cycle and explain why reference counting alone cannot identify it as reclaimable.
34. Use a weak reference to observe a user-defined instance. Separate the weak-reference contract from the timing observed in CPython.
35. Specify an ownership contract for an API exposing a collection. Compare returning its live list, an iterator, a tuple snapshot, and a deep copy.
36. Show that closing a file and making its Python object unreachable are distinct transitions. Rewrite the experiment with a context manager after consulting Chapter 11’s minimal definition.
37. Identify a case in which defensive copying prevents a defect and another in which it destroys required identity or imposes unacceptable cost.

### 5.21.9 Comparison and hashing

38. For a proposed equality relation, test reflexivity, symmetry, and transitivity. Include NaN as an explicit counterexample to an assumed universal law.
39. Create three distinct but equal hashable objects and use each to retrieve one dictionary association. Explain why dictionary length remains one after successive assignments.
40. Design a user-defined record whose equality depends only on an immutable identifier. State a coherent hash policy and what mutations remain permitted.
41. Explain why equality of hashes is insufficient evidence of equality. Construct or locate a collision without using it as a security claim.
42. Sort optional integers with missing values first, then with missing values last. Write the ordering key for each policy.
43. Design a tagged dictionary key that distinguishes Boolean true, integer one, and floating one despite ordinary numeric equality.

### 5.21.10 Numeric representation

44. Derive the exact integer ratio represented by <code>0.1</code> and compare it with (1/10). Compute absolute error.
45. Find three expressions demonstrating non-associativity of binary floating addition. Explain each rounding boundary.
46. Compare <code>round</code> for positive and negative halfway cases. State the tie policy and distinguish it from decimal-looking values that are not exact ties.
47. Implement a cyclic index using positive modulo. Extend the specification to negative movement and verify the reconstruction identity.
48. Pack a 16-bit unsigned integer in big- and little-endian order. Decode each with both orders and classify wrong-order success as a semantic defect rather than parser failure.
49. Choose among integer minor units, <code>Decimal</code>, <code>Fraction</code>, float, and complex for five original domains. Specify operations, error model, range, and performance.
50. Explain the difference between Python’s unbounded integer bit semantics and a 32-bit protocol field. Implement explicit unsigned wrapping and signed interpretation.

### 5.21.11 Text and bytes

51. Construct two canonically equivalent strings with unequal code-point sequences. Show lengths, UTF-8 bytes, normalised equality, and original preservation.
52. Find a grapheme cluster containing several code points. Reverse it by code point and explain why the visual or linguistic result is defective.
53. Compare <code>split()</code> with <code>split(",")</code> on leading, trailing, repeated, and whitespace separators. Derive the admitted record grammar for each.
54. Demonstrate why <code>strip("prefix")</code> is not prefix removal. Replace it with the exact operation and define absent-prefix behaviour.
55. Decode invalid UTF-8 under strict, replacement, and ignore policies. State exactly what information each result preserves or destroys.
56. Create a binary record using <code>struct</code>. Include byte order, field width, signedness, range checks, and length validation in its specification.
57. Use <code>memoryview</code> to mutate part of a bytearray without copying. Identify every alias and explain the exporter’s resize restriction.
58. Design a boundary that decodes once, performs Unicode-domain operations, and encodes once. Explain why <code>str(bytes_value)</code> violates it.

### 5.21.12 Calls, typing, and validation

59. Trace callable lookup, receiver evaluation, argument evaluation, signature binding, function-body entry, and return for a method call.
60. Construct a call using two starred positional sources and two double-starred mappings. Predict the resulting argument sequence and then introduce a duplicate keyword.
61. Demonstrate that argument effects can occur before duplicate binding raises <code>TypeError</code>. State which function body does not run.
62. Repair a mutable-default defect using <code>None</code>, then repair a case where explicit <code>None</code> is valid using a private sentinel.
63. Design one positional-only and two keyword-only parameters for an API. Justify the compatibility and readability consequences.
64. Give a protocol-based function that works for two unrelated classes. State the full behavioural contract rather than only method names.
65. Construct a case where <code>isinstance(value, int)</code> admits Boolean input contrary to a domain rule. Implement layered rejection.
66. Separate parsing, type admission, range validation, and cross-field validation for an original command input.

### 5.21.13 Evidence and integrated mastery

67. Take five observations involving identity, object size, hash, bytecode, and source path. Classify each as language, implementation, environment, or experiment.
68. Compare an AST and CPython disassembly for one constant expression. Explain why compiler folding cannot be required by source semantics.
69. Write a portability ledger for the integrated state trace in §5.19. Include the normative evidence required for every language claim.
70. Construct a program containing aliasing, shallow copying, augmented assignment, a definition-time default, a chained comparison, text decoding, and a handled arithmetic failure. Predict every binding, mutation, effect, and output before execution.
71. Extend the Chapter 3 computational dossier and Chapter 4 workshop dossier with a Chapter 5 semantic dossier: token structure, parse grouping, evaluation order, object graph, representation boundaries, failure points, language-versus-implementation classification, and independent oracles.
72. Review an unfamiliar twenty-line Python program using the fifteen-question semantic proof-obligation checklist. Do not execute it until the complete trace and predictions are recorded; then reconcile every deviation.
