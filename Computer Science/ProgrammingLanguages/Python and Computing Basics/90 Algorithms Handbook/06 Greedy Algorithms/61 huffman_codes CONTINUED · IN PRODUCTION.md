# huffman_codes CONTINUED · IN PRODUCTION

huffman_codes CONTINUED · IN PRODUCTION
STANDARD LIBRARY heapq + Counter recipe no install needed
If you do need the actual code table, this compact recipe is the usual approach: Counter for the frequencies, heapq for the merging.
CODE import heapq
from collections import Counter
frequencies = Counter('abracadabra')
heap = [[weight, [symbol, '']] for symbol, weight in frequencies.items()]
heapq.heapify(heap)
while len(heap) > 1:
lighter, heavier = heapq.heappop(heap), heapq.heappop(heap)
for pair in lighter[1:]:
pair[1] = '0' + pair[1]
for pair in heavier[1:]:
pair[1] = '1' + pair[1]
heapq.heappush(heap, [lighter[0] + heavier[0]] + lighter[1:] + heavier[1:])
sorted(heap[0][1:], key=lambda pair: (len(pair[1]), pair)) # [symbol, code], shortest first
OUTPUT [['a', '0'],
['r', '10'],
['b', '110'],
['c', '1110'],
['d', '1111']]
CS Algorithms Toolkit Greedy algorithms
61
