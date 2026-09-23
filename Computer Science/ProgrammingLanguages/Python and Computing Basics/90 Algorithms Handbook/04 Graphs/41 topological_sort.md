# topological_sort

topological_sort(directed_graph) FUNCTION
Return nodes ordered so every edge goes forward, or None if cyclic.
REMEMBER (Kahn) Count each node's incoming edges; repeatedly take a node with ZERO incoming edges, output it, and
"delete" its outgoing edges. If you can't output everything, there's a cycle.
WHEN TO USE Tasks with dependencies: build order, course prerequisites.
AVOID WHEN Undirected or cyclic graphs (no valid order exists).
REQUIRES DIRECTED graph, every node is a key (including sinks).
TIME O(V + E). SPACE O(V).
USED FOR Build systems (make), package installers, spreadsheet recalculation, scheduling, cycle detection in directed graphs.
def topological_sort(directed_graph):
incoming_edge_count = {node: 0 for node in directed_graph}
for node in directed_graph:
for neighbour in directed_graph[node]:
incoming_edge_count[neighbour] += 1
ready_nodes = [node for node in directed_graph if incoming_edge_count[node] == 0]
ordering = []
while ready_nodes:
current_node = ready_nodes.pop()
ordering.append(current_node)
for neighbour in directed_graph[current_node]:
incoming_edge_count[neighbour] -= 1
if incoming_edge_count[neighbour] == 0:
ready_nodes.append(neighbour)
if len(ordering) != len(directed_graph):
return None # leftover nodes are stuck in a cycle
return ordering
INPUT dependencies = {'shirt': ['tie'], 'tie': ['jacket'],
'trousers': ['jacket'], 'jacket': []} # 'x': ['y'] means x before y
topological_sort(dependencies)
OUTPUT ['trousers', 'shirt', 'tie', 'jacket']
INPUT topological_sort({'A': ['B'], 'B': ['A']}) # cycle -> no valid order
OUTPUT None
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY graphlib.TopologicalSorter (Python 3.9+) no install needed
graphlib is the standard library's one graph tool. It wants a map of node → things that must come BEFORE it, and raises CycleError on a
cycle. It can also hand out ready-to-run tasks for parallel scheduling.
CODE from graphlib import TopologicalSorter
dependencies = {'shirt': ['tie'], 'tie': ['jacket'], 'trousers': ['jacket'], 'jacket': []}
predecessors = {node: [] for node in dependencies}
for node, followers in dependencies.items():
for follower in followers:
predecessors[follower].append(node) # graphlib wants "who must come BEFORE me"
list(TopologicalSorter(predecessors).static_order())
OUTPUT ['shirt', 'trousers', 'tie', 'jacket']
CODE from graphlib import TopologicalSorter, CycleError
try:
list(TopologicalSorter({'A': ['B'], 'B': ['A']}).static_order())
except CycleError:
result = 'CycleError: no valid order'
result
OUTPUT 'CycleError: no valid order'
CS Algorithms Toolkit Graphs
41
