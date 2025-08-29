'''
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
1. The valid operators are '+', '-', '*', and '/'.
2. Each operand may be an integer or another expression.
3. The division between two integers always truncates toward zero.
4. There will not be any division by zero.
5. The input represents a valid arithmetic expression in a reverse polish notation.
6. The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ['2','1','+','3','*']
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ['4','13','5','/','+']
Output: 6
Explanation: (4 + (13 / 5)) = 6
'''

import math

def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token in '+-/*':
            second, first = stack.pop(), stack.pop()

            match token:
                case '+':
                    stack.append(first + second)
                case '-':
                    stack.append(first - second)
                case '*':
                    stack.append(first * second)
                case '/':
                    division = first / second
                    if division < 0:
                        stack.append(math.ceil(division))
                    else:
                        stack.append(math.floor(division))
        else:
            stack.append(int(token))

    return stack.pop()
