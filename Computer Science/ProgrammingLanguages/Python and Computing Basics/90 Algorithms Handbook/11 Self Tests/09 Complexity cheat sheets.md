# Complexity cheat sheets

Complexity cheat sheets
Sorting
Algorithm Best Average Worst Extra space Stable Note
Bubble sort O(n) O(n²) O(n²) O(1) Yes Early exit when a pass makes no
swaps
Selection sort O(n²) O(n²) O(n²) O(1) No At most n−1 swaps
Insertion sort O(n) O(n²) O(n²) O(1) Yes Best for small / nearly sorted
Merge sort O(n log n) O(n log n) O(n log n) O(n) Yes Guaranteed; external sorting
Quick sort O(n log n) O(n log n) O(n²) O(log n) No Bad pivots / many duplicates hurt
Heap sort O(n log n) O(n log n) O(n log n) O(1) No Guaranteed and in place
Counting sort O(n + k) O(n + k) O(n + k) O(k) — Integers in a small range k
Radix sort (LSD) O(d(n + b)) O(d(n + b)) O(d(n + b)) O(n + b) Yes d digits, base b
Timsort (built-in sorted) O(n) O(n log n) O(n log n) O(n) Yes Merge + insertion hybrid
Quickselect (k-th smallest) O(n) O(n) O(n²) O(1) — Partial quick sort
Searching and data-structure operations
Structure / operation Average Worst Note
Linear search O(n) O(n) Any sequence
Binary search (sorted array) O(log n) O(log n) Data must be sorted
Hash table (dict / set): lookup, insert, delete O(1) O(n) Worst case = many collisions
Binary search tree: search, insert O(log n) O(n) Worst case on sorted input
Balanced BST (AVL, red-black) O(log n) O(log n) Self-balancing
Binary heap: push / pop-min O(log n) O(log n) Peek O(1); build heap O(n)
Union-Find (rank + path compression) ≈ O(1) ≈ O(1) Amortised, inverse Ackermann
Trie: insert / search O(L) O(L) L = key length
Stack push/pop, queue enqueue/dequeue O(1) O(1) Python list end / index pointer
Linked list: search / access O(n) O(n) Insert or delete at a known node is O(1)
Python built-ins worth knowing
Operation Cost Note
lst[i], len(lst), lst.append(x), lst.pop() O(1) append is amortised O(1)
lst.insert(0, x), lst.pop(0), x in lst, lst.index(x) O(n) Use an index pointer or a deque for queues
x in set_or_dict, d[key], s.add(x) O(1) average Hash-based
sorted(lst), lst.sort() O(n log n) Timsort, stable
min(lst), max(lst), sum(lst) O(n) One pass
lst[a:b] (slice) O(b − a) Copies the slice
text += piece (inside a loop) O(n²) total Build a list and ''.join(...) instead
CS Algorithms Toolkit Complexity cheat sheets
9
