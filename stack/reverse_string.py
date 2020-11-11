from stack import Stack

def reverse(str):
    stack = Stack()

    for char in str:
        stack.append(char)

    _reversed = ''
    for _ in stack:
        _reversed += stack.pop()

    return _reversed

assert reverse('Hello') == 'olleh'

