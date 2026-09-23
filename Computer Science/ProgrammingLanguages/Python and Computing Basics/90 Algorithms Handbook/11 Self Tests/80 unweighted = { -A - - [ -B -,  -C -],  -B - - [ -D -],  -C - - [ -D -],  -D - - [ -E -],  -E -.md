# unweighted = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E"

unweighted = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E": []}
hops, parents = breadth_first_search(unweighted, "A")
assert hops == {"A": 0, "B": 1, "C": 1, "D": 2, "E": 3}
assert reconstruct_path(parents, "E") == ["A", "B", "D", "E"]
assert depth_first_search(unweighted, "A") == ["A", "B", "D", "E", "C"]
assert depth_first_search_iterative(unweighted, "A") == depth_first_search(unweighted, "A")
islands = {"A": ["B"], "B": ["A"], "C": [], "D": ["E"], "E": ["D"]}
assert len(connected_components(islands)) == 3
dressing = {"shirt": ["tie", "belt"], "tie": ["jacket"], "belt": ["jacket"],
"trousers": ["belt"], "jacket": []}
order = topological_sort(dressing)
for node, followers in dressing.items():
for follower in followers:
assert order.index(node) < order.index(follower)
assert topological_sort({"A": ["B"], "B": ["A"]}) is None
weighted = {"A": [("B", 4), ("C", 1)], "B": [("D", 1)], "C": [("B", 2), ("D", 5)],
"D": [("E", 3)], "E": []}
distances, parents = dijkstra(weighted, "A")
assert distances == {"A": 0, "C": 1, "B": 3, "D": 4, "E": 7}
assert reconstruct_path(parents, "E") == ["A", "C", "B", "D", "E"]
all_pairs = floyd_warshall(weighted)
assert all_pairs["A"]["E"] == 7 and all_pairs["E"]["A"] == float("inf")
bellman_distances, _ = bellman_ford(weighted, "A")
assert bellman_distances["E"] == 7
negative_edge_graph = {"A": [("B", 4), ("C", 5)], "B": [("C", -3)], "C": [("D", 2)], "D": []}
negative_distances, _ = bellman_ford(negative_edge_graph, "A")
assert negative_distances == {"A": 0, "B": 4, "C": 1, "D": 3}
negative_cycle_graph = {"A": [("B", 1)], "B": [("C", -2)], "C": [("A", 0)]}
assert bellman_ford(negative_cycle_graph, "A") == (None, None)
heuristic_table = {"E": 0, "D": 3, "B": 4, "C": 4, "A": 5} # consistent
cost, path = a_star_search(weighted, "A", "E", lambda node: heuristic_table[node])
assert cost == 7 and path == ["A", "C", "B", "D", "E"]
assert a_star_search(weighted, "A", "E", lambda node: 0)[0] == 7
edge_list = [(1, "A", "B"), (4, "B", "C"), (3, "A", "C"), (2, "C", "D"), (7, "B", "D")]
_, kruskal_total = kruskal_minimum_spanning_tree(["A", "B", "C", "D"], edge_list)
undirected = {"A": [], "B": [], "C": [], "D": []}
for edge_weight, node_a, node_b in edge_list:
undirected[node_a].append((node_b, edge_weight))
undirected[node_b].append((node_a, edge_weight))
_, prim_total = prim_minimum_spanning_tree(undirected, "A")
assert kruskal_total == prim_total == 6
def test_dynamic_programming():
assert fibonacci_memoised(10) == 55 and fibonacci_memoised(50) == 12586269025
assert fibonacci_bottom_up(10) == 55 and fibonacci_bottom_up(50) == 12586269025
assert knapsack_01([10, 20, 30], [60, 100, 120], 50) == 220
common = longest_common_subsequence("ABCBDAB", "BDCABA")
assert len(common) == 4
def is_subsequence(small, big):
big_iterator = iter(big)
return all(character in big_iterator for character in small)
assert is_subsequence(common, "ABCBDAB") and is_subsequence(common, "BDCABA")
assert edit_distance("kitten", "sitting") == 3 and edit_distance("", "abc") == 3
assert longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert minimum_coins_for_amount([1, 3, 4], 6) == 2
assert minimum_coins_for_amount([2], 3) == -1
assert maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert maximum_subarray_sum([-5, -2, -9]) == -2
def test_greedy_and_backtracking():
meetings = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
assert len(activity_selection(meetings)) == 3
assert fractional_knapsack([(10, 60), (20, 100), (30, 120)], 50) == 240.0
frequencies = {"a": 45, "b": 13, "c": 12, "d": 16, "e": 9, "f": 5}
codes = huffman_codes(frequencies)
assert sum(frequencies[symbol] * len(codes[symbol]) for symbol in frequencies) == 224
all_codes = list(codes.values())
for first_code in all_codes: # prefix-free check
for second_code in all_codes:
assert first_code == second_code or not second_code.startswith(first_code)
assert len(generate_subsets([1, 2, 3])) == 8
assert len(generate_permutations([1, 2, 3])) == 6
assert len(solve_n_queens(6)) == 4 and len(solve_n_queens(8)) == 92
def test_maths_and_strings():
CS Algorithms Toolkit Appendix: self-tests
80
