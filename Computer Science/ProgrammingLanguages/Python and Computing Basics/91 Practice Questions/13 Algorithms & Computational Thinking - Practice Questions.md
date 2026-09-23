# 13.21 Exercises

### 13.21.1 Complexity and proof

1. Prove from the formal definition that (7n+20\in O(n)) by giving constants.
2. Give tight (Theta) bounds for triangular nested loops, halving loops, and two pointers that each advance at most (n) times.
3. Analyse integer addition when input size is bit length rather than treating arbitrary integers as constant-time.
4. Produce aggregate or potential-method amortised reasoning for dynamic-array append.
5. Write an invariant that is true but insufficient for a sorting loop, then strengthen it until the postcondition follows.

### 13.21.2 Search and sort

6. Implement and prove lower and upper bound binary searches using half-open intervals.
7. Create minimal counterexamples for four off-by-one binary-search mutations.
8. Prove insertion-sort stability and give the exact comparison count for reversed distinct input.
9. Implement merge sort without slicing and compare allocation behaviour.
10. Derive the comparison-sorting lower bound using a decision tree in your own words.

### 13.21.3 Data structures

11. Add removal, indexing, and invariant checking to the linked list. State every cost including search.
12. Prove Floyd cycle detection’s meeting claim and locate the cycle entry as an extension.
13. Implement a binary heap from scratch with sift-up and sift-down; prove the array-index formulae.
14. Add deletion and resizing to the teaching hash map. Design adversarial colliding keys and measure chain lengths.
15. Implement a balanced-tree rotation and state which ordering relationships it preserves.

### 13.21.4 Graphs

16. Implement BFS parents and reconstruct a shortest unweighted path.
17. Use DFS colour states to detect a directed cycle and produce the cycle.
18. Implement Kahn topological ordering with deterministic lexical tie-breaking.
19. Construct the smallest graph demonstrating Dijkstra failure with a negative edge.
20. Compare adjacency matrix and list costs for dense and sparse graphs under several operations.

### 13.21.5 Greedy and dynamic programming

21. Prove earliest-finish interval scheduling with an exchange argument and defeat two tempting alternatives.
22. Design a dynamic program for longest common subsequence: state, recurrence, base, order, reconstruction, and cost.
23. Compare top-down memoisation and bottom-up evaluation for minimum coins.
24. Explain pseudo-polynomial complexity using target bit length.

### 13.21.6 Integrated exercise

25. Build a dependency planner. Parse a directed project graph, detect cycles with an explanatory path, produce deterministic topological order, compute earliest completion under task durations, and answer reachability queries. Choose representations, prove every algorithm, state (V/E) time and space, implement from scratch before using library helpers, test adversarial graphs, package the result, and benchmark only after completing the cost analysis.

### 13.21.7 Cost models and asymptotic notation

26. Define a cost model for comparing two lists of arbitrary-size non-negative integers lexicographically. Give one bound in element comparisons and a refined bound using total bit length. Construct inputs on which the two descriptions differ materially.

27. A function reads \(n\) compressed records and emits \(z\) decompressed bytes. Identify at least three defensible input-size variables and derive a bound that exposes output cost. Explain why a bound solely in \(n\) could be misleading.

28. Prove directly from the quantified definitions that \(4n^3+7n\in\Theta(n^3)\). Give explicit witnesses for both directions, then explain why \(O(n^4)\) is true but weaker.

29. Determine whether each claim is true and prove or refute it: \(n\log n\in O(n^{3/2})\); \(2^n\in O(3^n)\); \(n!\in O(n^n)\); \(\log(n!)\in\Theta(n\log n)\).

30. Construct two non-negative functions \(f\) and \(g\) such that neither belongs to \(O\) of the other. Your functions should alternate dominance infinitely often. State why the usual growth hierarchy does not imply every possible pair is comparable.

