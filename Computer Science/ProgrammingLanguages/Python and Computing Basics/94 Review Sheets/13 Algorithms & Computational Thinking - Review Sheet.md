# 13.20 Common misconceptions consolidated

1. **“Big-O is running time.”** It is a growth bound under a cost model.
2. **“Ignore constants means constants never matter.”** They disappear from asymptotic class but dominate finite performance often.
3. **“Two nested loops always mean (O(n^2)).”** Bounds depend on iteration counts and shared progress; two-pointer loops can be linear.
4. **“Binary search works on anything ordered.”** It requires a coherent sorted invariant and efficient access to the chosen middle.
5. **“Stable sort means values do not move.”** Equal-key elements preserve relative order; other positions change.
6. **“Linked-list insertion is (O(1)), so linked lists are faster.”** Finding the insertion point, allocation, locality, and workload matter.
7. **“A heap is a sorted list.”** It maintains parent priority, sufficient for extremum access, not global order.
8. **“BST operations are (O(\log n)).”** They are (O(h)); without balance, height can be linear.
9. **“BFS and DFS differ only in queue spelling.”** Their frontier order establishes different semantic properties.
10. **“Dijkstra works if negative edges are rare.”** One negative edge can invalidate the settled-distance proof.
11. **“Greedy means choose what looks best.”** Correctness requires an exchange, cut, matroid, or other structural argument.
12. **“Dynamic programming is recursion plus a cache.”** It requires a state definition, recurrence, base cases, dependency order, and complexity proof.

### 13.20.1 Misconceptions arise from crossing abstraction levels

Most algorithmic errors in prose can be traced to an unstated movement between levels:

| Level | Legitimate question | Typical invalid leap |
|---|---|---|
| problem | what outputs satisfy the contract? | treating one implementation’s behaviour as the problem definition |
| algorithm | what abstract operations and invariants solve it? | assuming a Python expression is one abstract operation |
| representation | how are values, edges, nodes, or states stored? | transferring an array bound to a linked representation |
| language specification | what behaviour does Python promise? | treating a CPython layout as portable semantics |
| implementation | what does CPython 3.12 currently do? | presenting a current strategy as timeless |
| machine/workload | what resource use is observed here? | generalising one measurement to all inputs and systems |

For example, “membership is constant-time” may mean expected hash-table probes under a distribution model, a measured median on one dictionary, or a mistakenly alleged Python guarantee. The sentence becomes defensible only after selecting a level:

> Under controlled load and ordinary hash-distribution assumptions, a conventional hash table performs expected \(O(1)\) equality/probe work per membership query; its worst case is \(O(n)\).

This statement does not claim that hashing a key is constant in key length, that resizing never occurs, or that wall-clock latency has no tail.

The corrective discipline is to name the noun being bounded. Instead of “this is linear”, write “the loop performs exactly \(n\) predicate calls”, “the function retains \(O(n)\) references”, or “the adjacency-list traversal examines each reachable vertex and outgoing edge once, subject to expected constant dictionary operations”.

### 13.20.2 Syntactic shape is evidence only after semantic counting

Source syntax suggests hypotheses, not bounds. A loop can be:

- constant-time because it returns on the first iteration under a precondition;
- logarithmic because its remaining domain shrinks geometrically;
- linear because an index advances once per input item;
- \(n\log n\) because each item participates at each of logarithmically many levels;
- quadratic because it visits all pairs;
- exponential because each state branches into independent subcases;
- non-terminating because no well-founded progress exists.

Nested loops likewise range from linear monotone-stack behaviour to cubic matrix processing. Recursion ranges from logarithmic binary search depth to exponential repeated Fibonacci calls. The method is always:

1. choose input variables and charged operations;
2. express repetition as a count, sum, or recurrence;
3. solve or bound that mathematical object;
4. restore hidden operation costs when the application requires them.

Consider duplicate detection:

~~~python
def contains_duplicate(values: list[object]) -> bool:
    observed: set[object] = set()
    for value in values:
        if value in observed:
            return True
        observed.add(value)
    return False
~~~

The loop is visibly linear in iterations, but the complete claim is conditional. With hashable stable keys and expected bounded collision behaviour, it performs expected \(O(n)\) table work and retains \(O(n)\) references. Worst-case table work can be \(O(n^2)\) across adversarial collisions. Hash computation may depend on value size. An unhashable element raises before a Boolean result. Equality or hashing can execute user code. The set loses encounter multiplicity internally, though the Boolean output does not require retaining it.

A pairwise nested-loop version has unconditional \(\Theta(n^2)\) equality comparisons in its no-duplicate case but accepts unhashable values. Neither implementation is simply “better”; their admitted domains and resource risks differ.

### 13.20.3 Correctness errors cluster around omitted obligations

A proof-like explanation should be audited for six omissions:

