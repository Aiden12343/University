# reconstruct_path

breadth_first_search CONTINUED · IN PRODUCTION
THIRD-PARTY networkx pip install networkx
NetworkX is the standard graph toolbox: it stores the graph, runs the algorithm and rebuilds paths for you (nx.shortest_path replaces
reconstruct_path too).
CODE import networkx as nx
graph = nx.DiGraph({'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []})
(dict(nx.single_source_shortest_path_length(graph, 'A')), nx.shortest_path(graph, 'A', 'D'))
OUTPUT ({'A': 0, 'B': 1, 'C': 1, 'D': 2}, ['A', 'B', 'D'])
reconstruct_path(parent_of, target_node) FUNCTION
Walk parent links back from target_node to the start, then reverse.
REMEMBER Follow "who discovered me?" backwards until you reach None, then flip the list.
REQUIRES parent_of from BFS / Dijkstra / Bellman-Ford (start maps to None).
TIME O(path length).
NOTE Returns None if target_node was never reached.
def reconstruct_path(parent_of, target_node):
if target_node not in parent_of:
return None
path_nodes = []
current_node = target_node
while current_node is not None:
path_nodes.append(current_node)
current_node = parent_of[current_node]
path_nodes.reverse()
return path_nodes
INPUT parent_of = {'A': None, 'B': 'A', 'D': 'B'} # e.g. from breadth_first_search
reconstruct_path(parent_of, 'D')
OUTPUT ['A', 'B', 'D']
IN PRODUCTION Same as the production variant of breadth_first_search.
CS Algorithms Toolkit Graphs
37
