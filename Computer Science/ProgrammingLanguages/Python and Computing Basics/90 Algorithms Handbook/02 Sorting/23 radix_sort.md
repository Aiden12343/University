# radix_sort

radix_sort(non_negative_integers) FUNCTION
Return a sorted copy by sorting digit by digit (least significant first).
REMEMBER Sort by the ones digit, then the tens, then the hundreds — each pass drops numbers into 10 buckets (0-9)
and reads them back in order; passes must be STABLE so earlier work survives.
WHEN TO USE Many integers (or fixed-length keys) with a modest digit count.
AVOID WHEN Few items with huge digit counts; non-integer/variable keys.
REQUIRES Every item is an integer ≥ 0.
TIME O(d × (n + 10)) where d = digits in the largest number. SPACE O(n + 10).
USED FOR Sorting IDs, phone numbers, fixed-width strings, punch cards.
def radix_sort(non_negative_integers):
sorted_items = list(non_negative_integers)
if not sorted_items:
return []
largest_value = max(sorted_items)
digit_place = 1 # 1, 10, 100, ...
while largest_value // digit_place > 0:
buckets_by_digit = [[] for _ in range(10)]
for number in sorted_items:
digit = (number // digit_place) % 10
buckets_by_digit[digit].append(number) # appending keeps order
sorted_items = [number for bucket in buckets_by_digit for number in bucket]
digit_place *= 10
return sorted_items
INPUT radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) # non-negative integers only
OUTPUT [2, 24, 45, 66, 75, 90, 170, 802]
IN PRODUCTION — the call you would actually write
BUILT-IN sorted() no install needed
There is no radix sort in the standard library and sorted() is almost always fast enough. NumPy's stable sort (kind='stable') can use a radix
sort for small integer types when you have huge arrays.
CODE sorted([170, 45, 75, 90, 802, 24, 2, 66])
OUTPUT [2, 24, 45, 66, 75, 90, 170, 802]
CS Algorithms Toolkit Sorting
23
