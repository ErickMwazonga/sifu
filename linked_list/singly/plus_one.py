'''
904 · Plus One Linked List
Link: https://leetcode.com/problems/plus-one-linked-list/
Link 2: https://www.lintcode.com/problem/904/

Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example 1
    Input: 1 -> 2 -> 3 -> null
    Output: 1 -> 2 -> 4 -> null
    Explanation: 123 + 1 = 124

Example 2
    Input: 9 -> 9 -> null
    Output: 1 -> 0 -> 0 -> null
    Explanation: 99 + 1 = 100
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def printList(head):
        if not head:
            return

        while head:
            print(head.data, end='')
            head = head.next


    def reverse(self, head):
        prev, curr = None, head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
    
    def plus_one(self, head):
        '''
        TIME: O(N), SPACE: O(N)
        INTUITION: Convert to list, add 1 then convert back to linked list.
        '''

        # convert the linked list to a list
        numbers = []
        while head:
            numbers.append(head.data)
            head = head.next

        # perform the addition
        carry = 1
        for i in range(len(numbers)-1, -1, -1):
            numbers[i] += carry
            carry, numbers[i] = divmod(numbers[i], 10)

        # create a new linked list from the digits
        new_head = Node(0)
        curr = new_head
        for digit in numbers:
            curr.next = Node(digit)
            curr = curr.next

        return new_head


    def plus_one_v2(self, head):
        '''
        TIME: O(N), SPACE: O(1)
        INTUITION: Reverse, add 1 as you iterate through the linked list, then reverse
        '''
         
        head = self.reverse(head)
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

        head = self.reverse(head)
        return head


if __name__ == '__main__':
    head = Node(9)
    head.next = Node(9)
    head.next.next = Node(9)
    head.next.next.next = Node(9)

    soln = Solution()
    print('List is: ', end='')
    soln.printList(head)

    head = soln.plus_one_v2(head)

    print('\nResultant list is: ', end='')
    soln.printList(head)
