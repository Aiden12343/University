# generate_subsets

7 BACKTRACKING
Build a candidate step by step; undo when it dead-ends.
Template: choose → explore (recurse) → un-choose. Prune early whenever a partial answer can no longer work.
generate_subsets(items) FUNCTION
Return all 2n
subsets (the power set) of items.
REMEMBER For each item, either LEAVE it or TAKE it, recurse to the next item, and undo the "take" afterwards.
WHEN TO USE Need every combination; small n (≤ ~20).
AVOID WHEN Large n — output size alone is 2n
.
REQUIRES Nothing.
TIME O(n × 2n
). SPACE O(n) recursion (+ output).
USED FOR Subset-sum, feature selection, brute force baselines.
def generate_subsets(items):
all_subsets = []
current_subset = []
def decide_from(position):
if position == len(items):
all_subsets.append(list(current_subset))
return
decide_from(position + 1) # leave it
current_subset.append(items[position]) # take it
decide_from(position + 1)
current_subset.pop() # undo
decide_from(0)
return all_subsets
INPUT generate_subsets([1, 2, 3])
OUTPUT [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY itertools.combinations no install needed
combinations(items, size) yields every subset of one size, lazily. Chain the sizes 0..n to get the whole power set.
CODE from itertools import chain, combinations
items = [1, 2, 3]
list(chain.from_iterable(combinations(items, size) for size in range(len(items) + 1)))
OUTPUT [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
CS Algorithms Toolkit Backtracking
62
