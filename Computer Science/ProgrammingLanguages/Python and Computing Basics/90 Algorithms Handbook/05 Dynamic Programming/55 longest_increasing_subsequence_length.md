# longest_increasing_subsequence_length

longest_increasing_subsequence_length(numbers) FUNCTION
Return the length of the longest strictly increasing subsequence.
REMEMBER Keep a list where slot k holds the SMALLEST possible tail of an increasing run of length k+1. For each number,
binary-search (lower_bound) its slot: replace it, or append if it's bigger than all tails.
WHEN TO USE Longest rising trend, patience sorting, scheduling chains.
REQUIRES Numbers comparable.
TIME O(n log n) (the simple DP version is O(n2
)). SPACE O(n).
USED FOR Stacking boxes/envelopes, version-history analysis.
NOTE The list is NOT the actual subsequence, only its length is right. For non-decreasing runs, use an upper bound instead.
def longest_increasing_subsequence_length(numbers):
smallest_tail_for_length = []
for number in numbers:
slot_index = lower_bound(smallest_tail_for_length, number)
if slot_index == len(smallest_tail_for_length):
smallest_tail_for_length.append(number)
else:
smallest_tail_for_length[slot_index] = number
return len(smallest_tail_for_length)
INPUT longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18]) # e.g. 2, 5, 7, 101
OUTPUT 4
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY the same algorithm with bisect_left no install needed
bisect_left replaces the hand-written lower_bound. There is no ready-made LIS function, so this is the production form.
CODE from bisect import bisect_left
smallest_tail_for_length = []
for number in [10, 9, 2, 5, 3, 7, 101, 18]:
slot_index = bisect_left(smallest_tail_for_length, number)
smallest_tail_for_length[slot_index:slot_index + 1] = [number] # replace slot / append
len(smallest_tail_for_length)
OUTPUT 4
CS Algorithms Toolkit Dynamic programming
55
