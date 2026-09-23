# assert gcd_euclid(48, 18) == 6 and lcm(4, 6) == 12

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
