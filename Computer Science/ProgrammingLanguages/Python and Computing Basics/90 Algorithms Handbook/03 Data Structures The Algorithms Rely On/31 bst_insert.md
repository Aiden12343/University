# bst_insert

bst_insert(root_node, value) FUNCTION
Insert value into a binary search tree; return the (new) root.
REMEMBER Smaller goes left, bigger goes right; walk down until you hit an empty spot and hang the new node there.
WHEN TO USE Ordered data with frequent inserts + lookups + in-order walks.
AVOID WHEN Sorted/adversarial input (tree degenerates into a list, O(n)): use a balanced tree (AVL, red-black) or a hash table.
REQUIRES Values comparable; duplicates are ignored in this version.
TIME O(h): O(log n) if balanced, O(n) if degenerate. SPACE O(h) recursion stack.
USED FOR Sorted sets/maps, ordered symbol tables, range queries.
def bst_insert(root_node, value):
if root_node is None:
return TreeNode(value)
if value < root_node.value:
root_node.left_child = bst_insert(root_node.left_child, value)
elif value > root_node.value:
root_node.right_child = bst_insert(root_node.right_child, value)
return root_node
INPUT root = None # empty tree
for value in [8, 3, 10]:
root = bst_insert(root, value) # smaller -> left, bigger -> right
(root.value, root.left_child.value, root.right_child.value)
OUTPUT (8, 3, 10)
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY bisect.insort no install needed
A hand-built BST is rarely used in Python. For modest data, keep a sorted list with insort.
CODE from bisect import insort
ordered_values = []
for value in [8, 3, 10]:
insort(ordered_values, value)
ordered_values
OUTPUT [3, 8, 10]
THIRD-PARTY sortedcontainers.SortedList pip install sortedcontainers
SortedList is the production replacement for a balanced BST / ordered set: O(log n)-ish add, remove, index and range queries, pure
Python, very widely used.
CODE from sortedcontainers import SortedList
ordered_values = SortedList([8, 3, 10, 1, 6])
ordered_values.add(4)
(list(ordered_values), ordered_values.bisect_left(6), 6 in ordered_values)
OUTPUT ([1, 3, 4, 6, 8, 10], 3, True)
CS Algorithms Toolkit Data structures the algorithms rely on
31
