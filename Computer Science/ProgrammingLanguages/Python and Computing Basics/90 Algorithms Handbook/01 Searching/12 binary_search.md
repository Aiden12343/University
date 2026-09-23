# binary_search

binary_search(sorted_items, target) FUNCTION
Return the index of target in sorted_items, or -1 if absent.
REMEMBER Guess the middle. Too small? Throw away the left half. Too big? Throw away the right half. Stop when the
two ends cross.
WHEN TO USE Data is sorted (or can be sorted once) and searched often; random-access containers such as lists/arrays.
AVOID WHEN Unsorted data (gives WRONG answers); linked lists (no O(1) middle access); very small lists (linear is just as fast).
REQUIRES sorted_items MUST be sorted ascending.
TIME O(log n). SPACE O(1) iterative (O(log n) if written recursively).
USED FOR Dictionary lookup, git bisect, finding a record in a sorted DB index, debugging "which commit broke it".
def binary_search(sorted_items, target):
low_index = 0
high_index = len(sorted_items) - 1
while low_index <= high_index:
middle_index = low_index + (high_index - low_index) // 2 # no overflow
middle_value = sorted_items[middle_index]
if middle_value == target:
return middle_index
if middle_value < target:
low_index = middle_index + 1
else:
high_index = middle_index - 1
return -1
INPUT sorted_numbers = [1, 3, 5, 8, 13, 21] # MUST be sorted
binary_search(sorted_numbers, 8)
OUTPUT 3
INPUT binary_search([1, 3, 5, 8, 13, 21], 4) # not present
OUTPUT -1
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY bisect.bisect_left no install needed
bisect does the halving for you and returns an insertion point, not a yes/no: check the slot yourself to know whether the value is really
there. Data must still be sorted.
CODE from bisect import bisect_left
sorted_numbers = [1, 3, 5, 8, 13, 21] # MUST be sorted
position = bisect_left(sorted_numbers, 8)
found = position < len(sorted_numbers) and sorted_numbers[position] == 8
(position, found)
OUTPUT (3, True)
CS Algorithms Toolkit Searching
12
