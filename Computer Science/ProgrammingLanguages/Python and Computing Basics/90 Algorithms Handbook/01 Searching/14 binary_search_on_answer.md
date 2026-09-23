# binary_search_on_answer

binary_search_on_answer(lowest_candidate, highest_candidate, is_good_enough) FUNCTION
Return the SMALLEST integer in range for which is_good_enough is True.
REMEMBER Binary search over possible ANSWERS instead of over a list: if the middle answer works, try smaller; if not, go
bigger.
WHEN TO USE "Minimum X such that condition holds" and checking one X is cheap (min capacity, min speed, integer square root...).
AVOID WHEN Conditions that are not monotonic (False..False True..True).
REQUIRES is_good_enough is monotonic: once True, stays True for bigger values. Returns None if even highest_candidate fails.
TIME O(log(range) × cost of one check). SPACE O(1).
USED FOR Minimum shipping capacity, Koko-eating-bananas, isqrt.
def binary_search_on_answer(lowest_candidate, highest_candidate, is_good_enough):
if not is_good_enough(highest_candidate):
return None
low_value = lowest_candidate
high_value = highest_candidate
while low_value < high_value:
middle_value = (low_value + high_value) // 2
if is_good_enough(middle_value):
high_value = middle_value # middle works: keep it, look lower
else:
low_value = middle_value + 1 # middle fails: must be higher
return low_value
INPUT # smallest whole number whose square is at least 50
binary_search_on_answer(0, 50, lambda candidate: candidate * candidate >= 50)
OUTPUT 8
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY bisect with key= (Python 3.10+) no install needed
Since Python 3.10 bisect accepts a key function, so you can binary-search a range of candidate answers directly. For plain integer square
roots, math.isqrt is the dedicated tool.
CODE from bisect import bisect_left
candidates = range(0, 51)
first_good = bisect_left(candidates, True, key=lambda candidate: candidate * candidate >= 50)
candidates[first_good] # smallest whole number whose square is at least 50
OUTPUT 8
CS Algorithms Toolkit Searching
14