31. Analyse a loop whose index progresses as \(i\leftarrow i+\lfloor\sqrt i\rfloor+1\). Derive a tight bound rather than classifying it from surface syntax. Justify any summation or integral comparison used.

32. For a rectangular \(r\times c\) matrix multiplication implemented with three loops, state bounds in \(r,c,k\) for multiplying an \(r\times k\) matrix by a \(k\times c\) matrix. Explain when compressing all dimensions to \(n\) is legitimate.

33. Compare a sequential \(O(n)\) scan requiring one storage-block transfer per \(B\) contiguous records with \(O(\log n)\) binary search requiring one random transfer per comparison. Develop a symbolic break-even inequality using sequential and random-transfer costs.

34. An API accepts an integer \(N\) in decimal and loops from 1 through \(N\). Express its time in numeric magnitude, decimal-character input length, and binary bit length. Classify whether it is polynomial in each measure.

35. Give an output-sensitive analysis for generating every pair of database rows sharing a key. Include input rows \(n\), index construction, number of groups, and output pairs \(z\). Identify a worst case for \(z\).

36. Prove the change-of-base result for logarithms and use it to explain both why asymptotic classes ignore the base and why an exact comparison count may not.

37. Analyse the total body executions of a loop that, for each \(i=1,\ldots,n\), visits multiples \(i,2i,\ldots,\lfloor n/i\rfloor i\). Establish a \(\Theta(n\log n)\) bound through harmonic sums.

38. Design a family of inputs showing that a linear-time algorithm with a large setup constant can lose to a quadratic algorithm across a specified finite range. Do not use this example to deny their asymptotic ordering; calculate the crossing point.

39. Classify seven claims from published-looking prose as definition, derivation, specification rule, implementation fact, empirical observation, modelling assumption, or judgement. Rewrite each so its evidential status is explicit.

40. Integrate Chapters 5, 7, and 12: build an instrumented comparison object that counts less-than and equality calls, use it to audit a search and a sort, and explain why the instrumentation itself can perturb time measurements without changing comparison counts.

### 13.21.8 Recurrences, amortisation, and proof

41. Solve \(T(n)=T(n-1)+n\) by expansion and induction. Give a tight bound and compare its recursion depth with \(T(n)=2T(n/2)+n\).

42. Solve \(T(n)=3T(n/2)+n\) for powers of two by a recursion tree and the Master theorem. Identify which term dominates and verify the proposed result by substitution.

43. Explain why the standard Master theorem does not directly cover \(T(n)=T(n/3)+T(2n/3)+n\). Use a recursion-level argument to derive a plausible tight bound, carefully controlling branch depth.

44. Derive exact operation counts for binary exponentiation on a positive exponent using its binary representation. Distinguish squarings, multiplications, bit inspections, and arbitrary-precision operand costs.

45. Use aggregate analysis to show that any sequence of \(m\) pushes, pops, and multi-pops on an initially empty stack costs \(O(m)\). State how the theorem changes when the initial stack contains \(n\) elements.

46. Construct an accounting proof for a dynamic array growing by a factor of two. Choose explicit credits, show they never become negative, and state which primitive writes and copies are charged.

47. Develop a potential function for a queue implemented with two stacks. Prove amortised \(O(1)\) enqueue and dequeue while acknowledging that one dequeue can move \(\Theta(n)\) items.

48. Show how resizing a table at occupancy one half in both directions can thrash. Give an alternating operation sequence, then propose separated thresholds and outline a potential proof.

49. For the maximum-scan implementation, write its precondition, normal and exceptional postconditions, frame condition, loop invariant, and variant. Identify the assumptions made about comparison methods.

50. Prove Euclid’s greatest-common-divisor algorithm totally correct. Use a loop invariant based on common divisors and a non-negative decreasing variant; refine the cost model to bit operations as an extension.

51. Give a minimal counterexample to each of four faulty binary-search updates. For every fault, state which invariant clause or progress obligation fails.

