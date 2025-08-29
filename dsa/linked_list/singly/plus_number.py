class Node:
    pass


def reverse(head):
    prev, curr = None, head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def addDigit(head, digit):
    head = reverse(head)
    curr = head

    carry = digit
    last = None

    while curr:
        curr.data += carry

        if curr.data >= 10:
            carry, rem = divmod(curr.data, 10)
            curr.data = rem

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
head2 = addDigit(head, digit)
