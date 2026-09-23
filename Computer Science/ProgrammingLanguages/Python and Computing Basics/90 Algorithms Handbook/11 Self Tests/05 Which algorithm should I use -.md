# Which algorithm should I use?

Which algorithm should I use?
If the problem says… Reach for Why / watch out
Find a value once in unsorted data linear_search Sorting first would cost more than just looking.
Many lookups in sorted data binary_search O(log n) — the data must be sorted.
Membership tests, order irrelevant set / dict (built-in) Average O(1); no sorting needed.
First occurrence / where to insert lower_bound Binary search that never says “found”.
Smallest X such that a condition holds binary_search_on_answer The condition must be monotonic (False… then
True…).
Sort with guarantees or stability merge_sort O(n log n) always; O(n) extra space.
Sort in memory, fastest on average quick_sort Worst case O(n²); not stable.
Sort with O(1) extra memory, guaranteed heap_sort Not stable.
Tiny or nearly-sorted list insertion_sort O(n) when nearly sorted.
Integers in a small range counting_sort / radix_sort Beats O(n log n); non-negative integers only.
k-th smallest / median quickselect_kth_smallest O(n) average without sorting everything.
Fewest edges; mazes breadth_first_search Unweighted graphs only.
Cheapest path, weights ≥ 0 dijkstra Negative weights give wrong answers.
Cheapest path, negative weights bellman_ford Also detects negative cycles; O(V·E).
Shortest path between every pair floyd_warshall O(V³): small graphs only.
One start, one goal, good heuristic a_star_search Heuristic must never overestimate.
Cheapest way to connect everything kruskal_minimum_spanning_tree /
prim_minimum_spanning_tree
Kruskal: edge list. Prim: adjacency list.
Tasks with prerequisites topological_sort Returns None if there is a cycle.
Are A and B connected? Groups merging UnionFind ≈O(1) per operation; groups cannot be split.
How many clusters / islands? connected_components Undirected graphs.
Explore everything; cycle checks depth_first_search Does not find shortest paths.
Autocomplete / prefix search Trie O(L) per word; memory heavy.
Ordered data with inserts and lookups bst_insert / bst_search Degenerates to O(n) on sorted input.
Repeatedly need the current smallest MinHeap O(log n) push and pop.
Matching brackets, nesting, undo is_balanced_brackets Stack: last in, first out.
Pick items under a budget, each once knapsack_01 Greedy fails here; O(n · capacity).
Items can be split fractional_knapsack Greedy by value per weight is optimal.
Fewest coins minimum_coins_for_amount Greedy works only for “canonical” coin systems.
Similarity of two sequences longest_common_subsequence /
edit_distance
O(m·n) table.
Longest rising trend longest_increasing_subsequence_leng
th
O(n log n).
Best contiguous stretch maximum_subarray_sum Kadane: O(n) time, O(1) space.
Fixed window / many range sums maximum_sum_fixed_window /
build_prefix_sums
Slide or precompute; never re-sum.
Most non-overlapping meetings activity_selection Sort by end time.
Lossless compression huffman_codes Frequent symbols get short codes.
Every subset / ordering / puzzle generate_subsets /
generate_permutations /
solve_n_queens
Exponential: small inputs only.
Find a pattern in text kmp_search / rabin_karp_search KMP: guaranteed O(n+m). Rabin–Karp: many
patterns.
CS Algorithms Toolkit Which algorithm should I use?
5
