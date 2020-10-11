class Node:
    '''Linked list node'''
    def __init__(self,data): 
        self.data = data 
        self.next = None

def printList(msg, head):
    print(msg, end='')
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def reverse(head):
    if not head: 
        return

    curr = head
    prev = None
    next_node = None

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev # Return new head

def addOne(head, digit):
    head = reverse(head)

    curr = head
    carry = digit

    while curry > 0:
        # get sum of current node and carry
		_sum = curr.data + carry

		# update value of the current node with the single-digit sum
		curr.data = _sum % 10

		# set carry for the next node
		carry = _sum // 10

		# break if current node is the last node
		if curr.next is None:
			break

		# move to the next node
		curr = curr.next
    
    # add a node at the end of linked list if there is any carry left
	if carry > 0:
		curr.next = Node(carry)

	# reverse the list again to restore the original order
	head = reverse(head)
	return head


if __name__ == '__main__':

	head = Node(9)
	head.next = Node(9)
	head.next.next = Node(9)
	head.next.next.next = Node(9)
	head.next.next.next.next = Node(3)

	digit = 7

	printList(" Original Linked List: ", head)
	head = addDigit(head, digit)
	printList("Resultant Linked List: ", head)

# RESULT
# Original Linked List: 9 -> 9 -> 9 -> 9 -> 9 -> None
# Resultant Linked List: 1 -> 0 -> 0 -> 0 -> 0 -> 0 -> None