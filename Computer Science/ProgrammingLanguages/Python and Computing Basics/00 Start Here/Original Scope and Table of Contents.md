# Computing and Python: Foundations to Mastery

## Scope and editorial standard

This is a single cumulative treatise issued in forty physical volumes for manageability. “Volume” is a binding and pagination unit, not an independent course: the mandatory trunk remains one unbroken dependency chain. The canonical edition targets **at least 4,200 densely typeset pages**, excluding indexes, blank leaves, and answer-key duplication. At an editorial density of approximately 430–500 words per main-text page after allowing for code, tables, diagrams, exercises, and references, the completed work requires approximately two million words of substantive content. Page count is not created by enlarged type, repeated templates, or one paragraph per page.

The prose adopts general conventions found in rigorous university texts: definitions precede dependent claims; abstractions are derived from the problems they solve; worked examples expose intermediate state; claims are qualified by their domain; exercises require proofs, constructions, experiments, and transfer; and bibliographic notes distinguish language specifications, implementation documentation, standards, and empirical observations. These are genre conventions, not imitation of any individual author’s phrasing.

The forty-volume binding plan is:

| Volumes | Contents | Canonical page budget |
|:---|:---|---:|
| I–III | Chapter 1: physical computation, digital logic, architecture | 360 |
| IV–V | Chapter 2: machine software and operating systems | 240 |
| VI–VII | Chapter 3: programs, algorithms, data, and computability | 220 |
| VIII | Chapter 4: the Python workshop | 120 |
| IX–XI | Chapter 5: Python syntax, semantics, and object foundations | 360 |
| XII–XIII | Chapter 6: control flow, iteration, generators, exceptions | 240 |
| XIV–XVI | Chapter 7: built-in structures, implementations, and costs | 360 |
| XVII–XIX | Chapter 8: functions, scope, closures, and decorators | 330 |
| XX–XXII | Chapter 9: objects, protocols, descriptors, and metaclasses | 350 |
| XXIII | Chapter 10: modules, packages, imports, and distribution | 130 |
| XXIV–XXV | Chapter 11: I/O, serialisation, resources, and the standard library | 250 |
| XXVI–XXVIII | Chapter 12: testing, debugging, Git, style, types, documentation | 350 |
| XXIX–XXXII | Chapter 13: correctness, complexity, structures, and algorithms | 480 |
| XXXIII–XXXV | Chapter 14: concurrency, parallelism, and performance | 330 |
| XXXVI–XXXVII | Chapter 15: CPython internals and native boundaries | 250 |
| XXXVIII | Branch A and Branch B: data science and machine learning | 180 |
| XXXIX | Branch C and Branch D: web development and cybersecurity | 180 |
| XL | Branch E, capstone syntheses, references, and indexes | 160 |
| **Total** | **Main work before uncounted blank matter** | **5,040 pages** |

The budget intentionally exceeds 4,000 pages by a substantial margin. It permits later copy-editing and consolidation without forcing the canonical edition below the requirement.

## Table of Contents

### The mandatory trunk

The trunk is linear. Each chapter presupposes every preceding trunk chapter; none is optional.

1. **The Physical Computer**
   1. Matter as a controllable signal
   2. Transistors and switching
   3. Boolean values and logic gates
   4. Binary representation
   5. Combinational and sequential circuits
   6. The stored-program computer
   7. CPU, memory, buses, and input/output
   8. Clock cycles and the fetch–decode–execute cycle
   9. Worked machine trace
   10. Misconceptions, exercises, and cumulative glossary
2. **From Hardware to Software**
   1. Instruction sets and machine code
   2. Assembly language and assemblers
   3. Why higher-level languages exist
   4. Compilation, interpretation, and just-in-time compilation
   5. Operating systems, kernels, and user space
   6. Processes, virtual memory, filesystems, and device mediation
3. **Programs, Algorithms, and Data**
   1. Problems, instances, specifications, algorithms, and executions
   2. Algorithms and data as the two irreducible ingredients
   3. Correctness, termination, and informal Turing-completeness
   4. Terminals, shells, commands, streams, and exit status
4. **Constructing a Python Workshop**
   1. Python implementations and version selection
   2. Installing and locating Python
   3. Interpreter sessions, the REPL, and scripts
   4. Project directories and filesystem conventions
   5. Virtual environments, `pip`, dependencies, and reproducibility
5. **Python Syntax and Semantics from First Principles**
   1. Source text, tokens, grammar, expressions, and statements
   2. Values, objects, identities, and types
   3. Names and bindings rather than boxes
   4. Mutability, immutability, aliasing, copying, equality, and identity
   5. Numeric, Boolean, text, byte, and null-like values
6. **Control Flow and Computation over Time**
   1. Truth testing and conditional execution
   2. Repetition with `while` and `for`
   3. Iterables, iterators, and generators
   4. Comprehensions and lazy pipelines
   5. Exceptions and structured error handling as control flow
7. **Built-in Data Structures and Their Costs**
   1. Lists and dynamic arrays
   2. Tuples and immutable records
   3. Dictionaries and hash tables
   4. Sets and frozensets
   5. Strings and Unicode-aware sequence behaviour
   6. Selection by invariant and operation cost
