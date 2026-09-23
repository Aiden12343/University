# reverse_linked_list

reverse_linked_list(head_node) FUNCTION
Reverse a singly linked list in place; return the new head.
REMEMBER Walk down with three names — previous, current, next: save next, point current backwards at previous,
then step all three forward.
REQUIRES Singly linked list ending in None.
TIME O(n). SPACE O(1).
USED FOR Palindrome checks on lists, undo stacks, interview classic.
def reverse_linked_list(head_node):
previous_node = None
current_node = head_node
while current_node is not None:
following_node = current_node.next_node
current_node.next_node = previous_node
previous_node = current_node
current_node = following_node
return previous_node
INPUT head_node = ListNode(1, ListNode(2, ListNode(3))) # 1 -> 2 -> 3
new_head = reverse_linked_list(head_node)
[new_head.value, new_head.next_node.value, new_head.next_node.next_node.value]
OUTPUT [3, 2, 1]
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY collections.deque / list.reverse no install needed
Hand-built linked lists are rare in Python: production code uses a list or deque, which reverse in one call.
CODE from collections import deque
values = deque([1, 2, 3])
values.reverse()
list(values)
OUTPUT [3, 2, 1]
CS Algorithms Toolkit Array & linked-list techniques
77
