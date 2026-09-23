# kruskal_minimum_spanning_tree

kruskal_minimum_spanning_tree(nodes, weighted_edges) FUNCTION
Return (chosen_edges, total_weight) of a minimum spanning tree/forest.
REMEMBER Sort edges cheapest first; take an edge unless its two ends are ALREADY connected (checked with
Union-Find); stop at V-1 edges.
WHEN TO USE Cheapest way to connect everything; sparse graphs; edges already in a list.
AVOID WHEN Directed graphs (needs arborescence algorithms); dense graphs (Prim with adjacency matrix is better).
REQUIRES UNDIRECTED graph given as a list of (weight, node_a, node_b). A disconnected graph yields a spanning FOREST.
TIME O(E log E) (dominated by the sort). SPACE O(V).
USED FOR Laying cable/pipes, clustering, approximating travelling salesman.
def kruskal_minimum_spanning_tree(nodes, weighted_edges):
connectivity = UnionFind(nodes)
chosen_edges = []
total_weight = 0
for edge_weight, node_a, node_b in sorted(weighted_edges):
if connectivity.union(node_a, node_b): # True = joined two groups
chosen_edges.append((node_a, node_b, edge_weight))
total_weight += edge_weight
return chosen_edges, total_weight
INPUT nodes = ['A', 'B', 'C', 'D']
weighted_edges = [(1, 'A', 'B'), (4, 'B', 'C'), (3, 'A', 'C'), (2, 'C', 'D')] # (weight, a, b)
kruskal_minimum_spanning_tree(nodes, weighted_edges) # (chosen_edges, total_weight)
OUTPUT ([('A', 'B', 1), ('C', 'D', 2), ('A', 'C', 3)], 6)
IN PRODUCTION — the call you would actually write
THIRD-PARTY networkx pip install networkx
One call builds the tree. Choose algorithm='kruskal' or 'prim'. scipy.sparse.csgraph.minimum_spanning_tree is the matrix-based version.
CODE import networkx as nx
graph = nx.Graph()
graph.add_weighted_edges_from([('A', 'B', 1), ('B', 'C', 4), ('A', 'C', 3), ('C', 'D', 2)])
tree = nx.minimum_spanning_tree(graph, algorithm='kruskal')
(sorted(tree.edges(data='weight')), tree.size(weight='weight'))
OUTPUT ([('A', 'B', 1), ('A', 'C', 3), ('C', 'D', 2)], 6.0)
CS Algorithms Toolkit Graphs
47
