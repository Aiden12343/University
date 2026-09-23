# maximum_subarray_sum

maximum_subarray_sum(numbers) FUNCTION
Return the largest sum of any contiguous slice (Kadane's algorithm).
REMEMBER At each number choose: extend the running slice or start fresh here (whichever is bigger); remember the
best running total seen.
WHEN TO USE Best contiguous stretch: stock profit, best streak.
AVOID WHEN Non-contiguous picks (just sum the positives).
REQUIRES Non-empty list of numbers (negatives allowed).
TIME O(n). SPACE O(1).
USED FOR Max profit windows, signal analysis, image max-sum regions.
def maximum_subarray_sum(numbers):
if not numbers:
raise ValueError("numbers must not be empty")
best_sum_ending_here = numbers[0]
best_sum_overall = numbers[0]
for number in numbers[1:]:
best_sum_ending_here = max(number, best_sum_ending_here + number)
best_sum_overall = max(best_sum_overall, best_sum_ending_here)
return best_sum_overall
INPUT maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) # slice 4, -1, 2, 1
OUTPUT 6
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY itertools.accumulate no install needed
accumulate carries a running value through a list with any two-argument function. Kadane's rule becomes one line, and max() picks the
best running total.
CODE from itertools import accumulate
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max(accumulate(numbers, lambda best_ending_here, number: max(number, best_ending_here + number)))
OUTPUT 6
CS Algorithms Toolkit Dynamic programming
57
