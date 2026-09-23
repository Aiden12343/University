# two_sum_hash_map

10 ARRAY & LINKED-LIST TECHNIQUES
two_sum_hash_map(numbers, target_sum) FUNCTION
Return indices (a, b) of two numbers adding to target_sum, or None.
REMEMBER For each number, ask the dictionary "have I already seen target - number?"; if not, record this number and
its index.
WHEN TO USE UNSORTED data, one pass, need original indices.
AVOID WHEN Memory-critical + already sorted (use two pointers, O(1) space).
REQUIRES Nothing.
TIME O(n). SPACE O(n).
USED FOR Pair matching, complements problems.
def two_sum_hash_map(numbers, target_sum):
index_of_value_seen = {}
for index, number in enumerate(numbers):
needed_number = target_sum - number
if needed_number in index_of_value_seen:
return index_of_value_seen[needed_number], index
index_of_value_seen[number] = index
return None
INPUT numbers = [2, 7, 11, 15] # need NOT be sorted
two_sum_hash_map(numbers, 9) # indices of 2 and 7
OUTPUT (0, 1)
IN PRODUCTION The dict IS the standard tool: this is already the production form.
two_sum_sorted_two_pointers(sorted_numbers, target_sum) FUNCTION
Return indices (low, high) of two numbers adding to target_sum, or None.
REMEMBER One pointer at each end: sum too small → move the left pointer up; sum too big → move the right pointer
down.
WHEN TO USE Sorted data, O(1) extra space. Same pattern: 3-sum, container with most water, removing duplicates.
REQUIRES sorted_numbers MUST be sorted ascending.
TIME O(n). SPACE O(1).
def two_sum_sorted_two_pointers(sorted_numbers, target_sum):
low_index = 0
high_index = len(sorted_numbers) - 1
while low_index < high_index:
current_sum = sorted_numbers[low_index] + sorted_numbers[high_index]
if current_sum == target_sum:
return low_index, high_index
if current_sum < target_sum:
low_index += 1
else:
high_index -= 1
return None
INPUT sorted_numbers = [2, 7, 11, 15] # MUST be sorted
two_sum_sorted_two_pointers(sorted_numbers, 26)
OUTPUT (2, 3)
IN PRODUCTION No library: two pointers on sorted data is the production solution.
CS Algorithms Toolkit Array & linked-list techniques
73