52. Prove insertion sort by a nested pair of invariants: one for the outer prefix and one for the shifting inner loop. Include multiset preservation and stability.

53. Translate recursive tree-height computation into structural induction. Then explain why the same recursion may not terminate on an arbitrary cyclic node graph.

54. Use a tournament argument to prove that finding a maximum among \(n\) distinct elements needs at least \(n-1\) comparisons. Extend the tournament record to find the second-largest value with at most \(n+\lceil\log_2 n\rceil-2\) comparisons when \(n\) is a power of two.

55. Integrate testing discipline: express five algorithm invariants as executable assertions, generate small exhaustive state spaces, and explain precisely why exhaustive testing up to size \(k\) is not a proof for all sizes.

### 13.21.9 Searching, selection, and sorting

56. Implement predicate-based linear search with an explicit result type that distinguishes an absent result from a found value equal to <code>None</code>. Compare raising, sentinel, and tagged-union APIs.

57. Implement a streaming search that returns the first matching index without retaining prior elements. Test its consumption behaviour on generators after success, failure, and predicate exception.

58. Given \(q\) membership queries and \(n\) immutable records, derive symbolic cost inequalities comparing scans, a sorted copy plus binary search, and a hash index. Include key-extraction cost and memory constraints.

59. Implement <code>lower_bound</code>, <code>upper_bound</code>, equal-range, predecessor, and successor using one partition-point primitive. Prove the boundary conditions for empty input and all-equal input.

60. Adapt exponential search to an unbounded monotonically indexed source that raises on unavailable positions. State what must be known about eventual predicate truth and exception semantics.

61. Compare standard-library <code>bisect</code> with a hand-written lower bound on records whose key derivation is expensive. Measure key-call counts using a counter and evaluate caching or parallel-key arrays.

62. Implement stable selection sort without swapping the selected minimum across equal elements. Derive its movement cost and compare it with the unstable implementation.

63. For insertion sort, prove that the number of shifts equals the input inversion count. Use this fact to derive its best and worst movement bounds.

64. Implement bottom-up merge sort using one auxiliary array and no slicing. Add a key function evaluated exactly once per item and prove stability under equal keys.

65. Implement an in-place quicksort with three-way partitioning. State its partition invariant, handle duplicate keys, avoid unbounded recursive depth by processing the smaller partition recursively, and analyse remaining worst cases.

66. Empirically compare first-element, median-of-three, and random pivots on sorted, reversed, equal, organ-pipe, and shuffled inputs. Report comparison distributions without claiming the experiment proves asymptotic bounds.

67. Prove bottom-up heap construction is linear by summing node heights. Confirm the operation count with an instrumented heap for powers of two.

68. Implement stable counting sort for signed integer keys. Reject a key range exceeding a declared memory budget, and document the fallback policy.

69. Implement least-significant-digit radix sort for non-negative integers. Prove why every digit pass must be stable, then extend or explicitly reject negative integers.

70. Design an adaptive selection service choosing among scan, bounded heap, quickselect, and full sort for minimum, top-\(k\), median, and fully ordered outputs. State the evidence behind each branch and test identical-result contracts.

### 13.21.10 Linked structures, stacks, queues, and heaps

71. Extend <code>LinkedSequence</code> with prepend, pop-front, indexed retrieval, and insertion after a private cursor. State time bounds including cursor acquisition.

72. Implement a doubly linked list with a circular sentinel. Write a single splice primitive used by insertion and deletion, and mechanically check forward/backward consistency after random operations.

73. Define iterator mutation semantics for your linked list. Implement either fail-fast modification counters or snapshot iteration and justify the chosen cost and user contract.

74. Reverse a singly linked list iteratively in place. Give a loop invariant describing the reversed prefix, untouched suffix, and node preservation; then implement a recursive version and compare depth.

75. Merge two sorted singly linked chains by relinking existing nodes. Define ownership after the operation and prevent accidental aliasing through the original handles.

