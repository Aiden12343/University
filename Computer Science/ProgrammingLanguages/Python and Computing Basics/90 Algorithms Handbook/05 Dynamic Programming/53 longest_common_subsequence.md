# longest_common_subsequence

longest_common_subsequence(first_text, second_text) FUNCTION
Return one longest subsequence common to both strings.
REMEMBER table[a][b] = LCS length of the first a and first b characters. Characters match → diagonal + 1; otherwise the
max of "skip one from first" (up) and "skip one from second" (left). Trace back from the corner to rebuild the
string.
WHEN TO USE Diff tools, DNA similarity, plagiarism, version comparison.
AVOID WHEN You need CONTIGUOUS matches (that's longest common substring).
REQUIRES Two strings (subsequence = order kept, gaps allowed).
TIME O(m × n). SPACE O(m × n) (needed for the traceback).
USED FOR diff, git merges, bioinformatics sequence alignment.
def longest_common_subsequence(first_text, second_text):
first_length = len(first_text)
second_length = len(second_text)
common_length_table = [[0] * (second_length + 1) for _ in range(first_length + 1)]
for first_position in range(1, first_length + 1):
for second_position in range(1, second_length + 1):
if first_text[first_position - 1] == second_text[second_position - 1]:
common_length_table[first_position][second_position] = (
common_length_table[first_position - 1][second_position - 1] + 1)
else:
common_length_table[first_position][second_position] = max(
common_length_table[first_position - 1][second_position],
common_length_table[first_position][second_position - 1])
characters_in_reverse = []
first_position, second_position = first_length, second_length
while first_position > 0 and second_position > 0:
if first_text[first_position - 1] == second_text[second_position - 1]:
characters_in_reverse.append(first_text[first_position - 1])
first_position -= 1
second_position -= 1
elif (common_length_table[first_position - 1][second_position]
>= common_length_table[first_position][second_position - 1]):
first_position -= 1
else:
second_position -= 1
return "".join(reversed(characters_in_reverse))
INPUT longest_common_subsequence('ABCBDAB', 'BDCABA')
OUTPUT 'BCBA'
IN PRODUCTION — the call you would actually write
THIRD-PARTY rapidfuzz.distance.LCSseq pip install rapidfuzz
RapidFuzz implements exact LCS length in optimised C++. Beware difflib.SequenceMatcher: it finds contiguous matching blocks, which is
NOT the same as a longest common subsequence.
CODE from rapidfuzz.distance import LCSseq
LCSseq.similarity('ABCBDAB', 'BDCABA') # length of the longest common subsequence
OUTPUT 4
CS Algorithms Toolkit Dynamic programming
53
