# _quick_sort_range

_quick_sort_range(items, low_index, high_index) HELPER
Sort items[low..high] IN PLACE: partition, then recurse on both sides.
REMEMBER Partitioning puts the pivot in its final slot, which leaves two independent, smaller quick-sort problems on
either side.
def _quick_sort_range(items, low_index, high_index):
if low_index >= high_index:
return
pivot_index = _partition_around_pivot(items, low_index, high_index)
_quick_sort_range(items, low_index, pivot_index - 1)
_quick_sort_range(items, pivot_index + 1, high_index)
INPUT items = [5, 2, 9, 1, 6]
_quick_sort_range(items, 0, len(items) - 1) # sorts IN PLACE, returns None
items
OUTPUT [1, 2, 5, 6, 9]
quick_sort(items) FUNCTION
Return a sorted copy using partitioning around a pivot.
REMEMBER Pick a pivot, shove smaller things to its left and bigger things to its right (the pivot is now in its final place),
then repeat on the left part and the right part.
WHEN TO USE General-purpose in-memory sorting of arrays; usually the fastest in practice thanks to cache-friendly in-place work.
AVOID WHEN Need guaranteed O(n log n) or STABILITY; input with MANY duplicates (this Lomuto version degrades to O(n
2
) and can
hit Python's recursion limit — use 3-way partition or merge sort).
REQUIRES Items must be mutually comparable.
TIME O(n log n) average, O(n2
) worst (bad pivots). SPACE O(log n) recursion stack on average. NOT stable.
USED FOR C's qsort, most language standard libraries (introsort).
def quick_sort(items):
sorted_items = list(items)
_quick_sort_range(sorted_items, 0, len(sorted_items) - 1)
return sorted_items
INPUT quick_sort([5, 2, 9, 1, 5, 6])
OUTPUT [1, 2, 5, 5, 6, 9]
IN PRODUCTION — the call you would actually write
THIRD-PARTY numpy.sort pip install numpy
For big numeric arrays NumPy's C implementation (introsort, with SIMD paths on modern CPUs) is far faster than sorted() on a Python list.
Use plain sorted() for ordinary lists.
CODE import numpy
numpy.sort(numpy.array([5, 2, 9, 1, 5, 6])).tolist()
OUTPUT [1, 2, 5, 5, 6, 9]
CS Algorithms Toolkit Sorting
20
