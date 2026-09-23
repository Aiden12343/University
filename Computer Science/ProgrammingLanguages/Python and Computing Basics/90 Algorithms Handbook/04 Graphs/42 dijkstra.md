# dijkstra

dijkstra(weighted_graph, start_node) FUNCTION
Return (shortest_distance, parent_of) from start_node to reachable nodes.
REMEMBER Always expand the CLOSEST unfinished node (min-heap); for each outgoing edge ask "is distance-so-far +
edge weight better than what I knew?" — if so, update and push.
WHEN TO USE Shortest paths with NON-NEGATIVE weights from one source: maps, routing, network latency.
AVOID WHEN NEGATIVE edge weights (gives wrong answers → Bellman-Ford); unweighted graphs (BFS is simpler); all-pairs
(Floyd-Warshall).
REQUIRES All edge weights ≥ 0. Every node is a key.
TIME O((V + E) log V) with a binary heap. SPACE O(V + E).
USED FOR GPS navigation, OSPF network routing, game pathfinding.
NOTE Unreachable nodes are simply absent from the returned dictionaries.
def dijkstra(weighted_graph, start_node):
shortest_distance = {start_node: 0}
parent_of = {start_node: None}
priority_queue = MinHeap()
priority_queue.push(0, start_node)
finalised_nodes = set()
while not priority_queue.is_empty():
distance_so_far, current_node = priority_queue.pop()
if current_node in finalised_nodes:
continue # stale, outdated entry
finalised_nodes.add(current_node)
for neighbour, edge_weight in weighted_graph[current_node]:
candidate_distance = distance_so_far + edge_weight
if (neighbour not in shortest_distance
or candidate_distance < shortest_distance[neighbour]):
shortest_distance[neighbour] = candidate_distance
parent_of[neighbour] = current_node
priority_queue.push(candidate_distance, neighbour)
return shortest_distance, parent_of
INPUT weighted_graph = {'A': [('B', 4), ('C', 1)],
'B': [('D', 1)],
'C': [('B', 2), ('D', 5)],
'D': [],
'Z': []} # 'Z' cannot be reached from 'A'
dijkstra(weighted_graph, 'A') # (shortest_distance, parent_of)
OUTPUT ({'A': 0, 'B': 3, 'C': 1, 'D': 4},
{'A': None, 'B': 'C', 'C': 'A', 'D': 'B'})
CS Algorithms Toolkit Graphs
42
