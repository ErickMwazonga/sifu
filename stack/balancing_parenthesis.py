'''
Given a string expression which consists only ‘}’ and ‘{‘.
The expression may not be balanced. You need to find the minimum
number of bracket reversals which are required to
make the expression balanced.
Return -1 if the given expression can't be balanced.

{{{ -> -1
{{{{}} -> 1
'''

def minimum_reversals(s: str) -> int:
    stack = []
    for ch in s:
        if ch == '{':
            stack.append(ch)
        else:
            if not len(stack) or stack[-1] == '}':
                stack.append(ch)
            elif stack[-1] == '{':
                stack.pop()

    # now the stack contains only unbalanced parenthesis
    split = 0
    n = len(stack)
    if not n:
        retun 0 # Already Balanced
    if n % 2 ! == 0:
        return -1 # Cannot be balanced
    
    while(n and stack[-1] != '}'):
        stack.pop()
        split += 1
  
    return ceil((n-split)/2) + ceil(split/2) 