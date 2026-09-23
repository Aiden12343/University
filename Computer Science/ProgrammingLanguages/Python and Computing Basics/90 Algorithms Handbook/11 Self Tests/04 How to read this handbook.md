# How to read this handbook

How to read this handbook
Tag What it tells you
REMEMBER One sentence that encodes the algorithm's steps. If you can recite it, you can re-derive the code.
WHEN TO USE Situations where this is the right tool.
AVOID WHEN Situations where it is the wrong tool (too slow, wrong answers, too much memory).
REQUIRES Preconditions: sorted data, non-negative weights, directed vs undirected… Break these and the result is silently wrong.
TIME · SPACE Big-O running time and extra memory. n = number of items, V = vertices, E = edges, m and n = string lengths, k = value
range, d = digits, L = word length.
USED FOR Real-world uses and the exam questions it usually answers.
INPUT → OUTPUT A worked example. The outputs were produced by actually running the code.
IN PRODUCTION The library call that replaces the hand-written version, tagged built-in, standard library or third-party (with its pip
install line). Also actually executed. If nothing standard exists, the entry says so.
Conventions
• Every sort returns a new sorted list; the input list is left untouched.
• No imports anywhere. Only builtins are used (len, range, enumerate, min, max, sum, sorted, pow, ord, isinstance,
reversed, float('inf') …).
• Variables have full names (shortest_distance, not d) so the code reads like the idea.
• In graph code, every node must appear as a key, even if it has no outgoing edges. For an undirected graph list each edge in both
directions.
unweighted_graph = {'A': ['B', 'C'], 'B': [], 'C': ['B']}
weighted_graph = {'A': [('B', 4), ('C', 1)], 'B': [], 'C': [('B', 2)]}
weighted_edges = [(4, 'A', 'B'), (1, 'A', 'C')] # (weight, node_a, node_b) for Kruskal
Glossary
Term Meaning
Big-O Upper bound on how cost grows with input size; constants and lower-order terms are ignored.
Stable sort Equal items keep their original relative order — matters when sorting records by several keys in turn.
In place Rearranges the data using only O(1) extra memory.
Amortised Average cost per operation over a whole sequence, even if an occasional single operation is expensive (e.g.
list.append).
Divide and conquer Split the problem, solve the parts, combine the answers: merge sort, quick sort, binary search.
Memoisation / tabulation The two flavours of dynamic programming: top-down recursion with a cache, or bottom-up filling of a table from
the smallest sub-problem.
Greedy Repeatedly take the locally best choice. Only correct when a proof (usually an exchange argument) says so.
Backtracking Build a candidate step by step; undo the last choice when it hits a dead end.
Relaxation If going via u gives a shorter route to v: distance[v] = min(distance[v], distance[u] + weight(u, v)).
Admissible / consistent A* heuristics. Admissible: never overestimates the remaining cost. Consistent: h(a) ≤ weight(a, b) + h(b).
Pseudo-polynomial Polynomial in the numeric value of an input (e.g. knapsack capacity), not in the number of bits needed to write it.
Sparse / dense graph Sparse: E is about V. Dense: E is about V². Adjacency lists suit sparse graphs.
DAG Directed acyclic graph. Only DAGs have a topological order.
Loop invariant A statement true before and after every iteration — the standard tool for proving correctness.
CS Algorithms Toolkit How to read this handbook
4