76. Prove Floyd’s cycle-entry algorithm algebraically using prefix length \(\mu\) and cycle length \(\lambda\). Generate cyclic chains covering every small pair of values and verify returned node identity.

77. Implement a queue with two lists used as stacks. Establish amortised \(O(1)\) operations and test alternating and burst workloads.

78. Solve sliding-window maximum with a monotone deque. Prove that retained indices are both position-increasing and value-decreasing, and derive linear total deque operations.

79. Implement a postfix-expression evaluator using a stack. Specify token grammar, arity, division policy, malformed-input errors, and numeric-domain behaviour.

80. Translate recursive depth-first tree evaluation into an explicit stack of enter/exit frames. Show why merely pushing children is insufficient for a post-order aggregate.

81. Complete <code>MinHeap</code> with bottom-up construction, peek, length, invariant checking, and a generic key policy. Test after every operation in random sequences.

82. Build a stable mutable priority queue with lazy deletion. Add periodic compaction when stale entries exceed a threshold and give an amortised argument for rebuild cost.

83. Implement a fixed-size top-\(k\) stream summary using a min-heap. Clarify how ties are retained, derive \(O(n\log k)\) time, and compare with sorting.

84. Merge \(k\) sorted iterables lazily with a heap. Include stable stream and within-stream tie-breaking, and derive \(O(N\log k)\) time for \(N\) yielded values.

85. Integrate Chapters 6, 8, and 11: design a generator-based external merge pipeline with context-managed temporary runs, bounded memory, exception-safe cleanup, and an explicit I/O cost model.

### 13.21.11 Trees and hashing

86. Extend the BST to store values and multiplicity counts. Define whether reinserting an order-equivalent key replaces key identity, adds a value, or increments count.

87. Implement iterative BST search, insertion, and deletion with parent tracking. Prove each is \(O(h)\), including successor search.

88. Write pre-order, in-order, post-order, and level-order iterators. Demonstrate on a tree where all four results differ and connect each order to one application.

89. Validate a purported BST without assuming only parent–child order. Carry permissible lower and upper bounds through the traversal and handle the duplicate policy.

90. Implement order statistics by augmenting every node with subtree size. Support selecting rank \(k\) and finding a key’s rank in \(O(h)\); show which updates deletion and rotation must perform.

91. Implement left and right AVL rotations with parent-free returned roots. Prove in-order preservation and test every empty/missing-child precondition.

92. Complete AVL insertion, including all straight and bent imbalance cases. Calculate height only from stored child heights and assert the balance invariant after random insertions.

93. Research and formally state red–black tree invariants. Derive the height bound from black height; do not implement deletion until the proof is complete.

94. Compare a BST, a sorted Python list with <code>bisect</code>, and a dictionary for read-heavy, update-heavy, range-query, and adversarial-key workloads. Include memory locality as a substantive, measured consideration.

95. Implement a trie for Unicode strings with insertion, exact lookup, deletion, and prefix enumeration. State whether traversal operates on code points, normalised text, or grapheme clusters.

96. Prove the Python hash/equality implication and build a deliberately broken mutable-key class. Demonstrate failed retrieval without relying on a particular bucket index.

97. Add deletion and shrinking to the chained teaching map. Use hysteresis, update <code>_size</code> correctly on replacement, and test all keys with identical hashes.

98. Analyse successful and unsuccessful chained lookup under a stated simple-uniform-hashing assumption. Separate expected chain length from worst-case adversarial behaviour.

99. Extend <code>OpenAddressSet</code> with iteration, length, and tombstone compaction. Prove that lookup stops safely only at a never-used cell.

100. Integrate Chapter 9’s object model: implement an immutable composite key with coherent equality and hashing, demonstrate dictionary insertion-order semantics, and distinguish those guarantees from CPython table layout.

### 13.21.12 Graph representation and traversal

101. Define a graph class supporting explicit isolated vertices, self-loops, parallel weighted edges, and direction. Explain why one adjacency-set representation cannot preserve every requirement.

