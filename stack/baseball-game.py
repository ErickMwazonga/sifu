'''
682. Baseball Game
https://leetcode.com/problems/baseball-game/description/

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

1. x - An integer x - Record a new score of x.
2. + - Record a new score that is the sum of the previous two scores.
3. D - Record a new score that is the double of the previous score.
4. C - Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

Example 1:
Input: ops = ['5','2','C','D','+']
Output: 30
Explanation:
'5' - Add 5 to the record, record is now [5].
'2' - Add 2 to the record, record is now [5, 2].
'C' - Invalidate and remove the previous score, record is now [5].
'D' - Add 2 * 5 = 10 to the record, record is now [5, 10].
'+' - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
'''

def calPoints(operations: list[str]) -> int:
    stack = []
    for operation in operations:
        if operation.lstrip('-').isdigit(): # isdigit doesn't work for negatives
            stack.append(int(operation))
        elif operation == '+':
            stack.append(stack[-1] + stack[-2])
        elif operation == 'D':
            stack.append(stack[-1] * 2)
        elif operation == 'C':
            stack.pop()
    
    return sum(stack)

def calPoints(operations: list[str]) -> int:
    stack = []
    for operation in operations:
        match operation:
            case op if op.lstrip('-').isdigit(): # isdigit doesn't work for negatives
                stack.append(int(op))
            case '+':
                stack.append(stack[-1] + stack[-2])
            case 'D':
                stack.append(stack[-1] * 2)
            case 'C':
                stack.pop()
            case _:
                continue
    
    return sum(stack)