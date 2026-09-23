# dijkstra CONTINUED · IN PRODUCTION

dijkstra CONTINUED · IN PRODUCTION
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY Dijkstra with heapq no install needed
The same algorithm using the library heap instead of the hand-written MinHeap: the lazy-deletion pattern (skip stale entries when
popped) is the standard production form.
CODE import heapq
weighted_graph = {'A': [('B', 4), ('C', 1)], 'B': [('D', 1)],
'C': [('B', 2), ('D', 5)], 'D': [], 'Z': []}
shortest_distance, frontier = {'A': 0}, [(0, 'A')]
while frontier:
distance_so_far, current_node = heapq.heappop(frontier)
if distance_so_far > shortest_distance[current_node]:
continue # stale entry: a shorter route exists
for neighbour, edge_weight in weighted_graph[current_node]:
candidate_distance = distance_so_far + edge_weight
if candidate_distance < shortest_distance.get(neighbour, float('inf')):
shortest_distance[neighbour] = candidate_distance
heapq.heappush(frontier, (candidate_distance, neighbour))
shortest_distance
OUTPUT {'A': 0, 'B': 3, 'C': 1, 'D': 4}
THIRD-PARTY networkx pip install networkx
One call returns distances and the actual paths. For very large graphs, scipy.sparse.csgraph.dijkstra is the compiled, matrix-based option.
CODE import networkx as nx
graph = nx.DiGraph()
graph.add_weighted_edges_from([('A', 'B', 4), ('A', 'C', 1), ('B', 'D', 1),
('C', 'B', 2), ('C', 'D', 5)])
graph.add_node('Z')
nx.single_source_dijkstra(graph, 'A') # (distances, paths)
OUTPUT ({'A': 0, 'C': 1, 'B': 3, 'D': 4},
{'A': ['A'],
'C': ['A', 'C'],
'B': ['A', 'C', 'B'],
'D': ['A', 'C', 'B', 'D']})
CS Algorithms Toolkit Graphs
43
