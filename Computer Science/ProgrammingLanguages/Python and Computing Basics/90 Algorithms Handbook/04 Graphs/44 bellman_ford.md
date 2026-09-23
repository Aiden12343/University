# bellman_ford

bellman_ford(weighted_graph, start_node) FUNCTION
Return (shortest_distance, parent_of), or (None, None) on negative cycle.
REMEMBER "Relax" every edge V-1 times (a shortest path has at most V-1 edges). If ONE MORE pass still improves
something, a negative cycle exists.
WHEN TO USE Graphs with NEGATIVE edge weights; detecting negative cycles (e.g. currency-arbitrage loops).
AVOID WHEN Non-negative weights (Dijkstra is much faster).
REQUIRES Directed graph, every node is a key. Undirected negative edges would themselves form negative cycles.
TIME O(V × E). SPACE O(V).
USED FOR Arbitrage detection, distance-vector routing (RIP).
NOTE Unreachable nodes have distance float("inf").
def bellman_ford(weighted_graph, start_node):
infinity = float("inf")
shortest_distance = {node: infinity for node in weighted_graph}
shortest_distance[start_node] = 0
parent_of = {start_node: None}
for relaxation_round in range(len(weighted_graph) - 1):
any_distance_improved = False
for node in weighted_graph:
if shortest_distance[node] == infinity:
continue
for neighbour, edge_weight in weighted_graph[node]:
candidate_distance = shortest_distance[node] + edge_weight
if candidate_distance < shortest_distance[neighbour]:
shortest_distance[neighbour] = candidate_distance
parent_of[neighbour] = node
any_distance_improved = True
if not any_distance_improved:
break
for node in weighted_graph: # the "one more pass" test
if shortest_distance[node] == infinity:
continue
for neighbour, edge_weight in weighted_graph[node]:
if shortest_distance[node] + edge_weight < shortest_distance[neighbour]:
return None, None
return shortest_distance, parent_of
INPUT graph_with_negative_edge = {'A': [('B', 4), ('C', 5)],
'B': [('C', -3)], # negative weight is fine here
'C': []}
bellman_ford(graph_with_negative_edge, 'A')
OUTPUT ({'A': 0, 'B': 4, 'C': 1}, {'A': None, 'B': 'A', 'C': 'B'})
INPUT graph_with_negative_cycle = {'A': [('B', 1)], 'B': [('C', -2)], 'C': [('A', 0)]}
bellman_ford(graph_with_negative_cycle, 'A') # loop A->B->C->A totals -1
OUTPUT (None, None)
CS Algorithms Toolkit Graphs
44