102. Write conversions among edge list, adjacency list, and adjacency matrix. State precisely what information each conversion can lose and include vertex-label/index mappings.

103. Implement BFS distances, parents, and path reconstruction for a directed graph. Prove shortest edge count and specify deterministic tie-breaking.

104. Implement multi-source BFS returning both nearest-source identity and distance. Define tie policy where two sources are equally near and show why independent BFS runs are unnecessary.

105. Implement 0–1 BFS with a deque: push zero-weight relaxations left and one-weight relaxations right. Prove the processing order and compare with binary-heap Dijkstra.

106. Implement a faithful iterative DFS producing discovery and finish times. Test that its event nesting matches a recursive reference implementation under the same neighbour order.

107. Detect a directed cycle using white, grey, and black states and return a concrete cycle. Ensure the reconstruction closes at the correct repeated vertex.

108. Detect a cycle in an undirected multigraph. Account for the parent edge’s identity so two parallel edges form a valid length-two cycle under the chosen convention.

109. Compute connected components of an undirected graph and weak components of a directed graph. Construct an input where weak and strong component partitions all differ.

110. Implement bipartite checking that returns either a two-colouring or an odd-cycle witness. Prove both output alternatives.

111. Implement Kosaraju–Sharir SCC decomposition and compare its partition with the Tarjan implementation over generated small directed graphs.

112. Prove that contracting SCCs yields a DAG. Build the condensation graph without duplicate component edges and topologically order it.

113. Find bridges and articulation vertices in an undirected graph using discovery and low-link values. Explain how the low-link meaning differs from Tarjan SCC low links.

114. Implement Kahn topological ordering with a deque and with a heap. Compare asymptotic bounds, deterministic policies, and outputs on DAGs having many valid orders.

115. Correctly normalise graphs containing neighbour-only vertices before topological sorting. Write a regression test that would catch dictionary-size mutation during iteration.

116. Implement reverse-finish DFS topological ordering and return a cycle witness rather than partial output on cyclic input. Cross-check against Kahn’s result validity.

117. Compute earliest start and completion times in a task DAG with vertex durations. Then compute latest permissible starts and identify a critical path under a fixed project deadline.

118. Count the number of topological orders for small DAGs using subset dynamic programming. Explain why enumerating every order can require exponential output.

119. Compare adjacency-list and bit-matrix reachability on graphs of increasing density. Keep representation construction outside or inside timing according to two separately stated questions.

120. Integrate Chapter 10 packaging: create a typed graph package with immutable public graph snapshots, documented complexity contracts, property-based tests, and command-line import/export of a non-executable data format.

### 13.21.13 Weighted graphs, greedy choice, and disjoint sets

121. Extend Dijkstra to stop when a target is settled and reconstruct its path. Explain why stopping when the target is merely discovered is incorrect.

122. Construct and minimise three negative-edge counterexamples for settled-vertex Dijkstra. Trace the priority queue after every relaxation.

123. Extend Bellman–Ford to reconstruct a reachable negative cycle. Distinguish vertices whose distances are unbounded below from vertices unreachable from that cycle.

124. Implement shortest paths in a DAG with negative edges. Prove that one topological relaxation pass is sufficient and reject cyclic input.

125. Implement Floyd–Warshall with a predecessor or next-hop matrix. Reconstruct paths and detect negative cycles through diagonal entries.

126. Implement A* on a rectangular obstacle grid with Manhattan distance. Prove admissibility and consistency for four-direction unit moves; defeat the proof by adding cheaper diagonal moves.

127. Implement earliest-finish interval scheduling and exhaustive-search verification for all small interval sets. Generate counterexamples to earliest-start, shortest-duration, and least-overlap heuristics.

128. Prove fractional-knapsack density order by an exchange argument. Implement exact rational density comparison without floating division and contrast with the 0/1 counterexample.

