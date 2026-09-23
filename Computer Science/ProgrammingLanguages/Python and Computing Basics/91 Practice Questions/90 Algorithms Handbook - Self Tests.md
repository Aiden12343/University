# Algorithms Handbook - Self Tests

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58 6. Greedy algorithms
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 58 activity_selection
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 59 fractional_knapsack
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60 huffman_codes
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62 7. Backtracking
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62 generate_subsets
. . . . . . . . . . . . . . . . . . . . . . . . . . . 63 generate_permutations
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64 solve_n_queens
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65 8. Number theory & maths
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65 gcd_euclid
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65 lcm
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66 fast_power
. . . . . . . . . . . . . . . . . . . . . . . . . . . 67 sieve_of_eratosthenes
. . . . . . . . . . . . . . . . . . . . . . . . . . . 68 is_prime_trial_division
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 69 prime_factorisation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70 9. String matching
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 70 build_failure_table
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71 kmp_search
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72 rabin_karp_search
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73 10. Array & linked-list techniques
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73 two_sum_hash_map
. . . . . . . . . . . . . . . . . . . . . . . . . 73 two_sum_sorted_two_pointers
. . . . . . . . . . . . . . . . . . . . . . . . . . 74 is_palindrome_two_pointers
. . . . . . . . . . . . . . . . . . . . . . . . . . 75 maximum_sum_fixed_window
. . . . . . . . . . . . . . . . . . . . . . . . 75 longest_unique_substring_length
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76 build_prefix_sums
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76 range_sum
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76 ListNode
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 77 reverse_linked_list
. . . . . . . . . . . . . . . . . . . . . . . . . . . 78 linked_list_has_cycle
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79 Appendix: self-tests
CS Algorithms Toolkit
3

APPENDIX — SELF-TESTS
Run the original file (python3 cs_algorithms_toolkit.py) to execute every check below. Reading them is also a quick way to
see each function in use.
def _linked_list_from(values):
head_node = None
for value in reversed(values):
head_node = ListNode(value, head_node)
return head_node
def _linked_list_to_python_list(head_node):
values = []
while head_node is not None:
values.append(head_node.value)
head_node = head_node.next_node
return values
def test_searching():
sorted_numbers = [1, 3, 3, 3, 5, 8, 13]
assert linear_search([4, 2, 7], 7) == 2 and linear_search([4, 2, 7], 9) == -1
assert binary_search(sorted_numbers, 8) == 5 and binary_search(sorted_numbers, 4) == -1
assert lower_bound(sorted_numbers, 3) == 1 # first 3
assert lower_bound(sorted_numbers, 4) == 4 # insertion point
assert lower_bound(sorted_numbers, 99) == len(sorted_numbers)
assert binary_search_on_answer(0, 50, lambda number: number * number >= 50) == 8
def test_sorting():
sample = [5, 2, 9, 1, 5, 6, -3, 0, 2]
expected = sorted(sample)
for sorting_function in (bubble_sort, selection_sort, insertion_sort,
merge_sort, quick_sort, heap_sort):
assert sorting_function(sample) == expected, sorting_function.__name__
assert sorting_function([]) == [] and sorting_function([7]) == [7]
non_negative = [170, 45, 75, 90, 802, 24, 2, 66, 0]
assert counting_sort(non_negative) == sorted(non_negative)
assert radix_sort(non_negative) == sorted(non_negative)
assert merge_two_sorted_lists([1, 4, 9], [2, 3, 10]) == [1, 2, 3, 4, 9, 10]
assert quick_sort([3] * 50 + [1] * 50) == [1] * 50 + [3] * 50
assert quickselect_kth_smallest(sample, 0) == -3
assert quickselect_kth_smallest(sample, 4) == expected[4]
assert quickselect_kth_smallest(sample, len(sample) - 1) == 9
def test_data_structures():
heap = MinHeap()
for priority in [7, 3, 9, 1, 4, 1]:
heap.push(priority, "item%d" % priority)
assert heap.peek()[0] == 1
assert [heap.pop()[0] for _ in range(len(heap))] == [1, 1, 3, 4, 7, 9]
groups = UnionFind(["a", "b", "c", "d", "e"])
assert groups.union("a", "b") and groups.union("c", "d")
assert not groups.are_connected("a", "c")
assert groups.union("b", "c") and groups.are_connected("a", "d")
assert not groups.union("a", "d") # already together
trie = Trie()
for word in ["car", "card", "care", "cat", "dog"]:
trie.insert(word)
assert trie.contains_word("car") and not trie.contains_word("ca")
assert trie.has_prefix("ca") and not trie.has_prefix("cx")
assert trie.words_with_prefix("car") == ["car", "card", "care"]
root = None
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
root = bst_insert(root, value)
assert traverse_in_order(root) == [1, 3, 4, 6, 7, 8, 10, 13, 14]
assert traverse_pre_order(root) == [8, 3, 1, 6, 4, 7, 10, 14, 13]
assert traverse_post_order(root) == [1, 4, 7, 6, 3, 13, 14, 10, 8]
assert traverse_level_order(root) == [8, 3, 10, 1, 6, 14, 4, 7, 13]
assert tree_height(root) == 4 and tree_height(None) == 0
assert bst_search(root, 7) and not bst_search(root, 5)
assert is_balanced_brackets("{[()]}") and not is_balanced_brackets("([)]")
assert not is_balanced_brackets("((") and not is_balanced_brackets(")")
def test_graphs():
CS Algorithms Toolkit Appendix: self-tests
79

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

assert gcd_euclid(48, 18) == 6 and lcm(4, 6) == 12
assert fast_power(2, 10) == 1024 and fast_power(3, 200, 13) == pow(3, 200, 13)
assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert is_prime_trial_division(97) and not is_prime_trial_division(91)
assert prime_factorisation(360) == [2, 2, 2, 3, 3, 5]
assert build_failure_table("ababaca") == [0, 0, 1, 2, 3, 0, 1]
for search_function in (kmp_search, rabin_karp_search):
assert search_function("abababca", "aba") == [0, 2]
assert search_function("aaaa", "aa") == [0, 1, 2]
assert search_function("hello", "xyz") == []
def test_array_techniques():
assert two_sum_hash_map([2, 7, 11, 15], 9) == (0, 1)
assert two_sum_sorted_two_pointers([2, 7, 11, 15], 26) == (2, 3)
assert two_sum_hash_map([1, 2], 10) is None
assert is_palindrome_two_pointers("A man, a plan, a canal: Panama")
assert not is_palindrome_two_pointers("hello")
assert maximum_sum_fixed_window([2, 1, 5, 1, 3, 2], 3) == 9
assert longest_unique_substring_length("abcabcbb") == 3
prefix = build_prefix_sums([3, 1, 4, 1, 5, 9])
assert range_sum(prefix, 1, 4) == 6
head = _linked_list_from([1, 2, 3, 4])
assert _linked_list_to_python_list(reverse_linked_list(head)) == [4, 3, 2, 1]
looping_head = _linked_list_from([1, 2, 3])
looping_head.next_node.next_node.next_node = looping_head # 3 -> 1
assert linked_list_has_cycle(looping_head)
assert not linked_list_has_cycle(_linked_list_from([1, 2, 3]))
def run_self_tests():
for test_function in (test_searching, test_sorting, test_data_structures,
test_graphs, test_dynamic_programming,
test_greedy_and_backtracking, test_maths_and_strings,
test_array_techniques):
test_function()
print("passed:", test_function.__name__)
print("All self-tests passed.")
if __name__ == "__main__":
run_self_tests()
CS Algorithms Toolkit Appendix: self-tests
81
