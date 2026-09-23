# traverse_pre_order

traverse_pre_order(root_node) FUNCTION
ROOT, left, right.
REMEMBER "Pre" = root comes BEFORE its children.
TIME O(n).
USED FOR Copying/serialising a tree, prefix expressions.
def traverse_pre_order(root_node):
if root_node is None:
return []
return ([root_node.value] + traverse_pre_order(root_node.left_child)
+ traverse_pre_order(root_node.right_child))
INPUT root = None
for value in [8, 3, 10, 1, 6, 14]: # tree: 8 -> (3 -> (1, 6), 10 -> (-, 14))
root = bst_insert(root, value)
traverse_pre_order(root)
OUTPUT [8, 3, 1, 6, 10, 14]
IN PRODUCTION No standard routine. Production code uses a generator with yield from, or an explicit stack for very deep trees.
traverse_post_order(root_node) FUNCTION
Left, right, ROOT.
REMEMBER "Post" = root comes AFTER its children.
TIME O(n).
USED FOR Deleting a tree (children first), evaluating expression trees, computing folder sizes.
def traverse_post_order(root_node):
if root_node is None:
return []
return (traverse_post_order(root_node.left_child)
+ traverse_post_order(root_node.right_child) + [root_node.value])
INPUT root = None
for value in [8, 3, 10, 1, 6, 14]: # tree: 8 -> (3 -> (1, 6), 10 -> (-, 14))
root = bst_insert(root, value)
traverse_post_order(root)
OUTPUT [1, 6, 3, 14, 10, 8]
IN PRODUCTION No standard routine. Production code uses a generator with yield from, or an explicit stack for very deep trees.
CS Algorithms Toolkit Data structures the algorithms rely on
33
