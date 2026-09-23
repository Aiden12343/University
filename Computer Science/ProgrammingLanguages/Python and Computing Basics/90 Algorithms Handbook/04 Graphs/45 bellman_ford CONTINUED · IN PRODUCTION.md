# bellman_ford CONTINUED · IN PRODUCTION

bellman_ford CONTINUED · IN PRODUCTION
IN PRODUCTION — the call you would actually write
THIRD-PARTY networkx pip install networkx
Handles negative edges. A reachable negative cycle raises NetworkXUnbounded instead of returning nonsense.
CODE import networkx as nx
graph = nx.DiGraph()
graph.add_weighted_edges_from([('A', 'B', 4), ('A', 'C', 5), ('B', 'C', -3)])
distances, paths = nx.single_source_bellman_ford(graph, 'A')
distances
OUTPUT {'A': 0, 'B': 4, 'C': 1}
CODE import networkx as nx
cyclic_graph = nx.DiGraph()
cyclic_graph.add_weighted_edges_from([('A', 'B', 1), ('B', 'C', -2), ('C', 'A', 0)])
try:
nx.single_source_bellman_ford(cyclic_graph, 'A')
except nx.NetworkXUnbounded:
result = 'NetworkXUnbounded: negative cycle'
result
OUTPUT 'NetworkXUnbounded: negative cycle'
CS Algorithms Toolkit Graphs
45
