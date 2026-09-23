# insertion_sort

insertion_sort(items) FUNCTION
Return a sorted copy by inserting each item into the sorted prefix.
REMEMBER Sort like a hand of cards: pick up the next card and slide it left past every bigger card until it fits.
WHEN TO USE Small lists (< ~20), nearly-sorted data, streaming data that arrives one item at a time (online). Fast in practice.
AVOID WHEN Large, random data.
REQUIRES Items must be mutually comparable.
TIME O(n2
) average/worst, O(n) best (already/nearly sorted). SPACE O(1). STABLE.
USED FOR Inner loop of Timsort/introsort for small chunks, sorting a hand of cards, keeping a small list sorted as items arrive.
def insertion_sort(items):
sorted_items = list(items)
for unsorted_index in range(1, len(sorted_items)):
value_to_insert = sorted_items[unsorted_index]
shift_index = unsorted_index - 1
while shift_index >= 0 and sorted_items[shift_index] > value_to_insert:
sorted_items[shift_index + 1] = sorted_items[shift_index]
shift_index -= 1
sorted_items[shift_index + 1] = value_to_insert
return sorted_items
INPUT insertion_sort([5, 2, 9, 1, 5, 6])
OUTPUT [1, 2, 5, 5, 6, 9]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY bisect.insort no install needed
insort drops each new item into its correct slot, keeping a list sorted as items arrive: the 'hand of cards' idea. It is O(n) per insert (shifting),
so use sortedcontainers.SortedList when the list gets big.
CODE from bisect import insort
hand = []
for card in [5, 2, 9, 1, 5, 6]:
insort(hand, card) # slide each new card into place
hand
OUTPUT [1, 2, 5, 5, 6, 9]
CS Algorithms Toolkit Sorting
17
