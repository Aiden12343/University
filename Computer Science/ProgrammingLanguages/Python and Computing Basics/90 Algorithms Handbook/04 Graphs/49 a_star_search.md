# a_star_search

a_star_search(weighted_graph, start_node, goal_node, estimate_remaining_cost) FUNCTION
Return (total_cost, path) from start to goal, or (None, None).
REMEMBER Dijkstra, but the heap priority is (cost so far) + (a GUESS of the cost still to go), so it heads toward the goal.
WHEN TO USE Single start→goal search where you have a good heuristic: grid maps, puzzles (8-puzzle), game AI.
AVOID WHEN No sensible heuristic (it degrades to Dijkstra); a heuristic that overestimates (path no longer optimal).
REQUIRES Weights ≥ 0. estimate_remaining_cost(node) must be ADMISSIBLE (never overestimates) and CONSISTENT (h(a) ≤
edge(a,b) + h(b)); this version never re-expands nodes.
TIME Worst case like Dijkstra; far fewer nodes with a good
heuristic.
SPACE O(V).
USED FOR Video-game pathfinding (Manhattan/Euclidean heuristics).
def a_star_search(weighted_graph, start_node, goal_node, estimate_remaining_cost):
cost_from_start = {start_node: 0}
parent_of = {start_node: None}
open_queue = MinHeap()
open_queue.push(estimate_remaining_cost(start_node), start_node)
finalised_nodes = set()
while not open_queue.is_empty():
_estimated_total_cost, current_node = open_queue.pop()
if current_node == goal_node:
return cost_from_start[goal_node], reconstruct_path(parent_of, goal_node)
if current_node in finalised_nodes:
continue
finalised_nodes.add(current_node)
for neighbour, edge_weight in weighted_graph[current_node]:
new_cost = cost_from_start[current_node] + edge_weight
if neighbour not in cost_from_start or new_cost < cost_from_start[neighbour]:
cost_from_start[neighbour] = new_cost
parent_of[neighbour] = current_node
open_queue.push(new_cost + estimate_remaining_cost(neighbour), neighbour)
return None, None
INPUT weighted_graph = {'A': [('B', 4), ('C', 1)],
'B': [('D', 1)],
'C': [('B', 2), ('D', 5)],
'D': []}
guess_to_goal = {'A': 3, 'B': 1, 'C': 3, 'D': 0} # optimistic guesses of remaining cost
a_star_search(weighted_graph, 'A', 'D', lambda node: guess_to_goal[node]) # (cost, path)
OUTPUT (4, ['A', 'C', 'B', 'D'])
IN PRODUCTION — the call you would actually write
THIRD-PARTY networkx pip install networkx
Pass the heuristic as a function of (node, goal). astar_path_length gives the cost.
CODE import networkx as nx
graph = nx.DiGraph()
graph.add_weighted_edges_from([('A', 'B', 4), ('A', 'C', 1), ('B', 'D', 1),
('C', 'B', 2), ('C', 'D', 5)])
guess_to_goal = {'A': 3, 'B': 1, 'C': 3, 'D': 0}
heuristic = lambda node, goal: guess_to_goal[node]
path = nx.astar_path(graph, 'A', 'D', heuristic)
(path, nx.astar_path_length(graph, 'A', 'D', heuristic))
OUTPUT (['A', 'C', 'B', 'D'], 4)
CS Algorithms Toolkit Graphs
49
