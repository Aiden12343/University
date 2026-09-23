# depth_first_search

depth_first_search(unweighted_graph, start_node) FUNCTION
Return nodes in the order DFS first visits them (recursive version).
REMEMBER Go as deep as you can down one path; on a dead end, back up and try the next branch. (Recursion = the
stack.)
WHEN TO USE Exhaustive exploration, cycle detection, topological ordering, connected components, maze solving, backtracking.
AVOID WHEN Shortest paths (DFS does NOT find them); very deep graphs with the recursive version (Python recursion limit ~1000).
REQUIRES Every node is a key in unweighted_graph.
TIME O(V + E). SPACE O(V) (recursion depth up to V).
USED FOR Solving mazes, finding cycles, dependency resolution.
def depth_first_search(unweighted_graph, start_node):
visit_order = []
already_visited = set()
def visit(current_node):
already_visited.add(current_node)
visit_order.append(current_node)
for neighbour in unweighted_graph[current_node]:
if neighbour not in already_visited:
visit(neighbour)
visit(start_node)
return visit_order
INPUT unweighted_graph = {'A': ['B', 'C'],
'B': ['D'],
'C': ['D'],
'D': []}
depth_first_search(unweighted_graph, 'A')
OUTPUT ['A', 'B', 'D', 'C']
IN PRODUCTION — the call you would actually write
THIRD-PARTY networkx pip install networkx
NetworkX's DFS is iterative, so it does not hit Python's recursion limit on deep graphs. The standard library has no graph module apart
from graphlib (topological sorting).
CODE import networkx as nx
graph = nx.DiGraph({'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []})
list(nx.dfs_preorder_nodes(graph, 'A'))
OUTPUT ['A', 'B', 'D', 'C']
CS Algorithms Toolkit Graphs
38
