# merge_two_sorted_lists

merge_two_sorted_lists(left_list, right_list) FUNCTION
Return one sorted list from two already-sorted lists.
REMEMBER Two queues of people sorted by height: repeatedly let the shorter front person through; when one queue
empties, append the rest of the other.
WHEN TO USE Combining sorted data, external sorting, merge sort's core.
REQUIRES BOTH inputs MUST already be sorted ascending.
TIME O(n + m). SPACE O(n + m).
USED FOR Merge sort, merging database runs, k-way merge of log files.
def merge_two_sorted_lists(left_list, right_list):
merged_items = []
left_index = 0
right_index = 0
while left_index < len(left_list) and right_index < len(right_list):
if left_list[left_index] <= right_list[right_index]: # <= keeps STABLE
merged_items.append(left_list[left_index])
left_index += 1
else:
merged_items.append(right_list[right_index])
right_index += 1
merged_items.extend(left_list[left_index:])
merged_items.extend(right_list[right_index:])
return merged_items
INPUT left_list = [1, 4, 9] # both MUST be sorted
right_list = [2, 3, 10]
merge_two_sorted_lists(left_list, right_list)
OUTPUT [1, 2, 3, 4, 9, 10]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY heapq.merge no install needed
heapq.merge merges any number of already-sorted inputs lazily (it is a generator), so it also works on files or streams too big for memory.
CODE import heapq
list(heapq.merge([1, 4, 9], [2, 3, 10])) # inputs MUST already be sorted
OUTPUT [1, 2, 3, 4, 9, 10]
CS Algorithms Toolkit Sorting
18
