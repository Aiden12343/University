# depth_first_search_iterative

depth_first_search_iterative(unweighted_graph, start_node) FUNCTION
Same order as depth_first_search but with an explicit stack.
REMEMBER Replace recursion with a list used as a stack; push neighbours in REVERSE so the first neighbour is popped
first.
WHEN TO USE Deep graphs where recursion would overflow.
TIME O(V + E). SPACE O(V).
def depth_first_search_iterative(unweighted_graph, start_node):
visit_order = []
already_visited = set()
stack = [start_node]
while stack:
current_node = stack.pop()
if current_node in already_visited:
continue
already_visited.add(current_node)
visit_order.append(current_node)
for neighbour in reversed(unweighted_graph[current_node]):
if neighbour not in already_visited:
stack.append(neighbour)
return visit_order
INPUT unweighted_graph = {'A': ['B', 'C'],
'B': ['D'],
'C': ['D'],
'D': []}
depth_first_search_iterative(unweighted_graph, 'A') # same order as recursive
OUTPUT ['A', 'B', 'D', 'C']
IN PRODUCTION Same as the production variant of depth_first_search.
CS Algorithms Toolkit Graphs
39
