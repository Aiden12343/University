# selection_sort

selection_sort(items) FUNCTION
Return a sorted copy by repeatedly selecting the minimum.
REMEMBER Find the smallest of what is left and swap it to the front; the sorted boundary grows one slot at a time.
WHEN TO USE Writes are expensive (makes at most n-1 swaps); tiny inputs.
AVOID WHEN Large inputs; when stability matters (it is NOT stable).
REQUIRES Items must be mutually comparable.
TIME O(n2
) ALWAYS (even if already sorted). SPACE O(1). NOT stable.
USED FOR Flash memory / hardware where swaps cost more than compares.
def selection_sort(items):
sorted_items = list(items)
for boundary_index in range(len(sorted_items)):
smallest_index = boundary_index
for scan_index in range(boundary_index + 1, len(sorted_items)):
if sorted_items[scan_index] < sorted_items[smallest_index]:
smallest_index = scan_index
sorted_items[boundary_index], sorted_items[smallest_index] = (
sorted_items[smallest_index], sorted_items[boundary_index])
return sorted_items
INPUT selection_sort([5, 2, 9, 1, 5, 6])
OUTPUT [1, 2, 5, 5, 6, 9]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY heapq.nsmallest (and min) no install needed
Selection sort's real-world job is 'pick the smallest k'. heapq.nsmallest does that in O(n log k) without sorting everything; min() picks just
one.
CODE import heapq
unsorted_numbers = [5, 2, 9, 1, 5, 6]
(heapq.nsmallest(3, unsorted_numbers), min(unsorted_numbers))
OUTPUT ([1, 2, 5], 1)
CS Algorithms Toolkit Sorting
16
