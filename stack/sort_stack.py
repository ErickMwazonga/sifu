'''
SORT STACK
https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/
Sort a stack using a temporary stack
Given a stack of integers, sort it in ascending order using another temporary stack.
Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]
'''

from stack import Stack


class SortedStack:
    def __init__(self, nums):
        self.stack = Stack()
        self.temp_stack = Stack()

        for num in nums:
            self.stack.append(num)

    def sort(self):
        while not self.stack.isEmpty():
            # pop out the first element
            popped = self.stack.pop()

            # while temporary stack is not
            # empty and top of stack is greater than temp
            while not self.temp_stack.isEmpty() and popped < self.temp_stack.peek():
                # pop from temporary stack and
                # push it to the input stack
                popped_from_temp = self.temp_stack.pop()
                self.stack.append(popped_from_temp)

            # push temp in tempory of stack
            self.temp_stack.append(popped)

        return self.temp_stack


ss = SortedStack([34, 3, 31, 98, 92, 23])
print(ss.stack.show())
ss.sort()
print(ss.temp_stack.show())
