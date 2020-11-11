'''
155. Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, x):
        self.stack.append(x)
        
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            current_min = min(x, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]