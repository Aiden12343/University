# breadth_first_search

4 GRAPHS
breadth_first_search(unweighted_graph, start_node) FUNCTION
Return (hops_from_start, parent_of) for every node reachable.
REMEMBER Ripples in a pond: queue the start; pop a node, queue its unseen neighbours — nearest nodes are always
processed first.
WHEN TO USE Shortest path in an UNWEIGHTED graph (fewest edges); level-by- level exploration; nearest-neighbour problems;
mazes.
AVOID WHEN Weighted edges (use Dijkstra); memory-tight on very wide graphs.
REQUIRES Every node is a key in unweighted_graph. Edges unweighted (or all equal).
TIME O(V + E). SPACE O(V).
USED FOR Social-network "degrees of separation", maze solving, web crawling, flood fill, minimum moves puzzles.
def breadth_first_search(unweighted_graph, start_node):
hops_from_start = {start_node: 0}
parent_of = {start_node: None}
queue = [start_node]
queue_head = 0
while queue_head < len(queue):
current_node = queue[queue_head]
queue_head += 1
for neighbour in unweighted_graph[current_node]:
if neighbour not in hops_from_start:
hops_from_start[neighbour] = hops_from_start[current_node] + 1
parent_of[neighbour] = current_node
queue.append(neighbour)
return hops_from_start, parent_of
INPUT unweighted_graph = {'A': ['B', 'C'],
'B': ['D'],
'C': ['D'],
'D': []}
breadth_first_search(unweighted_graph, 'A') # (hops, parent_of)
OUTPUT ({'A': 0, 'B': 1, 'C': 1, 'D': 2},
{'A': None, 'B': 'A', 'C': 'A', 'D': 'B'})
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY BFS with collections.deque no install needed
The same algorithm, with a deque so removing from the front is O(1). This is what production BFS looks like when you write it yourself.
CODE from collections import deque
unweighted_graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
hops_from_start, queue = {'A': 0}, deque(['A'])
while queue:
current_node = queue.popleft()
for neighbour in unweighted_graph[current_node]:
if neighbour not in hops_from_start:
hops_from_start[neighbour] = hops_from_start[current_node] + 1
queue.append(neighbour)
hops_from_start
OUTPUT {'A': 0, 'B': 1, 'C': 1, 'D': 2}
CS Algorithms Toolkit Graphs
36
