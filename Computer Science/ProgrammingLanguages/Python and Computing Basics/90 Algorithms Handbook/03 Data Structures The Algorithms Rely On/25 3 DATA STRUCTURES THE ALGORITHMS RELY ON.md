# 3 DATA STRUCTURES THE ALGORITHMS RELY ON

3 DATA STRUCTURES THE ALGORITHMS RELY ON
class MinHeap CLASS
Priority queue: always gives back the SMALLEST priority first.
REMEMBER A tree stored in a list: the children of index i live at 2i+1 and 2i+2. PUSH = add at the end and bubble up. POP
= move the last item to the top and sink it down.
WHEN TO USE "Give me the current best/cheapest/smallest" repeatedly: Dijkstra, Prim, Huffman, scheduling, top-k, event simulation.
AVOID WHEN Need to search arbitrary items or iterate in sorted order (a heap is only partially ordered).
REQUIRES Priorities must be mutually comparable.
TIME push O(log n), pop O(log n), peek O(1). SPACE O(n).
USED FOR OS task schedulers, A*/Dijkstra, merging k sorted streams.
NOTE (Python's built-in equivalent: heapq.)
INPUT heap = MinHeap()
heap.push(5, 'write report') # push(priority, item)
heap.push(1, 'fix bug')
heap.push(3, 'lunch')
[heap.pop(), heap.pop(), heap.pop()] # smallest priority always first
OUTPUT [(1, 'fix bug'), (3, 'lunch'), (5, 'write report')]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY heapq no install needed
heapq keeps a plain list arranged as a min-heap. Push tuples of (priority, item). When priorities can tie and the items cannot be compared,
add a counter as a tie-breaker. queue.PriorityQueue is the thread-safe wrapper.
CODE import heapq
heap = []
heapq.heappush(heap, (5, 'write report')) # (priority, item)
heapq.heappush(heap, (1, 'fix bug'))
heapq.heappush(heap, (3, 'lunch'))
[heapq.heappop(heap) for _ in range(3)]
OUTPUT [(1, 'fix bug'), (3, 'lunch'), (5, 'write report')]
CODE import heapq, itertools
tie_breaker = itertools.count()
heap = []
for priority, task in [(1, 'fix bug'), (1, 'lunch')]:
heapq.heappush(heap, (priority, next(tie_breaker), task)) # ties never compare tasks
heapq.heappop(heap)
OUTPUT (1, 0, 'fix bug')
CS Algorithms Toolkit Data structures the algorithms rely on
25
