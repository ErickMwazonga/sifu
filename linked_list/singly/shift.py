'''
Shift Linked List
Write a function that takes in the head of a Singly Linked List and an integer k, shifts the list in place
(i.e., doesn't create a brand new list) by k positions, and returns its new head.

Whether nodes are moved forward or backward is determined by whether k is positive or negative.
Each LinkedList node has an integer value as well as a next 
node pointing to the next node in the list or to None / null if it's the tail of the list.

head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0
k = 2
Sample Output
4 -> 5 -> 0 -> 1 -> 2 -> 3 // the new head node with value 4
'''

from index import Node, SinglyLinkedList as LinkedList


def getLength(head: Node):
    count = 1

    while head.next:
        head = head.next
        count += 1

    return count


def getTail(head: Node):
    tail = head

    while tail.next:
        tail = tail.next

    return tail


def shiftLinkedList(head: Node, k: int):
    length = getLength(head)
    tail = getTail(head)

    new_tail_idx = length - k - 1

    i = 0
    curr = head
    while i < new_tail_idx:
        curr = curr.next
        i += 1

    new_tail = curr
    new_head = curr.next

    new_tail.next = None
    tail.next = head

    head = new_head
    return head


llist = LinkedList()
llist.append(0)
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

llist.print_list()
head = llist.head

print('\n.....')
head = shiftLinkedList(head, 2)


while head:
    print(head.data, end="->")
    head = head.next
