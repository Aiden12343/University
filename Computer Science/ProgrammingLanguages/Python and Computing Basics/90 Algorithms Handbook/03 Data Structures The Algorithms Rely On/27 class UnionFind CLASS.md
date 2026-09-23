# class UnionFind CLASS

class UnionFind CLASS
Disjoint-set: tracks which elements belong to the same group.
REMEMBER Everyone points to a parent; find() climbs to the top boss (and flattens the path on the way back); union()
makes one boss report to the other, hanging the SHORTER tree under the TALLER one.
WHEN TO USE Groups merge over time and you ask "same group?": Kruskal, network connectivity, percolation, image segmentation.
AVOID WHEN You need to SPLIT groups (no un-union), or list group members.
REQUIRES All elements known up front (pass them to the constructor).
TIME ~O(1) amortised per operation (inverse-Ackermann). SPACE O(n).
USED FOR Kruskal's MST, detecting cycles in undirected graphs, friend-circles / connected-components problems.
class UnionFind:
def __init__(self, elements):
self._parent_of = {element: element for element in elements}
self._tree_rank_of = {element: 0 for element in elements}
def find_root(self, element):
root = element
while self._parent_of[root] != root:
root = self._parent_of[root]
while self._parent_of[element] != root: # path compression
next_element = self._parent_of[element]
self._parent_of[element] = root
element = next_element
return root
def union(self, first_element, second_element):
"""Merge the two groups. Return True if they were separate before."""
first_root = self.find_root(first_element)
second_root = self.find_root(second_element)
if first_root == second_root:
return False
if self._tree_rank_of[first_root] < self._tree_rank_of[second_root]:
first_root, second_root = second_root, first_root
self._parent_of[second_root] = first_root # taller tree wins
if self._tree_rank_of[first_root] == self._tree_rank_of[second_root]:
self._tree_rank_of[first_root] += 1
return True
def are_connected(self, first_element, second_element):
return self.find_root(first_element) == self.find_root(second_element)
INPUT groups = UnionFind(['a', 'b', 'c', 'd'])
groups.union('a', 'b')
groups.union('c', 'd')
connected_before_merge = groups.are_connected('a', 'c')
groups.union('b', 'c') # merge the two groups
(connected_before_merge, groups.are_connected('a', 'd'))
OUTPUT (False, True)
CS Algorithms Toolkit Data structures the algorithms rely on
27
