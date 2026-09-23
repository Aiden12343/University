# traverse_level_order

traverse_level_order(root_node) FUNCTION
Visit the tree row by row (breadth-first).
REMEMBER BFS on a tree: queue the root; pop a node, record it, queue its children.
TIME O(n). SPACE O(width of tree).
USED FOR Printing by depth, shortest depth to a node.
def traverse_level_order(root_node):
if root_node is None:
return []
visit_order = []
queue = [root_node]
queue_head = 0 # list + head index = cheap queue
while queue_head < len(queue):
current_node = queue[queue_head]
queue_head += 1
visit_order.append(current_node.value)
if current_node.left_child is not None:
queue.append(current_node.left_child)
if current_node.right_child is not None:
queue.append(current_node.right_child)
return visit_order
INPUT root = None
for value in [8, 3, 10, 1, 6, 14]: # tree: 8 -> (3 -> (1, 6), 10 -> (-, 14))
root = bst_insert(root, value)
traverse_level_order(root)
OUTPUT [8, 3, 10, 1, 6, 14]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY collections.deque as the queue no install needed
A deque pops from the left in O(1). The list-plus-index queue in the handbook works, but list.pop(0) would be O(n), so production code
uses deque.
CODE from collections import deque
root = None
for value in [8, 3, 10, 1, 6, 14]:
root = bst_insert(root, value) # builds the tree from the example above
queue, visit_order = deque([root]), []
while queue:
node = queue.popleft()
visit_order.append(node.value)
queue.extend(child for child in (node.left_child, node.right_child) if child)
visit_order
OUTPUT [8, 3, 10, 1, 6, 14]
CS Algorithms Toolkit Data structures the algorithms rely on
34
