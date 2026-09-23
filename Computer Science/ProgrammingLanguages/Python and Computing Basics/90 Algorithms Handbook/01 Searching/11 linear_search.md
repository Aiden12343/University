# linear_search

1 SEARCHING
linear_search(items, target) FUNCTION
Return the index of the first match of target, or -1 if absent.
REMEMBER Walk down the line asking each item "are you the one?" and give up at the end.
WHEN TO USE Unsorted data; tiny lists; you only search once (sorting first would cost more than just looking).
AVOID WHEN Big collections searched repeatedly — use a set/dict (O(1)) or sort once and use binary search.
REQUIRES Nothing. Works on any sequence, sorted or not.
TIME O(n) worst/average, O(1) best. SPACE O(1).
USED FOR Finding an item in an unsorted list, in operator internals.
def linear_search(items, target):
for index, item in enumerate(items):
if item == target:
return index
return -1
INPUT shopping_list = ['milk', 'eggs', 'bread'] # order does not matter
linear_search(shopping_list, 'eggs')
OUTPUT 1
INPUT linear_search([4, 2, 7], 9) # not present
OUTPUT -1
IN PRODUCTION — the call you would actually write
BUILT-IN list.index, the in operator, and set no install needed
list.index and in are the C-speed linear search. If you look things up more than a few times, build a set or dict once: every lookup is then
O(1) instead of O(n).
CODE shopping_list = ['milk', 'eggs', 'bread']
in_stock = set(shopping_list) # build once, then every lookup is O(1)
(shopping_list.index('eggs'), 'eggs' in in_stock, 'jam' in in_stock)
OUTPUT (1, True, False)
CS Algorithms Toolkit Searching
11
