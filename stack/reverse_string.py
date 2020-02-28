from stack import Stack

def reverse(str):
    stack = Stack()
    reversed = ''

    for i in str:
        stack.append(i)
    
    for i in range(len(stack)):
        reversed = reversed + stack.pop()

    return reversed

print(reverse('Hello'))