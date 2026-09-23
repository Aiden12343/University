# bst_search

bst_search(root_node, target) FUNCTION
Return True if target is in the BST.
REMEMBER Same as binary search: target smaller? go left. Bigger? go right.
REQUIRES root_node MUST be a valid BST.
TIME O(h). SPACE O(1).
def bst_search(root_node, target):
current_node = root_node
while current_node is not None:
if target == current_node.value:
return True
current_node = (current_node.left_child if target < current_node.value
else current_node.right_child)
return False
INPUT root = None
for value in [8, 3, 10, 1, 6]:
root = bst_insert(root, value)
(bst_search(root, 6), bst_search(root, 7))
OUTPUT (True, False)
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY bisect on a sorted list no install needed
A binary search over a sorted list is a BST lookup without the pointers. For plain membership (no ordering needed) a set is simpler and
O(1).
CODE from bisect import bisect_left
ordered_values = [1, 3, 6, 8, 10]
position = bisect_left(ordered_values, 6)
position < len(ordered_values) and ordered_values[position] == 6
OUTPUT True
traverse_in_order(root_node) FUNCTION
Left, ROOT, right. On a BST this yields values in SORTED order.
REMEMBER "In" = root goes IN the middle.
TIME O(n). SPACE O(h).
USED FOR Sorted output from a BST, validating a BST.
def traverse_in_order(root_node):
if root_node is None:
return []
return (traverse_in_order(root_node.left_child) + [root_node.value]
+ traverse_in_order(root_node.right_child))
INPUT root = None
for value in [8, 3, 10, 1, 6, 14]: # tree: 8 -> (3 -> (1, 6), 10 -> (-, 14))
root = bst_insert(root, value)
traverse_in_order(root) # sorted, because it is a BST
OUTPUT [1, 3, 6, 8, 10, 14]
IN PRODUCTION — the call you would actually write
THIRD-PARTY iterate a SortedList pip install sortedcontainers
Iterating an ordered container IS an in-order walk, so you rarely write the recursion yourself.
CODE from sortedcontainers import SortedList
list(SortedList([8, 3, 10, 1, 6, 14]))
OUTPUT [1, 3, 6, 8, 10, 14]
CS Algorithms Toolkit Data structures the algorithms rely on
32
