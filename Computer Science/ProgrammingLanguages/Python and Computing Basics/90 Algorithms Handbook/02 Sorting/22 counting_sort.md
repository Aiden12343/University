# counting_sort

counting_sort(non_negative_integers) FUNCTION
Return a sorted copy by tallying how often each value occurs.
REMEMBER Tally how many of each number exist, then read the tallies out in order: "two 0s, zero 1s, three 2s..."
WHEN TO USE Integers in a SMALL known range (ages, grades, byte values).
AVOID WHEN Huge value range (memory = max value); floats; strings; negative numbers (offset them first).
REQUIRES Every item is an integer ≥ 0. Range k = max value is small.
TIME O(n + k). SPACE O(k).
USED FOR Sorting exam scores, byte/characters, sub-step of radix sort.
def counting_sort(non_negative_integers):
if not non_negative_integers:
return []
occurrence_count_of_value = [0] * (max(non_negative_integers) + 1)
for value in non_negative_integers:
occurrence_count_of_value[value] += 1
sorted_items = []
for value, occurrence_count in enumerate(occurrence_count_of_value):
sorted_items.extend([value] * occurrence_count)
return sorted_items
INPUT counting_sort([3, 0, 2, 3, 1, 0]) # non-negative integers only
OUTPUT [0, 0, 1, 2, 3, 3]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY collections.Counter no install needed
Counter is the library 'tally table'. Counter.elements() replays each value as often as it occurred; sorted() then orders the distinct values.
CODE from collections import Counter
tallies = Counter([3, 0, 2, 3, 1, 0])
(sorted(tallies.elements()), dict(tallies))
OUTPUT ([0, 0, 1, 2, 3, 3], {3: 2, 0: 2, 2: 1, 1: 1})
CS Algorithms Toolkit Sorting
22
