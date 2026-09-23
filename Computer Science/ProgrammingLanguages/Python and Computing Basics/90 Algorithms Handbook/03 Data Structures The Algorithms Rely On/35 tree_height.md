# tree_height

tree_height(root_node) FUNCTION
Number of nodes on the longest root-to-leaf path (empty tree = 0).
REMEMBER Height = 1 + the taller of the two child heights.
TIME O(n). SPACE O(h).
def tree_height(root_node):
if root_node is None:
return 0
return 1 + max(tree_height(root_node.left_child),
tree_height(root_node.right_child))
INPUT root = None
for value in [8, 3, 10, 1, 6, 14]: # tree: 8 -> (3 -> (1, 6), 10 -> (-, 14))
root = bst_insert(root, value)
tree_height(root) # nodes on the longest root-to-leaf path
OUTPUT 3
IN PRODUCTION No standard routine: a short recursive function like this is the production form.
is_balanced_brackets(text) FUNCTION
Return True if every ( [ { is closed correctly and in the right order.
REMEMBER Stack: push every opener; on a closer, the top of the stack must be its matching opener; at the end the stack
is empty.
WHEN TO USE Nested / last-in-first-out structure (parsing, undo, DFS).
REQUIRES Nothing.
TIME O(n). SPACE O(n).
USED FOR Compilers, expression validation, HTML tag matching.
def is_balanced_brackets(text):
opener_for_closer = {")": "(", "]": "[", "}": "{"}
opener_stack = []
for character in text:
if character in opener_for_closer.values():
opener_stack.append(character)
elif character in opener_for_closer:
if not opener_stack or opener_stack.pop() != opener_for_closer[character]:
return False
return len(opener_stack) == 0
INPUT (is_balanced_brackets('{[()]}'), is_balanced_brackets('([)]')) # (valid, wrong order)
OUTPUT (True, False)
IN PRODUCTION No standard routine. A list used as a stack is the production form; real parsers use the ast or tokenize modules.
CS Algorithms Toolkit Data structures the algorithms rely on
35
