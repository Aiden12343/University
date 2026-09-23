# UnionFind CONTINUED · IN PRODUCTION

UnionFind CONTINUED · IN PRODUCTION
IN PRODUCTION — the call you would actually write
THIRD-PARTY networkx.utils.UnionFind pip install networkx
There is no union-find in the standard library. NetworkX ships a tested one (path compression + union by size); for a one-off, static 'which
items are connected?' question, scipy.sparse.csgraph.connected_components does it in C.
CODE from networkx.utils import UnionFind
groups = UnionFind(['a', 'b', 'c', 'd'])
groups.union('a', 'b')
groups.union('c', 'd')
connected_before_merge = groups['a'] == groups['c'] # groups[x] is x's group leader
groups.union('b', 'c')
(connected_before_merge, groups['a'] == groups['d'])
OUTPUT (False, True)
CS Algorithms Toolkit Data structures the algorithms rely on
28