| Obligation | Audit question |
|---|---|
| domain | are all required ordering, finiteness, mutability, and numeric assumptions stated? |
| initialisation | why is the invariant true before any transition? |
| preservation | does every branch, including exceptional control flow, preserve it? |
| progress | what well-founded measure prevents infinite execution? |
| exit | why do invariant and exit condition imply the complete postcondition? |
| preservation of content | does the output retain exactly the required inputs, multiplicities, identities, or edges? |

A sorted-output proof that omits permutation preservation permits fabricated values. A shortest-path proof that shows the returned route is feasible but not minimal proves too little. A greedy proof that argues the first choice “leaves room” without transforming an arbitrary optimum leaves the central theorem unsupported. A dynamic-programming recurrence that lists attractive branches but does not prove them exhaustive can omit the optimum.

Exceptions must be included when the contract cares about state. An in-place algorithm may establish its postcondition only on normal return. If a comparison raises after partial mutation, the exceptional postcondition might promise merely that the object remains a valid list, not that original order is restored. Transactional requirements need a copy, undo log, validation phase, or stronger algorithm.

### 13.20.4 Probabilistic words are not synonyms

The following claims answer different questions:

- average-case \(O(f(n))\): expectation over a declared input distribution;
- expected \(O(f(n))\): often expectation over internal random choices for each fixed input;
- amortised \(O(f(n))\): deterministic total bound over an operation sequence;
- with high probability: failure probability decreases according to a stated function of size;
- empirical mean or median: statistic calculated from observed runs;
- typical: informal and unacceptable without an operational definition in a rigorous claim.

Randomised quicksort and hash tables illustrate why qualifiers cannot be deleted. A random pivot makes bad partition sequences unlikely without changing the existence of a quadratic execution. A keyed hash can make deliberate collisions difficult for selected built-in keys without turning worst-case probe length into a constant. A dynamic array has amortised constant append even when inputs are chosen adversarially, because the resizing proof does not rely on probability.

When reporting expectation, name the probability space. “Expected \(O(n\log n)\)” could average over input permutations, pivot choices, hash functions, scheduler timing, or workload requests. Each supports different conclusions.

### 13.20.5 Data-structure folklore omits the operation sequence

A data structure is a bundle of trade-offs. Isolated operation slogans obscure required access:

| Slogan | Missing qualification |
|---|---|
| linked insertion is constant | only after the insertion location or predecessor is already known |
| BST lookup is logarithmic | only with a height bound; ordinary BST height can be \(n\) |
| heap removal is logarithmic | extremum removal is; arbitrary-item location is not supplied |
| list append is constant | amortised under geometric capacity management |
| set membership is constant | expected under hashing assumptions, with hash/equality cost separated |
| binary search is logarithmic | needs monotone order and sufficiently direct indexed access |
| BFS is linear | in \(V+E\) for an adjacency representation and the traversed graph portion |

Workload analysis begins by listing operations and frequencies. A sorted array offers excellent iteration and binary search, but interior insertion shifts a suffix. A balanced tree offers logarithmic ordered updates with allocation and locality costs. A dictionary offers equality lookup without sorted-key range traversal. A database B-tree persists pages and supports range queries while imposing I/O and transaction costs. No asymptotic slogan substitutes for that matrix.

### 13.20.6 Determinism, stability, and correctness are orthogonal

A correct algorithm may return any of several valid answers. Determinism requires selecting the same answer under a defined environment and input representation. Stability is one particular tie-preservation property for sorting. Canonicalisation selects one representation among equivalent ones.

A topological sort can be correct but vary with hash iteration order. A heap can correctly remove minimum priorities while varying equal-priority task order. BFS can return different shortest paths of equal length. Adding lexical or sequence-number ties creates reproducibility, sometimes at an extra \(O(\log V)\) heap cost or additional key storage.

Determinism is valuable for tests, caches, reproducible builds, and user expectations, but it is not automatically part of mathematical correctness. Conversely, deterministic output can be consistently wrong. State each property independently.

### 13.20.7 A compact audit procedure

Before accepting or publishing an algorithmic claim, perform this audit:

- restate the exact problem, including failure and mutation;
- identify encoded size variables and output size;
- name the cost model and charged operations;
- state worst, best, average, expected, or amortised qualifier;
- give the invariant or structural proof of correctness;
- prove termination separately;
- derive the bound rather than inferring it from syntax;
- identify representation assumptions and operation costs;
- separate Python guarantees from CPython facts;
- test boundary, adversarial, and generated small instances;
- measure representative implementations only after semantic equivalence is established;
- label the final statement by evidence category.

This procedure does not make sophisticated algorithms mechanical. It makes gaps visible. A visible gap can be proved, tested, constrained, or documented; an implicit one becomes folklore.