129. Build Huffman codes from a tree, encode and decode bytes, and handle a one-symbol alphabet. Separate payload bits, padding, and codebook overhead in compression measurements.

130. Complete DSU with iterative path compression, union by size, component count, and member validation. Explain the inverse-Ackermann amortised statement without calling it a literal constant.

131. Implement Kruskal and return a minimum spanning forest rather than rejecting disconnected input. Prove acyclicity, spanning within components, and safe-edge choice.

132. Implement Prim with lazy heap entries and compare its selected edge set with Kruskal on graphs with tied weights. Explain why different MSTs can have equal total weight.

133. Prove that if every edge weight is distinct, a connected graph has a unique MST. Show by example that the converse is false.

134. Distinguish a shortest-path tree, minimum spanning tree, minimum arborescence, and Steiner tree by contract. Provide one graph on which confusing the first two gives a poor result.

135. Integrate Chapters 11 and 12: ingest a weighted graph from validated JSON, reject NaN and malformed endpoints, compute a chosen tree/path product, serialise deterministic output, and test failure atomicity.

### 13.21.14 Dynamic programming and search

136. Draw the subproblem DAG for naive Fibonacci through \(n=6\). Count recursive call occurrences, distinct states, memoised calls, and retained cache entries.

137. Implement minimum-coins reconstruction, returning an actual multiset of coins. Specify deterministic tie-breaking and prove the sentinel remains safe.

138. Distinguish minimum coins from number of coin-change combinations. Derive a recurrence for combinations and show how loop order distinguishes combinations from ordered sequences.

139. Implement LCS length with rolling rows, then reconstruct with the full table. Generate pairs with several optimal LCS results and document your tie policy.

140. Prove the LCS recurrence in both equal-final and unequal-final cases. Identify which equality assumptions the argument needs for arbitrary Python objects.

141. Extend edit distance to weighted insertion, deletion, and substitution. State conditions under which the result is a metric and produce counterexamples when symmetry or triangle assumptions fail.

142. Add operation reconstruction to edit distance. Define how indices refer to the evolving or original string and test by replaying every returned edit script.

143. Implement 0/1 knapsack with both a full table and one row. Demonstrate experimentally and logically why ascending capacity changes it to unbounded reuse.

144. Implement weighted interval scheduling: sort by finish, binary-search the last compatible predecessor, derive the recurrence, and reconstruct an optimal schedule.

145. Derive matrix-chain multiplication dynamic programming. Define state and split choice, count states/transitions, and return a parenthesisation rather than only scalar cost.

146. Implement longest increasing subsequence first in \(O(n^2)\), then in \(O(n\log n)\) using partition points. Distinguish length reconstruction from merely maintaining minimal tails.

147. Solve a grid path-count problem with blocked cells by tabulation. Then reduce memory to one row and state how movement rules determine evaluation order.

148. Formulate all-pairs shortest paths as dynamic programming over permitted intermediate vertices. Explain why the intermediate index must be the outer loop in the in-place form.

149. Memoise a recursive solver whose output depends on mutable global state and exhibit the resulting defect. Redesign its cache key or state model so equal keys imply equal subproblems.

150. Implement \(n\)-queens as a generator rather than a materialised list. Compare peak storage and explain why total generation time remains output-sensitive.

151. Use bit masks rather than sets for \(n\)-queens occupancy. State the bounded-integer word-model assumption and refine it for Python arbitrary-size integers.

152. Implement a Sudoku solver with constraint propagation and backtracking. Define the state invariant, choose a minimum-remaining-values branch heuristic, and separate correctness from empirical speed.

153. Implement branch-and-bound for 0/1 knapsack using a fractional upper bound. Prove the bound is optimistic before permitting it to prune.

154. Compare backtracking, memoisation, and tabulation on a problem where different histories converge to the same state. Measure expanded nodes and explain when history prevents merging.

