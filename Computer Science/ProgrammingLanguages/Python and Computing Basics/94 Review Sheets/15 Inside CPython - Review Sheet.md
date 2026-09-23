# 15.21 Common misconceptions consolidated

1. **“Bytecode is Python’s machine code.”** It is a CPython interpreter representation; the physical CPU executes CPython’s native code.
2. **“`co_consts` stores variables.”** It stores compiler-selected constant references; runtime local bindings live in frames.
3. **“Constant means immutable forever and globally.”** In code-object terminology it means embedded compiled metadata under implementation constraints.
4. **“`co_consts` order is source semantics.”** It is compiler detail and can change through folding and version changes.
5. **“One bytecode instruction is one CPU instruction.”** It can invoke extensive C and Python machinery.
6. **“Frames are dictionaries.”** The language exposes local namespaces; CPython uses optimised frame storage and mapping views.
7. **“Reference counting is Python’s garbage-collection rule.”** It is CPython’s principal mechanism; the language does not promise immediate reclamation.
8. **“Deleting a name decrements the only reference.”** Other names, containers, frames, caches, or native owners may retain the object.
9. **“The cyclic collector finds all memory leaks.”** It finds selected unreachable cycles; reachable but unwanted state remains live.
10. **“Free-threaded CPython makes code automatically parallel and correct.”** It permits parallel execution; synchronisation, workload, and extension support remain necessary.
11. **“A lower-level explanation is more real.”** Each level answers a different contract question; implementation details do not invalidate language semantics.

### 15.21.1 Compilation and namespace corrections

12. **“The AST determines the value of every expression.”** It records semantic syntax. Name lookup, descriptor dispatch, argument values, exceptions, and external state remain runtime matters.
13. **“A tokenizer is a parser with less output.”** Lexical analysis classifies tokens and indentation; parsing establishes grammatical nesting and produces structural syntax. Either can reject input for different reasons.
14. **“A Store context names a physical storage address.”** It marks a syntactic target role. Symbol classification or object protocols determine the eventual binding/mutation mechanism.
15. **“A branch can change a name from global to local at runtime.”** The whole block is classified statically. Paths affect whether a local has acquired a value, not its category.
16. **“A closure keeps the complete outer call frame.”** It ordinarily keeps only required cells, while a traceback, explicit frame, or suspended execution may retain a frame independently.
17. **“A class dictionary lexically encloses methods.”** Unqualified method names do not normally search it; instance/class attribute access invokes the appropriate lookup protocol.
18. **“Defaults, decorators, annotations, and bodies all execute together.”** Their evaluation phases differ. Definition execution evaluates/assembles surrounding components; later calls execute the body.
19. **“Code objects carry the globals they use.”** Function objects carry a globals mapping. Code objects carry name metadata and operations that request lookup.
20. **“Stack size measures recursion depth.”** <code>co_stacksize</code> concerns temporary evaluation-stack entries for one code object, not Python call depth or native stack bytes.

### 15.21.2 Interpreter and protocol corrections

21. **“An opcode name fully states its work.”** Generic operations can call descriptors, numeric slots, iterators, allocators, and arbitrary Python fallback code.
22. **“Warm disassembly proves the same specialisation will occur in production.”** Workload, types, tracing, build and version govern adaptive state; the observation is conditional.
23. **“A cache stores an operation’s prior return value.”** Inline caches commonly retain structural/type evidence and indices, not semantic results.
24. **“A public frame object is the evaluator’s only activation record.”** Modern CPython separates efficient interpreter-frame state from materialised introspection objects.
25. **“Writing frame.f_locals is a portable debugger assignment.”** Optimised-local synchronisation has version-specific semantics; use supported debugger interfaces for the target version.
26. **“A Python exception is represented solely by a C return value.”** Native failure uses an error sentinel plus thread-state exception information under each API contract.
27. **“A finally suite runs only after an exception.”** It also runs during normal completion and control transfers such as return; its own exception can replace the active outcome with context.
28. **“Catching Exception catches process-exit and keyboard interruption.”** Several control exceptions derive directly from <code>BaseException</code> so ordinary recovery does not swallow them.
29. **“Import failure restores the process to its prior state.”** The failing cache entry is handled, but successfully imported dependencies and arbitrary side effects can persist.
30. **“Reload gives every client the new class and function objects.”** External references remain bound to old objects; the existing module dictionary can also retain obsolete names.