8. **Functions, Scope, and Abstraction**
   1. Function definitions, calls, parameters, and arguments
   2. Return values, side effects, and contracts
   3. Frames, namespaces, and LEGB name resolution
   4. First-class functions and closures
   5. Recursion and the call stack
   6. Decorators derived rather than memorised
9. **Objects, Classes, and the Python Data Model**
   1. Classes and instances
   2. Attribute lookup and method binding
   3. Inheritance, composition, and polymorphism
   4. Special methods and protocols
   5. Object construction with `__new__` and `__init__`
   6. Descriptors and metaclasses as the capstone
10. **Modules, Packages, Imports, and Distribution**
    1. Module objects and import execution
    2. Packages, relative imports, and public APIs
    3. `__name__ == "__main__"`
    4. `pyproject.toml`, builds, wheels, and publication
11. **Data and the Outside World**
    1. Bytes, text, encodings, files, buffering, and streams
    2. Paths and filesystem operations
    3. JSON, CSV, and pickle
    4. Context managers and resource lifetimes
    5. Systematic use of `pathlib`, `collections`, `itertools`, `functools`, and `dataclasses`
12. **Software Engineering Discipline**
    1. Requirements and maintainable design
    2. Unit, integration, property, and acceptance tests
    3. `pytest` and test doubles
    4. Debugging as hypothesis testing
    5. Git as a model of change
    6. PEP 8, documentation, type hints, and static analysis with `mypy`
13. **Computational Thinking and Algorithms**
    1. Cost models and asymptotic notation
    2. Correctness proofs, loop invariants, and induction
    3. Searching and sorting
    4. Linked lists, stacks, queues, and heaps
    5. Trees and graphs
    6. Greedy reasoning and dynamic programming
14. **Concurrency and Performance**
    1. Concurrency, parallelism, latency, and throughput
    2. Threads, locks, races, and deadlocks
    3. Processes and inter-process communication
    4. Coroutines, tasks, event loops, and `asyncio`
    5. The CPython GIL, including free-threaded builds
    6. Measurement, profiling, memory behaviour, and native escape hatches
15. **Inside CPython**
    1. Parsing, abstract syntax trees, and compilation
    2. Code objects, bytecode, frames, and the evaluation loop
    3. Object representation and reference counting
    4. Cyclic garbage collection
    5. Extension boundaries and a final unifying execution trace

### Optional branches

Each branch is a departure from the trunk. A branch may be omitted without creating a gap in another branch.

16. **Branch A — Data Science and Numerical Computing**  
    **Dependency map:** requires Chapters 1–15, with direct reliance on Chapter 7 (data structures and cost), Chapter 11 (external data), Chapter 12 (testing and types), Chapter 13 (complexity), and Chapter 14 (performance).
    1. Numerical representation and statistical vocabulary
    2. NumPy arrays, shapes, dtypes, strides, and vectorisation
    3. pandas indexes, tabular transformation, missingness, and joins
    4. Visualisation, inference, uncertainty, and reproducible analysis
17. **Branch B — Machine Learning**  
    **Dependency map:** requires the complete trunk, Chapters 1–15. Chapters 8–9 supply callable and object models; Chapters 12–14 supply verification, algorithmic, and cost reasoning. Branch A is optional: this branch restates the numerical and statistical concepts it needs.
    1. Learning as empirical risk minimisation
    2. Features, targets, estimators, fitting, and prediction
    3. Train/validation/test separation and leakage
    4. scikit-learn pipelines and evaluation
    5. Gradients, optimisation, neural networks, and framework semantics
18. **Branch C — Web Development**  
    **Dependency map:** requires Chapters 1–15, with direct reliance on Chapter 2 (processes and operating systems), Chapter 10 (packages), Chapter 11 (I/O and serialisation), Chapter 12 (engineering discipline), and Chapter 14 (concurrency).
    1. Networks, HTTP, URLs, requests, and responses
    2. WSGI, ASGI, and application servers
    3. Flask as a minimal framework and Django as an integrated framework
    4. Relational databases, transactions, and ORMs
    5. REST, GraphQL, authentication, deployment, and observability
19. **Branch D — Cybersecurity**  
    **Dependency map:** requires Chapters 1–15. Chapters 1–2 provide the hardware/OS trust model; Chapters 5–11 provide the language and I/O attack surface; Chapters 12 and 14 provide verification, isolation, and concurrency reasoning.
    1. Assets, adversaries, authority, and trust boundaries
    2. Memory and operating-system foundations of vulnerability
    3. Injection, traversal, deserialisation, and dependency risks
    4. Cryptographic primitives and safe library use
    5. Defensive reconnaissance and automation under explicit authorisation
20. **Branch E — Systems and DevOps**  
    **Dependency map:** requires Chapters 1–15, with direct reliance on Chapter 2 (processes and filesystems), Chapter 4 (environments), Chapter 10 (packaging), Chapter 12 (version control and tests), and Chapter 14 (concurrency and performance).
    1. Processes, signals, configuration, and service boundaries
    2. Containers and images
    3. Continuous integration and continuous delivery
    4. Infrastructure as code and cloud SDKs
    5. Reliability, telemetry, rollback, and incident reasoning

---

# Part I — The Mandatory Trunk
