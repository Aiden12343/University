# _sift_down_max_heap

_sift_down_max_heap(items, root_index, heap_size) HELPER
Push items[root_index] down until neither child is bigger.
def _sift_down_max_heap(items, root_index, heap_size):
while True:
left_child_index = 2 * root_index + 1
right_child_index = left_child_index + 1
largest_index = root_index
if left_child_index < heap_size and items[left_child_index] > items[largest_index]:
largest_index = left_child_index
if right_child_index < heap_size and items[right_child_index] > items[largest_index]:
largest_index = right_child_index
if largest_index == root_index:
return
items[root_index], items[largest_index] = items[largest_index], items[root_index]
root_index = largest_index
INPUT items = [1, 9, 5] # root (1) is smaller than its children
_sift_down_max_heap(items, 0, len(items)) # in place
items
OUTPUT [9, 1, 5]
heap_sort(items) FUNCTION
Return a sorted copy using a max-heap built inside the list.
REMEMBER Turn the list into a max-heap (biggest on top), then keep swapping the top to the back of the list and
repairing the heap that remains in front.
WHEN TO USE Need O(n log n) worst-case AND O(1) extra memory.
AVOID WHEN Need stability; cache-sensitive workloads (slower than quick).
REQUIRES Items must be mutually comparable.
TIME O(n log n) always (building the heap alone is O(n)). SPACE O(1). NOT stable.
USED FOR Embedded systems, guaranteed-latency sorting, introsort fallback.
def heap_sort(items):
sorted_items = list(items)
item_count = len(sorted_items)
for parent_index in range(item_count // 2 - 1, -1, -1): # build the heap
_sift_down_max_heap(sorted_items, parent_index, item_count)
for end_index in range(item_count - 1, 0, -1): # extract maxima
sorted_items[0], sorted_items[end_index] = sorted_items[end_index], sorted_items[0]
_sift_down_max_heap(sorted_items, 0, end_index)
return sorted_items
INPUT heap_sort([5, 2, 9, 1, 5, 6])
OUTPUT [1, 2, 5, 5, 6, 9]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY heapq.heapify + heappop no install needed
The heap-sort idea, using the library heap. In practice you would call sorted(), or heapq.nsmallest / nlargest when you only need the top
few.
CODE import heapq
heap = [5, 2, 9, 1, 5, 6]
heapq.heapify(heap) # O(n), in place
[heapq.heappop(heap) for _ in range(len(heap))] # smallest first
OUTPUT [1, 2, 5, 5, 6, 9]
CS Algorithms Toolkit Sorting
21
