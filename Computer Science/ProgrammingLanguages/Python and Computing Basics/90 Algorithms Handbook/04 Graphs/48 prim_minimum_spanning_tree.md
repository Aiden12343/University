# prim_minimum_spanning_tree

prim_minimum_spanning_tree(undirected_weighted_graph, start_node) FUNCTION
Return (chosen_edges, total_weight) of an MST grown from start_node.
REMEMBER Grow one tree from a start node; always grab the CHEAPEST edge leaving the tree (min-heap) that reaches a
new node.
WHEN TO USE Dense graphs; graph already stored as an adjacency list.
AVOID WHEN Disconnected graphs (only spans start_node's component).
REQUIRES UNDIRECTED graph (edges in both directions), every node a key.
TIME O(E log V) with a binary heap. SPACE O(V + E).
USED FOR Same as Kruskal: network design, clustering.
def prim_minimum_spanning_tree(undirected_weighted_graph, start_node):
nodes_in_tree = {start_node}
chosen_edges = []
total_weight = 0
edge_queue = MinHeap()
for neighbour, edge_weight in undirected_weighted_graph[start_node]:
edge_queue.push(edge_weight, (start_node, neighbour))
while not edge_queue.is_empty():
edge_weight, (tree_node, new_node) = edge_queue.pop()
if new_node in nodes_in_tree:
continue
nodes_in_tree.add(new_node)
chosen_edges.append((tree_node, new_node, edge_weight))
total_weight += edge_weight
for neighbour, next_edge_weight in undirected_weighted_graph[new_node]:
if neighbour not in nodes_in_tree:
edge_queue.push(next_edge_weight, (new_node, neighbour))
return chosen_edges, total_weight
INPUT undirected_weighted_graph = {'A': [('B', 1), ('C', 3)],
'B': [('A', 1), ('C', 4)],
'C': [('A', 3), ('B', 4), ('D', 2)],
'D': [('C', 2)]} # every edge listed both ways
prim_minimum_spanning_tree(undirected_weighted_graph, 'A')
OUTPUT ([('A', 'B', 1), ('A', 'C', 3), ('C', 'D', 2)], 6)
IN PRODUCTION — the call you would actually write
THIRD-PARTY networkx pip install networkx
Same call as Kruskal with a different algorithm= flag: the library picks the right data structures for you.
CODE import networkx as nx
graph = nx.Graph()
graph.add_weighted_edges_from([('A', 'B', 1), ('B', 'C', 4), ('A', 'C', 3), ('C', 'D', 2)])
tree = nx.minimum_spanning_tree(graph, algorithm='prim')
(sorted(tree.edges(data='weight')), tree.size(weight='weight'))
OUTPUT ([('A', 'B', 1), ('A', 'C', 3), ('C', 'D', 2)], 6.0)
CS Algorithms Toolkit Graphs
48
