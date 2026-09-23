# quickselect_kth_smallest

quickselect_kth_smallest(items, zero_based_rank) FUNCTION
Return the item that WOULD be at index zero_based_rank if sorted.
REMEMBER Quicksort that only follows the side containing the rank you want — the other side is ignored entirely.
WHEN TO USE Median / k-th smallest / top-k threshold without full sort.
AVOID WHEN You need the whole list sorted anyway.
REQUIRES 0 ≤ zero_based_rank < len(items). (0 = smallest.)
TIME O(n) average, O(n2
) worst. SPACE O(n) for the copy; O(1) beyond that.
USED FOR Median finding, percentile stats, "k-th largest element".
def quickselect_kth_smallest(items, zero_based_rank):
if not 0 <= zero_based_rank < len(items):
raise ValueError("zero_based_rank is out of range")
working_items = list(items)
low_index = 0
high_index = len(working_items) - 1
while low_index <= high_index:
pivot_index = _partition_around_pivot(working_items, low_index, high_index)
if pivot_index == zero_based_rank:
return working_items[pivot_index]
if pivot_index < zero_based_rank:
low_index = pivot_index + 1
else:
high_index = pivot_index - 1
INPUT numbers = [7, 10, 4, 3, 20, 15]
quickselect_kth_smallest(numbers, 2) # rank 0 = smallest, so rank 2 = 3rd smallest
OUTPUT 7
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY heapq.nsmallest and statistics.median no install needed
For a small k, nsmallest(k)[-1] is the k-th smallest. statistics.median is the ready-made median. For large arrays, numpy.partition is the true
quickselect.
CODE import heapq, statistics
numbers = [7, 10, 4, 3, 20, 15]
(heapq.nsmallest(3, numbers)[-1], statistics.median(numbers)) # 3rd smallest, median
OUTPUT (7, 8.5)
CS Algorithms Toolkit Sorting
24
