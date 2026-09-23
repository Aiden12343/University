# connected_components

connected_components(undirected_graph) FUNCTION
Return a list of groups of mutually reachable nodes.
REMEMBER For every node not yet seen, flood-fill (DFS) everything reachable from it: that flood is one component.
WHEN TO USE "How many separate clusters / islands are there?"
REQUIRES UNDIRECTED graph (edges listed both ways), all nodes as keys. For directed graphs you need strongly connected
components (Tarjan/Kosaraju) instead.
TIME O(V + E). SPACE O(V).
USED FOR Network clusters, counting islands in a grid, image labelling.
def connected_components(undirected_graph):
already_visited = set()
all_components = []
for start_node in undirected_graph:
if start_node in already_visited:
continue
component_nodes = []
stack = [start_node]
already_visited.add(start_node)
while stack:
current_node = stack.pop()
component_nodes.append(current_node)
for neighbour in undirected_graph[current_node]:
if neighbour not in already_visited:
already_visited.add(neighbour)
stack.append(neighbour)
all_components.append(component_nodes)
return all_components
INPUT undirected_graph = {'A': ['B'], 'B': ['A'], # island 1
'C': [], # island 2
'D': ['E'], 'E': ['D']} # island 3
connected_components(undirected_graph)
OUTPUT [['A', 'B'], ['C'], ['D', 'E']]
IN PRODUCTION — the call you would actually write
THIRD-PARTY networkx pip install networkx
One call returns the components. For huge graphs stored as sparse matrices, scipy.sparse.csgraph offers the same idea in compiled code.
CODE import networkx as nx
graph = nx.Graph([('A', 'B'), ('D', 'E')])
graph.add_node('C') # an isolated node is its own component
sorted(sorted(component) for component in nx.connected_components(graph))
OUTPUT [['A', 'B'], ['C'], ['D', 'E']]
CS Algorithms Toolkit Graphs
40
