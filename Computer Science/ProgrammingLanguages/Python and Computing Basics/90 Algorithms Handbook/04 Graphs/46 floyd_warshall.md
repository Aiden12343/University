# floyd_warshall

floyd_warshall(weighted_graph) FUNCTION
Return distance_between[source][target] for EVERY pair of nodes.
REMEMBER For each possible middle stop (outermost loop!), ask for every pair "is source → via → target shorter than
source → target?"
WHEN TO USE All-pairs shortest paths on small/dense graphs; transitive closure; negative weights allowed.
AVOID WHEN Big graphs (O(V3
)); single-source needs (Dijkstra is cheaper).
REQUIRES Directed or undirected (both directions listed), every node a key. A negative cycle exists if distance_between[x][x] < 0.
TIME O(V3
). SPACE O(V2
).
USED FOR Routing tables, graph diameter, reachability tables.
def floyd_warshall(weighted_graph):
infinity = float("inf")
nodes = list(weighted_graph)
distance_between = {source: {target: infinity for target in nodes} for source in nodes}
for node in nodes:
distance_between[node][node] = 0
for source_node, outgoing_edges in weighted_graph.items():
for target_node, edge_weight in outgoing_edges:
if edge_weight < distance_between[source_node][target_node]:
distance_between[source_node][target_node] = edge_weight
for via_node in nodes: # via MUST be outermost
for source_node in nodes:
for target_node in nodes:
distance_through_via = (distance_between[source_node][via_node]
+ distance_between[via_node][target_node])
if distance_through_via < distance_between[source_node][target_node]:
distance_between[source_node][target_node] = distance_through_via
return distance_between
INPUT weighted_graph = {'A': [('B', 3), ('C', 8)],
'B': [('C', 2)],
'C': []}
floyd_warshall(weighted_graph) # distance_between[source][target]
OUTPUT {'A': {'A': 0, 'B': 3, 'C': 5},
'B': {'A': inf, 'B': 0, 'C': 2},
'C': {'A': inf, 'B': inf, 'C': 0}}
IN PRODUCTION — the call you would actually write
THIRD-PARTY networkx pip install networkx
Returns a dict of dicts of distances (inf when unreachable). scipy.sparse.csgraph.floyd_warshall gives the same as a NumPy matrix.
CODE import networkx as nx
graph = nx.DiGraph()
graph.add_weighted_edges_from([('A', 'B', 3), ('A', 'C', 8), ('B', 'C', 2)])
all_pairs = nx.floyd_warshall(graph)
(all_pairs['A']['C'], all_pairs['C']['A']) # A to C via B; C to A is unreachable
OUTPUT (5, inf)
CS Algorithms Toolkit Graphs
46
