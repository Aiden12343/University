# build_prefix_sums

build_prefix_sums(numbers) FUNCTION
Return running totals with a leading 0: prefix[k] = sum of first k items.
REMEMBER Store a running total once; any range sum is "total up to the end minus total before the start".
WHEN TO USE MANY range-sum queries on data that does not change.
AVOID WHEN Data that changes often (use a Fenwick / segment tree).
TIME O(n) to build, O(1) per query afterwards. SPACE O(n).
def build_prefix_sums(numbers):
prefix_sums = [0]
for number in numbers:
prefix_sums.append(prefix_sums[-1] + number)
return prefix_sums
INPUT build_prefix_sums([3, 1, 4, 1, 5, 9])
OUTPUT [0, 3, 4, 8, 9, 14, 23]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY itertools.accumulate no install needed
accumulate is the library running total; initial=0 gives the leading zero. numpy.cumsum is the array equivalent.
CODE from itertools import accumulate
list(accumulate([3, 1, 4, 1, 5, 9], initial=0))
OUTPUT [0, 3, 4, 8, 9, 14, 23]
range_sum(prefix_sums, start_index, end_index_exclusive) FUNCTION
Sum of numbers[start_index : end_index_exclusive] in O(1).
def range_sum(prefix_sums, start_index, end_index_exclusive):
return prefix_sums[end_index_exclusive] - prefix_sums[start_index]
INPUT prefix_sums = build_prefix_sums([3, 1, 4, 1, 5, 9])
range_sum(prefix_sums, 1, 4) # numbers[1:4] = 1 + 4 + 1
OUTPUT 6
IN PRODUCTION Same as the production variant of build_prefix_sums.
class ListNode CLASS
One node of a singly linked list.
class ListNode:
def __init__(self, value, next_node=None):
self.value = value
self.next_node = next_node
INPUT node = ListNode(1, ListNode(2)) # 1 -> 2 -> None
(node.value, node.next_node.value, node.next_node.next_node)
OUTPUT (1, 2, None)
IN PRODUCTION Hand-built linked lists are rare in Python; lists and collections.deque are used instead.
CS Algorithms Toolkit Array & linked-list techniques
76
