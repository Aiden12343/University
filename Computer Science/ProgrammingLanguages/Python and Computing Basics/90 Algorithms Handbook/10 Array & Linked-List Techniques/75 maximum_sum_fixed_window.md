# maximum_sum_fixed_window

maximum_sum_fixed_window(numbers, window_size) FUNCTION
Return the largest sum of any window_size consecutive numbers.
REMEMBER Slide the window: add the number entering, subtract the number leaving — never re-sum from scratch.
WHEN TO USE Contiguous fixed-length ranges (moving averages, best k days).
REQUIRES 1 ≤ window_size ≤ len(numbers).
TIME O(n). SPACE O(1).
def maximum_sum_fixed_window(numbers, window_size):
if window_size <= 0 or window_size > len(numbers):
raise ValueError("window_size must be between 1 and len(numbers)")
window_sum = sum(numbers[:window_size])
best_window_sum = window_sum
for entering_index in range(window_size, len(numbers)):
window_sum += numbers[entering_index] - numbers[entering_index - window_size]
best_window_sum = max(best_window_sum, window_sum)
return best_window_sum
INPUT numbers = [2, 1, 5, 1, 3, 2]
maximum_sum_fixed_window(numbers, 3) # best 3 in a row: 5 + 1 + 3
OUTPUT 9
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY itertools.accumulate prefix sums no install needed
Prefix sums make every window sum a single subtraction. (NumPy users would reach for numpy.convolve or sliding_window_view.)
CODE from itertools import accumulate
numbers, window_size = [2, 1, 5, 1, 3, 2], 3
prefix_sums = list(accumulate(numbers, initial=0))
window_ends = range(window_size, len(numbers) + 1)
max(prefix_sums[end] - prefix_sums[end - window_size] for end in window_ends)
OUTPUT 9
longest_unique_substring_length(text) FUNCTION
Return the length of the longest substring with no repeated character.
REMEMBER Variable-size window: remember where each character was last seen; when a repeat appears inside the
window, jump the window start to just past that earlier copy.
TIME O(n). SPACE O(alphabet size).
USED FOR Longest run without repeats, sliding-window interview classics.
def longest_unique_substring_length(text):
last_seen_position = {}
window_start = 0
longest_length = 0
for position, character in enumerate(text):
if character in last_seen_position and last_seen_position[character] >= window_start:
window_start = last_seen_position[character] + 1
last_seen_position[character] = position
longest_length = max(longest_length, position - window_start + 1)
return longest_length
INPUT longest_unique_substring_length('abcabcbb') # 'abc'
OUTPUT 3
IN PRODUCTION No library: the sliding window is the production solution.
CS Algorithms Toolkit Array & linked-list techniques
75
