# rabin_karp_search

rabin_karp_search(text, pattern) FUNCTION
Return all start indices where pattern occurs in text (rolling hash).
REMEMBER Turn each text window into a number (hash); slide the window by subtracting the leaving character and
adding the arriving one; only compare characters when the hashes are equal.
WHEN TO USE Searching for MANY patterns of equal length; plagiarism checks.
AVOID WHEN Worst-case guarantees needed (hash collisions → O(n × m)).
REQUIRES Strings; empty pattern returns [].
TIME O(n + m) average, O(n × m) worst. SPACE O(1).
USED FOR Duplicate-document detection, rsync-style chunk matching.
def rabin_karp_search(text, pattern):
pattern_length = len(pattern)
if pattern_length == 0 or pattern_length > len(text):
return []
alphabet_size = 256
hash_modulus = 1_000_000_007
highest_place_value = pow(alphabet_size, pattern_length - 1, hash_modulus)
pattern_hash = 0
window_hash = 0
for position in range(pattern_length):
pattern_hash = (pattern_hash * alphabet_size + ord(pattern[position])) % hash_modulus
window_hash = (window_hash * alphabet_size + ord(text[position])) % hash_modulus
match_start_indices = []
for window_start in range(len(text) - pattern_length + 1):
if (window_hash == pattern_hash
and text[window_start:window_start + pattern_length] == pattern):
match_start_indices.append(window_start)
if window_start + pattern_length < len(text):
leaving_value = ord(text[window_start])
arriving_value = ord(text[window_start + pattern_length])
window_hash = ((window_hash - leaving_value * highest_place_value)
* alphabet_size + arriving_value) % hash_modulus
return match_start_indices
INPUT text = 'abababca'
rabin_karp_search(text, 'aba')
OUTPUT [0, 2]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY re with alternation no install needed
To search for several patterns at once, join them into one regex alternation. For thousands of patterns use Aho-Corasick (the
pyahocorasick package).
CODE import re
text = 'abababca'
patterns = ['aba', 'bca']
combined = '|'.join(map(re.escape, patterns))
[(match.start(), match.group()) for match in re.finditer(combined, text)]
OUTPUT [(0, 'aba'), (5, 'bca')]
CS Algorithms Toolkit String matching
72
