# From scratch to production

From scratch to production
The hand-written versions in this handbook teach you what is happening and are what exams ask for. At work you would normally
call a tested library instead: it is faster (often compiled C), handles edge cases, and is code someone else maintains. Every entry that
has such a replacement shows it under IN PRODUCTION; all of those snippets were actually executed (Python 3.12) and the printed
output is real.
Standard library and built-in items need nothing installed. Third-party items need pip install networkx scipy numpy sympy
rapidfuzz sortedcontainers. Version notes: bisect key= needs Python 3.10+; graphlib, math.lcm and functools.cache need
3.9+.
Hand-written here Production call Package Kind
linear_search items.index(target) · target in set(items) built-in built-in
binary_search bisect.bisect_left(sorted_items, target) bisect standard library
lower_bound bisect.bisect_left / bisect.bisect_right bisect standard library
binary_search_on_answer bisect_left(range(lo, hi + 1), True,
key=is_good_enough)
bisect standard library
bubble_sort sorted(items) · items.sort() built-in built-in
selection_sort heapq.nsmallest(k, items) heapq standard library
insertion_sort bisect.insort(sorted_list, item) bisect standard library
merge_two_sorted_lists heapq.merge(*sorted_iterables) heapq standard library
merge_sort sorted(items, key=...) built-in built-in
quick_sort numpy.sort(array) numpy third-party
heap_sort heapq.heapify(items); heapq.heappop(items) heapq standard library
counting_sort collections.Counter(items) collections standard library
radix_sort sorted(numbers) built-in built-in
quickselect_kth_smallest heapq.nsmallest(k, items)[-1] ·
statistics.median(items)
heapq / statistics standard library
MinHeap heapq.heappush / heapq.heappop heapq standard library
UnionFind networkx.utils.UnionFind(elements) networkx third-party
Trie bisect_left(words, prefix) bisect standard library
bst_insert bisect.insort(sorted_list, value) bisect standard library
bst_insert SortedList(values).add(value) sortedcontainers third-party
bst_search bisect_left(sorted_values, target) bisect standard library
traverse_in_order list(SortedList(values)) sortedcontainers third-party
traverse_level_order deque.popleft() collections standard library
breadth_first_search deque.popleft() collections standard library
breadth_first_search nx.single_source_shortest_path_length(G,
start)
networkx third-party
depth_first_search nx.dfs_preorder_nodes(G, start) networkx third-party
connected_components nx.connected_components(G) networkx third-party
topological_sort TopologicalSorter(predecessors).static_order() graphlib standard library
dijkstra heapq.heappush / heapq.heappop heapq standard library
dijkstra nx.single_source_dijkstra(G, start) networkx third-party
bellman_ford nx.single_source_bellman_ford(G, start) networkx third-party
floyd_warshall nx.floyd_warshall(G) networkx third-party
kruskal_minimum_spanning_tree nx.minimum_spanning_tree(G,
algorithm='kruskal')
networkx third-party
prim_minimum_spanning_tree nx.minimum_spanning_tree(G, algorithm='prim') networkx third-party
a_star_search nx.astar_path(G, start, goal, heuristic) networkx third-party
CS Algorithms Toolkit From scratch to production
7
