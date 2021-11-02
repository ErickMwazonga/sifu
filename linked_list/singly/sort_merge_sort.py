'''
Time complexity: O(nlogn)
Space complexity: O(logn)
'''


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def mergeSortedLists(head1, head2):
        ptr1 = head1
        ptr2 = head2

        returnedHead = None
        tail = None

        while ptr1 or ptr2:
            if ptr1 and ptr2:
                if ptr1.data < ptr2.data:
                    lower = ptr1
                    ptr1 = ptr1.next
                else:
                    lower = ptr2
                    ptr2 = ptr2.next
            elif ptr1:
                lower = ptr1
                ptr1 = ptr1.next
            else:
                lower = ptr2
                ptr2 = ptr2.next

            if returnedHead is None:
                returnedHead = lower
                tail = lower
            else:
                tail.next = lower
                tail = tail.next

        return returnedHead

    def mergeSort(head):
        if head is None or head.next is None:
            return head

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        headRightHalf = slow.next
        slow.next = None

        head = mergeSort(head)
        headRightHalf = mergeSort(headRightHalf)

        return mergeSortedLists(head, headRightHalf)


def sortList(list):
    list.head = mergeSort(list.head)
