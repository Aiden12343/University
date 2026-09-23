# linked_list_has_cycle

linked_list_has_cycle(head_node) FUNCTION
Return True if following next_node pointers ever loops back (Floyd).
REMEMBER Tortoise and hare: one pointer moves 1 step, the other 2; if there is a loop the hare eventually laps the
tortoise.
WHEN TO USE Detect loops without a visited-set.
TIME O(n). SPACE O(1).
USED FOR Corrupted-list detection, finding repeated states (e.g. PRNGs).
def linked_list_has_cycle(head_node):
tortoise_node = head_node
hare_node = head_node
while hare_node is not None and hare_node.next_node is not None:
tortoise_node = tortoise_node.next_node
hare_node = hare_node.next_node.next_node
if tortoise_node is hare_node:
return True
return False
INPUT last_node = ListNode(3)
head_node = ListNode(1, ListNode(2, last_node))
last_node.next_node = head_node # 3 points back to 1: a loop
(linked_list_has_cycle(head_node), linked_list_has_cycle(ListNode(1, ListNode(2))))
OUTPUT (True, False)
IN PRODUCTION No standard routine: Floyd's tortoise-and-hare is the production answer.
CS Algorithms Toolkit Array & linked-list techniques
78
