# kmp_search

kmp_search(text, pattern) FUNCTION
Return all start indices where pattern occurs in text (Knuth-Morris-Pratt).
REMEMBER Slide through text never moving backwards; on a mismatch use the failure table to jump the pattern forward
by the border it already matched instead of restarting.
WHEN TO USE Guaranteed linear time; long texts with repetitive patterns.
AVOID WHEN Trivial one-off searches (Python's str.find is fine); many patterns at once (Aho-Corasick).
REQUIRES Strings; empty pattern returns [].
TIME O(n + m). SPACE O(m).
USED FOR Text editors' find, DNA search, intrusion detection.
def kmp_search(text, pattern):
if pattern == "":
return []
failure_table = build_failure_table(pattern)
match_start_indices = []
matched_length = 0
for text_position, character in enumerate(text):
while matched_length > 0 and character != pattern[matched_length]:
matched_length = failure_table[matched_length - 1]
if character == pattern[matched_length]:
matched_length += 1
if matched_length == len(pattern):
match_start_indices.append(text_position - len(pattern) + 1)
matched_length = failure_table[matched_length - 1]
return match_start_indices
INPUT text = 'abababca'
kmp_search(text, 'aba') # start indices, overlaps allowed
OUTPUT [0, 2]
IN PRODUCTION — the call you would actually write
BUILT-IN str.find, in, and re.finditer no install needed
CPython's string search is heavily optimised C, so in and str.find are the answer for one match. For every start index, including overlaps,
use a regex with a lookahead.
CODE import re
text, pattern = 'abababca', 'aba'
every_start = [m.start() for m in re.finditer(f'(?={re.escape(pattern)})', text)] # overlaps too
(pattern in text, text.find(pattern), every_start)
OUTPUT (True, 0, [0, 2])
CS Algorithms Toolkit String matching
71