### 15.21.3 Representation and lifetime corrections

31. **“PyObject is the complete layout of any value.”** It is a common API prefix/model. Concrete types add fields, arrays, separate buffers, alignment, and possibly GC metadata.
32. **“A variable-size object is mutable.”** Size describes allocated representation. Tuples and integers vary in allocation size while remaining immutable at Python level.
33. **“String length is byte length.”** Python length counts code points; encodings produce separate byte lengths, and grapheme clusters are another concept.
34. **“Dictionary insertion order comes from hashing as a language necessity.”** Order is a semantic guarantee now; compact ordered tables are one CPython mechanism capable of satisfying it.
35. **“A hash collision means two keys are equal.”** Collisions merely share a hash; equality resolves candidate keys. Equal keys must hash equally, not conversely.
36. **“An owned reference means a newly allocated object.”** It means an independent lifetime claim; a new reference can point to an existing object.
37. **“A borrowed reference is a weak reference.”** Borrowing is a native ownership convention with a validity interval; a weak reference is an object that observes death safely.
38. **“Reference-count zero is reached for every unreachable graph.”** Internal strong edges keep counts positive in cycles, requiring cyclic graph analysis.
39. **“Immortal objects exempt extension code from ownership rules.”** Correct code must work for mortal objects too; public increment/decrement conventions remain mandatory.
40. **“An untracked object is outside memory management.”** It remains reference-counted/allocated; it is merely excluded from cyclic traversal at that moment.
41. **“A finaliser runs once at a predictable source line.”** It can be delayed, triggered by an unrelated release, suppressed by shutdown, resurrect its owner, or fail unraisably.
42. **“Weak-value caching guarantees one canonical live instance.”** Concurrent get/create/store needs synchronisation, and a value can vanish whenever independent strong ownership ends.
43. **“Resident memory equals the sum of live Python object sizes.”** It includes allocator reserves, native buffers, code, mappings, stacks, fragmentation, and shared pages under OS accounting.

### 15.21.4 Concurrency and evidence corrections

44. **“The GIL is a mutex around each Python source statement.”** It is interpreter implementation synchronisation; operations can span, release, or execute without it, and free-threaded builds remove the premise.
45. **“Built-in container locking creates application transactions.”** Internal locks protect representation integrity. A multi-operation invariant needs its own lock or transaction protocol.
46. **“A subinterpreter is a security sandbox.”** It partitions interpreter state but shares a process, native libraries, descriptors, address space, and many operating-system resources.
47. **“Free-threading means no locks.”** It replaces one broad lock with fine-grained locks, atomics, stop-the-world phases, ownership mechanisms, and application synchronisation.
48. **“Vectorcall skips signature checks.”** It compacts argument transport; the callee must still implement call binding and errors.
49. **“Debug builds give production performance evidence.”** They expose invariants and memory errors but change layout and overhead. Release and debug builds answer different questions.
50. **“A benchmark explains its result.”** Timing is observation. A causal explanation requires controlled variables, profiler/counter evidence, alternative hypotheses, and reproducibility.
51. **“The newest source tree explains the deployed Python.”** Deployment must be matched by version, commit, build, extensions and configuration; current main-branch code can differ fundamentally.
52. **“A PEP is always the current specification.”** Status, acceptance, subsequent amendments, documentation, and implementation matter. Historical PEPs explain design but do not freeze private mechanisms.
53. **“Internal knowledge licenses application dependence.”** Understanding a mechanism can guide measurement and extension work; portable application code still targets the highest adequate documented interface.

These corrections share one discipline: identify the abstraction boundary before stating causality. The exercises now require the reader to reproduce that discipline rather than recite structure names.
