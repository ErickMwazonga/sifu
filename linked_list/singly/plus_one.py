'''
Link: https://leetcode.com/problems/plus-one-linked-list/

Number is represented in linked list such that each digit corresponds to a node in linked list. Add 1 to it.
For example 1999 is represented as (1-> 9-> 9 -> 9) and adding 1 to it should change it to (2->0->0->0)
Below are the steps :

1. Reverse given linked list. For example, 1-> 9-> 9 -> 9 is converted to 9-> 9 -> 9 ->1.
2. Start traversing linked list from leftmost node and add 1 to it. 
    If there is a carry, move to the next node. Keep moving to the next node while there is a carry.
3. Reverse modified linked list and return head.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if not head:
        return

    while(head):
        print('{}'.format(head.data), end='')
        head = head.next


def reverse(head):
    prev, curr = None, head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def addOne(head):
    head = reverse(head)
    curr = last = head

    carry = 1

    while curr:
        curr.data += carry

        carry, rem = divmod(curr.data, 10)
        curr.data = rem

        if not curr.next:
            last = curr

        curr = curr.next

    if carry == 1:
        last.next = Node(carry)

    head = reverse(head)
    return head


if __name__ == '__main__':
    head = Node(9)
    head.next = Node(9)
    head.next.next = Node(9)
    head.next.next.next = Node(9)

    print('List is: ', end='')
    printList(head)

    head = addOne(head)

    print('\nResultant list is: ', end='')
    printList(head)
