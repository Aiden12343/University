# merge_sort

merge_sort(items) FUNCTION
Return a sorted copy using divide and conquer.
REMEMBER Split in half, sort each half (recursively), then zip the two sorted halves together taking the smaller front each
time.
WHEN TO USE You need guaranteed O(n log n); need STABILITY; sorting linked lists; data too big for memory (external sort).
AVOID WHEN Memory is tight (needs O(n) extra) — use heap sort/quick sort.
REQUIRES Items must be mutually comparable.
TIME O(n log n) best/average/worst. SPACE O(n). STABLE.
USED FOR Python's sorted() (Timsort), database sorting, counting inversions, sorting huge files.
def merge_sort(items):
if len(items) <= 1:
return list(items)
middle_index = len(items) // 2
sorted_left_half = merge_sort(items[:middle_index])
sorted_right_half = merge_sort(items[middle_index:])
return merge_two_sorted_lists(sorted_left_half, sorted_right_half)
INPUT merge_sort([5, 2, 9, 1, 5, 6])
OUTPUT [1, 2, 5, 5, 6, 9]
IN PRODUCTION — the call you would actually write
BUILT-IN sorted() with key= (stable) no install needed
Timsort is a merge sort under the hood. Because it is stable you can sort by one field, then another, and earlier order survives among ties.
CODE records = [('bob', 25), ('amy', 30), ('cat', 25)]
sorted(records, key=lambda record: record[1]) # bob stays ahead of cat: stable
OUTPUT [('bob', 25), ('cat', 25), ('amy', 30)]
_partition_around_pivot(items, low_index, high_index) HELPER
(Lomuto partition) Rearrange items[low..high] in place around a pivot and return the pivot's final index. Everything left of
it is smaller.
REMEMBER Park the pivot at the end, sweep along; every item smaller than the pivot is swapped into the "small zone" at
the front; finally drop the pivot right after the small zone.
def _partition_around_pivot(items, low_index, high_index):
middle_index = (low_index + high_index) // 2 # middle pivot: dodges the
items[middle_index], items[high_index] = ( # sorted-input worst case
items[high_index], items[middle_index])
pivot_value = items[high_index]
small_zone_end = low_index # first slot NOT yet small
for scan_index in range(low_index, high_index):
if items[scan_index] < pivot_value:
items[scan_index], items[small_zone_end] = (
items[small_zone_end], items[scan_index])
small_zone_end += 1
items[small_zone_end], items[high_index] = (
items[high_index], items[small_zone_end])
return small_zone_end
INPUT items = [5, 2, 9, 1, 6]
pivot_final_index = _partition_around_pivot(items, 0, len(items) - 1) # in place
(pivot_final_index, items) # smaller left of pivot, bigger right
OUTPUT (4, [5, 2, 6, 1, 9])
CS Algorithms Toolkit Sorting
19
