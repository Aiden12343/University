# generate_permutations

generate_permutations(items) FUNCTION
Return all n! orderings of items.
REMEMBER Fill slot after slot; at each slot try every item not yet used, mark it used, recurse, then unmark it.
WHEN TO USE Need every ordering; n ≤ ~9 (n! explodes).
REQUIRES Nothing (duplicates in items give duplicate permutations).
TIME O(n × n!). SPACE O(n) recursion (+ output).
USED FOR Brute-force travelling salesman, puzzle solving, test generation.
def generate_permutations(items):
all_permutations = []
current_permutation = []
item_already_used = [False] * len(items)
def fill_next_slot():
if len(current_permutation) == len(items):
all_permutations.append(list(current_permutation))
return
for item_index in range(len(items)):
if item_already_used[item_index]:
continue
item_already_used[item_index] = True
current_permutation.append(items[item_index])
fill_next_slot()
current_permutation.pop()
item_already_used[item_index] = False
fill_next_slot()
return all_permutations
INPUT generate_permutations([1, 2, 3])
OUTPUT [[1, 2, 3],
[1, 3, 2],
[2, 1, 3],
[2, 3, 1],
[3, 1, 2],
[3, 2, 1]]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY itertools.permutations no install needed
Lazy generator of every ordering: iterate it instead of building the whole list when n is not tiny. itertools.product covers Cartesian
products.
CODE from itertools import permutations
list(permutations([1, 2, 3]))
OUTPUT [(1, 2, 3),
(1, 3, 2),
(2, 1, 3),
(2, 3, 1),
(3, 1, 2),
(3, 2, 1)]
CS Algorithms Toolkit Backtracking
63
