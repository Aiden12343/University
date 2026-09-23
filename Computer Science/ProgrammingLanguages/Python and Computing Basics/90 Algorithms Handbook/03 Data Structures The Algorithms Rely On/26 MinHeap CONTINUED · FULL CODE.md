# MinHeap CONTINUED · FULL CODE

MinHeap CONTINUED · FULL CODE
class MinHeap:
def __init__(self):
self._entries = [] # each entry: (priority, order, item)
self._insertion_counter = 0 # tie-breaker so items are never compared
def __len__(self):
return len(self._entries)
def is_empty(self):
return len(self._entries) == 0
def peek(self):
"""Return (priority, item) of the smallest entry without removing it."""
priority, _, item = self._entries[0]
return priority, item
def push(self, priority, item):
self._entries.append((priority, self._insertion_counter, item))
self._insertion_counter += 1
self._bubble_up(len(self._entries) - 1)
def pop(self):
"""Remove and return (priority, item) with the smallest priority."""
top_entry = self._entries[0]
last_entry = self._entries.pop()
if self._entries:
self._entries[0] = last_entry
self._sink_down(0)
return top_entry[0], top_entry[2]
def _bubble_up(self, child_index):
while child_index > 0:
parent_index = (child_index - 1) // 2
if self._entries[child_index] < self._entries[parent_index]:
self._entries[child_index], self._entries[parent_index] = (
self._entries[parent_index], self._entries[child_index])
child_index = parent_index
else:
return
def _sink_down(self, parent_index):
entry_count = len(self._entries)
while True:
left_child_index = 2 * parent_index + 1
right_child_index = left_child_index + 1
smallest_index = parent_index
if left_child_index < entry_count and self._entries[left_child_index] <
↳ self._entries[smallest_index]:
smallest_index = left_child_index
if right_child_index < entry_count and self._entries[right_child_index] <
↳ self._entries[smallest_index]:
smallest_index = right_child_index
if smallest_index == parent_index:
return
self._entries[parent_index], self._entries[smallest_index] = (
self._entries[smallest_index], self._entries[parent_index])
parent_index = smallest_index
CS Algorithms Toolkit Data structures the algorithms rely on
26
