# huffman_codes

huffman_codes(symbol_frequencies) FUNCTION
Return {symbol: bit-string} giving an optimal prefix-free code.
REMEMBER Put every symbol in a min-heap by frequency; repeatedly merge the two RAREST into one node (frequencies
add); when one tree remains, left edge = "0", right edge = "1".
WHEN TO USE Lossless compression where symbol frequencies differ a lot.
AVOID WHEN Roughly uniform frequencies (little gain); streaming data with unknown frequencies (use adaptive Huffman).
REQUIRES Dict of symbol → positive count.
TIME O(k log k) for k distinct symbols. SPACE O(k).
USED FOR ZIP/DEFLATE, JPEG, MP3 entropy-coding stages.
def huffman_codes(symbol_frequencies):
if not symbol_frequencies:
return {}
if len(symbol_frequencies) == 1:
return {next(iter(symbol_frequencies)): "0"}
priority_queue = MinHeap()
for symbol, frequency in symbol_frequencies.items():
priority_queue.push(frequency, symbol) # leaf = the symbol
while len(priority_queue) > 1:
rarest_frequency, rarest_tree = priority_queue.pop()
second_rarest_frequency, second_rarest_tree = priority_queue.pop()
priority_queue.push(rarest_frequency + second_rarest_frequency,
(rarest_tree, second_rarest_tree)) # internal = tuple
_total_frequency, root_tree = priority_queue.pop()
code_for_symbol = {}
stack = [(root_tree, "")]
while stack:
tree, code_so_far = stack.pop()
if isinstance(tree, tuple):
left_subtree, right_subtree = tree
stack.append((left_subtree, code_so_far + "0"))
stack.append((right_subtree, code_so_far + "1"))
else:
code_for_symbol[tree] = code_so_far
return code_for_symbol
INPUT symbol_frequencies = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}
huffman_codes(symbol_frequencies) # frequent symbols get short codes
OUTPUT {'d': '111',
'e': '1101',
'f': '1100',
'b': '101',
'c': '100',
'a': '0'}
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY zlib (real compression) no install needed
Nobody ships hand-rolled Huffman coding: zlib/gzip use DEFLATE, which combines LZ77 with Huffman codes and is built into Python. bz2
and lzma are the other standard choices.
CODE import zlib
message = b'abracadabra' * 20
compressed = zlib.compress(message)
(len(message), len(compressed), zlib.decompress(compressed) == message)
OUTPUT (220, 21, True)
CS Algorithms Toolkit Greedy algorithms
60
