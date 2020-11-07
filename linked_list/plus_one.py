"""
Number is represented in linked list such that each digit corresponds to a node in linked list. Add 1 to it.
For example 1999 is represented as (1-> 9-> 9 -> 9) and adding 1 to it should change it to (2->0->0->0)
Below are the steps :

1. Reverse given linked list. For example, 1-> 9-> 9 -> 9 is converted to 9-> 9 -> 9 ->1.
2. Start traversing linked list from leftmost node and add 1 to it. 
    If there is a carry, move to the next node. Keep moving to the next node while there is a carry.
3. Reverse modified linked list and return head.
"""
  
class Node:
    '''Linked list node'''
    def __init__(self,data): 
        self.data = data 
        self.next = None

def newNode(data):
    '''Function to create a new node with given data '''
    return Node(data) 

def printList(head): 
    if not head: 
        return
        
    while(head): 
        print("{}".format(head.data),end="") 
        head=head.next

def reverse(head):
    '''Function to reverse the linked list'''
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

def addOne(head): 
    """
    # Adds one to a linked lists and return the head  
    # node of resultant list 
    """
    # Reverse linked list  
    head = reverse(head)
    curr = head
    carry = 1

    while curr:
        curr.data += carry
        if curr.data % 10 == 0: 
            # update carry for next calulation  
            carry = 1
            curr.data = 0
        else: 
            # update carry for next calulation  
            carry = 0
        curr = curr.next
    
    # add a node at the end of linked list if there is any carry left
	if carry > 0:
		curr.next = Node(carry)

	# reverse the list again to restore the original order
	head = reverse(head)
	return head


if __name__ == '__main__': 
    head = newNode(9) 
    head.next = newNode(9) 
    head.next.next = newNode(9) 
    head.next.next.next = newNode(9)

    print("List is: ",end = "") 
    printList(head) 
  
    head = addOne(head) 
  
    print("\nResultant list is: ",end="") 
    printList(head) 
  