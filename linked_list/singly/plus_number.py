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

def addDigit(head, digit):
    head = reverse(head)
    curr = head
    carry = digit
    last = None

    while curr:
        curr.data += carry

        if curr.data >= 10:
            val, rem = divmod(curr.data, 10)
            carry = 1
            curr.data = rem
        else:
            carry = 0
            break

        if not curr.next:
            last = curr

        curr = curr.next

    # add a node at the end of linked list if there is any carry left
    if carry == 1:
        last.next = Node(1)

    # reverse the list again to restore the original order
    head = reverse(head)
    return head


head = Node(9)
head.next = Node(2)
head.next.next = Node(9)
head.next.next.next = Node(3)

digit = 7

printList(" Original Linked List: ", head)
head2 = addDigit(head, digit)
printList("Resultant Linked List: ", head2)

# RESULT
# Original Linked List: 9 -> 9 -> 9 -> 9 -> 9 -> None
# Resultant Linked List: 1 -> 0 -> 0 -> 0 -> 0 -> 0 -> None