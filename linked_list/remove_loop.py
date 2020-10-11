class ListNode:
	def __init__(self, x):
    	self.val = x
    	self.next = None

def removeLoop(head: ListNode) -> bool:
    # Initialize slow and fast to head node.
	slow = fast = head
	# Boolean to check if a loop exists in the given Linked List.
	flag = False

	# Traverse the Linked List.
	while fast and fast.next:
    	slow = slow.next
    	fast = fast.next.next

    	if slow == fast:
        	flag = True
        	break

    # When there is a loop in the Linked List.
	if flag:
    	# Assign head to slow.
    	slow = head
    	# Loop until next of slow and fast are not equal.
    	while slow.next != fast.next:
        	slow = slow.next
        	fast = fast.next
    	# Make next of fast i.e last node of Linked List None.
    	fast.next = None

	return head