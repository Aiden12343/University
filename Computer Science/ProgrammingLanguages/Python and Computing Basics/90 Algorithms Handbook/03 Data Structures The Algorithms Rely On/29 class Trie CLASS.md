# class Trie CLASS

class Trie CLASS
Prefix tree for storing many strings.
REMEMBER A tree of letters: each step down is one character, and a special flag marks "a word ends here".
WHEN TO USE Autocomplete, prefix search, spell-check, dictionary of words sharing prefixes, IP routing.
AVOID WHEN Only exact lookups (a set is simpler/faster); memory-tight.
REQUIRES Keys are strings (or sequences of hashable symbols).
TIME insert / lookup / prefix check O(L), L = word length
(independent of how many words are stored).
SPACE O(total characters stored) — can be large.
USED FOR Search-box suggestions, T9 phone keyboards, word games.
class Trie:
END_OF_WORD = None # dictionary key that cannot clash with a character
def __init__(self):
self._root = {}
def insert(self, word):
node = self._root
for character in word:
node = node.setdefault(character, {})
node[Trie.END_OF_WORD] = True
def _walk(self, text):
node = self._root
for character in text:
if character not in node:
return None
node = node[character]
return node
def contains_word(self, word):
node = self._walk(word)
return node is not None and Trie.END_OF_WORD in node
def has_prefix(self, prefix):
return self._walk(prefix) is not None
def words_with_prefix(self, prefix):
"""Return every stored word starting with prefix, alphabetically."""
start_node = self._walk(prefix)
if start_node is None:
return []
found_words = []
stack = [(start_node, prefix)]
while stack:
node, text_so_far = stack.pop()
for key, child_node in node.items():
if key is Trie.END_OF_WORD:
found_words.append(text_so_far)
else:
stack.append((child_node, text_so_far + key))
return sorted(found_words)
INPUT trie = Trie()
for word in ['car', 'card', 'care', 'cat']:
trie.insert(word)
(trie.contains_word('car'), trie.contains_word('ca'), trie.words_with_prefix('car'))
OUTPUT (True, False, ['car', 'card', 'care'])
CS Algorithms Toolkit Data structures the algorithms rely on
29
