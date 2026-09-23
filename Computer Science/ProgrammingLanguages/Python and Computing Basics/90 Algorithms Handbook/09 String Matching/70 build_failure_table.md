# build_failure_table

9 STRING MATCHING
Find every start index of pattern inside text.
Naive matching is O(n × m). These two avoid re-checking characters.
build_failure_table(pattern) FUNCTION
For each prefix of pattern: length of its longest proper prefix that is also a suffix. Tells KMP how far to fall back after a
mismatch.
REMEMBER Match the pattern against ITSELF; on a mismatch fall back using the table entries already computed.
TIME · SPACE O(m).
def build_failure_table(pattern):
prefix_suffix_length = [0] * len(pattern)
matched_length = 0
for position in range(1, len(pattern)):
while matched_length > 0 and pattern[position] != pattern[matched_length]:
matched_length = prefix_suffix_length[matched_length - 1]
if pattern[position] == pattern[matched_length]:
matched_length += 1
prefix_suffix_length[position] = matched_length
return prefix_suffix_length
INPUT build_failure_table('ababaca')
OUTPUT [0, 0, 1, 2, 3, 0, 1]
IN PRODUCTION Internal KMP helper. Production code uses str.find or re instead (see kmp_search).
CS Algorithms Toolkit String matching
70
