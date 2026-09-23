# lower_bound

lower_bound(sorted_items, target) FUNCTION
Return the FIRST index whose item is ≥ target (insertion point).
REMEMBER Binary search that never shouts "found": if middle is too small go right of it, otherwise KEEP it and go left;
where the two ends meet is the answer.
WHEN TO USE First occurrence among duplicates; where to insert to keep the list sorted; counting items < target (the returned index).
AVOID WHEN Unsorted data.
REQUIRES sorted_items MUST be sorted ascending.
TIME O(log n). SPACE O(1).
USED FOR Python's bisect_left, range queries, LIS algorithm below. (Last occurrence = lower_bound(target + 1) - 1 for integers.)
def lower_bound(sorted_items, target):
low_index = 0
high_index = len(sorted_items) # high is EXCLUSIVE here
while low_index < high_index:
middle_index = (low_index + high_index) // 2
if sorted_items[middle_index] < target:
low_index = middle_index + 1
else:
high_index = middle_index
return low_index
INPUT sorted_numbers = [1, 3, 3, 3, 5, 8] # MUST be sorted
lower_bound(sorted_numbers, 3) # first of the 3s
OUTPUT 1
INPUT lower_bound([1, 3, 3, 3, 5, 8], 4) # 4 would be inserted here
OUTPUT 4
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY bisect_left and bisect_right no install needed
bisect_left is exactly lower_bound (first index ≥ target). bisect_right is its twin (first index > target), so the pair gives the whole run of
duplicates.
CODE from bisect import bisect_left, bisect_right
sorted_numbers = [1, 3, 3, 3, 5, 8]
(bisect_left(sorted_numbers, 3), bisect_right(sorted_numbers, 3), bisect_left(sorted_numbers, 4))
OUTPUT (1, 4, 4)
CS Algorithms Toolkit Searching
13