155. Integrate Chapters 8 and 9: design interchangeable strategy objects for an exact solver, approximation algorithm, and heuristic; give each a typed result carrying optimality or quality evidence rather than a bare value.

### 13.21.15 Complexity, experiments, and engineering decisions

156. Convert an optimisation problem of your choice into a threshold decision problem. Show how repeated decision calls recover optimum under bounded integer objectives and identify the additional witness-reconstruction problem.

157. For three candidate reductions, determine which direction proves the intended hardness statement. Write the yes-instance equivalence explicitly and account for transformation size.

158. Explain P, NP, NP-hard, and NP-complete without using “hard to solve” as a definition. Classify SAT, a hypothetical polynomial verifier, and a non-decision optimisation problem using conditional language where necessary.

159. Contrast an undecidable problem with a decidable exponential problem. Explain why a timeout changes the output contract but does not decide the original universal question.

160. Define and verify an approximation ratio for a simple covering or scheduling algorithm. Supply both the feasibility proof and the quality-bound proof.

161. Design a benchmark comparing linear scan and hash membership across build-once/query-many workloads. Record Python version, seed, input distribution, hit ratio, key size, query count, and memory.

162. Use geometric input sizes to test predicted linear, \(n\log n\), and quadratic implementations. Plot normalised time per \(n\), \(n\log n\), or \(n^2\), and explain deviations without fitting a theorem from noise.

163. Compare <code>perf_counter</code> measurements with <code>timeit</code>. Investigate garbage-collection policy, setup placement, warm caches, and process noise.

164. Instrument comparison and movement counts separately for five sorts. Relate observed counts to stability, inversion count, and input order.

165. Measure shallow size, traced Python allocation peak, and process-level memory for one data structure. Explain why the three numbers answer different questions.

166. Construct an adversarial user-defined hash class and measure dictionary lookup scaling. Perform the experiment only on local controlled data and distinguish denial-of-service implications from ordinary workloads.

167. Compare recursive and iterative DFS on a deep path. Record semantic equivalence, recursion failure threshold, explicit-stack memory, and interpreter/version dependence.

168. Write an algorithm decision record for maintaining one million timestamped events under append, latest retrieval, range query, deletion, and persistence requirements. Evaluate at least three representations.

169. Audit a real standard-library algorithmic API using official Python 3.12 documentation. Separate specification guarantees, documented complexity guidance, CPython implementation facts, and your empirical observations.

170. Revisit one optimisation made earlier in the book. Demonstrate a case where it worsens maintainability or correctness without material performance benefit, and write a justified decision to retain or revert it.

### 13.21.16 Integrative capstones

171. Build a versioned text index. Tokenise files under a declared Unicode policy, maintain term-to-document postings, answer Boolean and phrase queries, rank bounded results, update atomically, and persist without executable deserialisation. Prove query correctness, state expected and worst-case hash costs, test corruption, package the library, and benchmark separate indexing and query phases.

172. Build a transport-routing engine supporting unweighted hops, non-negative travel time, and scheduled prerequisite constraints. Select BFS, Dijkstra, or topological relaxation from validated graph metadata; return path evidence; reject invalid weights and cycles; and explain why the selector is sound.

173. Build an external-memory sorter for records larger than available memory. Generate stable sorted runs, write them through context managers, perform a \(k\)-way heap merge, tolerate malformed records under a declared policy, and report comparisons, bytes transferred, peak memory, and wall time.

174. Build an algorithm laboratory package. Supply instrumented implementations, reproducible dataset generators, correctness oracles for small inputs, property tests, benchmark metadata, CSV results, plots, and a claim ledger that prevents observations from being reported as proofs.

175. Produce a dissertation-style comparative study of one problem admitting at least three paradigms—for example brute force, dynamic programming, and approximation. State the formal problem and encoding; prove what each method guarantees; implement typed, tested Python 3.12 packages; analyse time, space, output, and failure boundaries; conduct reproducible experiments; interpret conflicting theory and measurement; and document threats to validity.
