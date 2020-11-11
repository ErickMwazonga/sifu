def reverse(_str):
    stack = []

    for char in _str:
        stack.append(char)

    _reversed = ''
    for _ in stack:
        _reversed += stack.pop()

    return _reversed

assert reverse('Hello') == 'olleh'

