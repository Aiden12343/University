# Graph algorithms

Graph algorithms
Algorithm Time Extra space Negative weights? Best for
BFS O(V + E) O(V) n/a (unweighted) Fewest edges, levels
DFS O(V + E) O(V) n/a Exploration, cycles, ordering
Topological sort (Kahn) O(V + E) O(V) n/a DAG ordering; None if cyclic
Connected components O(V + E) O(V) n/a Undirected clusters
Dijkstra (binary heap) O((V + E) log V) O(V + E) No Single-source, weights ≥ 0
Bellman-Ford O(V · E) O(V) Yes; detects neg. cycles Single-source, negative edges
Floyd-Warshall O(V³) O(V²) Yes (no neg. cycles) All pairs, small graphs
A* ≤ Dijkstra with good h O(V) No One goal + heuristic
Kruskal (MST) O(E log E) O(V) Fine Edge list, sparse graphs
Prim (MST, heap) O(E log V) O(V + E) Fine Adjacency list, dense graphs
Dynamic programming, greedy, backtracking, maths, strings and arrays
Algorithm Time Extra space
Fibonacci (memoised / bottom-up) O(n) O(n) / O(1)
0/1 knapsack O(n · capacity) O(capacity)
Longest common subsequence O(m · n) O(m · n)
Edit distance (two rows) O(m · n) O(n)
Longest increasing subsequence O(n log n) O(n)
Minimum coins O(amount · coins) O(amount)
Kadane (max subarray) O(n) O(1)
Activity selection / fractional knapsack O(n log n) O(n)
Huffman coding O(k log k) O(k)
All subsets / all permutations O(n · 2
n
) / O(n · n!) O(n)
N-Queens (all solutions) Exponential (pruned) O(n)
GCD (Euclid) / fast power O(log min(a, b)) / O(log e) O(1)
Sieve of Eratosthenes O(n log log n) O(n)
Trial-division primality / factorisation O(√n) O(1) / O(log n)
KMP search O(n + m) O(m)
Rabin-Karp search O(n + m) average, O(n · m) worst O(1)
Two-sum: hash map / two pointers O(n) / O(n) O(n) / O(1)
Sliding window, longest unique substring O(n) O(1) / O(alphabet)
Prefix sums O(n) build, O(1) query O(n)
Reverse linked list / Floyd cycle check O(n) O(1)
CS Algorithms Toolkit Complexity cheat sheets
10
