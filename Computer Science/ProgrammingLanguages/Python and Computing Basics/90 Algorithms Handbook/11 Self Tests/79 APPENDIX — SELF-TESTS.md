# APPENDIX — SELF-TESTS

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
