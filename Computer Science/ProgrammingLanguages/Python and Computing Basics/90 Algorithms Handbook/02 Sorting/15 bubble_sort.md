# bubble_sort

2 SORTING
Every function returns a NEW sorted list; input is untouched.
Stable = equal items keep their original relative order (matters when sorting records by one field after another). Python's built-in sorted() is
Timsort: merge + insertion, stable, O(n log n).
bubble_sort(items) FUNCTION
Return a sorted copy using repeated neighbour swaps.
REMEMBER Bubbles float up: swap any neighbours that are out of order; each pass sinks the biggest item to the end;
stop early if a pass swaps nothing.
WHEN TO USE Teaching; detecting "already sorted" cheaply (one pass).
AVOID WHEN Anything real — insertion sort is simpler AND faster.
REQUIRES Items must be mutually comparable (<, >).
TIME O(n
2
) average/worst, O(n) best (already sorted, early
exit).
SPACE O(1) extra (in-place on the copy). STABLE.
USED FOR Exams, demonstrating swaps and invariants.
def bubble_sort(items):
sorted_items = list(items)
for pass_number in range(len(sorted_items) - 1):
swapped_during_pass = False
for position in range(len(sorted_items) - 1 - pass_number):
if sorted_items[position] > sorted_items[position + 1]:
sorted_items[position], sorted_items[position + 1] = (
sorted_items[position + 1], sorted_items[position])
swapped_during_pass = True
if not swapped_during_pass:
break
return sorted_items
INPUT unsorted_numbers = [5, 2, 9, 1, 5, 6]
(bubble_sort(unsorted_numbers), unsorted_numbers) # original left untouched
OUTPUT ([1, 2, 5, 5, 6, 9], [5, 2, 9, 1, 5, 6])
IN PRODUCTION — the call you would actually write
BUILT-IN sorted() and list.sort() no install needed
sorted returns a new list; list.sort() sorts in place. Both use Timsort (stable, O(n log n), O(n) when the data is already nearly sorted) and
accept key= and reverse=. You should almost never hand-write a sort.
CODE unsorted_numbers = [5, 2, 9, 1, 5, 6]
(sorted(unsorted_numbers), sorted(unsorted_numbers, reverse=True))
OUTPUT ([1, 2, 5, 5, 6, 9], [9, 6, 5, 5, 2, 1])
CS Algorithms Toolkit Sorting
15
