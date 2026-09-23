# Trie CONTINUED · IN PRODUCTION

Trie CONTINUED · IN PRODUCTION
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY bisect on a sorted word list no install needed
For a fixed word list you don't need a trie: sort once, then binary-search the prefix range. Reach for a real trie library (pygtrie, marisa-trie)
or a search engine when the set is huge or changes constantly.
CODE from bisect import bisect_left
words = sorted(['car', 'card', 'care', 'cat', 'dog'])
prefix = 'car'
start = bisect_left(words, prefix)
end = bisect_left(words, prefix + '\U0010ffff') # just past every word starting with prefix
words[start:end]
OUTPUT ['car', 'card', 'care']
class TreeNode CLASS
One node of a binary tree.
class TreeNode:
def __init__(self, value):
self.value = value
self.left_child = None
self.right_child = None
INPUT node = TreeNode(5)
(node.value, node.left_child, node.right_child)
OUTPUT (5, None, None)
IN PRODUCTION Plain classes or @dataclass in production; Python has no built-in tree type.
CS Algorithms Toolkit Data structures the algorithms rely on
30
